# How much memory does a machine need?: Week 17 editable release

## Current release: October 23, 2026 card fixes

**Card fixes, October 23, 2026 (v3).** From the review card (plans/review/week-17.md in the project). Student pages: on K–1 P6, Grades 2–3 P4 and Grades 4–5 P2 the two rows of each pair now sit one above the other, joined by a brace to one "+ ____" line long enough for "can't", so the same added cards go after both rows; each row keeps its own answer to circle. No other student page changed except the v3 footers. Table kit: `materials/build_materials.py` builds `materials.pdf` (reference copy in `reference-pdfs/`; print copy `week-17-materials.pdf`), one card-stock sheet per table, cut on straight lines: 12 R and 12 B cards (30 mm; R a red square, B a blue circle), 12 blank 30 mm state circles and 4 markers (14 mm, two solid and two rings, small enough for the pages' 16.8 mm printed circles). `materials/verify_materials.py` measures it from the PDF and checks it against the problems' rows, pairs and machines. Guide: the kit, four markers, about 20 minutes to make three kits, crayons at K–1, a launch on R R B drawn large with partner roles (one turns the card and names the arrow, one moves the marker; switch each row), an hour with a 5-minute run and 38 minutes at the tables, check marks in the K–1 keys, sorting recorded rather than physical rows in K–1 P2, the P1 lines that are not answer counts, rows one above the other with both markers moved in the shared-ending hints, a Grades 4–5 offer of the Grades 2–3 machines (route note), and no leftover process notes. `review/verify_card_fixes_2026_10_23.py` checks these claims from the built PDFs and the guide source. The previous PDFs and ZIP are archived in the project. Unpiloted; the kit is physically unrehearsed.

### October 4, 2026 fresh-review revision

**Problem files.** The student pages are now stored as problem files, one per problem, in `problem-files/` (in the repository: `lowell-math-circle-year-2/source/week-17/`). The conversion changed no wording or figure. `src/regenerate.py` writes the student LaTeX from them, and `problem-files/tools/build.py` also builds first-route and return packets, a one-page problem menu and a key view.

The guide now gives first routes, readiness-dependent continuation and return visits; original mathematical investigations are retained.

This is an unpiloted theme library, not a fixed meeting schedule. Select a manageable first route in the guide and return for further investigations. Preserve the full Grades 4–5 material. Prerequisites, launch, materials, hints and theorem-first mathematical overview are in the separate adult guide. Physical fit, demonstrations and classroom timing have not been tested.

Current pages: **K–1 5; Grades 2–3 5; Grades 4–5 5; adult guide 11; table kit 1**. Print selected student pages single-sided on US Letter at Actual Size / 100%.

## Rebuild outside the project

Extract the complete ZIP. Install Python 3.11 or later with `requirements.txt`, a normal TeX Live distribution providing pdfLaTeX/TikZ/Helvetica, and Poppler's `pdftoppm` where used by the existing checks. Matching guide fonts and licenses are included; the root build selects package-local fonts in earlier packages. No project checkout or original workspace path is needed.

    python3 -m pip install -r requirements.txt
    bash build.sh
    python3 verify_revision.py
    python3 review/verify_card_fixes_2026_10_23.py

The current verifier compares paper geometry and every 100-dpi rendered page against `reference-pdfs/`; timestamps may differ. It permits only specifically audited full-page font/hyphenation alternatives for unchanged student PDFs. See `review/fresh-review-rebuild.md` for actual results. The original strict verifier (`verify_rebuild.py` or `verify.py`) is retained and rejects those alternatives. The corpus report explicitly records any pre-existing small TeX font-metric differences for unchanged student bands; their current print/reference PDFs stay byte-identical. For Weeks 24 and 35, the detailed student-stage record is `review/student-reviser-fresh-review.md`. The corpus release report records those differences explicitly rather than calling them pixel-identical.

Edit student problems in `problem-files/problems/*.md` (the machines, cards and page frame in `problem-files/figures.py`); `build.sh` regenerates `src/*.tex` from them before compiling and still runs `src/check_math.py`, so do not edit the TeX by hand. To build every view: `python3 problem-files/tools/build.py problem-files --out views`. Edit the existing guide source under `facilitator-src/`. Where present, `facilitator-src/route-note.json` holds the concise starting/return update; the root build regenerates the guide before appending it exactly once. Do not run the appender alone against an already appended guide. Build intermediates belong in a separate working copy; inspect changed pages before updating references.

The current reference manifest is `review/reference-manifest.json`; revision evidence is `review/fresh-review-2026-10-04.md`. Older review files and `review/README-before-fresh-review-2026-10-04.md` describe their dated versions. Prior releases are archived outside the current package in the project.

## Use and rights

Original worksheet prose, diagrams and builders are provided for the organizer's use and adaptation. Preserve source attribution. Third-party books and articles retain their rights and are not redistributed here. Included fonts retain their licenses. No broader third-party license is implied. Routine adult reading or recording is allowed; children should retain the mathematical choices.
