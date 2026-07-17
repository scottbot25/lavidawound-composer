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

This page is a **blank template** — it contains no patient data.

- Runs **100% in your browser**. Nothing you type is sent to this host or anywhere else.
- Entries are held in `sessionStorage` (this browser tab only) and are **wiped when you close the tab** —
  never written to disk, never networked.
- No third-party scripts, fonts, analytics, or CDNs.
- The only optional external calls are Microsoft sign-in / the facility handoff email, and both are
  actions **you** initiate from your own device.

Please still use an encrypted work device.

## Status

Both are prototypes in provider testing. The Microsoft Entra sign-in gate is built into the Composer
but **off by default** (tenant/client IDs are placeholders) until the tenant app is registered.

Facility email contacts in both tools are **test placeholders** pointing at an internal admin inbox,
so testing cannot email a real facility. The real approved contacts live in the private ops vault,
never in this repo.
