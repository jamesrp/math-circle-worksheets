# Week 2 redesign: pair switches, parity, and cheapest repairs

Prepared September 19, 2026. Replaces the old missing-stroke core. The [print packets](../lowell-math-circle-year-2/source/week-02/README.md) and four-page facilitator guide contain the full prompts, hints, checked solutions, and adult explanations. Grade bands are entry points; these activities have not yet been recorded as taught.

## The mathematical destination

Which targets can local moves reach, and what is the shortest move list? A reversible pair-toggle system connects concrete two-sided counters to parity, symmetric difference, binary incidence matrices, cycle spaces, and minimum-cardinality T-joins. Children prove something about **every** target, not merely repair a few pictures. The five-ring optimization is intentionally small enough to classify completely. Its depth comes from proving reachability, exactly two reduced solutions, and global optimality.

The original shape-union activity remains an optional one-minute bridge. Union retains a shared stroke once; toggling cancels an overlap. Thus symmetric difference has an undo identity that union-plus-deletion lacks. Do not mix these operations without announcing the change.

## Levels, prerequisites, and checked endpoints

| Level / identifier | Entry requirements | Investigation and result |
| --- | --- | --- |
| K–1 / F02-K-v2 | No reading; match two faces, count/pair up to four; follow both-endpoints rule. | Make adjacent and opposite pairs on a four-ring, undo moves, investigate one ON lamp. Pair-flips preserve even parity; a new singleton switch breaks it. |
| 2–3 / F02-M-v2 | Labels 1–4, counts to four; odd/even may be physical pairing. | Classify all eight reachable states: empty, six pairs, all four. A path toggles only its endpoints, proving each pair is reachable. |
| 4–5 / F02-U-v2 | Count to six, record yes/no; reason by exhaustive choices and bounds. | On a five-ring, targets {1,3} and {1,2,3,4} each need two presses. Choosing edge 51 forces all others. Every even target has exactly two complementary reduced edge sets; choose the smaller. Every achievable target needs at most two presses. On a six-ring opposite endpoints require three, with a tie. |
| Extra 6–7 / F02-X-v2 | Paths/components, parity, cut reasoning; no formal algebra needed. | Every component must have an even target count, and that is sufficient. On a tree, each edge is forced by parity on one side after cutting it; the reduced solution is unique. |

“Reduced” means each edge is used zero or one times. Repeated edges cancel and commute, so they cannot improve a shortest solution. There are infinitely many unreduced lists, not merely two lists. For the five-ring target {1,3}, the reduced solutions are {12,23} and {34,45,51}. A single press cannot light two nonadjacent lamps. For {1,2,3,4}, the solutions are {12,34} and {23,45,51}; one press cannot light four lamps.

For any connected graph, pair the desired ON vertices and press paths joining each pair. All intermediate contributions cancel. For disconnected graphs, do this within each component. Necessity follows because each move flips two lamps within one component. On the extra graph, A/D alone is impossible despite even total cardinality; A/C/D/E is made by AC and DE. For a tree, only its cut edge changes the parity on one side of that cut. Thus an edge is pressed an odd number of times exactly when one side contains an odd number of targets. This proves the forced-edge rule; existence follows from the path construction. The solution using each edge at most once is unique and shortest; unreduced lists can insert cancelling pairs of presses.

## Practical hour

For K,K,1 / 3,3,3 / 5 and two adults, prepare 29 two-sided counters (4 per youngest/middle child, 5 for upper), 8 spares, pencils, and mats. Paper circles with a shaded back work; coins work if faces are distinguished. No electronics or special kit. Print 3 K packets, 3 middle packets, 1 upper packet, and 1 extra in reserve. Adult A anchors the youngest triplet; organizer alternates between the middle and upper, returning to hear the fifth grader's proof. Triplet mover/target-maker/checker roles rotate, with each child retaining their own manipulatives.

- **0–10:** explore counters and make pictures freely.
- **10–15:** demonstrate one edge press and its undo. Launch: “Can we make any picture we want?”
- **15–35:** K pair targets; middle target collection; upper cheapest solutions. Adult A anchors K; organizer visits middle and upper.
- **35–40:** movement/reset break; stand, stretch, and leave the work ready to return to.
- **40–55:** continue the collection or use the optional proof paths below; offer the six-ring/extra only if wanted.
- **55–60:** share one discovery or impossibility; tidy counters.

Useful hints: check that an ON lamp flips OFF; classify both OFF/both ON/mixed endpoints; count touches at an interior path vertex; cover later columns in the forced-choice table and decide one edge at a time. A child who stalls can stay on four lamps and explain by demonstration. The extra is not required and may be kept for a later year.


### Satisfying stops and optional proofs

- **K–1 stop:** make and undo two pair targets. **Optional proof:** explain why a singleton is impossible by pairing the ON lamps.
- **2–3 stop:** collect the eight four-lamp targets. **Optional proof:** show why odd targets fail and why paths make every pair.
- **4–5 stop:** find shortest solutions for the two five-ring targets, with a reason one press fails. **Optional proof:** explain why each first-edge choice forces the rest, then use complements to prove every reachable target needs at most two presses.

These are choices for the shared hour, not a requirement to finish the packet. At the stop, continue playing or comparing examples if that suits the child. Record whether each result was tried, conjectured, verified in these cases, proved, or given as a theorem.

## Sources and boundaries

- **Undergraduate representation:** MIT 18.06SC, [Graphs, Networks, Incidence Matrices](https://ocw.mit.edu/courses/18-06sc-linear-algebra-fall-2011/pages/ax-b-and-the-four-subspaces/graphs-networks-incidence-matrices/). Its graph-matrix framework motivates our incidence matrix; adapting it to the two-element field is our classroom construction. The target equation is Ax=t over F₂. On a cycle the nonzero null vector is the all-edge set; on a connected graph the image is the even-parity subspace.
- **Research:** Edmonds and Johnson, *Matching, Euler tours and the Chinese postman*, *Mathematical Programming* 5 (1973), 88–124, [publisher page/DOI](https://doi.org/10.1007/BF01580113). The primary abstract verifies the matching/route-inspection optimization lineage. We do not claim to prove their algorithm.
- **Detailed mathematical reference:** Cornuéjols, *Combinatorial Optimization: Packing and Covering*, [author monograph](https://www.sfu.ca/~mdevos/notes/pack-cover/Cornuejols.pdf), Chapter 2, printed pp. 27–29 (PDF pp. 29–31), especially definition, matching reduction, Theorem 2.1. It takes acyclic T-join representatives; with nonnegative costs cycles can be removed without changing odd-degree vertices. Our general parity edge sets may include cycles; a minimum positive-cost solution does not.
- **Downloaded prior work:** Lowell Handout 11, problem 11.3, splitting/recombining pictures; Handout 9, problem 9.1, toggling doors by divisors. Both were read. The adjacent-pair network and targets are new; this preserves a theme while changing the representation and theorem.
- **Pedagogy actually reviewed:** *Math Circle by the Bay*, preface printed pp. viii–x: deep mathematical themes, manipulatives, changing pace, reserve challenges. Rozhkovskaya, Lesson 3 “At the lesson” item 1 (EPUB `OEBPS/part0013.xhtml`): attempts and explanations before tabular display; Lesson 7 item 1 (`part0017.xhtml`): missed legal moves can distort conclusions. The roster, timing, and role rotation are our adaptations.

## Verification and future progression

`lowell-math-circle-year-2/source/week-02/verify.py` enumerates every edge subset on rings of sizes 4–7, confirms all and only even states, complementary solutions, worst minimum floor(n/2), both upper examples, the disconnected obstruction, and all 32 even targets on a six-vertex tree. Facilitator proofs establish the results independently of enumeration. See the local `REVIEW.md` for PDF inspection.

Record actual target patterns and pages used as F02-K/M/U/X-v2. Future returns can introduce trees, arbitrary edge costs, networks with several independent cycles, or compare symmetric difference with ordinary shape union. Do not label untaught reserves as used.
