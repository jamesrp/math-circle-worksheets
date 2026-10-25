# Week 63 return visit, draft v1: mathematical review

Reviewer: independent math check (CRITIC-MATH stage). I did not edit the draft.

## How I checked

- I regenerated all three `.tex` files from `draft/src/build.py` into a scratch folder. They are byte-identical to `draft/src/*.tex`, so the PDFs match the sources.
- I parsed the TikZ sources rather than trusting `build.py`. From them I extracted every printed card row, every crossed-out card above every home (mapped to its home by coordinates), and every shaded grid square and dot (mapped to card line and home column). I then recomputed every answer by brute force:
  - fewest swaps by breadth-first search over swaps of any two cards (n ≤ 6), checked against n minus the number of loops;
  - exactly-m reachability for m ≤ 7;
  - home-match totals, totals per letter, pairs, and exact piles for n ≤ 7;
  - all C(16, 4) = 1820 four-spot boards on four cards;
  - every printed forbidden board and grid by enumeration and by its alternating rook-number sum.
- I rendered every page and inspected each diagram, with a zoomed check of the arrow directions on the 4–5 Problem 3 worked example.

Everything below that is not listed as a problem was confirmed correct, including all 23 printed rows and their fewest-swap answers, the two U–X swap demonstrations (VUWX, swap VX, gives XUWV), all 13 forbidden boards and 6 grids, and every intended count:

- fewest swaps 2, 2, 3 (no swap sequence of exactly 2 empties all five homes, and AB, CD, AE gives BEDCA);
- hardest rows 3 for four cards and 4 for five, with 24 five-card rows needing 4 and 20 of the 44 home-free rows needing 3;
- BACDE comes home in exactly 1, 3, 5, 7 swaps and BCADE in exactly 2, 4, 6;
- marks 6, 24, 120, two per letter on A–C and six per letter on A–D;
- pairs 12 and 60;
- piles 9, 8, 6, 0, 1 and 44, 45, 20, 10, 0, 1;
- forbidden-board counts: 1, 3 and 1 (K–1 boards); 9, 7, 4, 0 (2–3 boards); 1, 3, 16 (strip rule) and 2, 13 (ring rule);
- the grids give 3, 16, 2, 13, and the worked-example row VXUW obeys its own example shading.

## Band verdicts

- **K–1:** one wording problem (Problem 5). Everything else checks out.
- **Grades 2–3:** one problem (Problem 9). Everything else checks out.
- **Grades 4–5:** checks out completely. I found no mathematical errors, diagram mismatches or misleading readings.

## Located problems

### 1. K–1, page 4, Problem 5: both questions leave out the correct answer

Text: "Put a counter on every card at home on the six A–C outcome cards. Are there more counters or more outcome cards? Which letter has the most counters?"

Evidence: the six rows ABC, ACB, BAC, BCA, CAB, CBA carry 3, 1, 1, 0, 0, 1 home cards. That makes 6 counters on 6 outcome cards, with A, B and C each getting exactly 2: A in ABC and ACB, B in ABC and CBA, C in ABC and BAC. The intended outcome, "6 and 6, two per letter", is a tie in both cases. Both questions offer only unequal answers ("more counters or more outcome cards", "the most"). Read aloud once to a kindergartner, they suggest that one side must win. A child who correctly finds a tie may decide they made a mistake, or may pick a side.

Smallest fix: "Are there more counters, more outcome cards, or the same number? Does any letter get more counters than another?" The answer boxes can stay as they are.

### 2. Grades 2–3, page 6, Problem 9: the "as few as possible" half is already answered by Problem 8, and the "as many" half has its answer printed there too

Text: "Cross out four cards above these homes so that as many of the 24 outcome cards as possible obey the board. Then cross out four cards on another board so that as few as possible obey it."

Evidence: I enumerated all 1820 ways to cross out four card-in-home spots on four cards. The obeying counts that occur are exactly 0, 4, 6, 7, 8 and 9. There are 8 boards giving 0, 324 giving 4, 384 giving 6, 576 giving 7, 504 giving 8 and 24 giving 9.

- **Minimum, 0:** this is reached by crossing out the same card above every home, or all four cards above one home. The fourth board of Problem 8, on the page just before, is exactly "A crossed out above every home". Children have just counted that board as 0 obeying cards, and 0 is plainly the least possible. On a menu that shows all four cards above each home, crossing out a whole column is also the obvious first move. So this half takes no experimenting.
- **Maximum, 9:** this is reached by exactly the 24 boards with one crossed card per home and per card. The first board of Problem 8 (own homes, 9) is one of them, so a child can copy it without searching. The half is still true and worth keeping, because confirming that nothing beats 9 takes real trying. It is just less open than it looks.

Smallest fix: keep the first sentence and replace the second with a target that needs search and whose answers are not on Problem 8. For example: "Then, on the other boards, cross out four cards so that exactly 8 outcome cards obey, and so that exactly 6 obey. Can four crossed-out cards leave exactly 5?" Verified answers:

- 8 obey: A-in-A, B-in-B, D-in-C, D-in-D (also A-in-A, B-in-B, C-in-C, D-in-C);
- 6 obey: A-in-A, B-in-B, D-in-A, D-in-B;
- 5 is impossible, because no four-spot board gives 1, 2, 3 or 5.

This keeps the problem's point, that the number of forbidden spots does not decide the count, and needs no new diagram. A lighter alternative is to drop the second sentence and use the spare boards as extra workspace for the maximum.

## Not problems (checked, recorded so the reviser need not re-check)

- The recording spaces outnumber the answers on every "find every way" task (K–1: 3 slots for 1, 5 for 3, 3 for 1; 4–5: 2 for 1, 4 for 3, 18 for 16, 4 for 2, 15 for 13). No page states or implies a count, so this is spare room, not a wrong total.
- 4–5 Problem 1 records three- and four-card attempts in five-cell A–E records. This is a format question, not a mathematical one.
- 4–5 Problem 5's "exactly 4" for BCADE is reachable only by including at least one move that is not on a shortest route, such as swapping the same pair twice. The shared rules allow this, because "any two cards" means two distinct cards and no self-swap exists, so the parity answer is as intended.
- 4–5 Problem 10's "using homes A to C" leaves C's crossed-out picture above the covered home D. It cannot affect the count, because home D is unused.
