Week 94: Calibration lab

Mathematical kernels

1. An additive instrument reports y=x+b, with one fixed unknown offset b throughout an experiment. Every measurement is compatible with replacing all unknown lengths x by x+t and b by b-t, so repeated measurements alone need not recover absolute length. Differences between readings recover differences between lengths. A known reference length identifies b. A broken or shifted scale gives a concrete model: a rod's length is the number of unit intervals it spans, not the label at one end.

2. A fixed affine instrument reports y=a+bx with b>0. One known reference cannot determine both its offset and its stretch. Two different reference lengths do; subtracting their readings removes a, and the ratio of reading difference to length difference identifies b. A third standard may expose a non-affine instrument, but finitely many agreements do not certify every other input. Preserve this distinction between a model being stipulated and a model being investigated.

3. With two exact reference lengths separated by D>0 and each reading within e of its true report, the set of possible slopes has width 4e/D before restriction to positive slopes. Farther-apart references can therefore give tighter worst-case slope information. Repetitions cannot be assumed to average away a fixed bias or adversarial bounded errors. This is a readiness-dependent upper continuation, not a confidence-interval lesson.

Sources: NIST/SEMATECH e-Handbook sections 2.3.6.1 (https://www.itl.nist.gov/div898/handbook/mpc/section3/mpc361.htm), 2.3.6.3 (https://www.itl.nist.gov/div898/handbook/mpc/section3/mpc363.htm), and 2.4.5 (https://www.itl.nist.gov/div898/handbook/mpc/section4/mpc45.htm). The finite objects, exact identifiability proofs and bounded-error model are independently derived. Existing Week 51 already has interval sums, differences and intersections; this packet must be about identifying an instrument through chosen measurements, not repeating those exercises. Week 6's exact query game and Week 25's ambiguous shadows supply connections, but this is a shared nuisance parameter and experimental design.

Suggested emphasis by level

K–1: Concrete missing-zero scales, equal lengths at different positions, intervals versus endpoint labels. This may be a short standalone entry, honestly limited; do not invent four pages of routine subtraction to meet a quota.
Grades 2–3: Fixed shifted scales, multiple compatible object/instrument explanations, and the role of a known reference; count/compare distances, add/subtract within about 20, adult reading.
Grades 4–5: Distinguish offset and stretch, choose reference measurements, identify possible instruments; wider-separated references with bounded reading noise as a return-visit direction when ratios and multiple possible explanations are comfortable. Use concrete strips before symbolic parameters.

Materials

Per pair: 12 identical unit cubes (or twelve equal paper unit squares), four paper strips of lengths 2,3,4,6 units, one unit-spaced 0–20 number-line strip, one opaque cover to hide a scale's zero or offset, a pencil/whiteboard. Per table: scissors and tape handled by adult. Nominal printed unit 8 mm permits a 20-unit line within Letter width; do not claim fit to commercial cubes. Paper unit pieces must be supplied in the packet or built with ruler by adult; any printed working scale using separate rods must use the same unit. Clearly distinguish schematic illustrations from actual-size manipulatives. For an affine reading game use a partner operating a fixed hidden rule, or explicitly supplied paper scales with matching positions; a wrong reading must be checkable by a reveal at the end of a round. Changing instrument parameters between rounds must be explicit. No specialized hardware or real measurement precision is assumed. Shared launch demonstrates a non-task input, placement/intermediate reading action, and output without revealing the later identification method.
