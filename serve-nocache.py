"""Local test server for the Round Card that NEVER lets the browser cache anything.

Why this exists: `python -m http.server` sends ETag/Last-Modified, so Chrome happily serves a
stale redirect.html even with DevTools "Disable cache" ticked. On 2026-07-27 that cost hours -
the sign-in kept failing against a cached copy of a file that had already been fixed on disk,
and every diagnostic pointed somewhere else because the served file and the running file were
different things.

    python serve-nocache.py            # port 8080
    python serve-nocache.py 8123       # another port (must match the Entra redirect URI)

Then open  http://localhost:8080/Round-Card.html?sandbox=1

Serves the current directory only. Local testing tool - never expose it.
"""
import sys
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer


class NoCacheHandler(SimpleHTTPRequestHandler):
    def send_head(self):
        # THE ONE THAT ACTUALLY MATTERED. SimpleHTTPRequestHandler honours a conditional request
        # and answers 304 Not Modified *before* any response header of ours is involved - so the
        # browser keeps its stale copy no matter what Cache-Control we later add. Stripping the
        # response validators was not enough; the browser had already cached them from earlier
        # requests and kept sending them back. Drop the conditions and every request is a real
        # 200 with real bytes. (Caught 2026-07-27 by this server's own request log showing
        # "GET /redirect.html HTTP/1.1" 304.)
        for header in ("If-Modified-Since", "If-None-Match"):
            while header in self.headers:
                del self.headers[header]
        return super().send_head()

    def end_headers(self):
        # Belt and braces: no-store defeats the memory cache, and blanking the validators stops
        # Chrome revalidating its way back to a stale copy.
        self.send_header("Cache-Control", "no-store, no-cache, must-revalidate, max-age=0")
        self.send_header("Pragma", "no-cache")
        self.send_header("Expires", "0")
        super().end_headers()

    def send_header(self, keyword, value):
        if keyword.lower() in ("etag", "last-modified"):
            return
        super().send_header(keyword, value)

    def log_message(self, fmt, *args):
        # One readable line per request, so you can SEE whether redirect.html was fetched.
        sys.stderr.write("  %s\n" % (fmt % args))


if __name__ == "__main__":
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 8080
    print("Round Card test server on http://localhost:%d  (no caching)" % port)
    print("  open  http://localhost:%d/Round-Card.html?sandbox=1" % port)
    print("  stop  Ctrl-C\n")
    ThreadingHTTPServer(("127.0.0.1", port), NoCacheHandler).serve_forever()
