# Independent adversarial review

## Verdict

**Revise before finalizing, mainly for K–1 usability and the substantial-problem requirement.** The mathematics is sound, the diagrams are unusually clean, and the three six-page packets have a coherent progression. I found no false mathematical assertion, unsolvable task presented as solvable, clipping, accidental crossing, or wrong arrow in the rendered PDFs. The issues below are narrower than a redesign: clarify the K–1 game, make its exhaustive task practically recordable, and strengthen the repeated elementary rerouting pair.

I read `PROMPT.md`, inspected the source for exact graph definitions, independently rendered and viewed all 18 pages, and independently enumerated paths, edge-disjoint packings, minimum closing sets, and the two closing games. I also checked the residual examples and cut partitions. I did not edit the draft or execute its generation script. Independent check outputs and fresh renders are in `review-render/`.

## Revisions to make

### 1. Specify the K–1 game's players and what a winning answer means

**Location:** K–1, page 6, Problem 6. **Priority: medium; definite clarity defect.**

“Take turns closing one open arrow; whoever leaves no route wins. Find how to win on each board” never says that there are two players. This group has three children. Three children taking turns is a quite natural reading, but it is a different game. The older packet explicitly says “Two players” and should be the model here.

The upper board is a forced win for the **second** player: any first move destroys one of the two branches, and the second player can destroy the other. Thus “Find how to win” also needs the player-order question. A child assigned to move first should not be left looking for a nonexistent winning strategy.

A suitable two-sentence goal is: “Two players take turns closing one open arrow; whoever leaves no route wins. On each board, would you rather go first or second, and how can you win?” This supplies rules and the question without supplying a method or answer. Keep the two contrasting boards; they are well chosen.

### 2. Give K–1 a usable way to retain the exhaustive list

**Location:** K–1, page 5, Problem 5. **Priority: medium; practical student-page issue.**

There are **eight** successful pairs, but the page has only two identical, unlabelled boards. A child can experiment successfully with movable markers, but moving the markers erases the previous answer. Marking several pairs on the same board loses which two arrows belonged together. Nonreaders cannot fall back on a list such as “Start–A, Start–B,” as the older children can on their labelled board.

This matters specifically because the task asks for **every different pair**, rather than a few successful pairs: retaining answers and detecting duplicates are part of completing the task. The generous blank space is helpful for many tasks, but it does not give a young child the missing copies without asking them to redraw a seven-vertex network. Spare paper does not remove that burden.

Provide enough pictorial recording capacity for all eight outcomes, or change the concrete instance so that its full answer set fits the supplied boards. Preserve the real exhaustive mathematics. Do not solve this by printing a prescribed search order or by adding explanatory prose about what the blanks are for. This is not a reason to remove the problem; it is one of the strongest K–1 tasks once its record-keeping is feasible.

### 3. Make the second rerouting case do more mathematical work

**Locations:** Grades 2–3, page 5, Problem 5; Grades 4–5, page 1, Problem 1. **Priority: medium; substantial-problem standard.**

The lower board is precisely the upper four-vertex greedy trap with an independent Start–C–Finish route added. That additional route is already reserved and never interacts with the repair. The same one-arrow cancellation solves both boards. There is essentially one rerouting decision repeated twice, and the largest final collection is unique on both boards.

For grades 2–3, the upper graph was already optimized in Problem 1. For a quick fourth or fifth grader, the entire opening pair can be solved in a couple of minutes. Two pictures do not make this a five-minute substantial problem when the second adds no new obstruction or decision.

Replace or supplement the lower case with a genuinely different interaction: a different stuck reservation on a richer board, competing repairs, or a second cancellation that must be coordinated with the first. Keep it a concrete goal with an exact starting reservation, without giving rerouting steps. The later staircase task already demonstrates that the author can supply a good interacting example; avoid merely duplicating that later task verbatim.

## Smaller points worth addressing

- **K–1, page 4:** The intended experiment closes exactly one arrow at a time, independently of earlier trials. “Find every arrow you could close and still fit two routes” is likely understandable with the adult, but the initial “Close one arrow” can be read as leaving a first closure in place while searching for another. A short one-at-a-time formulation would remove that ambiguity without adding a hint.
- **Replacement drawings:** In grades 2–3 Problem 5 and grades 4–5 Problem 1, the old reservations are permanent printed gray strokes. New colored routes can be traced over them, so this is workable, not a mathematical defect. An unreserved working copy would make the final answer much clearer, especially for the allowed line-pattern rather than color method. Grades 4–5 Problem 5 already provides a useful clean copy.
- **Opening K–1 language:** The individual questions meet the one- or two-sentence limit. The shared rules are nevertheless a fairly dense verbal opening for children who mostly cannot read. The adult demonstration can carry them, as the session plan intends; keep any future edits from expanding this paragraph further. This is a caution, not a demand for picture legends or extra headings.

## Mathematical verification

All numerical checks below refer to the graphs actually drawn, not just the author's answer file.

### K–1

- **Problem 1:** Both boards have maximum two routes. The first has exactly one maximum collection; the second has two, distinguished by how the incoming and outgoing arms are paired at the shared middle dot. “Find another … if you can” is meaningful on both.
- **Problem 2:** The upper board needs two closing arrows and has four minimum pairs. The lower needs one, with two possible one-arrow closures. This is a useful contrast between an endpoint-visible limitation and a shared downstream edge.
- **Problem 3:** Maxima and minimum closure sizes are two on the upper board and three on the lower. Shared vertices are genuinely used on the upper board.
- **Problem 4:** On the upper board, exactly six arrows may be removed while retaining two routes: the three arrows leaving Start and the three that connect those branches to the common middle dot. On the lower board, only the vertical arrow may be removed.
- **Problem 5:** Exactly eight pairs stop all travel. Four block both branches before the middle dot; four block both branches after it. A mixed pair with only one closure on each side does not suffice.
- **Problem 6:** With two players, the upper board is a second-player win. The lower is a first-player win, and its only winning opening is closing the vertical arrow. These are correct contrasting game positions.

### Grades 2–3

- **Problem 1:** Both maxima and minima are two. The shared-dot board and the greedy-trap board are mathematically different and useful.
- **Problem 2:** Maximum two routes, even though Start has three outgoing arrows and Finish has three incoming arrows. There are 18 individual routes and 36 unordered maximum collections. A two-arrow closure can be taken across either side of the narrow middle portion. This is a strong interior-bottleneck problem.
- **Problem 3:** The exhaustive answer contains eight pairs, as above. Lettered vertices make written recording feasible, and there is ample writing space.
- **Problem 4:** Adding D→G on the upper board permits three routes. The lower board cannot admit three under any allowed added interior arrow because only two arrows leave Start. The requested impossible case is intentional and valid.
- **Problem 5:** The printed reservations genuinely block any additional disjoint route. Their sizes are one and two; the true maxima are two and three. The concern is repeated reasoning, not incorrect starting states.
- **Problem 6:** The player-order results and strategies are correct. Its two-player wording is clearer than K–1's.

### Grades 4–5

- **Problem 1:** Same verified rerouting cases as grades 2–3 Problem 5.
- **Problem 2:** Correct matching packing/obstruction task, with the obstruction explanation expressly requested where it matters.
- **Problem 3:** There are three qualifying Start-side sets: {Start, A}, {Start, A, B}, and {Start, A, B, D}. Each has exactly two outgoing cut arrows and at least one incoming arrow. Asking for two is feasible. The printed diagonal is C→B, and the vertical arrows are B→A and C→D; those directions render correctly.
- **Problem 4:** A valid witness is closing {A→C, B→D} and using the route Start→A→C→B→D→Finish. The route consumes both members of a minimum two-arrow obstruction, so it cannot coexist with any second route. The graph's maximum is two. This is an excellent distinction between “each route uses at least one cut arrow” and “each route uses exactly one.”
- **Problem 5:** The printed two-route reservation is locally stuck. The residual walk Start→A→D→B→E→C→F→Finish cancels B→D and C→E, yielding the three legal forward routes through A–D, B–E, and C–F. Both the marked board and the clean board contain all required arrows. A thin horizontal edge looked faint in the 85-dpi render but is present and clear in the 150-dpi verification; this is not a missing-edge defect.
- **Problem 6:** Residual-reachable dots are precisely Start, A, B, C, and D. The outgoing boundary {D→E, D→F} has size two and certifies the printed packing. The two printed paths share interior vertices legally.
- **Problem 7:** The assertion is true for finite directed unit-capacity networks with one common Start and Finish and the stated simple-route convention. The no-augmenting-walk hypothesis gives a matching outgoing cut. This is appropriately placed as the final, adult-supported destination, rather than assumed in the early tasks.

## Print, layout, and brief compliance

- All three PDFs are six pages of US Letter. Every page has the required one-line week/topic/level header, packet-specific footer, and correct page number.
- Problem labels use “Problem N:”. There are no activity headings, mascots, praise, exclamation marks, automatic explain-after-every-task prompts, or lettered procedural substeps.
- K–1 uses large type and unlabelled interior dots; older diagrams use helpful vertex letters. Arrowheads, endpoints, and reservation strokes are distinguishable in the print-scale/high-resolution views.
- The networks avoid accidental geometric crossings. The added-arrow problem explicitly specifies what an undotted crossing means.
- Diagrams are large enough for tracing. The shortest straight edges are about 25 mm before endpoint allowances; I found no obviously unusable closure-marker placement or diagram clipping. At the upper end of the proposed 15–20 mm marker size, the short horizontal edges deserve an actual printed-marker check, but I am not reporting a demonstrated failure.
- White space is generous and generally useful for explanations and experiments. The exception is the specific K–1 exhaustive-recording mismatch described above, not a general need to fill the pages.
- The common unit-capacity, directed, shared-vertex rules are preserved. The packet never substitutes sequential traffic for simultaneous packing and never claims a theorem for multiple prescribed source–target pairs or vertex-disjoint routes.
- There is plausibly enough total material for forty minutes in every band. The stronger criticism is the organizer's requirement that **each numbered problem** be substantial, particularly the duplicated simple rerouting pair. The exhaustive and game problems provide genuine depth and should be retained.

## Recommended disposition

Keep the overall sequence and diagrams. Make the three focused revisions above, re-render the changed pages, and recheck any replacement network independently. No wholesale mathematical rewrite is needed.
