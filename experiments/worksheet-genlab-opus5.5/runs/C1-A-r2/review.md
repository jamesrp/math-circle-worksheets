=================== Report 1: adversarial review ===================

# Review of the Week 1 tiling packet (draft in base/)

## Scope and method

- I read BRIEF.md, all three .tex files, preamble.tex, gen_figs.py, tri.py and check1–4.py.
- I rendered every page of the three PDFs (K–1: 6 pages, 2–3: 8 pages, 4–5: 8 pages) at 80 dpi, and the denser figures at 150 dpi, and looked at each one.
- I recompiled the sources in scratch/. They reproduce base/ pixel for pixel, with no overfull or underfull boxes. Regenerating the figures with gen_figs.py also gives identical files.
- I re-ran the author's checks. I also wrote my own checks in scratch/verify/v.py and v2.py, which use their own adjacency, tiling enumeration, flip detection, chain reading and game search. They check every numerical claim and answer the packet relies on.
- I measured the boards on the rendered pages. Every board meant for physical blocks prints with 1-inch triangle edges at 100% scale.

## Overall verdict

The mathematics is correct throughout, and the boards are well chosen.
- Every board with an even area that cannot be covered is blocked by an up/down imbalance, never by an odd area.
- The cases contrast in useful ways: possible against impossible, and in grades 4–5 Problem 3 a cube-count lower bound against a chain lower bound.
- The format follows the standard: header, footer, "Problem N:" labels, no titles, no exclamation marks, no encouragement, no dashes.
- K–1 gets real content from both kernels.

The problems to fix are mostly about sequencing, hints that leak, space to record, and a few wording and layout issues. In order of importance:

---

## Major

### 1. Grades 4–5: the explanations are asked for before the tool that answers them, and the tool is never connected back

- **Problem 3** asks: "For the first pair, explain why it cannot be done in fewer moves." The answer is 8 moves, from LLRR/LLRR to RRLL/RRLL.
- **Problem 4** asks the child to "explain why it cannot be done" for round trips of 5 and 7 moves.

Both explanations need an invariant: each move swaps one adjacent L/R pair in one chain, so the flip graph is bipartite and the distance is at least the sum of the chain inversion distances. The packet only introduces chains in Problem 5 and only asks how a move changes them in Problem 7.

After Problem 7 nothing asks the child to use that result, so the payoff the outline names ("every round trip takes an even number of flips", "prove facts about flips") is left disconnected. The other route, counting cubes (each move adds or removes one cube), is never shown either. It also cannot explain pair 2, where the cube counts are equal but the distance is 4.

This reverses the brief's development rule: "a child meets an idea in concrete cases, and uses it, before being asked to explain or generalize it."

Fix:
- Keep the concrete parts of Problems 3 and 4 where they are: find the fewest moves, and try round trips of 4, 5, 6 and 7 moves.
- Remove their "explain" clauses.
- Add one problem after Problem 7: "Explain why the first pair in Problem 3 cannot be done in fewer than 8 moves, and why no round trip in Problem 4 can use 5 or 7 moves."
- Alternatively, move Problems 5–7 (chains) ahead of Problems 3–4.

### 2. K–1: the packet rule leaves out "along the lines", and the game in Problem 6 depends on it

The K–1 rule is "blocks must stay inside the shape and must not overlap." The 2–3 rule adds "along its lines", but K–1 does not.

For the covering problems this hardly matters, because covering exactly forces the blocks onto the grid. For the game in Problem 6 it changes the game:
- A blue rhombus can slide anywhere along the 6-triangle strip.
- A green triangle can sit off the grid in the middle of the hexagon. That breaks the second player's symmetry strategy, which is the whole point of the hexagon case.

Kindergartners will put blocks down off the grid.

Fix: change the K–1 rule to "Blocks go on the lines of the shape. They must stay inside it and must not overlap", or add "on the lines" to Problem 6.

On the grid, the outcomes I verified are: hexagon, second player wins; 6-triangle strip, first player wins; 5-triangle strip, first player wins. These are good contrasting cases. The game is Kayles.

---

## Moderate

### 3. Hints that do the noticing for the child

- **Grades 2–3, Problem 5:** "Each side of triangle C is 4 inches long." It sits directly under Problem 4's "fewer than 4 green triangles", so the page itself pairs side 4 with 4 greens. That is the pattern the child is supposed to find.
  - Fix: describe the giant triangle without restating C. For example: "Imagine a triangle like the ones in Problem 2, with 10 small triangle edges along each side." Or put it in inches only: "with sides 10 inches long".
- **Grades 4–5, Problem 8:** "This board has only one small edge on its bottom side." The board is drawn, so this sentence does nothing except point to the one-chain counting method: 20 = C(6,3) chain words.
  - Fix: delete the sentence. The brief's rule is that the method belongs to the child.

### 4. Grades 2–3, Problem 4 gives away the answer to Problem 2C

"Explain why triangle C in Problem 2 cannot be covered with blue blocks and fewer than 4 green triangles" tells any child who reads ahead that the answer to Problem 2C is 4.

Fix: "Could triangle C be covered using fewer green triangles than you used in Problem 2? Explain." This keeps the "why is this packing best" explanation without the spoiler.

### 5. Grades 4–5: not enough recording space in Problems 4, 8 and 9

- **Problem 4:** "For each number, draw the coverings you pass through." The 4-move trip passes through 4 coverings and the 6-move trip through 6, which is at least 10 drawings. There are 8 copies, no note about using the back, and about 5 inches of empty page below them. Add a third row, or a row of 4 for each possible length, with a label "4 moves" and "6 moves".
- **Problem 8:** the answer is 20 coverings, and there are no recording copies at all, although the packet rule says "The small drawings of boards are for recording." Children either invent notation, which the deleted hint in item 3 was steering toward, or redraw a 30-triangle board by hand. Add small copies, or at least a ruled space.
- **Problem 9:** 16 copies for an answer of 20. Five rows of four at the same 0.4 scale fit on the page, since the current 16 end about 2.4 inches above the footer. Give 20 or 24 copies so that running out does not signal a count.

### 6. K–1 sentences are longer than "one or two short sentences" for a single hearing

- **Problem 6:** "Take turns with a partner putting one green block or one blue block on the shape; whoever puts down the last block wins." This is 23 words joined by a semicolon, followed by a second sentence. It also never says what to do with the printed words "first second" (circle one).
  - Suggested: "Take turns putting one green or one blue block on the shape. The player who puts down the last block wins. Circle who you would rather be: first or second."
- **Problem 5:** "Build the left picture with blue blocks, then change it into the right picture in as few moves as you can." This one sentence carries three instructions, followed by the definition of a move.
  - Suggested: "Build the left picture with blue blocks. Change it into the right picture with as few moves as you can." Then the move picture.
- **Problems 2 and 4** are also long, at 17–18 words before the second sentence, but they are tolerable.

### 7. Grades 2–3: page breaks split problems and mix up board labels

- Problem 1 runs from page 1 onto page 2. Boards E and F sit at the top of page 2 with no problem text.
- Problem 2 then starts halfway down that same page, so page 2 shows boards labelled E, F, A and B for two different problems. Problem 2 continues onto page 3 (C and D).
- Page 1 leaves about 3 inches empty below boards C and D, enough for board E.

Fix:
- Put E on page 1. F, the 4-inch parallelogram, can sit alone at the top of page 2, or move to page 1 if the vertical spacing is tightened.
- Start Problem 2 on a fresh page, or let the problem number travel with the labels (for example "2A").

### 8. Grades 4–5, Problem 5 introduces the word, the notation and a worked example all at first contact

"These blocks form a chain… In the picture, the left chain is shaded, and it is RLLR." The brief asks that a new word or notation come "only after the child has used the idea it names." Here the child has not yet followed a crossing strip of blocks before it is named and coded.

A lighter version would have children trace and shade, on Problem 1's coverings, the blocks met going from a bottom edge to the top before the L/R code is introduced. This is a judgment call, since the notation genuinely helps in Problems 6–9, but it is worth the organizer's attention.

---

## Minor

1. **Grades 2–3, Problem 6:** "Now use purple blocks…" The "Now" is narration and can be dropped. The same problem also says "Cover each triangle…" and then "Is there a board where…". Pick one word.
2. **Grades 4–5 packet rule:** "The small drawings of boards are for recording." This is untrue for Problems 3 and 5, where the small drawings are targets to read. A child may draw on them. Either drop the sentence or say "Blank small drawings are for recording."
3. **K–1 Problem 6** is the only K–1 problem outside the two kernels. It is a legitimate "work out how to win" task and it does use the pieces, but every other K–1 problem mirrors an older band. If space is needed for anything, this is the one to reconsider.
4. **Grades 2–3:** every board with balanced up/down counts can in fact be covered, and every board in Problem 3 with one up hole and one down hole is coverable (all 144 such hole pairs on that hexagon are). So the pages never challenge the tempting converse, "equal up and down means it can be covered". One balanced board that still cannot be covered would sharpen Problem 1 or 3: for example, two unbalanced parts joined only at a corner, or a bow-tie-like shape. This is optional.
5. **Grades 2–3, Problem 3** asks for explanations but marks no space for them. The right half of pages 4–5 is empty and can serve, but children may not see it as answer space.
6. **Grades 4–5, Problem 3:** the only room for the pair-1 explanation is the area beside the big board. This matters less if item 1 is adopted.
7. **Faint grids on small copies:** the 0.4–0.45-scale copies use 0.35 pt lines at 22% gray, which some school laser printers drop or break up. Consider 0.4–0.5 pt at about 30% gray.
8. **Footer margin:** the footer ink sits about 0.35 inch from the bottom edge. That is fine on most printers, but it is near the limit for some.

---

## Verified correct (no action needed)

| Packet / problem | What I checked | Result |
|---|---|---|
| All boards for physical blocks | Size | 1-inch triangle edges: K–1 all problems; 2–3 Problems 1–3 and the Problem 7 grid paper; 4–5 boards in Problems 1, 3 and 8, and the K–1 move picture |
| K–1 Problem 1 | Which shapes blues can cover | Hexagon, chevron and 2×2 parallelogram can be covered. The 4-triangle triangle (3 up/1 down), the "boat" (4/2) and the 4-2 trapezoid (7/5) cannot. All six have even area. |
| K–1 Problems 2–3, 2–3 Problem 2 | Fewest greens with blues | Sides 2, 3, 4, 5 need 2, 3, 4, 5 greens |
| 2–3 Problem 6 | Fewest greens with purples | 4, 5, 4, 5, so purple never does better (answer: no) |
| K–1 Problem 4 | Number of coverings | Hexagon 2, long shape 3. The 3 and 4 copies give no clue to the count. |
| K–1 Problem 5 | Fewest moves | 2 and 4 moves |
| 2–3 Problem 1 | Which boards can be covered | A, C, F can. B (5/3), D (6/4) and E (7/5) cannot. |
| 2–3 Problem 3 | Hole boards | A and D can be covered. B (two up holes) and C (two down holes) cannot. |
| 2–3 Problem 5 | Triangles of side 10 and 100 | 10 and 100 greens |
| 2–3 Problem 7 | A 12-triangle board needing at least 4 greens | One exists (8 up/4 down) |
| 4–5 Problems 1–2 | Coverings of the 2,2,1 hexagon and their move graph | 6 coverings. The move graph has 6 edges: a 4-cycle with two pendant coverings. |
| 4–5 Problem 3 | Fewest moves | 8 and 4 |
| 4–5 Problem 4 | Round trips with no immediate undo | Exist for 4 and 6 moves, none for 5 or 7. The graph is bipartite. |
| 4–5 Problem 5 | Pictures and chains | The example's shaded left chain reads RLLR. The L and R icons lean the right way. Coverings A–D exist as drawn. |
| 4–5 Problem 6 | Which chain pairs exist | LRLR/RRLL and RLRL/RLRL exist. RRLL/LLRR and LRRL/LRLR do not, because the chains would cross. |
| 4–5 Problem 7 | Effect of one move | Every move changes exactly one chain, by swapping one adjacent LR pair |
| 4–5 Problems 8–9 | Number of coverings | Both are 20: the 1,3,3 hexagon and the big 2,2,2 hexagon |
| All three packets | Format | Header, footer and page numbers correct. "Problem N:" labels only. No banned phrases, exclamation marks, dashes or extra headings. Fonts embedded, US Letter, nothing overflows. |


=================== Report 2: simulated classroom session ===================

# Session simulation: Week 1 Tiling packets (base draft)

I rendered every page of base/k-1.pdf (6 pp.), base/grades-2-3.pdf (8 pp.) and base/grades-4-5.pdf (8 pp.) and checked the boards against src/ with the author's own solver (tri.py). All boards meant for blocks print at actual size (1-inch edges), and the stated answers below were computed, not guessed: unit hexagon 2 coverings; "long shape" 3; 2-2-1 hexagon 6; big 2-2-2 hexagon 20; 1-3-3 board 20. K-1 move puzzles are 2 and 4 moves. 4-5 Problem 3 pairs are 8 and 4 moves. In the K-1 game the hexagon is a second-player win and both strips are first-player wins. With purple blocks the triangles need 4, 5, 4, 5 green triangles, against 2, 3, 4, 5 with blue.

Cast:
- **K-1** (parent volunteer reads each problem aloud exactly as printed): Ava (K), Ben (K), and Cora (grade 1, reads a few words, the quick child).
- **Grades 2-3** (second mathematician): Theo (quick, impatient), Priya (strong), Sam (middle), Lily (weaker).
- **Grades 4-5** (organizer nearby): Maya (fast grade 5), Jonah and Eli (grade 4).

---

## K-1

**Problem 1 (p. 1), six shapes, blue only, X the impossible ones.** The parent reads the rule and the problem once. The hexagon, chevron and 2x2 rhombus get covered in under a minute each. Ava's first hexagon is crooked, and the grey lines get her to straighten it. On the small triangle Ben places one blue and is left with two lone corners. He turns the blue, gets the same result, and Cora says "it can't." On the boat and the 12-triangle trapezoid the children always end up with two loose triangles. Cora gives up on the trapezoid after three tries and they draw Xs. Everyone is engaged and the X recording works. *Cora: 0 to 6 min.*

**Problem 2 (p. 2), three triangles, fewest greens.** Ava first fills the small triangle with four greens ("I covered it!"). The parent rereads "as few green blocks as you can" and Ava swaps in a blue to get 2. On the middle triangle Ben uses 5 greens and Cora uses 3. On the big one Cora gets 4 on her second try and Ben gets 6. The children can write single digits next to the green icon. *Cora: 6 to 12.*

**Problem 3 (p. 3), guess, then cover the side-5 triangle.** "Guess how many green blocks this big triangle needs" is heard as "how many greens does it take to fill it." Ava guesses "a hundred" and Ben guesses "twenty". Cora counts small triangles in the bottom row and says 9. Nobody links the guess to 2, 3, 4 from Problem 2, so it works as a filler line. Covering 25 small triangles takes 5 to 7 minutes and Ben drifts. Cora gets 5 greens on her second attempt. *Cora: 12 to 18.*

**Problem 4 (p. 4), every covering of the hexagon (3 copies) and the long shape (4 copies).** The children find both hexagon coverings in a minute and draw them easily by darkening three grey spokes (a "Y" and an upside-down "Y"). Then the third empty copy drives everything. They turn the blocks, draw a "Y" again, and the parent sees it matches the first drawing and says "find a different one." Three minutes of turning blocks follow. The parent cannot tell from the page whether a third way exists, so she keeps encouraging. Ben gives up. On the long shape Cora finds the three coverings in about four minutes and then the same hunt starts over the fourth copy. Ava fills it with a repeat. The parent cannot tell whether it is new and accepts it. *Cora: 18 to 28, with about 4 of those minutes spent on coverings that do not exist.*

**Problem 5 (p. 5), move puzzles.** Building eight blues on the left picture takes about 2 minutes. Ben starts placing blocks on the small right-hand picture, finds they are too big, and says "it's broken." The parent redirects him. Nobody can see a "three blue blocks that make a hexagon" inside the eight-block picture until the parent and Cora compare it with the example pair. Cora then turns one, and the first puzzle is done in 2 moves. The second puzzle has only one hexagon to turn at the start. The children turn back and forth, lose count, and the parent counts. They write 6 (the fewest is 4). The kindergartners are fading. *Cora: 28 to 36.*

**Problem 6 (p. 6), the game.** The parent reads "would you rather go first or second?" Ava and Ben shout "First!" before any game and want to circle "first" under every shape. The page never says to circle anything, so the parent improvises. In the strip game Ben sets a green crooked across two spaces to block Cora. Cora protests, but the K-1 rule only says "stay inside the shape and must not overlap", so the parent cannot settle it from the page. After a few games they circle whoever won the last one. The hexagon, a second-player win, gets "first". *Cora: 36 to 40, still playing when time is called.* She never runs out of work.

## Grades 2-3

**Problem 1 (pp. 1-2), six boards.** Theo covers A, C and F in under a minute each. B, D and E always leave two triangles, so he draws Xs. He skips "draw lines on it to show where your blocks went" until the adult insists, which costs about 1.5 minutes of grumbling. Lily takes 10 minutes. *Theo: 0 to 6.*

**Problem 2 (pp. 2-3), triangles A to D.** Theo gets 2 and 3, then 6 on C before retrying to 4, then 5 on D on his second try. Priya says "it's how long the side is." *Theo: 6 to 13.*

**Problem 3 (pp. 4-5), hexagons with holes.** Board A takes Theo about 3 minutes. On B everyone is left with two triangles every time, and Priya notices "both holes point up." Theo calls C impossible ("both point down") before building it, and predicts D is possible, then builds it. With the adult's push, Priya puts the explanation into words: each blue covers one up-triangle and one down-triangle. The blank space beside each board is enough to write in. Strong engagement. *Theo: 13 to 24.*

**Problem 4 (p. 6), explain why C needs 4 greens.** Theo first writes "we tried." The adult points back to the holes, and he counts 10 up-triangles and 6 down-triangles. *Theo: 24 to 28.*

**Problem 5 (p. 6), sides 10 and 100.** Theo says "10 and 100" in 30 seconds. To the adult's "how do you know?" he says "pattern." Counting 1+2+...+10 = 55 up-triangles against 45 down-triangles takes him a few minutes with help. *Theo: 28 to 31.*

**Problem 6 (p. 7), purple blocks.** On A no purple fits, so it needs 4 greens. B takes one purple and 5 greens. On C Theo first gets 8 greens, then 4 after several minutes of real puzzling. D is half done when he gets impatient. Priya writes "no, a purple is just two blues." *Theo: 31 to 38.*

**Problem 7 (p. 8), design a 12-triangle board.** Theo reads "every way of covering it ... uses at least 4 green triangles" as "a board that I can cover using 4 greens." He outlines a 2-by-3 parallelogram of 12 triangles, covers it with 4 blues and 4 greens, and announces he is done. The adult has to explain "every way". After that, Theo starts trying to make a shape with "lots of up ones." *Theo: 38 to 40, still working.* He never runs out of work.

## Grades 4-5

**Problem 1 (p. 1), all coverings of the 2-2-1 board, copies A to H.** Maya has 4 coverings drawn by minute 4 and 6 by minute 7. Copies G and H sit empty with letters printed on them, so she assumes two are missing and hunts for 3 to 4 minutes. She draws a 7th covering in G that is a mis-copy of C. Jonah and Eli find 5 and also believe there are 8. "Explain how you know that you have found them all" gets "we tried everything" in the 2.5 x 1.3 in gap beside H. She is unsure, because the empty letters say otherwise. *Maya: 0 to 11.*

**Problem 2 (p. 2), move graph.** Maya writes A to G in the box. G (the mis-copy) collects the same lines as C until she notices the two are identical and erases it. She ends with the right graph, a square with one tail at each of two opposite corners. Engaged. *Maya: 11 to 16.*

**Problem 3 (p. 3), two pairs.** Building 12 blues from the small picture takes about 2 minutes. Pair 1 has only one hexagon to turn at the start. Her first run takes 10 moves and her second takes 8. "For the first pair, explain why it cannot be done in fewer moves" stalls her. Her best argument is "none of the 12 blocks stay put and a move changes 3, so at least 4." That gives 4, not 8. Nothing on the page so far (no chains, no cubes) gives her a way to reach 8, and the adult can only hint. Pair 2 takes 4 moves. Jonah and Eli finish pair 1 near the end of the hour and stall at the same point. *Maya: 16 to 28.*

**Problem 4 (p. 4), round trips of 4, 5, 6, 7 moves.** She finds the 4-move trip (turn two separate hexagons, then turn each back). She asks whether turning the first one back counts as "undo", and the adult answers from the page. She draws the 4 coverings at 0.4-inch edges, about 1.5 minutes each, getting sloppier. She finds a 6-move trip with blocks, draws 4 of its coverings, and runs out of copies (8 printed, 10 needed). The back is blank paper and she cannot draw these hexagons freehand, so she stops recording. She tries 5 and 7, fails, and writes "we couldn't." She has no reason to give, because the chain argument comes three problems later. *Maya: 28 to 36, partly bored by the copying.*

**Problem 5 (p. 5), reading chains.** The shaded example and the L/R icons are clear. Maya reads the chains of A and B correctly in about 3 minutes. *Maya: 36 to 40.*

**Problems 6 to 9.** Nobody reaches these in the 40 minutes. Maya never runs out of work.

---

## Problems exposed by the simulation

**1. K-1, p. 4, Problem 4.**
- **Text and diagram:** "Find every way to cover the hexagon with blue blocks, and every way to cover the long shape. Draw each way in a different copy." The page prints 3 hexagon copies (2 coverings exist) and 4 long-shape copies (3 exist).
- **What went wrong:** The children took the empty copies as proof of more ways. They redrew duplicates and hunted for coverings that do not exist. The parent could not tell them they were done, and about 4 of the quick child's minutes went to the hunt.
- **Smallest fix:** Print exactly 2 hexagon copies and 3 long-shape copies.

**2. K-1, p. 6, Problem 6.**
- **Text and diagram:** "For each shape, would you rather go first or second?" with bare "first second" under each shape.
- **What went wrong:** The kindergartners answered a preference question ("First!") before playing and circled "first" everywhere, including the hexagon, which is a second-player win. The page never says to circle.
- **Smallest fix:** "Play each shape several times. Then circle the player who can always win: first or second."

**3. K-1, p. 1, the packet rule as used in Problem 6.**
- **Text and diagram:** "In every problem, blocks must stay inside the shape and must not overlap."
- **What went wrong:** In the game a child placed a green crooked across two spaces to block, which the rule allows. The parent could not settle the dispute from the page. The 2-3 packet already has the missing words.
- **Smallest fix:** "In every problem, blocks go along the lines, stay inside the shape, and must not overlap."

**4. K-1, p. 5, Problem 5.**
- **Text and diagram:** The right-hand target pictures are printed at 62% size (k1_p5_0_end_small, k1_p5_1_end_small) beside the actual-size start.
- **What went wrong:** A kindergartner tried to build on the small target. The blocks did not fit ("it's broken"), and the children could not lay blocks on the target to check whether they had matched it.
- **Smallest fix:** Give each puzzle its own page, with the start and the target both at actual size, stacked.

**5. K-1, p. 3, Problem 3.**
- **Text and diagram:** "Guess how many green blocks this big triangle needs."
- **What went wrong:** Heard once, "needs" meant "how many greens fill it." The guesses ("a hundred", "twenty", 9) had nothing to do with the fewest greens, so the guess did not connect to Problem 2.
- **Smallest fix:** "Guess the fewest green blocks you will need for this big triangle."

**6. Grades 2-3, p. 8, Problem 7.**
- **Text and diagram:** "...so that every way of covering it with blue blocks and green triangles uses at least 4 green triangles."
- **What went wrong:** The quick child read this as "a board I can cover with 4 greens." He drew a 12-triangle parallelogram, covered it with 4 blues and 4 greens, and declared it done.
- **Smallest fix:** "...so that it cannot be covered with blue blocks and fewer than 4 green triangles." This matches Problem 4's wording, which the children have already used.

**7. Grades 4-5, p. 1, Problem 1.**
- **Text and diagram:** Eight lettered copies A to H, while the board has 6 coverings.
- **What went wrong:** All three children believed there were 8 coverings. Maya spent 3 to 4 minutes hunting and filled G with a mis-copy. That duplicate then went into Problem 2's graph as an extra vertex. The completeness explanation stalled, because the printed letters contradicted it.
- **Smallest fix:** Print six copies, A to F. Completeness is still the question: "Explain how you know that you have found them all."

**8. Grades 4-5, pp. 3-4, Problems 3 and 4.**
- **Text and diagram:** Problem 3 says "For the first pair, explain why it cannot be done in fewer moves." Problem 4 says "...or explain why it cannot be done."
- **What went wrong:** Both explanations are asked for before the children have any tool for them. The chains, and the fact that a move swaps one adjacent LR pair, arrive only in Problems 5 to 7. Maya's natural argument (12 blocks differ, 3 per move) gives 4, not 8. For 5 and 7 she could only write "we couldn't." The fourth graders stalled at the same sentence.
- **Smallest fix:** Move Problem 4 to after Problem 7. Move Problem 3's last sentence into it, for example: "...Also explain why pair 1 of Problem 3 cannot be done in fewer moves."

**9. Grades 4-5, p. 4, Problem 4.**
- **Text and diagram:** "For each number, draw the coverings you pass through," with 8 small copies at 0.4-inch edges.
- **What went wrong:** A 4-move trip and a 6-move trip need 10 drawings. Maya ran out of copies partway through the 6-move trip, and the blank back cannot hold freehand hexagons. Copying 12-block coverings at that size also wore her out.
- **Smallest fix:** Add a third row of four copies (12 in all). The lower half of the page is empty.

## Quick child's engaged minutes (out of about 40 working minutes)

- **K-1 (Cora, grade 1):** about 33. She lost roughly 4 minutes hunting nonexistent coverings in Problem 4, about 2 minutes to the small target and setup in Problem 5, and about 1 minute to the game-rule dispute. She did not run out of work.
- **Grades 2-3 (Theo):** about 34. He lost roughly 1.5 minutes to forced line-drawing in Problem 1, about 2 minutes stuck at the start of Problem 4, and about 2 minutes on the misread of Problem 7. He did not run out of work.
- **Grades 4-5 (Maya, grade 5):** about 31. She lost roughly 4 minutes to the phantom G and H in Problem 1, about 2 minutes stalled on the Problem 3 explanation, and about 3 minutes of copying fatigue and running out of copies in Problem 4. She did not run out of work and reached Problem 5.


=================== Report 3: mathematical check ===================

# Mathematical review: Week 1 Tiling packets (base/)

Method: I parsed every TikZ figure in `src/figs/` back into lattice cells, pieces and shaded holes, using my own code (`scratch/geo.py`, `scratch/solve.py`, `scratch/flip.py`, `scratch/offgrid.py`) rather than the author's `tri.py`. I then enumerated tilings, maximum packings, flip graphs, chains and game positions from those coordinates. Rebuilding the sources reproduces `base/*.pdf` pixel for pixel at 50 dpi, so the parsed figures are the printed ones. Every board meant to carry physical blocks measures at actual size (1 inch per small edge) on the rendered pages.

## Problems found

### 1. K–1, page 6, Problem 6: the hexagon game has the opposite answer under the page's own rule (serious)

Text: "In every problem, blocks must stay inside the shape and must not overlap." / "Take turns with a partner putting one green block or one blue block on the shape; whoever puts down the last block wins. For each shape, would you rather go first or second?" Diagrams: hexagon (6 triangles), parallelogram strip (6), trapezoid strip (5).

Intended answers, with blocks placed on the grid triangles: hexagon **second**, 6-strip **first**, 5-strip **first**. My game search over grid placements confirms this. The hexagon is Kayles on a 6-cycle, so the second player wins.

The K–1 packet never says that blocks go along the lines. The 2–3 packet does say so, and the K–1 packet does not. Under the printed rule, the first player wins the hexagon in one move:
- Lay a blue block across the centre of the hexagon, so its long diagonal runs from the midpoint of the bottom edge (0.5, 0) to the midpoint of the top edge (0.5, 1.732), with its other corners at (0, 0.866) and (1, 0.866).
- That is a genuine 1-inch, 60° rhombus, and it lies inside the hexagon.
- What is left is two thin bent strips, each 0.43 in thick. A search over 1.6 million positions and angles finds no green triangle that fits in either strip, so no further block can be placed.
- Even if a block did fit, the rhombus is centred on the hexagon's centre, so the first player could copy each opponent move by a half-turn and still win.

A kindergartner putting a blue block "standing up in the middle" is a very likely first move. The two strips stay first-player wins in the free-placement game too, by mirror play after a centred first move. So only the hexagon flips, and it is the one contrasting case.

**Fix:** add "along the lines" to the K–1 packet rule: "In every problem, blocks go on the lines of the shape, stay inside it, and must not overlap." This matches the 2–3 packet rule. The covering problems (P1–P5) need no change, because exact coverings of these lattice regions are forced onto the grid.

### 2. Grades 4–5, page 1, Problem 1 (with Problem 2): "find every way" next to eight lettered slots, and "different" is undefined (minor)

Text: "Find every different way to do it, and draw each way in one of the small copies below." Below the text are eight copies, pre-labelled **A–H**. Problem 2 then says "write the letters of your coverings from Problem 1".

The board (hexagon with sides 2, 2, 1) has exactly **6** blue coverings. The eight printed letters suggest 8, and G and H would stay empty. The board also has 4 symmetries (half-turn and two reflections). Counting turned or flipped copies as the same gives **3** coverings. A child who counts that way gets 3 vertices in Problem 2 instead of the intended graph: 6 coverings and 6 moves, a 4-cycle with two pendant coverings.

**Fix:** remove the pre-printed letters, so children letter the coverings they find. Then add one sentence to Problem 1: "Coverings count as different when the blocks sit in different places on this board."

### 3. K–1, page 4, Problem 4: copy counts imply more ways than exist (minor)

Text: "Find every way to cover the hexagon with blue blocks, and every way to cover the long shape. Draw each way in a different copy." The page shows 3 hexagon copies and 4 long-shape copies.

True counts: hexagon **2**, long shape (sides 2, 1, 1) **3**. Pre-readers treat "fill every box" as the task, so the extra copy invites a repeated drawing. The same "turned copy" issue applies here: the hexagon's two coverings are 60° turns of each other, and the long shape has 2 coverings up to symmetry.

**Fix:** keep the copies and add a short sentence such as "Some copies may stay empty." If the organizer prefers fixed counts on the board, use 2 hexagon copies and 3 long-shape copies instead.

### 4. Grades 4–5, page 4, Problem 4: not enough recording copies for a full answer (minor)

Text: "Can this be done in exactly 4 moves? In 5? In 6? In 7? For each number, draw the coverings you pass through, or explain why it cannot be done." The page gives 8 copies.

Answers: 4 **yes**, 5 **no**, 6 **yes**, 7 **no**. The flip graph has 20 coverings and 32 moves, and it is bipartite, because each move changes the cube count by one. There are 120 closed 4-move walks with no immediate undo and 756 such 6-move walks, including simple 6-cycles. Drawing both round trips takes 4 + 6 = 10 coverings, which is more than the 8 copies printed.

**Fix:** add "If you run out of copies, you can draw more on the back." (as in Problem 9), or print 10 copies.

## Problems checked with no error found

**K–1:**
- P1: hexagon yes, small triangle no (3 up / 1 down), chevron yes, boat no (4/2), 2×2 rhombus yes, trapezoid no (7/5). All areas are even, so parity alone never decides a board.
- P2: fewest greens 2, 3, 4.
- P3: fewest greens 5.
- P5: pair 1 takes 2 moves (two shortest routes). Pair 2 takes 4 moves, and its start has exactly one available move. The move picture shows the two fillings of a hexagon.

**Grades 2–3:** this band checks out completely.
- P1: A yes (1 way), B no (5/3), C yes (3 ways), D no (6/4), E no (7/5), F yes (1 way).
- P2: fewest greens 2, 3, 4, 5.
- P3: A yes, B no (two up-holes), C no (two down-holes), D yes. Every one-up/one-down hole pair in this hexagon is coverable, 144 of 144.
- P4: 10 up and 6 down triangles, so at least 4 greens.
- P5: 10 and 100 greens, and both are attainable.
- P6: blue row 2, 3, 4, 5; purple row 4, 5, 4, 5. Answer: no.
- P7: possible. For example, take triangle B (side 3) and add one down triangle and two up triangles along its lower right. That gives 12 connected triangles, 8 up and 4 down, so at least 4 greens. There are 3 such shapes inside triangle C.

**Grades 4–5:**
- P2: graph has 6 vertices and 6 edges.
- P3: pair 1 takes 8 moves, and fewer is impossible because each move swaps one adjacent pair in one chain, and each chain LLRR→RRLL needs 4 swaps. Pair 2 takes 4 moves.
- P5: the shaded example is the left chain and reads RLLR, matching the L/R pictures. The answers are A (LLRR, RRLL), B (LRLR, RLRL), C (LRRL, LRRL) and D (RRLL, RRLL).
- P6: LRLR/RRLL is possible, RRLL/LLRR is impossible, RLRL/RLRL is possible, and LRRL/LRLR is impossible because the chains would cross.
- P7: every move changes exactly one chain, by swapping one adjacent LR or RL pair. I checked every move on all three boards.
- P8: 20 coverings, one chain of 3 L and 3 R, C(6,3).
- P9: 20 coverings.
