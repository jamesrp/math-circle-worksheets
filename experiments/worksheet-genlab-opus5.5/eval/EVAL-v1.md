# EVAL-v1 (FROZEN 2026-09-30 ~22:10 PT, before any wave-1 result was judged)

Nothing below may change for the rest of the experiment unless a clear bug is found, in which case the whole eval is re-run under a new version.

## Frozen artifacts (sha256, first 12 hex)
- eval/prompts/AUDIT.md          6341fad331c8
- eval/prompts/PAIR.md           66560815dbaa
- eval/prompts/judge-standard.md 7ce602d2f1ac  (James's AGENTS.md student-page/design guidance, condensed, + his three stated complaints)
- tools/bundle.py                b97f93cb0b76  (110 dpi PNG per page + pdftotext -layout per band; blinded PIDs)
- tools/lint.py                  c667d6b1046b
- tools/make_job.py              06d4de9408a3
- Judge model: Opus (general-purpose subagent, fresh context per job). Agent prompt: "You are a judge in an evaluation. Your complete instructions are in <JOB.md>. Read that file and follow it exactly. Read only the files it names."

## Instruments
1. LINT (deterministic): surface tells per packet (descriptive).
2. AUDIT x2 per packet (independent fresh judges): itemized edit list (category, minutes 1/3/10/30), est. minutes of work for quick/typical child per band, eight 0–5 dimension scores per band.
3. PAIR (both orders): which packet the organizer should take, per band and overall.

## Pre-registered metrics (chosen from validation data only)
- PRIMARY: AQI = mean of the eight 0–5 audit dimension scores over the three bands, averaged over the two audits.
  Validation: replicate reliability ICC 0.98 (6 packets x 2 audits); ranks GOLD-A 3.40 > VAR-SLOP-A 3.25 > VAR-THIN-A 2.90 (both seeded degradations detected).
- Holistic: pairwise preference (both orders; inconsistent orders = tie).
  Validation: GOLD-A beat VAR-SLOP-A and VAR-THIN-A on every band in both orders; 4/4 validation pairs order-consistent overall.
- Secondary profile (always reported):
  - Voice: human_voice score (ICC 0.94), number of SLOP edits (ICC 0.98), lint tells per 100 words.
  - Substance: math_substance (0.95), level_fit (0.98), volume (0.96), quick-child minutes per band, concreteness, clarity.
  - Correctness: number and minutes of MATH edits.
  - Edit minutes (organizer time). Demoted from primary: ICC only 0.75 because 30-minute VOLUME edits are coarse, and it barely separated VAR-SLOP-A from GOLD-A (+7.5 min; slop edits are logged at 1 minute each).
- Seeded-slop recall: 14/14 injected items logged by both audits.

## Validation observations worth remembering
- The judge rated the naive A0-A packet above the human-edited GOLD-A, both by AQI (3.60 vs 3.40) and pairwise (won 2/2 orders, losing only the 2–3 band). Its stated reason: A0's slop is "removable clutter", while GOLD-A's K–1 is thin (est. 19 min of work for a quick child) and its 4–5 page 2 shows all six tilings right after asking children to find them. This is a substantive judgment, not position bias. Whether James agrees is the main question for the human blind ranking.
- The judge is harsh in absolute terms (GOLD-A readiness 2.5/5, ~180 edit minutes). Use scores relatively.
