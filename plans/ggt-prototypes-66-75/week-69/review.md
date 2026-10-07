# Adversarial review: Week 69, Thin and fat road triangles

## Verdict

**Pass for revision-stage handoff; no mathematical or visual blocker found.** This is a strong shared Grades 4–5 prototype: children control shortest routes, compare a zero-gap choice with a positive-gap choice, and only later tackle arbitrary size and every tree. One small vocabulary clarification would improve the final universal question.

## Scope and evidence

Read the actual repository `AGENTS.md`, `README.md`, complete run `PROMPT.md`/`CRITIC.md`, and the source LaTeX, README, and checker. Rendered and visually inspected all four US Letter pages at 120 dpi, `critic-render/page-1.png` through `page-4.png`. PDF SHA-256: `d6c7c06021fb878c7e1e0620960ba063449938f5d4c3944933800ebdc26a8b82`.

Ran the writer's checker successfully, including every monotone diagonal route through size 6 and every triple on both exact printed trees. The independent mathematical and exact-instance audits agree; their PDF/source fingerprints match this draft. Independently checked the displayed examples and the proof mechanisms below. No student sources/PDFs were edited, and no physical rehearsal or classroom pilot was performed.

## Small clarification

**Low-to-medium priority, before Problem 5:** “Tree” is demonstrated by two accurate pictures but never defined as a class of maps. That suffices for the concrete first task, but “any tree” in the final question should not depend on a child guessing what counts. A short statement such as “A tree is a connected road map with no loops” would fix the scope. An adult can unpack that a loop goes around without retracing roads. Keep the definition brief and do not print the tripod argument or the intended conclusion.

## Mathematical and page-by-page audit

- **Page 1, route convention:** The worked P-to-Q path has two horizontal steps and one vertical step, and its three edges realize the Manhattan lower bound. It introduces edge-count distance rather than physical line length. The three pairwise routes are explicitly chosen, may overlap, and retain separate color marks when they do. This is the right definition of a road triangle when shortest routes are nonunique.
- **Page 1, Problem 1:** Both drawn maps are connected, acyclic trees, with 12 and 11 vertices. For every choice of three different homes, each used edge lies in exactly two of the pairwise paths, never exactly one. Cutting a used edge divides the three homes 1-versus-2; precisely the two cross-partition pairs use it. The checker covers all 220+165=385 triples. The children first encounter overlapping routes as an action before the term “gap” is introduced.
- **Page 2, gap convention:** The P-to-dark-side example is correctly distance **3**, using the horizontal interior route. “Either of the other two” means the minimum distance to their union; the explicit permission to use uncolored roads and the explicit zero-gap case are essential and correct. The example does not give away a target road triangle.
- **Page 2, Problem 2:** The homes are (0,0), (4,0), (4,4) on both maps. Choose AC via B for a zero-gap triangle; every used road then belongs to another side. Choose AC via the opposite corner (0,4) for a gap **4** at that corner, meeting the request for a gap at least 2. All three sides remain shortest. This paired task correctly disproves the misconception that every grid triangle must be fat.
- **Page 3, Problem 3:** The grid side lengths are **2, 4, 6**, and the exact optimal biggest gaps are **2, 4, 6**. AB and BC are forced along the bottom and right; AC may be any monotone diagonal route. The left/top choice reaches the claimed gaps. No point can have a gap above n on the n-by-n board: AC points are within n of the bottom/right union, and AB/BC points are within n of a shared endpoint on another side. The 6, 70, and 924 possible AC shortest routes agree with this bound.
- **Page 4, Problem 4:** Given the partner's whole number k, choose n=k+1, with A=(0,0), B=(n,0), C=(n,n), AB bottom, BC right, and AC left then top. Side lengths n,n,2n equal the required Manhattan distances. The opposite corner (0,n) has distance exactly n to the bottom/right union, even when all interior grid roads remain usable. This is an arbitrary-size construction and explanation, not an extrapolation from the three boards.
- **Page 4, Problem 5:** No tree road triangle has a positive gap. Its three shortest paths are the unique simple paths and form a tripod, possibly with one arm of length zero; each point/edge of a side lies in another side. The conclusion is universal, unlike the finite experiment on page 1.
- The worksheet deliberately measures gaps at vertices. That is a sound elementary model and already witnesses arbitrarily large grid thinness. The tree conclusion also holds throughout continuous edges. Do not claim these vertex tests alone compute every possible continuous-edge triangle constant; that extra assertion is neither needed nor printed.

## Visual and operational review

- Correct consistent headers, Grades 4–5 labeling, footer IDs, and Problem 1–5 numbering. No overflow, missing symbols, collisions, clipped lines, or extra blank pages were found.
- Tree branches are clear and large enough for adjacent colored traces. The shared-color convention is especially important here and should be preserved. Homes remain the children's choice in Problem 1.
- Page 2's boards have 16 mm spacing. Page 3's 2-, 4-, and 6-unit boards use about 15.5, 13, and 12.5 mm spacing, respectively. These are workable pencil-route boards; the task does not require manipulatives sized to fill cells. The grids have equal x/y scaling within each board.
- Different physical scales across page 3 do not change mathematical distance: unit edge counting is expressly stated at the beginning, and visible dot counts make the three board sizes distinguishable. Do not infer a ruler-length gap from their printed sizes.
- Page 4 intentionally provides free drawing space for an arbitrary-size plan rather than a misleading fixed grid. This is justified by the previous three concrete boards. The two explanation regions are ample.
- Three colored pencils/string paths and home markers are ordinary materials. A partner checks shortestness and tries to defeat an overlarge gap claim, so legality is not held only in the pupil's head. Actual marking/erasing and counter fit still need rehearsal.

## Depth and age fit

The Grades 4–5 gate is honest. This packet combines shortest routes, three simultaneously retained sides, overlap, and a minimum distance to the union of two sets. The source README identifies these prerequisites. The first page permits concrete drawing and partner choices, while the general proof demands are late. The board optimization and adversarial partner check can sustain substantial work even after the basic gap pattern becomes visible.

A potential learning difficulty is confusing the distance to a particular circled point on another side with the distance to the entire side. The definition and the worked point-to-side example already address this adequately. Observe it in a pilot; do not add a long procedure or prematurely supply the maximizing corner construction.

## Revision priority

Optionally define “tree” before the universal claim, keep the existing instances and open route choices, then inspect every re-rendered page if anything changes. No weakening of the arbitrary-size or universal-tree tasks is warranted.
