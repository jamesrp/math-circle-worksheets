# Guide solution backbone (drafting support, not student pages)

## Week1

Boundary law includes ALL boundaries (holes included), excludes point contacts from adjacency, assumes full unit-edge sharing/no overlap. Six green triangles alone have boundary6 (regular unit hexagon) or8 (tree-like strip); fewer than six triangles in an edge-connected triangular lattice have no dual cycle, so their boundary is fixed at t+2. This is a useful guard against choosing a trivial inventory.

Sharp green/blue corners contribute one sector; blunt blue corners two. With p pieces at one point, p<=6 and at least3; the number of blunt corners must be6-p. Mixes among green and sharp blue remain free. All16 triples g,a,o solving g+a+2o=6 are geometrically realizable as local fans; this does not assert any chosen outer boundary can then be tiled. Unit-hexagon green/blue tilings are the18 matchings of a six-cycle: 12 have symmetryorder1, three order2, two order3, one order6. The five rotation-equivalence classes are optional adult continuation.

## Week2

An observation before/after a known switch press gives its exact toggled set. Three arbitrary three-lamp switch masks contain9 bits; each observed three-lamp result carries at most3 bits, so even adaptive full-snapshot experiments need at least3 in worstcase. If trials means one switch press, simpler lowerbound: an untouched switch can have any hidden wiring. Three individually observed presses attain the bound. This assumes fixed deterministic switch action and visible initial state, no noisy/errorful operator.

Three-neighbor ring switches: for n4 and5 all targets are reachable and uniquely solved as press subsets; for n6 reachable16 of64, with four subsets per reachable target. Let residue groups {1,4},{2,5},{3,6}: their ON-count parities must all agree. Empty-target press sets at n6 are empty, {1,2,4,5}, {1,3,4,6}, {2,3,5,6}; indexing switchi toggles i,i+1,i+2. Image/kernel independently enumerated. Any repeated switch can be canceled pairwise.

Adjacent-exchange lamp switches preserve ON-count (not merely parity). Connected graph allows every same-count target; disconnected graph requires same count on every component. Line minimum matches sorted ON positions, sum absolute displacements. No crossing or simultaneous move shortcut allowed; a switch exchanges exactly one adjacent pair.

## Week3

Each adjacent swap changes the inversion count by1, and adjacent inverted pairs can be swapped until zero. This proves exact minimum, not just a lowerbound; whole-row reversal needs n(n-1)/2 swaps. Rotate/reverse moves preserve cyclic unordered adjacency. For n>=3 distinct labels they generate exactly2n orders; a single ring can be read at any starting position in either direction. Duplicated labels change counts. Machine roots need even cycles to occur in pairs; square an oddlengthcycle to get one odd cycle, an evenlengthcycle splits in two equal halves. Fixed labels matter.

## Week4

Meetings are checked only AFTER both counters move in a turn; crossing arcs doesn't count. Starting together always gives a future meeting, but a different start may prohibit it: gcd(n,u-v) must divide the offset. A meeting need not return both counters home. Two allowed clockwise hops generate exactly positions divisible by gcd(n,a,b); directed search computes shortestroutes. Inverting a clockwisehop on a finite ring is possible by repeating it until one step short of its period.

Sixbeads, three red: rotationrepresentatives BBBRRR, BBRBRR, BBRRBR, BRBRBR. Classes have6,6,6,2 distinct labeled rotations (20 total). The middle two are mirrorpartners; reflectionequivalence merges them, givingthree. The alternating coloring has symmetryorder3 (three legal rotations) and rotationalperiod2; other three have symmetryorder1. Necklace registration dots should not count as design marks.

## Week5

Alternating rectangle trades preserve the two participating values in each selected row/column. A 3by3 alternating a,b/b,a rectangle would force both remaining entries of the selected rows to be the third value c in the same column, a contradiction. Order4 has4 or12 trades, even allowing nonadjacent rows/columns. For both3by3 diagonals: the center has c, so the corners on each diagonal are a,b. Top corners differ (row condition), forcing topmiddlec and bottommiddlec, a repeated column value. Order4 bothdiagonalexample: rows1234/3412/4321/2143. There are48 labeled examples; listing them is not a student requirement.

Roof paths strictly increase, hence cannot return or continue indefinitely. Terminal vertices are local peaks; all n tallest towers are peaks, but lower ones can be. Every start has some route to a globalmax iff all localpeaks have maximalheight: follow any increasing step until a peak; conversely a lowerpeak cannot leave. n3 possiblepeakcounts3,4; n4 possiblecounts4,5,6,7,8. Counts were enumerated over12 and576 cities, not inferred from sampleexperiments. Sideadjacency only, no wraparound, no diagonals.
