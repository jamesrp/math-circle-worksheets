# Catalan bijections: Week 12 editable release

## Current release: October 23, 2026 card fixes

**Guide corrections.** The adult guide carries the corrections from its review card: the K–1 Problem 4 duplicate hint (p. 4), the K–1 timing order (p. 3) and the Grades 2–3 return-visit line (p. 10) are corrected, and the preparation (p. 2) asks for strings about 20 cm long instead of 40 cm, a length measured from the printed boards but not yet rehearsed. See `review/card-fixes-2026-10-23.md`.

**Problem files.** The student pages are now stored as problem files, one per problem, in `problem-files/` (in the repository: `lowell-math-circle-year-2/source/week-12/`). The conversion changed no wording or figure. `src/regenerate.py` writes the student LaTeX from them, `src/check_catalan.py` runs the old builder's mathematical checks, and `problem-files/tools/build.py` also builds first-route and return packets, a one-page problem menu and a key arranged by problem.

**Student-page fixes.** After the conversion: K–1 Problem 3 prints every drawn pair twice (eight frames), so the page no longer shows which starts can be finished, and its prompt says to leave a string on the drawn pair; K–1 Problem 4 continues on a new page 5 with ten more frames (16 for the 14 pairings) and no longer sends children to blank paper; the K–1 mats on pages 2–4 and 6 sit a little higher, clear of the frame labels; Grades 4–5 page 2 drops "Numbers show the walk order." Only K–1 pages 2–7, Grades 4–5 page 2 and guide pages 1 and 4 changed; the Grades 2–3 packet is unchanged. See `review/card-fixes-2026-10-23.md`, checked by `review/verify_card_fixes_2026_10_23.py` and `review/verify_student_fixes_2026_10_23.py`.

**Partner lists.** Later on October 23 the guide's page 7 gallery began printing each eight-dot code's partner list, as page 3 does for six dots. No other page changed.

The October 4 revision gave the guide first routes, readiness-dependent continuation and return visits; original mathematical investigations are retained.

This is an unpiloted theme library, not a fixed meeting schedule. Select a manageable first route in the guide and return for further investigations. Preserve the full Grades 4–5 material. Prerequisites, launch, materials, hints and theorem-first mathematical overview are in the separate adult guide. Physical fit, demonstrations and classroom timing have not been tested.

Current pages: **K–1 7; Grades 2–3 6; Grades 4–5 6; adult guide 10**. Print selected student pages single-sided on US Letter at Actual Size / 100%.

## Rebuild outside the project

Extract the complete ZIP. Install Python 3.11 or later with `requirements.txt`, a normal TeX Live distribution providing pdfLaTeX/TikZ/Helvetica, and Poppler's `pdftoppm` where used by the existing checks. Matching guide fonts and licenses are included; the root build selects package-local fonts in earlier packages. No project checkout or original workspace path is needed.

    python3 -m pip install -r requirements.txt
    bash build.sh
    python3 verify_revision.py
    python3 review/verify_student_fixes_2026_10_23.py

The current verifier compares paper geometry and every 100-dpi rendered page against `reference-pdfs/`; timestamps may differ. It permits only specifically audited full-page font/hyphenation alternatives for unchanged student PDFs. See `review/fresh-review-rebuild.md` for actual results. The original strict verifier (`verify_rebuild.py` or `verify.py`) is retained and rejects those alternatives. The corpus report explicitly records any pre-existing small TeX font-metric differences for unchanged student bands; their current print/reference PDFs stay byte-identical. For Weeks 24 and 35, the detailed student-stage record is `review/student-reviser-fresh-review.md`. The corpus release report records those differences explicitly rather than calling them pixel-identical.

Edit student problems in `problem-files/problems/*.md` (figures and the page template in `problem-files/figures.py`); `build.sh` regenerates `src/*.tex` from them and reruns `src/check_catalan.py` before compiling, so do not edit the TeX by hand. To build every view: `python3 problem-files/tools/build.py problem-files --out views`. Each problem file's key repeats the main answer from the guide, and `problem-files/guide/overview.tex` repeats the guide's first page; `python3 problem-files/check_guide_copy.py` confirms every copied sentence is still in `facilitator-src/build_guide.py`. Edit the existing guide source under `facilitator-src/`. Where present, `facilitator-src/route-note.json` holds the concise starting/return update; the root build regenerates the guide before appending it exactly once. Do not run the appender alone against an already appended guide. Build intermediates belong in a separate working copy; inspect changed pages before updating references.

The current reference manifest is `review/reference-manifest.json`; revision evidence is `review/fresh-review-2026-10-04.md` and, for the October 23 card fixes, `review/card-fixes-2026-10-23.md` with its checks `review/verify_card_fixes_2026_10_23.py` and `review/verify_student_fixes_2026_10_23.py`. Older review files and `review/README-before-fresh-review-2026-10-04.md` describe their dated versions. Prior releases are archived outside the current package in the project.

## Use and rights

Original worksheet prose, diagrams and builders are provided for the organizer's use and adaptation. Preserve source attribution. Third-party books and articles retain their rights and are not redistributed here. Included fonts retain their licenses. No broader third-party license is implied. Routine adult reading or recording is allowed; children should retain the mathematical choices.
