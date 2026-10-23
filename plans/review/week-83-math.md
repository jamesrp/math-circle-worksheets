# Week 83 (Hackenbush balances): math check

Scope:
- `lowell-math-circle-year-2/week-83/week-83-students.pdf`, 7 pages, one shared packet:
  - p. 1 (header "Grades 2–5"): the shared rules, the worked cut (B,R,B → Red cuts R → B), Problem 1 (boards A–D).
  - p. 2: Problem 2 (boards A–C). p. 3: Problem 3 (boards A–C). p. 4: Problem 4 (two blank ground lines).
  - p. 5 (header "Grades 4–5"): the birthday rule, the example −2 □ 2 → 0, Problem 5 (four mats).
  - p. 6 (header "Grades 4–5"): Problem 6 and the 15 birthday cards. p. 7: extra workspace.
- `week-83-facilitator.pdf`, 5 pages.

Sources read: `source/week-83/student/students.tex`, `guide/facilitator.tex`, `build.py`, `README.md` and `SOURCES.md`. I looked at the opening of the package's `check_math.py` only to see what it is. I did not run it or import from it. My scripts and their outputs are in this run folder, for `plans/review/checks/week-83/`. Checked October 23, 2026.

**Result: every printed board, the worked cut, every winner class, the Problem 5 answers and all 15 cards are correct, and so is every solution the guide gives. I found 2 problems, both minor:**
1. **Problem 4 can be answered by copying.** The two balanced boards already printed on pp. 2–3 meet its condition, and the guide's two examples are exactly those boards.
2. **The guide's nursery treats every empty pair of bounds as "not in this catalog".** It never says the left bound must be below the right one. If a child's invented pair has the left card at or above the right card, no number of any day fits, but the guide's advice suggests a later day would supply one.

## How it was checked

- **`check_math.py`** (output `check_math.py.out`, 0 failures). Standard library and exact fractions only.
  - **The game.** Stalks are strings read from the ground up, and a cut at segment j leaves the part below it. Who wins comes from plain minimax over legal moves, with no theory. Values are computed separately, from each whole board's options and never by adding stalk values. Each is the simplest number between the best Blue and best Red options, computed two ways: from the birthday tree and from a closed form. The two always agree.
  - **The theory the guide relies on**, replayed on all 1,528 boards of up to 3 stalks of length ≤ 4 (≤ 8 segments):
    - the sign of the value always matches the minimax winner (positive Blue, negative Red, zero second player);
    - the value of a whole board equals the sum of its stalk values;
    - swapping colours negates the value;
    - the sign-expansion rule gives the value of all 510 single stalks of length 1–8.
  - **Printed boards.** Read from `students.tex`. For each: value, winner class, every winning first move for each starter, and a full reply table showing how the winner answers every opening by the other colour.
  - **The guide's response proof** for BR + BR + R. It is replayed as a strategy against every opponent move, and it wins in all lines.
  - **Problem 4.** The guide's examples, the copy shortcut and seven other balanced boards; every stalk plus its colour-swapped copy balances.
  - **Nursery.** The birthday tree for days 0–3 against the guide's list and the 15 printed cards. The p. 5 example and the Problem 5 answers. Every ordered pair of card bounds: whether a card fits, whether the earliest card is unique, and whether the catalogue pick is the true simplest number. Which pairs choose a card newer than both bounds. The guide's Problem 6 examples.
  - **Asides.** Material counts, the edge-count hint, the encore's "same value, same outcome with any test stalk", and the green-edge remark.
- **`check_diagrams.py`** (output `check_diagrams.py.out`, 0 failures). Reads the delivered student PDF with PyMuPDF:
  - **Every page.** Headers, footers, problem numbers 1–6 once each, no Name field.
  - **pp. 1–3.** Every thick coloured segment is taken from the PDF drawing list. Segments are chained into stalks, and each stalk must stand on a black ground line. Every printed letter must match its segment's colour (53 segments). All segments are 62.4 pt long. Boards are named by the nearest board letter and compared with the boards in the math check.
  - **p. 1 worked cut.** Solid B,R,B; then solid B with dashed R and B above it and an X on the dashed R; then B alone.
  - **pp. 5–6.** The four mats' bounds in order, the example's cards and days, and the 15 cards with day counts 1, 2, 4, 8.
  - **Guide page references.** Cards on page 6, workspace on page 7.
- **`check_rebuild.py`** (output `check_rebuild.py.out`, 0 failures). Compiles both `.tex` sources. Checks that the rebuilt PDFs match the delivered ones: same extracted text, every word within 1 pt, and pages that render the same at 80 dpi (the guide differs only by anti-aliasing).

The facts the packet rests on, by hand:
- **Stalk values.** Blue's options are on the left and Red's on the right:
  - B = {0 | } = 1 and R = { | 0} = −1;
  - BR = {0 | 1} = 1/2: Blue's cut drops everything, and Red's leaves B;
  - BRR = {0 | 1/2, 1} = 1/4: the upper R cut leaves BR, the lower leaves B;
  - RB = {−1 | 0} = −1/2 and BB = 2.
  - The p. 1 example BRB is 3/4 and is not a task board.
- **The balances.** A zero board is a second-player win.
  - **BR + BR + R.** The guide's three cases are the only openings up to symmetry, and every later move is forced. The replay confirms this.
  - **BRR + BRR + RB.** If Blue opens by removing a whole BRR, Red cuts the other BRR's top R (BR + RB = 0). If Blue cuts the top B of RB, Red cuts a top R (BR + BRR + R = −1/4). If Red cuts a top R, Blue removes a whole BRR (BR + RB = 0). If Red cuts a middle R, Blue removes the remaining whole BRR (B + RB = 1/2). If Red cuts the R of RB, Blue removes a whole BRR (BRR = 1/4).
- **Simplicity.** For numbers L < R, exactly one number in between has the earliest birthday. If two different numbers had the same birthday, an earlier-born number would lie between them. The script confirms this on all 91 card pairs with left < right that some card fits.

## Student packet (pp. 1–7): correct except items 1 and 2

- **Rules and worked cut (p. 1).** Red's only cut on B,R,B removes the middle R, and the top B drops, leaving B. That is what the three pictures show, with the X on the cut R and the "drops" arrow on the B above.
- **P1 (p. 1).**
  - A: B = 1, so Blue always wins. With Red starting, Red cannot move and loses at once.
  - B: R = −1, so Red always wins.
  - C: B + R = 0, a second-player win, so no colour always wins.
  - D: BB + R = 1, so Blue always wins. With Blue starting, Blue must cut the top B; cutting the bottom B loses (see "Not counted").
  - So one colour can always win on A, B and D.
- **P2 (p. 2).**
  - A: BR + R = −1/2, a Red win. Red starting cuts the top R, leaving B + R.
  - B: BR + BR + R = 0, which balances.
  - C: 3·BR + R = 1/2, a Blue win. Blue starting removes a whole BR.
  - Only B balances.
- **P3 (p. 3).**
  - A: BRR + RB = −1/4, a Red win. Red's only winning first move cuts the top R of BRR, leaving BR + RB = 0. If Blue starts:
    - Blue removes BRR, and Red cuts the R of RB;
    - Blue cuts the top B of RB, and Red cuts either R of BRR.
  - B: BRR + BRR + RB = 0, which balances.
  - C: 3·BRR + RB = 1/4, a Blue win. Blue starting must remove a whole BRR; cutting the top B of RB loses. If Red starts, every Red move leaves a positive board, and the reply table in `check_math.py.out` lists Blue's answers.
  - Only B balances. "Find a way for the winning color to win each other board, whoever starts" is possible for A and C.
- **P4 (p. 4).** Possible. Item 1 is a shortcut.
- **P5 (p. 5).** The opening rule's example is right: −1, 0 and 1 all fit between −2 and 2, and 0 (day 0) is earliest. The four mats give:
  - greater than 0, less than 3: 1 (day 1), not the midpoint 3/2;
  - greater than −1, less than 1: 0;
  - greater than 0, less than 1: 1/2;
  - greater than 1/2, less than 1: 3/4.

  In each case the earliest card is unique and is the true simplest number.
- **P6 (p. 6).** Both tasks are possible with the printed cards.
  - **Same card from two pairs:** for example (−1, 1) and (−2, 2), both choosing 0.
  - **A card newer than both bounds:** exactly 8 card pairs do this. They are (−2, −1) → −3/2, (−1, −1/2) → −3/4, (−1, 0) → −1/2, (−1/2, 0) → −1/4, (0, 1/2) → 1/4, (0, 1) → 1/2, (1/2, 1) → 3/4 and (1, 2) → 3/2.
  - **The cards.** The 15 cards are exactly the numbers born on days 0–3 (1, 2, 4 and 8 of them), each with its correct first birthday.
- **Diagrams.** Every board on pp. 1–3 matches what the page and the guide assume. Every letter matches its segment's colour, all segments are the same length, and every stalk stands on its ground line. The mats and cards are both 40 × 24 mm, so a card fits a mat's middle box.

### 1. p. 4 Problem 4 (minor): copying the balanced boards from pp. 2–3 satisfies the task, and the guide's examples are exactly those boards

- **Quoted text.**
  - Student p. 4: "Problem 4: Make two different boards that balance. Each board must include a stalk with at least two segments."
  - Guide p. 4: "Problem 4 examples: BR+BR+R, and BRR+BRR+RB are different balanced boards and each has a multi-segment stalk."
- **Evidence.**
  - BR + BR + R is the board printed as Problem 2B, and BRR + BRR + RB is Problem 3B. Both are balanced, and both contain a stalk of two or three segments (`check_math.py.out`). So a child who copies the two "yes" answers from the previous two pages has met every printed condition without building anything.
  - The two-segment condition rules out B + R from Problem 1C, which suggests that new boards were intended. The guide's first route ("10 minutes constructing a difficult board for a partner") also points to invention. But the guide's own key gives only the copied boards, so an adult has no new example to offer.
  - Many new balanced boards exist. Among small boards of up to 3 stalks of length ≤ 4, 42 balance and contain a stalk of length ≥ 2. Examples:
    - BR + RB, and in general any stalk with its colour-swapped copy;
    - B + RB + RB;
    - BB + RR;
    - BRB + RBR;
    - BBR + R + RB;
    - BR + BRR + BRR + R.
- **Smallest fix.**
  - Student: "Problem 4: Make two different boards that balance and are not on pages 1–3. Each board must include a stalk with at least two segments."
  - Guide: replace the examples with, for example, "BR + RB (any stalk with its colour-swapped copy balances: copy your partner's moves), B + RB + RB, and BR + BRR + BRR + R."

## Adult guide (5 pp.): correct except item 2

The overview's facts are true as stated:
- **Values.** The stalk values (B = 1, R = −1, BR = 1/2, BRR = 1/4, RB = −1/2) and the two zero sums are right.
- **Outcomes.** A zero board is a second-player win with no draw, and a positive or negative value is a win for Blue or Red whoever starts. The script replays both on 1,528 boards.
- **Equality.** It means indistinguishable in every sum, not equal edge counts. The encore pairs of the same value give the same outcome with every one of 31 test stalks, and BR and BRR are told apart by adding RB.
- **The nursery examples** {0 | 3} = 1, {−1 | 1} = 0, {0 | 1} = 1/2 and {1/2 | 1} = 3/4.
- **Finite birthdays give dyadics.** The day 0–3 lists are right.

The solutions are correct:
- BR = {0 | 1} and BRR = {0 | 1, 1/2}, with the option descriptions as given.
- The winner classes for Problems 1–3.
- The three-case response proof for BR + BR + R. It is complete: these are the only openings up to symmetry, and the replay wins against every line.
- Problem 5's 1, 0, 1/2, 3/4.
- Problem 6's (−1, 1) and (−1/2, 1/2) → 0, and (0, 1) → 1/2, newer than both bounds.
- The asides:
  - "No finite-day card is greater than all 0, 1, 2, …; the simplest surreal with those lower bounds is ω".
  - {0 | 1, 1/2, 1/4, …} is a positive infinitesimal.
  - Week 82's ordinal 1 + ω = ω against the commutative surreal 1 + ω = ω + 1.
  - A single green edge is ∗, a first-player win. G plus a stalk of value −x is never a second-player win for any x of birthday ≤ 3, consistent with "cannot be any number".
  - Twelve segments of each colour suffice; the largest board, 3C, needs 4 blue and 7 red.

### 2. Guide pp. 1 and 4, nursery (minor): no hypothesis that left bounds are below right bounds, and "not in this catalog … later construction" for every pair with no card

- **Quoted text.**
  - Guide p. 1: "Optional Grades 4–5 nursery: choose the earliest-born number strictly above all left bounds and below all right bounds."
  - Guide p. 4: "When the supplied finite catalog has no permitted card, say "not in this catalog" before discussing later construction."
  - Student p. 6: "Problem 6: Make two different pairs of bounds that choose the same number card. Make a pair that chooses a card newer than both bounds."
- **Evidence.** Problem 6 has children choose their own bounds from the 15 cards. Of the 210 ordered pairs of two different cards, 105 put the larger card on the left, and for all of these no number of any birthday fits (`check_math.py.out`; for example 1 on the left and 1/2 on the right). That is a different case from pairs such as (1/4, 1/2), (2, 3) and (3/4, 1), whose numbers 3/8, 5/2 and 7/8 are born on day 4 and so are only missing from the catalogue (14 such pairs).
  - The guide gives one instruction for both cases. Saying "not in this catalog" and then "discussing later construction" tells a child with a reversed pair that a later day will supply a number, which is false.
  - The overview's rule is stated without the hypothesis L < R. The simplicity theorem {L | R} = simplest number needs it. With L ≥ R, the game {L | R} is not a number at all; {0 | 0}, for instance, is the green edge ∗ the guide mentions on p. 3.
- **Smallest fix.**
  - Overview p. 1: "…choose the earliest-born number strictly above all left bounds and below all right bounds (this needs every left bound below every right bound)."
  - Guide p. 4: "When the left card is below the right card but no card fits (for example 1/4 and 1/2, whose number 3/8 is born on day 4), say "not in this catalog" before discussing later days. When the left card is not below the right card, no number of any day fits."

**Not counted (outside the math scope, accepted design, or correct as printed):**
- **Problem 1D trap.** The guide's key says only "Blue" for BB + R. With Blue starting, cutting the bottom B removes both blue segments, and Red then wins by cutting R. Only the top cut wins. A pair that plays D once each way can record it as "not always won". The guide's hint covers trying both starters but not trying other moves. One sentence in the key would help: "on D, Blue starting must cut the top segment." The same holds on 3C, where Blue must not cut the top B of RB, and on 3A, where Red's only winning opening is the top R of BRR.
- **No key for "Find a way … whoever starts" (Problem 3A and 3C) or for the 3B balance.** The guide gives winner classes and the arithmetic 1/4 + 1/4 − 1/2 = 0 only. Its statements are correct; a reply key for adults is in `check_math.py.out` ("Reply tables") and in the hand proofs above.
- **Placement.** The guide's Problem 3 paragraph contains "One BR plus R is negative … three BR plus R is positive", which is about Problem 2. It is true as stated.
- **Strictness in the p. 5 example.** The example's bounds (−2, 2) give 0 whether "greater than" is read strictly or not, so it does not show strictness. Under a non-strict reading, Problem 5 would give 0, 0, 0, 1. The printed words are "greater than" and "less than", which are strict, and the guide says so: "A left-bound card means strictly greater; right means strictly smaller".
- **Problem 6 second task can be copied from Problem 5.** Mats 3 and 4 already choose cards newer than both bounds: (0, 1) → 1/2 and (1/2, 1) → 3/4. This is legitimate.
- **Edge-count hint.** "Play B versus BR and compare a cut at the bottom" is terse but correct under either reading. Read as separate boards, B = 1 and BR = 1/2 are both Blue wins, though their blue-minus-red counts are 1 and 0. Read as B + RB, the value is 1/2, a Blue win.
