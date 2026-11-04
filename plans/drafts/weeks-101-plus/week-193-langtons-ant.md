# Week 193 (draft plan): The ant that builds a highway

**Strand:** logic (Codes and logic), with a dynamics flavour. **Deep-math field:** cellular automata, reversible dynamics, open problems. **Status:** draft plan, November 2026. No student pages, guide, review card or pilot.

## The deep idea

Langton's ant (Chris Langton, 1986) walks on a grid of white squares. On a white square it turns right, on a black square it turns left; it flips the square's colour and steps forward one square. From an all-white grid it makes small, often symmetric patterns for a few hundred steps, then a large irregular blob, and then, near step 10,000, it starts a "highway": a 104-step cycle that moves it two squares diagonally each time, repeated forever (the check here finds the 104-step repeat from step 9,976 on; sources say 9,977, a matter of counting from 0 or 1). Proved: from every finite start, the ant's path is unbounded; it never stays in a bounded region. The proof is one children can follow in parts: the rule is reversible (from the picture and the ant's position and heading one can run it backward, so a bounded path would repeat and revisit every square forever), and the ant's moves alternate horizontal and vertical, so each square is always entered the same way; looking at the top-right-most square ever visited, its colour flips force the ant to turn the wrong way on a later visit. Sources credit this theorem differently: Gale's 1993 column credits X. P. Kong and E. G. D. Cohen; Boon (2000) cites Bunimovich and Troubetzkoy (1992); Wikipedia says the result was misattributed and calls it the Cohen–Kong theorem. Open: whether every finite start eventually builds a highway (every tested start has; no proof), and why the early patterns are symmetric. With grey squares added the unboundedness theorem fails (Cohen found a 52-step repeating path; cited from Gale). A single ant's path can compute any Boolean circuit (Gajardo and others, 2000). Children can discover the first steps (four steps go round a square back home), the alternation of horizontal and vertical moves, the run-backward trick, and, on a computer, the surprise of the highway.

## Sources

Every link was opened and read on the date given; nothing is cited from memory or from a search snippet.

- <https://ics-websites.science.uu.nl/docs/vakken/b2nb/stuff/The industrious ant - D. Gale - 1993.pdf> — David Gale, "The Industrious Ant", Mathematical Intelligencer 15(2), 1993 (read November 4, 2026). The rule, chaos for about 10,000 steps then the highway, the unboundedness theorem credited to Kong and Cohen with its proof idea (reversibility, alternating moves, a maximal cell), the open highway question, and grey squares.
- [How fast does Langton's ant move?](https://arxiv.org/pdf/cond-mat/0004331) — Jean Pierre Boon, arXiv cond-mat/0004331, 2000 (read November 4, 2026). The highway after "9977" steps, the 104-step period, and unboundedness credited to Bunimovich and Troubetzkoy.
- [Langton's ant](https://en.wikipedia.org/wiki/Langton%27s_ant) — Wikipedia, secondary pointer (read November 4, 2026). Langton 1986; the three phases; the open highway conjecture; the Cohen–Kong naming and misattribution note; Gajardo et al. (2000) on Boolean circuits.
- [Further Travels with My Ant](https://arxiv.org/pdf/math/9501233v1) — David Gale, James Propp, Scott Sutherland and Serge Troubetzkoy, arXiv math/9501233 (read November 4, 2026). Generalised ants, recurrent symmetry for some rule strings, and that the symmetric early patterns of Langton's ant await an explanation.
- Prior use with children: [Comprehension Task 1: Langton's Ant](https://www.mcsoxford.org/wp-content/uploads/2020/05/Comp-1-Langtons-Ant_Worksheet.pdf) — Tim Elton, 2020, a school worksheet (age not stated) (read November 4, 2026): students draw the board after steps 6 and 21. No K–5 use was found (searched "Langton's ant classroom activity students grid paper counters lesson").

## A kid-friendly way in

Be the ant. A floor grid of 7 by 7 paper plates, white side up, black (or red) on the back; one child is the ant, wearing an arrow card on their chest to show the heading. On white: turn right, flip the plate, step. On black: turn left, flip, step. The room calls out each move. At tables: the same on a 9-by-9 grid with two-colour counters and a toy ant with a nose. Children run 20 steps (the ant ends two squares diagonally from home, with 6 black squares) and draw the picture. Prep: 49 paper plates coloured on one side (or a printed floor sheet), table grids, counters and toy ants; about 25 minutes. Launch (3 minutes): the floor ant takes its first four steps; the room predicts the fifth step (it lands on a black square for the first time and turns left).

## By band

- **K–1:** Be the ant on the floor and on a table grid for the first 10 to 20 steps, taking turns. Do the first four steps come back home? Children play "turn and flip" with an adult reading the colour. No reading.
- **2–3:** Run 50 or 100 steps in pairs (one moves, one checks), photograph or draw the picture, then watch a computer run to 11,000 steps. What changes after about 10,000? Then the reverse game: a partner shows a picture and the ant; run it backward to the start.
- **4–5:** Why do moves alternate left-right and up-down? Why can you always run the ant backward? Follow the facilitator's story of why the ant can never stay in a box forever. Discuss the open question honestly: nobody knows whether every start makes a highway.

## Checked facts

All in `check_logic_3.py`, function `check_week_193()`, by simulation on an all-white grid (turn right on white):
- After 4 steps the ant is back at the start with 4 black squares.
- After 20 steps: 6 black squares, 11 squares visited, the ant two squares diagonally from home.
- Moves alternate horizontal and vertical for 12,000 steps.
- From step 9,976 on, every 104 steps shift the ant by 2 squares in each direction.
- Running the rule backward from step 500 returns to the empty grid, the start square and the start heading.
- Cited, not computed: unboundedness for every finite start (Gale; Boon); the open highway conjecture (Gale; Wikipedia); circuit construction (Wikipedia).

## Nearest existing themes

Draft Week 137 (The Game of Life) is a cellular automaton with whole-grid updates; the ant updates one square at a time and has a heading. Week 91 (Rotor-router machines) is the closest catalog relative: a counter follows an arrow and then turns it, and the rotor's evenness is proved; here the turning rule makes chaos and the main question is open. Week 72 (A robot that remembers area) has a robot on a grid with a memory strip; draft Week 138 (busy beaver) acts out a machine head on cups. Week 3 (Shuffle machines) undoes a machine by reversing its arrows, the same reversibility used here. No week or atlas family uses Langton's ant. New: a reversible rule whose long-run behaviour is observed but unproved, and a proof (unboundedness) that uses reversibility and alternation.

## App connection

Codes and logic region (or Chance and machines), possible family "Ant trails": a grid with the ant; children step, run, or run backward; a step counter and a black-square counter. Puzzles: "Where is the ant after 20 steps?"; "Here is a picture and an ant: run it back to the empty grid"; "Add one black square at the start: does the ant still build a highway?"; a fast-forward to 11,000 steps to watch the highway. Week 91's rotor art could share the arrow-turning animation.

## Open questions

- Will children keep track of heading on the floor, or does the ant need a clear arrow card and a "turn first, flip, then step" chant? Rehearse 20 steps with a real group of plates.
- Errors are not self-correcting: one wrong turn changes everything after it. A partner checker, or stopping at 20 steps, may be necessary.
- The highway needs a computer; decide whether a projector demonstration fits the circle.
- Settle the attribution of the unboundedness theorem from the original papers (Kong and Cohen; Bunimovich and Troubetzkoy 1992) before a guide names one.
