# Independent adversarial review: Week 25

## Verdict

The draft is mathematically sound and visually usable. I found no wrong counts, impossible task presented as achievable, false theorem, incorrect switch distance, clipped material, or undersized working grid. All three PDFs have six US Letter pages. The mathematical progression is substantially faithful to the brief, including a genuine general connectivity-and-shortest-distance problem in grades 4–5.

There is no blocking mathematical or rendering correction. I recommend a small recording-instruction edit before printing. The other observations below are classroom-usability risks rather than demonstrated failures. A wholesale rewrite is not warranted.

## Findings, in priority order

### 1. Explicitly request a lasting record in the enumeration problems

**Locations:** K–1 Problem 2, page 2; K–1 Problem 3, pages 3–4; grades 2–3 Problem 2, pages 2–3; grades 4–5 Problem 1, pages 1–2.

The tasks say to “make” or “find” every picture, but never ask the child to draw or mark the pictures after using the counters. The available blank grids strongly suggest that intention, but the supplied twelve-counter limit makes it important. The K–1 page 2 lists require eighteen counters if all six pictures are left in place. All six K–1 permutation pictures require eighteen; the five middle-band pictures require twenty; the six oldest-band pictures require twenty-four. Those sets cannot all be preserved as counter arrangements with the specified materials.

This is not a mathematical error or a reason to add more counters: pencil recording solves it. Make the output explicit in the task itself, for example “Find and draw every different picture with these counts.” That is a concrete requested result, not a hint, worked method, or forbidden sentence explaining what the blank spaces are for. The adult can still supply all instruction about handling the counters.

### 2. The oldest band's shortest-route task offers no blank intermediate board

**Location:** grades 4–5 Problem 3, page 4.

The task asks the child to “Record a shortest route.” The shortest route has three switches and therefore two intermediate pictures. The only two printed grids are the filled start and target. A child can record a route as pairs of column labels in the substantial blank area below, so the problem remains usable and does not need a mandated notation. However, a child who wants to record successive pictures must draw the grids or move to loose paper; the pictured endpoints cannot serve as blank records because their dots are permanent.

Consider supplying two blank intermediate grids on an additional page, preserving the 22 mm working-cell size. Do not show arrows, a prescribed number of numbered moves, or a sample route. Alternatively, accept that this is an open recording choice and make sure the stated blank paper is actually present. This is a lower-priority usability issue, not a false or inaccessible task.

### 3. K–1 has a weaker reserve of work than its six-page length suggests

**Locations:** K–1 Problem 2, page 2, and Problem 5, page 6.

Problem 2's two cases are top/bottom reversals of the same three-choice problem, one of which has already appeared in Problem 1. The six permutations in Problem 3 are real mathematics, and the later unique/ambiguous comparisons are worthwhile, but the final construction task asks for only one four-counter example on each of two shapes. A quick child can choose those examples, let a partner answer, and be done without a further mathematical goal. Six pages should not by itself be taken as evidence that there is more than forty minutes of work for the quickest child.

Because the slot is unpiloted, this is a pacing risk rather than a confidently established shortfall. If adding one reserve problem, ask for a concrete contrast among student-made pictures, such as a four-counter picture whose counts force it and another whose counts allow alternatives, with the needed grids. Do not add generic “try more” language or an adult-style menu of hints. The current K–1 packet should retain its enumeration and impossibility work.

## Independent mathematical checks

I did not rely solely on `draft/src/answer-checks.json`. I independently enumerated binary grids for the fixed margin cases and constructed switch graphs to check the two-row distances. The check output is in `review-render/independent-checks.json`.

- K–1 Problem 1: the three pairs allow respectively 2, 2, and 3 pictures. Each request for two different pictures is achievable.
- K–1 Problem 2: each set allows exactly 3 pictures, so the three slots per set suffice.
- K–1 Problem 3: exactly 6 pictures, with six total recording grids across pages 3–4.
- K–1 Problem 4: the 2-by-3 case with row counts (3,1) and column counts (2,1,1) is unique; the 3-by-3 (2,1,0)/(2,1,0) case is unique; the (2,1,1)/(2,1,1) case has 5 pictures. The deliberate impossibility questions are valid.
- The final K–1 construction problem can produce both unique and ambiguous examples with four counters on either printed board shape.
- Grades 2–3 Problem 1: the three margin sets have 3, 1, and 2 pictures. The “if you can” qualification is necessary and present.
- Grades 2–3 Problem 2: exactly 5 pictures. Six available grids are adequate; an unused grid is not an error.
- Grades 2–3 Problem 3, page 3: the only alternative moves the counters at A1 and C3 to A3 and C1. This correctly requires a rectangle whose rows and columns are nonadjacent.
- Grades 2–3 Problem 3, page 4: the four printed pictures have respectively 0, 1, 3, and 0 available switches, in reading order. Every printed row and column count agrees with its picture.
- Grades 2–3 Problem 4: the four one-count columns with two top counters have one start, four pictures at distance 1, and one at distance 2. Both requested constructions exist. The two-switch lower bound is genuine.
- Grades 2–3 Problem 5: a unique four-counter construction is possible on both board shapes, so the closing question has an affirmative answer worth explaining.
- Grades 4–5 Problem 1: exactly 6 pictures. All are connected by switches, and their switch graph has diameter 2, answering Problem 2.
- Grades 4–5 Problem 3: the printed endpoints have distance 3. For example, switches in column pairs (1,4), (2,5), and (3,6) transform the start into the target. Each switch can remove only one of the three unwanted top-row positions, establishing the lower bound.
- Grades 4–5 Problem 4: the endpoints have distance 2; the margins allow exactly 6 pictures; the maximum shortest distance is 2. Column 1 is necessarily full and column 3 necessarily empty, so this adds an important concrete case before the universal question.
- Grades 4–5 Problem 5 correctly restricts its theorem to two rows. It does not incorrectly extrapolate the elementary argument to arbitrary-height boards. The exact rule is the number of columns occupied in the top row of the start but not the target; pairing unwanted and missing top positions gives an attaining route. No further mathematical assumptions are missing.

## Visual and page-by-page inspection

I rendered the supplied PDFs afresh at 90 dpi and inspected all 18 page images, rather than relying on the author's renders. The fresh images are in `review-render/`.

- **K–1 pages 1–2:** all six grids on each page fit, with the totals and permanent labels distinct. No crowding causes an actual overlap.
- **K–1 page 3:** four full-sized permutation grids, with adequate separation.
- **K–1 page 4:** the continuation of Problem 3 and start of Problem 4 are clearly separated.
- **K–1 page 5:** both contrasting pairs are fully visible; the bottom counts clear the footer.
- **K–1 page 6:** both construction pairs and all empty count circles are visible and usable.
- **Grades 2–3 page 1:** all three contrasting pairs fit.
- **Grades 2–3 pages 2–3:** six total enumeration slots are available; the new concrete move problem is clearly separated on page 3.
- **Grades 2–3 page 4:** all four printed pictures match their totals; the lower diagrams and total circles clear the footer.
- **Grades 2–3 page 5:** start, middle, and bottom grids are distinct and large enough for counters. The prompt is readable.
- **Grades 2–3 page 6:** both construction pairs and count circles fit; no cropping or footer intrusion.
- **Grades 4–5 pages 1–2:** six full-sized solution slots across the two pages; labels, totals, and page numbers are correct.
- **Grades 4–5 page 3:** the switch rule and distance question fit without collision, with three usable working grids.
- **Grades 4–5 pages 4–5:** the 2-by-6 start/target pictures are large, clear, and accurately counted. Blank space remains for written work.
- **Grades 4–5 page 6:** the generalization is legible; two blank 2-by-6 boards are available for examples; footer clearance is satisfactory.

The sources set each cell to 22 mm with a 1 mm TikZ coordinate scale. The PDFs are 612 by 792 points and are intended to be printed at 100%, so the working size satisfies the brief. Preprinted dots are approximately 9.2 mm across and leave room for the supplied counters. Headers, packet identifiers, footers, and page numbering are consistent throughout.

## Adherence to the organizer's standard

- Only the required header and numbered problem labels function as headings.
- No mascots, decorative framing, praise, exclamation marks, activity narration, or worked answers appear.
- K–1 problem statements are one or two sentences and use concrete objects.
- The switch rule explicitly allows any two rows and columns and preserves intervening cells. Permanent row and column labels are retained even when counts are zero.
- The packets use whole-line counts, not run clues or visual silhouettes.
- The middle band encounters a concrete two-counter move before receiving the switch definition.
- Explanation requests generally have a mathematical purpose: completeness, impossibility, minimality, or a general rule. They are not attached mechanically to every task.
- No complete switch graph, nested ordering, proof scaffold, or sequence of small lettered substeps gives away the method.
- Repeated problem numbers continue the same task across page breaks; they are not conflicting references. No renumbering is required.
- The older packet chooses the permitted two-row theorem route rather than trying to cover both major kernels superficially.

**Bottom line:** retain the mathematical cases and visual system. Clarify how enumeration results are to be recorded, consider the route-recording space, and treat K–1 pacing as something to strengthen or test rather than assuming that six pages guarantees an hour's reserve.
