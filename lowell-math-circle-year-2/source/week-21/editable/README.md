# Shortest reflected paths: Week 21 editable release

## Current release: October 23, 2026 review-card fixes

The October 23, 2026 fixes from the review card (`plans/review/week-21.md` in the project) are recorded in `review/card-fixes-2026-10-23.md` and checked by `review/check_card_fixes.py`, the last step of `build.sh`. Grades 2–3 Problem 7 now asks the Grades 4–5 question (W21-23-v3); K–1 and Grades 4–5 are unchanged. The guide gives each contact from the line's end mark, says what string can and cannot settle, plans for eleven children with four strings per table, and numbers the route update 18 / 18.

The October 4, 2026 fresh-review revision gave the guide first routes, readiness-dependent continuation and return visits; original mathematical investigations are retained.

This is an unpiloted theme library, not a fixed meeting schedule. Select a manageable first route in the guide and return for further investigations. Preserve the full Grades 4–5 material. Prerequisites, launch, materials, hints and theorem-first mathematical overview are in the separate adult guide. Physical fit, demonstrations and classroom timing have not been tested.

Current pages: **K–1 7; Grades 2–3 7; Grades 4–5 7; adult guide 19**. Print selected student pages single-sided on US Letter at Actual Size / 100%.

## Rebuild outside the project

Extract the complete ZIP. Install Python 3 with `requirements.txt`, a normal TeX Live distribution providing pdfLaTeX/TikZ/Helvetica, and Poppler's `pdftoppm` where used by the existing checks. Matching guide fonts and licenses are included; the root build selects package-local fonts in earlier packages. No project checkout or original workspace path is needed.

    python3 -m pip install -r requirements.txt
    bash build.sh
    python3 verify_revision.py

The current verifier compares paper geometry and every 100-dpi rendered page against `reference-pdfs/`; timestamps may differ. It permits only specifically audited full-page font/hyphenation alternatives for unchanged student PDFs. See `review/fresh-review-rebuild.md` for actual results. The original strict verifier (`verify_rebuild.py` or `verify.py`) is retained and rejects those alternatives. The corpus report explicitly records any pre-existing small TeX font-metric differences for unchanged student bands; their current print/reference PDFs stay byte-identical. For Weeks 24 and 35, the detailed student-stage record is `review/student-reviser-fresh-review.md`. The corpus release report records those differences explicitly rather than calling them pixel-identical.

Since October 23, 2026 the student pages are problem files (in the repository `../week.toml`, `../figures.py` and `../problems/`; in the ZIP `problem-files/`, with the tools in `problem-files/tools/`): `src/regenerate.py` writes `src/*.tex` from them and runs the board checks. Edit the problem files, not the generated TeX. Edit the existing guide source under `facilitator-src/`. Where present, `facilitator-src/route-note.json` holds the concise starting/return update; the root build regenerates the guide before appending it exactly once. Do not run the appender alone against an already appended guide. Build intermediates belong in a separate working copy; inspect changed pages before updating references.

The current reference manifest is `review/reference-manifest.json`; revision evidence is `review/fresh-review-2026-10-04.md`. Older review files and `review/README-before-fresh-review-2026-10-04.md` describe their dated versions. Prior releases are archived outside the current package in the project.

## Guide production and rebuild notes

These notes were in the guide until October 23, 2026; they concern how it was made, not how to run the session.

- **Production, October 3, 2026.** The guide is a separate production, not a classroom-tested part of the student-page workflow. All 21 final problem numbers and board assignments were read from the final PDFs and matched to the final source. Drawing coordinates were independently transcribed into rational numbers (`facilitator-src/board-data.json`), then compared to the final source without executing its builder. The check recomputed every assigned reflected optimum, exact squared minimum, permitted crossing and required reflected point. K-1 P2 is the guesses board and K-1 P3 the reflected-partner board. The student PDFs were not changed. Since October 23, 2026, `check_geometry.py` reads the board data from `figures.py` and each band's board order from the problem files.
- **Rebuild and review.** `bash build.sh` runs `facilitator-src/check_geometry.py`, then `build_guide.py`, `build_overview.py` and `add_route_note.py`, with ReportLab and the DejaVu fonts in `fonts/`. The guide builders write only the guide; they do not regenerate student packets. Render the PDF with `pdftoppm` and inspect every changed page after edits. The readable `facilitator-src/guide-content.md` export and the Python source are editable. The guide remains draft and unpiloted pending organizer review and classroom use.

## Use and rights

Original worksheet prose, diagrams and builders are provided for the organizer's use and adaptation. Preserve source attribution. Third-party books and articles retain their rights and are not redistributed here. Included fonts retain their licenses. No broader third-party license is implied. Routine adult reading or recording is allowed; children should retain the mathematical choices.
