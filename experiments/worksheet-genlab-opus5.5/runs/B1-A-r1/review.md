# Review of the Week 1 tiling packet (draft in base/)

## How I checked it

- I rendered all 20 pages (K–1: 6, grades 2–3: 7, grades 4–5: 7) and looked at each one, with high-resolution crops of the 4–5 flip picture, the pairs A–F and the ribbon example.
- I measured the boards in the renders. Every board a child puts blocks on is at actual size, with a 1-inch small-triangle edge (for example the side-2 hexagon is 4.0 in wide and the 1,3,3 board is 5.2 in tall). Pages are US Letter. I recompiled all three sources in scratch/build: there are no overfull or underfull boxes, only harmless math-font size substitutions.
- I wrote my own solver (scratch/verify.py) that rebuilds every board and every drawn covering from the figure .tex files, rather than from the author's gen.py, and re-derived each answer. Everything the pages rely on is correct:
  - **K–1 P1:** coverable, not, coverable, not, coverable, not. The 8-triangle trapezoid has 5 up and 3 down triangles.
  - **K–1 P2:** fewest greens 2, 3, 4.
  - **K–1 P3:** 2 and 3 coverings.
  - **K–1 P4:** fewest blocks 3, 3, 4, with or without purple.
  - **K–1 P5:** first, second, first, first, second.
  - **K–1 P6 / 4–5 P1:** 6 coverings.
  - **2–3 P1:** A yes (1 way), B no (odd area), C no (7 up, 5 down), D yes.
  - **2–3 P2:** E no (both holes are up-triangles), F no (balanced 4/4 but the halves only touch at a point), G yes (4 ways).
  - **2–3 P3:** 2, 3, 4, 5. **2–3 P5** with chevrons: 4, 5, 4, 5.
  - **2–3 P6:** feasible. The author's comb works, and so do two side-3 triangles joined by one down-triangle plus one up-triangle. This 13-up/7-down board is also the largest imbalance a connected 20-triangle board can have, so the problem is an extremal construction.
  - **2–3 P7:** all 144 up/down pairs are coverable and no same-direction pair is.
  - **4–5:**
    - The 1,2,2 flip graph has diameter 4.
    - Side-2 hexagon: 20 coverings, flip graph diameter 8.
    - Pairs A→B = 3, C→D = 4, E→F = 8.
    - Every flip swaps one adjacent LR pair in exactly one ribbon.
    - The ribbon example reads LRRLR and the L/R icons match it.
    - The 1,3,3 board has 20 coverings.

The mathematics, the diagrams and the actual-size boards are sound. The problems below are about whether a child at the table can do what each page asks and whether the answer comes out as the author intends.

---

## Serious problems

### 1. The upscale blocks break the "fewest" problems, and no page excludes them (all three packets)
The materials list puts 2× and 3× pattern blocks in the room, and children will have handled them during free play. The packet rules only say that blocks must fit inside the outline and "sit on the thin lines" (K–1) or "cover whole small triangles of the board" (2–3, 4–5). Upscale blocks satisfy both rules.

- **K–1 Problem 4:** all three boards are single upscale blocks. The big triangle is a 3× green, the rhombus is a 2× blue, and the trapezoid is a 2× red (the source even calls it `trap2x`). Under the stated rules each answer is 1, not 3, 3, 4. "You may use any of these blocks" does not prevent this, because the icons are not to scale and a 2× blue is still a blue block.
- **K–1 Problem 2 and 2–3 Problem 3:** the side-2 and side-3 triangles are exactly a 2× and a 3× green, so "fewest green" becomes 1. The side-4 triangle needs only 2 greens (a 3× green plus one small green), and the side-5 triangle needs 2 (a 3× and a 2× green). I checked these with the solver: the fewest greens go from 2, 3, 4, 5 to 1, 1, 2, 2. The pattern "n greens for side n", which 2–3 Problems 4 and 5 build on, disappears. The up/down argument also no longer gives a lower bound, because a 2× green covers 3 up and 1 down.
- **2–3 Problems 5–7:** these depend on green counts in the same way.
- **4–5 Problems 1, 7 and 8:** a 2× blue fits in every corner-cube covering, so "all the different ways" gains extra coverings.

**Fix:** state once, in the packet rule at the top of page 1, that only the small blocks are used, for example "Use only the small blocks." The other way is to say "small" in the problem text wherever counts matter.

### 2. 4–5 Problem 4 cannot be done from the covering the child most likely starts with
"Start with any covering of the hexagon board from Problem 3. … Find a way to do this with 4 flips that never flips the same hexagon twice in a row."

- Of the 20 coverings, exactly two have only one possible flip: E and F, the two "big cube" coverings. From those two, a 4-flip round trip without an immediate repeat is impossible, because the walk has to leave and return through the same single neighbor.
- Problem 3 ends with the board in covering F. A child who starts with what is on the board, or with the most natural-looking covering, is stuck on an impossible task. "Any" also reads as "every", which is false.
- The author's check in gen.py (`c4 > 0`) only shows that some 4-cycle exists somewhere, so it missed this.

**Fix:** name a specific starting covering that lies on a 4-cycle, such as A or C (both verified), or say "Choose a covering".

### 3. 2–3 Problem 7 asks third graders to prove the hard direction
"Find a rule that tells which places for the two green triangles work, and explain why your rule is right."

- The correct rule is one up-triangle and one down-triangle. Its "never works" half is the counting argument the packet has been building.
- Its "always works" half means showing that all 144 up/down placements can be covered. A third grader has no argument for that beyond exhaustive cases.
- As written, a careful child cannot finish the explanation, and a less careful one will think a few examples prove the rule.

**Fix:** ask for the rule and for an explanation of why the other placements can never work. Or ask "Which places work? Explain why the ones that fail can never work."

### 4. K–1 pre-readers are asked to record by fine drawing (K–1 Problem 6, partly Problem 3)
- **Problem 6** asks kindergartners to draw each of 6 coverings, each with 8 rhombi, on half-size copies whose triangles have 0.5-inch edges. That is a drawing task beyond most 5-year-olds. The standard asks K–1 pages to "lean on pictures and objects".
- The mathematics of finding all 6 ways is fine for K–1. The recording is the problem.
- **Problem 3** avoids this by putting blocks on actual-size copies.

**Fix:** use actual-size copies for Problem 6 as well, spread over two pages if necessary, so each way can be built and left in place. Or allow colouring instead of line drawing.

---

## Moderate problems

### 5. K–1 Problem 1 gives away its answers in the layout
- Every shape in the left column (hexagon, rhombus, chevron) can be covered, and every shape in the right column (side-2 triangle, 3-triangle trapezoid, 8-triangle trapezoid) cannot.
- Children notice that kind of pattern quickly, and it removes the decision the problem is about.

**Fix:** mix the order, for example by swapping the shapes in the middle row.

### 6. 4–5 Problem 2 is busywork and tells the child the method
- **Busywork:** "On the small boards below, draw all your coverings from Problem 1 again" makes the child copy six coverings that are already drawn on page 1.
- **Method:** "Draw a line between two coverings whenever one flip changes one into the other" hands over the way to organise the work, which is the graph. The question that carries the mathematics is "Which two coverings need the most flips to get from one to the other?"
- The standard keeps method suggestions with the adult.
- The 2×4 grid of boards also makes drawing graph edges awkward: lines between non-neighbouring boards cross other boards.

**Fix:** ask the question directly, with blank space or small boards the child can arrange freely. Leave the graph idea to the adult.

### 7. 4–5 Problem 4 has nowhere to record a flip sequence
The problem asks the child to find a 4-flip round trip, but it gives only two ruled lines and no hexagon outlines. A sequence of coverings or flip locations cannot reasonably be written in words. The standard requires "the diagrams the child needs" and "space to record".

**Fix:** add five small side-2 hexagons in a row (start, after 1, 2, 3, 4 flips).

### 8. 4–5 Problems 2 and 5 name the ideas before the child has used them
- **Problem 2** names "flip" before the child has made one.
- **Problem 5** opens with a six-sentence definition (short edge, flat bottom edge, go down, L/R, "ribbon") before any task. The standard says a new word or notation should come "only after the child has used the idea it names".
- Problem 5 also introduces the tool that Problems 6–8 are designed to need, so it comes close to handing over the solution idea. Ribbons are in the outline's kernel, so including them is right, but how they are introduced matters.

**Fix:** let the child flip first. In Problem 1 or Problem 3 they will meet three rhombi that make a hexagon, and the name can follow. For ribbons, trim the definition to the essential rule plus the worked picture, and keep the sentences short.

### 9. K–1 Problem 5 is long for one hearing, and its answer choices are words
- The problem is two sentences of about 20 words each and combines the game rules with a meta-question ("circle whether you should go first or second to be sure to win").
- The answer choices are the printed words "first" and "second", which K–1 children cannot read.

**Fix:** split it, for example: "Take turns putting one blue block on a board. Whoever puts down the last block wins." Then "On each board, should you go first or second to be sure to win? Circle it." Use symbols the children can read (1st/2nd, or one dot and two dots).

### 10. K–1 Problem 3: "each shape" is unclear when 7 outlines are printed
The page shows three copies of one hexagon and four of another. Read aloud, "Find all the ways to cover each shape … Put each way on a shape of its own" does not tell a 5-year-old that there are only two shapes, or which copies belong together. Spare copies are right (the hexagon has 2 ways on 3 copies, the long hexagon 3 ways on 4), but the wording should make the two-shape grouping clear, for example by a visible gap between the two groups and "this shape … this shape".

---

## Minor problems

11. **2–3 page 4 is unlabelled.** It holds only the side-5 triangle, an answer box and writing lines. A child or the parent volunteer who picks up that page cannot tell it belongs to Problem 3. The Problem 3 text says "each big triangle" without saying it continues overleaf. Consider a short reference in the Problem 3 text ("the four triangles on this page and the next").
12. **K–1 rule "sit on the thin lines".** Heard aloud, this can mean "put blocks on top of the lines". "Blocks must match the thin lines" or "line up with the thin lines" says what is meant.
13. **"the fewest number of"** (2–3 P4, 4–5 P3) is awkward. Use "the fewest green triangles" or "the smallest number of flips".
14. **2–3 Problem 4 may run short of the five-minute bar.** A child who has the table 2, 3, 4, 5 answers it in seconds, and it asks for no explanation. Consider merging it into Problem 3 or Problem 5, or asking why the side-10 board cannot do better.
15. **4–5 Problem 7: "Draw them on the small hexagons"** means drawing 20 coverings of 12 rhombi each on 0.3-inch triangles, which takes up most of the remaining time. After Problem 5, a list of ribbon pairs shows the enumeration just as well. Consider "Draw or list them".
16. **4–5 Problem 6, first sentence:** "whenever you make flips and end at the covering you started with" does not name a board. It should say "on the hexagon board".
17. **2–3 explanation load.** Explanations are asked in Problems 1, 2, 3, 5 and 7. Each is a legitimate "why impossible / why best" question, so this is not a violation, but for third graders it is a lot of writing. The adult can take some answers orally, and the page could say "explain" without always adding ruled lines.

---

## Compliance with the organizer's "leave these off" list

- Headers and footers match the required format on every page, with problem labels "Problem N:". There are no other headings, no encouragement, no exclamation marks, no talk about the activity, no mascots or themed names, no em-dash asides, no "not X but Y" constructions, and no lettered sub-steps.
- The packet-wide rule appears once, at the top of page 1 of each band.
- Page counts (6, 7 and 7) meet the "four or more pages" expectation, and each band has more than enough for 40 minutes.
- The only items close to the list are the method instruction in 4–5 Problem 2 (item 6) and the definition-first vocabulary in 4–5 Problems 2 and 5 (item 8).

## What works and should be kept

- K–1 gets real versions of every kernel-1 idea: possible/impossible with an even-area impossible case, fewest greens, all ways, fewest pieces, and a winning-strategy game.
- The 2–3 sequence is well built:
  - Parity-impossible (B) next to colour-impossible (C).
  - A balanced-but-impossible hourglass (F) that shows counting is not sufficient.
  - E and G as concrete cases of the Problem 7 rule.
  - The chevron comparison.
  - An extremal construction.
- The 4–5 pairs A–F (3, 4, 8 flips) give a clean progression into the parity and lower-bound explanation in Problem 6.
