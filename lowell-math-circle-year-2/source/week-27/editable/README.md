# Stable matching and two-sided choices: Week 27 editable release

## Table kit, October 23, 2026

`materials/build_materials.py` builds `materials.pdf` (reference copy in `reference-pdfs/`; print copy `week-27-materials.pdf`): nine US Letter pages, three per table band, to print on card stock at 100%. Each band's sheets hold its tokens (A, B, X, Y for K–1; A–D and W–Z for the older bands, 24 mm), four links and a dashed link, the launch card, and one case card for every printed case in its packet, with all of that case's strips at the guide's 20 mm icon size (four-choice strips 122 mm). K–1 adds sixteen 18 mm letter tiles for swapping and filling strips; Grades 4–5 adds sixteen already-asked markers. Profiles are read from `src/math_checks.json`, the student builder's data, so nobody copies a case by hand. Every page has a 10 cm scale check and a per-table print count. `materials/verify_materials.py` measures every size and reads each case card back letter by letter; `build.sh` runs both. The guide's page 2 now names the kit and counts cutting time, and its shared launch uses a profile printed in no packet (A: Y > X; B: X > Y; X: A > B; Y: A > B); no other guide page and no student page changed. A clean rebuild from the extracted ZIP reproduces the guide and the kit with exact 100-dpi pixels; with TeX Live 2023 the unchanged student packets rebuild with small font-metric differences outside the audited allowances, as they did before this change, and their print and reference copies are unchanged. The previous guide and ZIP are archived in the project. The kit is physically unrehearsed.

Current pages: **K–1 7; Grades 2–3 6; Grades 4–5 6; adult guide 19; table kit 9**.

## Current release: October 4, 2026 fresh-review revision

The guide now gives first routes, readiness-dependent continuation and return visits; original mathematical investigations are retained.

This is an unpiloted theme library, not a fixed meeting schedule. Select a manageable first route in the guide and return for further investigations. Preserve the full Grades 4–5 material. Prerequisites, launch, materials, hints and theorem-first mathematical overview are in the separate adult guide. Physical fit, demonstrations and classroom timing have not been tested.

Current pages: **K–1 7; Grades 2–3 6; Grades 4–5 6; adult guide 19**. Print selected student pages single-sided on US Letter at Actual Size / 100%.

## Rebuild outside the project

Extract the complete ZIP. Install Python 3 with `requirements.txt`, a normal TeX Live distribution providing pdfLaTeX/TikZ/Helvetica, and Poppler's `pdftoppm` where used by the existing checks. Matching guide fonts and licenses are included; the root build selects package-local fonts in earlier packages. No project checkout or original workspace path is needed.

    python3 -m pip install -r requirements.txt
    bash build.sh
    python3 verify_revision.py

The current verifier compares paper geometry and every 100-dpi rendered page against `reference-pdfs/`; timestamps may differ. It permits only specifically audited full-page font/hyphenation alternatives for unchanged student PDFs. See `review/fresh-review-rebuild.md` for actual results. The original strict verifier (`verify_rebuild.py` or `verify.py`) is retained and rejects those alternatives. The corpus report explicitly records any pre-existing small TeX font-metric differences for unchanged student bands; their current print/reference PDFs stay byte-identical. For Weeks 24 and 35, the detailed student-stage record is `review/student-reviser-fresh-review.md`. The corpus release report records those differences explicitly rather than calling them pixel-identical.

Edit student generators and their generated TeX in `src/` or `student-src/`. Edit the existing guide source under `facilitator-src/`. Where present, `facilitator-src/route-note.json` holds the concise starting/return update; the root build regenerates the guide before appending it exactly once. Do not run the appender alone against an already appended guide. Build intermediates belong in a separate working copy; inspect changed pages before updating references.

The current reference manifest is `review/reference-manifest.json`; revision evidence is `review/fresh-review-2026-10-04.md`. Older review files and `review/README-before-fresh-review-2026-10-04.md` describe their dated versions. Prior releases are archived outside the current package in the project.

## Use and rights

Original worksheet prose, diagrams and builders are provided for the organizer's use and adaptation. Preserve source attribution. Third-party books and articles retain their rights and are not redistributed here. Included fonts retain their licenses. No broader third-party license is implied. Routine adult reading or recording is allowed; children should retain the mathematical choices.
