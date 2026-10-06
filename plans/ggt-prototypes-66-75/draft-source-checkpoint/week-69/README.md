# Week 69 writer prototype

One shared four-page Grades 4–5 packet. Prerequisites: count road edges, recognize shortest grid routes, maintain three colored sides even where they overlap, and compare a point’s distances to two sets of dots. The late questions require explaining an arbitrary-size construction and a statement about all tree triangles. Unpiloted writer draft, not a final revision or adult guide.

Build: `python3 build.py [--out PATH]`. Check: `python3 check_math.py`. Requires Python 3 and TeX Live with TikZ, fancyhdr, amssymb. All source is standalone; no repository imports or external assets.

The explicit route example precedes triangle construction; the gap-distance example precedes first measurement. Children retain the choice of shortest sides. The two different grid triangles on page 2 distinguish thin choices from fat choices. Gap measurement may use every road in the full grid, including uncolored interior roads. The checks enumerate all monotone diagonal routes for n=1 through 6 and all triples on the two printed trees. The three-corner family has maximum vertex gap n, so vertices alone witness unbounded thinness. For the full metric graph the tree sides still lie in the union of the other two sides and the corner witnesses still apply. Experiments are separate from the late general claims.

Mathematical source: Druţu–Kapovich, Geometric Group Theory, thin triangles, printed p.363 / PDF p.383, https://www.math.ucdavis.edu/~kapovich/EPR/ggt.pdf . Original student text and diagrams. No physical rehearsal or classroom piloting claimed.
