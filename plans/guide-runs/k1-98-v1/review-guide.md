# Review: Week 98 K–1 adult guide, draft v1 (W98-K-FAC-v1)

I reviewed `draft/k1-guide.pdf` (4 pages) and its source against the final K–1 pages, `plans/k1-drafts/week-98/k-1.pdf` (9 pages). I rendered and read every page of both, plus a 200 dpi crop of the page-1 rule pictures. I also read AGENTS.md, the outline, both page reviews, the draft's README entry and the week's guide (W98-FAC-v4, 5 pages), and I checked the older packets' problem pages. I did not edit the guide or the pages, and I did not run `build.sh`.

**How I checked.** I wrote my checks before opening the writer's checker.

- `review-guide-check/parse_pages.py` reads the boards straight from the student PDF's vector drawings, not from any source file. For every page it gives each board's size, its square size in mm and the squares with a printed seed. Output: `review-guide-check/pages.json`.
- `review-guide-check/check_answers.py` re-derives every answer the guide prints, using the at-least-two rule. It covers the launch, P1's six placements, P2's finishes over every growth order, and exhaustive minima for P3–P7. For P3–P5 it rules out every start with one seed fewer (36, 560 and 12,650 starts) and finds every fewest-seed start on the strips. It also tests every single removal on P8 and the full removal tree on P9. Output: `check_answers.out`, all pass.
- `review-guide-check/check_extras.py` backs the findings below: the "exactly two" misreading, a return-visit demonstration, the strip count, and the 14 three-seed fills of 3 × 3. Output: `check_extras.out`.
- Afterwards I ran a copy of the writer's `check_guide.py` from `/tmp`. It agrees with mine.

**Verdict.** This is a correct guide, keyed to the final pages. I found no must-fix items.

- Every printed answer is right, and every "find all" list is complete: P1's six starts, P6's fewest-seed starts, and P9's two endings.
- Problem numbers, page numbers, board positions, square sizes (30 mm working, 15–16 mm records) and counter counts (6 + 20 per pair) match the PDF. The guide follows the revisions: printed starts are Problem 2, the rule says "two or more", the ✓ square has three neighbors, P1 has six record boards and P9 has two.
- It does not contradict W98-FAC-v4.
- The should-fix items are gaps: facts missing from the overview, one step missing from the P6 argument, a kit item with no activity, a procedure with no demonstration, extra bookkeeping, and an incomplete merge instruction.

## Must-fix

None found.

## Should-fix

### 1. The overview leaves out the strip and two-wide facts, and gives no example of "needed but not fewest" (p. 1)

- **The gap.** "The facts" states three things: one finish, n seeds for n × n, and "every seed needed need not be fewest". Problems 6 and 7 rest on facts the overview never states. Problem 9's question ("a different number?") rests on a fact it states only abstractly.
  - The strip end argument appears only as a quoted child explanation.
  - The point that the square pattern stops working (4 × 2 needs no more seeds than 3 × 2) appears only on p. 3.
- **Why it matters.** AGENTS asks that an adult understand the destination without reading every solution. Two of the nine problems would surprise an adult who has read only the overview.
- **Fix.** Add to "The facts":
  - "On a one-row strip of L squares, each end has one neighbor, so it must be a seed, and two empty squares side by side never fill. So the fewest is ⌊L/2⌋ + 1: 2, 3, 3 and 4 on the printed strips."
  - "For an a × b board the fence count gives at least ⌈(a + b)/2⌉ seeds. The printed two-wide boards attain it (3, 3, 4), so a longer board need not need another seed."
  - After the third fact: "for example, the four middle-edge seeds on 3 × 3 are all needed, yet three slanting seeds fill. Taking seeds off one at a time from one start can stop at 3 or at 4 (Problem 9)."

### 2. The Problem 6 completeness argument never shows why fewer seeds fail (p. 3)

- **What it has.** "Why these are complete" proves that a strip fills exactly when both ends are seeds and no two empty squares are side by side. Then it says "With the stated minimum number of seeds…". It never derives that minimum, for example why 1 × 6 cannot be done with 3.
- **Why it matters.** The guide itself insists that failed attempts do not prove a minimum.
- **Fix.** Insert before "With the stated minimum": "Seeds and single gaps alternate, so s seeds cover at most 2s − 1 squares. A strip of L needs s ≥ (L + 1)/2: 2, 3, 3 and 4. A child can show it as seed, gap, seed, gap, seed." I checked the count in `check_extras.py`.

### 3. The kit lists fence sticks for a demonstration the guide never describes (p. 1, "The table"; p. 1, "K–1 destination")

- **What it says.** The guide asks for 20 card strips per pair "for an optional fence demonstration with at most five seeds". Nothing says when or how to run the demonstration.
- **Why it matters.** A parent volunteer would cut 40 strips, which the "five extra minutes" does not cover, and then have no route for using them.
- **Fix.** Either drop the sentence, or add three sentences after Problems 3–5:
  - When: "For a child who has hunted hard for two seeds on 3 × 3."
  - How: "Lay a stick on every side of a seed that faces an empty square or the board's edge. When a square is added, move sticks so they still mark those sides. The count never goes up. The full 3 × 3 needs 12, and two seeds bring at most 8."
  - Add the cutting time to the preparation estimate.

### 4. The removal procedure has no table demonstration before Problems 8–9 (p. 2 launch; p. 4)

- **The problem.** "Take one off, grow, put it back" (P8) and "keep it off if it still fills" (P9) are new procedures. The page reviews found the cumulative misreading to be the likeliest error. The guide gives the adult only prose. AGENTS ("Launch together") asks for a short demonstration of an unfamiliar procedure on a non-task instance.
- **Fix.** Add a one-minute return-visit launch at the table:
  - Rebuild the launch 2 × 3 start and add a fourth seed at the top right. Grow it: it fills.
  - Clear the growth color, lift that top-right seed and grow again. It stops at four, the launch finish.
  - Put the seed back.
- **Checked:** `check_extras.py`. Demonstrate only that one test. Lifting the top-left seed instead leaves a three-seed fill of 2 × 3, which answers Problem 7's 3 × 2 board.

### 5. Problem 9's running seed sketch adds bookkeeping and competes with the page's two record boards (p. 4)

- **What it says.** "Use a small seed sketch to remember successful removals" and "pool their seed sketches".
- **Why it is not needed.** The current start is already visible: after each test the seed-color counters still on the board are the current start, and the bare dots show seeds already taken off.
- **The cost.** The page prints exactly two record boards, one for each ending. A running sketch on one of them leaves no room for the second ending, and it goes against AGENTS "Keep bookkeeping light".
- **Fix.** Replace the sentence with: "The seed-color counters left on the board are the current start; bare dots show seeds already taken off. Draw only each ending." Change "pool their seed sketches" to "pool their endings".

### 6. "Where it goes" leaves a sentence in the base guide that would become false (p. 4)

- **The gap.** The section replaces the p. 2 "K–1 route, adult-led" and says to retain "the older-band overview". But that overview (base guide p. 1, "What children discover") ends: "No K–1 packet is claimed; the preparation section gives an adult-led K–1 route on the Grades 2–3 pages."
- **Two more omissions on base guide p. 2.**
  - "Per pair" gives 16 counters and does not mention the K–1 table's 26.
  - "Staffing" lists only the middle and upper tables.
- **Fix.** Add: "Also replace p. 1's 'No K–1 packet is claimed…' with a pointer to this section, and add the K–1 table (one adult, two pairs, 6 + 20 counters per pair) to p. 2's Per pair and Staffing paragraphs."

## Minor

1. **Problem 2, middle-row wording (p. 2).** "Empty squares touch several counters diagonally" is not right for the corner squares, which touch one counter at a corner (`check_extras.out`). Write "each empty square touches one counter along a side and one or two at corners, so counting corners would let every square grow."
2. **Say where "exactly two" shows (p. 2 launch; pp. 3–4).** "Say two or more, not exactly two" does not tell the adult what the misreading looks like.
   - Under that reading, P8's four-corner board stops at 7 or 8 squares, the three-corners-and-center board at 7, and the middle-edge board at 8 (`check_extras.out`). So the P8 instruction "First grow its full printed start" is where it shows.
   - The guide's own P7 examples need a square with three filled neighbors ((2, 1) on 3 × 2 and (4, 2) on 5 × 2), and under the misreading they stall at 5 of 6 and 9 of 10.
   - Add one sentence: "A child who refuses a square with three or four filled neighbors is using 'exactly two'; Problem 8's printed starts will then not fill."
3. **Six seed counters also cap the search (p. 1, "Per pair").** On P4–P5 a child's guess or first try may use more than six seeds, which they cannot place. Say what to do. For example: draw that start on a record board, or ask "Can you do it with six?"
4. **Where the guess goes (p. 3).** "Preserve a child's guess on Problems 4 and 5" has no place on the page. Add "write it beside the problem number before the hunt".
5. **Other correct answers to Problem 3 (p. 3).** The key shows only diagonals, but children often find three corners first. Add one line, checked in `check_extras.out`. The 14 three-seed fills of 3 × 3 are:
   - the two slanting lines;
   - any three corners (4);
   - two corners of one side with the middle of the opposite side (4);
   - one corner with the middles of the two far sides (4).

   Every straight line of three is stuck.
6. **Problem 8 workload (p. 4).** The page needs four full grows and 15 single-removal tests.
   - Suggest splitting the boards between the two pairs (one pair takes the L and the four corners, the other the three-corners-and-center and middle-edge boards) and comparing the rings (1, 4, 2, 0).
   - Suggest testing seeds in reading order so none is missed.
7. **Process residue and unclear sentences.**
   - p. 2: delete "Use the page's positions, not invented board letters."
   - p. 2: simplify "a turned or flipped pair is not discarded as a duplicate unless it occupies the same two squares" to "a turned copy in different squares is a different way".
   - p. 4: "A later comparison of two growth orders is natural here; it changes the experiment, not the seed set or the rule" is unclear. Use "Late question: if two children grow the same seeds in different orders, do they finish the same?"
   - p. 1: "Print all nine pages of the draft k-1.pdf". This section is meant for the approved guide, so name the eventual `week-98-k-1.pdf` (W98-K-v1).
8. **Repetition (pp. 1, 3).**
   - "Failed attempts do not prove…" is in the overview and comes back twice in the Problems 3–5 paragraph. Cut "The overview's fence argument proves no smaller start can fill; a few unsuccessful trials do not."
   - "One board at a time" appears on p. 1 and p. 4.
   - "Celebrate the construction" is generic. "Let the child choose whether to seek fewer" is enough.
9. **Launch board (p. 1, "The table").** Say whether the K–1 table carries over the whole-group 2 × 3 board or draws its own copy.
10. **First-hour close (p. 2).** The destination calls "predicting the next square's seed count" a conjecture, but the first route ends at 3 × 3. A closing question, "How many seeds for the next size?", saved for the return visit, would make that conjecture happen.

## Checklist results

1. **Correctness.** All printed answers are verified:
   - P1: 6 starts, 2 diagonals fill.
   - P2: finishes 4, 3, 6 and 9, one finish over all orders.
   - P3–P5: 3, 4, 5, with no smaller start filling.
   - P6: 2, 3, 3, 4, with the complete lists.
   - P7: 3, 3, 4 (10, 8 and 48 fewest-seed starts), and the guide's examples fill.
   - P8: rings {(1,1)}, all four corners, {(1,1), (2,2)}, none.
   - P9: first removals (1,1), (1,2), (2,1); exactly two endings, with 4 and 3 seeds.
   - Launch: one addition, stuck at 4. Rule pictures: ✓ has 3 side-neighbors, ✗ has 1.
2. **Agreement with the pages and the week.**
   - Matches the final PDF and the shared launch.
   - No contradiction with W98-FAC-v4. Should-fix 6 is about merging the section, not a contradiction.
3. **Overview.** Theorem-first, with assumptions (side-neighbors, at least two, no outside squares, counters stay) and short proofs. It names experiment, conjecture and explanation, and says what K–1 children discover before any solution. It is incomplete for P6, P7 and P9 (should-fix 1).
4. **Launch.** Brief (2 minutes), concrete, on the shared non-task 2 × 3 instance, with a three-panel worked visual of the seed-only record, and free of every answer. It has no counterpart for the removal procedure (should-fix 4).
5. **Usability and age fit.**
   - Kit, counts, square sizes and one-board-at-a-time handling are right.
   - The one-hour route adds up to 60 minutes, and its later routes are sensible.
   - Every hint is a question.
   - Staffing honestly says what the adult does and does not do.
   - Gaps: the sticks (should-fix 3), P9 bookkeeping (should-fix 5), the seed cap (minor 3), and P8's workload (minor 6).
6. **Brevity.** 2,546 words over 4 pages, against 3,026 words for the 5-page week guide. Some repetition and residue (minor 7–8). No narration of the pages.

## The writer's flagged issues

I agree with all six of the writer's student-page risks:

- the outside squares are left unstated;
- six seed counters cannot load a whole page;
- growth counters must be cleared before each removal test;
- P1 counts positions;
- P4–P5 overlap with the older packets (an organizer decision, not a guide fault);
- failed searches prove nothing.

On item 2, the six-counter limit also caps the trials a child can make (minor 3).

I also confirmed the writer's out-of-scope note on the base guide. In the grades 4–5 packet, Problems 2–6 are on pages 3–7, but the base guide cites pages 2–3, 4, 5 and 6.

I disagree only by omission. The writer's report lists the sticks as kit without noticing that the guide gives no activity for them (should-fix 3).

## What works and should be kept

- **The overview's three proofs**, short enough for a parent: first missed square for one finish, slanting line plus fence count for n × n, and "removals compare only subsets of one start". Also the experiment / conjecture / proof sentence and "Failed attempts do not prove that fewer seeds are impossible."
- **The Status line** naming exactly what is untested: printing, counter fit, the two-finger check, resets, preparation and pacing.
- **Staffing:** "Children place seeds, choose legal additions and decide when growth has stopped", and "an adult doing those jobs for them is a reason to return to a smaller board".
- **The table launch figure** (start, one addition and stuck, seed record after reset). Also the note that the page-1 ✓ shows one addition with three neighbors, not a filled board.
- **"Running out of counters is not being stuck"** and "work one board at a time".
- **P1's completeness count** (3 + 2 + 1), and the hint "With this seed fixed, have we tried every place for the other?"
- **P2's middle-row rule check**, and the advice to compare seeds and look for an unfinished addition when two finishes differ.
- **The explicit P8 versus P9 contrast** ("put it back" against "stays deleted"), including "a printed dot under a removed counter is a location mark", "The rings do not say all four can go together", and "the four-seed ending is the important contrast".
- **The tables** for P3–P5, P6 and P9, and the P7 fence bound with "no claim about all rectangles is needed".
- **"Where it goes"**, which names the exact section, page and version.
