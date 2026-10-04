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
