# Week 68 reviewed prototype

One shared four-page Grades 3–5 packet. Prerequisites: follow routes, distinguish vertices from roads, preserve blocked vertices while tracing, distinguish a finite trapped pocket from an endless continuation. Later questions require extending a repeating rule beyond a finite picture and explaining a general claim. Status: reviewed prototype, unpiloted. Revised student pages only; the adult guide is a separate stage.

Build with `python3 build.py [--out PATH]`; check with `python3 check_math.py`. Requires Python 3, pdflatex, TikZ, fancyhdr, amssymb. Portable source has no repository imports or external assets.

Preparation: provide at least 10 small opaque blockers per pair, about 6–8 mm across. The grid vertices are 10 mm apart; larger counters can conceal an adjacent open dot. Paper squares are suitable. Ten blockers cover the center and all vertices through radius 2 on the tree. The radius-3 continuation can be reasoned about without covering it physically. Print at 100% on US Letter. Physical material fit still needs rehearsal.

Every continuation edge is arrowed. The printed windows are not closed boundaries. A blocker removes the vertex and all incident roads; the finite square example demonstrates this before play. The tree continuation explicitly forbids reconnections. The nested tree deletions have 3,6,12,24 infinite components. Finite experiments do not prove an infinite statement; the checks state the separate tail, enclosing-square, and never-rejoin arguments. The student phrase “forever pieces” refers to unbounded components after the specified deletion, not the number of boundary arrows or necessarily the graph’s number of ends after one small deletion.

Mathematical source: Druţu–Kapovich, Geometric Group Theory, ends, printed pp.287–289 / PDF pp.307–309, https://www.math.ucdavis.edu/~kapovich/EPR/ggt.pdf . All student wording/diagrams are original. No physical rehearsal or classroom piloting claimed.
