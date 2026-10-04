Week 39: Which journeys can shrink away?

Mathematical kernels

1. On a fixed graph of narrow roads, an edge immediately followed by the same edge in reverse is a removable detour: the outward-and-back motion can continuously shrink while endpoints remain fixed and the path stays on the roads. Every finite edge path has a unique reduced edge path after all such immediate reversals are removed, regardless of deletion order. An elementary proof uses a running stack of oriented edges: a new edge cancels the opposite top edge, otherwise it is appended. Inserting/deleting an adjacent inverse pair does not change the final stack. Every deletion reduces length, so a deletion process ends at the same invariant stack. This algorithm is an adult proof device or a later representation; do not give it to children as the method before they have investigated choices. Empty path means stay at the basepoint, not a missing answer. Stationary pauses do not matter.

2. On a finite tree, every closed journey reduces to the empty path, and every path between two given vertices reduces to the unique simple route. A farthest visited vertex on a closed nonempty tree walk forces a reversal somewhere; equivalently a nonempty reduced closed walk would create a cycle. On a ring, a full trip need not vanish. On a figure-eight road with loops a and b based at the common junction, a then b differs from b then a. The journey a b a^-1 b^-1 uses each loop once in each direction yet remains a nonempty reduced word. Thus net counts alone do not determine a journey. This is a faithful elementary entrance to the graph's fundamental group, not parity homology. No move may jump across the empty space inside a ring, cancel separated reverse letters, swap subjourneys, or move the basepoint. Ordinary paths may retrace/self-overlap; they are not embedded strings.

Sources: Allen Hatcher, Algebraic Topology, Chapter 1 §1.2 (free products/reduced words), §1A (graphs and free groups), https://pi.math.cornell.edu/~hatcher/AT/ATch1.pdf . The finite reduction proof above is self-contained. Atlas AD-22 toggles boundaries of filled faces over F2; this is deliberately a different object and equivalence relation. GA-25 removes graph edges to produce a tree; here the graph stays fixed while journeys change.

Suggested emphasis by level:
K–1: Act out and shorten journeys on a small tree with a pawn; show what happens to an actual out-and-back excursion without symbol strings.
Grades 2–3: Compare alternative detour-removal choices and contrast a tree with a ring; invent a long journey that can be shortened a lot.
Grades 4–5: Explain why every cancellation order agrees and test two-loop journeys with the same net counts; formal group notation is optional.

Materials

Per child: one pawn, a tree road mat with 4–6 vertices and wide roads; one ring mat; six pairs of two-sided arrow tiles (outward/reverse) at least 30 mm long. Per table: one 200 mm figure-eight mat with a marked home junction, 20 spare arrow tiles, two transparent sleeves and erasable pens. Roads must not cross accidentally: a crossing is a junction only when visibly marked. Use a short shared demo A→B→C→B→D changing to A→B→D, with the same colored/lettered vertices before and after and the erased B→C→B excursion clearly identified. This is the required input/process/output example; it does not solve the tree or two-loop discoveries. Children may replay rather than transcribe routes; adults can record one chosen route. No real rope needs to be tightened, tied around anyone, or forced across itself.

Novelty and readiness: Beyond the atlas's exact kernels, related to AD-22 and GA-25 but not duplicates. Distinct from route packing, finite-state machine memory, and Euler/postman travel: no capacities, memory optimization, or requirement to cover every road. Draft and unpiloted. Keep the action playful; do not require a page of word reductions.
