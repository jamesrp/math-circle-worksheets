# Review of the facilitator guide: Who beat whom (draft, 7 pages)

Reviewed: `draft/facilitator.pdf` and `draft/src/facilitator.tex`, against the final student pages `k-1.pdf` (5 pp., 10 problems), `grades-2-3.pdf` (6 pp., 9 problems) and `grades-4-5.pdf` (8 pp., 13 problems). I also read the outline, both page reviews, the drafts README entry and the Week 98 model guide. I rendered every page of the guide and of all three packets and read them.

## Verdict

The guide is close to ready. Every answer it prints for a printed picture is correct, every problem and page number matches the final PDFs, and the launch, staffing and pacing follow AGENTS.md. Three statements are false and must be fixed: the proof idea for the "passing list always happens" half of Landau's theorem, and two remarks about the pictures in grades 2–3 Problem 7. Each fix is a sentence or two. The rest is usability polish.

## How I checked

Scripts are in `review-guide-check/`:

- `parse_figs.py` reads each figure file of the final pages (`plans/topic-scouting/drafts/who-beat-whom/src/figs/*.tex`) and works out who beat whom from the geometry alone: circles and labels, link segments, and the direction from notch to tip of each arrowhead polygon. It does not use the writer's or the page author's specs. I compared several parsed pictures with the rendered pages by eye; they agree.
- `check.py` computes the line-ups (Hamiltonian paths), wins, kings, possible first players and the places where X can join, for every printed tournament.
- `general.py` enumerates every labelled tournament on 3–6 players. It confirms the line-up counts, king counts, oddness, "unique line-up exactly for a ranking", "a top scorer is a king", and the first-player criterion (checked up to 5 players). It also confirms the four-player shape table (24/16/24 boards; 1/3/3/5 line-ups; 1/1/3/3 kings), that the only five-player win list with four kings is 1,2,2,2,3, and the printed P9/P10 numbers (read top first, then clockwise) together with their Landau verdicts. Finally it lists the possible sorted win lists (4, 9, 22) and the lists that have the right total but cannot happen.
- `constructions.py` checks every tournament the guide builds: the K–1 P5 and P6 examples (including all four diagonal choices), and the 4–5 P9 and P10 constructions.
- `landau_moves.py` tests the overview's Landau proof idea (finding 1 below).
- The guide recompiles with no overfull or underfull boxes, and its text is identical to the delivered PDF. The arXiv citation is accurate. Authors Schweser, Stiebitz and Toft, Theorem 1.1, and the arc-reversal parity argument from a transitive tournament all appear in Section 1, as the guide says.

All of these answers agree with my computation: K–1 P3, P4 (every line-up), P5, P6 and P7; 2–3 P2, P4, P7 (the king sets) and P8; 4–5 P2, P3, P5, P7, P9, P10, P11 and P13.

## Must-fix

**1. Overview, page 1, theorem 3, "A passing list always happens (proof idea)": the key step is false as stated.**
The text says to keep moving one win from "a player with too many to a player with too few", by reversing one arrow or two (richer → r → poorer). It then says "The inequalities keep such a move available until the list is reached." That is not true when the players are chosen freely. Starting from the ranking and making only legal moves of this kind, the process can get stuck. Here is a six-player example whose target is the first list of grades 4–5 Problem 10, 1,1,1,4,4,4:

- Players P0–P5 have target wins 1,1,1,4,4,4.
- The current results: P1 beat P0; P2 beat P0 and P1; P3 beat P0, P1 and P2; P4 beat P0–P3; P5 beat P1–P4; P0 beat P5. So the current wins are 1,1,2,3,4,4.
- Only P2 has too many wins and only P3 too few. P3 beat P2, and both of P2's victims, P0 and P1, lost to P3. So no one-arrow or two-arrow move exists.

The writer's script avoids this only because it uses a particular choice rule that the guide never states. (It takes the weakest player still short and a stronger player with a surplus; that player then has at least two more wins.) Because the printed sketch fails for the very list the 4–5 children work on, an adult who tries it on 1,1,1,4,4,4 can get stuck.
*Fix:* replace the sketch with the path argument. It is just as short and correct for any choice:

> *A passing list always happens* (proof idea): start from any tournament, say a ranking. From the players with too many wins, follow arrows forward. If you reach a player with too few, reverse every arrow on that path: only its two ends change, by one win each. If you cannot reach one, the players you can reach lost every game to the others, so they won exactly the games among themselves, while the list gives them fewer. The list then fails the test. Each reversal brings the wins closer to the list.

(In the stuck example, the path P2 → P0 → P5 → P3 finishes the job.) Alternatively, keep the two-arrow version and state the choice rule. If you do, change the sentence about the script to match.

**2. Grades 2–3 Problem 9, page 5: "kings need not be top scorers (top left and bottom left)".**
In Problem 7's top left square, A, C and D each won 2 games, which is the most, and they are exactly the kings. That picture shows no king who is not a top scorer. Only the bottom left pentagon does: A, C and E are kings with 2 wins, and D has 3.
*Fix:* "kings need not be top scorers (bottom left: A, C and E won 2 games, D won 3)."

**3. Grades 2–3 Problem 7, bottom right, page 5: "each beat the next two going round".**
That is false around the drawn pentagon. A lost to B and to D, and going either way round A, B, C, D, E, no player beats the next two. (Each beats its counterclockwise neighbour and the player two places clockwise.) It is true only around the star A, C, E, B, D. An adult checking the picture with this sentence will be confused.
*Fix:* "all five; every player won 2 games, and following the star A → C → E → B → D → A, each beat the next two." Or simply: "every player won 2, and from each player its two victims reach the other two."

## Should-fix

**4. Preparation time is optimistic and has no session total (page 2, "Per pair" and "Preparation time").**
"About 10 minutes per K–1 pair" covers six animal cards with hand-drawn pictures, 15 arrow strips with marker arrowheads, and a six-box strip ruled across two taped sheets. A volunteer drawing six recognizable animals per pair will take longer, and the guide gives no total for a typical meeting. *Fix:* give a total, for example "three K–1 pairs and six older pairs: about 45–60 minutes the first time, reusable". Report as an open item for the organizer that the draft supplies no printable card sheet or line-up strip. The page sources already contain the animal pictures (`src/animals.tex`), so one printed sheet would cut most of this time. The guide must not change the pages, but it should name the gap.

**5. Arrow cards for grades 4–5 (page 2).**
"Older bands: 6 per pair, optional, to lay out a first tournament" fits grades 2–3 (4 players, 6 games). It does not fit grades 4–5 Problem 1, which has 10 games among five animals and 15 with the pig. *Fix:* "Grades 2–3: 6 per pair, optional. Grades 4–5: 10 if they lay out the five-animal tournament first, otherwise none."

**6. No launch for the return visits (page 3, "A first visit").**
The guide plans kings (2–3 P7–9, 4–5 P5–8) and win counts (4–5 P9–12) for later visits. Both bring in a new procedure, following one or two arrows, or reading a number in a dot as a win count, but only the first meeting has a launch. *Fix:* add a two-minute return-visit launch on a non-task instance. For example, three children stand in the page's own P → Q → R circle and walk "one arrow, or two arrows" to each other. Every player there is a king with equal wins, so it gives away neither the top-scorer theorem nor any page answer. For win counts, the same three children each count the arrows leaving them.

**7. Predictions about an unpiloted activity are written as observations.**
"Children usually start with the animal that won the most" (K–1 P1, page 3). "Children often describe it as 'best to worst'" (K–1 P5, page 3). "Children often propose 'at most one 0…'" (4–5 P12, page 7). "Most children will offer the unbeaten case" (4–5 P8, page 6). AGENTS.md asks for observations to be kept separate from hypotheses. *Fix:* "may", "expect", "a likely first proposal is…".

**8. K–1 Problem 4's hint fits only half the pictures (page 3).**
"Which animal did nobody beat?" helps with the top left (pig) and top right (rabbit). The bottom left and bottom right have no unbeaten animal, so there the hint points at nothing. *Fix:* "Which animal could stand first? Whom did it beat?"

**9. The hardest 4–5 problems have no hint question (pages 6–7).**
Problem 12 (find a test) and Problem 8 (never two kings) get adult explanations but no question to ask when a child is stuck. *Fix:* for P12, "Look at the lists you could not build in Problems 9–11. Which group of players is in trouble together?" For P8, "Suppose nobody beat everyone. Who beat your king, and is one of them a king too?"

**10. The 4–5 later-visit route assumes Problems 5–6 were reached (page 3).**
"Later visits: kings (Problems 7–8)" leaves out Problems 5–6 when the first visit ended at Problem 4, which the guide expects to be common. *Fix:* "Later visits: kings (Problems 5–8, from wherever the first visit stopped), then win counts (Problems 9–12)."

## Minor

- **Repetition of the joining argument.** It is stated in full in the overview, in K–1 P2, in 2–3 P5 and in 4–5 P3, and summarized again in 2–3 P6 and 4–5 P4. Keep it in the overview and in one band entry, and write "as theorem 1" elsewhere.
- **Page narration.** 2–3 P3 ("Children copy their line-up into the boxes above the frog, draw arrowheads… write the new line-up in the five-box row…") and 4–5 P1 ("The hexagon holds all 15 games…") describe what the page already shows. They could be cut to the answer and the hints.
- **Launch details.** Have a child, not the adult, lay each arrow card, since children should make the legal moves. Arrow cards on the floor are small for a whole group; say that the whiteboard drawing is what everyone watches. The launch figure shows one possible outcome of rock-paper-scissors; label it "for example".
- **Staffing total.** The guide implies at least two adults (one at the K–1 table, one moving between the older tables) but never says so. State the minimum.
- **Print quantities.** The guide never says whether packets are per child or per pair. Page 1 of the K–1 packet is one per pair as the mat. Say how many of everything else to print.
- **Explanation list.** The 4–5 staffing sentence lists explanations in Problems 3–4, 6, 8 and 12. Problem 13 also asks "Explain".
- **First-player criterion.** "An animal can be first exactly when it can get to every other animal along arrows" is a general theorem: the top strong component has a Hamiltonian cycle (Camion). It is not just a result checked up to six players. This is optional to change.
- **Layout.** Page 3 ends about a quarter blank because `\needspace` pushes K–1 Problem 6 to page 4. This is cosmetic.

## Agreement with the pages (all checked, no defects)

- **Page counts and numbering.** Page counts (5, 6, 8) and every problem and page number cited match the final PDFs.
- **Picture positions.** The descriptions (top left and so on, pentagon or hexagon, read from the top dot clockwise) match each picture.
- **K–1 big board.** The dimensions match `k1_board.tex`: 4 cm squares, lanes 2.3 cm wide, 10.8 cm on the sides and 15.27 cm on the diagonals. The 10.2 cm strips from a 4 × 6 inch card fit; the 12.7 cm strips from a 3 × 5 card do not, which corrects the outline. The two diagonal cards must overlap at the centre. "Mat for Problems 1, 5, 6, 8, 9, 10" matches the pages.
- **Diagram and box counts.** All match the pages:
  - K–1 P6 has six recording rows.
  - 2–3 P5 has two blank pictures and P8 eight squares.
  - 4–5 P7 has four squares and six pentagons, and P11 five squares and twelve pentagons.
  - The 5-box and 6-box rows in 2–3 P3 and 4–5 P1.
  - K–1 P2 has nine games and 15 arrow cards (6, 4 and 5).
  - K–1 P4 has no recording boxes.

## What works and should be kept

- **The overview.** It opens theorem-first. It gives the model and its assumptions, including the limit that a line-up can fail if two players never met, and the insertion proof in a form the frog, pig and X problems act out. The uniqueness argument and the never-two-kings argument are correct and short; I checked both by hand and by enumeration. It is honest about what is computer-checked and what stays adult knowledge, and it ends with a clear split into experiments, conjectures and explanations and a band map.
- **The launch.** Three children as players make a non-task instance. It shows a row that fails, stops after one good row without asking about others or about "always", and has a worked visual (before, one game, all three games). It meets "Launch together".
- **Staffing.** The adult's role at K–1 (read, referee, record; point to one pair of neighbours rather than saying yes or no), and the signal that an adult choosing the next animal means the task should shrink, are exactly the operational age-fit test AGENTS.md asks for.
- **Physical guidance.** The K–1 Problem 2 table layout, the strip made from two taped sheets, and the warning that a K–1 child may wrongly believe P10 succeeded.
- **Completeness arguments.** The guide says how to know a list is complete: 4–5 P11 ("the right total adds only 0,0,3,3…"), 4–5 P2 ("try each player first") and K–1 P6 ("their evidence is that no board they try beats it").
- **Win-count reasoning.** The 4–5 P12 point that the children's likely rule works for four and five players but fails on Problem 10's second list. The note that every printed total is right, so the total never decides a list.
- **Status and records.** The status line names what is physically untested, and "What to record" separates observation from interpretation.
- **Sources.** The section separates consulted from cited sources, and the arXiv reference is accurate.
- **Length and look.** Seven pages for three bands, in the model guides' style, with a clean build.
