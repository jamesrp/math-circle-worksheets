# Week 8 (rook race and Nim): math check

Scope:
- Student packets in `lowell-math-circle-year-2/week-08/`: `week-08-k-1.pdf` (F08-K-v4, 7 pp., Problems 1–8), `week-08-grades-2-3.pdf` (F08-M-v4, 5 pp., Problems 1–9) and `week-08-grades-4-5.pdf` (F08-U-v4, 7 pp., Problems 1–9).
- Adult guide: `week-08-facilitator.pdf` (F08-FAC-v4, 9 pp.).
- Return-visit companion in the same folder: `week-08-return-visit.pdf` (F08-RV-v1, 5 landscape pp., Problems 1–3) and `week-08-return-visit-facilitator.pdf` (RV8-FAC-v1, 5 pp.).
- Sources: `source/week-08/src/` (`build.py`, `tikzlib.py`, the generated `.tex`), `source/week-08/guide-src/facilitator.tex` with `figs/`, and `source/week-08-return-visit/` (`student/return-visit.tex`, `facilitator.tex`).

I did not use the packet's own checks (`src/check.py`, `guide-src/check.py`, or the return visit's `verify.py`, `student/check_math.py` and `student/check_pdf.py`). I ignored the archive folders and opened no session records. My scripts and their outputs are in [checks/week-08/](checks/week-08/). Checked October 10, 2026.

**Result: every answer in all three bands and in the return visit is correct, and every problem can be done as stated. Every board, dot, arrow and pile in the student PDFs matches its text. The adult guide's answers, hints, overview, launch and materials arithmetic are correct. There are three small problems (items 1–3): one answer picture shows 15 red squares beside the text "14 red squares", one return-visit guide sentence has a wrong half, and one materials line misstates a square size. None changes an answer.**

## How it was checked

- **`pdfdraw.py`** is a small standard-library PDF reader of my own. It handles compressed object streams, walks the page tree and interprets the path operators under the transformation matrix. It returns every painted path in inches, with fill and stroke colours. PyMuPDF is not installed here.
- **`extract_pdf.py`** (outputs `extract_pdf.out` and `pdf_geometry.json`) reads the three student PDFs back. For every board it records:
  - the number of squares;
  - the square size in both directions (all uniform, all square);
  - the star's square, always bottom left;
  - every token dot as (right, up) from the star, each centred in its square;
  - every arrow as start square → tip square.

  It also counts every counter tower on its base line, records the "1st/2nd" boxes, and assigns each item to its "Problem N:" heading using `pdftotext -bbox`.
- **`games.py`** contains my own solvers, which search the game tree directly. They use no xor, no diagonal rule and no Wythoff pairs. It covers the rook race, the queen game, Nim with any number of piles (normal and last-counter-loses), the two-board race, the coin row and "take 1, 2 or 3".
- **`check_answers.py`** (output `check_answers.out`) solves every student problem from the data read out of the PDFs. The 4–5 starts printed as text come from `pdftotext`. It compares each result with the page and with the guide's answers, which I transcribed by hand. Before using any guide sentence, it confirms the sentence is in the delivered guide. It also tests:
  - the guide's proof steps, strategies and overview claims;
  - the launch;
  - the fallbacks;
  - the materials arithmetic;
  - every answer picture's source in `guide-src/figs/`.

  Result: 80 OK, 0 mismatches. Its 3 NOTE lines are items 1 and 3, plus one consistent observation about 4–5 P9.
- **`guide_figs_pdf.py`** (output `guide_figs_pdf.out`) reads all 18 answer pictures out of the delivered guide PDF: grid, star, start dot, shaded squares and arrow. It checks each against the search. Result: 18 OK, and one NOTE (item 1).
- **`return_visit.py`** (output `return_visit.out`) reads the return-visit PDF: the counters in every pile card, every 12-square coin row with its wall and coins, and every rook board with its star, token and A/B label. It then solves and compares with that guide. Result: 28 OK, 0 mismatches, and one NOTE (item 2).
- **`source_vs_pdf.py`** (output `source_vs_pdf.out`) confirms three things: the delivered PDFs carry the opening rules and all 26 problem statements from the `.tex` sources, `src/*.tex` is exactly what `src/build.py` generates now, and the return-visit statements are in its PDF. Result: 42 OK.
- **Run order:** `extract_pdf.py` first, because `check_answers.py` reads `pdf_geometry.json`. The other scripts are independent. No LaTeX is installed here, so I could not test a clean rebuild. The text and geometry comparisons stand in for it.

## K–1: checks out completely

- **Rules picture:** the token is on (2, 3) of a 4-by-4 board, with arrows to (0, 3) and (2, 0). Both are legal moves.
- **P1** (3-by-3, 1-inch squares): from (2, 2), 2nd. From (1, 2), 1st, and the only winning move is down 1 to (1, 1).
- **P2** (4-by-4, 1-inch squares): (3, 3) 2nd; (3, 0) 1st, onto the star; (2, 2) 2nd; (1, 3) 1st, only down 2 to (1, 1).
- **P3** (5-by-5): each board has exactly one winning move. From (0, 3) it is the star itself, from (3, 1) it is (1, 1), from (2, 4) it is (2, 2), and from (4, 3) it is (3, 3).
- **P4** (6-by-6): the squares to move to are the diagonal (0, 0) to (5, 5), six squares including the star.
- **P5:** the drawn piles are 3/3, 4/1, 2/2 and 5/3.
  - 3/3: 2nd.
  - 4/1: 1st, and the only winning move leaves 1/1.
  - 2/2: 2nd.
  - 5/3: 1st, and the only winning move leaves 3/3.
- **P6:** 7 and 7 (14 counters drawn) is 2nd, by copying.
- **P7:** the picture shows a dot on (7, 7) of an 8-by-8, which is 2nd. The copy reply is always legal and always returns to the diagonal.
- **P8:**
  - 1, 1, 1: 1st, by taking any pile.
  - 1, 1, 2: 1st, and the only winning move is taking the 2.
  - 1, 2, 3: 2nd.
  - 2, 2, 3: 1st, by taking the 3 or taking 1 from either 2.
- The 14 pairs of 1st/2nd boxes match the 14 starts in P1, P2, P5 and P8.

## Grades 2–3: checks out completely

- **P1** (5-by-5): (4, 4) 2nd; (4, 2) 1st, only to (2, 2); (3, 3) 2nd; (1, 4) 1st, only to (1, 1).
- **P2:** red is the 7 diagonal squares and the other 56 are green.
- **P3:** the dot is on (7, 7), which is 2nd.
- **P4:** each drawn count matches its label.
  - 4/4: 2nd.
  - 6/2: 1st, only to 2/2.
  - 5/3: 1st, only to 3/3.
  - 7/7: 2nd.
- **P5:** the dot is on (5, 2), so the piles are 5 and 2. From every square of an 8-by-8, the board moves are exactly the two-pile moves.
- **P6:** 52 and 37 is 1st, and the only winning move is taking 15 from the 52.
- **P7:**
  - 1, 1, 1; 1, 1, 2; and 2, 2, 3: 1st.
  - 1, 2, 3: 2nd. The guide's six-reply table covers all six moves from 1, 2, 3, and every reply leaves two equal piles.
- **P8:** of the 10 starts, only 1, 2, 3 is 2nd.
- **P9:** of the 56 starts, 20 have three different piles. The 2nd starts are 1, 2, 3; 1, 4, 5; 2, 4, 6; and 3, 5, 6. Every start with a repeated pile (piles 1–30) is 1st, as the guide's crossing-out argument says.

## Grades 4–5: checks out completely

- **P1:** the same as 2–3 P2.
- **P2:**
  - The dot is on (6, 3), so the piles are 6 and 3.
  - 23 and 17: first, and the only winning move is taking 6 from the 23.
  - 30 and 30: second.
- **P3:**
  - 1, 1, 1: first.
  - 1, 1, 2: first.
  - 1, 2, 3: second.
  - 2, 2, 5: first, and the only winning move is taking the 5.
  - 1, 3, 4: first, and the only winning move is taking 2 from the 4.
  - 1, 4, 5: second.
- **P4:** of the 84 starts, 7 are second-player: 1, 2, 3; 1, 4, 5; 1, 6, 7; 2, 4, 6; 2, 5, 7; 3, 4, 7; and 3, 5, 6.
- **P5:** all five printed "second player" starts are second-player wins, and all four "first player" starts are first-player wins. Each pile splits into stacks in only one way. The rule "every stack size an even number of times" agrees with the search for every 3-pile start with piles 0–31 and every 4-pile start with piles 0–9.
- **P6:**
  - 3, 5, 7: first. There are exactly three winning moves: take 1 from any pile.
  - 6, 10, 12: second.
  - 13, 9, 7: first, and the only winning move is taking 3 from the 7.
  - 11, 14, 21: first, and the only winning move is taking 16 from the 21.
- **P7:** I tested both steps of the guide's proof.
  - Step (a): every move from a balanced start (piles 0–31) unbalances it.
  - Step (b): the guide rebuilds the pile that has the biggest odd stack, switching every odd size. For every unbalanced start with piles 0–63, this is a legal move to a balanced start.
- **P8:** the picture's three arrows from (3, 4) end at (0, 4), (3, 0) and (0, 1), all legal queen moves. Red is (1, 2), (2, 1), (3, 5), (5, 3), (4, 7) and (7, 4), and the other 57 squares are green.
- **P9:**
  - There are 14 red squares: (1, 2), (3, 5), (4, 7), (6, 10), (8, 13), (9, 15), (11, 18) and their mirror images. The next pair, (12, 20), is off the board.
  - Rows 12, 14, 16, 17 and 19 have no red square on the board. This is consistent with the guide's row-by-row argument, which reproduces exactly these 14 when row 0's red square is taken to be the star.

## Adult guide

Every problem answer and every hint is correct. I checked all "only move" and "exactly one" claims. The following are also correct:

- **"How to win" list:** all three piles strategies, and the queen list up to (12, 20) with differences 1, 2, 3, ….
- **Launch:** from (1, 3) the moves are one left, or one, two or three down.
- **Fallbacks:** in "take 1, 2 or 3", leave multiples of 4, and from 20 you would rather go second. The worded last-counter-loses strategy wins from every last-counter-loses start that is a first-player win: three piles 0–12 and four piles 0–6.
- **Materials arithmetic:** tokens 8 + 1 + 3 = 12. Problem 6 needs 46 counters. There are 7 8-by-8 boards and 3 5-by-5 boards, and an 8-inch board leaves ¼ inch margins on Letter.
- **Section 5 overview:**
  - P- and N-positions.
  - Rook race = two-pile Nim.
  - Bouton's proof, valid for any number of piles.
  - Wythoff's pairs and the closed form ⌊nφ⌋, ⌊nφ²⌋, checked on a 60-by-60.
  - Beatty's theorem, with the two sequences covering 1–60 once each.
  - The last-counter-loses rule.
  - Subtraction games.
  - Moore's Nim₂ rule, checked on four piles 0–7.

All 18 answer pictures in the delivered PDF show the right start, the right shaded squares and the right arrow. The one exception is item 1. Section 1 states the main facts in words before the tables; the theorems and proofs are in Section 5, after the solutions.

## Return visit: checks out; one guide sentence (item 2)

- **P1 (last counter loses):** the drawn counters match the printed numbers. The winners of Starts 1–12 are second, first, first, second, first, second, first, second, first, first, second, first. The guide's first moves all win, including 2, 3, 4 → 2, 3, 1.

  Both the guide's two-pile rule and its general rule match the search. The general rule says that odd singletons lose, and otherwise xor 0 loses when some pile exceeds 1; this holds for 1–4 piles. The guide's one-large-pile strategy also holds: reduce the large pile to one when the singletons are even, and remove it when they are odd.
- **P2 (coin row):** every row has 12 squares and a thick wall. The coins sit as the guide lists them, and the worked example (4 → 2, with 10 fixed) is legal. Starts 1–6 and 7–14 alternate second, first, as the guide says, and the gap pairs (a, b) are right.

  The paired-gap xor rule matches the search for 1–4 coins on 12 squares. Starts 1 (1, 2) and 7 (1, 2, 3) have no legal move at all, so the first player loses at once. The printed rule "A player with no move loses" covers this, and the guide's answer, second, is right.
- **P3 (two rook boards):** the worked turns (2, 2) → (0, 2) and (1, 3) → (1, 1) are single legal moves. The pairs match the guide's coordinates, and the winners are second, second, second, first, second, first. The guide's (0, 3; 1, 2) does cancel.

  The four-pile xor law matches the search on all boards up to 4. Two diagonal starts together lose, identical starts lose, and the "same totals" example is right. Starts 3 and 5 already meet the invention task, which is why it says "another". On 4-by-4 boards, 18 unordered pairs of different off-diagonal starts cancel.
- **Materials:** 12 × 0.85 = 10.2 inches, the boards are 3.4 inches, and four 0.65-inch counters fit in 2.9 inches. The largest printed pile has 4 counters. The play boards measure 0.85 inches per square.

## Problems found

### 1. The 20-by-20 answer picture shows 15 red squares beside "14 red squares" (guide p. 8, 4–5 Problem 9)

- **Quoted text:** "14 red squares: (1, 2), (3, 5), (4, 7), (6, 10), (8, 13), (9, 15), (11, 18) and their mirror images." The legend on p. 3 reads "red = the square to move to, or the squares where you would rather go second."
- **Evidence:** `guide_figs_pdf.out` reads 15 shaded squares in the delivered picture: the 14 listed plus the corner square (0, 0). Unlike every other answer board, this picture draws no star (`figs/queen20.tex` fills (0, 0) and has no star node). So the corner looks like a fifteenth red square.

  Problem 8, which defines the colouring, says "Color every square ... except the star". An adult comparing a child's 14 marks with the picture would look for a missing one, or ask the child to mark the corner. The 8-by-8 answer pictures (p. 5, 2–3 Problem 2; p. 7, 4–5 Problem 8) also shade the star's square while their text says 7 and 6 red squares, but they draw the star on it, so they read correctly.
- **Smallest fix:** draw the star in the corner of the 20-by-20 picture, as in the 8-by-8 queen picture. Alternatively, leave (0, 0) unshaded in all three no-start pictures.

### 2. Return-visit guide: "its size determines" which singletons to leave (return-visit guide p. 3, Problem 1, "General rule")

- **Quoted text:** "If only one large pile remains, its size determines which final singletons to leave: reduce it to one when the existing singleton count is even, or remove it when that count is odd."
- **Evidence:** the choice depends only on the parity of the singleton count, as the rest of the sentence says, and never on the size of the large pile. For example, 1, 1, 2 and 1, 1, 9 are both won by reducing the big pile to one. `return_visit.out` confirms the stated rule wins for every 4-pile position (piles 0–9) with exactly one pile above 1.
- **Smallest fix:** "If only one large pile remains, the number of singletons decides what to leave: reduce the large pile to one when that number is even, or remove it when it is odd."

### 3. Materials: page 5 of the K–1 packet does not have 1-inch squares (guide p. 1, "What to print")

- **Quoted text:** "The boards on pages 1–3 and 5 have 1-inch squares".
- **Evidence:** `extract_pdf.out` measures 1.000 inches on pages 1–3, but 1.050 inches on page 5 (K–1 Problem 4, a 6-by-6). This is harmless for play. The guide's printing test, "Measure a square on each printed sheet: 1 inch. If smaller, the printer scaled the page", still works, because the page 5 squares are larger.
- **Smallest fix:** "The boards on pages 1–3 have 1-inch squares, and page 5 slightly larger ones".

## Not checked

- The archived versions.
- Physical fit of the real tokens and counters, and printer scaling of the 8-inch separate boards.
- A clean rebuild, because no LaTeX is installed here. The source-to-PDF text check and the geometry read-back stand in for it.
