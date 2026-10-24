# Mathematical review: Poisoned cookie (Chomp) draft

Reviewer: independent math critic (CRITIC-MATH stage). The draft was not edited.

## Method

- Board shapes were read from the TikZ coordinates in `draft/src/*.tex` and turned back into row lengths. Each one was compared with the rendered pages of `draft/*.pdf`, rendered at 50 dpi and inspected page by page. The `.tex` files and PDFs were built in the same run (timestamps 15:11:54–15:12:01), and every board on the rendered pages matches the parsed shape.
- Win/lose labels and all winning bites were computed with two solvers written for this review. Neither uses the author's `chomp.py`. Solver A works on arbitrary sets of cells, so it handles any arrangement of counters. Solver B works on row-length tuples. A third, specialised three-row solver went up to 3 by 60. All of them agree wherever they overlap.
- Notation: a bite (r, c) is row r, column c, counted from the poison corner. A position is written as its row lengths, bottom row first, so (4,2,2) is a bottom row of 4 cookies with rows of 2 and 2 above it. "Mover" means the player whose turn it is.

General facts verified:
- On squares from 2 by 2 to 9 by 9, the only winning first bite is (2,2).
- On an L shape with arms a (to the right) and b (upward), the mover loses exactly when a = b. Checked for all a, b ≤ 11.
- On two rows, the mover loses exactly when the top row is one shorter than the bottom row. Checked for every bottom row up to 40, counting a single row as a top row of length 0.
- Every rectangle up to 5 by 8 has exactly one winning first bite. In particular: 3 by 4 → (2,3), leaving (4,2,2). 3 by 5 → (3,4), leaving (5,5,3). 3 by 6 → (2,4), leaving (6,3,3). 4 by 5 → (3,3), leaving (5,5,2,2). These match all the claims in the outline.
- Strategy-stealing check on 3 by 4. Eating the top-right cookie leaves (4,4,3), and the mover there wins. The only winning reply is (2,3), leaving (4,2,2), which the first player could have produced directly. The same check gives the same result on 3 by 3, 4 by 4, 3 by 5, 3 by 6 and 4 by 5.

## Located problems

### 1. Grades 4–5, page 4, Problem 5: "L position" also reads as "L-shaped position"

Quoted text: "…the second player would answer with a bite that leaves an L position. … Then the second player would face the L position…"

Evidence. In this packet, "L" was defined only in Problem 2, as a box label ("Write W in its box if so, and L if not"). But L shapes are everywhere a 4–5 child has just worked:
- the square strategy asked for in Problem 3 produces an L with equal arms;
- the board printed under Problem 5 is itself an L, (3,1,1).

A child who reads "L position" as an L-shaped position and checks Ana's reasoning on 3 by 4, as Problem 5 asks, finds this: after the top-right bite, the second player's only winning reply is (2,3). It leaves (4,2,2), which is not an L shape. So the child concludes that Ana is wrong, which is the opposite of the intended answer.

Smallest fix:
- Replace "leaves an L position" with "leaves a position where the player whose turn it is cannot make sure to win".
- Replace "would face the L position" with "would face that position".

A shorter alternative is "leaves a position you would mark L in Problem 2".

### 2. Grades 4–5, page 4, Problem 5: "it's not a rectangle" answers the last question without the key idea

Quoted text: "Then explain why her reason does not work on this board, where the first player cannot make sure to win." The board is (3,1,1).

Evidence. Ana's statement begins "On a rectangle…", and (3,1,1) is not a rectangle. So "her reason does not work here because it is not a rectangle" is a complete, correct answer to the question as printed. It skips the intended discovery, which is that no cookie lies in every bite:
- The bite at (1,2) eats the right arm and misses (3,1).
- The bite at (2,1) eats the top arm and misses (1,3).

So the step "the first player could have made that same bite at the start" has no cookie to steal with.

Smallest fix: "Then explain which step of her reason breaks on this board, where the first player cannot make sure to win."

### 3. Grades 4–5, page 3, Problem 3, and Grades 2–3, page 3, Problem 5: the 1 by 1 square is an exception

Quoted text:
- Grades 4–5: "…on every rectangle with two rows and on every square, however long the sides are."
- Grades 2–3: "Explain how the first player can make sure to win on every square board, even this 10 by 10 one."

Evidence. On a 1 by 1 board the only cookie is the poison, so the first player must eat it and loses. Ana's statement in 4–5 Problem 5 correctly says "with more than one cookie". The two-row part of 4–5 Problem 3 is fine at its smallest case: on 2 by 1 the first player eats the top cookie and wins.

Smallest fix:
- Grades 4–5: "on every square bigger than one cookie".
- Grades 2–3: "every square board bigger than one cookie, even this 10 by 10 one".

### 4. K–1, page 5, Problem 6, and Grades 2–3, page 5, Problem 7: nothing limits what shape a "board" can be

Quoted text:
- K–1: "Build a board where the player who goes second can always win, and color it on a grid. Find as many different boards as you can." The page has six 4 by 5 grids.
- Grades 2–3: "Find boards with three rows where the player who goes second can always win. Color each one you find on a grid." The page has eight 3 by 7 grids.

Evidence.

Under the intended reading, a board is a shape that can arise in play: each row starts at the poison's column and is no longer than the row below it.
- In the 4 by 5 grid there are exactly 16 second-player wins, counting the poison alone: (1), (2,1), (3,2), (4,3), (5,4), (3,1,1), (2,2,1), (4,2,2), (5,3,2), (5,5,3), (4,1,1,1), (2,2,2,1), (3,3,1,1), (5,2,1,1), (5,3,3,2), (5,5,2,2).
- In the 3 by 7 grid exactly 10 use all three rows: (3,1,1), (2,2,1), (4,2,2), (5,3,2), (6,4,2), (6,3,3), (5,5,3), (7,5,2), (7,4,3), (7,7,4).
- So the six and eight grids fit.

But children build with loose counters, and the bite card plays any arrangement. Under that reading, solver A finds:
- 28,577 second-player-win arrangements in 4 by 5;
- 46,930 that use all three rows of 3 by 7.

The simplest has three counters with gaps: the poison, (1,3) and (3,1). Whatever the mover bites, the opponent bites the other cookie, and the mover is left with the poison. A connected example is poison, (1,2), (1,3), (1,4), (2,1), (2,2), (3,2): the top cookie overhangs a gap.

Nobody at the K–1 table can check such answers. That table's adult is the non-mathematician parent, and there is no guide.

Material fit compounds this.
- K–1: answers such as (5,5,2,2), (5,3,3,2) and (5,2,1,1) need a board 4 rows by 5 columns, larger than any printed board (largest: 4 by 4 and 3 by 5).
- Grades 2–3: five of the ten three-row answers need 6 or 7 columns. The printed three-row boards stop at 3 by 5, and 2 by 6 has only two rows.
- So children must lay counters loose on the table, which is exactly when odd shapes appear.

Smallest fix: make the board by bites, which the bite card enforces. Shapes reachable by bites from a full grid are exactly the intended ones.
- K–1: "Take bites from a full grid of cookies to make a board where the player who goes second can always win, and color it on a grid. Find as many different boards as you can."
- Grades 2–3: "Take bites from a full 3 by 7 grid of cookies to make boards with three rows where the player who goes second can always win. Color each one you find on a grid."

If children are expected to build these, also add a 4 by 5 board (K–1) and a 3 by 7 board (2–3) to the materials.

## Problem-by-problem verification

All answers below come from my solvers. A dash means the mover loses, so no X is expected.

### K–1: correct apart from item 4

| Problem | Asks | Boards on page | Intended answer (verified) |
|---|---|---|---|
| 1 (p1) | Mark a winning first bite if one exists | (4), (2,1), (2,2), (3,1) | (1,2) leaving (1); —; (2,2) leaving (2,1); (1,3) leaving (2,1). Each winning bite is the only one. |
| 2 (p2) | Find the winning first bite against the adult | 2 by 3, 2 by 4 | (2,3); (2,4). Top-right, the only winning bite. |
| 3 (p2) | Same task | 3 by 3 | (2,2), the only winning bite, leaving the L (3,1,1) |
| 4 (p3) | Circle the second-player wins | L shapes (3,1,1), (4,1,1), (4,1,1,1), (2,1,1,1) | Circle (3,1,1) and (4,1,1,1), the equal-arm ones. Arms are 2/2, 3/2, 3/3 and 1/3. |
| 5 (p4) | Find the winning first bite | 4 by 4, 2 by 6 | (2,2), the only one; (2,6), the only one |
| 6 (p5) | Find second-player-win boards | six 4 by 5 grids | 16 staircase answers (see item 4) |

- Every diagram matches its text: 25 mm cells, the poison in the bottom-left corner, and one cookie on every other cell.
- The launch picture is correct. On 2 by 5, the bite (1,3) with the card corner at the bottom-left of cell (1,3) leaves (2,2).

### Grades 2–3: correct apart from items 3 and 4

| Problem | Asks | Boards on page | Intended answer (verified) |
|---|---|---|---|
| 1 (p1) | Mark a winning first bite, or explain why none exists | (3,1), (2,1), (2,2), (3,2), (4,2), (3,1,1) | (1,3); —; (2,2); —; (1,4) leaving (3,2); —. Each winning bite is the only one. |
| 2 (p2) | Find the winning first bite | 2 by 3, 2 by 4, 2 by 6 | Top-right: (2,3), (2,4), (2,6), each the only one |
| 3 (p2) | Mark winning bites, then find and explain the two-row rule | (5,4), (5,2), (6,6), (4,1), (6,5), (6,3) | —; (1,4) leaving (3,2); (2,6); (1,3) leaving (2,1); —; (1,5) leaving (4,3). The rule "the mover loses exactly when the top row is one shorter" holds up to 40. |
| 4 (p3) | Find the winning first bite | 3 by 3, 4 by 4 | (2,2) on each, the only one |
| 5 (p3) | Explain the square strategy | 10 by 10 drawn (99 cookies) | Bite (2,2), then mirror on the equal arms. True for every square except 1 by 1 (item 3). |
| 6 (p4) | Find the winning first bite | 3 by 4 | (2,3), the only one, leaving (4,2,2) |
| 7 (p5) | Find three-row second-player wins | eight 3 by 7 grids | 10 staircase answers (see item 4) |

### Grades 4–5: correct apart from items 1–3

| Problem | Asks | Boards on page | Intended answer (verified) |
|---|---|---|---|
| 1 (p1) | Find the winning first bite | 2 by 4, 2 by 6, 3 by 3, 4 by 4 | (2,4); (2,6); (2,2); (2,2). Each is the only one. |
| 2 (p2) | Label W or L for every position | all 19 positions inside 3 by 3 | Row 1: W W W W W. Row 2: W W **L** **L** **L** ((3,2), (3,1,1), (2,2,1)). Row 3: W W W W **L** ((2,1)). Row 4: W W W **L** ((1)). That is 5 L and 14 W. The 19 shapes are exactly all positions in the 3 by 3 box, with none missing or repeated. |
| 3 (p3) | Explain the two-row and square strategies | none | Correct except for 1 by 1 (item 3) |
| 4 (p3) | Find every winning first bite | 3 by 4 | Exactly one: (2,3). "Mark each one" is fine for a find-all task, but the answer is a single X. |
| 5 (p4) | Judge Ana's strategy-stealing argument; say why it fails on (3,1,1) | (3,1,1) | Ana is right. (3,1,1) is a second-player win. See items 1 and 2 for wording. |
| 6 (p5) | Find the winning first bite on three-row boards | 3 by 5, 3 by 6 (25 mm cells) | (3,4) leaving (5,5,3); (2,4) leaving (6,3,3). Each is the only one. |

## Note for the facilitator (not an error)

Grades 4–5, Problem 6, sets up a tempting false pattern. Together with 3 by 4 from Problem 4, the boards suggest this rule:
- even n: bite (2, n/2 + 1);
- odd n: bite (3, (n+3)/2).

It holds for 3 by 4 up to 3 by 8 and first fails at 3 by 9, whose only winning bite is (3,7), not (3,6). After that the rule fails at most widths (computed up to 3 by 60). The page's claim "Nobody knows a simple rule" stands. An adult who wants to test a child's conjecture can use 3 by 9.
