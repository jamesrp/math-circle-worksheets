# Week 42 Fair results from a bag editable source

## Current release: October 23, 2026 card shoulds, on the October 4 fresh-review revision

The guide gives first routes, readiness-dependent continuation and return visits; original mathematical investigations are retained.

**Card shoulds, October 23, 2026.** The student pages are stored as problem files (see `src/README.md`). The review card's nine student-page and guide shoulds and four coulds were made there and in the guide: K–1 page 1 says to put each counter back after every draw and captions its bags; K–1 page 4 pictures all 16 marked pairs of the one-red and two-red bags, Problem 5 (now on page 5) starts "Keep your rule." and Problem 6 asks whether six random pairs always give a shape; Grades 2–3 Problems 3 and 5 have blank 4 × 4 grids, Problem 6 ends at "within six pairs?" and page 2 drops a narrating sentence; Grades 4–5 Problem 2 asks "Do the shape chances match? Explain." above a grid headed R1, R2, R3, B; "independently" and some bag captions are cut; the guide's materials, launch, overview and keys follow. All three packets are now v3. `review/card-shoulds-2026-10-23.md` lists the changes; `review/verify_card_shoulds_2026_10_23.py` checks them.

This is an unpiloted theme library, not a fixed meeting schedule. Select a manageable first route in the guide and return for further investigations. Preserve the full Grades 4–5 material. Prerequisites, launch, materials, hints and theorem-first mathematical overview are in the separate adult guide. Physical fit, demonstrations and classroom timing have not been tested.

Current pages: **K–1 6; Grades 2–3 4; Grades 4–5 4; adult guide 6**. Print selected student pages single-sided on US Letter at Actual Size / 100%.

## Rebuild outside the project

Extract the complete ZIP. Install Python 3 with `requirements.txt`, a normal TeX Live distribution providing pdfLaTeX/TikZ/Helvetica, and Poppler's `pdftoppm` where used by the existing checks. Matching guide fonts and licenses are included; the root build selects package-local fonts in earlier packages. No project checkout or original workspace path is needed.

    python3 -m pip install -r requirements.txt
    python3 build.py
    python3 verify_revision.py

The current verifier compares paper geometry and every 100-dpi rendered page against `reference-pdfs/`; timestamps may differ. It permits only specifically audited full-page font/hyphenation alternatives for unchanged student PDFs. See `review/fresh-review-rebuild.md` for actual results. The original strict verifier (`verify_rebuild.py` or `verify.py`) is retained and rejects those alternatives. The corpus report explicitly records any pre-existing small TeX font-metric differences for unchanged student bands; their current print/reference PDFs stay byte-identical. For Weeks 24 and 35, the detailed student-stage record is `review/student-reviser-fresh-review.md`. The corpus release report records those differences explicitly rather than calling them pixel-identical.

Edit student generators and their generated TeX in `src/` or `student-src/`. Edit the existing guide source under `facilitator-src/`. Where present, `facilitator-src/route-note.json` holds the concise starting/return update; the root build regenerates the guide before appending it exactly once. Do not run the appender alone against an already appended guide. Build intermediates belong in a separate working copy; inspect changed pages before updating references.

The current reference manifest is `review/reference-manifest.json`; revision evidence is `review/fresh-review-2026-10-04.md`. Older review files and `review/README-before-fresh-review-2026-10-04.md` describe their dated versions. Prior releases are archived outside the current package in the project.

## Use and rights

Original worksheet prose, diagrams and builders are provided for the organizer's use and adaptation. Preserve source attribution. Third-party books and articles retain their rights and are not redistributed here. Included fonts retain their licenses. No broader third-party license is implied. Routine adult reading or recording is allowed; children should retain the mathematical choices.
