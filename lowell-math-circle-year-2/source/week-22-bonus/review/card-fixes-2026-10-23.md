# Week 22 bonus: fix from the base week's review card, October 23, 2026

The review card for Week 22 (`plans/review/week-22.md` in the project, with its math check `week-22-math.md`) read this companion only for its math check item 1 and listed one should for it. The student packet is now W22-BON-v2 and its guide W22-BON-FAC-v2.

- **Should 4, student p. 1, Problem 1.** T was at (4, 3.2), 1.3 mm from segment BE on the printed board, so a ruled BE grazed T's ring and two dots looked enough. T is now at (3.2, 3.4), at least 12.9 mm from every joining segment (closest CF, then BE at 12.95 mm), and inside the same eight triangles (ABE, ACE, ADE, ADF, BDF, BEF, CDF, CEF), so the answer is unchanged: three dots, any of those eight. The label sits beside it at (3.32, 3.4).
- **Guide p. 2, Problem 1-2.** The adult coordinates read T=(16/5,17/5), and the containment certificate is now "BEF contains T: T=(2/5)B+(2/5)E+(1/5)F" (it was CEF with weights 11/25, 4/25, 2/5, which no longer give the new T).

No other page changed: against a rebuild of v1 in this container, student pages 2-5 and guide pages 1 and 3-5 differ only in the footer's version.

## Verification

- `python3 review/verify_card_fix_2026_10_23.py [folder]` checks the printed T, its distance from all fifteen segments at the board's 16.25 mm scale, the eight containing triangles, the new weights, both footers and the guide's sentence.
- `math/independent-check.py`, `guide-src/guide-independent-check.py` and `student-src/writer-check.py` now use the new T (and the guide check the BEF weights) and pass. The first still compares `student-src/bonus.tex` with the historical reviewed draft in `math/fixtures/`, after applying exactly the two v2 substitutions (T's position and the footer). Their outputs are generated; `review/checks.json` and `review/guide-checks.json` remain the October 4 audit, as do the review notes (`answer-notes.md` and the audits still give the old T), and `release-validation.json` records the original release.
- `verify_rebuild.py` passes against the new `reference-pdfs/`; a clean rebuild from the extracted source ZIP passes it and the card-fix verifier.
- The v1 PDFs are archived in the project in `week-22/archive-before-card-fixes-2026-10-23/`, and the v1 source ZIP in `source/week-22/archive-before-card-fixes-2026-10-23/`.

The companion remains unpiloted.
