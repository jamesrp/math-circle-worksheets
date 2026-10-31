# Week 57 K–1 adult-guide source

Writer-stage companion to the seven-page `N57-K-v1` student packet. This is
unpiloted; print fit, preparation, handling, tracing, staffing and timings have
not been physically rehearsed. No student file is changed.

## Portable build

Dependencies: pdfLaTeX with the ordinary `geometry`, `fontenc`, `lmodern`,
`amsmath`, `amssymb`, `array`, `booktabs`, `fancyhdr`, and `tikz` packages;
Python 3; Poppler's `pdftotext`.

Place the approved student `k-1.pdf` beside this source folder, then run:

```sh
cd src  # or guide-src after packaging
./build.sh
```

This produces `../k1-guide.pdf`, removes temporary LaTeX files, and ends with
`check_guide.py`. The checker first uses `../k-1.pdf`; while inside the repository
it can instead find `plans/k1-drafts/week-57/k-1.pdf` by ascending from its own
location. There is no machine-specific environment or absolute input path.
The build refuses LaTeX errors and overfull boxes.

The checker pins the final student PDF's SHA-256 and its seven problem/page
labels, because the old reviews describe an earlier six-page version with P5/P6
in the opposite order. If the student PDF changes, re-inspect its diagrams and
recompute/review the guide before deliberately updating that pin.

## Independent mathematics

The verifier imports no student-author or review code. It enumerates unions of
quarter-cell triangles, using exact integer coordinates. A half consists of two
such atoms; a square consists of four. New halves must share a whole side and
have disjoint interiors. Every side-connected piece arrangement has a connected
adjacency graph, so it has an ordering in which each new piece touches earlier
pieces; the search retains even invalid intermediate unions. Canonicalization
identifies lattice translations, quarter turns and reflections. At the final
stage edge cancellation requires a single degree-two boundary loop, excluding
holes and pinches. Corner incidence counts inside and outline dots independently
of Pick's theorem.

Checks include:

- P1 polygon area by shoelace, dots by exact cross products/winding, all six records;
- the non-task three-square demonstration;
- all half-piece regions of sizes 1–8, hence the P2 and P3 conclusions and all
  P7 successes (two shapes with six outline dots); fits on the final board sizes;
- all 16 P5 square/half choices around a dot, collapsing to six rotation classes;
- the P4 quarter-turn bound; the six required cells for the P6 lower bound and
  all 16 six-piece constructions before symmetry (seven shape classes);
- guide page count and problem-to-student-page references.

All diagrams in the guide are compact adult illustrations, not cutting or
piece-fitting templates. The student working grids and materials are the
20 mm templates. Sources and teaching context remain with the main Week 57
facilitator guide, p. 10; the local private books were not available here.
