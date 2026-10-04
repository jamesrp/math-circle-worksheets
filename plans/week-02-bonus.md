# Week 2: Fast Finisher / Bonus Challenges

Prepared September 30, 2026; **unpiloted reserve**. These four variations implement the organizer's brief as a separate supplement to the compact and upper catalogs. Each numbered problem occupies one US Letter page. Offer a problem by interest and readiness; finishing a packet is not a prerequisite for access.

- [Student packet: four pages](../lowell-math-circle-year-2/week-02/week-02-bonus-challenges.pdf), **F02-BONUS-v1**.
- [Facilitator notes and solutions: two pages](../lowell-math-circle-year-2/week-02/week-02-bonus-facilitator.pdf), **F02-BONUS-FAC-v1**.
- [Editable PDF builder](../lowell-math-circle-year-2/source/week-02/build-bonus.py), [instance data](week-02-bonus-data.json), [exhaustive verifier](verify-week-02-bonus.py), [checked results](week-02-bonus-checks.json).

## Use and prerequisites

The printed guide supplies setup, launch, timing, hints, solutions and further questions. Everyone first sees the ordinary pair-flip action in the common Week 2 launch. At the bonus table, allow handling and trying before explaining; show the special button separately when it is introduced. Pencils and erasers, paper, or the existing whiteboards suffice; two-sided counters are optional. Print at Actual Size, and give a selected page rather than requiring a four-page sequence.

Children need to follow the pair-flip rule, compare lamp pictures and track several moves. Adults can read and record. Problems 1-3 need only small counts; Problem 4 adds counting presses and adding costs up to 5. The depth is in completeness, predicting a forced choice, constructing arbitrary targets, and distinguishing two optimization goals. There are no algebra, matrix or graph-vocabulary prerequisites, and no fixed grade gate. Suggested time within the existing hour: 10-15 minutes for Problem 1 or 2, 10-20 for Problem 3, and 5-10 for Problem 4. These are design estimates, not observed completion times.

## Exact instances and checked mathematics

**Problem 1: Do-nothing moves.** All lamps start OFF. Every selected line is pressed once, and at least one must be selected. A is a four-lamp path: no nonempty solution. An endpoint forces its only line to be omitted, and the same argument continues along the path. B is a five-lamp ring: selecting its whole outline is the unique nonempty solution. C is a square with just one diagonal, from top left to bottom right: the upper-right triangle, lower-left triangle and outside square are its exactly three nonempty solutions. Each lamp in a selected shape is changed twice. More generally, each lamp must be touched an even number of times, including zero. The adult guide supplies a completeness argument by separating whether the diagonal is selected; the student sheet leaves that organizing choice open.

**Problem 2: Bridge detective.** Two triangles are joined by one long horizontal line. There is a deliberate at-most-once-per-line rule for this problem only. Otherwise, a forced omission would not literally be an omission: any pair of extra bridge presses could be inserted harmlessly.

For data and adult verification, left lamps 1 and 2 are the upper/lower far-left lamps and 3 is the left bridge end. Right lamp 4 is the right bridge end, with 5 above and 6 below at the far right. These numbers are absent from the student page.

| Puzzle | Start ON | Target ON | Lamps that change, left / right | Bridge | Example solution |
|---|---|---|---|---|---|
| A | 1, 4 | 2, 3 | 1, 2, 3 / 4 | Press | Left vertical line; bridge |
| B | 1, 4 | 2, 5 | 1, 2 / 4, 5 | Leave alone | Left vertical line; right triangle's upper slope |

Both starts and both targets have two lamps ON. Counting only total ON lamps cannot distinguish the puzzles. Internal lines change two lamps on one side; only the bridge changes an odd number there. The changed-lamp counts are therefore the relevant quantities: 3 and 1 for A, 2 and 2 for B. Exhaustive enumeration finds four valid line sets per puzzle, all agreeing on the bridge. The student is asked to predict before solving; no parity rule is printed.

**Problem 3: One solo switch.** A six-lamp ring has a star beside its top lamp. Every working board begins empty. The special button toggles only that lamp, while a line still toggles both endpoints. The at-most-once condition from Problem 2 does not carry over. A needs the button alone; B needs it plus a line to a neighbor; C can use it plus three consecutive lines to the opposite lamp. Other reasonably distant choices are allowed by the wording. D asks the child to choose a target, then the final question asks whether every target can be made.

To toggle any ordinary lamp alone, press the button and a route from the special lamp to that lamp. The special lamp and each intermediate lamp are changed twice; only the chosen endpoint changes once. The special lamp itself needs only the button. Compose these constructions for the desired ON lamps. Repeated presses cancel in pairs, even with overlapping routes. This works on any connected drawing. The exhaustive check verifies all 64 six-lamp states; without the button exactly the 32 even states are reachable. The proof, not the enumeration, supports the general claim.

**Problem 4: Cheapest, not fewest.** A square starts all OFF, with the two top lamps ON in the target. The top line costs 5; the other three cost 1 each. The only line sets reaching the target are the top line alone (1 press, cost 5) and the other three lines (3 presses, cost 3). For either choice about the top line, the lamp conditions force every other line. No repeated-press sequence improves either optimum: two identical presses cancel and all prices are positive. The adult extension changes the price 5 to 3 (a cost tie) and then 2 (the direct line becomes cheapest).

The optional edge-lamp mega-bonus is omitted to preserve working space for the four requested investigations and avoid a fifth rule system on the final page.

## Prior use and sources

The problem choices and mathematical intentions come from the organizer's September 30 request. The two approved Week 2 catalogs supply the visual convention: an empty circle is OFF, a dot is ON, and the arrow runs from start to target. This packet matches their Arial typography, grayscale vector drawings, brief numbered tasks, and header/footer structure.

Related prepared material is not evidence of classroom use. The upper catalog already studies solution sets, components and shortest moves. This supplement changes the focal questions: nonempty actions with no net change; predicting one compulsory line before solving; a new single-lamp action; and unequal prices. The solo-button idea also occurred in the archived K-1 design described in [week-02-redesign.md](week-02-redesign.md); it is not claimed to be new to the entire library. Check the use log before offering it to a returning child.

The organizer's [Fall 2025 Handout 9](../lowell-math-circle-year-1/lowell-math-circle/Math%20Circle%20Fall%202025/Handouts%209.docx), Problem 9.1, uses divisor-based door switching. It supplies earlier toggle context, not these line-press instances. It establishes prior material, not which child encountered or mastered it.

Teaching references consulted in Natasha Rozhkovskaya's [*Math Circles for Elementary School Students*](../external-resources/msri-math-circle-books/Math%20Circles%20for%20Elementary%20School%20Students.epub):

- **“Introduction: Berkeley 2009”** describes additional instructors and actively involved parents helping children individually.
- **Lesson 6, “At the lesson,” item 2, “About sausages” (Problems 6.2-6.3)** reports that a verbal explanation did not convince everyone, so the group considered more examples before an argument emerged.
- **Lesson 6, “At the lesson,” item 4, “Experiments with triangles and quadrilaterals” (Problems 6.6-6.8)** reports limited child enthusiasm despite adults appreciating the demonstration. The author's proposed explanation is distinguished there from the observation.

Our design inferences are to keep experimentation first, reserve hints for adults, and observe which variations children actually want to continue. These lamp activities are not taken from that book, and mathematical correctness does not establish that a page will work well in the room.

## Build and review

From the repository root, using Python with ReportLab:

```sh
python3 plans/verify-week-02-bonus.py
python3 lowell-math-circle-year-2/source/week-02/build-bonus.py
```

The local bundled interpreter is `/Users/jamespfeiffer/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3`. No LaTeX is used. The bonus has its own build; the main Week 2 and combined packets are not rebuilt or replaced.

The verifier enumerates every subset for the exact graphs and states read by the builder, checks every bridge solution, enumerates all 64 solo-button states and independently confirms them by breadth-first search, and verifies both priced optima. The checked JSON records the actual line sets. All four student pages and both adult pages were rendered with Poppler and visually reviewed; text bounds, US Letter geometry, numbering, prohibited student terminology and PDF metadata were checked separately. Review intermediates belong in `tmp/pdfs/week-02-bonus/`.

After use, record the exact problem and cases, whether a hint was needed, what was tried, conjectured or proved, and whether the child wanted to continue. Leave unused pages marked as reserves.
