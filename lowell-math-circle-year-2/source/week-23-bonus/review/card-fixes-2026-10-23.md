# Week 23 bonus: fix from the base week's review card, October 23, 2026

The review card for Week 23 (`plans/review/week-23.md` in the project) noticed this companion without reviewing it and said, under should 3, that it repeats the base packets' rule wording "sends the smaller value to the lower-numbered lane", where "lower" reads as lower on the page. The student packet is now W23-BON-v2 and its guide W23-BON-FAC-v2.

- **Student p. 1, the shared rule.** "sends the smaller value to the lower-numbered lane" is now "sends the smaller value to the upper lane", as in the base packets' new grades 2–5 rule.
- **Guide p. 1, Selection.** The same phrase in the adult summary now reads "send the smaller value to the upper lane".

No other wording changed: against the v1 references, every other page differs only in the footer's version. No problem, diagram or answer changed.

## Verification

- `math/independent-check.py` still compares `student-src/bonus.tex` with the historical reviewed draft in `math/fixtures/`, now after applying the earlier substitution and exactly these two v2 substitutions (the rule and the footer), and passes; `student-src/writer-check.py` passes. Their outputs are generated; `review/checks.json` and `review/guide-checks.json` remain the October 4 audit, and `release-validation.json` records the original release.
- The base package's `review/verify_card_fixes_2026_10_23.py`, given this package's build folder, checks the new rule and both footers in the PDFs.
- `verify_rebuild.py` passes against the new `reference-pdfs/`; a clean rebuild from the extracted source ZIP passes it.
- The v1 PDFs are archived in the project in `week-23/archive-before-card-shoulds-2026-10-23/`, and the v1 source ZIP in `source/week-23/archive-before-card-shoulds-2026-10-23/`.

The companion remains unpiloted.
