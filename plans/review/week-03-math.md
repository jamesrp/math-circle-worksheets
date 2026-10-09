# Week 3 (shuffle machines): math check

Scope: `lowell-math-circle-year-2/week-03/week-03-k-1.pdf` (F03-K-v5, 10 pp., Problems 1–8), `week-03-grades-2-3.pdf` (F03-M-v5, 11 pp., Problems 1–8), `week-03-grades-4-5.pdf` (F03-U-v5, 8 pp., Problems 1–10) and `week-03-facilitator.pdf` (F03-FAC-v5, 10 pp.). Sources: `lowell-math-circle-year-2/source/week-03/src/` (`k-1.tex`, `grades-2-3.tex`, `grades-4-5.tex`, `figures.py`, `machines.py`) and `guide-src/facilitator.tex`. I did not use the packet's own `figures.py` assertions or `guide-src/check_answers.py`. The return visit (`week-03-return-visit.pdf`, W03-RV-v1, 3 pp., with `week-03-return-visit-facilitator.pdf`, F03-RV-FAC-v1, 4 pp.) is a companion and was checked only briefly (last section). The archive folders were not checked. My scripts and their outputs are in [checks/week-03/](checks/week-03/). Checked October 9, 2026.

**Result: every answer in all three bands is correct, and every problem can be done as stated. Every printed machine matches its text and the guide. The guide's answers, cube rows, examples, counts and mathematical overview are all correct. I found one problem, a minor one in the guide's materials notes: it sends the 6- and 7-slot machines to a 5-slot test mat (item 1).**

## How it was checked

- `pdfmats.py` reads every mat straight from the vector drawings of the final PDFs. It finds the slot squares, pairs each top row with the row below it, and reads each arrow from its start dot to its end. It checks that the arrowhead tip sits over the same bottom slot and touches it, that no slot sends or receives two arrows, and which picture is above each top slot. `dump_mats.py` lists all 120 mats (output `dump_mats.out`): 48 printed machines (7 in K–1, 12 in 2–3, 18 in 4–5, 11 in the guide) and 72 blank mats or recording rows.
- `check_week03.py` (output `check_week03.out`) recomputes every answer without cycle formulas. It moves block labels turn by turn and finds every undo machine by searching all machines. It finds every "A then B" by running blocks through both machines, and does every perfect shuffle by interleaving card lists. Return-time sets and records come from searching every machine up to 8 slots, and from loop splits for 9 and 10. It compares 120 results with the pages and with the guide's printed answers, which I transcribed by hand. It found 0 mismatches. It also:
  - reads every coloured cube row printed in the guide from the PDF (`guide_rows.py`, output `guide_rows.out`) and matches all 13 answers against rows computed from the student mats. No printed row is left unmatched.
  - measures the geometry. Every slot is square, every green triangle is equilateral and every yellow hexagon is regular (all within 1%). Slots are 1.2 in on the cube mats (1.15 in on the 6-slot mats).
  - checks legibility. Arrowheads sit at most 0.24 slot-widths from the centre of their slot. The shallowest crossing is 12° (4–5 p. 1, second machine, arrows from slots 1 and 2), and arrow ends clear other arrows by at least 0.13 slot-widths. All of this reads clearly at print size.
- The delivered machines are the ones the sources define (`figures.py`'s `P(...)` calls), so source and PDF agree. pdfLaTeX is not installed here, so I did not test a clean rebuild.

Machines below are written as arrow targets for slots 1, 2, 3, …: [3, 1, 2] means 1→3, 2→1, 3→2.

## K–1: checks out completely

- **P1:** [3, 1, 2] takes 3 turns; [1, 3, 2] takes 2 turns.
- **P2:** [3, 4, 2, 1] takes 4 turns (one loop of 4); [3, 4, 1, 2] takes 2 turns (green–red and blue–yellow swap).
- **P3:** [2, 4, 3, 1] takes 3 turns (red stays). [3, 4, 1, 5, 2] takes 6 turns: green and red are home at 2 and 4, blue, yellow and purple at 3, everything at 6.
- **P4:** all three targets are possible on 4 slots. There are 9 machines taking 2 turns, 8 taking 3 and 6 taking 4. Read with P1's "do turns until every block is back", a turn count is the first time all are home, so straight arrows do not count as a 2-turn machine. The partner's check with blocks settles it.
- **P5:** impossible. No machine on 1–7 slots moves exactly one block, and the answer stays "no" if the question is read as "after several turns", since repeating a machine still gives a machine.
- **P6:** after one turn of [4, 3, 1, 2] the row is red, yellow, blue, green. The only machine that sends it home is [3, 4, 2, 1], the first machine with its arrows reversed.
- **P7:** 6 machines; nine mats are printed, so the page does not give the count away.
- **P8:** 20 five-slot machines take 6 turns, all with loops of 2 and 3; 19 differ from Problem 3's.

## Grades 2–3: checks out completely

- **P1:** [4, 2, 1, 3]: blocks home after 3, 1, 3, 3; all after 3. [3, 5, 4, 1, 2]: 3, 2, 3, 3, 2; all after 6.
- **P2:** [2, 5, 1, 4, 3] → 4; [4, 3, 6, 1, 2, 5] → 4 (loops 2 and 4); [4, 1, 6, 2, 3, 5] → 3 (loops 3 and 3); [5, 6, 3, 1, 4, 2] → 6 (loops 3, 2, 1). At most 3 loops on one machine, so three colours per child suffice.
- **P3:** every number from 1 to 6 is possible with 5 slots.
- **P4:** the rows after one turn are red, green, yellow, blue and blue, purple, yellow, red, green. Each undo machine is unique: [3, 1, 4, 2] and [2, 5, 4, 3, 1]. Each takes the same number of turns as the machine it undoes (4 and 6).
- **P5:** 26 five-slot machines undo themselves (1 with no swap, 10 with one swap, 15 with two). A machine undoes itself exactly when every loop has 1 or 2 slots (checked on all 120).
- **P6:** page 8 (swaps 1–2 and 2–3): blue, red, green, yellow and red, green, blue, yellow, which differ. Page 9 (swaps 1–3 and 2–4): red, yellow, green, blue both ways.
- **P7:** 6 slots allow exactly 1–6 turns, and eight mats are printed for six answers.
- **P8:** only loops of 3 and 4 give more than 10 turns (12), and 12 is the most on 7 slots. The 7-slot return times are 1–7, 10 and 12.

## Grades 4–5: checks out completely

- **P1:** [3, 2, 5, 1, 4]: 4, 1, 4, 4, 4; all after 4. [5, 4, 1, 2, 3]: 3, 2, 3, 2, 3; all after 6.
- **P2:** 3, 6, 10, 7, 6, 4 (top left to bottom right), with loops (1 3 5)(2 6 4), (1 5)(2 3 6)(4), (1 4 7 2 5)(3 6), (1 4 2 7 3 5 6), (1 3 2 5 7 6)(4 8), (1 3 6 8)(2 5 7 4).
- **P3:** 1–6, with nine mats for six answers.
- **P4:** the most is 6 for 6 slots (one loop of 6, or 3 + 2 + 1) and 12 for 7 slots (4 + 3 only).
- **P5:** interleaving gives A, 5, 2, 6, 3, 7, 4, 8 as printed. The shuffle counts are 4 cards → 2, 6 → 4, 8 → 3, 10 → 6 and 12 → 10. The 8-card machine is [1, 3, 5, 7, 2, 4, 6, 8], with loops (2 3 5)(4 7 6). A child who draws the arrows backwards gets the same loops and the same 3.
- **P6:** pair 1: A then B is [3, 1, 2, 4] and B then A is [2, 3, 1, 4]. Pair 2: [2, 1, 4, 3] both ways. Pair 3: [3, 4, 1, 2] and [2, 1, 4, 3].
- **P7:** pair 1: A then B = [4, 2, 1, 3], undo A = [3, 1, 2, 4], undo B = [1, 3, 4, 2], undo (A then B) = [3, 2, 4, 1]. Pair 2: [3, 1, 4, 2], [2, 1, 3, 4], [1, 4, 2, 3], [2, 4, 1, 3]. In both pairs "undo B, then undo A" works and the other order fails, so the page separates the two rules.
- **P8:** among the 9 machines that move all four blocks there are 12 commuting pairs, so the task is possible.
- **P9:** 1, 2, 3, 4, 6, 6, 12, 15, 20, 30. Search of every machine confirms the values up to 8 slots. No: 6 slots do no better than 5, and that is the only step from 1 to 10 slots with no gain.
- **P10:** 8 shuffles. Physically interleaving 52 cards gives six loops of 8, the loop (18 35), and the top and bottom cards fixed.

## Adult guide

All answers, hints, examples and "watch for" notes are correct for all 26 problems. That includes the 13 printed cube-row answers, the 11 example mats (K–1 Problems 4, 6 and 7) and the 4–5 pair counts (3 + 3 + 6 = 12). The launch is also correct: the chair rows, "green and blue home after 2, the rest after 3, everyone after 6", and the floor drawing, which does draw 1→2, 2→1, 3→5, 5→4, 4→3 without crossings. So are the materials arithmetic (25 + 30 + 20 = 75 cubes, 14 of each of five colours and 5 pink) and the pattern-block sizes. Pink appears only on the 6-slot mats of 2–3 Problem 2, as stated.

The overview (Sections 1 and 5) states its facts with the right hypotheses. Loops split the slots. The return time is the lcm of the loop lengths. The return-time sets are right for 5, 6 and 7 slots. Landau's g(n) never decreases, can stay level, and satisfies log g(n) ~ √(n log n). Inverses keep the cycle type, and the inverse of "A then B" is "undo B, then undo A". Involutions number 26 on 5 slots. The out-shuffle order is the order of 2 mod 2m − 1, and the in-shuffle needs 52 for 52 cards. Elmsley's rule holds: the script checked every target position 1–51 by shuffling.

### 1. The test mat cannot run the 6- and 7-slot machines (pp. 2 and 5)

- **Quoted text:** p. 5, grades 2–3: "The small mats (Problems 3, 5, 7, 8) are too small for cubes: run a drawn machine on a spare K–1 page 9 test mat, or trace it with a finger." p. 2, materials table: "Test mats … Extra copies of K–1 page 9 (a blank 5-slot mat with pictures): 2 for the 2–3 table, 2 for the 4–5 table, to run machines drawn on the small mats."
- **Evidence:** `dump_mats.out` shows that K–1 page 9 is a single 5-slot mat. The small mats of 2–3 Problem 7 have 6 slots and those of Problem 8 have 7. The 4–5 Problem 4 mats have 6 and 7 slots. A 6- or 7-slot machine cannot be run on a 5-slot mat. The cube sets also fall short: 6 colours per child at 2–3 and 5 at 4–5 (guide p. 1), so 7 distinct cubes are not available. Only the finger-tracing fallback works for those problems. The 5-slot (2–3 Problems 3 and 5, 4–5 Problem 3) and 4-slot (4–5 Problems 6–8) machines do fit the test mat. Severity: minor, because the same sentence offers finger tracing and nothing on a student page depends on it.
- **Smallest fix:** p. 5: "The small mats are too small for cubes. Run a drawn 5-slot machine (Problems 3 and 5) on a spare K–1 page 9 test mat; trace the 6- and 7-slot machines of Problems 7 and 8 with a finger." p. 2: "… to run 4- and 5-slot machines drawn on the small mats."

## Return visit (companion, brief check): checks out

Every number the companion guide gives is right:
- **Problem 1:** the rows 21354, 31425 and 53421 need 2, 3 and 9 neighbour swaps by breadth-first search. The hardest five-card row needs 10, and the inversion count equals the swap distance for all 120 rows.
- **Problem 2:** from 1234 the moves reach 8 orders (10 from 12345). 3412 and 2143 can be made; 1324 and 2413 cannot.
- **Problem 3:** each printed root gives the stated intermediate and final rows, and output 213 has no root. 3, 12 and 270 targets have roots on 3, 4 and 6 slots. The answers do not depend on reading an output row as a card list or as an arrow list, because a machine and its reverse have the same loop sizes.

The cut-out cards and the working-mat squares measure 25 mm, as the guide says.
