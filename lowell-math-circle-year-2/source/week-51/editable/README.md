# Week 51 Honest measurement ranges editable source

## Problem files, October 23, 2026

The student pages are stored as problem files: `problem-files/week.toml`, `problem-files/figures.py` and one file per problem in `problem-files/problems/`, with each band's wording inside it (in the repository, `lowell-math-circle-year-2/source/week-51/`). `src/regenerate.py` writes the band LaTeX from them, and `src/build.sh` runs it before compiling, so `build.py` here and the problem-file tools (`problem-files/tools/build.py`) give the same student PDFs. The conversion changed no wording or figure: the regenerated LaTeX is byte-identical to the old builder's (`make.py`, archived in the project). The adult guide keeps its source in `facilitator-src/content.json`; the problem files repeat its keys for a key view arranged by problem, and `problem-files/check_guide_copy.py` checks that the two agree.

## Card fixes, October 23, 2026

Made in the problem files after the conversion: K–1's shared-A problem (now Problem 6) says the two A's in the top picture are the same length and that each try may use new lengths (the review card's second must); the gap page now comes before the shared-A page in every band, so the problems are renumbered; the fill-9 page has A from 3 to 7 and four boards; page 1's launch draws one join from the ruler's 0; K–1 Problem 3 says fitting within 9 includes 9; K–1 Problem 5 has two rulers; "One possible setting;" is cut. The guide's launch, keys and route note match, and its hour plan fits 35 to 40 minutes at the tables (should 8). [review/card-fixes-2026-10-23.md](review/card-fixes-2026-10-23.md) lists the changed pages, what was deferred and how it was checked. Current pages: **K–1 6; Grades 2–3 6; Grades 4–5 6; adult guide 4; table kit 1**.

## Table kit, October 23, 2026

`materials/build_materials.py` builds `materials.pdf` (reference copy in `reference-pdfs/`; print copy `week-51-materials.pdf`): one US Letter page to print on card stock at 100%, one per pair or trio. It holds two gray strips of every whole length from 1 to 15 units and two white add-ons each of 4 and 1 units, all 10 mm wide at the student pages' 10 mm per unit, in abutting rows of 16 units (160 mm, one 0–16 ruler). Each strip carries its length. No sleeves: a child lays a strip along a printed band from 0 and checks that its end lands inside, then joins strips on a 0–16 ruler; every extreme in the keys is a whole length. The page has a 10 cm scale check and a per-table print count. `materials/verify_materials.py` measures every strip, reads its numeral back, reads the printed ranges from the student reference PDFs and rebuilds every key's witnesses from one set; `build.py` runs both. The guide's page 1 now names the kit, replaces the sleeves and add-on instructions, and counts cutting time; no other guide page and no student page changed. A clean rebuild from the extracted ZIP reproduces the guide and the kit with exact 100-dpi pixels; with TeX Live 2023 the unchanged Grades 2–3 and 4–5 packets rebuild with two different hyphenations outside the audited allowances, and their print and reference copies are unchanged. The previous guide and ZIP are archived in the project. The kit is physically unrehearsed.

Current pages: **K–1 6; Grades 2–3 6; Grades 4–5 6; adult guide 4; table kit 1**.

## Current release: October 4, 2026 fresh-review revision

The guide now gives first routes, readiness-dependent continuation and return visits; original mathematical investigations are retained.

This is an unpiloted theme library, not a fixed meeting schedule. Select a manageable first route in the guide and return for further investigations. Preserve the full Grades 4–5 material. Prerequisites, launch, materials, hints and theorem-first mathematical overview are in the separate adult guide. Physical fit, demonstrations and classroom timing have not been tested.

Current pages: **K–1 6; Grades 2–3 6; Grades 4–5 6; adult guide 4**. Print selected student pages single-sided on US Letter at Actual Size / 100%.

## Rebuild outside the project

Extract the complete ZIP. Install Python 3 with `requirements.txt`, a normal TeX Live distribution providing pdfLaTeX/TikZ/Helvetica, and Poppler's `pdftoppm` where used by the existing checks. Matching guide fonts and licenses are included; the root build selects package-local fonts in earlier packages. No project checkout or original workspace path is needed.

    python3 -m pip install -r requirements.txt
    python3 build.py
    python3 verify_revision.py

The current verifier compares paper geometry and every 100-dpi rendered page against `reference-pdfs/`; timestamps may differ. It permits only specifically audited full-page font/hyphenation alternatives for unchanged student PDFs. See `review/fresh-review-rebuild.md` for actual results. The original strict verifier (`verify_rebuild.py` or `verify.py`) is retained and rejects those alternatives. The corpus report explicitly records any pre-existing small TeX font-metric differences for unchanged student bands; their current print/reference PDFs stay byte-identical. For Weeks 24 and 35, the detailed student-stage record is `review/student-reviser-fresh-review.md`. The corpus release report records those differences explicitly rather than calling them pixel-identical.

Edit student problems in the problem files (above); `src/` holds the generated TeX. Edit the existing guide source under `facilitator-src/`. Where present, `facilitator-src/route-note.json` holds the concise starting/return update; the root build regenerates the guide before appending it exactly once. Do not run the appender alone against an already appended guide. Build intermediates belong in a separate working copy; inspect changed pages before updating references.

The current reference manifest is `review/reference-manifest.json`; revision evidence is `review/fresh-review-2026-10-04.md`. Older review files and `review/README-before-fresh-review-2026-10-04.md` describe their dated versions. Prior releases are archived outside the current package in the project.

## Use and rights

Original worksheet prose, diagrams and builders are provided for the organizer's use and adaptation. Preserve source attribution. Third-party books and articles retain their rights and are not redistributed here. Included fonts retain their licenses. No broader third-party license is implied. Routine adult reading or recording is allowed; children should retain the mathematical choices.
