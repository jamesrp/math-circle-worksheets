# Week 191 (draft plan): Say what you see

**Strand:** logic (Codes and logic). **Deep-math field:** words and rewriting, growth rates, Conway's audioactive decay. **Status:** draft plan, November 2026. No student pages, guide, review card or pilot.

## The deep idea

The look-and-say sequence reads each row aloud to make the next: 1 is "one 1", so 11; then "two 1s", 21; then 1211, 111221, 312211, 13112221, 1113213211, and so on. Facts at child scale, all proved by short arguments: every row after the first has even length (it is a list of count-digit pairs); every row ends in 1 (the last digit is always the digit it describes); and starting from 1 no digit above 3 ever appears. The last is an argument children can follow: a count of 4 would need four equal digits in a row in the row before; in a reading of pairs, four equal digits in a row force two neighbouring pairs to describe the same digit, which a reading never does, since equal neighbours would have been counted together. So four equal digits never occur, counts never exceed 3, and the only digits are 1, 2 and 3 (checked here on 55 rows, where 333 also never appears). Conway's results (J. H. Conway, "The weird and wonderful chemistry of audioactive decay", Eureka 1986 and a 1987 book chapter): rows eventually split into 92 "elements" (named Hydrogen to Uranium) that evolve without touching each other; the Cosmological Theorem says every starting string except the empty one and 22 splits, after at most 24 steps, into common elements and two families of "transuranic" ones. Conway and Parker's proof and Guy's proof were both lost; Ekhad and Zeilberger gave a computer-assisted proof (1997) and Litherland one with the sharp bound 24. Row lengths grow by Conway's constant λ ≈ 1.303577, the only positive real root of a degree-71 polynomial, for every start except 22 (proved, via the 92-element matrix). The row lengths 1, 2, 2, 4, 6, 6, 8, 10, 14, 20, 26, 34, … and the ratio 1.3037 at row 55 are checked here. Children can discover the rules (even lengths, last digit, no 4), the fixed point 22, the never-ending last digit of other starts (from 4, the 4 stays at the end alone forever), and which strings can be readings at all: 1111 is never a reading, since "one 1, one 1" would have been said "two 1s".

## Sources

Every link was opened and read on the date given; nothing is cited from memory or from a search snippet.

- [Look, There's More to Say about Conway's Look and Say Sequence](https://arxiv.org/html/2405.11103v1) — Gregory P. Dresden and Jacob Siehler, arXiv 2405.11103 (2024) (read November 4, 2026). Conway's 92 elements; the lost proofs by Conway and Parker and by Guy; the computer-assisted proof by Zeilberger, improved by Litherland; λ = 1.303577…, the positive root of a degree-71 polynomial.
- [Conway's Cosmological Theorem](https://oeis.org/A005150/a005150_3.pdf) — R. A. Litherland, Louisiana State University, 2003, revised 2006 (read November 4, 2026). The theorem with N = 24 steps, Guy's atoms showing 24 is sharp, Ekhad and Zeilberger's N = 29, the 92 common elements and the transuranic families.
- [Look and Say Sequence](https://mathworld.wolfram.com/LookandSaySequence.html) — Eric Weisstein, MathWorld (read November 4, 2026). λ ≈ 1.303577269, the same for every start except 22; Conway's Eureka 46 (1986) and 1987 references; Ekhad and Zeilberger's 1997 proof.
- Prior use with children: [Diseño e implementación de tareas de alta demanda cognitiva basadas en la sucesión look and say](https://dialnet.unirioja.es/descarga/articulo/8189998.pdf) — Víctor Manero, José M. Muñoz-Escolano and Antonio M. Oller-Marcén, AIEM 20, 2021 (read November 4, 2026): task sets for 15- and 16-year-olds in a mathematical-talent workshop (computing terms, conjecturing long-run behaviour, finding predecessors). No K–5 use was found (searched "look and say sequence math circle elementary students activity").

## A kid-friendly way in

Read rows aloud with cubes. A row is a line of snap cubes in three colours (or digit cards 1, 2, 3). To make the next row, a child says the row out loud in runs ("two reds, one blue") and builds what they said: a 2-card then a red cube, a 1-card then a blue cube. With digits only, children read "one one" and lay down 1, 1; then "two ones": 2, 1. Each table builds rows on a long paper strip, one row per line, and pools results on a wall chart. Prep: digit cards 1 to 3 (about 60 per table) or printed digit strips, a long sheet per table; about 15 minutes. Launch (2 minutes): the whole room chants the first five rows from 1 together, an adult writing each on the board.

## By band

- **K–1:** Say-and-build with cubes from "1" for five or six rows, then from a two-colour start. Is any row the same as the one before? (22 is.) Count the cards in each row with cubes. No reading.
- **2–3:** Continue from 1 for ten rows, sharing the work in pairs, and look for rules: which digits appear, how rows end, which row lengths occur. Try other starts (3, 22, 4) and predict what stays.
- **4–5:** Explain why a 4 can never appear from the start 1, and why every row ends in 1. Play the game backward: which strings are the reading of some row (1211 is, 1111 and 111 are not)? Find the row before 312211. Growth: compare each row's length with the one before and watch the ratio settle near 1.3.

## Checked facts

All in `check_logic_3.py`, function `check_week_191()`:
- The first eight rows from 1 and the lengths 1, 2, 2, 4, 6, 6, 8, 10, 14, 20, 26, 34.
- On 55 rows: digits only 1, 2, 3; no four equal digits in a row; no 333; every row ends in 1; even length from row 2.
- Length ratio of row 55 to row 54 within 0.01 of 1.3036 (it is 1.3037).
- 22 reads to 22; from 4, the single 4 stays at the end for 12 rows; 3 gives 13 then 1113.
- 1111, 111 and 0211 are not readings of any row; 1211 and 3112 are; every row from 1 is a reading.
- Cited, not computed: the 92 elements, the Cosmological Theorem with N = 24, λ as a root of the degree-71 polynomial (Litherland; Dresden and Siehler; MathWorld).

## Nearest existing themes

Week 76 (Substitution strips) and draft Week 144 (The MU puzzle) are the closest: rule-driven rewriting of words, with an invariant that bans some strings (AAA in Week 76; a count mod 3 in 144). Look-and-say is a different kind of rule (it reads runs, so a row's length can grow or shrink) and its ban (no 4) comes from the reading itself. Week 17 (Machine memory) reads words with machines. Draft Week 154 (Bulgarian solitaire) shares the "repeat a rule and watch what settles" format. No catalog week, atlas family or scouting draft uses look-and-say. New: run-length reading, a self-describing growth rule, and a famous growth constant children can watch emerge.

## App connection

Codes and logic region, possible family "Say it again": a row of coloured beads; the child drags count tiles and bead colours to build the next row, and the app checks it. Puzzles: "Build the next three rows from 1"; "Find a row that never changes" (22); "Which row came before 312211?"; "Can this strip ever appear?" (1111, no). Week 76's "Shrink strips" could share the strip interface, run backward.

## Open questions

- Is saying a row aloud reliable for K–1 children once rows pass eight digits? A finger or a sliding window card may be needed; keep K–1 to the first six rows.
- How much of the elements story to tell: perhaps only the fact that rows split into pieces that never touch again, shown with one example split from the guide.
- Whether the backward game (finding parents) is the strongest 2–3 task, since it is checkable without long rows.
- Transcription errors compound quickly; a pair check after each row may be needed.
