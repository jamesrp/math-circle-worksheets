# Week 77: Persistent holes

A six-page shared Grades 4-5 prototype, F77-45-v4. Grade labels are approximate. The prerequisites are following short edge labels, keeping an earlier loop's edge list unchanged, matching physical triangle tiles to their complete boundaries, and cancelling identical token pairs with support. No separate younger-band editions are intended. The general explanation and final two-loop construction are readiness-dependent.

## Build

Requires Python 3.11+ (standard library only) and a working TeX Live installation with `pdflatex`, TikZ/PGF, geometry, fancyhdr, and Computer Modern fonts. No network access or downloaded reference is used during building.

```sh
python3 check_math.py
python3 build.py --out /path/to/output
```

The source is the problem files (`../problem-files/` in the portable ZIP, `lowell-math-circle-year-2/source/week-77/` in the repository); `build.py` first runs `regenerate.py`, which writes `students.tex` from them. Edit the problem files, not `students.tex`. The builder runs the finite checks and creates `students.pdf` and a diagnostic `build.log` in the requested directory. It fails on TeX errors or overfull boxes. It uses a temporary build directory inside `--out`, then removes that directory. On minimal TeX images lacking an initialized format, it discovers installed package trees read-only and builds a private format inside that temporary directory; it does not modify the system or home TeX cache. Poppler's `pdftoppm` and `pdfinfo` are useful for independent output inspection but are not build dependencies.

## Print and materials

Print single-sided on US Letter at 100%, without fit-to-page. Square sides are 6.2 cm. The joined-triangle board is 11.6 cm wide and 5.8 cm high; its triangles meet only at the printed dot C. The page 6 square has 8 cm sides, with a center vertex O; its four triangular interiors do not overlap.

Print `week-77-materials.pdf` (F77-M-v1, two pages) at 100%. Page 1 has the tiles at board scale, each with its name, its board and each edge's name along that side: ABC/ACD for the square, ABC/CDE for the joined board, ABO/BCO/CDO/DAO for the center-vertex square, and the small XYZ launch tile; keep the three board sets separate. Page 1 also has seven labelled edge strips (the square's four sides and diagonal, the joined board's AB and DE). The page 6 diagram is deliberately unfilled: use removable tiles for its partly filled start, and remove them only when resetting to the new build with no filled triangles. Page 2 has stage cards 0, 2, 3, 4, 5, 8 with two blanks, and three tokens each for AB, BC, CD, DA, AC, CE, DE, AO, BO, CO, DO. This suffices when testing one saved loop at a time. For the printed launch demonstration it also has two XY tokens, two YZ tokens, and two XZ tokens; the shaded printed triangle shows that XYZ is filled. AD and DA denote the same edge. Pencil and two colors suffice for saved edge lists and schedules. A reset starts a new build; pieces do not disappear within a build.

Only student pages are included. This is a revised prototype, not an approved classroom release. Digital mathematics and rendering checks do not establish physical readiness. Tile preparation, edge-marker fit, handling, pacing, and children's command of the recording rule remain untested. A pair can work with the third child checking legal additions and rotating roles. The six pages need not all be completed in one meeting.

## Contents and provenance

- `students.tex`: the LaTeX/TikZ student pages and diagrams, written by `regenerate.py` from the problem files.
- `regenerate.py`: writes `students.tex` from the problem files.
- `build.py`: portable standard-library builder.
- `check_math.py`: exhaustive cycle/boundary tests, all stated finite schedules, independent inclusion-map rank checks, and all 24 filling orders on the final four-triangle board. The final board also has a separate integer-bitmask verification that uses its eight explicitly listed edge positions rather than the earlier chain routines.
- `README.md`: dependencies, prerequisites, and limits.

The teaching instances and diagrams are independently devised. Background: H. Edelsbrunner, D. Letscher, A. Zomorodian, *Topological Persistence and Simplification*, sections 2-3, https://pub.ista.ac.at/~edels/Papers/2002-J-04-TopologicalPersistence.pdf. No source paper, borrowed problem text, images, workflow prompts, or generated environment files are included in this portable source set. The run's separate research note records exact source locations and the independently checked algebra.
