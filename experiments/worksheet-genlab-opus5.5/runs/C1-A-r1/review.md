=================== Report 1: adversarial review ===================

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


=================== Report 2: simulated classroom session ===================

# Simulated session review: Week 1 Tiling, base draft

I rendered all 20 pages and read the sources. Where a child's likely result depended on the mathematics, I checked it by computer using the author's own solver, run on a scratch copy. Those checks were: random-play outcomes of the K–1 games, how many chevron packings exist, how many greens a board grown from the side-4 triangle can need, and which hexagon coverings lie on a 4-flip cycle.

Cast:
- K–1: Ava (K) and Ben (K) cannot read. Leo (1st grade) reads a few words and is the quick child here. The parent volunteer reads each problem aloud exactly as printed.
- Grades 2–3: Quinn (quick, impatient), Sara (strong), Dev and Lily (middling). A mathematician sits with them.
- Grades 4–5: Ana and Ben (4th grade) and Zoe (fast 5th grader). A mathematician is nearby.

Times are minutes of the 40-minute work block, measured for the quick child.

---

## K–1

**Packet rule and Problem 1 (p.1, Leo 0–6).** The parent reads "sit on the thin lines". Ava sets a blue block straddling a thin line, and the parent nudges it into the triangles. Ava starts the hexagon with a yellow block and Ben starts the chevron with a purple one, because those shapes look like those blocks. The parent rereads "blue blocks", and both shapes are then covered in about a minute. The 2-triangle triangle and the 3-triangle trapezoid get an X quickly: "a little triangle is left over." The 2×2 rhombus is easy. On the 8-triangle trapezoid all three children try about three times, and each time two holes are left in different places. Leo says "it always has two holes." The "say why" is oral and fine. The parent cannot tell whether the 8-triangle board is truly impossible or just unsolved, and accepts the X. Everyone is engaged.

**Problem 2 (p.2, Leo 6–13).** Ben fills the small triangle with 4 greens and writes 4. The parent rereads "as few green blocks as you can", and Ben gets 2. Leo gets 3 on the middle triangle. On the big triangle Leo stands a couple of blues upright, strands extra triangles, gets 6 greens and writes 6. Nothing on the page or from the parent tells him to keep going. Ava writes a backwards 3, which the parent fixes. They are engaged, and the boxes are big enough.

**Problem 3 (p.3, Leo 13–21).** The parent reads "Find all the ways to cover each shape with blue blocks. Put each way on a shape of its own."
- Ava and Ben hear "cover each shape" and cover all three hexagons in the same way, the cube shape they always make.
- The parent says the ways should be different. Leo makes the other way.
- Ben says "that's the same, you just turned it." The page does not say whether a turned way counts, so the parent cannot settle it.
- The third hexagon has no third way (there are 2). The children spend about 3 minutes on it. Leo rebuilds an earlier way and calls it new. The parent sees that it is the same, and Leo sulks.
- The long shapes go the same way: three ways are found in about 4 minutes, and the fourth copy cannot be filled because only 3 ways exist.
- About 5 engaged minutes, then about 3 frustrated ones.

**Problem 4 (p.4, Leo 21–27).** The children reach for pink, teal and gray pieces from the tub, and the parent points to the five pictured blocks.
- On the triangle all three put the yellow hexagon in the middle with 3 greens and write 4. Nobody tries three reds, which gives 3.
- On the rhombus Leo remembers "4 blues" from Problem 1 and writes 4. Ava finds yellow plus 2 greens and writes 3.
- On the trapezoid they get yellow, red, blue and green, which is 4.

The answers are mixed. The children are engaged.

**Problem 5 (p.5, Leo 27–35).** There are three children, so Ava plays Ben, and Leo plays the parent.
- Each board gets one or two quick games, and they circle whoever won the last one. "To be sure to win" does not land after one hearing.
- Ava and Ben cannot read "first" and "second". Ben circles the left-hand word because it comes first, and Ava circles at random. Leo can read "first" and gets the left word on purpose.
- On the 4-strip the first player wins only by playing the middle, and wins just 1/3 of random games. On the hexagon the second player wins by replying opposite, but the first player wins 2/3 of random games. So two of the five boards are likely circled wrong, and the parent cannot check.

The games are the most popular part of the hour.

**Problem 6 (p.6, Leo 35–40).** Leo builds one way of covering the big shape with 8 blues in about 2 minutes. Then: "Draw each way on a small shape."
- The small shapes have half-size triangles, so the blocks do not fit on them.
- Leo tries to trace block outlines along the gray lines with a pencil. The lines wander, and his drawing cannot be read even by him.
- After one more attempt he stops.

Ava and Ben are still on Problem 5 at minute 40 and never reach this page.

Leo is still working at minute 40 and does not run out of work. His dead time is the phantom third and fourth ways in Problem 3 and the drawing in Problem 6.

---

## Grades 2–3

**Packet rule and Problem 1 (p.1, Quinn 0–6).**
- On the star (A), Quinn sees that each point has only one neighbor, and covers it in 1 minute.
- On B: "Nine, that's odd," in 1 minute.
- D takes 1 minute.
- On C, three attempts each leave two triangles, and Quinn writes "C: always 2 left."

Dev and Lily take about 10 minutes for this problem. The mathematician probes C. The children are engaged, and the 4 lines are enough.

**Problem 2 (p.2, Quinn 6–13).**
- E: three attempts, then "always 2 left."
- F: "each half is the little triangle that didn't work," in 1 minute.
- G: covered on the second try.

Sara notices that both holes in E point up and the holes in G do not. Everyone is engaged.

**Problem 3 (pp.3–4, Quinn 13–21).** Quinn builds row by row and gets 2, 3 and 4 in about 4 minutes. Then he hits the last sentence: "Then explain why nobody can cover the biggest triangle with fewer green triangles than you used."
- He takes "the biggest triangle" to be the largest one on page 3, the triangle with 4 on a side, and finds no writing lines on that page.
- He turns over and finds a triangle with a box and lines but no problem number. He asks, "Is this a new one?"
- Once told it belongs to Problem 3, he writes 5 without building it.
- His explanation is "each row has one left over." That is not a reason, because an upright rhombus crosses rows. The mathematician pushes, and Quinn stalls for about 3 minutes and leaves one line.

Dev and Lily never turn to page 4.

**Problem 4 (p.5, Quinn 21–22).** "10. 100." This takes 30 seconds, because the answer is read off the pattern 2, 3, 4, 5. Nothing is left to think about.

**Problem 5 (p.5, Quinn 22–31).** The problem says "Go back to the four triangles in Problem 3," and Dev answers "There were three." Quinn copies 2, 3, 4, 5 into the blue column. Then the chevrons:
- Side 2: no chevron fits, so 4.
- Side 3: one chevron, so 5.
- Side 4: Quinn gets 2 chevrons and writes 8. There are 39 ways to place two chevrons but only 8 ways to place three, which is the minimum.
- Side 5: 4 chevrons, so 9.

His answer: "No, a chevron is just two blues." The conclusion is right even though some numbers are not minimal. He is engaged.

**Problem 6 (p.6, Quinn 31–38).** Quinn's natural first idea is the side-4 triangle (which needs 4 greens) plus 4 more triangles.
- I checked by computer: every board made that way needs at most 4 greens.
- Two attempts take about 5 minutes. Each needs counting 20 triangles on the grid and covering with about 10 blocks.
- He then draws a blob, covers it sloppily with 6 greens, and announces he is done. The mathematician has to check it by hand.

He stalls for about 4 minutes in all.

**Problem 7 (p.7, Quinn 38–40).** Quinn places the first pair of greens. Nobody else reaches this problem.

Quinn is still working at minute 40. His dead time is the explanation stall in Problem 3, the empty minute in Problem 4, and the stall in Problem 6.

---

## Grades 4–5

**Packet rule and Problem 1 (p.1, Zoe 0–13).** Zoe covers the 16-triangle board with 8 blues in 1 minute.
- She draws each covering by darkening grid lines on the 0.4-inch small boards, about 1 minute each.
- Moving blues around, she has all 6 coverings in about 8 minutes.
- Ten boards are printed, so she says "There must be ten." She hunts for 3 minutes.
- Ana draws a mirror image that is already on the sheet. Ben's drawing has a misplaced rhombus.
- Zoe writes "we couldn't find any more."

**Problem 2 (p.2, Zoe 13–23).** The flip picture is clear. Then: "draw all your coverings from Problem 1 again." Zoe asks "Again?" and copies six drawings in about 6 bored minutes. Ana and Ben stop after three.
- The coverings went into the fixed 2×4 grid in the order they were drawn, so flip lines run across other drawings.
- Zoe still reads off the farthest pair (4 flips) in about 3 minutes. The 4th graders' graphs cannot be read.

**Problem 3 (p.3, Zoe 23–38).** Zoe reads covering A off a 1.4-inch picture that has no grid lines and builds it at actual size in 2 minutes. Ana copies one rhombus the wrong way round, so her count is for a different pair.
- A→B: Zoe finds 3 flips after an attempt with 5.
- C→D: 4 flips.
- E→F: 8 flips.

She is fully engaged. At the end, covering F is on her board.

**Problem 4 (p.4, Zoe 38–40).** The problem reads "Start with any covering of the hexagon board from Problem 3." Zoe uses F, which is already on the board.
- F (like E) has exactly one flippable hexagon. Any 4-flip round trip from F must repeat a flip twice in a row. I checked this: E and F are the only coverings of the 20 that lie on no 4-flip cycle.
- After 2 minutes Zoe says "4 is impossible."

Time runs out. Ana and Ben are partway through Problem 3. **No one reaches Problems 5–8, the ribbons.**

---

## Problems the simulation exposed

**1. K–1, p.5, Problem 5: the game question cannot be read or answered as intended.**
- **Text:** "circle whether you should go first or second to be sure to win," with the printed words "first" and "second" beside each board.
- **What happened:** The kindergartners could not tell the two words apart. The children played once or twice and circled whoever won last. Random play misleads on the 4-strip (first player wins only 1/3 of random games, but first is correct) and on the hexagon (first wins 2/3, but second is correct). The parent cannot check.
- **Smallest fix:** Print a large "1" and "2" in place of the words. Change the question to "Who can always win on this board, the 1st player or the 2nd player? Circle 1 or 2."

**2. K–1, p.6, Problem 6: recording at half size.**
- **Text:** "Draw each way on a small shape," with eight half-size copies.
- **What happened:** The blocks do not fit the small shapes, and a 6-year-old cannot draw rhombi on half-inch triangles. Leo's drawings could not be read, and he quit after two.
- **Smallest fix:** Replace the eight small copies with six actual-size copies over two pages. Use the wording from Problem 3: "Put each way on a shape of its own."

**3. K–1, p.3, Problem 3: more shapes than ways.**
- **Text:** "Find all the ways to cover each shape … Put each way on a shape of its own," with three hexagons (2 ways exist) and four long shapes (3 ways exist).
- **What happened:** The children covered every copy the same way. Then they spent minutes chasing a third and fourth way that do not exist, and ended thinking they had failed. The parent could not settle "a turned one is the same."
- **Smallest fix:** Print 2 hexagons and 3 long shapes, and add "Make every shape a different way." This trades "know you have them all" for closure that K–1 children and a non-mathematician parent can manage.

**4. Grades 2–3, pp.3–4, Problem 3: the fourth triangle is lost.**
- **Text:** "explain why nobody can cover the biggest triangle with fewer green triangles than you used." The page shows sides 2, 3 and 4. The side-5 triangle, its box and its writing lines are on page 4 with no label.
- **What happened:** Quinn took "biggest" to mean the side-4 triangle and asked whether page 4 was a new problem. Dev and Lily never found page 4. Problem 5's "the four triangles in Problem 3" then confused them.
- **Smallest fix:** Change the sentence to "explain why nobody can cover the triangle on the next page with fewer green triangles than you used." Add "There are four triangles, three on this page and one on the next."

**5. Grades 2–3, p.5, Problem 4: a 30-second problem.**
- **Text:** "Imagine a triangle board with 10 small triangles along each side … What if the board has 100 …?"
- **What happened:** Quinn wrote "10, 100" at once from the pattern in Problem 3. Nothing was left to think about.
- **Smallest fix:** Delete Problem 4. If the large cases are wanted, add them to Problem 3's explanation sentence ("…or a triangle with 100 on each side…").

**6. Grades 2–3, p.6, Problem 6: the natural route is closed.**
- **Text:** "draw the outline of a board made of exactly 20 small triangles that needs at least 6 green triangles."
- **What happened:** Quinn grew the side-4 triangle from Problem 3. Every 20-triangle board made that way needs at most 4 greens. After two slow attempts he gave up and claimed a sloppily covered blob.
- **Smallest fix:** Change the numbers to "exactly 19 small triangles that needs at least 5 green triangles." That target is reachable by adding three triangles to the side-4 triangle, so the first idea pays off and the child still needs the up/down reason to explain it. If the organizer wants the harder 20/6 version, the adult should expect to step in.

**7. Grades 4–5, p.2, Problem 2: forced recopying.**
- **Text:** "On the small boards below, draw all your coverings from Problem 1 again. Draw a line between two coverings whenever one flip changes one into the other."
- **What happened:** It took about 6 minutes of pure copying. The 4th graders quit partway. Because the boards sit in a fixed 2×4 grid, the flip lines cross other drawings, and the 4th graders' graphs could not be read.
- **Smallest fix:** "Give each of your coverings in Problem 1 a letter. Below, write the letters and draw a line between two letters whenever one flip changes one covering into the other." Replace the eight small boards with blank space.

**8. Grades 4–5, p.4, Problem 4: the obvious start is the one covering where it fails.**
- **Text:** "Start with any covering of the hexagon board from Problem 3 … Find a way to do this with 4 flips that never flips the same hexagon twice in a row."
- **What happened:** Zoe started from F, which was left on the board after Problem 3. F and E each allow only one flip, so no valid 4-flip round trip exists from them. Zoe concluded 4 is impossible.
- **Smallest fix:** "Start with covering A from Problem 3." A lies on a 4-flip cycle.

**9. Grades 4–5, p.1, Problem 1: more boards than coverings.**
- **Text:** "Find all the different ways to do it, and draw each way on one of the small boards," with ten small boards (6 coverings exist).
- **What happened:** Zoe hunted for 3 minutes for four more. Ana drew a mirror image that was already there, and Ben drew an invalid one. These would have been carried into the Problem 2 graph.
- **Smallest fix:** Print 6 small boards. "Explain how you know you have found them all" still stands as the real question.

**10. Grades 4–5, p.3, Problem 3: the target pictures are hard to copy.**
- **Text:** Coverings A–F are drawn at about 1.4 inches with no grid lines.
- **What happened:** Ana copied one rhombus the wrong way round onto the actual-size board, so her flip count was for a different pair, and nobody noticed.
- **Smallest fix:** Draw faint grid lines inside the six covering pictures, as on the small boards.

---

## Quick child's engaged minutes (of 40)

- **K–1 (Leo): about 34.** He never runs out of work. He loses about 3 minutes chasing ways that do not exist in Problem 3 and about 3 minutes on the unusable drawing in Problem 6.
- **Grades 2–3 (Quinn): about 33.** He never runs out of work and reaches Problem 7 at about minute 38. He loses about 3 minutes stalled on the Problem 3 explanation, gets 1 minute from Problem 4, and stalls about 4 minutes in Problem 6.
- **Grades 4–5 (Zoe): about 30.** She never runs out of work, but loses about 3 minutes hunting phantom coverings in Problem 1, about 6 copying in Problem 2, and about 2 stuck at F in Problem 4. She never reaches the ribbon problems (5–8). Fixes 7–9 would save about 10 minutes and get her to Problem 5 by about minute 30.


=================== Report 3: mathematical check ===================

# Correctness review: Week 1 tiling packets (C1-A-r1 base draft)

## Method

I rendered all 20 pages (K–1: 6, grades 2–3: 7, grades 4–5: 7) and looked at each one. I rebuilt every board from the printed TikZ figure files (`src/figs/*.tex`). I parsed the drawn segments, holes and filled tiles back into triangular-lattice coordinates, so every check below is on what actually prints and not on `gen.py`'s region definitions. I then re-checked everything with my own solvers (scripts in `scratch/geo.py`, `k1.py`, `g23.py`, `chev.py`, `p7.py`, `g45.py`, `p4.py`, `rib.py`):

- exhaustive blue-rhombus tiling enumeration
- bipartite up/down matching
- exact minimum-cover search, with pieces classified from geometry: chevron = 4 edge-connected triangles sharing a vertex, hexagon = 6 around a vertex, trapezoid = any 3-triangle chain
- memoized normal-play game search
- flip graphs with BFS distances
- enumeration of closed flip walks
- ribbon reading

Every board that children put physical blocks on prints at 1 inch per triangle edge (80 px per edge at 80 dpi, on a Letter page at 612×792 pt with no scaling).

---

## Located problems

### 1. Grades 4–5, page 4, Problem 4: the task cannot be done from two of the six pictured coverings, including the one left on the board after Problem 3

**Text:** "Start with any covering of the hexagon board from Problem 3. Make flips, one at a time, until you are back at the covering you started with. Find a way to do this with 4 flips that never flips the same hexagon twice in a row."

**Evidence:** I built the flip graph of the side-2 hexagon. It has 20 coverings and is bipartite. Then I listed every closed walk of length 4 from each covering, keeping only walks where two flips in a row never use the same hexagon.

- 18 coverings have such a walk.
- Coverings **E** (ribbons RRLL, RRLL) and **F** (ribbons LLRR, LLRR) have **none**.

Each of E and F has exactly one flippable hexagon, the central one. So the first and last flips must both use it, and flips 2 and 3 are forced to be the same hexagon done and undone (a hexagon flipped twice in a row).

The shortest allowed round trip from E or F takes 6 flips. A child who goes on from Problem 3 has covering F on the board, which is a natural reading of "any covering … from Problem 3". That child gets a task that cannot be done, and the page does not say so. Covering A has 3 flippable hexagons and 6 valid 4-flip round trips.

**Smallest fix:** change the first sentence to "Start with covering A from Problem 3." Another option is "Start with covering A, B, C or D from Problem 3." Coverings B, C and D also have valid 4-flip round trips (8, 2 and 2 of them).

### 2. K–1, page 3, Problem 3, and page 6, Problem 6 (minor): there are more blank shapes than ways, and the count depends on whether turned pictures count as new

**Text:** "Find all the ways to cover each shape with blue blocks. Put each way on a shape of its own." The page prints 3 hexagons and 4 long hexagons. Problem 6 ("Find all the ways … Draw each way on a small shape.") prints 8 small shapes.

**Evidence:**
- Exhaustive enumeration gives exactly **2** coverings of the hexagon, **3** of the long hexagon (top and bottom sides 2, slanted sides 1), and **6** of the Problem 6 shape.
- Children who cannot read take the number of blank shapes as the target. On the hexagon they will look for a third way that does not exist, or draw a repeat to fill the last shape.
- The two hexagon coverings are the same picture turned 60°. Two of the three long-hexagon coverings are mirror images. A child who counts "the same, just turned" as one way gets 1 and 2, and the page does not say which count is meant.

The mathematics is right, but the page suggests a different count than the true one.

**Smallest fix (pick one):**
- Add one sentence to each problem: "Some shapes may stay empty."
- Print exactly 2 hexagons and 3 long hexagons in Problem 3.

The adult at the table should know that turned copies count as different ways on the printed shape.

### 3. Grades 4–5, page 5, Problem 6 (minor wording): the second sentence assumes the child's Problem 3 answer is the true minimum

**Text:** "Then explain why nobody can change covering E into covering F in Problem 3 with fewer flips than your answer."

**Evidence:** The true minimum from E to F is 8 flips. This is the BFS distance, and it is also the ribbon lower bound: each ribbon must go from RRLL to LLRR, which takes 4 adjacent swaps, and each flip makes exactly one adjacent swap in one ribbon. A child who wrote 10 in the Problem 3 box is asked to explain something false.

**Smallest fix:** "Then find the fewest flips that change covering E into covering F, and explain why nobody can do it with fewer." This keeps the answer hidden and makes the claim true for every child.

The same presupposition is in grades 2–3 Problem 3: "explain why nobody can cover the biggest triangle with fewer green triangles than you used". It is harmless there, because a child who used more than 5 finds out when the explanation fails. You can leave it.

---

## Band-by-band verification (everything not listed above checks out)

### K–1: correct apart from note 2

| Problem | Intended answer | Verified |
|---|---|---|
| P1: cover with blues or X | hexagon yes; triangle of side 2 no (3 up, 1 down); side-2 rhombus yes (1 way); trapezoid no (3 triangles); chevron yes (1 way); 8-triangle trapezoid no (5 up, 3 down, so even area but impossible) | yes |
| P2: fewest greens on triangles of side 2, 3, 4 | 2, 3, 4 | yes (minimum cover) |
| P3: all ways | hexagon 2, long hexagon 3 | yes |
| P4: fewest blocks (G, B, R, Y, P) | side-3 triangle 3 (three trapezoids; hexagon + 3 greens = 4; no 2-piece cover); side-2 rhombus 3 (two chevrons cannot fit, since only the centre vertex has 4 triangles around it); double trapezoid 4 (7 up, 5 down rules out three chevrons; hexagon leaves an isolated corner) | yes |
| P5: blue-block game, last move wins | strip 4: first (cover the middle pair); strip 5: second; strip 6: first (cover the middle pair); strip 7: first; hexagon: second | yes (full game search; matches Dawson's Kayles values 2, 0, 3, 1 and the 6-cycle) |
| P6: all ways on the (1,2,2) hexagon | 6 | yes |

### Grades 2–3: checks out completely

| Problem | Intended answer | Verified |
|---|---|---|
| P1 | A star: yes (12 triangles, 6/6, exactly 1 covering); B side-3 triangle: no (6 up, 3 down); C double trapezoid: no (7 up, 5 down); D long hexagon: yes (3 coverings) | yes |
| P2 | E (holes are two up-triangles): no (10 up, 12 down); F hourglass: no (balanced 4/4, but its halves touch only at a point and each is a side-2 triangle with an imbalance of 2); G (one up hole, one down hole): yes (4 coverings) | yes; hole orientations in the drawings match |
| P3 | sides 2, 3, 4, 5 need 2, 3, 4, 5 greens; lower bound is the number of up-triangles minus down-triangles | yes (matching and exact search) |
| P4 | 10 and 100 (leave one up-triangle per row) | yes |
| P5 table | blues: 2, 3, 4, 5; chevrons: 4, 5, 4, 5 (most chevrons that fit: 0, 1, 3, 5); chevrons never do better, because each splits into two blues | yes (brute force over all chevron placements) |
| P6 | possible, e.g. a 13-triangle row strip with 6 up-triangles above it and 1 more triangle: 20 triangles, 13 up, 7 down, edge-connected, fits on the 7-inch actual-size grid | yes |
| P7 | rule: works exactly when one green points up and one points down | yes, all 144 up/down pairs give a coverable board and none of the 132 same-direction pairs do |

### Grades 4–5: correct apart from notes 1 and 3

| Problem | Intended answer | Verified |
|---|---|---|
| P1 | 6 coverings of the (1,2,2) hexagon | yes |
| P2 | flip graph has 6 coverings, 6 edges, degrees 1, 1, 2, 2, 3, 3; the unique farthest pair is 4 flips apart (ribbons LLRR and RRLL) | yes |
| P3 | the A–F pictures are valid coverings of the side-2 hexagon; fewest flips A→B = 3, C→D = 4, E→F = 8 (E→F is the largest distance in the graph) | yes (BFS) |
| P4 | 4-flip round trip exists from 18 of 20 coverings (see note 1); 5 and 7 are impossible because the flip graph is bipartite | yes |
| P5 | L and R pictures match the definition; the example on the (1,3,2) board is a valid covering whose followed chain reads LRRLR, with every label on the correct rhombus; the 6 coverings from Problem 1 have the 6 distinct ribbons with two L and two R; on the side-2 hexagon the 20 coverings have 20 distinct ribbon pairs, and every flip swaps one adjacent LR pair in exactly one ribbon | yes |
| P6 | round trips are even (each flip changes the total count of R-before-L pairs by exactly 1); E→F needs 8 | yes |
| P7 | 20 coverings (25 small hexagons given) | yes |
| P8 | (1,3,3) hexagon: 30 triangles, 20 coverings (one ribbon with three L and three R, so C(6,3) = 20) | yes |
