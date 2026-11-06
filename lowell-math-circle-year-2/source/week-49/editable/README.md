# Week 49 Four towers and differences editable source

## Current release: November 6, 2026 kid-fit revision (v4)

A kid-fit pilot (critic, then reviser, student pages only) revised all three packets, and James approved adopting them on November 6, 2026. The packets are now v4 (footers F49-K-v4, F49-23-v4, F49-45-v4; key view F49-G-v4) with 7, 8 and 8 pages. K–1: short spoken rules on page 1 with a cup and counter for each move, Problem 1 on its own page beside the mats, the orders of 0, 1, 2 and 4 moved forward to Problem 2 with three record rows, then the longest run (3), one and two moves (4–5, "take exactly two moves") and three stations (6). Grades 2–3: Problem 1 beside the mats, orders moved forward to Problem 2, then the longest run (3), predecessors (4), three stations (5) and the tallest tower on its own page (6, "for each question"). Grades 4–5: Problem 1 runs only (1,1,0,0) and (0,0,0,2) and asks which lasts longer; the numbering is unchanged; Problem 5 has two columns of letter boxes. In every band the new mats and new rings are shaded grey, and the station-count problem has four-station mats and A–B–C–D rows on its page and the three-station mats and rows on the next. The adult guide (v4, still 3 pages and the route page) is renumbered to match, adds a cup and 10 counters per K–1 pair, says that the Grades 4–5 doubled start takes 36 of the 40 cubes, and adds short notes on two-move starts, the (1,1,1,0) predecessor and building the parity rule with cubes. `review/verify_kid_fit_2026_11_06.py` checks the new pages and guide; `src/check.py` checks the new counts. Unpiloted; physical fit is unrehearsed.

## Earlier release: October 23, 2026 card fixes

The review card's shoulds and clear coulds were made in the problem files and the guide: new printed orders and blank rings so no page shows an answer, 36 mm stations with a 9 mm gap and an arrow between the old and new mats, record rows on the three-station, predecessor and parity pages, the all-zero rule on page 1, new Grades 4–5 scaling starts, one theme name ("Four towers and differences"), and the guide's materials (40 cubes per pair), launch, hour and keys. `review/card-fixes-2026-10-23.md` lists every change and the checks; `src/check.py` and `review/verify_card_fixes_2026_10_23.py` run them. Unpiloted; the respaced mats are physically unrehearsed.

## Earlier release: October 4, 2026 fresh-review revision

The guide now gives first routes, readiness-dependent continuation and return visits; original mathematical investigations are retained.

This is an unpiloted theme library, not a fixed meeting schedule. Select a manageable first route in the guide and return for further investigations. Preserve the full Grades 4–5 material. Prerequisites, launch, materials, hints and theorem-first mathematical overview are in the separate adult guide. Physical fit, demonstrations and classroom timing have not been tested.

Current pages: **K–1 7; Grades 2–3 8; Grades 4–5 8; adult guide 4**. Print selected student pages single-sided on US Letter at Actual Size / 100%.

The student pages are stored as problem files: `problem-files/week.toml`, `problem-files/figures.py` and one file per problem in `problem-files/problems/`, with each band's wording inside it (in the repository, `lowell-math-circle-year-2/source/week-49/`). `src/regenerate.py` writes the band LaTeX from them, and `src/build.sh` runs it before compiling, so `build.py` here and the problem-file tools (`problem-files/tools/build.py`) give the same student PDFs. The conversion, on October 23, 2026, changed no wording or figure: the PDFs matched the previous ones in text and 100-dpi pixels (`make.py`, the old builder, is archived in the project). The card fixes followed it the same day.

## Rebuild outside the project

Extract the complete ZIP. Install Python 3 with `requirements.txt`, a normal TeX Live distribution providing pdfLaTeX/TikZ/Helvetica, and Poppler's `pdftoppm` where used by the existing checks. Matching guide fonts and licenses are included; the root build selects package-local fonts in earlier packages. No project checkout or original workspace path is needed.

    python3 -m pip install -r requirements.txt
    python3 build.py
    python3 verify_revision.py
    python3 verify_math.py
    python3 review/verify_kid_fit_2026_11_06.py

`review/verify_card_fixes_2026_10_23.py` checks the October 23 (v3) PDFs, which are archived in the project; it fails on the v4 pages by design.

The current verifier compares paper geometry and every 100-dpi rendered page against `reference-pdfs/`; timestamps may differ. It permits only specifically audited full-page font/hyphenation alternatives for unchanged student PDFs. See `review/fresh-review-rebuild.md` for actual results. The original strict verifier (`verify_rebuild.py` or `verify.py`) is retained and rejects those alternatives. The corpus report explicitly records any pre-existing small TeX font-metric differences for unchanged student bands; their current print/reference PDFs stay byte-identical. For Weeks 24 and 35, the detailed student-stage record is `review/student-reviser-fresh-review.md`. The corpus release report records those differences explicitly rather than calling them pixel-identical.

Edit student problems in the problem files (above); `src/` holds the generated TeX. Edit the existing guide source under `facilitator-src/`. Where present, `facilitator-src/route-note.json` holds the concise starting/return update; the root build regenerates the guide before appending it exactly once. Do not run the appender alone against an already appended guide. Build intermediates belong in a separate working copy; inspect changed pages before updating references.

The current reference manifest is `review/reference-manifest.json`; revision evidence is `review/fresh-review-2026-10-04.md`. Older review files and `review/README-before-fresh-review-2026-10-04.md` describe their dated versions. Prior releases are archived outside the current package in the project.

## Use and rights

Original worksheet prose, diagrams and builders are provided for the organizer's use and adaptation. Preserve source attribution. Third-party books and articles retain their rights and are not redistributed here. Included fonts retain their licenses. No broader third-party license is implied. Routine adult reading or recording is allowed; children should retain the mathematical choices.
