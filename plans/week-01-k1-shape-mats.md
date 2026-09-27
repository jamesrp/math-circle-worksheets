# Week 1 K–1: Fill a shape

September 23, 2026. **F01-K-v3**, planned, not yet recorded as taught. Replaces the two-page shop/flip packet with four pages of easy physical tiling. The child pages have ten blank mats for eight shapes and short spoken prompts. More time comes from building, rebuilding, and comparing, without adding harder mathematics. Children seeking harder work may choose the existing grades 2–3 packet.

## Preparation and hour

Print [the student PDF](../lowell-math-circle-year-2/week-01/week-01-k-1.pdf) at **Actual Size / 100%, US Letter, single-sided**, and check the one-inch line against a small block. Use only small (1×) pieces. For each child set out **3 purple chevrons, 12 green triangles, 6 blue rhombi, and a few red trapezoids/yellow hexagons**. Reuse blocks between mats. An adult may trace the joins before the pieces are lifted; children need not write. Give one page at a time.

**Prerequisites:** matching a boundary and turning pieces; no independent reading, writing, arithmetic, or counting. The mathematical ideas are composing a whole, decomposing the same region in different ways, and attending to a simple piece restriction.

Use 0–10 minutes for free building; 10–15 for the brief launch, “Can you fill this outline?”; 15–35 for the first mats; 35–40 for movement/reset; 40–55 for chosen remaining mats or refilling; 55–60 for showing a favorite and tidying. This is flexible: every successful filling is a stopping point, and finishing the packet is not required.

Ask “Which piece could fit here?”, “What happens if you turn it?”, and “Can you fill it another way?” If needed, turn a piece beside the mat or offer just one starting piece. Keep solution diagrams out of sight. Easy continuations are using a different mix, comparing with a partner, or tracing a child's own construction. There is no shop, piece-count minimum, impossibility task, enumeration demand, or formal flip rule.

## Mats and checked examples

| Page | Shape | Child's rule | Example filling |
|---|---|---|---|
| 1 | Sailboat | Any small pieces | 11 greens |
| 1 | Cat | Any small pieces | 7 greens |
| 2 | Hexagon, printed twice | Fill the twin differently | 1 yellow; or 3 blues; or 6 greens |
| 2 | Diamond, printed twice | Fill the twin differently | 4 blues; or 8 greens |
| 3 | Arrow | Only purple chevrons | 2 purples, side by side |
| 3 | Star | Only purple chevrons | 3 purples meeting around the center |
| 4 | Long hexagon | Only blue rhombi; then refill freely | 5 blues |
| 4 | Mountain | Only green triangles; then refill freely | 9 greens |

These are attainable examples, not targets for minimizing pieces. Every mat is possible with its stated pieces. Page 2 accepts different piece types; tracing before lifting allows reuse without doubling the supply. The [facilitator PDF](../lowell-math-circle-year-2/week-01/week-01-facilitator.pdf), p. 2, shows the chevron-only solutions. The JSON includes exact green/blue/purple witnesses whenever those single-piece fillings exist.

The [verification script](week-01-k1-shape-checks.py) uses triangular-lattice cells, checks area and full-edge connectivity, validates the boundary, and finds exact covers by rotated blocks. It checks that each witness covers all cells once. The [JSON](week-01-k1-shape-checks.json) supplies the eight outlines and solution placements to [the TikZ generator](../lowell-math-circle-year-2/source/week-01/generate-k1-geometry.py). Unit geometry is shared by the child mats and adult examples. Recheck after changing any polygon.

## Source and progression notes

- **Prior Lowell, _Pattern Block Exercises_, p. 1, problems 1–3:** filling an outline and restricting piece types are familiar formats in the organizer's collection. The new K–1 mats do not reuse that sheet's packing/impossibility questions.
- **Early Family Math, _Pattern Blocks – Least Pieces_, p. 1, “Variations”:** encourages creating fun game-board designs. We use the outline-making format and remove its optimization goal. All eight silhouettes here are our constructions.
- **_Math Circle by the Bay_, preface pp. ix–x (PDF pp. 10–11):** describes manipulatives, independent attempts, varied pacing, and adjustment to groups. Our inference for this revision is to offer more physical examples and time to refill, while leaving harder questions in the middle packet.
- **Returning children:** the small hexagon revisits a familiar pattern-block shape. Track actual silhouette and rule in the [use log](fall-k-5-year-a-use-log.md); this revision does not establish that any child has already used these mats. Later visits can use different silhouettes or the existing middle/upper questions.
