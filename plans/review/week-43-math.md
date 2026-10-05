# Week 43 (Shuffling picture cards): math check

Scope: `lowell-math-circle-year-2/week-43/week-43-k-1.pdf` (4 pp., Problems 1–5), `week-43-grades-2-3.pdf` (4 pp., Problems 1–6), `week-43-grades-4-5.pdf` (4 pp., Problems 1–7) and `week-43-facilitator.pdf` (6 pp.). I also checked the bonus companion in the same folder: `week-43-bonus.pdf` (3 pp., Problems 1–3) and `week-43-bonus-facilitator.pdf` (3 pp.). I ignored archive folders. Sources read: `source/week-43/editable/src/write.py` and `common.py` (base pages), `facilitator-src/guide.json`, and `source/week-43-bonus/student/build.py`. My scripts and their outputs are in [checks/week-43/](checks/week-43/). Checked October 5, 2026.

**Result: no stated answer is wrong in any band, the guide or the bonus. I found 2 problems. In K–1 Problem 2, the crossed-out card and the four answer rows per card fit the reading "this card cannot be first" (4 rows). The guide expects "this card was drawn first" (2 rows). In Grades 2–3, the worked example for the three-swap rule on page 4 is a complete answer to Problem 5.**

## How it was checked

- The six delivered PDFs are byte-identical (MD5) to `source/week-43/editable/reference-pdfs/` and `source/week-43-bonus/reference-pdfs/` (`extract.out`).
- `extract.py` uses PyMuPDF to read every picture card straight from the delivered PDFs: its fill colour, shape, position and letter label. It also reads every ticket number, swap arrow and cross-out line, and every empty answer frame. It writes `extracted.json` (365 checks, 0 failures, `extract.out`):
  - Every icon's shape matches its colour and letter: A orange square, B green circle, C violet triangle, D cyan diamond, E yellow pentagon.
  - Every letter label sits in the same card as its icon.
  - Every square, circle and diamond has equal x and y extent. The triangle is an isosceles picture icon, not a regular figure.
  - Every printed swap arrow is correct when computed from its input row: "1 with 3" ABC→CBA, "2 with 2" CBA→CBA, "3 with 1" CBA→ABC.
  - The chooser picture (triangle, then square, then row C A B) matches its caption in all three bands.
  - In the bonus, all model cards and cells are squares and the circles are round. The A1/A2 cards show squares and B1/B2 show circles; the model cards are 72 pt = 25.4 mm, as the bonus guide says. The cut bar sits between X and Y, and WXYZ → YZWX. The three gap bars sit before X, between X and Y, and after Y, with the numbers 1, 2 and 3 directly under them. Inserting Z at gap 2 gives XZY.
- `check_base.py` enumerates every base task by brute force (108 checks, 0 failures, `check_base.out`):
  - the 6 first-two chooser stories;
  - the 6 two-swap stories from every one of the 6 starts (a bijection each time);
  - the missing-ticket cases and the same-story/different-start comparisons for all start pairs;
  - the 27 wrong-range stories and the no-self-swap rule;
  - left-to-right Fisher–Yates for n = 2…6, including the 4- and 5-card versions from every start;
  - the guide's "locate the target card" construction for every target with n = 3, 4, 5;
  - n^n not divisible by n! for n = 3…7.

  It reads the printed ticket pairs, targets and answer frames from `extracted.json`. It parses the guide's tables and lists from the PDF and compares each one.
- `check_bonus.py` checks every bonus task and guide claim (46 checks, 0 failures, `check_bonus.out`):
  - P1: the 24 labeled orders and the multinomial multiplicities for several card multisets;
  - P2: closure under cuts, and under cuts with reversal, for 4 and 5 cards; the neighbour invariant; the first-card distribution after one or more random cuts; that a random cut after a uniform shuffle stays uniform;
  - P3: all 24 row-and-gap insertion stories and the four printed targets; that a biased old shuffle stays biased; that a gap choice which depends on the old row can have uniform gaps and still reach only 12 orders; the 5- and 6-card insertion extensions.

## K–1: one wording/space problem (Problem 1 below); everything else correct

- **P1:** six rows, ABC, ACB, BAC, BCA, CAB, CBA. The page prints 6 record rows and a 3-slot mat.
- **P2:** guide answer: A first gives ABC, ACB; B first gives BAC, BCA; C first gives CAB, CBA. No two first-two draws give the same row. The answer is correct for the guide's reading, but see Problem 1.
- **P3:** (1,2)→ABC, (1,3)→ACB, (2,2)→BAC, (2,3)→BCA, (3,2)→CBA, (3,3)→CAB. No row comes from two stories. The page prints 6 records of two tickets and a row.
- **P4:** the printed first-ticket sets are {2,3}, {1,3} and {1,2}. Removing ticket 1 rules out ABC and ACB, ticket 2 rules out BAC and BCA, ticket 3 rules out CAB and CBA. The page prints 2 rows per case.
- **P5:** no. All six comparisons in the guide's table are correct. More generally, no fixed story sends two different starts to the same row (all 30 start pairs × 6 stories). Undoing the swaps in reverse order recovers the start.

## Grades 2–3: one problem (Problem 2 below); every answer correct

- **P1:** six rows, each from exactly one first-two story, each with chance 1/3 × 1/2 = 1/6.
- **P2:** the printed pairs, in reading order, are (1,2), (2,2), (3,2), (1,3), (2,3), (3,3). They give ABC, BAC, CBA, ACB, BCA, CAB, exactly the guide's "printed order". The rule is fair.
- **P3:** from BAC, every row is reachable exactly once: ABC (2,2), ACB (2,3), BAC (1,2), BCA (1,3), CAB (3,2), CBA (3,3). This matches the guide's table and the six printed targets.
- **P4:** (1,2) six times gives ABC six times, which is a legal outcome. For adults: the chance that six fair shuffles show all six rows is only 6!/6^6 = 5/324 ≈ 1.5%.
- **P5:** exactly four stories give ABC: (1,2,3), (1,3,2), (2,1,3) and (3,2,1). The guide's descriptions of which slots are swapped twice are correct. Every row has at least 4 stories, so three records can always be filled.
- **P6:** no. 27 is not a multiple of 6. The exact counts are 4, 5, 5, 5, 4, 4 for ABC, ACB, BAC, BCA, CAB, CBA, as in the guide.

## Grades 4–5: no errors

- **P1–P2:** both rules are fair. The 6 stories biject onto the 6 orders.
- **P3:** from CBA the chances stay 1/6. The guide's relabelling argument (swap the labels A and C) checks out story by story.
- **P4:** not fair, because 27/6 is not a whole number. The counts are 4, 5, 5, 5, 4, 4.
- **P5:** only BCA (via BAC) and CAB (via CBA), each with chance 1/2 if the first choice is fair. Not a fair shuffle of all six.
- **P6–P7:** left-to-right Fisher–Yates with ticket sets {i..n} gives 24 and 120 equally likely stories, one per order, from every start.

## Adult guide (base)

The overview is true with its stated hypotheses:

- the direct chooser and the left-to-right Fisher–Yates bijection, for n cards and any fixed start;
- the 27-story divisibility proof and its 4, 5, 5, 5, 4, 4 distribution;
- that the no-self-swap rule gives only BCA and CAB;
- that a fixed history is a bijection of starts, and how this differs from the uniform distribution.

The limits it states (equal conditional ticket chances, resets, distinct cards, small samples) are the right ones. Every answer-key table, list and count on pp. 3–5 matches my enumeration. So do the launch examples on p. 2: draw C then A to get CAB; ticket 3 then ticket 2 to get CBA. The route note on p. 6 cites the right problem numbers. The only guide issue is the K–1 P2 sentence discussed in Problem 1.

## Bonus companion and its guide: no errors

- **P1:** six picture rows (AABB, ABAB, ABBA, BAAB, BABA, BBAA), each with exactly 4 labeled orders, so each has chance 1/6. The four AABB labelings and the extensions are correct: A1, A2, A3, B1 gives 4 rows × 6, and three A with two B gives 10 rows × 12.
- **P2:** cuts alone give ABCD, BCDA, CDAB, DABC. Reversal adds DCBA, CBAD, BADC, ADCB. ABDC is impossible under both rules, and so are ADBC and ACBD; the cyclic-neighbour argument is correct. Five cards give 5 and 10 rows. A fair first card does not make a fair shuffle.
- **P3:** ABCD comes from ABC with gap 4, DACB from ACB with gap 1, BDCA from BCA with gap 2, and CBAD from CBA with gap 4. The 24 stories biject onto the 24 orders, so each has chance 1/24. The independence hypothesis is needed (counterexample in `check_bonus.out`). Fair gaps cannot repair a biased old shuffle. The 120-story extension for E is correct.

## Problems found

### 1. K–1, page 2, Problem 2: the crossed-out card and four rows per card invite a different answer from the guide's

- **Quoted text:** "Problem 2: For each crossed-out first card, find every row still possible. Could two different first-two draws make the same row?"
  - Diagram: a square, a circle and a triangle, each struck through by a diagonal line, each followed by four empty three-card rows.
- **Guide (p. 3):** "In the three displayed cases the crossed-out card is the card already drawn first. If A is first, the rows are ABC and ACB; if B is first, BAC and BCA; if C is first, CAB and CBA."
- **Evidence:**
  - `extract.out` and `check_base.out` show 12 three-card rows on the page, exactly 4 beside each crossed-out card.
  - Under the guide's reading ("this card was drawn first") each case has 2 rows.
  - Under the natural reading of a struck-through picture ("this card cannot be first") each case has exactly 4 rows: square crossed out gives BAC, BCA, CAB, CBA, and so on. This matches the printed space exactly.
  - Nothing on the student page says that a cross-out means "drawn and kept out". The guide has to supply that convention in its own answer.
  - Elsewhere in this collection a K–1 cross-out means "impossible" (Week 27 P3–P4, Week 44 P2: "cross out any impossible bag").
  - The answer depends on the reading (2 rows versus 4 per case). An adult reading the problem aloud has no cue for the intended one.
- **Smallest fix:** remove the slashes and put each card in the first box of two rows. Print two rows per card, not four, and write: "Problem 2: Each row starts with the card drawn first. Find every row still possible. Could two different first-two draws make the same row?" Then change the guide's first sentence to "Each displayed card is the card drawn first." Alternatively, keep the page and change the guide answer to the four rows that do not start with the crossed-out card. That changes the problem's intent from fixing the first draw to excluding it.

### 2. Grades 2–3, page 4, Problem 5: the worked example is itself a P5 collision

- **Quoted text:** shared rule "Change the rule: use tickets 1, 2, 3 at every swap. Swap slot 1, then slot 2, then slot 3 with the chosen slot…", followed by the picture ABC →"1 with 3"→ CBA →"2 with 2"→ CBA, then CBA →"3 with 1"→ ABC. Then "Problem 5: Start with A B C each time. Find several different three-ticket stories that give the same final row."
- **Evidence:** the pictured complete story is (3,2,1), and it ends at ABC (`extract.out`, p4 arrows; `check_base.out`). The do-nothing story (1,2,3) also ends at ABC, so the page already shows two different stories with the same final row. That collision, "swap and then swap back", is the discovery P5 asks for. The guide's P5 key lists (3,2,1) as one of the four ABC answers. Two of the three record slots can be filled from the example, and the third follows from the same trick: (1,3,2) or (2,1,3).
- **Smallest fix:** change the example's last step to "3 with 2", so CBA → CAB and the shown story (3,2,2) ends at CAB. This still shows slot 3 reaching back to an earlier slot. The other CAB stories, (1,1,1), (2,2,1) and (3,3,3), are left for the children to find. "3 with 3", ending at CBA with the story (3,2,3), would also work.

## Notes (not errors)

- The shared demonstrations reuse task instances:
  - The chooser example CA → CAB is one of the six rows in K–1 P2 and in P1 for Grades 2–3 and 4–5.
  - The two-swap demo (3,2) → CBA answers the printed (3,2) cell of 2–3 P2 and is one of the six answers to K–1 P3 and 4–5 P2.
  - The guide's launch asks for exactly these demonstrations.

  No count is given away, so this is a design point for the card review, not a mathematical error.
- On 2–3 p. 4, in the second demo row (CBA → ABC), the letters C and A touch the lower corners of their icons. It is cosmetic, and the letters are still correct.
- The guide's route note on p. 6 has the typo "The27-story".
- I could not check the citation "Elementary Sorts lecture, slide 71 (PDF p. 18)" because the lecture is not in the repository. The guide describes `shuffleAlternate` as swapping slot i with a uniform slot in i..n. That matches the left-to-right algorithm the pages use, but I did not check it against the source.
