# Week 50 Staircases and lengths editable source

## Current release: October 23, 2026 card fixes

The review card's shoulds and coulds were made in the problem files and the guide: the page-1 example lettered in path order with one 70 mm bar, reworded Problems 2, 3 and 5, a 7.5 mm strip and a fewest-turns question for Grades 4–5 Problem 5, three stale phrases removed, and the guide's overview (the turn optimum), materials (a K–1 pipe cleaner), launch, hour and keys. `review/card-fixes-2026-10-23.md` lists every change and the checks; `src/check.py` and `review/verify_card_fixes_2026_10_23.py` run them. Unpiloted; the pipe cleaner is untried.

## Earlier release: October 4, 2026 fresh-review revision

The guide now gives first routes, readiness-dependent continuation and return visits; original mathematical investigations are retained.

This is an unpiloted theme library, not a fixed meeting schedule. Select a manageable first route in the guide and return for further investigations. Preserve the full Grades 4–5 material. Prerequisites, launch, materials, hints and theorem-first mathematical overview are in the separate adult guide. Physical fit, demonstrations and classroom timing have not been tested.

Current pages: **K–1 5; Grades 2–3 5; Grades 4–5 6; adult guide 4**. Print selected student pages single-sided on US Letter at Actual Size / 100%.

The student pages are stored as problem files: `problem-files/week.toml`, `problem-files/figures.py` and one file per problem in `problem-files/problems/`, with each band's wording inside it (in the repository, `lowell-math-circle-year-2/source/week-50/`). `src/regenerate.py` writes the band LaTeX from them, and `src/build.sh` runs it before compiling, so `build.py` here and the problem-file tools (`problem-files/tools/build.py`) give the same student PDFs. The conversion, on October 23, 2026, changed no wording or figure: the PDFs matched the previous ones in text and 100-dpi pixels (`make.py`, the old builder, is archived in the project). The card fixes followed it the same day.

## Rebuild outside the project

Extract the complete ZIP. Install Python 3 with `requirements.txt`, a normal TeX Live distribution providing pdfLaTeX/TikZ/Helvetica, and Poppler's `pdftoppm` where used by the existing checks. Matching guide fonts and licenses are included; the root build selects package-local fonts in earlier packages. No project checkout or original workspace path is needed.

    python3 -m pip install -r requirements.txt
    python3 build.py
    python3 verify_revision.py
    python3 verify_math.py
    python3 review/verify_card_fixes_2026_10_23.py

The current verifier compares paper geometry and every 100-dpi rendered page against `reference-pdfs/`; timestamps may differ. It permits only specifically audited full-page font/hyphenation alternatives for unchanged student PDFs. See `review/fresh-review-rebuild.md` for actual results. The original strict verifier (`verify_rebuild.py` or `verify.py`) is retained and rejects those alternatives. The corpus report explicitly records any pre-existing small TeX font-metric differences for unchanged student bands; their current print/reference PDFs stay byte-identical. For Weeks 24 and 35, the detailed student-stage record is `review/student-reviser-fresh-review.md`. The corpus release report records those differences explicitly rather than calling them pixel-identical.

Edit student problems in the problem files (above); `src/` holds the generated TeX. Edit the existing guide source under `facilitator-src/`. Where present, `facilitator-src/route-note.json` holds the concise starting/return update; the root build regenerates the guide before appending it exactly once. Do not run the appender alone against an already appended guide. Build intermediates belong in a separate working copy; inspect changed pages before updating references.

The current reference manifest is `review/reference-manifest.json`; revision evidence is `review/fresh-review-2026-10-04.md`. Older review files and `review/README-before-fresh-review-2026-10-04.md` describe their dated versions. Prior releases are archived outside the current package in the project.

## Use and rights

Original worksheet prose, diagrams and builders are provided for the organizer's use and adaptation. Preserve source attribution. Third-party books and articles retain their rights and are not redistributed here. Included fonts retain their licenses. No broader third-party license is implied. Routine adult reading or recording is allowed; children should retain the mathematical choices.
