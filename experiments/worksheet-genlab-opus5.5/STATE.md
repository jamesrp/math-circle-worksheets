# STATE (checkpoint file — read this first when resuming)

Experiment: AI worksheet-generation workflows, scored by a frozen AI eval. Owner: James. Orchestrator: Claude (Cowork, Opus 5.5).
Canonical copy: ~/math-circle/experiments/worksheet-genlab-opus5.5/ (synced from cloud workspace /home/claude/genlab after each checkpoint).

## Decisions from James (2026-09-30)
- Inputs: outline A = Week 1 tiling (anchors: GOLD-A = current human-edited week-01; ASTRA-A = archive-v1 pre-edit AI); outline B = Week 7 take-away games (anchor: ASTRA-B = current unreviewed AI packet).
- Each run produces 3 student PDFs (K–1, 2–3, 4–5), no facilitator guide.
- James will do a ~30 min blind ranking at the end.
- Models: Opus for all agents (Fable hit its usage limit on first probe, 2026-09-30).
- Up to 10 generation approaches.

## Phase plan
- [x] P0 Research (R1 sources, R2 web) -> research/
- [x] P0 Inputs, harness, arm prompt blocks, eval prompts, tools
- [x] P1 Vertical slice: A0 x A generation; pilot audit on GOLD-A; fix bugs
- [x] P1 Judge validation: audits on anchors + seeded variants (VAR-SLOP-A, VAR-THIN-A); pairs GOLD vs variants; then FREEZE eval (EVAL-v1)
- [x] P2 Wave 1: single-agent arms A0-A3 x outlines A,B (8 runs) + eval
- [x] P3 Wave 2: B1-B5 (critic/reviser variants on shared A3 drafts; plan-first) + eval
- [x] P4 Wave 3: C1 triple-critic (r1 reuse + r2 fresh), A3 replicate r2, B1 on r2, anchors + eval
- [x] P5 Analysis (analysis/), human blind-review pack (human-review/), REPORT.md
- [x] P6 James's blind ranking received 2026-10-01 (X = Y > W > Z); agreement scored in analysis/human-review.json and NOTES.md; key released

## Current status
See bottom of NOTES.md for the latest log entry. Runs live in runs/<ARM>-<OUTLINE>-r<k>/, eval outputs in eval/results/<PID>/, blinding map in eval/private/blind-map.json.
