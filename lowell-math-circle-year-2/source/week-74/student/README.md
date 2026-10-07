# Doubling elevators student prototype

Independently reviewed prototype awaiting organizer review, unpiloted. Four US Letter student pages, Grades 4–5. Physical pawn/board rehearsal is untested. Reading simple move letters, locating a horizontal coordinate, doubling, and reasoning about a move budget are prerequisites. The third child can referee or rotate into either partner role.

Build with `python3 build.py --out /chosen/output` using Python 3 and a normal TeX Live installation with pdflatex, TikZ, geometry, fancyhdr, and Latin Modern. The source entrypoint is `students.tex`; the output is `students.pdf`. Run `python3 check_math.py` for exact route checks and the all-routes budget bound. The finite printed board is a working window, not a mathematical boundary.

Source lineage: Nicholas Touikan, *Introduction to Combinatorial and Geometric Group Theory*, section on HNN extensions and Baumslag–Solitar groups, https://ntouikan.ext.unb.ca/MATH6022/IntroCGGT/html_output/section-15.html (read October 6, 2026). The elevator game is an independently authored nonnegative-height exponential-shortcut model, not the full Cayley graph of BS(1,2). Outline also references Cornelia Druţu and Michael Kapovich, *Geometric Group Theory*, printed p.285 / PDF p.305, https://www.math.ucdavis.edu/~kapovich/EPR/ggt.pdf . No source text or downloaded reference is packaged.

## Mathematical and material boundaries

The graph has every integer coordinate at every nonnegative level. The board's coordinate-dot spacing is 0.23 inches (about 5.84 mm). Use a pointed or very small marker, or a pencil tip, so adjacent positions stay distinguishable. Rehearse a horizontal move from an odd coordinate at a high level. The checking partner must apply the printed stride: ordinary row lines do not mechanically enforce it. Keep all integer dots, shared coordinate alignment, and unrestricted continuation beyond the page.

For an at-most-N-move ground-to-ground route of maximum height H, at least 2H moves are vertical. Every remaining horizontal move has magnitude at most 2^H. Thus total rightward displacement is at most (N−2H)2^H even with left moves, intermediate-level steps or repeated excursions. This universal counting argument, rather than finite search alone, rules out seven or fewer moves to 16. The budget maxima 4,6,8,12,16 for N=4,5,6,7,8 are attained by a single ascent, rightward run, and descent.

The final comparison should remain a later challenge. Coordinates 9,15,17,23 have optimal distances 7,9,9,10 with left moves; without left moves their optima are 7,9,9,11. Overshooting to 16 then moving left for 15 only ties a no-left optimum. The strict improvement is at 23, with a ten-move route via 24. The separate guide should justify both optima rather than treat a found route as proof of superiority.

The portable local checker uses coordinate-unbounded breadth-first search with a depth budget, verifies every printed exact answer, and constructs witnesses for the budget maxima. Physical marker fit, partner rule enforcement and classroom pacing remain unrehearsed and unpiloted. Later all-routes explanations are readiness-dependent.
