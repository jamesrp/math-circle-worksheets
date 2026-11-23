# Week 106 source: coloring maps

Problem files for Week 106 (coloring maps), in the two print levels, K–1 and grades 2–5. The pages were written through the worksheet workflow on November 20, 2026 as a December 2 option; James chose them for December 2 on November 22. Run notes, the five reviews and the outline are in [plans/drafts/weeks-101-plus/week-106-pages/](../../../plans/drafts/weeks-101-plus/week-106-pages/README.md). There is no adult guide: the answers, the games' outcomes and the opener are in the [December 2 room plan](../../../plans/room-plans/2026-12-02-map-coloring.md). Unpiloted.

- `week.toml`, `problems/`: the packets (flow layout, one template per band: `template-k-1.tex`, `template-2-5.tex`).
- `src/common.tex`: the shared preamble. `src/figs/`: every map, written by `src/figs.py`, which also checks each map's color count.
- `src/game.py`: plays every line of the Painter and Spoiler games on the strip, pond and tic-tac-toe maps. `src/check_torus7.py`: checks that the seven donut countries of 2–5 Problem 14 each border all six others. `src/mksheet.py`: a contact sheet of the figures.

Build and check (from the repository root):

```sh
(cd lowell-math-circle-year-2/source/week-106/src && python3 figs.py && python3 game.py && python3 check_torus7.py)
python3 lowell-math-circle-year-2/source/problem-files/build.py lowell-math-circle-year-2/source/week-106 --out tmp/week-106-views
cp tmp/week-106-views/k-1.pdf lowell-math-circle-year-2/week-106/week-106-k-1.pdf
cp tmp/week-106-views/grades-2-5.pdf lowell-math-circle-year-2/week-106/week-106-grades-2-5.pdf
```

`figs.py` is only needed when a figure changes.
