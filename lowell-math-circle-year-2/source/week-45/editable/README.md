# Week 45 The visible side editable source

## Current release: October 4, 2026 fresh-review revision

The guide now gives first routes, readiness-dependent continuation and return visits; original mathematical investigations are retained.

**Problem files, October 23, 2026.** The student pages are now stored as problem files, one per problem with its band variants, in `problem-files/` (in the repository: `lowell-math-circle-year-2/source/week-45/`). The conversion changed no wording or figure. `src/regenerate.py` writes the student LaTeX from them, and `problem-files/tools/build.py` also builds first-route and return packets and a one-page problem menu. The answer keys stay in the guide.

**Card fixes, October 23, 2026.** After the conversion the review card's shoulds 1–7 and coulds 10–13 were made: all three packets (now v3) and the guide (now 9 pages, with a hint and an extension for every problem and a 35–40 minute plan) changed. `review/verify_card_shoulds_2026_10_23.py` checks every changed claim, key and extension answer against `reference-pdfs/`; the source README in the repository lists what changed and what was deferred.

**Critic follow-up, October 23, 2026 (v4).** An independent critic noted that the student pages still broke words across lines ("keep-ing", "cer-tain", "some-times", "when-ever"), since `figures.py` protected only "better" and "differ", and that K–1 Problem 4 said "this chooser" under a rule line that says "Only tickets 1 and 3 are in the cup". Hyphenation is now off on the student pages (`\hyphenpenalty=10000` in `figures.py`'s page preamble, as Week 40 does) and K–1 Problem 4 says "Add just one extra ticket to this cup". Wording is otherwise unchanged; the reflowed pages are K–1 p. 3, Grades 2–3 pp. 3–4 and Grades 4–5 p. 4, and every packet moves to v4 (W45-k-1-v4, W45-grades-2-3-v4, W45-grades-4-5-v4). The guide did not change. `review/verify_card_shoulds_2026_10_23.py` now checks the v4 footers.

This is an unpiloted theme library, not a fixed meeting schedule. Select a manageable first route in the guide and return for further investigations. Preserve the full Grades 4–5 material. Prerequisites, launch, materials, hints and theorem-first mathematical overview are in the separate adult guide. Physical fit, demonstrations and classroom timing have not been tested.

Current pages: **K–1 4; Grades 2–3 4; Grades 4–5 4; adult guide 9**. Print selected student pages single-sided on US Letter at Actual Size / 100%.

## Rebuild outside the project

Extract the complete ZIP. Install Python 3.11 or later with `requirements.txt`, a normal TeX Live distribution providing pdfLaTeX/TikZ/Helvetica, and Poppler's `pdftoppm` where used by the existing checks. Matching guide fonts and licenses are included; the root build selects package-local fonts in earlier packages. No project checkout or original workspace path is needed.

    python3 -m pip install -r requirements.txt
    python3 build.py
    python3 verify_revision.py
    python3 review/verify_card_shoulds_2026_10_23.py

The current verifier compares paper geometry and every 100-dpi rendered page against `reference-pdfs/`; timestamps may differ. It permits only specifically audited full-page font/hyphenation alternatives for unchanged student PDFs. See `review/fresh-review-rebuild.md` for actual results. The original strict verifier (`verify_rebuild.py` or `verify.py`) is retained and rejects those alternatives. The corpus report explicitly records any pre-existing small TeX font-metric differences for unchanged student bands; their current print/reference PDFs stay byte-identical. For Weeks 24 and 35, the detailed student-stage record is `review/student-reviser-fresh-review.md`. The corpus release report records those differences explicitly rather than calling them pixel-identical.

Edit student problems in `problem-files/problems/*.md` (figures in `problem-files/figures.py`); `src/build.sh` regenerates `src/*.tex` from them before compiling, so do not edit the TeX by hand. To build every view: `python3 problem-files/tools/build.py problem-files --out views`. Edit the existing guide source under `facilitator-src/`. Where present, `facilitator-src/route-note.json` holds the concise starting/return update; the root build regenerates the guide before appending it exactly once. Do not run the appender alone against an already appended guide. Build intermediates belong in a separate working copy; inspect changed pages before updating references.

The current reference manifest is `review/reference-manifest.json`; revision evidence is `review/fresh-review-2026-10-04.md`. Older review files and `review/README-before-fresh-review-2026-10-04.md` describe their dated versions. Prior releases are archived outside the current package in the project.

## Use and rights

Original worksheet prose, diagrams and builders are provided for the organizer's use and adaptation. Preserve source attribution. Third-party books and articles retain their rights and are not redistributed here. Included fonts retain their licenses. No broader third-party license is implied. Routine adult reading or recording is allowed; children should retain the mathematical choices.
