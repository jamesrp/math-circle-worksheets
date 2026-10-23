# Week 78: Three-armed lines

One shared Grades 4–5 prototype: 5 student pages and a separate 4-page theorem-first adult guide. Independently reviewed and digitally checked; organizer-approved and promoted October 17, 2026 (v2), and revised from its review card on October 23 (v3), after that approval. The week number is a library identifier, not an adopted schedule. Physical preparation/handling and classroom piloting remain unperformed.

## Review-card fixes, October 23, 2026

These fixes post-date the organizer's October 17 approval of v2; the activity is the same seven problems on the same five pages. From the keep card (`plans/review/week-78.md`), all four shoulds and coulds 5, 6 and 9 are done (student packet F78-S-v3, guide F78-FAC-v3):

- Problem 5 asks only "Find all possible junctions of a line through each pair of points."; the guide's second hint now says a whole stretch of junctions can be the answer.
- Problems 2 and 4 open with (2,6) and (6,2), a falling diagonal: in Problem 2 the lines meet only at (6,6), and in Problem 4 the junction is still (2,2). The guide's Problem 3 explanation says "same row, column or rising diagonal".
- Problem 3 has a blank 0–8 board. Page 1 marks the off-line point Q with a cross, since open circles are targets later.
- The guide makes one traced three-arm shape per pair standard: it is made in preparation, used in the launch and named in Problem 4's first hint.
- The guide adds an adult-led younger entry on student page 4, for K–1 or Grades 2–3, with a plain-words key. It is a prediction and untested.

`checks/check_card_fixes.py` checks every changed claim and runs with the other checks. Left: could 7 (giving Problem 6's rule its own number would renumber the approved packet and the guide), could 8 (a new late problem on the min rule adds substance), and the second half of should 2. The organizer's October 15 revision deliberately made page 1 and Problem 1 ask for a single-point meeting and a whole-stretch overlap, so that wording is his call. The replaced PDFs are in [../../week-78/archive-before-card-fixes-2026-10-23/](../../week-78/archive-before-card-fixes-2026-10-23/README.md) and the replaced ZIP in [archive-before-card-fixes-2026-10-23/](archive-before-card-fixes-2026-10-23/README.md).

## Problem files, October 23, 2026

The student pages are stored as [problem files](../problem-files/README.md): `week.toml`, `template.tex` (the old preamble), `figures.py` (the boards, drawn from `student/data.py`, which both checkers read) and one file per problem in `problems/`, with the opening page as `problems/00-intro.md`. `student/regenerate.py` writes `student/students.tex` from them, and `student/build.py` runs it first; edit the problem files, not the generated LaTeX. The conversion changed no wording or figure: the rebuilt packet has the same pages, text and 100-dpi pixels as `week-78-students.pdf`. The ZIP holds the tools in `tools/`. The hand-written LaTeX, the old builder and the ZIP they came from are in [archive-before-problem-files-2026-10-23/](archive-before-problem-files-2026-10-23/README.md).

    python3 lowell-math-circle-year-2/source/problem-files/build.py lowell-math-circle-year-2/source/week-78 --out tmp/week-78-views --tex
    python3 lowell-math-circle-year-2/source/problem-files/package.py lowell-math-circle-year-2/source/week-78 --flat --zip week-78-source.zip --top week-78

The published band views stay the slices in [band-views/](../../band-views/README.md); the problem-file menu, key and route packets stay in `tmp/`.

## Rebuild from this package

Use Python 3 and normal TeX Live/MacTeX with pdfLaTeX, TikZ/PGF, Computer Modern/Latin Modern, geometry, fancyhdr, AMS packages and the small standard packages listed in the student/guide READMEs. No network, repository files, private reference, external artwork or custom Python library is required.

    python3 build.py --out output
    python3 build.py --verify-only

The first command reconstructs both named PDFs in the chosen output directory; the second runs independent, student and guide checks without TeX. Build intermediates are isolated. Edit the problem files (student pages), student/data.py (board coordinates) and guide/facilitator.tex, then rebuild. All required authored inputs are packaged.

## Readiness and use

Print single-sided US Letter at 100% / Actual Size. Read student/README.md for reading, arithmetic, spatial and recording prerequisites, and the adult guide for exact materials, a short shared launch, hints, solutions and sensible stopping points. The approximate grade range is not a classroom-readiness guarantee. No K–1 edition is implied, and completing every page is not the goal.

MATHEMATICS.md records precise hypotheses and general arguments. SOURCES.md separates mathematical lineage from independently authored examples. The repository's plans/frontier-prototypes-76-78/week-78/ record preserves reviews, revision decisions, final checks and the actual extracted-ZIP reconstruction result. Different TeX/font versions can affect appearance.

The portable ZIP excludes stage prompts, borrowed style examples, downloaded books/papers, external fonts, runtime format files, caches, render images, logs, superseded drafts and private classroom information.

## October 15 introduction revision

Preserved the minimum-tie definition and added a completed two-colour crossing. Problem 1 now explicitly asks for a single-point meeting and a whole-stretch overlap. All seven investigations remain; student task pages are now 2–5. This organizer-directed revision is unpiloted.

Organizer promotion: October 17, 2026, after review of the current packet. The student and facilitator PDFs are unchanged. Unpiloted; physical preparation, timing and classroom procedures remain untested.
