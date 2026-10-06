# The gentlest stretch student prototype

Writer-stage draft, four US Letter student pages, Grades 4–5. Unpiloted; physical dot/strip/ruler rehearsal is untested. Prerequisites: ruler use, halves, ratios understood as a distance multiplier, and locating a midpoint. Exact whole-sheet explanations are a later readiness-dependent task.

Build with `python3 build.py --out /chosen/output` using Python 3 and a normal TeX Live installation with pdflatex, TikZ, geometry, fancyhdr, and Latin Modern. The source entrypoint is `students.tex`; the output is `students.pdf`. `python3 check_math.py` checks the finite pin examples and the exact inequality.

Children control the new location of O and the pairs tested. In the first game, the five-pin maximum is 2 at every interior O position. This is deliberately only a finite-sample score. The next page adds legal midpoint probes that detect all off-center placements in the triangle-wise affine family. Neither a finite pin score nor a finite sample is a certificate for the whole sheet. For an interior O, the four affine triangle maps form a side-preserving homeomorphism; the centered choice is (x,y) -> (x/2,2y). Pages 3–4 ask for whole-sheet rules and explanations, including the arbitrary side-preserving lower bound. This is an elementary Lipschitz comparison, not a Teichmüller metric calculation.

Source lineage: Moon Duchin, *Billiards and Geometric Topology*, November 3, 2005 abstract, https://people.reed.edu/~davidp/talks/talks05-06/talks/duchin.html (read October 6, 2026). Metric-comparison inspiration only. The elementary rectangle calculation and child-controlled pin/fan game are independently authored; no claim they occurred in that talk. No borrowed source text or reference PDF is packaged.
