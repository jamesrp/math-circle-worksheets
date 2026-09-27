# Week 1 redesigned around mathematical questions

September 19, 2026. The first draft offered valid small optimization puzzles, but the middle group's color restriction did not develop far enough, and the upper question ended too soon. The replacement begins with mathematical questions that remain interesting when the board gets larger: **existence, obstruction, optimality, completeness, and reconfiguration**. Children still start with blocks and experiments; their endpoint is an explanation, a generalization, or a new question.

**K–1 update, September 23:** the historical K–1 trade/flip proposal below is superseded by [four pages of easy shape-filling mats](week-01-k1-shape-mats.md), F01-K-v3. Middle and upper investigations continue unchanged. The current activity guide and facilitator PDF reflect the replacement.

## The actual materials

The organizer has 21st Century Pattern Blocks and many Upscale sets containing triangle/rhombus/trapezoid/hexagon at 1×, 2×, and 3× scales. The measured small green edge is approximately one inch, consistent with [the designer's one-inch description](https://talkingmathwithkids.com/blog/minnesotas-largest-pattern-block-mosaic/) and [compatibility statement](https://talkingmathwithkids.com/blog/21st-century-pattern-blocks-scaling-up/). The mats remain at nominal 25.4 mm; print calibration handles unresolved 25 versus 25.4 mm manufacturing differences.

The absence of a square does not prevent any core investigation. The purple **chevron** (concave hexagon) is a useful new tile precisely because it can be replaced by two small blue rhombi. Pink right triangles provide a contrasting new tile that changes tileability. Teal kites and gray darts remain available during free exploration and are reserved for future questions; they are not silently admitted into an argument whose premises concern blue rhombi.

The Upscale pieces provide exact physical boundary templates. They also support a mathematical distinction: scaling a puzzle and all its pieces preserves its combinatorics, while refining a board into smaller tiles can change the configuration space dramatically.

## What the research suggests teaching

| Mathematical question | Concrete investigation | Where the mathematics continues |
|---|---|---|
| **Can it be tiled?** | Four-cell triangle versus four-cell parallelogram, using blue rhombi. Same area; different answers. | Coloring invariants; necessary conditions; tilings as perfect matchings. |
| **What is the best possible packing?** | Cover a side-three triangle with as many blues as possible, then fill the unavoidable gaps with greens. | A matching upper bound and construction; the side-n theorem; extremal combinatorics. |
| **Does a new tile change what is possible?** | Purple can be replaced by two blues, so it cannot rescue a blue-impossible region. Two pink triangles can fill the side-two triangle. | Reductions between decision problems; the importance of a theorem's assumptions. |
| **How many solutions exist?** | Find the six tilings of the 1,2,2,1,2,2 hexagon and classify them by two-left/two-right ribbons. | Bijections, lattice paths, order ideals, plane partitions, exact enumeration. |
| **Can small changes reach every solution?** | Draw the six-state graph of three-rhombus flips. | Connectivity of tiling spaces, boundary conditions, height functions. |
| **What is the shortest sequence?** | A to F takes four flips; prove that a smaller number cannot work. | Graph distances, inversion statistics, potential functions and height-distance formulas. |
| **What does random play sample?** | Later: choose a random legal flip and compare visits to the six states. | Stationary distributions, mean return times, mixing times, random tilings. |

These are actual instances of the mathematical objects, not merely activities decorated with advanced terminology.

## The research-level sources

William Thurston's [*Conway's Tiling Groups* (1990)](https://www.ibr.cs.tu-bs.de/users/fekete/oldhp/Sem06/thurston.pdf), especially §4 and printed p. 767, connects boundary information and tilings with group methods and lifted height surfaces. The elementary activity does not teach tiling groups; it retains the central move of extracting information from a tiling that rules out an impossible goal or limits a sequence of moves.

Saldanha and Tomei's [*An overview of domino and lozenge tilings*](https://arxiv.org/pdf/math/9801111), §3, Theorems 3.1–3.2, supplies the direct continuation: for the relevant simply connected regions, local flips connect all tilings, and height differences determine minimum distances. Our three-blue-hexagon swap is exactly the lozenge flip in this theory. The no-hole and tile-set hypotheses matter; these conclusions should not be asserted for arbitrary mixed pattern blocks.

Cohn, Larsen, and Propp's [*The Shape of a Typical Boxed Plane Partition* (1998)](https://nyjm.albany.edu/j/1998/4-10.html) studies the large-scale random counterpart of these hexagonal lozenge tilings and cube piles. Wilson's [*Mixing times of lozenge tiling and card shuffling Markov chains* (2004)](https://arxiv.org/abs/math/0102193) directly links tiling dynamics with shuffling. We leave the limiting and mixing theorems to the adult research trail; they identify meaningful questions to return to later.

## The undergraduate source trail

There is a direct curriculum connection, not just a thematic resemblance. [MIT 18.312, advanced undergraduate Algebraic Combinatorics](https://math.mit.edu/~apost/courses/18.312-2005/), lectures 20–23, covers domino tilings, Hall's theorem, matching enumeration, and plane partitions/rhombus tilings. Its other topics include inversions, lattices, and lattice paths, all visible in the six-state investigation.

Brian Kell's [CMU polyomino activity](https://www.math.cmu.edu/~bkell/21110-2010s/polyominoes.html) presents the mutilated checkerboard and deficient-board tromino problems. Oscar Levin's [*Discrete Mathematics: An Open Introduction*, §2.7](https://discrete.openmathbooks.org/dmoi4/sec_matchings.html) supplies Hall's theorem and matching. MIT's [*Mathematics for Computer Science*, §5.1.5](https://ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-spring-2015/mit6_042js15_textbook.pdf), printed pp. 119–122, develops the recursive construction for a 2^n by 2^n square board with any one cell missing.

The checkerboard obstruction transfers naturally to up/down triangles paired by rhombi. The L-tromino theorem does **not** automatically transfer to a chevron: four triangles are not three squares. Its strong induction/divide-and-conquer question is worth a future session with paper square-grid tiles, starting at 4×4 and extending to 8×8.

## The revised hour by entry level

**Default rhythm:** 0–10 materials and free exploration; 10–15 brief shared launch; 15–35 group investigation; 35–40 movement/reset; 40–55 continue or choose an optional proof; 55–60 share and tidy. One adult stays mainly with KK1 while the organizer alternates between 333 and the fifth grader. Stop with a worthwhile explanation; none of the continuations below is required to finish the hour.

| Group | Satisfying stopping point | Optional explanation or proof continuation |
|---|---|---|
| K–1 | Make and check a fair trade for the purple outline. | Demonstrate a hexagon flip and undo it, explaining what stays fixed. |
| 2–3 | Tile the parallelogram and explain why the equal-area T2 cannot tile with blues. | Construct a three-gap T3 packing and prove fewer gaps are impossible; then test a new tile. |
| 4–5 | Explain a shortest A-to-F route in the supplied six-state graph. | Prove completeness using ribbons, or prove the odd-return obstruction. |

**K–1: a fair trade, then a reversible local move.** Build the purple chevron using blues and then greens. Check by superimposing the original. Fill a small hexagon with three blues and find the other arrangement; keep the outside fixed and undo the move. The mathematical ideas are decomposition and a local transformation that preserves a boundary. Reading, writing, and numerical proof are optional. For children who want more, find the little flippable hexagon inside a larger picture.

**Grades 2–3: impossibility becomes a provable optimum.** First try the two four-cell boards. Every blue covers one up and one down triangle, so the 3-up/1-down triangle cannot tile. Then optimize the side-three triangle: six up and three down spaces force at least three gaps; an explicit packing attains three. With green fillers, this is a minimum of three greens. The pattern generalizes to exactly n greens in a side-n triangle: each row has one surplus up triangle, and a systematic pairing attains the bound. Purple does not change the bound because it splits into blues. Pink breaks the pairing premise and rescues the side-two triangle. A balanced six-cell bottleneck is a reserve counterexample to “equal counts always suffice.”

**Grades 4–5: classify the solutions and optimize their transformations.** Use eight small blues in the specified hexagon. After attempts, supply the six state cards. A legal move exchanges the two fillings of a small three-rhombus hexagon. The complete graph is A–B, the diamond B–C–E–D–B, and E–F. Four moves are necessary and sufficient from A to F; all returns have even length. A ribbon crosses each tiling in two left and two right steps. Its six possible orders prove completeness; swaps of adjacent unlike steps correspond to flips. The number of L-before-R pairs proves the four-move bound without requiring formal height notation.

Finding all six states and explaining a shortest route can occupy the whole older session. The six cards alone do not prove the list exhaustive. Until the ribbon argument, explicitly describe completeness as supplied or awaiting explanation; a proof about routes in the supplied graph is still a substantial result. The ribbon proof is an extension to offer when useful, not a demand that every child master several representations in one hour.

## Why the cup example is a useful design test

The point is the progression from concrete moves to a state graph, then to a question that survives enlargement. The new upper activity has exactly that progression. It also offers a useful surprise: six states do not by themselves imply mean return six.

For uniformly chosen **legal** flips, degrees are (1,3,2,2,3,1); stationary occupancy is degree divided by 12, and mean first positive return to A is 12 moves. Choose uniformly among four fixed interior locations instead, counting failed attempts as stay-put turns, and the symmetric chain has uniform occupancy and mean return six turns. The three-cup transposition graph is regular, so its uniformity is a feature of the transition rule, not simply the number of pictures. These are adult follow-ups for now.

## Keeping future sessions substantive

For a proposed activity, record the question, the child's available experiments, what would count as a convincing explanation, and how the question changes when a parameter or rule changes. A source connection is useful when it helps choose those questions. It should not replace time to play or turn the session into a lecture about advanced mathematics.

The prior Lowell hexagon work means the tiny hexagon is a launch or young-child entry, not the main problem for returners. The new middle obstruction and upper state graph provide different mathematical work. The original minimum-piece puzzles remain preserved as reserves. Actual use is still unrecorded; no child is assumed to have completed a printed page.

See the [packets and LaTeX](../lowell-math-circle-year-2/source/week-01/README.md), [detailed undergraduate constructions](week-01-undergraduate-notes.md), and [research proofs/data](week-01-research-level-notes.md). The enumeration script verifies finite claims; the facilitator guide provides mathematical explanations independent of the program.
