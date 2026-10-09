# Week 82 independent mathematical review

Reviewed the selected Grades 3–5 packet `draft/students.pdf`: all four task pages and all three material pages. Independently rendered the actual PDF and viewed pages 1–7. Also compiled the root facilitator source into a review-only temporary directory, rendered it, and viewed all four pages. No author/revision source was edited. K–1 and Grades 2–3 packets are deliberately outside the approved scope.

**Verdict:** the mathematical targets, diagrams, and infinite-order obstructions are correct. Clarify the universal condition in the shared order-preservation rule. The guide should also supply the missing finite catalog and invention-task examples. These are small corrections, not reasons to change the selected grade gate or mathematics.

## Located issue: universal pair condition

- **Band/page/problem:** Grades 3–5, page 1, shared rules before Problem 1.
- **Exact text:** “It keeps order when two customers and their partners appear in the same order.”
- **Evidence:** order preservation must hold for *every* pair. The match R1→B1, R2→B3, R3→B2 preserves the order of R1/R2 but reverses R2/R3. Under a literal “some two customers” reading it passes; under the intended definition it fails. The independent exhaustive checker finds six bijections and only R1→B1, R2→B2, R3→B3 preserves all three pair relations.
- **Smallest fix:** insert “any” before “two customers,” or use “Whenever one customer is before another, its partner must also be before the other's partner.” The existing worked visual is otherwise correct.

## Guide completeness: two missing solutions

- **Location:** facilitator page 3, “Facilitator explanations and hints,” which begins with the infinite prepending argument and does not cover Problems 1 or 4.
- **Evidence/expected additions:** Problem 1 has all six partner sequences `(1,2,3), (1,3,2), (2,1,3), (2,3,1), (3,1,2), (3,2,1)` when listing the B partner of R1,R2,R3. Exactly the first keeps order. For Problem 4, an endless row alone versus star followed by the row is a valid pair of different arrangements admitting an order-preserving match. A row alone versus row followed by a star is a valid pair admitting a size match but no order-preserving match. Each uses the permitted one row and at most two stars.
- **Smallest fix:** add a short Problem 1 paragraph and these two sample constructions with their inverse/last-customer checks. In the Problem 3 explanation, prefer the page's R/B labels to fresh A/B labels: D→E can simply match each Rn to Rn and each Bn to Bn, ignoring order. State that labels/colors identify customers and do not constrain whom they may match.

## Problem-by-problem verification

### Page 1, Problem 1

Asks for all bijections between the three red-numbered customers and three blue-numbered customers, and which keep left-to-right order. The six permutations above are exhaustive; a bijection is determined by R1's three possible partners, R2's two remaining possibilities, and R3's final partner. The order-preserving map is unique because the first customer must go to the first, then the second to the second. The source coordinates and rendered diagram correctly show two three-customer queues in that order. Shapes→letters in the preceding worked visual correctly demonstrate that customer symbols need not be equal.

### Page 2, Problem 2

A is the ordinary endless queue; B has a star before it; C has a star after *every* numbered customer, displayed in a separate labeled panel. Both B and C have a size bijection to A: star↦1 and n↦n+1. For every target m, its unique inverse is star if m=1 and m−1 if m≥2. This covers all target customers and proves both injectivity and surjectivity, rather than relying on a finite drawing.

For B, the star is first and the numerical shift preserves every before/after relation. For C, no order-preserving bijection exists: its star is last, and an order-preserving bijection would make its image last in A, whereas every A customer m has successor m+1. The picture does not place C's star after merely the printed customer 3. The continuation arrow is labeled as an instruction, not a customer. These distinctions pass.

### Page 3, Problem 3

D consists of all R customers followed by all B customers. E consists of R1,B1,R2,B2,… . Matching identically named customers gives a bijection D↔E with identity inverse; matching their positions to the ordinary numbered queue gives Rn↦2n−1 and Bn↦2n, with inverse m odd↦R((m+1)/2), m even↦B(m/2).

An order-preserving bijection is impossible. B1 in D has infinitely many predecessors, including every Rn, and has no immediate predecessor. Every E customer has finitely many predecessors (Rk has 2k−2 and Bk has 2k−1); each except R1 has an immediate predecessor. Any order isomorphism would map the entire predecessor set of B1 bijectively onto the predecessor set of its image. That cannot turn infinite into finite. D's separate blue row is explicitly after every red customer; E's arrow lists the continuing alternating pattern. Both rendered diagrams agree with the mathematics.

### Page 4, Problem 4

Asks children to create an order-compatible pair and an order-incompatible but size-compatible pair from one or two endless rows and at most two stars. The guide samples above satisfy all constraints. This is an existence/invention task, not an asserted exhaustive student catalog.

For an optional adult check, all 16 unlabeled row/star concatenations have order type ω·k+t, where k is the number of rows (1 or 2) and t is the number of stars following the final endless row (0,1,2). A finite block before an endless row is absorbed by an explicit finite shift; it does not create a last customer for that block's whole order. Thus there are six order types among these arrangements. All are countably infinite in cardinality. The blank boards do not reveal the intended examples.

## Materials and guide assumptions

Pages 5–7 correctly supply four continuation strips, R1–R12/B1–B12 cards, four extra star cards, and separate “after EVERY” customer/row panels. Printed finite customers plus a continuation rule represent a specified infinite order; they do not claim to be physically infinite. The repeated copies support multiple comparisons and are not extra customers within a single queue. The diagrams retain distinct R/B labels, so color alone is not necessary to distinguish customers.

The guide begins with actual order-type facts and states Grades 3–5 readiness, the infinite schematic demand, bijection/inverse verification, and unpiloted/physical-fit limits. Its distinction between ordinary ordinal concatenation and commutative surreal addition is essential and correct: ordinal 1+ω=ω while ω+1 differs; surreal addition instead has 1+ω=ω+1. No student page imports surreal addition into these queue operations. The optional ω² rows are accurately teacher-led continuation, not an assessed core theorem.

## Independent computation and limits

`independent-math-check.py` imports no author code. It exhaustively checks all six finite bijections, separately verifies the non-universal-order counterexample, replays both explicit infinite inverse formulas through 10000, and checks the symbolic finite concatenation catalog used for adult examples. It writes input SHA-256 hashes and results in `independent-math-results.json`.

The general infinite claims rest on the arbitrary-customer inverse and obstruction arguments above, not on a finite prefix test. No mathematical gap was found in those arguments. No physical fit, printing, yarn handling, timing, or classroom rehearsal was performed. No claim of classroom validation or proof-assistant certification is made.
