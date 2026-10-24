# Review: Poisoned cookie (Chomp), draft v1

Reviewer stage. I did not edit the draft.

## What I checked

- Rendered all 15 pages (5 per band) at 80 dpi and looked at each one. I measured one K–1 board at 254 dpi: its cells are 25.0 mm, so pages printed at 100% match the 25 mm counters. The LaTeX logs show no overfull or underfull boxes, and nothing on any page overflows or overlaps.
- Rebuilt the draft from `draft/src/build.py` in a scratch copy. Every page renders pixel-identical to `draft/*.pdf`, so the sources match the PDFs.
- Read every board's shape directly from the TikZ coordinates in the generated `.tex` files rather than from the author's intent in `build.py`, and solved each board with my own Chomp solver (not the author's `chomp.py`). Every board is a proper staircase with the poison in the bottom-left corner.
- Checked the outline's claims independently:
  - On 3 by 4, (2,3) is the only winning bite. On 3 by 5 it is (3,4), on 4 by 5 it is (3,3), and on 3 by 6 it is (2,4), each the only one.
  - With two rows, the player to move loses exactly when the top row is one shorter than the bottom row (checked for bottom rows up to 15).
  - On an L-shaped board, the player to move loses exactly when the arms are equal (checked for arms up to 5).

**Verdict.** The mathematics is correct on every page. Every printed board has the answer the page implies, and the packet follows the organizer's format closely: correct header and footer, no titles, no encouragement, no hints, no lettered sub-steps. Each band builds sensibly from playing to explaining. The problems that need fixing are of a different kind:

- **4–5 Problem 5 can be misread in a way that flips its answer.** It uses "L position" to mean a losing position, and the board printed next to it is L-shaped.
- **The bite card covers the neighbouring board.** The card is 15 cm, and on every page that draws boards at playing size, it reaches the next board.
- **4–5 has two gaps.** It asks for a general two-row explanation without a concrete two-row stage first, and its "find every" problem has nowhere to record the work.
- **Smaller wording and sequencing points** are listed in section B.

## Answer check, every problem

Bites are given as (row, column), counted from the poison corner. Positions are row lengths, bottom row first. "L" means the player to move cannot make sure to win.

| Band / problem | Boards | Verified outcome |
|---|---|---|
| K–1 P1 | (4), (2,1), (2,2), (3,1) | (4): bite (1,2). (2,1): no winning bite. (2,2): bite (2,2). (3,1): bite (1,3). |
| K–1 P2 | 2×3, 2×4 | Only (2,3) and only (2,4), each leaving the top row one shorter |
| K–1 P3 | 3×3 | Only (2,2), leaving the equal L (3,1,1) |
| K–1 P4 | (3,1,1), (4,1,1), (4,1,1,1), (2,1,1,1) | Circle the 1st and 3rd boards (equal arms). The 2nd board wins by (1,4); the 4th by (3,1). |
| K–1 P5 | 4×4, 2×6 | Only (2,2); only (2,6) |
| K–1 P6 | 4×5 grids | 16 losing boards fit: (1); (2,1) (3,2) (4,3) (5,4); (3,1,1) (4,1,1,1); (2,2,1) (2,2,2,1) (3,3,1,1) (4,2,2) (5,3,2) (5,2,1,1) (5,3,3,2) (5,5,3) (5,5,2,2) |
| 2–3 P1 | (3,1), (2,1), (2,2), (3,2), (4,2), (3,1,1) | Wins: (1,3); none; (2,2); none; (1,4); none |
| 2–3 P2 | 2×3, 2×4, 2×6 | Top-right cookie each time, the only winning bite |
| 2–3 P3 | (5,4), (5,2), (6,6), (4,1), (6,5), (6,3) | None; (1,4); (2,6); (1,3); none; (1,5) |
| 2–3 P4 | 3×3, 4×4 | Only (2,2) |
| 2–3 P5 | 10×10 | (2,2), then copy the opponent's bite on the other arm |
| 2–3 P6 | 3×4 | Only (2,3), leaving (4,2,2) |
| 2–3 P7 | 3×7 grids | 10 three-row losing boards: (2,2,1) (3,1,1) (4,2,2) (5,3,2) (5,5,3) (6,3,3) (6,4,2) (7,4,3) (7,5,2) (7,7,4) |
| 4–5 P1 | 2×4, 2×6, 3×3, 4×4 | (2,4); (2,6); (2,2); (2,2), each the only one |
| 4–5 P2 | all 19 boards inside 3×3 | In page order, boards 8 (3,2), 9 (3,1,1), 10 (2,2,1), 15 (2,1) and 19 (poison alone) are L. The other 14 are W. The set is complete, with no repeats. |
| 4–5 P3 | — | True for every two-row rectangle and every square larger than 1×1 (see B1) |
| 4–5 P4 | 3×4 | Exactly one X, at (2,3). Each of the other 10 bites has a refuting reply; table in section D. |
| 4–5 P5 | 3×4; (3,1,1) | Ana's argument is valid. On 3×4, after the top-right bite, the second player's only winning reply is (2,3), the first player's own winning bite. On (3,1,1), no cookie lies in every bite. |
| 4–5 P6 | 3×5, 3×6 | Only (3,4), leaving (5,5,3); only (2,4), leaving (6,3,3) |

## A. Changes needed

### A1. 4–5 Problem 5: "L position" collides with L-shaped boards (page 4)

Quoted: "the second player would answer with a bite that leaves an **L position** … Then the second player would face **the L position**".

"L position" is the author's shorthand for a board labelled L in Problem 2. In this packet, though, "L" already names a shape, and it is the shape children use to explain the square trick in Problems 1 and 3. Worse, the board printed under Problem 5, (3,1,1), is literally L-shaped.

Following the instruction "Check her reason on the 3 by 4 board", a child eats the top-right cookie, finds the reply (2,3), and gets (4,2,2). That board is not L-shaped. A child reading "L position" as a shape will conclude that Ana is wrong, which flips the answer to "Is Ana right?". The term was also never introduced as a noun: Problem 2 only asks children to write the letter.

Fix: reword Ana without the abbreviation. For example: "…the second player would have an answer after which the first player cannot make sure to win. But every bite on the full board eats the top-right cookie too, so the first player could have made that same bite at the start. Then the second player would face that same board, and the first player would be the one who can make sure to win. …"

### A2. The 15 cm bite card covers other boards on the same page (K–1 pages 1–4, 4–5 page 5)

The bite card is the device that enforces the rule ("eat every cookie under the card"). It reaches 15 cm up and right of the chosen cookie, and on these pages the playing-size boards sit closer together than that:

- **K–1 page 1.** The (2,1) board is 22 mm to the right of the 1×4 row. A bite at (1,2) on the row puts the whole (2,1) board under the card. The lower boards, (2,2) and (3,1), are 10 mm below the upper ones, so any bite on them covers parts of both upper boards.
- **K–1 page 2.** The 2×3 and 2×4 boards sit side by side. The 3×3 board is about 30 mm below them, and its card reaches them.
- **K–1 page 3.** The four L boards are in a 2-by-2 block, so the same overlaps occur.
- **K–1 page 4.** The 2×6 board is 12 mm below the 4×4 board, and its card covers most of the 4×4.
- **4–5 page 5.** The 3×6 board is 12 mm below the 3×5 board, with the same result.

If counters are on more than one board, which is likely with kindergartners, the material now enforces the wrong rule. That is exactly the failure from the lamp session.

Fix, choosing one of these:

- (a) Lay the boards on a falling diagonal, each later board lower and to the right of the one before. A card then never reaches another board. This fits two boards per page.
- (b) Give one playing-size board per page or region.
- (c) Keep these diagrams compact for marking X's, and have children play on the separate printed boards from the materials list, as 2–3 and 4–5 already do.

Whichever is chosen, rehearse it, along with the card itself. With an opaque 15 cm card resting on counters, can a child see and remove exactly the covered counters? Where exactly does the card's corner go: on the cookie, or at the bottom-left corner of its square? Mark this as untested.

### A3. 4–5 asks for a general two-row explanation with almost no two-row experience (Problem 3)

Problem 3 asks children to explain "every rectangle with two rows … however long the sides are". That explanation needs the fact that a two-row board whose top row is one shorter loses for the player to move, at every length. Before Problem 3, the 4–5 band has seen only two two-row rectangles (P1) and the two-row boards up to 3 columns inside P2.

The 2–3 band gets a whole problem (2–3 P3) on two-row boards of length up to 6. The standard says children should meet an idea in concrete cases and use it before explaining it.

Fix: add four to six compact two-row boards before Problem 3, either in Problem 1 or as a new problem, with at least two "one shorter" boards among them. Use the same form as 2–3 P3's first sentence: "It is your turn on each board. If you can make sure you win, mark your first bite with an X." Good choices are (5,4), (6,3), (6,5), (4,1) and (5,2), all of which fit the printed 2×6 board.

### A4. 4–5 Problem 4 ("Find every…") has nowhere to record the case analysis (page 3)

"Find every" means showing that 10 of the 11 bites fail, each with a refuting reply. Doing that requires knowing the outcome of up to 15 boards that are not in Problem 2, all of them with a bottom row of 4. The page gives one 11 mm 3×4 board, which makes memory and transcription the main demand.

Fix: add about 10 small blank 3×4 grids below the board, with no label and no sentence describing them. Children can record bites and replies however they choose. This also serves Problem 5's check.

### A5. 4–5 Problem 5: "Check her reason on the 3 by 4 board" gives no concrete action

Ana's argument starts from an assumption that is false on 3×4, so "check" has no obvious meaning. Children need to know what to do and what to produce.

Fix: give the concrete step and a place to put it. For example: "On the 3 by 4 board, the first player eats only the top-right cookie. Find a bite that makes sure the second player wins from there, and mark it on this board." Then draw a compact (4,4,3) board and ask "Is Ana right?".

Keep the final sentence about (3,1,1), which is the best part of the problem.

### A6. K–1 Problems 2 and 3 tie up the only adult (pages 2–3)

The K–1 table has one parent volunteer and two pairs. "Play the adult on each board" leaves one pair waiting through two problems, and it requires the volunteer, who is not a mathematician, to play both strategies perfectly.

Fix: say "Play on each board, taking turns going first", or "Play the adult or your partner…". Then pairs can continue while the adult rotates.

The facilitator guide must give the volunteer both strategies: on two rows, keep the top row one shorter; on squares, bite diagonally next to the poison, then copy on the other arm. It must also give the P4 and P6 answers.

## B. Smaller fixes

1. **"Every square" includes the 1×1 square, where the first player loses** (2–3 P5, 4–5 P3). Write "every square board bigger than one cookie" or "every square board with two or more rows". Ana's text already says "more than one cookie".
2. **K–1 order: L shapes (P4) are the reason the 3×3 bite (P3) works.** Swap them so children play equal and unequal L's before facing 3×3. The adult's bite on 3×3 then leaves a shape they already know. P1's (2,1) prepares this.
3. **2–3 P3 repeats a board.** 2–3 P3's 2×6 board (6,6) is the same board and the same task as the third board of P2. Replace it with a winning two-row board P2 lacks, for example (5,3) (win at (1,5), leaving (4,3)) or (6,2).
4. **2–3 P7 grids are 3 by 7, but the printed three-row boards stop at 5 columns** (3×5). Six of the ten answers need 6 or 7 columns. Use 3×5 grids (5 answers) or 3×6 grids (7 answers) so children can build what they colour.
5. **4–5 P6 presupposes a unique winning bite.** "Nobody knows a simple rule for **the** winning first bite on rectangles with three rows" assumes every three-row rectangle has exactly one winning bite. That is true for 3×5 and 3×6, but not known in general. Write "for finding a winning first bite". The sentence is also the one piece of commentary in the packet. It matches the outline ("three-row boards where nobody knows a rule"), so keep it, but the organizer may move it to the guide.
6. **Redundant recording instruction (2–3, 4–5).** The opening rules already say "To record a bite, draw an X on the chosen cookie". Even so, 2–3 Problems 1, 2, 3, 4 and 6 and 4–5 Problems 1, 4 and 6 repeat "mark it with an X" or a variant of it. The repetitions can go.
7. **Phrasing drifts between "make sure you win", "make sure to win", "always wins", "can always win" and "makes sure the first player wins".** Pick one wording per band, for example "make sure you win" in K–1 and "can make sure to win" in the older bands. A related point is that "a first bite that makes sure the first player wins" is loose: the bite alone does not ensure the win. In 4–5 P4, where "every" makes the meaning matter, "a first bite after which the first player can make sure to win" is exact.
8. **4–5 P2 introduces "position"** where every other page says "board". Use "board".
9. **2–3 and 4–5 rules: "every cookie above it, to its right, or both" is awkward.** The picture and the card carry the rule, so this is optional. "Every cookie above it or to its right, including those up and to the right" is clearer if it is kept.
10. **K–1 P1: a child has no way to show "I can't win here" on (2,1).** Leaving it blank looks the same as not having tried. This is optional: the adult sees the play. If changed, ask children to circle boards where they cannot make sure to win, and keep the problem to two sentences.

## C. Keep as it is

- **The launch picture** (input, card on the board, result) on a non-task 2×5 board. The bite is a losing one and gives nothing away.
- **Rules stated once.** There are no titles, encouragement, hints or lettered sub-steps, and every problem has its own boards.
- **K–1's range.** It goes from deciding (P1, P4) through finding winning bites to inventing second-player boards (P6), with as much to do as the older bands.
- **2–3's contrasts.** P1 mixes three winning and three losing boards, with "If you can't, explain why". P3 sets up the rule with contrasting two-row boards.
- **4–5 P2.** A complete, correct classification of the 3×3 box, a good backward-induction task.
- **4–5 P5's (3,1,1) board,** which makes the role of "every bite eats the top-right cookie" concrete.
- **4–5 P6's boards.** Each has a unique winning bite, and both are printed at playing size, though they need the A2 fix.

## D. Facilitator-guide material (out of scope for student pages)

- **Refuting each wrong first bite on 3×4 (4–5 P4).** Bite → board → reply → losing board left for the biter:
  - (1,2) → (1,1,1) → (2,1) → poison alone
  - (1,3) → (2,2,2) → (3,2) → (2,2,1)
  - (1,4) → (3,3,3) → (2,2) → (3,1,1)
  - (2,1) → (4) → (1,2) → poison alone
  - (2,2) → (4,1,1) → (1,4) → (3,1,1)
  - (2,4) → (4,3,3) → (2,3) → (4,2,2), or (3,1) → (4,3)
  - (3,1) → (4,4) → (2,4) → (4,3)
  - (3,2) → (4,4,1) → (1,3) → (2,2,1)
  - (3,3) → (4,4,2) → (2,3) → (4,2,2)
  - (3,4) → (4,4,3) → (2,3) → (4,2,2)

  The board (4,2,2) loses for the player to move. Each of its seven bites has an answer (bite → board → answer → board left):
  - (1,2) → (1,1,1) → (2,1) → poison alone
  - (1,3) → (2,2,2) → (3,2) → (2,2,1)
  - (1,4) → (3,2,2) → (2,2) → (3,1,1), or (3,1) → (3,2)
  - (2,1) → (4) → (1,2) → poison alone
  - (2,2) → (4,1,1) → (1,4) → (3,1,1)
  - (3,1) → (4,2) → (1,4) → (3,2)
  - (3,2) → (4,2,1) → (1,3) → (2,2,1)
- **Answer lists for the open problems.** K–1 P6 has 16 boards, and 2–3 P7 has 10 boards (or 5 inside 3×5); both are listed in the table above. A non-mathematician volunteer cannot check K–1 P6 without them.
- **Physical readiness.** Card size and placement, counters under an opaque card, and board spacing (A2) are untested and need rehearsal.
