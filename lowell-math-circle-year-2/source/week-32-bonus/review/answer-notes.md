# Week 32 final student answers

Unpiloted selected-band companion, grades 2–5. Concrete tasks need whole-grid square fitting, piece counts, and the familiar biggest-square removal action. Multiplication/area reasoning to35 supports the lower bounds. Compressed recipes need reliable distinction between a size and a count. The working grids are 10 mm in both directions. Physical precut tile fit and pacing have not been rehearsed. Colored-pencil boundaries with a partner checking fit are an alternative.

## Three investigations

1. Biggest-square tiling versus fewest pieces, Problems1–2.
2. Restricted square sizes, Problem 3.
3. Reconstructing a size-free recipe, Problem 4.

The six-by-five construction serves the first two kernels and is not counted as a fourth investigation. No last-square/gcd or identical-square task is repeated.

## Precise answers

Problem 1: For6×5, greedy gives one5×5 and five1×1, total 6. A tiling with5 squares consists of two3×3 along a6×3 strip and three2×2 along the remaining6×2 strip. Coordinates (x,y,side): (0,0,3),(3,0,3),(0,3,2),(2,3,2),(4,3,2). These fill the printed6×5 without overlap. Rotating/reflection gives equivalent constructions. For4×3, greedy is one3×3 plus three1×1, total 4 and optimal. Any1–2 square area decomposition fails; the only three-square area decomposition of12 is4+4+4. Three2×2 squares cannot fit in height 3 unless horizontal projections are disjoint, requiring width 6>4. Four is achieved by greedy. The student need only compare this contrast; a full4×3 proof is optional.

Problem 2: The minimum is5. Squares have sides1–5. One square cannot have area 30. No two square areas sum to30. The only three-square area decomposition is25+4+1; a side5 square and side2 square cannot be disjoint because5+2 exceeds both width 6 and height 5. The only four-square area decomposition is16+9+4+1; side4 and side3 likewise cannot be disjoint. For axis-aligned squares with disjoint interiors, at least one pair of coordinate projections must have disjoint interiors. Thus the listed larger pairs rule out both possibilities. This is only for whole-grid axis-aligned squares, not arbitrary tilted squares.

Problem 3:5×5 impossible;6×5 possible by the5-square construction above;7×5 impossible. For5×5 area 25=4u+9v with nonnegative integer counts forces u=4,v=1. Each horizontal side of length5 must be a sum of tile widths2 and3, and thus requires a3-square touching it. A single3-square cannot touch both opposite horizontal sides at distance5. For7×5 area 35 forces u=2,v=3. Since two3-squares have total height 6>5, every pair has overlapping vertical projection and so must have disjoint horizontal projections. Three3-squares require width 9>7. Area alone permits both impossible cases, exposing genuine geometric obstructions.

Worked recipe visual:5×2 is two side2 squares and two side1 squares. The distinct-size groups have counts2 and2; recipe[2,2]. The first count is not a side length. This is not one of the student's recipe targets.

Problem 4: Minimal coprime rectangles and square records: [1,2] gives3×2, sizes2,1,1; [2,1,2] gives8×3, sizes3,3,2,1,1; [1,1,3] gives7×4, sizes4,3,1,1,1. They fit within the supplied8×4 work grids; children should draw a subrectangle and its pieces rather than tile the whole work grid. Every positive integer enlargement has the same recipe, e.g6×4,16×6,14×8. Rotation alone is not a different-sized realization. Prepare spare graph paper so enlarged reconstructions are not restricted by the printed 8-by-4 workspaces. The end-removal convention keeps each remainder rectangular for the Euclidean recipe; free fewest-piece tilings in Problem 1 are not constrained by that rule. The nonsquare recipe determines the long/short ratio by the finite continued fraction q1+1/(q2+1/(...+1/qk)); the actual size remains undetermined. Geometric reversal: set final square side1, rebuild each earlier rectangle backward from the next remainder and count, then scale. The final distinct-size count is at least2 (except a square's recipe[1]), avoiding the alternate continued-fraction ending in1. Formal continued fractions are adult context, not a student requirement.

Source context: supplied encore outline, local minimum-tiling, restricted-fit and reversed-recipe directions. Euclid VII.2 supports base common-divisor context rather than the new optimality claims. No prior classroom use is claimed.
