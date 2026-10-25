# Review: facilitator guide for "Breaking and drawing games" (draft/facilitator.pdf, 6 pp.)

What I read: the guide (rendered at 80, 110 and 250 dpi) and its source (`facilitator.tex`, `solutions.tex`); all 23 final student pages (K–1 7, Grades 2–3 7, Grades 4–5 9), rendered and read, with zoomed crops of the Problem 11 drawings and the Brussels Sprouts rule pictures; the outline; both page reviews; the drafts README entry; `worksheet-workflow/context.md`; and the Week 98 model guide. I also checked the JRMF Sprigs guide and the Wikipedia Sprouts article online.

My own checks are in `review-guide-check/`, with output in `review-checks.out`:

- `planar_games.py` and `run_games*.py` are an independent face-and-boundary engine with exhaustive search. It finds these lengths:
  - 2-Sprigs, 1–6 dots: only n.
  - 3-Sprigs: 2 dots {3}, 3 dots {4}, 4 dots {5, 6}, 5 dots {6, 7}. This matches the JRMF table.
  - Sprouts: 1 spot {2}, 2 spots {4, 5}, 3 spots {6, 7, 8}, 4 spots {8–11}. With best play the 2nd player wins with 1 or 2 spots, and the 1st player wins with 3 or 4.
  - Brussels Sprouts: 1 cross {3}, 2 crosses {8}, 3 crosses {13}.
- `sequences.py` replays every game the guide prints, one of my own, and a counterexample to the guide's strategy (finding M1).
- `bars.py` covers every break order for every printed bar, the last-break-wins outcomes, the K–1 Problem 8 groups as breakable pieces, and the stacking bound.

All printed numbers are right. Every problem number, page number, board size (91 × 96 mm with spots 44 mm apart on Grades 4–5 page 5; spots 84 mm apart on Grades 2–3 pages 5–6), bar list, square count (74, 56 and 58 per pair; 41 bars and 345 squares in all), cut count (54, 49 and 41 per pair) and page total (83) matches the final PDFs and the current group of 11. The build has no box warnings.

## Must fix

**M1. The guide's recipe for the longest Sprouts game is false, and Grades 2–3 Problem 8 has no example 8-move game (p. 1 Sprouts paragraph; p. 5 Grades 2–3 Problem 8; p. 5 Grades 4–5 Problem 7).**

The overview says "Cooperative play reaches this by never shutting a spot that has a token into a region alone". Grades 2–3 Problem 8 says "An 8-move game exists: never shut a spot that has a token in alone."

Following that rule does not guarantee 3n − 1. Counterexample with spots A, B and C:

1. A–B (new spot D).
2. A–B again, round C, so that C lies inside the ring A–D–B–E (new spot E).
3. D–E on the side of the ring away from C (new spot F).

After each move, every spot with a token still shares a region with another spot that has a token, so no spot is shut in alone. Yet `sequences.py` shows that every continuation ends at 6 or 7 moves. F is cut off from C, so the game finishes with at least two tokens left.

The property that actually works is the one the math review stated and Grades 4–5 Problem 7 half-states: keep every spot with a token on the edge of one region. The adult also needs a concrete 8-move game to check a child's game against.

Fix:
- In the overview, replace the sentence with: "Cooperative play reaches this by keeping every spot with a token on the edge of one region: join two such spots that are next to each other along that edge, or loop a spot without enclosing any other spot that has a token."
- In Grades 2–3 Problem 8, give the witness instead of the recipe: "A–B (D); B–C (E); A–C (F), which closes a ring; then, all on one side of the ring, A–D (G), G–B (H), H–E (I), I–C (J), J–F (K); only K keeps a token." `sequences.py` verifies it: 8 moves, the game is over, and 1 token is left.
- In Grades 4–5 Problem 7, put the "one region" clause first and drop "never shut a spot with a token in alone" as the leading rule.

## Should fix

**S1. The overview's opening claim does not fit Brussels Sprouts (p. 1, first paragraph).** "Three games here have it because a count changes by the same amount every move and the game cannot stop until the count runs out." No such count appears in the Brussels argument that follows: free arms stay at 4n, and the proof works from the forced final shape plus Euler's formula.

Fix, either:
- name the count: "regions minus separate pieces of the drawing rises by exactly one each move, from 1 − n to 4n − 1, so 5n − 2 moves"; this is Euler's formula one move at a time; or
- reword: "Bars and 2-Sprigs have such a count. Brussels Sprouts has a forced final shape, and Euler's formula turns that shape into a move count."

**S2. The Brussels connectivity step is too compressed for an adult to follow (p. 1).** The current text is "(The finished drawing is in one piece, since (2) holds for each separate piece of a region's edge.)" Fix: "Each separate piece of a region's edge always keeps a free arm pointing into that region. A finished region holds only one free arm, so its edge is in one piece, and therefore the whole drawing is in one piece."

**S3. The 2-Sprigs launch demonstrates a different action from the one used at the tables (p. 2, launch and figure).** At the launch, token circles are drawn on the board and "a child erases one token at each end". At the tables, the partner removes beans, and the guide passes counters round but never uses them in this demonstration. AGENTS asks the launch to show the concrete action everyone will use.

Fix: run the seven-dot demonstration with real counters on a sheet on a table, or on a whiteboard with magnets. Have one child draw while a second child, acting as the partner, removes the tokens. Keep the four-panel figure as the adult's reference.

**S4. Spare bars mentioned in the solutions are not counted, and the grid card has no named source (p. 2 "Per pair" and "Print and prepare"; p. 3 K–1 Problems 1, 2 and 8; p. 4 Grades 2–3 Problem 2).**
- K–1 Problem 1 says to "break a spare bar with the adult watching".
- The K–1 Problem 2 hint says "Try it on the spare bar". The only spare is the 3×4 already set aside "for a second try".
- K–1 Problem 8 says to check "by breaking a spare bar into the same pieces". That takes another 2×3, 3×3 and 3×4.
- Grades 2–3 Problem 2 expects shortcut attempts ("three strips first") but has no second 3×4.
- "Card stock printed with 1-inch grid" leaves the volunteer to find a grid.

Fix:
- Add a small table spare pool, for example one 3×4, one 3×3 and one 2×3 for each of the K–1 and 2–3 tables.
- Recount the bars, squares, sheets and preparation time.
- Name the grid: a 1-inch graph-paper PDF printed on card stock at 100%. Alternatively, report to the organizer that the packet lacks a bar sheet; do not change the pages.

**S5. K–1 cutting and adult preparation have no fallback (p. 2, Status, Per pair, Staffing).**
- The K–1 first route needs about 54 cuts of card stock per pair, roughly 27 per child, with child scissors, in about 25 minutes. Kindergarten scissor skill on card is the likeliest bottleneck.
- The adult preparation is 40–50 minutes, against the outline's 10–15. The guide does not say who does it, and the K–1 adult is the parent volunteer.
- The guide marks both as untested but offers no plan if they fail.

Fix:
- Add to Staffing: "If cutting is slow, the child points to the line and the partner or adult cuts; the child still chooses every break."
- Name a lower-preparation route: cube slabs for K–1, or for every replayed bar.
- Say who prepares the bars, for example the organizer, so the parent volunteer does not cut 41 bars alone.

## Minor

- **m1 (p. 4, K–1 Problem 8).** "(from a 2×3, a 3×3 and a 3×4 bar)" is not forced: groups 2 and 3 could also come from a 1×9, 1×12 or 2×6 bar (`bars.py`). The answer pieces − 1 does not depend on the bar. Write "for example from…".
- **m2 (p. 1, Sprouts).** "loop-then-join play (Grades 4–5 Problem 7)": the page does not contain this play. Write "(see the Grades 4–5 Problem 7 solution)".
- **m3 (p. 2).** "Flat slabs of interlocking cubes, about 12 per pair" could mean 12 slabs. Write "12 cubes per pair, enough for one 3×4 slab at a time".
- **m4 (p. 1, map of the bands).** No Grades 4–5 prerequisites are given. Add, for example, "reads the rule paragraphs; multiplies 8×13 and 25×40".
- **m5 (p. 5, Grades 4–5 Problem 8).** "Wikipedia gives the argument" for the 2n lower bound overstates it: the article only sketches it, mentioning survivors with two dead neighbours and "pharisees". Either write "Wikipedia sketches it; Winning Ways ch. 17 has the argument (not consulted)", or drop the pointer.
- **m6 (p. 6, Sources).** "The proofs for 2-Sprigs and Brussels Sprouts … are ours." The 5n − 2 Euler argument is classical (Gardner, ch. 1). Write "written out by us".
- **m7 (p. 5, Grades 4–5 Problem 5 hint).** "Start at a dot with one token and follow its lines" prescribes the route of the proof. A question keeps the hint lighter: "What do you know about a dot that has only one token left?"
- **m8 (p. 2, Staffing).** "The adult … runs the cup": let the partner drop the counters, as the page says ("Drop a counter in the cup"), so the record stays with the children.
- **m9 (p. 3, return visits).** Say which Grades 2–3 first route is preferred. The outline's point is the contrast with Sprouts, and the default first hour leaves Sprouts out.
- **m10 (brevity).**
  - K–1 Problem 4: in "A game is over when no line can be drawn; when every token is gone nothing more can be drawn", the second half adds nothing.
  - Grades 4–5 Problem 9's slip list could also name "a line that crosses itself", which is the slip the page review found.

## The overview and the launch against AGENTS

- **Overview.** It is theorem-first and comes before any solution. It states each fact with its assumptions and limits:
  - one piece per break, with the stacking contrast;
  - the two printed clarifications that make 2-Sprigs fixed, and 3-Sprigs, where the length varies;
  - Sprouts as a bound rather than a fixed length.

  The 2-Sprigs proof is complete and an adult can follow it. It separates experiments, conjectures and explanations and maps all three bands. Apart from M1, S1 and S2 it meets the rule.
- **Launch.** It is brief and concrete. It uses non-task instances (the 2×5 bar, seven dots, and four-spot or four-cross scrap boards, none of which appear on any page). It stops before finishing or counting the bar and gives away neither the theorem nor an answer. The only gap is S3.

## What works and should be kept

- Every answer, list and length is correct and independently confirmed, including the Problem 11 counts (5, 4, 1; 4, 5, 3; 2, 3, 3; 4, 6, 4) and the finished-game Euler checks 4 − 6 + 4 and 10 − 16 + 8.
- The source note corrects the outline: JRMF pp. 4–5 give 3-Sprigs counts, and 2-Sprigs "ends in n moves" appears on p. 4 without proof. I verified this against the PDF online.
- The K–1 "Key in plain words for the adult" suits the parent volunteer.
- The rule "adults do not announce winners or name the rule; an adult choosing breaks or lines means the board is too big" keeps the mathematical choices with the children.
- The spare counter for the starting player, and circling the seat rather than a name.
- The honest status paragraph, which lists exactly what is physically untested.
- The first-hour routes and return visits for each band, and the closing share questions.
- The worked 1-spot, 2-spot and loop-then-join Sprouts games.
- The 3-Sprigs and stacking extensions, which show where each theorem stops.
- The length of 6 pages, which is in line with the model guides.
