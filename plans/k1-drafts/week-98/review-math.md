# Week 98 K–1 draft: mathematical review

Reviewed: `draft/k-1.pdf` (9 pages; identical to `draft/src/k-1.pdf`). I parsed the board, counter and dot coordinates from `draft/src/k-1.tex` itself, not from `gen.py` or `check.py`, and checked every claim by exhaustive enumeration. The script is `review-math-check.py` in this run folder; run it as `python3 -I review-math-check.py draft/src/k-1.tex`. A 300 dpi render of page 2 measures the working-board squares at 29.97 to 30.01 mm. No LaTeX overfull warnings appear, and no diagram overflows the page.

## What checks out

These parts are correct as printed, using the rule as the brief means it (a square needs at least two filled side neighbours):

- **P1 (2-by-2, every placement of 2 seeds).** There are 6 placements. The two diagonal pairs fill. The four side-by-side pairs are stuck and never grow.
- **P2 to P4 (fewest seeds).** 3-by-3 needs 3 (14 of 84 three-seed starts fill). 4-by-4 needs 4 (130 of 1820). 5-by-5 needs 5: none of the 12,650 four-seed starts fills, and 1615 of 53,130 five-seed starts do.
- **P5 (strips).** 1-by-3 needs 2 (only the two ends). 1-by-4 needs 3 (squares 1,2,4 or 1,3,4). 1-by-5 needs 3 (only 1,3,5). 1-by-6 needs 4 (1,2,4,6 or 1,3,4,6 or 1,3,5,6).
- **P6 (two-wide boards).** The boards are drawn 3, 4 and 5 rows by 2 columns. They need 3 seeds (10 of 20 starts fill), 3 seeds (8 of 56) and 4 seeds (48 of 210).
- **P7 (four printed starts).** Board A (top-left L) grows by one square, to the 2-by-2 block of 4. Board B (middle row) is already stuck. Board C, with (1,1), (1,3), (2,1), grows to the top two rows (6). Board D, the left column plus (1,3), fills the board (2 complete growth orders, one finish). On board B, all six other squares touch two counters if corner touches are counted, so it catches the diagonal mistake as intended.
- **P8, intended reading (each seed taken off alone).** Board 1 (2-by-2 L): only the corner of the L, (1,1), can come off. Board 2 (four corners): all four can come off. Board 3, with (1,1), (1,3), (2,2), (3,1): (1,1) and (2,2) can come off, and taking off (1,3) or (3,1) leaves 6 filled. Board 4 (middle of each side): none can come off, since every single removal finishes with 6 filled.
- **P9 (top row plus left column).** Only (1,1), (1,2) and (2,1) can come off first. Every route of removals ends in one of exactly two sets:
  - **4 seeds:** (1,2), (1,3), (2,1), (3,1). One route reaches it: take off (1,1) first. Its single removals finish with 3, 6, 3 and 6 filled.
  - **3 seeds:** the three corners (1,1), (1,3), (3,1). Two routes reach it: take off (1,2) and then (2,1), or (2,1) and then (1,2).

  So the answer to "Can you end with a different number?" is yes: 3 and 4. A 3-by-3 filling start in which every seed is needed has 3 seeds (14 starts) or 4 seeds (9 starts), never more.
- **Page 1 rule pictures.** The check-mark patch is legal: the target has two filled side neighbours. The cross patch is illegal: the target has none.
- **Counters (26 per pair: 6 seed colour, 20 growth colour).** Each board can be done on its own. The biggest need is P4: 5 seeds and 20 growth counters fill the 5-by-5 exactly.

## Located problems

### 1. P8 can be read as cumulative removal, which changes the answers on two boards
- **Where:** K–1, page 8, Problem 8.
- **Text:** "Put seeds on the dots. Ring each seed you can take off while the others still fill the board."
- **Evidence:** The page never says to put a seed back before testing the next one. A child who takes a seed off, sees the board fill, and leaves that seed off rings exactly one seed on boards 1 to 3, in every one of the 24 testing orders, and none on board 4. The intended single-removal answers are 1, 4, 2 and 0. Read cumulatively, Problem 8 also becomes the same task as Problem 9. That removes the contrast the pair is built on: a seed can be removable on its own without a set of seeds being removable together (four corners: any one can go, but no two).
- **Smallest fix:** Make single removal explicit, for example: "Put seeds on the dots. Take off one seed, grow, then put it back. Ring each seed the board can do without." Another option is to add one sentence: "Put each seed back before you try the next one."

### 2. The rule says "two" neighbours, not "two or more"; the literal reading breaks P8 and some P6 starts
- **Where:** K–1, page 1, the shared rules. The effect shows on pages 6 and 8.
- **Text:** "A square gets a counter when two squares next to it, not corner to corner, have counters." The brief's rule says "at least two".
- **Evidence:** A literal K–1 listener, or a non-mathematician parent, may refuse a square that has three or four filled neighbours ("it has four, not two"). Under that "exactly two" reading:
  - **P8 boards 2, 3 and 4 never fill**, so the premise "the others still fill the board" is false before anything is taken off. The middle-edge board stops at 8, because the centre has four filled neighbours from the start. The four-corners board stops at 7 or 8, depending on order. Three corners plus the centre stops at 7.
  - **P6:** 2 of the 10 fewest-seed starts for the 3-by-2 board can stick. These are (1,1), (2,2), (3,1) and its mirror image, where the middle of the outer column gets three neighbours. On the 5-by-2 board, 12 of the 48 four-seed fillers can stick.
  - **Order-dependent finish:** the four-corners board can stop at different finishes, which contradicts the fact that the finish depends only on the seeds.

  P1 to P5, P7, P9, and the fewest-seed starts on 3-by-3 and 4-by-4 are unaffected.
- **Smallest fix:** "A square gets a counter when two or more squares next to it, not corner to corner, have counters." The partner can still point to any two of them.

### 3. The page-1 rule picture shows the answer to Problem 1
- **Where:** K–1, page 1, the check-mark rule picture above Problem 1.
- **Diagram:** A 3-by-3 patch with counters at (1,2) and (2,1), the dashed target at (2,2), and a check mark.
- **Evidence:** The top-left 2-by-2 corner of this patch is exactly P1's board holding a diagonal pair. The picture shows one empty square being added, and the other empty square, (1,1), is legal by the same pair. So the rule picture works one of the two fill answers to P1. It also gives away the key fact in P8 board 1: the L can lose its corner because the diagonal pair fills. The brief says "no worked example on them may be the answer to a K–1 task."
- **Smallest fix:** Show a legal addition between two opposite neighbours: counters at (1,2) and (3,2), dashed target at (2,2), check mark. On 3-by-3 that start stops at the middle column, which answers no K–1 task. Optionally, change the cross example to one side neighbour plus one corner, such as counters at (1,2) and (3,3) with target (2,2), so that it shows the likeliest K–1 mistake. The current cross, with two corners and no side neighbours, is correct as it stands.

### 4. P1 prints 8 record boards for a find-every-way task with 6 answers
- **Where:** K–1, page 1, Problem 1.
- **Text and diagram:** "Find every way to put 2 seeds on this board. Draw each way with dots, and ring the ways that fill." It is followed by eight blank 2-by-2 record boards.
- **Evidence:** There are C(4,2) = 6 placements, or 2 if turned copies count as the same. Young children read the number of boxes as the number of answers. A child who has all 6 will keep looking for two more, or draw repeats. A complete list is the point of the problem, so the box count should not suggest a wrong total.
- **Smallest fix:** Print 6 record boards (two rows of three, as on page 2).

### 5. P4's "find out" promises a check K–1 children cannot make
- **Where:** K–1, page 4, Problem 4.
- **Text:** "Guess how few seeds can fill this board. Then find out, and draw the seeds."
- **Evidence:** Children can find out that 5 seeds suffice. They cannot find out by experiment that 4 never fill: there are 12,650 four-seed starts, and the reason is the fence count, which the brief keeps as adult background. Problems 2 and 3 use the honest "as few seeds as you can". A child who guesses 4 and fails a few times has not found out anything definite.
- **Smallest fix:** "Guess how few seeds can fill this board. Then fill it with as few seeds as you can, and draw the seeds."

### 6. P9 prints three record boards, but there are only two possible endings
- **Where:** K–1, page 9, Problem 9.
- **Evidence:** All three removal routes end in one of two sets: the three corners, or (1,2), (1,3), (2,1), (3,1). This is a minor version of item 4: the third box may suggest a third ending. A third box does give room to record a mistaken run, and children who look for an ending with 2 seeds will find there is none.
- **Smallest fix:** Print two record boards, or keep three only if the adults know the answer is exactly two endings.

### 7. P8's four boards need 15 seed-colour counters at once; a pair has 6
- **Where:** K–1, page 8, Problem 8.
- **Text:** "Put seeds on the dots." Below it are four boards with 3, 4, 4 and 4 dots.
- **Evidence:** A pair given the brief's 6 seed-colour counters cannot carry out the instruction on the whole page at once. Board by board it works: at most 4 seeds and 5 growth counters. P9's 5 seeds also fit.
- **Smallest fix:** No change to the mathematics is needed. Either the adult does the boards one at a time, or the page says "Put seeds on the dots of one board" (or similar), or the K–1 table gets 15 or more seed-colour counters per pair.
