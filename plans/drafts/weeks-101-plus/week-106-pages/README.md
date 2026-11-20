# Week 106 pages (coloring maps): workflow run, November 20, 2026

Student pages for K–1 and grades 2–5, written as a December 2, 2026 option at James's ask ("Build both map coloring and stars/wheels and I'll compare", November 20). Not approved and unpiloted, so they live here and in the room plan, not in `lowell-math-circle-year-2/`.

- Print PDFs: [K–1](../../../room-plans/2026-12-02-map-coloring-k-1.pdf) (12 pages), [grades 2–5](../../../room-plans/2026-12-02-map-coloring-grades-2-5.pdf) (12 pages). Room plan: [2026-12-02-map-coloring.md](../../../room-plans/2026-12-02-map-coloring.md).
- Outline: [worksheet-workflow/outlines/week-106-coloring-maps.md](../../../../worksheet-workflow/outlines/week-106-coloring-maps.md). The run used the two-level default (first two-level run of the workflow): writer, adversarial review, math check, kid-fit review, adult cold read, reviser, second adult read. Reviews are in `reviews/`.
- Results: every map count, game outcome and the seven-country donut map (21 bordering pairs) checked by code in two independent passes; kid-fit rated both activities strong and both pages workable; the second adult read found nothing blocking.
- After the second adult read, Claude made four wording fixes it suggested: 2–5 Problem 4 (the space outside the ring is not a country), 2–5 Problem 13 (what a piece of a country is), K–1 Problem 3 (loops that cross each other), K–1 Problem 4 (use more pencils if you need them). Not done: asking separately who wins with each player first in 2–5 Problems 6–7 (on the 3-by-3 board the answer is the same either way).
- Rebuild: in `src/`, run `python3 figs.py` if figures change, then `pdflatex k-1.tex` and `pdflatex grades-2-5.tex` (twice). `check_torus7.py` and `game.py` re-check the donut map and the games.
- If James chooses this week, convert it to problem files under `lowell-math-circle-year-2/` as AGENTS.md says and add its catalog record.
