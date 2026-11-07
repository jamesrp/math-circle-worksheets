# Nontransitive dice and decks: Week 24 editable release

## Current release: November 7, 2026 adult-read fix of the November 6 kid-fit revision

**Adult-read fix, November 7, 2026.** An adult cold-read pilot (`plans/review/ADULT-READ-PILOT.md`) found that a parent volunteer reading the pages alone could not tell what Problem 1 was in any band: K–1 page 1 named bags, decks and games before any page showed what was in a deck, and the Grades 2–3 and 4–5 First pick / Second pick table did not say what to record. James approved a fix the same day. The shared rules now say "Decks A, B and C are bags of three number cards, shown below" and every band's page 1 pictures the three decks (K–1 as dot cards in a row above Problem 1's game); K–1 Problem 1 says to play with a partner and names the three games; the pick-first table's first row is a shaded example, "A, 4 wins" and "C, 6 wins" (a first try, "A 4, C 6", was read by a fresh adult reader as card values). Only page 1 of each band changed; problem numbering is unchanged. Packets F24-K-v5 (9 pages), F24-23-v4 (8) and F24-45-v5 (8); the guide's page 2 names them. Unpiloted.

**Kid-fit revision, November 6, 2026.** The student pages were revised by a kid-fit pilot and adopted as approved by James on November 6, 2026: F24-K-v4 (9 pages), F24-23-v3 (8) and F24-45-v4 (8). Every band opens with a new short game as Problem 1 and the other problems moved down one; K–1 adds ten-frame dot cards, a cycle triangle, a chosen-deck box and a swap grid; Grades 2–3 P3 becomes a hidden-bag guessing game and P6 adds the four-card decks; Grades 4–5 P5 is shortened. The guide, dated 2026-11-06 (16 pages), adds page 3 on what a short game cannot show (the favored deck wins a 6-round game outright about 45% of the time and a 10-round game about 52%; the cycle shows by counting all the card pairs), renumbers every problem and page reference, keys the new and rewritten problems and updates the materials (small counters, Grades 2–3 hidden-bag letter slips). Unpiloted. See `review/kid-fit-2026-11-06.md`; `python3 review/verify_kid_fit_2026_11_06.py` checks the built PDFs and the mathematics.

## Earlier releases

**Critic follow-up, October 23, 2026 (guide only).** The guide's card list (p. 1) adds a 0 card for Grades 2–3 Problem 4 (58 cards) and has the spares written in soft pencil, so they can be erased and rewritten for Grades 4–5 Problem 3, whose decks may repeat a value three times. The student packets are unchanged.

**Card fixes, October 23, 2026.** Every should and could of the review card was done after the problem-file conversion below: student packets F24-K-v3 (K–1 Problems 1–4 and 6 reworded) and F24-45-v3 (Problem 1's decks lowered), Grades 2–3 unchanged at F24-23-v2, and guide pages 1–4, 7, 10, 13, the overview and the route page. See `review/card-fixes-2026-10-23.md`; `review/verify_card_fixes_2026_10_23.py` checked each fix against that release's PDFs (it does not pass on the current release). The release before it was the October 4, 2026 fresh-review revision.

**Problem files, October 23, 2026.** The student pages are now stored as problem files, one per problem, in `problem-files/` (in the repository: `lowell-math-circle-year-2/source/week-24/`). The conversion changed no wording or figure. `src/regenerate.py` writes the student LaTeX from them, `src/check_answers.py` still checks the answers, and `problem-files/tools/build.py` also builds first-route and return packets, a one-page problem menu and a key arranged by problem.

The guide now gives first routes, readiness-dependent continuation and return visits; original mathematical investigations are retained. K–1 shares the pictured pair comparisons among children and pools one nine-case page per deck comparison; all original tasks and older student bands remain.

This is an unpiloted theme library, not a fixed meeting schedule. Select a manageable first route in the guide and return for further investigations. Preserve the full Grades 4–5 material. Prerequisites, launch, materials, hints and theorem-first mathematical overview are in the separate adult guide. Physical fit, demonstrations and classroom timing have not been tested.

Current pages: **K–1 9; Grades 2–3 8; Grades 4–5 8; adult guide 16**. Print selected student pages single-sided on US Letter at Actual Size / 100%.

## Rebuild outside the project

Extract the complete ZIP. Install Python 3 with `requirements.txt`, a normal TeX Live distribution providing pdfLaTeX/TikZ/Helvetica, and Poppler's `pdftoppm` where used by the existing checks. Matching guide fonts and licenses are included; the root build selects package-local fonts in earlier packages. No project checkout or original workspace path is needed.

    python3 -m pip install -r requirements.txt
    bash build.sh
    python3 verify_revision.py

The current verifier compares paper geometry and every 100-dpi rendered page against `reference-pdfs/`; timestamps may differ. It permits only specifically audited full-page font/hyphenation alternatives for unchanged student PDFs; since the November 6 revision changed every packet, none are listed. `verify_revision.py` needs PyMuPDF; `verify_rebuild.py` needs only pypdf and Poppler. See `review/fresh-review-rebuild.md` for actual results. The original strict verifier (`verify_rebuild.py` or `verify.py`) is retained and rejects those alternatives. The corpus report explicitly records any pre-existing small TeX font-metric differences for unchanged student bands; their current print/reference PDFs stay byte-identical. For Weeks 24 and 35, the detailed student-stage record is `review/student-reviser-fresh-review.md`. The corpus release report records those differences explicitly rather than calling them pixel-identical.

Edit student problems in `problem-files/problems/*.md` (figures and the page template in `problem-files/figures.py`); `build.sh` regenerates `src/*.tex` from them before compiling, so do not edit the TeX by hand. To build every view: `python3 problem-files/tools/build.py problem-files --out views`. Edit the existing guide source under `facilitator-src/`. Where present, `facilitator-src/route-note.json` holds the concise starting/return update; the root build regenerates the guide before appending it exactly once. Do not run the appender alone against an already appended guide. Build intermediates belong in a separate working copy; inspect changed pages before updating references.

The current reference manifest is `review/reference-manifest.json`; revision evidence is `review/kid-fit-2026-11-06.md` (and, for earlier releases, `review/card-fixes-2026-10-23.md` and `review/fresh-review-2026-10-04.md`). Older review files and `review/README-before-fresh-review-2026-10-04.md` describe their dated versions. Prior releases are archived outside the current package in the project.

## Use and rights

Original worksheet prose, diagrams and builders are provided for the organizer's use and adaptation. Preserve source attribution. Third-party books and articles retain their rights and are not redistributed here. Included fonts retain their licenses. No broader third-party license is implied. Routine adult reading or recording is allowed; children should retain the mathematical choices.
