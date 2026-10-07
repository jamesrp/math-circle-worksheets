# The gentlest stretch student prototype

Independently reviewed prototype awaiting organizer review, unpiloted. Four US Letter student pages, Grades 4–5. Physical dot/strip/ruler rehearsal is untested. Prerequisites: ruler use, halves, ratios understood as a distance multiplier, and locating a midpoint. Exact whole-sheet explanations are a later readiness-dependent task.

Build with `python3 build.py --out /chosen/output` using Python 3 and a normal TeX Live installation with pdflatex, TikZ, geometry, fancyhdr, and Latin Modern. The source entrypoint is `students.tex`; the output is `students.pdf`. `python3 check_math.py` checks exact rational pin samples, the squared-distance identity and the target examples. These finite regression tests supplement the universal argument below.

Children control the new location of O and the pairs tested. In the first game, the five-pin maximum is 2 at every interior O position. This is deliberately only a finite-sample score. The next page adds legal midpoint probes that detect all off-center placements in the triangle-wise affine family. Neither a finite pin score nor a finite sample is a certificate for the whole sheet. For an interior O, the four affine triangle maps form a side-preserving homeomorphism; the centered choice is (x,y) -> (x/2,2y). Pages 3–4 ask for whole-sheet rules and explanations, including the arbitrary side-preserving lower bound. This is an elementary Lipschitz comparison, not a Teichmüller metric calculation.

Source lineage: Moon Duchin, *Billiards and Geometric Topology*, November 3, 2005 abstract, https://people.reed.edu/~davidp/talks/talks05-06/talks/duchin.html (read October 6, 2026). Metric-comparison inspiration only. The elementary rectangle calculation and child-controlled pin/fan game are independently authored; no claim they occurred in that talk. No borrowed source text or reference PDF is packaged.

## Mathematical certification and physical limits

For any displacement (u,v), 4(u²+v²) − (u²/4+4v²) = 15u²/4 ≥ 0. This proves the centered rule bounds every pair, including diagonal and off-grid pairs. Opposite named horizontal sides force stretch at least 2, so the optimum is exactly 2. For target dimensions W,H > 0, the same argument gives optimum max(W/4,H). The exact midpoint test in the fan family uses the two unit disks centered at (1,0) and (1,2); their only common point is (1,1). None of these universal claims is inferred from finite measurements.

Measured success identifies a candidate only. The quarter-unit grid has physical unit 0.94 inches; at O=(1.25,1), the midpoint witness exceeds the doubled old distance by about 0.735 mm. Nearer off-center choices have still smaller discrepancies. Do not demand exact detection from a ruler, a paper dot, or a strip. Every legal five-pin placement ties at 2, so the opening game's purpose is to expose the limitation of sparse tests; it need not be prolonged once children notice the tie. Children retain control of placements and test pairs. Exact diagonal/all-pairs reasoning belongs to the later readiness-dependent problems.

Before classroom use, rehearse dot placement, paper-strip comparison and midpoint measurement at 100% print scale. No physical rehearsal or classroom pilot has been performed. Guide authors should distinguish an observed candidate, the exact fan-family midpoint argument, and the whole-sheet proof.
