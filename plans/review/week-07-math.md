# Week 7 (take-away games): math check

Scope: `lowell-math-circle-year-2/week-07/week-07-k-1.pdf` (F07-K-v4, 6 pp., Problems 1–9), `week-07-grades-2-3.pdf` (F07-M-v4, 5 pp., Problems 1–9), `week-07-grades-4-5.pdf` (F07-U-v4, 8 pp., Problems 1–14) and `week-07-facilitator.pdf` (F07-FAC-v4, 9 pp.). Sources: `lowell-math-circle-year-2/source/week-07/src/` and `guide-src/facilitator.tex`. I did not use the packet's own `guide-src/check.py`. The return visit (`week-07-return-visit*.pdf`) and the archive folders were not checked, and I opened no use logs or session records. My scripts and their outputs are in [checks/week-07/](checks/week-07/). Checked October 5, 2026.

**Result: every answer in all three bands is correct, and every problem can be done as stated. All diagrams match their text. K–1 Problems 8 and 9 print 1st/2nd choices that the text never asks for (item 6). The adult guide has one false general statement (item 1) and four smaller problems (items 2–5). None of them changes an answer to a problem.**

## How it was checked

- `games.py` is my own solver. It searches the game tree directly, with no remainder formulas, for any move list, any number of piles, and both win rules. It follows the 4–5 rule that a player who cannot move while counters are left loses. It also has Grundy values, the opening move "take as many as allowed", and a test of whether that greedy play wins against every reply.
- `extract_pdf.py` (output `extract_pdf.out`, `pdf_geometry.json`) reads the student PDFs back:
  - **Counters.** Every drawn counter, grouped into rows and piles: 113 counters in K–1, 87 in 2–3 and 14 in 4–5. They are all circles 0.4 in across.
  - **Tracks.** All 39 number tracks are numbered 0–10, 0–20 or 0–30 with no gaps. Every square is 0.676 in on both sides. Consecutive numbers always share an edge with no thick wall, and every pair of neighbouring squares with non-consecutive numbers (1|20, 11|30, …) is walled off.
  - **4–5 chart.** 10 × 10 square cells of 0.39 in, labelled 0–9 on both axes.
  - **Labels.** The 1st/2nd and first/second labels on every pile row.
- `check_answers.py` (output `check_answers.out`) solves every problem, reading pile sizes and track ranges from the PDF, and runs 97 checks of the pages and the guide against the solver: answers, hints, the reply table, the launch, the three race games, the overview claims and the materials counts. It found 0 mismatches. Its three NOTE lines are items 1 and 5 below, plus one true statement that I do not count as a problem: "In K–1 P8, 1 and 4 is P" is a position of that game but not one of its printed pairs.
- `misere_and_periodicity.py` (output `misere_and_periodicity.out`) tests two general claims in the guide. It covers all 255 move lists made from 1–9 with up to four moves.
- `source_vs_pdf.py` (output `source_vs_pdf.out`) confirms the delivered PDFs carry the source text I read: all 32 problem statements and the three sets of opening rules. It also confirms that every guide sentence quoted below is in the delivered guide. pdfLaTeX is not installed here, so I could not test a clean rebuild.

## K–1: all answers correct; one gap between text and page (item 6)

- **P1:** go 2nd with 3 and 6. Go 1st otherwise: 2 take 2, 4 take 1, 5 take 2, 7 take 1, 8 take 2.
- **P2, P3:** the first player wins from 10. Every winning line lands on exactly 9, 6, 3, 0, because each winning move is the only one.
- **P4:** take 2 from 5, 1 from 7, 2 from 8, 1 from 10. Each is the only winning move.
- **P5:** go 2nd on 3, 6 or 9. Otherwise go 1st and take 1 from 1, 4, 7, 10 or 2 from 2, 5, 8.
- **P6:** with 1, 2 or 3 from 10, only taking 2 wins. Every winning line lands on 8, 4, 0.
- **P7:** with 1 or 4 from 8, only taking 1 wins. The winning lines land on 7, 5, 0 or 7, 2, 0.
- **P8:** go 2nd with 2/2, 3/3 and 4/4. Go 1st with 1/2 (only move: 1 from the 2) and with 2/4 (2 from the 4, or 1 from the 2).
- **P9 (last counter loses):** go 2nd with 1 and 4. Go 1st with 2 (take 1), 3 (take 2), 5 (take 1) and 6 (take 2).

## Grades 2–3: checks out completely

- **P1:** 2 second, 5 take 3, 6 take 4, 7 second, 8 take 1. Each winning move is the only one.
- **P2:** 0, 2, 7, 9, 14, 16.
- **P3:** go second from 14 and 16. From 10 and 17 two moves win; from every other start, exactly one.
- **P4:** Lena is right. The guide's reply table wins against every line.
- **P5:** Omar does not always win. The two refutations are 13 → 9 → 8 → 4 → 0 and 13 → 9 → 5 → 1 → 0. Omar's first move, taking 4, is the only winning first move.
- **P6:** with 50, go first and take 1, the only winning move. With 100, go second.
- **P7:** 5/5 second. 5/6 first, with exactly two winning moves: 1 from the 6, giving 5/5, or 1 from the 5, giving 4/6.
- **P8:** 5 second, 6 take 1 or 4, 8 take 1, 9 take 4, 10 second.
- **P9:** with 1 or 4, 0, 2, 5, 7, 10, 12, 15, 17, 20. With 1, 3 or 5, the even squares.

## Grades 4–5: checks out completely

- **P1:** 7 take 1, 9 second, 11 take 2, 12 second, 16 take 1.
- **P2:** multiples of 3, and multiples of 4.
- **P3:** 5 take 3, 8 take 1, 9 second, 11 take 4, 14 second.
- **P4:** 0, 2, 7, 9, 14, 16, 21, 23, 28, 30.
- **P5:** 5, 8, 10, 12, 15, 17, 19, 22, 24, 26, 29. If greedy play lasted the whole game, the list would add 13, 18, 20, 25 and 27, and greedy play is unbeatable only from 1, 3, 4, 6 and 11, as the guide says.
- **P6:** with 1 or 2, go first and take 1. With 1, 2 or 3, go second. With 1, 3 or 4, go second.
- **P7:**
  - 1 or 4: remainder 0 or 2 on dividing by 5.
  - 2 or 3: remainder 0 or 1 on dividing by 5. Square 1 is coloured because no move is possible from it.
  - 1, 3 or 5: the even squares.
- **P8:** the pattern repeats every 7 from 0 (checked to 1000).
- **P9:** a search of all 4,095 move lists drawn from 1–12, on piles up to 120, gives the multiples of 5 exactly for the lists containing 1, 2, 3 and 4 and no multiple of 5. It gives the multiples of 3 exactly for the lists containing 1 and 2 and no multiple of 3. So there are infinitely many answers.
- **P10:** 1 second, 3 take 2, 5 take 1, 7 second, 8 take 1.
- **P11:** 1, 4, 7, …, 19, and 1, 5, 9, 13, 17. Square 0 is not coloured.
- **P12:** second.
- **P13:** 34 cells, those with |a − b| = 0, 3, 6 or 9. Piles of 20 and 11: second.
- **P14:** 0, 1, 4, 8, 11, 12, 15, 19, 22, 23, 26, 30. The pattern repeats every 11 from 0, and no shorter period works. Kim is right for any finite list.

## Adult guide

All 32 problem answers and their hints are correct. So are the launch script, the races to 10, 21 and 100, the materials and copy counts, and the overview's statements about moves 1 to k, Grundy values, two piles and designing a rule. The problems are below.

### 1. Overview: the "last counter loses" shift is not special to moves 1 to k (p. 8)

- **Quoted text:** "With moves 1 to k, P = remainder 1 on dividing by k + 1: the player facing 1 must take it, and the same complement strategy aims at 1 instead of 0. (The shift by one is special to moves 1 to k.)"
- **Evidence:** in `misere_and_periodicity.out`, with one pile, the last-counter-loses squares are exactly the ordinary squares moved up by one for all 255 move lists tested (piles 0–60), under the packet's 4–5 rule that a player who cannot move loses. For example:
  - 1, 3 or 4: the ordinary squares are 0, 2, 7, 9, 14, 16; the last-counter-loses squares are 1, 3, 8, 10, 15, 17.
  - 2 or 3: 0, 1, 5, 6, … become 1, 2, 6, 7, ….

  The reason: taking the last counter is never good unless forced, so a pile of n plays like an ordinary pile of n − 1. The usual textbook convention, where a player who cannot move wins, gives the same shift for every list containing 1.

  The shift does fail for two piles. With 1 or 2, piles of 1 and 1 are a win for the player to move (take one, and the opponent must take the last counter), so copying no longer works.

  This matters in the session. The guide's own claims to listen for at 4–5 include "when the last counter loses, every coloured square moves up 1." A child who tests that claim on 1, 3 or 4 is right, but this sentence would lead the adult to say otherwise.
- **Smallest fix:** replace the parenthesis with: "(For one pile the shift by one works for every rule on these pages: taking the last counter is never good unless forced, so a pile of n plays like an ordinary pile of n − 1. It fails for two piles: with 1 or 2, piles of 1 and 1 are a win for the player to move.)"

### 2. "The pattern always repeats" leaves out its conditions (p. 1)

- **Quoted text:** "The pattern always repeats, and it changes when the rule changes."
- **Evidence:** the pattern repeats only for a finite list of moves, and it may repeat only after a start-up stretch. Nine of the 255 lists tested repeat only from a later square. With moves 2, 4 or 7, the squares to leave are 0, 1, 6, 9, 12, …: 3 is not coloured, and the pattern repeats every 3 only from square 4. With 1, 6 or 9, the pattern repeats every 5 only from square 10. Page 8 ("from the first of them on the labels repeat") and the P14 answer state this correctly. Every rule on the student pages does repeat from 0.
- **Smallest fix:** "For any finite list of moves the pattern ends up repeating (for every rule on these pages, right from 0), and it changes when the rule changes."

### 3. The reply table names the wrong column for "remainder" (p. 3)

- **Quoted text:** "'Remainder' means the remainder on dividing by the number in the second column."
- **Evidence:** the second column is "Where", which holds entries such as "K–1 P7; 2–3 P8, P9; 4–5 P7". The divisor ("dividing by 5", "dividing by 7") is in the third column, "Squares to leave". An adult following the sentence literally has no divisor, or might divide by the 7 in "P7".
- **Smallest fix:** "…dividing by the number in the 'Squares to leave' column."

### 4. "Take 1" is not always legal under the table's own rules (p. 3)

- **Quoted text:** "If you are handed one of the squares you want to leave, there is no good move: take 1 and wait for a mistake."
- **Evidence:** the same table lists the rules "2 or 3" (4–5 P7) and "2, 5 or 6" (4–5 P14). Under these rules taking 1 is not allowed. From square 1 under "2 or 3" no move is possible at all, so the player loses.
- **Smallest fix:** "take the smallest number allowed and wait for a mistake."

### 5. Gaps in the reply table's last column (p. 3)

- **Quoted text:**
  - Row 1 or 4: "remainder 1: take 1; 3: take 1; 4: take 4".
  - Row 1 or 2: "what makes 3 with their take: they 1, you 2; they 2, you 1".
- **Evidence:**
  - **1 or 4.** From remainder 1, taking 4 also wins (6 → 2, 11 → 7). The guide accepts this at 2–3 P8 ("6: first, take 1 or 4"), and the other rows list every winning take ("3: take 1 or 3", "3: take 2 or 3"). An adult checking a child's 6 → 2 against this row would wrongly correct it.
  - **1 or 2, and 1, 2 or 3.** These rows give only the reply to an opponent's take. They do not give a move when the adult starts from an ordinary pile, such as 16 at 4–5 when "the third child may play the adult: choose the pile and who goes first". Nothing is wrong, and the problem-by-problem answers cover the printed cases.
- **Smallest fix:**
  - Row 1 or 4: "remainder 1: take 1 or 4".
  - Row 1 or 2: begin with "take the remainder on dividing by 3; after that, …".
  - Row 1, 2 or 3: begin with "take the remainder on dividing by 4; after that, …".

### 6. K–1 Problems 8 and 9: the text does not ask for the printed choice (K–1 p. 6)

- **Quoted text:**
  - P8: "Now make two piles, and take 1 or 2 counters from one pile. Whoever takes the last counter on the table wins."
  - P9: "Now whoever takes the last counter loses. Play each pile many times with your partner."
- **Evidence:** both problems print "1st 2nd" beside every row, as P1 does, and the guide's answers are choices to circle ("Circle 1st or 2nd for 2 and 2, …"). Neither problem's text asks the child to circle anything, and P8 does not ask the child to play. This is a wording gap rather than a mathematical error, but the printed labels are not tied to any task.
- **Smallest fix:** end both problems with P1's sentence: "Circle whether you would rather go 1st or 2nd." In P8, add "Play each pair of piles many times with your partner." before it.

## Not checked

- The return visit and its guide.
- The archived versions.
- Physical fit of real counters and tokens on the 0.676 in squares.
- A clean rebuild (pdfLaTeX is not available here). The text comparison above stands in for it.
