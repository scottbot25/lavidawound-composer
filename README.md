# LaVida Provider Tools

Two self-contained, browser-based tools for wound care. Same privacy posture (below), same
no-install, no-new-hardware approach.

## 1. Wound Note Composer

Turns LaVida's PointClickCare (PCC) wound-care global macros into a fill-in form and rebuilds each
note section for paste-back into PCC. It also generates a facility handoff from the same data.

**Open it:** <https://notes.lavidaheal.com/>

## 2. Round Card *(new — Phase 1)*

The **orders** tool, for the bedside. It solves a different problem: facility nurses are measured on
how fast orders land, but today orders don't exist until charting is finished, hours after rounds.
The Round Card produces the nurse's orders **before the provider leaves the building**.

Per wound, exactly the six things the nurses asked for — location · type · size · stage (only if
pressure) · drainage · orders. At the end of the round you review the sheet, then email it to an
approved facility contact or print it.

It **does not replace the facility handoff** — it's deliberately the nurses' short list, sent early.
The full handoff still comes from the Composer during charting.

**Open it:** <https://notes.lavidaheal.com/round-card.html>

Phone-first. Typing today; hold-to-talk dictation is Phase 2.

## Privacy / PHI posture

The pages themselves are **blank templates** — no patient data is baked into either file, and none
is stored in this repository.

**Once you sign in, what you type IS saved to ClinicalVault.** That is what signing in is for, and
ClinicalVault is the practice's own Microsoft 365 tenant, which is covered by a BAA. Specifically:

- **Round records** → `RoundCards/<facility>/`, one JSON per patient, kept about 45 days.
- **Your working draft** → `Drafts/<you>/<date>.json`, a folder only you can see.
- **The nurse's handoff sheet** → `Daily Handoffs/<facility>/<date>/`.
- **A count of patients seen** → `QC Feed/`. Counts only, no names.

Signed **out**, nothing leaves the device: the round lives in `sessionStorage` and goes when you
close the tab.

- Nothing is sent to the host that serves these pages. No third-party scripts, fonts, analytics or
  CDNs — the Microsoft sign-in library is served from this repo, not from a CDN.
- One value persists on the device between sessions: `rc_last_prov`, the provider name the round
  card puts back in the box for you. No patient data is kept outside the tab.
- All vault traffic goes to Microsoft Graph, and only after **you** have signed in.

Use an encrypted work device.

> **Corrected 2026-07-28.** This section used to say the tool ran "100% in your browser", that
> entries were "never written to disk, never networked", and that the only external calls were
> sign-in and an email. None of that had been true since the vault integration shipped. Noted here
> rather than quietly rewritten, because someone may have relied on it.

## Status

Both are in daily provider use. The Microsoft Entra sign-in gate is **live** — the tenant and client
IDs in these files are the real registered app, not placeholders, and signing in is what connects the
tools to ClinicalVault.

Facility email contacts in both tools are **test placeholders** pointing at an internal admin inbox,
so testing cannot email a real facility. The real approved contacts live in the private ops vault,
never in this repo.
