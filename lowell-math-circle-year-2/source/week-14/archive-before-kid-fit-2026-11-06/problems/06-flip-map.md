+++
id = "w14.flip-map"
title = "The flip map of the pentagon"
grades = ["2-3", "4-5"]
route = {"2-3" = "return", "4-5" = "first"}
kernel = "The pentagon's five fillings and their flips form a five-cycle, so a filling can return to itself after an odd number of flips."
+++

## prompt [2-3]
A change of one inside line that keeps the polygon filled with triangles is called a flip. Join two drawings when one flip changes one into the other. Include every possible join.

## prompt [4-5]
A change of one inside line that keeps the polygon filled with triangles is called a flip. Join two drawings when one flip changes one into the other. Include every possible join. Can you return to a filling after an odd number of flips? Show a route, or explain why it is impossible.

## figure
flip_example()

## text @4.02,2.12 w=3.6 size=11.5
Example: erase AC, draw BD. The join connects whole fillings; it is not an inside line.

## figure
pentagon_map()

## key [2-3]
The complete pentagon map has exactly five joins: $F_A F_C$, $F_C F_E$, $F_E F_B$, $F_B F_D$, $F_D F_A$. There are no other joins. The revised student layout follows this cycle around the page. Each adjacent pair keeps one diagonal and replaces the other. Each of the five fillings has only two interior diagonals, hence exactly two possible flips; the displayed joins account for both and prove completeness.

## key [4-5]
The complete map is the five-cycle on page 6. The five-flip loop $F_A,F_C,F_E,F_B,F_D,F_A$ is an odd return. Its reverse is also valid. The graph is not bipartite: alternating two colors around the cycle makes the final edge join two same-colored vertices. Fidelity warning. A parity invariant from lozenge tiling flips does not transfer here. The objects and moves are different; a polygon five-cycle is a direct counterexample to an even-return claim.
