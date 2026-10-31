# Review: Week 57 K–1 adult guide section, draft v1 (N57-K-FAC-v1)

I reviewed `draft/k1-guide.pdf` (4 pages) and its TeX source against the final student pages `plans/k1-drafts/week-57/k-1.pdf` (7 pages, Problems 1–7). I rendered and read every page of both. I also read the outline, both page reviews, the drafts README entry, the week's guide W57-FAC-v4 (all 10 pages), its materials file N57-M-v1 and the Week 98 model guide. I did not edit the guide or the pages.

**How I checked.** I wrote my own checks before opening the writer's checker. They are in `review-guide-check/`:

- `pieces.py` models squares and halves as quarter-triangles of unit cells. It reads inside and outline dots from the corner angles on each dot, so Pick's rule is never assumed. It finds gaps by flood fill and allows only joins along whole sides.
- `check_answers.py` and `check_regions.py` enumerate every side-joined shape of 1–8 halves, and every shape of 1–6 mixed pieces (37,438 fixed shapes at six pieces). Their output is in the matching `.out` files. The half shapes reproduce the polyabolo counts 1, 3, 4, 14, 30, 107, 318 and 1116. The rule "outline + 2 × inside = halves + 2" holds for every gap-free shape I generated.
- `check_pages.py` reads the student PDF's vector paths. It gives the six Problem 1 shapes, the board sizes and the 20 mm spacing, and works out what one kit can hold.

I then ran the writer's `check_guide.py` from a copy in `/tmp`; it passes, and it agrees with my results.

**Verdict.** The guide is correct and keyed to the final pages. It needs revision, but nothing in it is wrong enough to block approval.

- Every answer it prints is right. That includes the complete P5 catalog of six (16 placements reduce to 6, and flips add none), the P6 bound of six pieces with all 16 six-piece placements, and the two P7 shapes.
- Problem numbers, page numbers, board sizes (3 × 4, 5 × 5, 3 × 3, 6 × 5 and 4 × 5 dots), stars and kit counts match the seven-page packet, not the six-page draft the reviews describe.
- Nothing contradicts W57-FAC-v4.

The should-fix items are about the K–1 table in practice:

- what the table demonstration shows;
- one missing step in the overview's explanation;
- wrong picture notes in P1;
- the missing P2 catalog;
- what one kit can hold;
- the first-hour route;
- an extra rule added to P7.

## Must-fix

None found.

## Should-fix

### 1. The table demonstration never shows halves (p. 2, "After the whole-group launch"; p. 1, "Print and prepare")

- **The problem.** The demonstration row uses three whole squares. So before Problem 1, children never see:
  - a half on the dots;
  - a legal half join next to a tip-to-tip one;
  - why three squares are recorded as 6.
- **Why it matters.** These are the new parts at this table and the likeliest causes of wrong counts.
  - Halves joined only at a tip turn P2's five outline dots into six (`review.md`, point 4).
  - A square written as 1 hides the P5 pattern.
  - The shared launch has just said "One little square has area 1" (main guide p. 3), but the K–1 record writes a square as 2.
- **Two smaller points.**
  - "Touch a middle-of-side dot" does not fit the example: each long side of a 1 × 3 row has two dots between its corners, and neither is in the middle.
  - The spare grid is the older p. 4. It carries a Grades 3–5 question and an "I = B = area =" line.
- **Fix.**
  - Build the same 1 × 3 row from two squares and two halves, with the halves making the third square. Count it aloud: "two, four, six halves." The row is still not a task instance, and the record stays 6 and 8.
  - Set one extra half tip to tip against the row and ask "Is this joined?" Then remove it.
  - Add: "At this table say 'halves', not 'area': a square is written 2."
  - Change "middle-of-side dot" to "a dot on a side between two corners".
  - In "Print and prepare", say to cover the older p. 4's question and record line, as the old K–1 route did.

### 2. The overview gives only half of the explanation for the main rule (p. 1, "What children discover")

- **The problem.**
  - The guide says: "a new half sharing one side adds one outline dot; a closing corner changes the count." The first half is the explanation of the bold rule when no dot is inside. "Changes the count" does not say by how much or why. That step is the reason each inside dot takes the place of two outline dots, which is P3's and P7's mathematics.
  - "Let children notice the contrast before offering the rule" also sits awkwardly beside "The full dot rule is adult knowledge".
- **Fix.** Replace the last two sentences of that paragraph with the outline's piece-by-piece bookkeeping (kernel 1), for example:

  > Build a shape one piece at a time. A half laid along one side adds one new outline dot, and a square adds two. A piece fitted into a notch, along two sides, covers the corner between them, and that dot goes inside. A half there takes one dot off the outline. A square there adds one new corner, so the outline stays the same. Either way, outline + 2 × inside grows by one for each half, starting from 3 for one half. Let children notice the contrast; the rule itself stays with the adult.

  I checked the arithmetic. A half in a notch changes the outline by −1 and the inside count by +1, a net +1. A square in a notch changes them by 0 and +1, a net +2. A square in a slot between three sides changes them by −2 and +2, a net +2.

### 3. Problem 1's notes misdescribe the pictures (p. 2, "Problem 1")

- **The problem.** The answers (1, 3), (2, 4), (2, 4), (2, 4), (4, 6), (4, 6) are right, but two notes about the pictures are not (from `check_pages.out`):
  - "In the wide triangle and bottom trapezoid, a dot halfway along a straight side counts too." The rectangle also has a dot between corners on each long side, and the note leaves it out. The trapezoid has two dots on its long bottom side, at the thirds, not one halfway.
  - "The paper amount stays the same in each contrasting pair." The top row pairs one half (1) with the square (2).
- **Fix.**

  > The wide triangle has one dot between corners, the rectangle one on each long side, and the trapezoid two on its long side. The square, wide triangle and slanted shape each take two halves and have 4 outline dots; the rectangle and trapezoid each take four and have 6.

### 4. Problem 2 does not say how many shapes there are (p. 2, "Problem 2")

- **The problem.**
  - The page has six boards. The guide says that filling them all is not required, but never gives the count: three halves make 4 shapes up to turns and flips, or 6 if a flipped shape counts as new. All have five outline dots and none inside, and all fit the 3 × 4-dot boards (`check_regions.out`).
  - The overview names "a complete small catalog" as one way to explain a claim. Without this catalog the adult cannot tell a child whether "always five" has been checked on every shape, or answer "Are there more?"
- **Fix.** Add one sentence and a strip of four small pictures, like P5's:
  - a square with a half on one side;
  - three halves around one dot (the tilted square with one half missing);
  - a slanted strip of three halves;
  - the wide triangle with a half on one of its short sides.

### 5. One kit cannot keep a shape on every board (p. 1, "Per pair"; p. 2, adult role; pp. 2–3)

- **The problem.** "One on each board" invites children to leave each shape built. One kit holds 10 squares and 20 halves (`check_pages.out`):
  - P3's six four-half shapes need 24 halves, so only five can stay built.
  - The six P5 shapes need 12 squares and 12 halves together, and the kit has only 10 squares.
  
  The guide's "If every attempt needs adult tracing, preserve one shape per pair" points the same way: keep shapes built.
- **Fix.** Add to "Per pair" or the adult-role paragraph:

  > Trace each shape and lift its pieces before building the next: one kit holds only five four-half shapes and not all six P5 shapes at once. To keep shapes built for comparing, take pieces from the spare bag.

  In P5, "pool their kept pictures" then makes clear that the pooled items are traced pictures.

### 6. The first hour may end without the contrast (p. 2, "A first hour")

- **The problem.** After the reset the guide offers "choose P3 or continue P2". P2 has only four shapes, and all of them give five outline dots. Twenty-five minutes on it risks a thin finish. The hour would also end before the discovery the overview names: "then closing in a dot changes it."
- **Fix.**

  > 38–50: P3; the tilted square is the hour's turning point. Stay with P2 only while joins or counts are still unreliable.

### 7. Problem 7 adds a rule the page does not state (p. 4, "Problem 7")

- **The problem.** "P7 uses eight half pieces, not intact squares" goes beyond the page. Page 1's shared rule says "A square counts as two halves", so the roofed hexagon built from two squares and four halves (P6's own answer, which the guide says to save) is a shape "from eight halves" in the page's counting. Squares and halves give exactly the same two shapes and counts (`check_answers.out`: the four piece-arrangements with fewer than 8 outline dots are 2 shapes), so nothing is gained by turning such a child away.
- **Fix.**
  - Replace the italic sentence with: "A square may stand for two halves; the shapes and counts are the same."
  - Reword the hint to "How many halves of paper are in your saved six-piece shape?"

## Minor

1. **"Where it goes" (p. 4).** Also list the W57-FAC-v4 p. 3 first-hour row "10–25 … Younger: the K–1 four-square route below, with the parent". Both print options on p. 2 mention the younger pairs' p. 4 copies; "p. 2 younger print quantities" covers them, but name both options.
2. **Printing (p. 1).**
   - Name the file as it will be after integration (`week-57-k-1.pdf`, per the drafts README), with the draft name in brackets.
   - Add a spare set, or spare pp. 2, 3 and 5, for retries. The week's guide prints a spare set.
   - Say whether the 10–15 minutes come on top of the week's 15–25 minutes to print and rehearse, or inside them.
3. **Checker narration and repeated reassurances (pp. 2–4).** These help no parent at the table:
   - Cut "The checker exhausts the possibilities independently" (P2).
   - Cut "An independent exhaustive check gives … This is an adult completeness check" (P3), keeping the number 14.
   - Cut the P7 sentence beginning "The independent search checks every side-connected region".
   - Cut "this section's counts are independently rechecked against N57-K-v1" (p. 4).
   - Four lines say the boards are not targets ("no requirement to find six", "not a demand to draw all 14", "not nine required answers", "not an extra first-visit demand"). Say it once, in "A first hour".
   - Change "13 of the latter kind and this one" to "13 have six outline dots; the tilted square is the 14th".
   - Change "up to 12 halves if recording the six-square solution": P6 has no record line.
4. **An extension for the quickest pair (p. 4, P7).** The outline keeps the whole trade for the quickest pair, with the adult, but the guide never gives it a place. Add: "Ready pairs: make an eight-half shape with no dot inside (10 outline dots) and set the three records 10, 8 and 6 side by side: each dot inside takes two off the outline."
5. **Sources (p. 4).** Add one clause, from the outline: the halves form of the rule, the closing-in problems and all their instances are newly worked for these pages. The main guide's p. 10 sources do not cover them.

## Checklist results

1. **Correctness.** All printed answers re-derived by my own enumeration.
   - P1: (1, 3), (2, 4), (2, 4), (2, 4), (4, 6), (4, 6), no inside dots.
   - P2: 4 shapes (6 with mirror images), all five outline dots.
   - P3: 14 shapes; 13 have six, and the tilted square has four with one inside. All fit 3 × 4 dots.
   - P4: no shape of one to three pieces has an inside dot.
   - P5: 6 shapes with turns the same, 6 with flips too, 16 fixed placements. The table's half pieces, paper in halves and outline counts are all right (4, 5, 6, 6, 7, 8). The six pictures are drawn correctly.
   - P6: no shape of five or fewer pieces has two inside dots. There are 7 six-piece shapes and 16 horizontal placements, each with squares in the two shared cells. They use 8–12 halves and have 6–10 outline dots.
   - P7: 1,105 gap-free shapes of eight halves give (outline, inside) counts of (10, 0) 1,038 times, (8, 1) 65 times and (6, 2) twice, and both six-dot shapes fit 4 × 5 dots. Shapes with a gap have at least 9 outline dots.
   - Demonstration: 6 halves, 8 outline dots.
   - The two P7 pictures are valid eight-half divisions.
   - The overview's general claims hold. Wrong statements about the pictures: should-fix 3.
2. **Agreement with pages and week.** Problem numbers, page numbers, board sizes, the stars, kit counts and the five-kit card-stock arithmetic all match. The guide follows the final P5/P6 order. The hour slots and staffing agree with W57-FAC-v4. Gaps: picture notes (should-fix 3) and the shared launch's "area 1" (should-fix 1).
3. **Overview.** It comes before any solution. It states the rule in halves with its assumptions and exclusions, gives the three-piece and two-dot bounds with reasons, separates experiment, conjecture and explanation, and refers to the main guide for the older bands. Its explanation of the main rule stops halfway (should-fix 2).
4. **Launch.** It is brief and concrete. The instance is not a task, and the three-panel visual reveals no answer. It does not show halves or the joining rule (should-fix 1).
5. **Usability and age fit.**
   - Staffing is honest: one adult who reads and records, partners who trace, and a fallback when tracing stalls.
   - Hints are questions, and preparation time is plausible.
   - Gaps: kit capacity (should-fix 5), the first-hour default (should-fix 6), P7's added rule (should-fix 7).
6. **Brevity.** It runs 2,358 words in 4 pages, with no generic encouragement. It has some checker narration and repeated reassurances (minor 3).

## The writer's report

- **Agreement.** I agree with every risk the report flags: pieces hide dots, tracing can bottleneck one adult, the p. 1 strip is at 12 mm, stars are targets, cracks prove nothing, pinched gaps and tip-to-tip pairs are illegal, the boards do not demand distinct answers, and P6–P7 are later work. The guide handles each well. I also found no error on the student pages.
- **"Kit and print arithmetic are checked."** Partly. The per-shape counts are right, but the report did not set one kit against the boards (should-fix 5).
- **The boards are not targets.** Agreed, but the adult still needs the P2 catalog (should-fix 4).
- **The demonstration grid.** The report says it uses an existing spare p. 4 grid. That is right, but the grid's printed question needs covering (should-fix 1).

## What works and should be kept

- **The P5 section.** It has a complete catalog with the reason it is complete: a right angle at the star from each of four cells, two choices per cell, then the rotation classes and "flipping adds none". The table and the six correct pictures give a parent everything needed to judge a child's shape.
- **The P6 argument.** Six cells must each hold a piece, the shared cells must be squares, and "this describes every six-piece solution without asking children to enumerate them". Both witnesses come with their paper and outline counts.
- **The P4 and overview corner arguments**, including what a child can do: "place the corners, point to the missing quarter".
- **"Keep the rules visible."** It says stars are targets, the whole shape must connect through sides while opposite pieces may meet at a corner, children trace and lift before deciding, and cracks are not tests. Together with the P7 notes on tip-to-tip tilted squares and corner gaps, these are exactly the operational traps the reviews identified.
- **The adult-role paragraph.** Partners hold and trace in turn; the adult helps only where slipping prevents a recoverable outline; if every attempt needs adult tracing, the pair keeps one shape rather than letting the adult run both investigations.
- **The three-panel demonstration visual**, which mirrors the page 1 strip, with the demonstration done on a real 20 mm grid and a non-task row.
- **Status and "Where it goes".** They name exactly what is physically untested, keep the scissors with the adult, keep K–1 pieces apart from the older tables' cut duplicates, and name the exact paragraph and page the section replaces.
- **Keeping "always five" as a conjecture** until there is a reason, and the P3 advice to compare the tilted square with a six-dot drawing rather than ask for more routine examples.
