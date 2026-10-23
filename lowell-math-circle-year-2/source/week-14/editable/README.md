# Polygon triangulations and flips: Week 14 editable release

## Current release: October 4, 2026 fresh-review revision, with the October 23 card fixes

The guide now gives first routes, readiness-dependent continuation and return visits; original mathematical investigations are retained. On October 23, 2026 the student pages became problem files, and the review card's should fixes were made in them (v3 packets): K–1 Problem 5's copies print their start in light gray, grades 2–3 page 8 is headed "Problem 7 (continued)" only, four questions are plainer, grades 4–5 Problem 4 has arrows to the target, and grades 2–3 page 6's copies clear the footer. The guide adds a referee check for every change, quarter-cut tracing sheets for eleven children, a menu matching the group's hour, two key notes, a route-recording hint and the corrected route note. See `review/card-fixes-2026-10-23.md`.

This is an unpiloted theme library, not a fixed meeting schedule. Select a manageable first route in the guide and return for further investigations. Preserve the full Grades 4–5 material. Prerequisites, launch, materials, hints and theorem-first mathematical overview are in the separate adult guide. Physical fit, demonstrations and classroom timing have not been tested.

Later on October 23 the tightest recording copies were enlarged (K–1 p. 4, Grades 2–3 p. 6, Grades 4–5 p. 5; footers v4, named on guide p. 2).

Current pages: **K–1 6; Grades 2–3 8; Grades 4–5 7; adult guide 14**. Print selected student pages single-sided on US Letter at Actual Size / 100%.

## Rebuild outside the project

Extract the complete ZIP. Install Python 3 with `requirements.txt`, a normal TeX Live distribution providing pdfLaTeX/TikZ/Helvetica, and Poppler's `pdftoppm` where used by the existing checks. Matching guide fonts and licenses are included; the root build selects package-local fonts in earlier packages. No project checkout or original workspace path is needed.

    python3 -m pip install -r requirements.txt
    bash build.sh
    python3 verify_revision.py

The current verifier compares paper geometry and every 100-dpi rendered page against `reference-pdfs/`; timestamps may differ. It permits only specifically audited full-page font/hyphenation alternatives for unchanged student PDFs; after the October 23 card fixes every reference was rebuilt, so `review/rebuild-pixel-allowances.json` lists none. See `review/fresh-review-rebuild.md` for actual results. The original strict verifier (`verify_rebuild.py` or `verify.py`) is retained and rejects those alternatives. The corpus report explicitly records any pre-existing small TeX font-metric differences for unchanged student bands; their current print/reference PDFs stay byte-identical. For Weeks 24 and 35, the detailed student-stage record is `review/student-reviser-fresh-review.md`. The corpus release report records those differences explicitly rather than calling them pixel-identical.

The student pages are stored as problem files (since October 23, 2026): in the portable ZIP they are in `problem-files/` (`week.toml`, `figures.py`, `problems/*.md`) with the tools in `problem-files/tools/`; in the repository they are in the week folder that holds `editable/`. Edit the problem files; `src/regenerate.py` writes `src/*.tex` from them and the build runs it first, followed by the enumeration checks in `src/student_checks.py`. `problem-files/tools/build.py problem-files --out <folder>` also builds the menu, key and route packets. Edit the existing guide source under `facilitator-src/`. Where present, `facilitator-src/route-note.json` holds the concise starting/return update; the root build regenerates the guide before appending it exactly once. Do not run the appender alone against an already appended guide. Build intermediates belong in a separate working copy; inspect changed pages before updating references.

The current reference manifest is `review/reference-manifest.json`; revision evidence is `review/fresh-review-2026-10-04.md`. Older review files and `review/README-before-fresh-review-2026-10-04.md` describe their dated versions. Prior releases are archived outside the current package in the project.

## Use and rights

Original worksheet prose, diagrams and builders are provided for the organizer's use and adaptation. Preserve source attribution. Third-party books and articles retain their rights and are not redistributed here. Included fonts retain their licenses. No broader third-party license is implied. Routine adult reading or recording is allowed; children should retain the mathematical choices.
