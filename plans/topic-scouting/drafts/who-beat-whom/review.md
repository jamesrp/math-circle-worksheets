# Review: Who beat whom, draft v1

Reviewed: `draft/k-1.pdf` (4 pages, 9 problems), `draft/grades-2-3.pdf` (6 pages, 9 problems), `draft/grades-4-5.pdf` (7 pages, 13 problems), and `draft/src/`. I rendered every page at 80 dpi and checked the dense diagrams again at 200 dpi.

## Verdict

The mathematics is correct and the pages are clean. Header, footer, the rules block with its worked example, and the "Problem N:" format all follow the standard. None of the banned material appears: no headings, encouragement, hints, dashes or Name/Date fields. The upper bands are close to ready. **The K–1 packet is not usable as printed.** Several of its problems tell children to "lay the arrows on the board", but the board they are told to use can't hold arrow cards, or the problem never says which board, or the board has nowhere to put the new arrows. Found line-ups also have to be held in memory. The 2–3 insertion problem has a similar gap: there is nowhere to record the results. The main jobs for revision:

- fix the work surfaces and recording in K–1;
- make the K–1 board's lanes match the real arrow cards;
- give 2–3 Problem 3 a recording diagram;
- enlarge the diagrams in 4–5 Problem 7;
- soften the proof demand in 4–5 Problem 12.

## What I verified

- **Every printed tournament, read from the drawn arrowheads.** I wrote an independent parser for `draft/src/figs/*.tex`. It reads which way each arrowhead points along its link and works out who beat whom, ignoring the author's specs. From that it recomputes line-ups, kings, win counts and which players can be first in a line-up. All of these agree with `answers-check.txt`:
  - K–1 P2 (left/right): 1 and 3 line-ups.
  - K–1 P3: 1, 3, 3 and 5 line-ups.
  - K–1 P8, players who can be first: dog only; cat, pig and rabbit; all four.
  - 2–3 P2: 5, 1, 1 and 3 line-ups, so the tournaments with only one line-up are the top-right and bottom-left ones.
  - 2–3 P4, places where X can join: C–D; after E; A–B and after E; before A, C–D and after E.
  - 2–3 P7 kings: {A, C, D}, {C}, {A, C, D, E}, all five.
  - 4–5 P2: 5, 3, 1 and 3 line-ups. These four tournaments are the four possible shapes of a four-player tournament, which is a nice setup for P13.
  - 4–5 P3: B–C and D–E; then D–E only.
  - 4–5 P5 kings: {A, C, D}, {B, C, D, E}, all six, {A, D, F}.
- **Lists of win counts, brute-forced.** Each list in 4–5 P9 and P10 has the right total (10 or 15), so checking the total never settles a case. P9: lists 2 and 4 are impossible and the rest possible. P10: list 2 is impossible and the rest possible. In P10, list 2 fails because of a three-player clash (0, 1, 1), which is a different kind of obstruction from P9's two-player clashes. Good choice.
- **Whole-family facts, checked by enumeration:**
  - Four players: 4 possible sorted lists of win counts; line-up counts {1, 3, 5}; king counts {1, 3}.
  - Five players: 9 possible sorted lists; king counts {1, 3, 4, 5}.
  - Three animals can all win equally. Four animals cannot, and two of four animals cannot both win every game.
  - So K–1 P7, 2–3 P8, 4–5 P7, P11 and P13 all have the answers the author expects.
- **Text.** I scanned the pdftotext output for exclamation marks, dashes, "Let's", "Remember" and Name/Date. None found.
- **Line weights.** Some edges look bold at 80 dpi (2–3 P1, P6; 4–5 P7, P10). At 200 dpi every line has the same weight, so this is a rendering artifact and not a defect.

## Blocking issues

### 1. K–1 P4–P7 and P9: the working surface is wrong or missing

- **P4, P5:** "Lay the arrows on the board so that…". Under each is a small board: animal circles 4.6 cm apart, with about 2.7 cm of line between circles. A 2 × 10 cm arrow card can't be laid there. A child either can't do what the page says, or has to guess that "the board" means the large board on page 1. If so, the small picture has no stated purpose. The page never says to draw.
- **P6, P7:** "Can you lay the arrows on the board…" / "Can you lay the arrows to make each of these happen?" There is no picture at all. P7's first case ("With three animals…") doesn't say which three animals or where.
- **P9:** "The frog plays each animal on the board, then joins their line-up without changing its order." This has three problems:
  - The big board has lanes for only the four original animals. The frog's 4 arrows and the pig's 5 arrows have nowhere to go.
  - "The board" no longer holds the Problem 1 tournament. P4–P7 told children to rearrange it, so "their line-up" has nothing definite to refer to.
  - The sentence reads as a story, not an instruction. Read aloud once, a kindergartner doesn't hear what to do.
- **Why it matters:** the K–1 adult is the parent volunteer, who is not a mathematician. This is the table where a clear physical surface matters most, and where the outline asks for the rules to be enforced by the materials.
- **Fix:**
  - Pick one surface per problem and name it. For P4–P7 the simplest choice is: "Lay arrow cards on the big board from Problem 1."
  - Then either drop the small boards, or keep them as a record with a direct instruction: "Then draw the arrows here." Drawing an arrowhead on a 2.7 cm line is within a K–1 child's reach, and the adult can draw it if needed.
  - For P7, either say "on the big board" (the three-animal case uses three of the four squares), or print a small three-animal triangle and a four-animal square.
  - For P9, print a K–1 "joining mat", a concrete version of the 2–3 X-diagram:
    - four 5 cm line-up boxes in a row;
    - a frog box below them;
    - one card-sized lane from the frog to each box.
  - Then a second mat with five boxes and the pig.
  - Reword P9 as instructions: "Play the frog against each animal in your line-up from Problem 1. Lay the arrows on the mat. Fit the frog into the line-up without moving the other animals. Then do the same with the pig."
  - Alternatively, move the frog and pig problem to just after P1 or P3, while the first line-up is still on the table.

### 2. K–1 P1: the board's lanes don't fit the arrow cards

- `figs/k1_board.tex` draws the side lanes 8.2 cm long (`(-4.1,5.6) rectangle (4.1,7.6)`) and the diagonal lanes 11.6 cm long.
- The outline asks for 2 × 10 cm arrow cards, made from index cards cut in thirds. A 3 × 5 in index card cut in thirds gives 1 × 5 in strips, which are about 2.5 × 12.7 cm.
- Either way, a card overhangs the side lanes onto the animal squares by about 1–2.3 cm at each end, and a 12.7 cm strip is longer than the diagonal lanes too. A dashed outline that the card visibly doesn't fit invites fiddling and arguments at the K–1 table.
- **Fix:** make the board and the cards agree. One option is to shrink the animal squares to about 4 cm and spread the centres to about 14.5–15 cm. Side lanes then come out around 10.5–11 cm, which suits 10 cm strips. Diagonal lanes become longer still, which is harmless.
- Once the guide exists, its materials list must state the card length, for example "cut strips 2 × 10 cm" rather than "index cards in thirds".
- Mark the fit as unrehearsed until someone lays real cards on a printed board.

### 3. 2–3 P3: nowhere to record the frog's and pig's games

- The text: "The frog joins your last tournament from Problem 1 and plays the other four animals. Fit the frog into your line-up… Then the pig joins and plays the other five."
- The page gives only a 5-box row and a 6-box row. The 4 + 5 game results have nowhere to go, so children must remember 9 rock-paper-scissors outcomes while they search for a place.
- That makes memory the main demand, which AGENTS.md asks us to avoid. It also misses the natural bridge to P4.
- **Fix:** under P3, print the P4 newcomer diagram with blank links:
  - the four line-up boxes in a row with the frog dot below and four plain links;
  - the same with five boxes and the pig.
- Children draw arrowheads as they play, then write the new line-up in the existing box rows. P4's printed X-diagrams then reuse a representation the children have already used with their own results.

### 4. K–1: counting and comparing line-ups depends on memory

- **The problem:**
  - P2 asks "How many ways can these three animals line up?"
  - P5 asks "…as many ways as possible. How many ways is that?" The answer is 5 line-ups out of 24 orders.
  - P8 asks which animals can be first.
  - Each pair has one set of animal cards and one line-up strip, and the page records nothing. So a child has to remember which orders were already found while building the next one.
- **Why it matters:**
  - At P5, the answer of 5 can only be counted reliably if the found line-ups stay visible.
  - The P5 answer box asks for a number that the materials don't help produce.
- **Fix:**
  - Give P2 and P5 a light record. For example, add a few blank 4-box line-up rows (3 per P2 picture, 6 under P5). The child or the adult writes each found line-up there as initials or small marks.
  - Routine adult recording is allowed. The point is that found line-ups stay on the page.
  - For P8, make the action explicit: "Circle the animals that can be first in each picture."

## Should fix

### 5. 4–5 P7: diagrams too small, and their count leaks the answer

- The five-player diagrams (`pent_blank_s`) have radius 1.75 cm and circles of 0.45 cm. That leaves about 1.2 cm of visible side and about 0.8 cm of diagonal before the first crossing for each of 10 hand-drawn arrowheads. Then the child still has to check kings, all at that size.
- There are exactly four pentagons, and exactly four king counts are possible for five players (1, 3, 4, 5). That quietly tells children how many to find, and leaves no room for failed attempts at 2 kings.
- The four-player squares (2.7 cm) are usable but tight.
- **Fix:**
  - Use the P9 size (radius 2.25 cm or larger) and give P7 its own page.
  - Use more diagrams than there are answers. For example, six squares and six pentagons, with the extras clearly spare workspace and not tied to particular answers.

### 6. 4–5 P11: no diagrams for building tournaments

- The task is "Find every list of win counts… for four players. Then… for five players."
- The outline says children decide which lists can happen by building tournaments for them. The page gives blank space but no dots.
- Five players means 9 possible lists out of 12 sorted lists with the right total, so a child needs room for about 9 small tournaments.
- **Fix:** add a grid of blank four- and five-player diagrams at the P9 size, or say on the page that children should draw their own. The standard is to show the diagrams the child needs.

### 7. 4–5 P12 asks for a proof beyond the level

- The text: "Find a test that tells from a list of win counts alone whether some tournament has those win counts. Explain why your test works."
- **Why it's too much:**
  - "Works" includes the hard direction of Landau's theorem: every list that passes the test really does come from some tournament.
  - That is a genuine theorem with a nontrivial proof.
  - The other direction is very accessible to a fourth or fifth grader: the k weakest players already play k(k−1)/2 games among themselves.
- **Fix:** keep the discovery and ask for the part a child can explain, for example: "…Explain why a list that fails your test cannot happen."
- Leave the converse for conversation with the organizer. It is checked for four and five players through P11.

### 8. 4–5 P6 states the conclusion; 2–3 P9 asks it openly

- 4–5 has: "Explain why a player who won the most games is always a king."
- 2–3 has: "Is a player who won the most games always a king? Explain."
- AGENTS.md asks for open questions. The open form also suits 4–5. P5's fourth tournament already shows a king with one win (F) and a non-king with three (B), so the question is live for them.
- **Fix:** use the 2–3 wording in 4–5. The same applies, more mildly, to 4–5 P4 ("Explain why every tournament has a line-up…"). After P1 and P3 that is defensible, but "Does every tournament have a line-up, however many players it has? Explain." keeps it open at no cost.

### 9. Kings arrive as a definition before children have used the idea

- 2–3 P7 and 4–5 P5 define a king as follows: "A player is a king if, for every other player, the king beat that player or beat someone who beat that player."
- The standard says to introduce a new word only after the idea has been used. This sentence is also the densest one in either packet for one hearing.
- **Fix:** phrase it as an action on the picture: "A player is a king if you can get from that player to every other player by following one arrow or two arrows." It means exactly the same thing and is much easier to act on.
- Optionally, add a tiny non-task example in the same problem: a 3- or 4-player picture with one king and its two-step paths shown.

### 10. 2–3 P8: too little room to explore

- The text: "Try to make a tournament of four players with exactly 1 king, … 2 kings, … 3 kings, and … 4 kings."
- Four small squares, one per target, leave no room for the repeated failed attempts that 2 and 4 kings will produce.
- P7 on the previous page already shows 1 king (top right) and 3 kings (top left), so the real work is the impossible cases.
- **Fix:** add four to six more blank squares, clearly spare workspace. The sizes are otherwise fine.

## Minor / polish

### 11. Arrowheads on crossing diagonals sit on the winner's side

`figs.py` `place_arrows` tries t = 0.5, then 0.44, 0.56…, always measured from the winner. Wherever diagonals cross at their midpoints, every arrowhead therefore lands at t ≈ 0.33–0.38, near the winner. Examples are all K–1 P3 and P8 pictures and the squares in 2–3 P2, P7 and 4–5 P2.

A young child who reads "the arrow is next to the cat" as "it points at the cat" will misread every diagonal. Side arrows sit at the midpoint, so the pattern isn't even consistent.

**Fix:** try t > 0.5 first, toward the loser, so that being near and pointing at agree. Or let the arrowheads on the two crossing diagonals sit on opposite sides of the crossing. Either way they stay well clear of the dots.

### 12. 2–3 P5: make the action explicit

"Choose results for X…" leaves the action implicit. Write: "Draw arrowheads on the lines to X so that X cannot join the line-up A, B, C, D, E anywhere, or explain why that is impossible."

### 13. 4–5 P10: "these tournaments" is not accurate yet

"Do the same for these tournaments of six players." These are lists to try to realize, not tournaments yet. Write: "Do the same for six players."

### 14. K–1 P6: children may wrongly think they've succeeded

"Can you lay the arrows… so that the four animals cannot line up at all?" A K–1 child who fails to find an existing line-up will report success. Two options:

- Place P6 after the frog and pig joining problem. Joining one animal at a time is then a way to find a line-up on any board, and the child can test their own claim.
- Or make sure the guide warns the parent volunteer.

### 15. 4–5 P3: optional third case

4–5 P3 gives only two cases. In both, X lost to A and beat E, so both are "switch in the middle" cases. A third case where X joins only at the front or only at the back would make the explanation account for the ends. This is optional; P1's real insertion may already cover it.

### 16. The K–1 line-up strip has no file

Problems 1, 3, 5, 8 and 9 all rely on "the line-up strip", but no file supplies it. Six 5 cm boxes plus gaps measure more than 33 cm, wider than a portrait page. The guide and materials list need to say how it is made, for example two landscape half-strips taped together. Nothing on the student pages needs to change unless the reviser prints it as a page.

### 17. Placeholders

"Week NN" and "FNN-…-v1" need the real week number before printing. This is expected at the draft stage.

## Keep these strengths when revising

- The rules blocks are brief, and their three-player example takes the reader from tournament to line-up without giving anything away.
- **2–3:** P2 chooses its tournaments so that alphabetical order is never a line-up. The two answer rows per tournament fit the "only one?" question exactly. P4's four cases give 1, 1, 2 and 3 places.
- **4–5:** P2 covers all four shapes of a four-player tournament, which makes P13 answerable from the child's own work. P5's fourth tournament separates kings from top scorers. The P9 and P10 lists include zero-win players and a three-player obstruction.
- The order within each band runs from concrete work to explanation, theme by theme. The 4–5 explanation problems (P3–P4, P6, P8, P12–P13) are the points the outline names.
- K–1 has real content at the right scale: one line-up versus several (P2, P4, P5), an impossibility (P6, P7), and an insertion (P9). Once its surfaces are fixed it carries as much as the other bands.

## Not established by this review

- The arrow-card fit, the joining mats and the K–1 pacing are physical and classroom matters. Digital checks don't establish them; they stay untested until rehearsed.
- No facilitator guide exists yet. K–1 P5, P6 and P7 in particular depend on the adult knowing the answers: 5 line-ups at most; no board without a line-up; equal wins possible with three animals but not with four; two animals can't both win every game. The guide must supply these.
