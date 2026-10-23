# Week 34 revision verification

Revised all three five-page packets. Category-only matching is explicit, all spots must align, and the first motion uses filled/hollow circles so the depicted action is physically faithful. K–1 square edits compare both surviving and destroyed asymmetry; eight-ring designs must be genuinely different and recorded separately. The upper six-ring explanation no longer dictates avoiding physical overlay checks. Independent geometric-map enumeration verifies finite cases through size 10. All 15 pages were rendered and inspected. No classroom trial is claimed.

Run `bash build.sh` with Python 3, pdfLaTeX/TikZ and Poppler. The build regenerates source, runs both the existing and independent checks, compiles twice, and renders every page. The source uses no machine-specific runtime paths. A fixed default SOURCE_DATE_EPOCH is included for reproducible metadata. These are student PDFs and source/QA records, not an adult guide.

October 23, 2026: the build now writes the source from the problem files (`regenerate.py`) and runs the old builder's finite checks as `check_distinguishing.py`; the LaTeX is byte-identical.

October 23, 2026, card fixes (v3): the example adds a flip panel with its axis, every goal reads "a pattern that no turn or flip can match", the rules say "neighbors may be the same kind", and Grades 4-5 get a sixth page of extra workspace (seven- and nine-rings). Checked by `plans/review/checks/week-34/check_card_fixes.py` in the project.
