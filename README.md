# LaVida Wound Note Composer

A self-contained, browser-based tool that turns LaVida's PointClickCare (PCC) wound-care
global macros into a fill-in form and rebuilds each note section for paste-back into PCC.
It also generates a facility handoff from the same data.

**Open it:** <https://scottbot25.github.io/lavidawound-composer/>

## Privacy / PHI posture

This page is a **blank template** — it contains no patient data.

- Runs **100% in your browser**. Nothing you type is sent to this host or anywhere else.
- Entries are held in `sessionStorage` (this browser tab only) and are **wiped when you close the tab** —
  never written to disk, never networked.
- No third-party scripts, fonts, analytics, or CDNs.
- The only optional external calls are Microsoft sign-in / the facility handoff email, and both are
  actions **you** initiate from your own device.

Please still use an encrypted work device.

## Status

Prototype in provider testing. The Microsoft Entra sign-in gate is built in but **off by default**
(tenant/client IDs are placeholders) until the tenant app is registered.
