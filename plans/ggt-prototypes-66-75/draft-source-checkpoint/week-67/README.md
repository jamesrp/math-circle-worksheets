# Week 67 writer prototype

One shared four-page Grades 3–5 packet. Prerequisites: count road edges, distinguish a shortest route from an arbitrary route, keep three pairwise tests on one unchanged board, draw paths in different colors. Page 4 additionally requires comparing three-place 0/1 labels; no binary arithmetic. Unpiloted writer draft, not a guide or final revision.

Build: `python3 build.py [--out PATH]`. Requires Python 3 and a TeX Live installation with TikZ, fancyhdr, amssymb. Outputs students.pdf and build.log. The source is self-contained, with no repository imports or borrowed reference text.

Check: `python3 check_math.py`. Verifies all 2,300 triples on a 5-by-5 vertex grid, all 56 triples on a cube, and the specific tree/3-cycle/4-cycle. The common dot means membership in some shortest path for each pair, not in every chosen path. The three checks use unchanged homes and a single unchanged candidate.

Mathematical source: Druţu–Kapovich, Geometric Group Theory, median graphs, printed pp.177,180 / PDF pp.197,200, https://www.math.ucdavis.edu/~kapovich/EPR/ggt.pdf . Student text and diagrams newly authored. Digital verification is not classroom piloting or physical rehearsal.
