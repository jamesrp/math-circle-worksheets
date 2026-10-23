# Discrete tomography and hidden pictures: Week 25 editable release

## Current release: October 23, 2026 card fixes

The adult guide carries the corrections from its review card: the Grades 2–3 lower-bound held hint now accepts the counter-counting argument (p. 11), supplies are 24 counters per table (p. 1; 15–16 mm wide since Critic J's could, the same day), and the launch uses a one-picture example (p. 2). Later the same day the student pages, stored as problem files, got the card's student-page fixes: a clearer p. 1 rule in every band, continuing pages headed "Problem N (continued)", grades 2–3 renumbered P1–P6 with a recorded switch, spare grids in grades 4–5 P1 and P3, a new grades 4–5 workspace page for P4, and the card's K–1 P6 wording. Then two small coulds: the grid rows of K–1 p. 2, Grades 2–3 pp. 1 and 5 and Grades 4–5 p. 3 are spaced so that circled counts no longer crowd the next grid's labels (Grades 4–5 p. 3 now has Problem 1's 18.5 mm cells), and the guide's overview and p. 1 carry the student headers' theme name, "Row and column shadows". See `review/card-fixes-2026-10-23.md`.

**Problem files.** The student pages are now stored as problem files, one per problem, in `problem-files/` (in the repository: `lowell-math-circle-year-2/source/week-25/`). The conversion changed no wording or figure. `src/regenerate.py` writes the student LaTeX from them, `src/check_answers.py` runs the old builder's exhaustive checks of every printed set of counts (writing `src/answer-checks.json`), and `problem-files/tools/build.py` also builds first-route and return packets, a one-page problem menu and a key arranged by problem.

The October 4 revision gave the guide first routes, readiness-dependent continuation and return visits; original mathematical investigations are retained.

This is an unpiloted theme library, not a fixed meeting schedule. Select a manageable first route in the guide and return for further investigations. Preserve the full Grades 4–5 material. Prerequisites, launch, materials, hints and theorem-first mathematical overview are in the separate adult guide. Physical fit, demonstrations and classroom timing have not been tested.

Current pages: **K–1 8; Grades 2–3 6; Grades 4–5 8; adult guide 20**. Print selected student pages single-sided on US Letter at Actual Size / 100%.

## Rebuild outside the project

Extract the complete ZIP. Install Python 3 with `requirements.txt`, a normal TeX Live distribution providing pdfLaTeX/TikZ/Helvetica, and Poppler's `pdftoppm` where used by the existing checks. Matching guide fonts and licenses are included; the root build selects package-local fonts in earlier packages. No project checkout or original workspace path is needed.

    python3 -m pip install -r requirements.txt
    bash build.sh
    python3 verify_revision.py

The current verifier compares paper geometry and every 100-dpi rendered page against `reference-pdfs/`; timestamps may differ. It permits only specifically audited full-page font/hyphenation alternatives for unchanged student PDFs. See `review/fresh-review-rebuild.md` for actual results. The original strict verifier (`verify_rebuild.py` or `verify.py`) is retained and rejects those alternatives. The corpus report explicitly records any pre-existing small TeX font-metric differences for unchanged student bands; their current print/reference PDFs stay byte-identical. For Weeks 24 and 35, the detailed student-stage record is `review/student-reviser-fresh-review.md`. The corpus release report records those differences explicitly rather than calling them pixel-identical.

Edit student problems in `problem-files/problems/*.md` (figures and the page template in `problem-files/figures.py`); `build.sh` regenerates `src/*.tex` from them and reruns `src/check_answers.py` and `src/check_examples.py` before compiling, so do not edit the TeX by hand. To build every view: `python3 problem-files/tools/build.py problem-files --out views`. Each problem file's key repeats the main answer from the guide, and `problem-files/guide/overview.tex` repeats the guide's overview; `python3 problem-files/check_guide_copy.py` confirms every copied sentence is still in `facilitator-src/build_guide.py` or `overview-content.json`. Edit the existing guide source under `facilitator-src/`. Where present, `facilitator-src/route-note.json` holds the concise starting/return update; the root build regenerates the guide before appending it exactly once. Do not run the appender alone against an already appended guide. Build intermediates belong in a separate working copy; inspect changed pages before updating references.

The current reference manifest is `review/reference-manifest.json`; revision evidence is `review/fresh-review-2026-10-04.md` and, for the October 23 card fixes, `review/card-fixes-2026-10-23.md` with its checks `review/verify_card_fixes_2026_10_23.py` (guide) and `review/verify_student_fixes_2026_10_23.py` (student pages), and `review/verify_small_coulds_2026_10_23.py` for the small coulds. Older review files and `review/README-before-fresh-review-2026-10-04.md` describe their dated versions. Prior releases are archived outside the current package in the project.

## Use and rights

Original worksheet prose, diagrams and builders are provided for the organizer's use and adaptation. Preserve source attribution. Third-party books and articles retain their rights and are not redistributed here. Included fonts retain their licenses. No broader third-party license is implied. Routine adult reading or recording is allowed; children should retain the mathematical choices.
