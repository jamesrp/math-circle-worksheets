# Week 49 math check: Four-tower differences

Checked: the current student PDFs `week-49-k-1.pdf` (5 pages), `week-49-grades-2-3.pdf` (5), `week-49-grades-4-5.pdf` (6) and `week-49-bonus.pdf` (3), with the adult guides `week-49-facilitator.pdf` (4) and `week-49-bonus-facilitator.pdf` (2), all in `lowell-math-circle-year-2/week-49/`. Archive folders were ignored. Every page was rendered and looked at, and the builders in `source/week-49/editable/src/` and `source/week-49-bonus/student/` were read for coordinates. The data used in the checks comes from the PDFs themselves.

Method: `pdf_extract.py` reads every ring from the delivered PDFs with Poppler: stations, arrowheads and their direction, printed heights, A–D labels, printed gaps, mat sizes, cycle edges and table sizes. It writes `pdf_geometry.json`. `check_base.py` and `check_bonus.py` then recompute every task from that data, along with every arrow chain, count and claim in both guides. They use exhaustive enumeration: all 625 and 1,296 bounded starts, all 24 orders, all predecessors with a proof that the search is complete, all 16 parity patterns, all starts up to height 20 for termination and divisibility, and all 64 six-rings and 256 eight-rings. Run `pdf_extract.py` first. Outputs are in `*.out`. No author checker was used.

**Result: no wrong answer, false claim or broken diagram anywhere.** Every printed ring, worked example and gap label is right, and so is every key, trajectory, count and proof in both guides. I found four minor located problems and one note. The first is a printed giveaway, the second is mat spacing, and the third and fourth are wording edge cases. They follow the per-problem record.

## Per-problem record (all verified)

The rule is new = |old − next old| at the arrow's tail, with all stations updated from one unchanged old ring. In every band the arrows run A→B→C→D→A (A→B→C→A for three stations), as the shared rule and the guide assume (`pdf_extract.out`).

**Page 1 example (all bands).** The old ring (1,4,2,0) has printed gaps 3, 2, 2, 1 on A→B, B→C, C→D and D→A. The new ring (3,2,2,1) equals D(old). The caption is right.

**K–1**
- P1: run the four starts to zero. (1,1,0,0) takes 3 moves, (1,0,1,0) takes 2, (2,1,0,1) takes 2 and (0,0,0,2) takes 4. These match the guide.
- P2: find the longest run with heights 0–4. The maximum is 7, reached by 16 of the 625 starts, including (0,1,2,4). This matches the guide.
- P3: one-move starts are exactly the positive constants (checked for heights 0–9). P4: two-move starts are exactly those whose four gaps equal one positive c (170 starts in 0–9). The guide's examples (0,1,0,1) and (0,1,2,1) are right.
- P5: (1,0,0,0) reaches zero in 4 moves. The three-station start (1,0,0) gives (1,0,1), (1,1,0), (0,1,1), then (1,0,1) again, a period-3 cycle. The big three-station mats have the same labels and arrows as the small diagram.
- P6: of the 24 orders of 0, 1, 2, 4, eight last 7 moves (the rotations and reversals of (0,1,2,4)) and sixteen last 4. The printed rings take 7 and 4 moves (see problem 1 below).

**Grades 2–3** (P1, P2 and P4 are the same as K–1's P1, P2 and P5, with range 0–5: maximum 7, reached by 32 of 1,296 starts)
- P3: (2,0,2,0) is possible. Its normalised predecessors are (0,2,2,0) and (2,0,0,2). (1,1,1,0) is impossible because its total is odd. (1,1,1,1) is possible, with six normalised predecessors. (0,0,0,2) is impossible: its total is even, but three zero gaps force a constant ring. The search is complete because 2(max − min) ≤ sum of the gaps. The guide's answers and parity argument are right.
- P5: same as K–1 P6. The guide's rotation and reversal classification, with representatives of 7, 4 and 4 moves, is right.
- P6: no new height can exceed the old maximum (checked for heights 0–8, and |a−b| ≤ max(a,b) in general). The tallest height can stay, as in (0,1,2,4) → (1,1,2,4).

**Grades 4–5** (P1–P4 are the same as Grades 2–3)
- P5: the letter rule is the parity of the gap, and the worked example EOEE → OOEE is right. After 1, 2, 3 and 4 moves the possible letter rings are 8, 4, 2 and 1 patterns, and only EEEE remains after four moves. The guide's rows (a+c, b+d, a+c, b+d) and (s, s, s, s) are right.
- P6: (2,8,4,0) = 2 × (1,4,2,0). Both runs, and the tripled run, take 4 moves. Scaling by 2, 3 or 5 keeps the move count for every start in 0–5.
- P7: the answer is no, by the same bound as 2–3 P6. P8: yes, every start terminates (all 194,481 starts with heights 0–20 checked). After 4k moves every height is divisible by 2^k (k = 1–5). The number of moves is at most 4k when 2^k > max, as the guide's proof gives.

**Base guide.** Every arrow chain it prints follows the gap rule (9 chains). Its move counts and its 625 and 1,296 maxima are right. So are the overview claims: the maximum never increases, it need not drop each move, the total height is not conserved, three stations can cycle, a nonzero constant start takes 1 move, and positive scaling keeps the move count. The material figures are right: 40 mm squares, centres 52 mm apart, the three-station span of 52 × 52 mm, and 40 cubes = 8 × 5. The route note's problem numbers match the packets. **Checks out completely.**

**Bonus.** The examples (1,3,2,0) → (2,1,2,1) and the directed (1,3,3,1) → (+2,0,−2,0) are right.
- P1: the complete sets, with heights 0–3 and a 0, are 6 old rings for (1,1,1,1) and 4 for (1,2,1,2). These are exactly the guide's lists, the restriction loses no normalised predecessor, and both fit the 6-row tables.
- P2: 100100 enters a period-3 cycle from round 1. 10000000 is 11111111 at round 7 and 0 at round 8. All 256 eight-rings are 0 by round 8. The doubling-distance identity holds.
- P3: (0,1,0,1) first exceeds 10 at round 5 (16). (0,0,1,1) does so only at round 9. Every directed output sums to 0.

The guide's lists, chains, the second-run listing, the sign counts (6 and 4), the translation/complement and collision claims, the station sizes (20.5 mm and 21.9 mm), the 16 counters, the 8 cards and the 12 cubes (the largest listed old ring plus its new ring needs exactly 12) are all right. **Checks out completely**, apart from the wording edge in problem 4.

## Located problems

### 1. K–1 P6 and Grades 2–3 P5 print a longest order, so the page answers the question (should)

- Where: K–1 page 5, Problem 6, "Put 0, 1, 2, and 4 around the four stations. Find an order that lasts longer than the other orders you try." Also Grades 2–3 page 5, Problem 5, "Try different orders of 0, 1, 2, and 4. Which order lasts longest?" Both print the rings A=0, B=1, C=2, D=4 and A=0, B=1, C=4, D=2.
- Evidence (`check_base.out`, section "orders"): (0,1,2,4) lasts **7** moves, the maximum over all 24 orders, and (0,1,4,2) lasts 4. Running the first printed ring already gives a longest order. All that is left to do is confirm that nothing beats 7.
- The same ring also gives away Problem 2. (0,1,2,4) is one of the 7-move maxima for both the 0–4 and the 0–5 ranges. It is printed on K–1 page 5 and twice on Grades 2–3 page 5 (P5 and P6).
- Smallest fix: replace the printed (0,1,2,4) in K–1 P6 and 2–3 P5 with a 4-move order such as (0,2,1,4), keeping (0,1,4,2). Children then have to find the 7-move order themselves; a third of all orders are 7-move ones, so it can be found. In the guide key, add "(0,2,1,4) lasts 4". Optionally, give 2–3 P6 the witness (0,1,2,3) → (1,1,1,3) (maximum stays 3; 5 moves to zero) in place of (0,1,2,4), and update the guide's "Equality can persist" example to match.

### 2. The old and new working mats touch: a 1.0 mm gap on pages 2 and 4 of every band (could)

- Where: K–1 pages 2 and 4 (P2, P5), and Grades 2–3 and 4–5 pages 2 and 4 (P2, P4).
- Evidence (`check_base.out`, "Guide: mat sizes"): the clear gap between the old mat's right-hand squares (four-station B; three-station B) and the new mat's left-hand squares (A; C) is 1.00 mm in all six places. The eight squares read as one grid, "A B A B / D C D C". Only the small "old" and "new" headings, and the arrows staying inside each mat, separate them. The page-1 example, by contrast, separates old and new by about 27 mm with an arrow.
- Why it matters: the rule depends on keeping one old ring untouched while building the new one. This is a layout point, not a wrong diagram; it is untested physically.
- Smallest fix: make the stations 36 mm, keep the centres 52 mm apart and move each mat 2 mm outward. This uses the full 0–185 mm frame and leaves a 9 mm gap. Add a vertical rule or the page-1 old→new arrow between the mats. Change the guide's "40 mm square stations" to match.

### 3. K–1 P3 does not say "first", but the key excludes (0,0,0,0) (could)

- Where: K–1 page 3, Problem 3, "Find different starts that become all zeros in one move." Problem 4 on the same page does say "first become all zeros on the second move". The guide says "Do not count (0,0,0,0), which takes zero moves."
- Evidence: D(0,0,0,0) = (0,0,0,0), so under the literal wording the all-zero ring is all zeros after one move. The convention that it takes 0 moves is only printed on page 2. An adult following the key may reject a defensible answer.
- Smallest fix: "Find different starts that first become all zeros on the first move," to match P4.

### 4. Bonus P3: the answer depends on counting round 5 (could)

- Where: bonus page 3, Problem 3, "Which start gets an entry more than 10 away from 0 within five rounds?"
- Evidence (`check_bonus.out`): (0,1,0,1) is 8 from 0 at round 4 and 16 at round 5. (0,0,1,1) passes 10 only at round 9. The intended answer, the first start, therefore needs round 5 included. A child who fills five rows of the table (rows 0–4) finds that neither start passes 10.
- Smallest fix: "…more than 10 away from 0 by round 5?" This matches the table's row numbers 0–7.

### Note (not an error): Grades 4–5 page 1 example equals P6's first start

The page-1 worked example (1,4,2,0) → (3,2,2,1) is the same ring as the first start of Grades 4–5 Problem 6, and the guide's launch also uses it. P6's first move is therefore printed on page 1. This does not affect P6's question, which is about doubling. If a non-task example is wanted, change P6's pair, for example to (2,5,1,0) (6 moves) and (4,10,2,0), and update the guide's P6 chains.

## Files

- `common.py`: repository discovery (four folders up from `plans/review/checks/week-49/`, falling back to a walk upward), PDF readers and the gap maps.
- `pdf_extract.py` → `pdf_geometry.json`, `pdf_extract.out`
- `check_base.py` → `check_base.out`. Its 2 FAIL lines are problem 1; the EDGE line is problem 3.
- `check_bonus.py` → `check_bonus.out`. The EDGE line is problem 4.
