# Week 6 (code breaking): math check

Scope: `lowell-math-circle-year-2/week-06/week-06-k-1.pdf` (F06-K-v4, 7 pp., Problems 1–9), `week-06-grades-2-3.pdf` (F06-M-v4, 10 pp., Problems 1–11), `week-06-grades-4-5.pdf` (F06-U-v4, 9 pp., Problems 1–10) and `week-06-facilitator.pdf` (F06-FAC-v4, 10 pp.). I also checked the return-visit companion in the same folder: `week-06-return-visit.pdf` (F06-RV-v1, 3 pp., Problems 1–3) and `week-06-return-visit-facilitator.pdf` (RV6-FAC-v1, 5 pp.). Sources: `source/week-06/src/`, `source/week-06/guide-src/facilitator.tex` and `source/week-06-return-visit/`. I did not use the packet's own check scripts (`check_codes.py`, `check_puzzles.py`, `check_guide.py`, `verify.py`, `check_answers.py`). Archive folders were ignored, and I opened no use logs or session records. My scripts and their outputs are in [checks/week-06/](checks/week-06/). Checked October 5, 2026.

**Result: every answer in all three student bands and the return visit is correct, and every problem can be done as stated. All diagrams match their text. The adult guide has six small problems (items 1–6). One is a materials count, and another could lead an adult to correct a right 4-test method. None changes the answer to a printed problem.**

## How it was checked

- `codegame.py` is my own solver. It searches the code game exhaustively, with no formulas from the guide:
  - the fewest tests that always identify the secret, with later tests allowed to depend on earlier scores, for 2–5 counters;
  - the fewest tests that always end on a full score;
  - the smallest set of tests fixed in advance;
  - the secrets that fit a finished game.

  It also solves the yes-or-no games by searching over all question splits, and the return-visit weighing, message-plan and code-book tasks. For the code books it uses Sardinas–Patterson and a search of all messages up to length 8.
- `extract_pdf.py` (output `extract_pdf.out`, `pdf_data.json`) reads the delivered PDFs back with `pdftotext -bbox` and `pdftocairo -svg`. It finds:
  - **Code boards.** All 7 boards. On each:
    - the secret row is thick and the copy row thin;
    - every slot is a circle 1.04 in across;
    - there is one equilateral triangle outline, 1.000 in on a side, under each column;
    - every test row has a 1.00 in score box;
    - all rows line up column by column.
  - **Trays and record tables.** K–1 has 6 two-slot trays on p3 and 10 three-slot trays on p6. Every record-table count matches its source.
  - **Block drawings.** All 32, on four pages:
    - the triangle and hexagon are regular, with the same scale in x and y;
    - the rhombus and trapezoid have 60°/120° angles;
    - the chevron is a concave six-sided piece with the area of two blue rhombi;
    - the kite has 4 sides and is convex; the dart has 4 sides and is concave.
  - **Puzzle records.** Every drawn test and score in K–1 P7, 2–3 P7 and 4–5 P3, and the fill colour behind each letter. Red counters and pink cells carry R; yellow ones carry Y.
- `check_answers.py` (output `check_answers.out`) solves every problem from the data read out of the PDFs. It then runs about 140 checks of the pages, the guide and the return visit against the solver. Before checking any guide sentence, it confirms that the sentence is in the delivered PDF. There are 0 mismatches. Its 6 NOTE lines are items 1–6 below.
- `source_vs_pdf.py` (output `source_vs_pdf.out`) confirms that the delivered PDFs carry the sources I read:
  - all 30 problem statements and the 4–5 opening rules, word for word;
  - all 15 puzzle records, matching the drawn ones;
  - all 256 plain sentences of the guide source;
  - all 6 return-visit text paragraphs.

  3 of the 138 sentences in the return-visit guide do not match. All three are line-break hyphenation in the PDF ("threeobject", "optimalcoding") or a `\{A,B\}` escape in the source. XeLaTeX and pdfLaTeX are not installed here, so I could not test a clean rebuild.
- Every page of all six PDFs was rendered (pdftoppm, 80 dpi) and looked at.

## Facts the packet rests on (all confirmed)

- **Code game.** The fewest tests that always identify the secret are 2, 3 and 4 for 2, 3 and 4 counters. With 5 counters, 3 tests are not enough and 4 are. To be sure of a test that scores full marks takes 3, 4 and 5 tests.
- **Second method for the lower bounds.** A separate plain-loop search confirms the three lower bounds the pages ask children to explain: 1 test for 2 counters, 2 for 3, and 3 for 4.
- **Fixed tests.** RRR, YRR, RYR give all 8 secrets different scores. RRRR, YRRR, RYRR, RRYR give all 16 different scores. The guide's five-counter set RRRRR, RRRYY, RRYRY, RYRRY gives all 32 different scores, and 4 is the fewest fixed tests for five counters.
- **Yes-or-no questions.** 2 questions find one of 4 things, 3 one of 8, 4 one of 16, 5 one of 20 and 7 one of 100. "Is it this one?" questions alone need 7 for 8 blocks.
- **Two questions for eight blocks.** I tried every adaptive two-question plan, with all 256 subsets allowed at each question. Every one leaves two blocks together.

## K–1: checks out completely

- **P1:** yes. "Does it have four sides?" splits the four blocks 2/2 (rhombus and trapezoid against triangle and hexagon).
- **P2:** 7.
- **P3:** yes. The guide's plan (top row?, four sides?, then point) ends at one block for all 8 as drawn.
- **P4:** no.
- **P5:** 4 secrets; 6 trays are printed.
- **P6:** one test is never enough, because every test has exactly two secrets that score 1. Two tests always are: RR first, and after a score of 1 the only second tests that work are RY and YR.
- **P7:** RR; YR; RY and YR; RY; YY. No row needs more than its two trays.
- **P8:** 8 secrets (1, 3, 3, 1 by number of reds); 10 trays are printed.
- **P9:** yes. RRR, YRR, RYR works: a score that goes up one means yellow, down one means red.

## Grades 2–3: checks out completely

- **P1:** good questions take 3; naming one block at a time, at most 7.
- **P2:** three questions exist. The guide's fixed questions give the drawn blocks 8 different answer patterns, exactly as listed.
- **P3:** no.
- **P4, P5:** one test is never enough; two always are. The fixed pair RR, RY gives (2,1), (1,2), (1,0), (0,1).
- **P6:** 3.
- **P7:** the five games:
  - RRY, RYR, YRR;
  - YRR, YYY;
  - RRY (each row alone leaves 3 secrets and each pair leaves 2, so all three rows are needed);
  - RRR;
  - none.
- **P8:** RRR, YRR, RYR. The guide's score table is correct in all 24 entries.
- **P9:** yes, by the fourth test. Ending by the third cannot be promised.
- **P10, P11:** 4 tests, and 3 never always work.

## Grades 4–5: checks out completely

- **P1:** 4 for 1–16 (8 patterns < 16) and 5 for 1–20 (16 < 20). The chain 20, 10, 5, 3, 2, 1 is right.
- **P2, P4:** 3 tests.
- **P3:** the five games:
  - RRR;
  - RRY, RYR;
  - RYYY;
  - RRRR and YYYY;
  - none.

  In game 5 all three tests have an even number of Y, so all three scores must have the same parity, and 1, 3, 2 do not. The child's reason (changing two counters moves a score by 0 or 2) holds for every pair of rows.
- **P5, P6:** 4 tests. Each later score of the guide's method is one more or one less than the first.
- **P7:** the score never changes. Checked for every pair of rows of length 1–5 and every place.
- **P8:** both impossibilities hold. Turning over one counter of a row always changes its score on any test by exactly 1.
- **P9:** no. The guide's formula s − 2 + 2|Q∩D| holds for all 16 first tests and all 16 later tests. So do its splits (6; 3+3; 1+4+1; 3+3; 6), "never two, two and two", and the claim that every group of three or more keeps two secrets together under any third test.
- **P10:** 4 and 5. Checked by search, and the guide's reduction (ending by test k means knowing after k − 1) holds for 2–4 counters.

## Return visit: checks out completely

- **P1:** 2 weighings. I searched over actual card sets with equal pans; one weighing cannot do it. The guide's plan, 123 | 456 and then one card on each pan, finds all 9.
- **P2:** 14 questions in all for the batch. Every optimal plan has depths A 1, B 2, C 3, D 3, so the answer to "most questions for one message" is 3 whichever optimal plan a child finds. The balanced plan costs 16.
- **P3:** only Book 1 is ambiguous (B and AC both give RY). Books 2 and 3 are uniquely decodable.

All of the return-visit guide's statements check out, as do the printed M = YR, N = R example and the 3.05 × 1.35 in pans. One remark is more cautious than it needs to be: "an equal-pan constraint may forbid a desired split." With only one heavy card, equal pans never force more than the fewest possible weighings (the smallest k with 3^k ≥ N); I checked every N from 1 to 30. That is not an error.

## Adult guide

Everything else in the guide is correct and matches the pages:

- every answer and hint for all 30 problems;
- the "Problem N page P" references;
- the board-page list, the counts of counters, triangles, folders, pencils and whiteboards, the copy counts;
- the attention-span games;
- the sharing question;
- the section-5 statements, including the five-counter set and the parity rule.

The problems are below. I list them from the most to the least likely to cause trouble in the room.

### 1. The launch has too few counters for its own script (p. 2)

- **Quoted text:** "At the front: a cut two-counter board (an extra copy of 2–3 p. 3), one folder, 6 counters, 2 green triangles." Then steps 2–5: a child fills the first test row; "I copy your test under my secret"; "Take the copy and the triangles away. A second child makes the next test; score it the same way"; and at the end "Re-copy each test".
- **Evidence:** to score the second test you need four rows at once: the secret (2 counters), the first test row (2, kept because step 5 re-checks it), the second test row (2) and the copy of the second test (2). That is 8 counters. With 6, the organizer runs out in the middle of the second scoring, in front of the whole group.
- **Smallest fix:** "8 counters" (or "10 counters, a full two-counter board").

### 2. 2–3 Problem 11: a natural 4-test method is said to take 5 (p. 7)

- **Quoted text:** "RRRR, YRRR, RYRR, RRYR; the fourth counter from the number of reds: at most 4 tests. Testing every place separately without the count takes 5."
- **Evidence:** testing every place separately also works in 4 tests if the all-red test is left out. Take YRRR, RYRR, RRYR, RRRY:
  - Each one scores (reds in the secret) + 1 where the secret is yellow, and − 1 where it is red. So the higher scores mark the yellow places.
  - If all four scores are equal, the secret is RRRR (all 3s) or YYYY (all 1s).
  - All 16 secrets get different scores (`check_answers.out`). For example, RYRY gives 1, 3, 1, 3.

  A child at 2–3 or 4–5 can easily find this "turn each place yellow" method. The sentence would lead an adult to say it needs a fifth test.
- **Smallest fix:** "All red and then each of the four places takes 5. Using the count, or leaving out the all-red test (YRRR, RYRR, RRYR, RRRY: the higher scores are the yellow places; all 3s mean RRRR, all 1s mean YYYY), takes 4."

### 3. Overview: a wrong score does not always make a game impossible (p. 1)

- **Quoted text:** "One wrong score makes a game impossible to solve, so scoring is done with objects and every score is checked at the end."
- **Evidence:** in play the breaker stops as soon as one secret fits. So a wrong score can leave exactly one secret fitting, and it is the wrong one. In the guide's own two-counter game, take secret RY. RR truly scores 1. If the keeper says 2, the breaker names RR at once; if 0, YY.

  I played the guide's ways with one score off by 1, every secret and every test. The scores then fit no secret, or fit exactly one wrong secret, this often:

  | Counters | Fits no secret | Fits one wrong secret |
  |---|---|---|
  | 2 | 4 | 4 |
  | 3 | 24 | 6 |
  | 4 | 84 | 8 |

  The guide's "When a score is wrong" box already lists "the breaker names a secret and the reveal shows another". Only the overview's statement of fact is too strong.
- **Smallest fix:** "One wrong score can make the scores fit no secret, or point to the wrong one, so scoring is done with objects and every score is checked at the end."

### 4. The triangle outlines are exactly the size of the green triangle, so the print check cannot work as worded (pp. 1–2)

- **Quoted text:**
  - "the slots must be 1 inch for a counter, and the triangle outlines must fit a green triangle."
  - "A counter fits inside a printed slot and a green triangle inside a printed outline. If not, the printer shrank the page."
- **Evidence:** on all 7 boards each outline is an equilateral triangle exactly 1.000 in on a side, measured along the centre of a 0.7 pt line (`extract_pdf.out`). The green block's edge is 1 in (Week 1's measurement). So at 100% the block covers the outline exactly. It cannot sit "inside" it, and a printer shrink of a few per cent would be hard to see. The 1.04 in slots leave a 1 in counter only about 0.02 in on each side. This is a digital measurement; I did not try real blocks or a printer.
- **Smallest fix:** check the print with a ruler: "Each score box should measure 1 inch." Say the triangle "covers its outline". Alternatively, draw the outlines at about 1.1 in; the columns are 1.2 in apart, so they still fit.

### 5. 2–3 Problem 2: "top row of the picture", but that page's picture has one row (p. 6)

- **Quoted text:** "Three fixed questions: Q1 'Is it the triangle, rhombus, trapezoid or hexagon?' (top row of the picture)".
- **Evidence:** the picture beside 2–3 Problem 2 (p. 2) is a single row of eight small blocks (`extract_pdf.out`, `source/week-06/src/common.tex` `\smallblocks`). The two-row picture is on p. 1. The question itself names the four blocks, so nothing is wrong mathematically, but an adult who repeats "top row" to a child on p. 2 points at nothing.
- **Smallest fix:** "(the first four blocks in the picture)" or "(the top row of the picture on p. 1)".

### 6. 4–5 Problem 9: the proof skips the case where all six stay together (p. 9)

- **Quoted text:** "As |D| = 0, 1, 2, 3, 4, test 2 splits the six as 6; 3+3; 1+4+1; 3+3; 6, so a group of 3 or 4 is left. Test 3 gives a group of four at most three values. A group of three is either …"
- **Evidence:** when |D| = 0 or 4, the group left after test 2 is all six rows, not 3 or 4, and the next two sentences treat only groups of four and three. The conclusion is still right: a third test gives six rows at most three values. `check_answers.out` confirms that every group of three or more keeps two secrets together under any test 3.
- **Smallest fix:** "… so a group of 3, 4 or 6 is left. Test 3 gives a group of four or six at most three values."

## Not checked

- Physical fit of real counters, green triangles and folders. Item 4 is a measurement of the PDF only.
- The real shapes of the pink right triangle, teal kite and gray dart; the README says the drawings are approximate. The guide's answers depend only on their side counts and colours. These match the drawings and the Week 1 description of the chevron as the concave six-sided piece.
- A clean rebuild (XeLaTeX and pdfLaTeX are not available here). The text and drawing comparison in `source_vs_pdf.out` stands in for it.
- The archived versions and the packet README.
