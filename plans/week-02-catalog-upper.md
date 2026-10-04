# Week 2 upper catalog: facilitator notes and checks

Prepared September 30, 2026; **unpiloted**. The organizer's assessment is that the original upper material over-directs children and gives them too much text. This revision responds with six investigations intended to sustain at least five minutes each. These are design intentions, not reported classroom outcomes.

[Student PDF](../lowell-math-circle-year-2/week-02/week-02-shared-catalog-upper.pdf) · [Builder](../lowell-math-circle-year-2/source/week-02/build-shared-catalog-upper.py) · [Instance data](week-02-catalog-upper-data.json) · [Exhaustive checks and exact edge sets](week-02-catalog-upper-checks.json)

## Use at the table

Entry requirements: understand the demonstrated pair flip, compare two pictures, and track a few moves. Adult reading and scribing are fine. Counting to eight helps; odd/even language can emerge from pairing objects. The further reasoning concerns impossibility, shortest solutions, and completeness, without algebraic prerequisites. No grade cutoff is intended.

Materials: this packet, pencils/erasers, and the existing whiteboard tablets or blank paper. Children can enlarge a chosen diagram for counters if useful. Print US Letter at Actual Size. Offer one page at a time; this is a choice library, not an assignment to finish all six pages.

For an hour: allow about three minutes of free experimenting with a small ring, then demonstrate one legal pair flip and one start-to-target attempt to the whole group (two minutes). Point out what the arrow means; do not demonstrate a solving method. Allow two substantial work periods of roughly 15–20 minutes with a short movement break, and five minutes to share discoveries. Select pages by interest. Allow 8–15 minutes for each of Problems 1–3, 10–20 for 4 or 5, and 10–15 for 6; a group may stay on one question longer.

Only Problems 3 and 6 restrict a solution to pressing each chosen line once. A set of lines ignores order. Choosing no lines is allowed. If children count reordered lists as different sets, clarify that vocabulary without revealing the answer. Keep trial work and explanations on blank paper or whiteboards; the student PDF deliberately avoids recording tables and prescribed intermediate steps.

## Investigations and reasoning

**1. Which pictures can be reached?** Six connected graphs, including starts with lights already ON. Answers A–F: possible, possible, impossible, possible, impossible, possible. Expected exploration: try solutions, then formulate a rule. Every move preserves the parity of the number of ON lamps. Equivalently, the number of lamps that differ between start and target must be even. Odd-to-odd transitions in B and D prevent “targets need an even number of lights” from fitting the examples. If needed, ask what happens to the number of lights after one move. To establish sufficiency, pair lamps that need to change and connect each pair by a path. Pressing a path changes only its endpoints. Repeated edges can be canceled in pairs; arbitrary overlaps cause no problem. This construction is an adult follow-up, not a prerequisite algorithm.

**2. Separate pieces and a bridge.** Answers A–F: possible, impossible, possible, possible, impossible, possible. B and C have identical states but a different graph: the new bridge makes the transition possible. D and F have odd numbers of ON lamps in each component both before and after, and are possible. E has an even total but is impossible. The complete rule is an even number of **changed** lamps in every component, equivalently matching start/target ON-count parity within each component. The path-pairing argument works separately in each component. If stuck, ask which lamps can influence a chosen lamp. Extension: invent a network and a pair of equally numerous start/target light sets that still cannot be connected by moves.

**3. All solutions on a ring.** Each case has exactly two sets of lines; they are complements. Their sizes are A: 0 and 4; B: 2 and 3; C: 3 and 3; D: 2 and 5. Pressing the full ring changes every lamp twice, so exchanging used and unused edges has no net effect on the result. To see there cannot be a third set, compare any two solutions: edges belonging to just one set must meet each vertex an even number of times. On a cycle this forces either no edges or the entire ring. A gives a concrete entry through “do nothing”; C provides equal-length solutions on an even ring. If children have one solution, ask whether they can find a solution using a different first line. Do not announce the complement rule before they have compared examples. Optional extension: when would complementing work on a network with branches? Precisely when every vertex has even degree.

**4. Fewest moves.** The minima for A–F are **2, 4, 3, 5, 4, 4**. After a child has a candidate, ask what rules out a shorter solution. Useful lower bounds:

- A: four lamps must change and one move affects two, so at least two moves; the two lit adjacent pairs attain it.
- B: all four target lamps must change, but no line joins two of them, so each move can affect at most one of these four; four moves suffice.
- C: six lamps require at least three moves; use alternating edges.
- D: both endpoints of the bent path must change. Cutting any of its five lines leaves one changed endpoint on each side, so every line must be used an odd number of times. All five suffice.
- E: each of the four leaves can change only through its own line. All four lines suffice; the center changes four times.
- F: no line joins two of the four corners, so at least four moves are needed. Use both top-row lines and both bottom-row lines (or the two outer columns).

These contrast a simple changed-lamp count with stronger bounds coming from the graph. They do not require children to name these techniques. A and B even have the same graph and the same number of changed lamps, yet different minima.

**5. Design the hardest target.** The records on 5-, 6-, 7-, and 8-lamp rings are **2, 3, 3, 4** moves. Here “needs” means the fewest moves a solver can achieve, not a deliberately long solution. For an n-lamp cycle, the complementary solutions have sizes k and n−k, so one uses at most floor(n/2) edges. Two target lamps separated by floor(n/2) edges attain this bound. This is both a construction and a proof that the construction cannot be beaten. Let children trade targets and try to improve each other's solutions before asking for the general rule. If needed, return to the two solutions found in Problem 3. Rings are shown in reading order 5, 6, 7, 8; children draw their own target dots.

**6. All solutions on trees.** A and B have one solution each; C has none; D has just the empty set. A uses the two lines meeting the upper branch point on its left/top and the two lines meeting the lower branch point on its bottom/right; it omits the middle joining line. B uses all six spokes. C has three changed lamps. D needs no changes. Exact numbered edge sets are also in the check JSON; vertex numbers follow the coordinate arrays in the data file and are not printed on student pages.

Every reachable target on a tree has exactly one set of lines. One proof starts at a leaf: its only line is forced by whether the leaf needs to change. Remove that leaf and continue. Another compares two hypothetical solutions; the edges used by just one would form a nonempty forest with every vertex of even degree, but a nonempty forest has a leaf. For a cut-based explanation, remove any edge: it must be pressed exactly when one side contains an odd number of changed lamps. Reachability is still required; “a tree always has a solution” is false. If needed, ask about a lamp with only one neighbor. Extension: add one line joining two existing nonadjacent vertices and investigate how the solution count changes.

## Source and use record

This is a new presentation of *Week 2 / Lamp lab / Shared collection*, original Problems 15–32 and 43–50. Rough correspondence: new 1 draws on 15–22; new 2 on 43–47; new 3 on 24–31; new 4–5 on 24 and 31–32; new 6 on 48–50. Examples are partly new, with varied graphs and starting configurations. The visual reference is the organizer's four-page *week-02-shared-catalog.pdf*. Original PDFs and combined packets remain separate.

Relevant source lessons reviewed: *Math Circle by the Bay*, preface, printed pp. viii–ix (PDF pp. 9–10), advocates substantial themes, independent solving, manipulatives, and statements that are both clear and understandable. Lowell's prior *Pattern Block Exercises – Google Docs*, PDF p. 1, begins with free play and then gives small groups open construction/comparison tasks. **Our inference/application:** retain a short demonstrated action and substantial mathematics, but let one short prompt support a sustained investigation. Neither source specifies our six-page structure or five-minute minimum.

The verifier exhaustively enumerates every edge subset and independently computes state-space shortest paths on all 15 graphs. It checks all 26 printed transitions, the component criterion for every state, complement pairing on each cycle, uniqueness on each tree, and the four hardest-ring records. Every rendered student page has been visually reviewed. Record actual examples attempted, conjectures made, and places needing adult rescue in the existing use log only after use; do not mark these new revisions as taught.
