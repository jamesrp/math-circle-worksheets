# Week 34 Hidden turns editable source

## Current release: November 6, 2026 kid-fit revision (v4)

**Kid-fit revision, November 6, 2026.** The student pages were revised after a kid-fit review and James approved adopting them on November 6, 2026: the shared rules say how to copy (a dot of each counter's colour) and make testing a builder-against-tester game, K-1 has shorter rules, K-1 Problem 3 gets its own page with a printed start, K-1 Problem 6 asks for one eight-ring pattern, Problem 4 in Grades 2-3 and 4-5 asks for an explanation instead of a list of moves, and Grades 4-5 get open answer boxes. Problem numbering is unchanged. The guide keys the new pages, says that each changed pattern needs a copy before testing (an adult may make slow K-1 copies) and that K-1 Problem 1 is always won by the tester. Ids: W34-k-1-v4, W34-grades-2-3-v4, W34-grades-4-5-v4; guide footer "Student packet v4 / Revised November 6 2026". Unpiloted.

### Previous release: October 23, 2026 card fixes (v3)

The review card's shoulds and clear coulds: a flip panel with a drawn axis in the page-1 example, one goal phrase ("a pattern that no turn or flip can match"), "neighbors may be the same kind" in the rules, a Grades 4-5 workspace page with a seven-ring and a nine-ring, and a guide that says how to make a coloured tracing copy, makes one in the launch, plans eleven children and keys the kind swap and the odd rings. Unpiloted.

The October 4 fresh-review revision gave the guide first routes, readiness-dependent continuation and return visits; original mathematical investigations are retained.

This is an unpiloted theme library, not a fixed meeting schedule. Select a manageable first route in the guide and return for further investigations. Preserve the full Grades 4–5 material. Prerequisites, launch, materials, hints and theorem-first mathematical overview are in the separate adult guide. Physical fit, demonstrations and classroom timing have not been tested.

Current pages: **K–1 6; Grades 2–3 5; Grades 4–5 6 (the sixth is extra workspace); adult guide 6**. Print selected student pages single-sided on US Letter at Actual Size / 100%.

## Rebuild outside the project

Extract the complete ZIP. Install Python 3 with `requirements.txt`, a normal TeX Live distribution providing pdfLaTeX/TikZ/Helvetica, and Poppler's `pdftoppm` where used by the existing checks. Matching guide fonts and licenses are included; the root build selects package-local fonts in earlier packages. No project checkout or original workspace path is needed.

    python3 -m pip install -r requirements.txt
    python3 build.py
    python3 verify_revision.py

The current verifier compares paper geometry and every 100-dpi rendered page against `reference-pdfs/`; timestamps may differ. Since the November 6 kid-fit revision changed every student packet and the guide, it permits no alternatives (`review/rebuild-pixel-allowances.json` is empty). See `review/fresh-review-rebuild.md` for actual results. The original strict verifier (`verify_rebuild.py` or `verify.py`) is retained and rejects those alternatives. The corpus report explicitly records any pre-existing small TeX font-metric differences for unchanged student bands; their current print/reference PDFs stay byte-identical. For Weeks 24 and 35, the detailed student-stage record is `review/student-reviser-fresh-review.md`. The corpus release report records those differences explicitly rather than calling them pixel-identical.

**Problem files, October 23, 2026.** The student pages are stored as problem files: in this ZIP `problem-files/` (with `week.toml`, `figures.py`, `problems/` and the tools in `problem-files/tools/`), in the repository `lowell-math-circle-year-2/source/week-34/`. `src/regenerate.py` writes the band LaTeX from them and `src/build.sh` runs it before compiling; edit the problem files, not the generated `.tex`. Python 3.11+ is needed for `tomllib`.

Edit the guide source under `facilitator-src/`. Where present, `facilitator-src/route-note.json` holds the concise starting/return update; the root build regenerates the guide before appending it exactly once. Do not run the appender alone against an already appended guide. Build intermediates belong in a separate working copy; inspect changed pages before updating references.

The current reference manifest is `review/reference-manifest.json`; revision evidence is `review/fresh-review-2026-10-04.md`. Older review files and `review/README-before-fresh-review-2026-10-04.md` describe their dated versions. Prior releases are archived outside the current package in the project.

## Use and rights

Original worksheet prose, diagrams and builders are provided for the organizer's use and adaptation. Preserve source attribution. Third-party books and articles retain their rights and are not redistributed here. Included fonts retain their licenses. No broader third-party license is implied. Routine adult reading or recording is allowed; children should retain the mathematical choices.
