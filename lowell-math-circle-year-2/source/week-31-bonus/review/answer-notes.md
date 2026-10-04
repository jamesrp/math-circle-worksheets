# Week 31 final student answers

Unpiloted selected-band companion, grades 2–5. Prerequisites: exact collinearity with threads/rulers, across/up coordinates, two-component addition; area in grid squares for Problem 4. General explanations in Problems 2,4,6 need stronger multiplicative/factor reasoning and are optional return work. Every working grid has equal x/y scaling, 20 mm spacing. Physical thread accuracy and pegboard fit are untested.

## Three investigations

1. Two-lookout coverage, Problems 1–2.
2. Empty lattice triangles, Problems 3–4.
3. Neighbor-direction growth, Problems 5–6.

In Problem 3, B is also the clear-sided triangle with interior dots; having visible sides only controls boundary dots. The redundant separate witness task was merged into this collection. The regularly spaced orchard continues beyond the printed grid.

Base visibility census and gcd derivation are not repeated. The classification table is one record for the same targets against two unchanged lookouts. Direction cards retain one ordered construction; no traversal log is required.

## Precise answers

Problem 1: L=(0,0), R=(1,0). A target (a,b) is visible from L iff gcd(|a|,b)=1, and from R iff gcd(|a−1|,b)=1. Row 3, across 0–6: 1,1,B,1,1,B,1. Row 6: 1,1,1,0,0,1,1. The only doubly hidden printed targets are (3,6),(4,6). At a=0, gcd(0,b)=b, but visibility from R holds; at a=1 the roles reverse. Only strictly intermediate points block.

Problem 2: None, on the entire row 4. Hidden from each would require 2 to divide both a and a−1, impossible. This is an explanation using the only prime factor of 4; testing only the printed grid is experimental evidence, not the infinite argument.

Problem 3: A: vertices (0,0),(1,0),(0,1), area 1/2; empty. B: (0,0),(1,2),(3,1), area 5/2; each side primitive, interior dots (1,1),(2,1), no extra boundary dots; not empty. C: (0,0),(2,0),(0,2), area 2; extra boundary dots (1,0),(0,1),(1,1), no strictly interior dots; not empty. D: (0,0),(2,1),(1,1), area 1/2; empty.

Problem 4: Many constructions accepted. Examples: A; D; vertices (0,0),(3,1),(2,1), each area 1/2 and empty. These are distinct shapes (A has unit perpendicular sides; D has side lengths 1,sqrt2,sqrt5; third has 1,sqrt5,sqrt10). They all fit the 3×3 grids. For any nondegenerate empty lattice triangle, Pick's theorem area=I+B/2−1 gives I=0,B=3, hence 1/2. Conversely area 1/2 implies empty because nonnegative integer I and B≥3 force I=0,B=3. Children may disassemble/copy specific triangles to find area, then conjecture a common area; that is not by itself a proof of Pick's theorem. Area is geometric, no determinant notation is required of children. Degenerate collinear triples are not triangles.

Worked direction visual: neighboring (2,1),(1,1) sum to(3,2), plotted 3 across and 2 up; determinant2·1−1·1=1. This is a non-task input, not a solved target.

Problem 5: Begin (1,0),(0,1). Insert (1,1). To its left insert (2,1), then (3,2) between(2,1),(1,1), then (4,3) between(3,2),(1,1). To the right of (1,1) insert (1,2), then (2,3) between(1,1),(1,2), then (3,4) between(1,1),(2,3). Final increasing-slope row: (1,0),(2,1),(3,2),(4,3),(1,1),(3,4),(2,3),(1,2),(0,1). Other insertion orders give the same directions. (4,2) is impossible: every generated direction is primitive. If neighboring u=(a,b),v=(c,d) have determinant±1, any common divisor of a+c,b+d divides a(b+d)−b(a+c)=ad−bc, hence is 1. Both child neighbor determinants remain±1.

Problem 6: Every positive primitive direction can be reached. To target T in cone(u,v), write T=A u+B v; determinant-one gives integral coefficients and the inside condition gives A,B>0. If A>B, restrict to(u,u+v) and replace coefficients by (A−B,B); if B>A, restrict to(u+v,v) with (A,B−A). The sum decreases. When A=B, primitiveness forces A=B=1, giving the inserted sum. These interval choices are forced, hence each positive primitive direction appears once. Concrete examples (5,2),(2,5),(5,3),(3,5),(6,1),(1,6) all satisfy the condition. Arbitrary addition of nonneighbors need not preserve visibility; the rule requires neighboring cards throughout.

Source context: translated visibility criterion, Pick's theorem, Stern–Brocot/Farey neighbor construction from supplied encore outline. Local tasks are not evidence of prior classroom use. Any refreshed Week 31 PROMPT attribution applies; no additional classroom/source claim is made here.
