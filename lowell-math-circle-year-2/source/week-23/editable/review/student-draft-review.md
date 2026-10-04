# Independent adversarial review

## Verdict

The packet is mathematically sound and visually clean. All three PDFs have six US Letter pages, and I found no false assertion, unsolvable promised repair, incorrect comparator, clipped text, or overlapping diagram. The main revision need is problem sequencing: some later construction tasks can be completed by copying machines already obtained earlier. In particular, grades 2–3 Problem 6 does not meet the organizer's requirement that each numbered problem offer at least five minutes of fresh experimenting and thinking.

I recommend targeted revisions, not a rebuild. Preserve the fixed-network rules, the contrasting good and bad machines, the middle packet's incomplete binary certificate, and the older packet's threshold development.

## Findings, in priority order

### 1. Grades 2–3, page 6, Problem 6: both requested answers have already been produced on page 3

**Severity: medium; clear task-design defect.**

Problem 6 asks for two different five-bar machines sorting all orders of 1, 2, 3, 4, where the lists of lane pairs differ. In Problem 3 the first two machines are

- (1,2), (3,4), (1,3), (2,4)
- (1,3), (2,4), (1,2), (3,4)

Appending (2,3) repairs each one, and these give exactly the two different five-bar machines requested on page 6. A child who completed page 3 can simply copy both finished answers. There is no new property to establish or condition to meet. Moreover, even without those two earlier answers, the stated distinction allows a child to obtain a second list just by reversing two consecutive disjoint comparators in one known sorter.

**Revision direction:** replace this with a genuinely new constraint or question, checked independently for feasibility, or consolidate it with the earlier repair problem. Do not count the present page as another substantial problem merely because it supplies two large blank diagrams.

### 2. K–1, pages 2–4: the construction challenge is weakened by displaying its answer first

**Severity: medium; sequencing and pacing risk, rather than a mathematical error.**

The first machine in Problem 2 is the complete three-bar sorter (1,2), (2,3), (1,2). Problem 3 then asks children to build a machine sorting the same three distinct cards, using as few bars as they can. They have just handled a valid minimum construction. The remaining new challenge is whether two bars could suffice, but the task does not specifically ask children to resolve that question or record a reason; copying the previous successful machine is a natural stopping point.

Problem 4 has meaningful new material because it introduces repeated values and the two binary multisets. Still, the exact same machine from Problems 2 and 3 solves its construction request. It may become another six-start verification of a known machine instead of an independent invention problem. This is not grounds to remove the repeated-value task; it is grounds to reconsider when the full sorter becomes visible.

Problem 5 does supply three contrasting repairs, including a comparator that spans the middle lane, and Problem 6 is a substantial four-lane extension. Thus the K–1 packet is not simply too short. The specific concern is that six pages overstate how many distinct construction problems it contains, and its central invention task is already substantially answered.

**Revision direction:** put the first genuine construction opportunity before the complete working example, or make the later task require a genuinely different mathematical decision. Keep the short oral wording and concrete dot cards. Do not fix the pacing by adding hints or a longer written explanation requirement for nonreaders.

### 3. Grades 4–5, page 6, Problem 6: the minimum-count argument is a substantial unprepared jump

**Severity: medium developmental risk; not an incorrect or illegitimate challenge.**

Problems 3–5 give the zero–one argument a real progression: concrete threshold rows, commutation with one comparator, an inverted output, and an audit of two candidate networks. The other stated kernel, the comparison-count lower bound, receives no corresponding concrete development. No earlier task asks children to examine swap/no-swap histories or how many different orders a fixed history can correctly sort. Problem 6 goes directly from constructing/testing networks to ruling out every shorter network on both three and four lanes.

The three-lane lower bound is accessible by a small direct investigation. The four-lane case is different: there are 1,296 four-comparator lists, and removing a bar from one successful five-bar machine does not exclude other four-bar machines. A quick builder can therefore reach the last page without an accessible experimental route toward the intended universal argument. The adult may have to supply its decisive idea rather than help children develop an idea they have already used.

This can be retained as an ambitious final problem, particularly with a mathematician at the table. However, it is the weakest point in the packet's mathematical development and should be reconsidered if establishing the specified counting argument is an important session outcome.

**Revision direction:** consider an earlier, genuine problem about a fixed machine's possible swap/no-swap records or the inputs associated with one record, so the counting object is familiar before the minimum question. Avoid inserting the calculation 24 > 16 or the proof itself as a hint on the final page. Preserve the child's choice of method.

## Independent mathematical checks

I simulated the diagrams from their actual lane-pair lists, independently of the author's saved audit. I used all six distinct three-card orders, all 24 distinct four-card orders, and all binary starts where relevant.

### K–1

- Problem 1's two-bar machine sorts four of the six pictured starts. Its failures are (2,3,1) and (3,2,1), both ending at (2,1,3). All six permutations are pictured once.
- Problem 2's upper machine sorts every start. The lower machine repeats (1,2) and has the same two failures as Problem 1. This correctly distinguishes order of operations from simply having three bars.
- Problem 3 has minimum three. Exhausting all nine two-comparator lists finds no sorter.
- Problem 4 really does require three bars to sort both shown multisets, (0,0,1) and (0,1,1), in all orders. These supply the six nonconstant binary inputs; the two omitted constant inputs sort automatically.
- Problem 5's required final bars are, from top to bottom, (1,2), (2,3), and (2,3). Each promised repair works.
- Problem 6 is feasible with five bars. Its blank diagrams do not disclose the answer by preallocated comparator slots.

### Grades 2–3

- Problem 1: the top machine fails on (2,3,1) and (3,2,1); the middle one fails on (3,1,2) and (3,2,1); the bottom one sorts all six orders.
- Problem 3: the top two machines each have the unique successful appended bar (2,3). No appended comparator repairs the bottom machine. For the latter, input (2,4,1,3) finishes at (2,1,4,3), which cannot be sorted by one further comparison. This supplies an especially concise impossibility witness.
- Problem 4 is a good deliberate trap, not a defective sorter accidentally presented as correct. The machine sorts all six arrangements of two 0s and two 1s, but fails on 0010, 0100, 1000, and 1110. Thus testing only the displayed multiset does not certify all binary inputs.
- Problem 5 is feasible and introduces a genuinely new demand: a complete binary audit, rather than just reproducing a machine.
- Problem 6 is feasible but redundant for the reasons above.

### Grades 4–5

- Problem 1's upper machine fails on the distinct orders noted above and on the repeated-value start (3,3,1). It sorts every order of (1,1,3). The lower machine sorts all of these cases.
- Problem 3 produces respectively four, five, and two distinct threshold rows. In increasing threshold order they are:
  - (-2,8,5,8): 1111, 0111, 0101, 0000.
  - (6,2,9,4): 1111, 1011, 1010, 0010, 0000.
  - (4,4,4,4): 1111, 0000.
  Equal values change together. The rule using values at most t is consistent, including at equality.
- The commutation question and Problem 4's proposed 9-before-4 output correctly support the zero–one principle, including repeated values. Choosing any threshold t with 4 ≤ t < 9 yields the prohibited 1-before-0 output.
- Problem 5's upper machine sorts all 16 binary inputs and all 24 distinct orders. The lower machine fails on binary inputs 0100 and 1000, each ending at 0010. The diagrams correctly differ in comparator order.
- The minima in Problem 6 are three and five. I independently enumerated all nine two-comparator three-lane lists and all 1,296 four-comparator four-lane lists; none sorts. The intended history argument is also valid: a fixed history is a fixed permutation of distinct tokens, so it sorts at most one initial order; 6 > 2² and 24 > 2⁴. No confusion between comparator count and parallel stages appears in the wording.

## Visual and editorial audit

I freshly rendered and visually inspected every page of all three delivered PDFs, rather than relying on the existing preview images or the author's QA file. I also checked text and drawing bounds in the PDFs.

- All 18 pages are 612 × 792 points, US Letter.
- Headers, packet identifiers, and page numbers are present and consistent.
- No text or drawing extends outside a page. I found no collisions, cropped task text, lost comparator endpoints, or unreadable mathematical symbols.
- Comparator bars have endpoint dots at exactly the two participating lanes. A bar crossing a third lane has no extra dot there. This is essential and is handled correctly.
- Diagram arrows consistently run left to right; lane numbering consistently runs top to bottom.
- The K–1 tasks are each one or two sentences, with specific pictured card sets. The initial shared rules are substantially longer, but the planned adult demonstration can carry them.
- There are no prohibited activity headings, mascots, encouragement, exclamation marks, worked solutions, automatic reflection prompts, or lettered microsteps.
- The printed lane boxes are approximately 0.92 cm square and are not usable holders for the stipulated cards of at least 3 cm square. This is acceptable only because the session materials explicitly include a separate full-size reusable mat; the pages are recording diagrams. Do not mistake these PDFs for replacements for that mat.
- The packets provide generous blank working space, although a complete middle-band audit will sensibly use the supplied blank paper or reusable mat as well.

## Recommended disposition

Revise grades 2–3 Problem 6. Reconsider the K–1 construction order and how the older group reaches the four-lane impossibility argument. The remaining mathematics, diagram fidelity, print layout, and restrained student-page register are ready to preserve.
