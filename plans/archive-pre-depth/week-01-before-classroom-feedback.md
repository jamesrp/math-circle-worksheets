# Week 1 plan before September 27 classroom feedback

Historical plan only; see the current activity guide and classroom review for revised tasks and actual-use evidence.

## Week 1: Tiling, impossibility, and flips

**Revision:** September 23, 2026 for K–1; activity IDs **F01-K-v3 / F01-M-v2 / F01-U-v2**. Use the organizer's **21st Century Pattern Blocks**, which have no square. The earlier color-ban/minimum-piece tasks are preserved below as an untaught reserve. They minimized **piece count**; the target area was fixed.

**Mathematical questions:** When is a tiling possible? How can we prove a packing has the fewest gaps? Can one tiling be changed to another by small moves, and what is the shortest route? These are concrete instances of invariants, matchings, optimization, enumeration, and tiling flip graphs. The [undergraduate notes](/Users/jamespfeiffer/math-circle/plans/week-01-undergraduate-notes.md) and [research notes](/Users/jamespfeiffer/math-circle/plans/week-01-research-level-notes.md) give the source trail and checked mathematics.

**Prepare:** use the [Week 1 print packet](/Users/jamespfeiffer/math-circle/lowell-math-circle-year-2/source/week-01/README.md), or trace the specified shapes at the size of the actual blocks. Use **1× pieces only** for the core investigations; the small green equilateral triangle is the unit. The organizer also has many Upscale Pattern Block sets with green, red, blue, and yellow pieces at 1×, 2×, and 3× scales. Sort those sizes before the constrained puzzles. The designer's [mosaic account](https://talkingmathwithkids.com/blog/minnesotas-largest-pattern-block-mosaic/) gives a nominal one-inch edge and the [scaling-up account](https://talkingmathwithkids.com/blog/21st-century-pattern-blocks-scaling-up/) discusses compatibility with existing blocks. The organizer measured a green edge at approximately one inch, without resolving 25 mm versus 25.4 mm. Print at Actual Size and compare the calibration line with a physical 1× green or blue edge. If the fit is off, trace the actual pieces; the 2× and 3× green triangles give exact T2 and T3 outside boundaries for this kit.

A 132-piece set has **24 green, 18 blue, 12 red, 12 yellow, 12 purple, 24 pink, 18 teal, and 12 gray** pieces. The simultaneous core investigations for this roster need **35 1× blues, 45 greens, and 12 purples**: each of KK1 has 6 blues, 12 greens, and 3 purples; each of 333 has 3 blues, 3 greens, and 1 purple; the fifth grader has 8 blues. Add 2 pinks per middle child and a few reds/yellows per K–1 child. Reuse blocks from one mat to the next. Gather small blues and greens across the Upscale sets; one standard 21st Century set alone is insufficient. The packet's twelve-rhombus cutout sheet is an optional backup. Let all pieces be available during free exploration; introduce each investigation's allowed pieces separately.

Make or print these mats:

- Four K–1 pages per child, with ten blank full-size mats and eight distinct shapes. Print all four; offer them one at a time.
- For each middle child, an upward equilateral triangle of side two (**T2**, four unit-triangle cells), a four-cell parallelogram made from two blues, and an upward equilateral triangle of side three (**T3**, nine cells). Keep the triangular grid visible.
- For the upper child, the hexagon **H122** with consecutive side lengths 1,2,2,1,2,2, requiring eight blues, plus the fixed-orientation A/F reference tilings and blank recording diagrams. Mark the same edge or corner on every copy. Keep the complete six-state answer gallery hidden initially.

**Shared launch:** after ten minutes of handling and free building, point to an outline: “Can you fill this shape?” Let children place the first pieces, then send them to their own mats.

### K–1 — Fill a shape · F01-K-v3

**Prerequisites:** match boundaries and turn pieces; no independent reading, writing, counting, or arithmetic. Reasoning: combine pieces into a whole and compare different fillings of the same outline.

**Materials and preparation:** 3 purples, 12 greens, 6 blues, and a few reds/yellows per child; four printed pages; pencil for optional adult tracing. Check print scale. Reuse pieces after each filling.

**First 20 minutes:** fill the sailboat and cat freely, then try the paired hexagon and diamond mats. Trace one filling before lifting the blocks. Any changed piece arrangement or mixture is another way; no requirement to discover a formal flip.

**Next 15 minutes:** choose the chevron-only arrow and star, or the blue-only long hexagon and green-only mountain. Refill with a different mix afterward. Include the shared movement/reset break. Children can stay with a favorite shape rather than finish every mat.

**Ask:** “Which piece fits this corner?” “What happens if you turn it?” “Can you fill it another way?” **Hint:** offer just one starting piece, or turn a piece beside the mat. **Easy extension:** refill, compare with a partner, or make and trace a new outline. Offer the existing 2–3 packet if a child wants harder work.

**Satisfying stop:** fill and check an outline. **Facilitator solutions:** sailboat 11 greens; cat 7 greens; hexagon 1 yellow, 3 blues, or 6 greens; diamond 4 blues or 8 greens; arrow 2 purples; star 3 purples; long hexagon 5 blues; mountain 9 greens. These are examples, not minimum-piece goals. The facilitator PDF shows the two chevron constructions. See the [full mat notes and exact geometry checks](week-01-k1-shape-mats.md). Record the specific shapes and rules used, not merely “Week 1.”

### 2–3 — Can it fit? How few gaps? · F01-M-v2

**Prerequisites:** count through nine with support and distinguish triangle orientations; all prompts may be spoken. Reasoning: test a conjecture, find an invariant, and combine an example with a reason it is optimal. No multiplication or area formulas are required.

**First 20 minutes:** try to fill the four-cell parallelogram and T2 using **blue rhombi only**. Piece edges must follow printed triangle edges; no overlap, overhang, or stacking. Both regions have room for two blues by area. Does that guarantee both work? Let children experiment before inviting them to mark up-pointing and down-pointing triangle spaces differently.

**Next 15 minutes:** on T3, cover as much as possible with blues and count the **uncovered unit-triangle spaces**. Green triangles may mark those gaps. Try to leave fewer gaps, then explain why the best construction cannot be improved. If there is time, allow purple chevrons and ask whether this can reduce the number of gaps. Keep the objective as gap count or green fillers; total block count is a different question.

**Ask:** “What two kinds of spaces does each blue cover?” “Can every up-pointing space find a down-pointing partner?” “What would change if we split every purple into two blues?” **Hint:** first put two greens over one blue and turn the pair; then compare the orientations on the mat. **Further:** draw a side-four triangle and predict its minimum gaps before building. Save the balanced six-cell bottleneck from the undergraduate notes for a later session or a child who wants a new challenge; it is not part of the required hour.

**Satisfying stop:** tile the parallelogram and explain T2's obstruction. **Optional proof:** find a three-gap T3 packing and show why fewer gaps cannot work, then test what changes when purple or pink is allowed.

**Facilitator check:** the parallelogram tiles with two blues. T2 has three up cells and one down cell, while each blue covers one of each; it cannot be tiled by blues. T3 has six up and three down cells, so at most three blues fit and at least **three gaps** remain. This is achievable: in a side-three triangle with axial vertices `(0,0),(3,0),(0,3)`, pair `U(i,j)` with `D(i,j)` for `(i,j)=(0,0),(1,0),(0,1)`, leaving `U(2,0),U(1,1),U(0,2)`. Here `U(i,j)` has vertices `(i,j),(i+1,j),(i,j+1)` and `D(i,j)` has `(i+1,j+1),(i+1,j),(i,j+1)`; the basis directions are one green edge right and one green edge up-right. The printed answer diagram gives the same construction without coordinates.

Each purple is two blues, so any blue/purple tiling can be converted to all blue: purple cannot rescue a blue-impossible region or reduce T3 below three green fillers. For a side-`n` triangle, each row has one extra up cell. Thus at least `n` fillers are necessary; pair `U(i,j)` with `D(i,j)` whenever `i+j<=n-2` to attain exactly `n`.

**Different objective:** on T3, purple reduces the minimum total block count from six to **five**, while the minimum greens remains three. Use purple on `U(1,0),D(1,0),U(1,1),D(0,1)`, blue on `U(0,0),D(0,0)`, and greens on `U(0,1),U(0,2),U(2,0)`. The facilitator guide illustrates it. Four total blocks cannot suffice: at least three would be greens, and one additional piece covers at most four more triangle units, totaling at most seven of the required nine.

**Optional change of assumptions:** now allow the pink right triangles. **Two pinks fill T2**, meeting along its altitude. Pink has side lengths `1, sqrt(3), 2` in green-edge units. The long side of each pink follows one length-two outer side; their long legs share the altitude, and their short legs divide the base. The original up/down proof required every permitted piece to be a union of whole paired triangular cells. Pink cuts across those cells, so that proof no longer applies. This is a useful changed-rule experiment, not a contradiction. The designer's *Five Fun Things*, “Compare Side Lengths,” supplies the short-side/hypotenuse relationship; the packet's kit notes document the geometry.

### 4–5 — Six tilings and the shortest route · F01-U-v2

**Prerequisites:** match a tiling diagram, count small sets, and reason about odd/even numbers. No independent technical reading, algebra, or probability is needed. Reasoning: explore a state space, distinguish an observed list from an exhaustive one, prove a shortest route, and find a parity obstruction.

**First 20 minutes:** give the child eight blues and H122. Let them find a filling before showing tiling A. Demonstrate a flip using three blues in a separate unit hexagon. Then ask them to change A into F using only these flips and record the intermediate tilings. Keep the marked side fixed: tilings that occupy different internal positions count separately; the blue pieces themselves are indistinguishable.

**Next 15 minutes:** collect tilings on cards, link two cards when one legal flip connects them, and improve the A-to-F route. Ask whether every possible tiling has been found and how they could check. Offer the checked six-state gallery when needed so the child can investigate distances even if exhaustive enumeration is unfinished. Do not equate finding six examples with proving there are only six.

**Satisfying stop:** explain a shortest route in the supplied six-state graph. **Optional proof:** use ribbons to exclude a seventh tiling, or establish the odd-return obstruction. Until completeness is explained, record it as supplied rather than proved by the child.

**Ask:** “Which three pieces could move together?” “Could two different first choices reach the same later tiling?” “How do you know three moves cannot reach F?” “Can you return in three flips?” **Hint:** label the states and draw a line for each verified one-flip change. **Extension:** find two different shortest A-to-F routes, or find the distance from C to D. Probability and larger-board enumeration are reserves for later discussion.

**Facilitator check:** H122 has sixteen unit-triangle cells and exactly six tilings, A–F. Their complete flip graph has edges **A–B, B–C, B–D, C–E, D–E, E–F**. Exhaustive matching enumeration and all legal flips are checked in the research notes and verification script. The shortest A-to-F routes are **A–B–C–E–F** and **A–B–D–E–F**, both four flips. Assign levels `0,1,2,2,3,4` to A–F; every edge changes level by one, so four is a lower bound as well as an attained route. Every flip switches level parity, so every return has even length. C-to-D takes two flips, via B or E. The level argument is justified by the complete verified graph, not merely the subset a child happened to draw.

**Adult continuation:** these levels encode cube counts in a two-by-two-by-one box; the flips add or remove a cube. Randomly choosing among currently legal flips produces long-run state weights proportional to degree, `(1,3,2,2,3,1)/12`, not uniform weights. Mean first positive returns to A–F are `12,4,6,6,4,12` flips. This direct connection to the cup-swapping example is optional adult material; the core hour needs neither probability nor the general theorem. The research notes specify the random rule and explain the different uniform-sampling rule.

**Optional scale investigation:** scaling both a board and every permitted piece by two preserves its tilings and flip graph. Use three 2× blues on the outline of a 2× yellow hexagon: there are still two fillings. Keep that larger hexagon but switch to 1× blues and the question changes: it takes twelve pieces and has twenty tilings. This is a later extension about what similarity preserves and what changing relative scale changes, not an extra required task.

**Adult route / closing:** the parent stays with KK1 while the organizer starts 333 and then returns regularly to the fifth grader's route and graph. At closing, share one K–1 filling, one reason a tiling fails, and one shortest-route argument. Ask for one discovery, not completion of every reserve question.

**Sources and returners:** the pieces and exact instances are our adaptations. Lowell Handout 3, problem 3.4, already used multiple hexagon fillings; the youngest task adds an explicit reversible flip, while the upper task uses the larger H122 state graph. Undergraduate lineage includes CMU's polyominoes activity, Levin's matching chapter, and MIT's combinatorics courses; Thurston's *Conway's Tiling Groups* and subsequent work on lozenge flips, height functions, and random tilings supply the research direction. See the linked research notes for exact sections and limitations. Mark only the instances actually encountered in the use log, including whether pink, the all-`n` argument, or probability was introduced.

