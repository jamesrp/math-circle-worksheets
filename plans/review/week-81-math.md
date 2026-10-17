# Week 81 (Buckets of Fish): math check

Scope:
- `lowell-math-circle-year-2/week-81/week-81-students.pdf`, 5 pages:
  - p. 1 (header "Grades 2–5"): the shared rule, the capped-refill rule for Problems 1–3, a worked visual and Problem 1.
  - p. 2: the reusable three-bucket board with Supply and Removed boxes.
  - p. 3: Problem 2 and its sixteen two-bucket sorting cards.
  - p. 4: Problem 3.
  - p. 5 (header "Grades 4–5"): the uncapped rule, a written-quantity visual, then Problems 4 and 5.
- `week-81-facilitator.pdf`, 4 pages.

Sources read: `source/week-81/student/students.tex`, `guide/facilitator.tex`, `build.py`, `README.md`, `QA.md` and `SOURCES.md`. I read the package's `check_math.py` only to see what it claims. I did not run it or import from it. My scripts and their outputs are in this run folder, for `plans/review/checks/week-81/`. Checked October 17, 2026.

**Result: every printed start, answer, diagram and worked example is correct, and so is every solution in the guide. I found 1 problem, a minor one in the guide's overview: one sentence describes the winning move as adding "0 or 1 to each earlier odd bucket". Read literally, that lets you add 0 to an odd bucket, which leaves it odd. The guide's own p. 3 states the move correctly.**

## How it was checked

- **`check_math.py`** (output `check_math.py.out`, 0 failures). It reads the printed starts from `students.tex` and generates every legal move from the p. 1 rule. Outcomes and game lengths come from a plain recursion over the legal moves; no parity formula drives it.
  - **Problems 1–3:** the outcome and every winning move for each printed start, under the warm-up cap (add 0 or 1 to each bucket to the left).
  - **The parity theorem, checked on finite cases:** the second player wins exactly when every bucket is even. This holds for refill caps 1 to 6: 1,554 starts each for caps 1–2 (1–4 buckets, 0–5 counters each) and 155 starts each for caps 3–6 (1–3 buckets, 0–4 each). The answer doesn't depend on the cap.
  - **The repair move:** the guide's p. 3 move is legal and reaches all-even. From an all-even position, no move reaches all-even.
  - **Lengths:** with refills capped at K, the longest game from (0,1) is K+1 moves and from (1,1,1) it is 1 + (K+1) + (K+1)², checked for K = 1 to 6. Under the warm-up cap, no game from (0,1) lasts more than 2 moves.
  - **Problem 4:** taking from bucket 2 and refilling bucket 1 with 9, 29, 99 or 999 gives games of exactly 10, 30, 100 and 1,000 moves. After the first move, every move is forced.
  - **Problem 5 and the ordinal:** 300 random plays from (1,1,1), with refills of up to 60 per bucket, all end. One deliberately long play (refill 500 each time) ends after 251,503 moves. In 5,000 random uncapped moves, ω^(m−1)a_(m−1) + … + a_0 always decreases.
  - **The encore:** with 1, 2 or 3 taken and refills capped at 3, 4 or 6, the second player wins exactly when every bucket is a multiple of 4. With caps 1 and 2 this fails, for example at (1,1).
  - **Materials:** how many counters capped play from the printed starts needs.
  - **Other readings:** two misreadings of the rule.
- **`check_diagrams.py`** (output `check_diagrams.py.out`, 0 failures). Uses pdfplumber on the released student PDF:
  - **Reading the pictures:** bucket boxes are the unfilled outlines and counters are the filled circles. Each counter is assigned to the box that contains it. Boxes are grouped into pictures and read with their printed labels 1, 2, 3.
  - **Layout:** headers, footers and consecutive problem numbers; the board and card dimensions.
  - **Counters:** none pokes out of its box, and they are spaced apart.
  - **Guide page references:** checked against the student PDF.

The infinite statements are proved by hand, not just sampled:
- **Termination (fixed finite number of buckets, finite starting counts, finite refills).** Use induction on the number of buckets. Nothing is ever added to the rightmost bucket, so its count never increases. It therefore changes only finitely often. After its last change, the rest of the play is a play on the buckets to its left, which ends by induction. Equivalently, ω^(m−1)a_(m−1) + … + a_0 drops at every move: its first change from the right is the −1 at the bucket taken from.
- **Parity.** From an all-even position, the bucket you take from becomes odd. From any other position, take one from the rightmost odd bucket j and add 1 to each odd bucket left of j and 0 to each even one. This is legal under the warm-up cap, and the result is all-even. The game always ends, at the all-zero position, which is all-even. So the player who keeps restoring all-even makes the last move.
- **Unique winning move under the cap.** A move to all-even must leave everything right of the bucket taken from unchanged and even. The bucket taken from must turn from odd to even. So it must be the rightmost odd bucket j. Each bucket left of j then needs exactly its parity added, 0 or 1, so the move is forced. The script confirms this on every first-player position with 1–4 buckets and 0–5 counters each.
- **No length bound from (0,1).** Bucket 1 is empty, so the only first move takes the counter from bucket 2 and adds some M ≥ 0 to bucket 1. Then each move must take one from bucket 1, and nothing can be added to its left. So the game lasts exactly M+1 moves, and every positive length occurs. Every play ends, yet there is no bound on how long.

## Student packet: checks out

- **Opening rule and visual (p. 1).** Before (1,1,2), after removal (1,1,1), after the refill (2,2,1). The removed counter is drawn struck through under bucket 3, and the move is legal under the cap. The picture adds to two buckets at once, which rules out two misreadings:
  - "at most one counter in total": under it, (3,3,1) in Problem 3 would become a second-player win;
  - "only the adjacent bucket": under it, no printed outcome changes.
- **P1 (p. 1).** The starts are (0,0,1), (1,1,0), (2,1,1), (2,2,2).
  - The first player wins from the first three. The unique winning moves go to (0,0,0), (2,0,0) and (2,2,0).
  - The second player wins from (2,2,2).
  - Game lengths are 1–4, 2–3, 4–8 and 6–14 moves.
- **P2 (p. 3).** The sixteen cards are every (left, right) pair with 0–3 in each, in reading order. They print 48 counters in total.
  - The second player wins exactly at (0,0), (0,2), (2,0) and (2,2). At (0,0) the first player cannot move and loses at once, as the printed rule says.
  - The longest game on any card is 9 moves, from (3,3).
- **P3 (p. 4).** (2,2,2) and (0,2,0) are second-player wins, and the other four starts are first-player wins.
  - Each first-player start has exactly one winning move under the cap: to (0,2,2), (2,0,2), (2,2,0) and (4,4,0). So "a rule for choosing a winning move" has an exact answer: make every bucket even.
  - (3,3,1) is the one printed start whose winning move adds to two buckets.
- **P4 (p. 5).** The picture is (0,1). Refills of 9, 29 and 99 give games of exactly 10, 30 and 100 moves, and a refill of N beats any named N. The page lifts the cap before this problem, and that is necessary: under the warm-up cap, no game from (0,1) lasts more than 2 moves.
- **P5 (p. 5).** The picture is (1,1,1). No agreed play goes on forever, by the termination proof above.
- **Quantity visual (p. 5).** It draws 12 counters, then "12 counters", then "remove 1", then "11 counters". That is correct.
- **Diagrams.**
  - **Board (p. 2):** three equal buckets, 56 × 139 mm, labelled 1, 2, 3 left to right.
  - **Cards (p. 3):** sixteen equal 39 × 27.5 mm cards, each labelled 1, 2.
  - **Pictures:** every small picture is labelled 1, 2, 3 (or 1, 2) left to right, and empty boxes stand for zero.
  - **Counters:** all are true circles inside their boxes. In three-counter boxes, the top counter touches the lower-left one, overlapping by 0.1 mm (0.28 pt). The counts are still unambiguous in a render.

## Adult guide: correct except item 1

- **Overview (p. 1).**
  - **Termination:** the statement and its proof sketch (rightmost bucket, then induction) are true under the stated hypotheses.
  - **"Finite refills and a fixed finite number of buckets are essential":** true in the sense that neither can simply be dropped. A bucket holding infinitely many counters never empties. With buckets running endlessly to the left, a single counter can be passed left forever.
  - **No uniform bound from (0,1):** correct, with exactly M+1 moves.
  - **Parity:** the all-even characterization is correct for both the capped and the uncapped game. Only the wording of the repair move is off; see item 1.
- **Materials (p. 2).**
  - The page references (board p. 2, cards p. 3, continuation p. 5) match the student PDF.
  - "Thirty loose counters" is ample. The most a capped play from any printed start ever uses is 14 counters, even if removed counters are never reused. At most 8 are on the board at once, and at most 8 sit in one bucket.
- **Solutions (p. 3).** All correct: the Problem 1–3 answers, the Problem 4 lengths and their L+1 construction, the Problem 5 argument, the parity paragraph and the ordinal ω^(m−1)a_(m−1) + ⋯ + ωa_1 + a_0. That ordinal is written in the correct order, ω^k·a, and it decreases at the bucket taken from.
- **Encore (p. 4).** Take 1, 2 or 3, and the losing positions are exactly those where every bucket is a multiple of four. This is correct with any refill allowance of at least 0–3. Under the warm-up cap it fails: (1,1), for example, is a second-player win. The guide warns about this.
- **Return visit (p. 4).** One bucket of n always lasts exactly n moves. Total counter count can rise, from 4 to 5 in the p. 1 example. Both statements are correct.

### 1. Guide p. 1, overview, third paragraph (minor): the repair move is misstated

- **Quoted text:** "From any other position, remove from the rightmost odd bucket and add 0 or 1 to each earlier odd bucket to restore all-even."
- **Evidence:** read as written, the sentence allows adding 0 to an earlier odd bucket, which leaves it odd.
  - From (1,0,1), take from bucket 3 and add 0 to the odd bucket 1. That gives (1,0,0), which is not all-even.
  - The move that works adds exactly 1 to each earlier odd bucket and 0 to each earlier even one, giving (2,0,0) (`check_math.py.out`, "Guide p. 1 overview sentence" block).
  - Under the warm-up cap, this is the only winning move (proof above).

  The guide's p. 3 parity paragraph says it correctly: "Every earlier odd bucket is repaired by adding one, and earlier even buckets by adding zero." An adult who reads only the overview could still accept a child's "add nothing" repair as a winning move.
- **Smallest fix:** "…remove from the rightmost odd bucket and add 1 to each earlier odd bucket (0 to each earlier even one) to restore all-even."
