# Week 31 Hidden orchard editable source

## Current release: October 23, 2026 card fixes (guide, then v3 student packets)

The adult guide carries the corrections from its review card: the optional extension's moved-viewer example is corrected (p. 4), and the launch shows the recording marks with timing for 35–40 minutes at the tables (p. 2). Later the same day, after the problem-file conversion below, the review card's student-page items were made as v3 packets: Grades 4–5 reorders Problems 3–5 (rule, ray groups, then the common-factor question), rewords Problems 1 and 6 and adds a 0–25 by 0–15 grid to Problem 3; K–1 Problems 4 and 5 and Grades 2–3 Problem 6 are reworded; the "(4, 2)" label sits beside its ring; and the p. 1 captions clear the axis numerals. See `review/card-fixes-2026-10-23.md`.

**Problem files, October 23, 2026.** The student pages are now stored as problem files in `problem-files/` (in the repository: `lowell-math-circle-year-2/source/week-31/`), one file per problem with its band differences inside it. The conversion changed no wording or figure; the PDFs were unchanged until the student-page fixes above. `student-src/regenerate.py` writes the student LaTeX from them and compiles it, and `problem-files/tools/build.py` also builds first-route and return packets, a one-page problem menu and a key arranged by problem.

The October 4 revision gave the guide first routes, readiness-dependent continuation and return visits; original mathematical investigations are retained.

This is an unpiloted theme library, not a fixed meeting schedule. Select a manageable first route in the guide and return for further investigations. Preserve the full Grades 4–5 material. Prerequisites, launch, materials, hints and theorem-first mathematical overview are in the separate adult guide. Physical fit, demonstrations and classroom timing have not been tested.

Current pages: **K–1 5; Grades 2–3 5; Grades 4–5 6; adult guide 5**. Print selected student pages single-sided on US Letter at Actual Size / 100%.

## Rebuild outside the project

Extract the complete ZIP. Install Python 3.11 or later with `requirements.txt`, a normal TeX Live distribution providing pdfLaTeX/TikZ/Helvetica, and Poppler's `pdftoppm` where used by the existing checks. Matching guide fonts and licenses are included; the root build selects package-local fonts in earlier packages. No project checkout or original workspace path is needed.

    python3 -m pip install -r requirements.txt
    python3 build.py
    python3 verify_revision.py

The current verifier compares paper geometry and every 100-dpi rendered page against `reference-pdfs/`; timestamps may differ. It permits only specifically audited full-page font/hyphenation alternatives for unchanged student PDFs. See `review/fresh-review-rebuild.md` for actual results. The original strict verifier (`verify_rebuild.py` or `verify.py`) is retained and rejects those alternatives. The corpus report explicitly records any pre-existing small TeX font-metric differences for unchanged student bands; their current print/reference PDFs stay byte-identical. For Weeks 24 and 35, the detailed student-stage record is `review/student-reviser-fresh-review.md`. The corpus release report records those differences explicitly rather than calling them pixel-identical.

Edit student problems in `problem-files/problems/*.md` (figures and the page template in `problem-files/figures.py`); `build.py` regenerates `student-src/*.tex` from them before compiling, so do not edit the TeX by hand. To build every view: `python3 problem-files/tools/build.py problem-files --out views`. Each problem file's key repeats the main answer from the guide, and `problem-files/guide/overview.tex` repeats the guide's first page; `python3 problem-files/check_guide_copy.py` confirms every copied sentence is still in `facilitator-src/guide.json`. Edit the existing guide source under `facilitator-src/`. Where present, `facilitator-src/route-note.json` holds the concise starting/return update; the root build regenerates the guide before appending it exactly once. Do not run the appender alone against an already appended guide. Build intermediates belong in a separate working copy; inspect changed pages before updating references.

The student-page fixes are checked by `python3 review/verify_student_fixes_2026_10_23.py`. The current reference manifest is `review/reference-manifest.json`; revision evidence is `review/fresh-review-2026-10-04.md` and, for the October 23 guide corrections, `review/card-fixes-2026-10-23.md` with its check `review/verify_card_fixes_2026_10_23.py`. Older review files and `review/README-before-fresh-review-2026-10-04.md` describe their dated versions. Prior releases are archived outside the current package in the project.

## Use and rights

Original worksheet prose, diagrams and builders are provided for the organizer's use and adaptation. Preserve source attribution. Third-party books and articles retain their rights and are not redistributed here. Included fonts retain their licenses. No broader third-party license is implied. Routine adult reading or recording is allowed; children should retain the mathematical choices.
