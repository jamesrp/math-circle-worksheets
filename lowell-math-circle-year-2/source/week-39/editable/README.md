# Week 39 Road detours editable source

## Current release: October 4, 2026 fresh-review revision

The guide now gives first routes, readiness-dependent continuation and return visits; original mathematical investigations are retained. K–1 adds short physical tree and ring trips before the five retained investigations. All existing board coordinates and older packets remain.

**Problem files, October 23, 2026.** The student pages are now stored as problem files, one per problem with its band variants, in `problem-files/` (in the repository: `lowell-math-circle-year-2/source/week-39/`). The conversion changed no wording or figure: the generated LaTeX is byte-identical. `src/regenerate.py` writes the student LaTeX from them, and `problem-files/tools/build.py` also builds first-route and return packets, a one-page problem menu and a key arranged by problem.

**Card fixes, October 23, 2026.** After the conversion, K–1 Problem 7 (page 6) now asks "Can two of your remaining trips use the same four roads?", the guide key (page 3) accepts "no" with the reason that the tiles differ, and the K–1 packet prints F39-K-v3. The other pages are unchanged in content. `review/card-fixes-2026-10-23.md` lists what changed, what was deferred and how it was checked; `review/verify_card_fixes_2026_10_23.py` checks it.

**Card shoulds, October 23, 2026.** Later the same day the card's remaining shoulds and coulds were made: the rules name "an out-and-back pair" and every problem uses it; the worked example is labelled with its routes; Grades 2–3 and 4–5 Problem 1 have answer lines; K–1 Problems 5–6, Grades 2–3 Problems 2 and 5 and Grades 4–5 Problems 4 and 6 are reworded or given new examples; the guide has one K–1 key, a first route per band, "n / 7" footers and no unprinted mat. Grades 2–3 and 4–5 now print v3 IDs. `review/card-shoulds-2026-10-23.md` lists the changes and checks; `review/verify_card_shoulds_2026_10_23.py` checks them.

This is an unpiloted theme library, not a fixed meeting schedule. Select a manageable first route in the guide and return for further investigations. Preserve the full Grades 4–5 material. Prerequisites, launch, materials, hints and theorem-first mathematical overview are in the separate adult guide. Physical fit, demonstrations and classroom timing have not been tested.

Current pages: **K–1 6; Grades 2–3 4; Grades 4–5 4; adult guide 7**. Print selected student pages single-sided on US Letter at Actual Size / 100%.

## Rebuild outside the project

Extract the complete ZIP. Install Python 3.11 or later with `requirements.txt`, a normal TeX Live distribution providing pdfLaTeX/TikZ/Helvetica, and Poppler's `pdftoppm` where used by the existing checks. Matching guide fonts and licenses are included; the root build selects package-local fonts in earlier packages. No project checkout or original workspace path is needed.

    python3 -m pip install -r requirements.txt
    python3 build.py
    python3 verify_revision.py
    python3 review/verify_card_fixes_2026_10_23.py
    python3 review/verify_card_shoulds_2026_10_23.py

The current verifier compares paper geometry and every 100-dpi rendered page against `reference-pdfs/`; timestamps may differ. It permits only specifically audited full-page font/hyphenation alternatives for unchanged student PDFs. See `review/fresh-review-rebuild.md` for actual results. The original strict verifier (`verify_rebuild.py` or `verify.py`) is retained and rejects those alternatives. The corpus report explicitly records any pre-existing small TeX font-metric differences for unchanged student bands; their current print/reference PDFs stay byte-identical. For Weeks 24 and 35, the detailed student-stage record is `review/student-reviser-fresh-review.md`. The corpus release report records those differences explicitly rather than calling them pixel-identical.

The October 4 K–1 reference was compiled with pdfTeX 1.40.27; under pdfTeX 1.40.25 its rebuild had identical text and drawings but slightly different glyph rasters. Since the October 23 card fixes, the K–1 reference is compiled with pdfTeX 1.40.25 (TeX Live 2023), like the other packets and the guide, and all four rebuild exactly there.

Edit student problems in `problem-files/problems/*.md` (figures in `problem-files/figures.py`); `src/build.sh` regenerates `src/*.tex` from them before compiling, so do not edit the TeX by hand. To build every view: `python3 problem-files/tools/build.py problem-files --out views --tables K-1=3,2-3=4,4-5=3`. The problem files also repeat the guide's answer keys, overview, hints and source for that key view; `python3 problem-files/check_guide_copy.py` confirms they still match `facilitator-src/content.json` and `route-note.json`. Edit the existing guide source under `facilitator-src/`. Where present, `facilitator-src/route-note.json` holds the concise starting/return update; the root build regenerates the guide before appending it exactly once. Do not run the appender alone against an already appended guide. Build intermediates belong in a separate working copy; inspect changed pages before updating references.

The current reference manifest is `review/reference-manifest.json`; revision evidence is `review/fresh-review-2026-10-04.md`. Older review files and `review/README-before-fresh-review-2026-10-04.md` describe their dated versions. Prior releases are archived outside the current package in the project.

## Use and rights

Original worksheet prose, diagrams and builders are provided for the organizer's use and adaptation. Preserve source attribution. Third-party books and articles retain their rights and are not redistributed here. Included fonts retain their licenses. No broader third-party license is implied. Routine adult reading or recording is allowed; children should retain the mathematical choices.
