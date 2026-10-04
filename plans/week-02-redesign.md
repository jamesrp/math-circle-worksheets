# Week 2 redesign: pair switches, parity, and cheapest repairs

Revised September 27–28, 2026 from the September 19 design. **All revisions are unpiloted.** The current format is the [shared collection](week-02-shared-collection.md): [42 student pages, 50 problems](../lowell-math-circle-year-2/week-02/week-02-shared.pdf), one [adult guide](../lowell-math-circle-year-2/week-02/week-02-shared-facilitator.pdf), and [current build/print notes](../lowell-math-circle-year-2/source/week-02/README.md). Its student ID is F02-S-v1. It supersedes the separate K–1, middle, upper, extra, and auxiliary print routes described in earlier revisions.

## September 28 shared collection and staffing

The organizer approved one shared collection after the [visual revision](week-02-visual-review.md). It combines making and walking puzzles (pp. 1–8), state collection (pp. 9–16), shorter solutions (pp. 17–28), shapes and rooms (pp. 29–34), and networks and trees (pp. 35–42). The same mathematical substance remains available, with local working boards, pictured targets, and adult-supported recording. Begin together; then choose pages by interest and prerequisites. A child may skip familiar work after a couple of successful attempts or begin drawing immediately. Page completion is not a readiness measure.

There are **ten children, KK1 / 3333 / 445, and three adults**: two mathematicians and one parent. Keep the parent with KK1, the other mathematician with 3333, and the organizer with 445 initially. These are coverage anchors, not three mathematical tracks. Use the agreed help handoff before an adult visits another table. Paper and pencil/eraser or whiteboards suffice; existing counters are optional. The current guide supplies the common launch, selected-page print plan, parent scripts, and solutions. All four combined student sets include the same shared Week 2 library; print it only once.

## Historical design record

The following September 19/27 rationale preserves the earlier grade labels and original activity IDs to document the mathematical development. The September 28 auxiliary and visual revisions are documented in their own historical notes. **Their separate packet routes, page numbers, seven-child/two-adult logistics, and earlier combined-packet arrangements are superseded by the shared plan above.** Earlier PDFs and editable sources are preserved under `archive-before-shared-collection-2026-09-28/` beside the current outputs and sources. No historical design or prepared revision is thereby marked taught.

## Applying the Week 1 classroom guidance

The evidence is the organizer's [Week 1 report](week-01-classroom-review.md): short investigations needed more concrete examples, unclear continuation actions required rescue, and unfamiliar representations needed their own work. The changes below are design inferences for Week 2, not observations about children doing these tasks. No v3 packet has been reported taught.

- K: repeat the pair move and its undo; make adjacent, opposite, all-on and empty pictures; try three odd targets; only then add a fixed lamp-1 button. This gives parity several contrasting instances before the rule change.
- Middle: record four successful target constructions, mix possible and unresolved targets, examine the three endpoint cases, then try two explicit paths. Introduce the four-circle state record only when collecting examples; sorting and completeness follow the collection.
- Upper: compare three target constructions, test order and repeated-press cancellation, and test four complementary edge pairs before the forced-choice table. Apply that table to two possible targets and a singleton, then contrast odd/even ring minima. The global reachability and two-press theorem remain available as facilitator proof conversations.
- Extra: six targets on disconnected pieces precede a component rule; adding a bridge tests that rule, and overlapping paths demonstrate cancellation. A supplied six-lamp tree and two targets precede cut-parity prediction. The arbitrary-graph and unique-tree proofs remain in the guide.

Every student page now has the consistent week/topic/level header, v3 footer, and sequential numbered problems with needed diagrams and recording space. Name/date lines, duplicate titles, generic encouragement, standalone rules, and unnumbered continuations are removed. Explanation and general proof opportunities remain in the facilitator; they are invitations after concrete work rather than mandatory writing gates.

**Practical printing:** start with one first page per child (three K, three middle, one upper: seven sheets), plus the facilitator. Keep continuation masters ready and copy selected pages as needed; retain earlier mats when later problems reference them. The extra can remain digital until chosen. Expanded page counts provide time and choices, not a requirement to print or complete every page.

**September 27 suggested stops:** K pair targets; middle contrasting reachability attempts; upper short versus long constructions; extra component examples. Continue the same investigation when that is productive. Introduce each table, loop, or compact record with one replayable example, then let the child use it on more than one case before generalizing.

**Evidence to record next time:** exact problems and instances attempted; what children could replay unaided; where an adult had to demonstrate the task or record again; statements or drawings supporting a conjecture or proof; and what they wanted to continue. Keep observations separate from proposed explanations and revision hypotheses. Track tried / conjectured / checked in cases / proved / supplied, and record v3 IDs only after actual use.

**Teaching-source review for this revision:** reread *Math Circle by the Bay*, preface printed viii–x (deep themes, manipulatives, varied pace, explicit statements, and the limits of predicting lesson duration), and Rozhkovskaya, Lessons 3,7,8 “At the lesson” (attempts and explanation before a table; missed legal moves; copying displacing mathematical work). Those are source observations. The exact staged examples, launch, seven-sheet start, and stopping choices here are our proposals.

## The mathematical destination

Which targets can local moves reach, and what is the shortest move list? A reversible pair-toggle system connects concrete two-sided counters to parity, symmetric difference, binary incidence matrices, cycle spaces, and minimum-cardinality T-joins. Children prove something about **every** target, not merely repair a few pictures. The five-ring optimization is intentionally small enough to classify completely. Its depth comes from proving reachability, exactly two reduced solutions, and global optimality.

The original shape-union activity remains an optional one-minute bridge. Union retains a shared stroke once; toggling cancels an overlap. Thus symmetric difference has an undo identity that union-plus-deletion lacks. Do not mix these operations without announcing the change.

## Earlier levels, prerequisites, and checked endpoints

| Level / identifier | Entry requirements | Investigation and result |
| --- | --- | --- |
| K–1 / F02-K-v3 | No reading; match two faces, count/pair up to four; follow both-endpoints rule. | Make adjacent and opposite pairs on a four-ring, undo moves, investigate one ON lamp. Pair-flips preserve even parity; a new singleton switch breaks it. |
| 2–3 / F02-M-v4 | Labels 1–4, counts to four; odd/even may be physical pairing. | Classify all eight reachable states: empty, six pairs, all four. A path toggles only its endpoints, proving each pair is reachable. |
| 4–5 / F02-U-v4 | Count to six, record yes/no; reason by exhaustive choices and bounds. | On a five-ring, targets {1,3} and {1,2,3,4} each need two presses. Choosing edge 51 forces all others. Every even target has exactly two complementary reduced edge sets; choose the smaller. Every achievable target needs at most two presses. On a six-ring opposite endpoints require three, with a tie. |
| Extra 6–7 / F02-X-v3 | Paths/components, parity, cut reasoning; no formal algebra needed. | Every component must have an even target count, and that is sufficient. On a tree, each edge is forced by parity on one side after cutting it; the reduced solution is unique. |

“Reduced” means each edge is used zero or one times. Repeated edges cancel and commute, so they cannot improve a shortest solution. There are infinitely many unreduced lists, not merely two lists. For the five-ring target {1,3}, the reduced solutions are {12,23} and {34,45,51}. A single press cannot light two nonadjacent lamps. For {1,2,3,4}, the solutions are {12,34} and {23,45,51}; one press cannot light four lamps.

For any connected graph, pair the desired ON vertices and press paths joining each pair. All intermediate contributions cancel. For disconnected graphs, do this within each component. Necessity follows because each move flips two lamps within one component. On the extra graph, A/D alone is impossible despite even total cardinality; A/C/D/E is made by AC and DE. For a tree, only its cut edge changes the parity on one side of that cut. Thus an edge is pressed an odd number of times exactly when one side contains an odd number of targets. This proves the forced-edge rule; existence follows from the path construction. The solution using each edge at most once is unique and shortest; unreduced lists can insert cancelling pairs of presses.

## Earlier September 27 practical hour (superseded logistics)

For K,K,1 / 3,3,3 / 5 and two adults, prepare 29 two-sided counters (4 per youngest/middle child, 5 for upper), 8 spares, pencils, and mats. Paper circles with a shaded back work; coins work if faces are distinguished. No electronics or special kit. Use the seven-sheet starting plan above and selected continuations. Adult A anchors the youngest triplet; organizer alternates between the middle and upper, returning to hear the fifth grader's proof. Triplet mover/target-maker/checker roles rotate, with each child retaining their own manipulatives.

- **0–10:** handle the materials freely.
- **10–15:** gather everyone for one concrete legal attempt and its record: Flip both endpoints of a visible four-lamp mat, first 12 then 23; reset and replay the written move list 12,23.
- **15–35:** K 1–4; middle 1–3; upper 1–2. Adult A anchors the youngest group; organizer visits middle and upper.
- **35–40:** stand, stretch, reset.
- **40–55:** continue, or choose one next stage when the previous action/record is understood.
- **55–60:** share one attempt or explanation and tidy. These are proposed intervals, not a completion schedule.

Useful hints: check that an ON lamp flips OFF; classify both OFF/both ON/mixed endpoints; count touches at an interior path vertex; cover later columns in the forced-choice table and decide one edge at a time. A child who stalls can stay on four lamps and explain by demonstration. The extra is not required and may be kept for a later year.


### Later optional destinations and proofs

- **K–1 later destination:** make and undo two pair targets. **Optional proof:** explain why a singleton is impossible by pairing the ON lamps.
- **2–3 later destination:** collect the eight four-lamp targets. **Optional proof:** show why odd targets fail and why paths make every pair.
- **4–5 later destination:** find shortest solutions for the two five-ring targets, with a reason one press fails. **Optional proof:** explain why each first-edge choice forces the rest, then use complements to prove every reachable target needs at most two presses.

These are choices for the shared hour, not a requirement to finish the packet. The earlier stops above remain complete sessions; choose these later destinations only when useful. Record whether each result was tried, conjectured, verified in these cases, proved, or given as a theorem.

## Sources and boundaries

- **Undergraduate representation:** MIT 18.06SC, [Graphs, Networks, Incidence Matrices](https://ocw.mit.edu/courses/18-06sc-linear-algebra-fall-2011/pages/ax-b-and-the-four-subspaces/graphs-networks-incidence-matrices/). Its graph-matrix framework motivates our incidence matrix; adapting it to the two-element field is our classroom construction. The target equation is Ax=t over F₂. On a cycle the nonzero null vector is the all-edge set; on a connected graph the image is the even-parity subspace.
- **Research:** Edmonds and Johnson, *Matching, Euler tours and the Chinese postman*, *Mathematical Programming* 5 (1973), 88–124, [publisher page/DOI](https://doi.org/10.1007/BF01580113). The primary abstract verifies the matching/route-inspection optimization lineage. We do not claim to prove their algorithm.
- **Detailed mathematical reference:** Cornuéjols, *Combinatorial Optimization: Packing and Covering*, [author monograph](https://www.sfu.ca/~mdevos/notes/pack-cover/Cornuejols.pdf), Chapter 2, printed pp. 27–29 (PDF pp. 29–31), especially definition, matching reduction, Theorem 2.1. It takes acyclic T-join representatives; with nonnegative costs cycles can be removed without changing odd-degree vertices. Our general parity edge sets may include cycles; a minimum positive-cost solution does not.
- **Downloaded prior work:** Lowell Handout 11, problem 11.3, splitting/recombining pictures; Handout 9, problem 9.1, toggling doors by divisors. Both were read. The adjacent-pair network and targets are new; this preserves a theme while changing the representation and theorem.
- **Pedagogy actually reviewed:** *Math Circle by the Bay*, preface printed pp. viii–x: deep mathematical themes, manipulatives, changing pace, reserve challenges. Rozhkovskaya, Lesson 3 “At the lesson” item 1 (EPUB `OEBPS/part0013.xhtml`): attempts and explanations before tabular display; Lesson 7 item 1 (`part0017.xhtml`): missed legal moves can distort conclusions. The roster, timing, and role rotation are our adaptations.

## Verification and future progression

`lowell-math-circle-year-2/source/week-02/verify.py` enumerates every edge subset on rings of sizes 4–7, confirms all and only even states, complementary solutions, worst minimum floor(n/2), both upper examples, the disconnected obstruction, and all 32 even targets on a six-vertex tree. Facilitator proofs establish the results independently of enumeration. See the local `REVIEW.md` for PDF inspection.

Record current use by F02-S-v1 problem number, page, target, and actual mathematical experience. Preserve the older F02-M/U-v4, F02-K/X-v3, and F02-K-AUX-v1 IDs only when identifying their archived materials. Future returns can introduce trees, arbitrary edge costs, networks with several independent cycles, or compare symmetric difference with ordinary shape union. Do not label untaught reserves as used.
