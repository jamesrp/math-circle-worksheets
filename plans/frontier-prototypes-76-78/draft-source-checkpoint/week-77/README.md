# Week 77: Persistent holes

A four-page shared Grades 4-5 prototype, F77-45-v1. Grade labels are approximate. The prerequisites are following short edge labels, keeping an earlier loop's edge list unchanged, matching physical triangle tiles to their complete boundaries, and cancelling identical token pairs with support. No separate younger-band editions are intended. The last explanation is readiness-dependent.

## Build

Requires Python 3 (standard library only) and a working TeX Live installation with `pdflatex`, TikZ/PGF, geometry, fancyhdr, and Computer Modern fonts. No network access or downloaded reference is used during building.

```sh
python3 check_math.py
python3 build.py --out /path/to/output
```

The builder runs the finite checks and creates `students.pdf` and a diagnostic `build.log` in the requested directory. It fails on TeX errors or overfull boxes. It uses a temporary build directory inside `--out`, then removes that directory. Poppler's `pdftoppm` and `pdfinfo` are useful for independent output inspection but are not build dependencies.

## Print and materials

Print single-sided on US Letter at 100%, without fit-to-page. Square sides are 6.2 cm. The joined-triangle board is 11.6 cm wide and 5.8 cm high; its triangles meet only at the printed dot C.

Per pair, prepare matching opaque paper triangle tiles by tracing the two halves of an extra page 1 square and both triangles of an extra page 3 board. Label them ABC/ACD for the square and ABC/CDE for the joined board; keep the two sets separate. Prepare edge markers or short yarn pieces, stage cards 0, 2, 3, 4, 5, 8, and three tokens each for AB, BC, CD, AD, AC, CE, DE. AD and DA denote the same edge. Pencil and two colors suffice for saved edge lists and schedules. A reset starts a new build; pieces do not disappear within a build.

Only student pages are included. This is a writer draft, not an approved classroom release. Digital mathematics and rendering checks do not establish physical readiness. Tile preparation, edge-marker fit, handling, pacing, and children's command of the recording rule remain untested. A pair can work with the third child checking legal additions and rotating roles. The four pages need not all be completed in one meeting.

## Contents and provenance

- `students.tex`: original LaTeX/TikZ student pages and diagrams.
- `build.py`: portable standard-library builder.
- `check_math.py`: exhaustive cycle/boundary tests, all stated finite schedules, and independent inclusion-map rank checks.
- `README.md`: dependencies, prerequisites, and limits.

The teaching instances and diagrams are independently devised. Background: H. Edelsbrunner, D. Letscher, A. Zomorodian, *Topological Persistence and Simplification*, sections 2-3, https://pub.ista.ac.at/~edels/Papers/2002-J-04-TopologicalPersistence.pdf. No source paper, borrowed problem text, images, workflow prompts, or generated environment files are included in this portable source set. The run's separate research note records exact source locations and the independently checked algebra.
