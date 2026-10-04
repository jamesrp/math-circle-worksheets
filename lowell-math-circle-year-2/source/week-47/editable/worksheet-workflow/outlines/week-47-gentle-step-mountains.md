Week 47: Mountains with a gentle-step rule

Mathematical kernels

1. On a row of equally spaced sites, neighboring nonnegative whole-number heights may differ by at most one. Some heights are fixed. A completion exists exactly when every pair of clues differs in height by no more than the number of steps between them. Necessity follows because each step changes height by at most one. Sufficiency is constructive: the lowest completion at site i is max(0, max over clues j of [h(j)−distance(i,j)]); the highest is min over clues j of [h(j)+distance(i,j)]. Each cone changes by at most one per step, and pointwise maxima/minima preserve that property. The clue-pair condition makes both envelopes meet every clue. These are the finite McShane–Whitney Lipschitz extensions; no algebraic formula is required from children.

2. Concrete seven-site instance, positions 0,...,6, clues h(0)=1,h(4)=3,h(6)=1: lowest [1,0,1,2,3,2,1], highest [1,2,3,4,3,2,1], ten completions in all. The two extremal landscapes are useful certificates; children need not list all ten. A height difference of three over only two steps is impossible. Show a legal example of a small landscape and an illegal neighboring jump. If introducing cone envelopes, show one clue's allowed heights radiating along its labeled sites before combining clues; do not print the extremal construction as a recipe before children search. This is a bounded-rate problem, not the older average-of-neighbors landscape.

Sources: McShane, Extension of range of functions (1934), DOI 10.1090/S0002-9904-1934-05978-0. An accessible verified occurrence of the extension formula is Gigli–Pasqualetto, §1.2, equation (1.16): https://iris.sissa.it/retrieve/3bdd69aa-8d1f-4cc9-b9c9-7784d542dd98/GHTM.pdf. The finite case, feasibility proof, and extremal examples above are independently derived; exhaustive check found ten completions.

Suggested emphasis by level:

K–1: build or trace legal small hills between pictured height clues, finding impossible jumps.
Grades 2–3: search for highest/lowest allowed heights and give distance-based explanations.
Grades 4–5: construct whole extremal landscapes and explain why pairwise clue consistency suffices; formulas optional.

Materials

Per child: a seven-column height board, columns at least 22 mm wide, with levels 0–5 spaced at least 20 mm; seven movable height markers at least 18 mm wide; three removable clue flags. Ten kits, 70 markers and 30 clue flags. Optional physical towers for the youngest: at least 35 same-size cubes per child when using all seven sites, with no artificial total-block budget. Otherwise the printed height board is the exact model. Zero height must be visibly represented, not mistaken for a missing clue. Boards for small entries may have fewer columns but use the same step rule. No requirement to copy large tables of solutions.
