# Review: Hex, the game with no draws, draft v1

Reviewer stage. I did not edit the draft.

## What I checked

- I rendered all 19 pages (K–1 has 6, 2–3 has 6, 4–5 has 7) at 80 dpi and looked at each one. I also zoomed to 200–250 dpi on the example board, a K–1 play board and the 4–5 boundary-path page. No text or diagram overflows or overlaps anywhere.
- I rebuilt the draft from `draft/src/build.py` in a scratch copy. The generated `.tex` files are byte-identical to `draft/src/*.tex`, and every page renders pixel-identical to `draft/*.pdf`. The pdflatex logs show no overfull or underfull boxes.
- I read the sizes from the TikZ code (all lengths are in mm, with no scaling):
  - Play boards (3×3, 4×4, 5×5) and the square board: 24 mm across the flats.
  - 4–5 Problem 9, the 7×7 board: 22 mm.
  - 2–3 Problem 5 puzzle boards: 14 mm.
  - 4–5 Problem 5 path boards: 16 mm.
  - Recording boards: 13 mm.
  - Example board: 7.5 mm.
- I checked the mathematics with my own solver, not the author's `check_hex.py`, `check_puzzles.py` or `hexsolve.py`. Its adjacency matches the drawing: rows shift right by half a hexagon, and the sharp corners are (0,0) and (n−1,n−1).
  - Full boards: on all 512 full 3×3 boards and all 65,536 full 4×4 boards there is exactly one winner, split 256/256 and 32,768/32,768.
  - 3×3 first moves, (row, column) from the top left: Red wins by opening at (0,2), (1,0), (1,1), (1,2) or (2,0), which is 5 of the 9 cells. Red loses at (0,0), (0,1), (2,1) and (2,2). After Red opens at (0,0), Blue's only winning reply is the centre.
  - Fewest blue counters that stop Red when every other hexagon is red: 3, 4 and 5 on the 3×3, 4×4 and 5×5 boards.
  - Example board: 7 red and 6 blue counters, which is a legal finished game with Red going first. Red has a chain and Blue does not. Every red counter is needed for the chain.
  - Puzzles and boundary paths: see the table below.

**Verdict.** The mathematics is correct on every page, and the packet follows the organizer's format closely. Every band has the correct header and footer, a brief rules block, consecutive "Problem N:" labels and the boards a child needs. There are no titles, encouragement, hints or lettered sub-steps. Each band starts with a game every child can play at once, and in each band the explanation problems come after concrete work on the same idea. The issues are about how the pages work in use:

- **K–1 states three impossible tasks as instructions**, and the adult at that table is a non-mathematician with no guide (A1).
- **4–5 asks for the strategy-stealing argument with no concrete stage before it** (A2).
- **The 2–3 puzzle positions are too small to play on** (A3).
- **2–3 Problem 4 is thin for that band** (A4).
- **The 4–5 boundary path has only the two printed boards**, which is not enough to test the conjecture (A5).
- **The counter size is never stated**, and the 7×7 board is smaller than the outline asks for (A6).

## Answer check, every problem

| Band / problem | What is on the page | Verified outcome |
|---|---|---|
| K–1 P1, P4 | Play on 3×3, then 4×4 | Open play |
| K–1 P2, P5 | Fill 3×3 / 4×4 so nobody wins | Impossible (every full board has a winner) |
| K–1 P3 | Fill 3×3 so both win | Impossible |
| K–1 P6 | 3×3, Red's first counter on the centre star / on the top-left (sharp) corner star | Centre: no, Blue cannot stop Red. Corner: yes, but only by answering in the centre |
| K–1 P7 | Fewest blue, rest red, 3×3 and 4×4 | 3 and 4 (any blue left-right chain of that length) |
| 2–3 P1 | Play on 5×5 | Open play |
| 2–3 P2 | 4×4: nobody wins? both win? | No to both |
| 2–3 P3 | 4×4 squares, side-sharing chains, nobody wins | Possible, for example a checkerboard |
| 2–3 P4 | 5×5 fewest blue | 5 |
| 2–3 P5 | Four 4×4 positions, Blue to move | Game 1: yes, only at (3,1). This is forced, because Red threatens to win there at once. Game 2: no, because Red has two one-move wins, (2,0) and (2,1). Game 3: no, because Red's two counters are joined to each other and to both edges by two-way gaps. Game 4: yes, only at (2,1). Counter counts are legal for Red going first, and no game is already won |
| 2–3 P6 | 3×3 winning first moves | The 5 cells listed above |
| 4–5 P1, P9 | Play 5×5, 7×7 | Open play |
| 4–5 P2 | 5×5: nobody wins? both win? | No to both |
| 4–5 P3 | 4×4 squares: nobody wins with sides; both win with corners | One checkerboard does both |
| 4–5 P4, P6 | Explain why not both; explain why someone must | Explanation problems |
| 4–5 P5 | Two full 5×5 colourings, path from the top-left star | Board 1: Red wins, and the path (23 sides) ends at the bottom-left corner. Board 2: Blue wins, and the path (26 sides) ends at the top-right corner. The two boards give different endpoints, as they should |
| 4–5 P7 | Same as 2–3 P6 | The 5 cells listed above |
| 4–5 P8 | Maya claims a second-player win on 11×11 | Strategy stealing shows she is wrong. "Nobody knows a sure way to win on it" is accurate: 11×11 is unsolved |

## A. Changes needed

### A1. K–1 Problems 2, 3 and 5 present impossible tasks as instructions (pages 2 and 4)

Quoted: "Put a red or a blue counter on every hexagon so that nobody wins." The same wording appears in Problem 3 with "so that Red and Blue both win", and again in Problem 5.

All three tasks are impossible. The older bands ask the same thing as a question ("Can you put…?"), which is honest. In K–1 the adult reads the instruction aloud, and that adult is the parent volunteer: a non-mathematician with no facilitator guide. An instruction tells both the adult and the child that a solution exists. Two failures are likely: the adult keeps pushing the children toward a solution, or the adult accepts a board where a wiggly chain went unnoticed. Hex chains bend, so young children miss them easily. That turns the week's main theorem into a "success" that is false.

Fix: use the older bands' question form, which is still one short sentence.
- "Problem 2: Can you put a red or a blue counter on every hexagon so that nobody wins?"
- Problem 3: the same question, ending "so that Red and Blue both win?"
- Problem 5: the same question as Problem 2, on the 4×4 board.

This matches the register of the organizer's own example: "If you can, find ten coins … If you can't, explain why it is impossible."

### A2. 4–5 Problem 8 (strategy stealing) has no concrete stage (page 6)

Quoted: "Hex players often use a board with 11 rows of 11 hexagons. Nobody knows a sure way to win on it. Maya says she has a way to always win on this board when she goes second. Explain why Maya must be wrong."

The argument has two steps. The first is that Hex has no draws, which Problems 2–6 build. The second is that an extra counter of your own can never hurt you, and nothing on the page lets a child meet that idea first. The standard asks that "a child meets an idea in concrete cases, and uses it, before being asked to explain or generalize it." As written, Problem 8 is a cold proof question about a board the child cannot see or touch. Problem 7 does show that the first player can win on 3×3, which helps, but it does not reach the extra-counter idea. The outline also says that if the Chomp week is used, its strategy stealing should come first. The page cannot rely on that.

Fix: add one concrete numbered problem just before Maya. For example, print a full-size 4×4 position where Red can make sure to win, and ask: "Put one more red counter on any empty hexagon. Can Red still make sure to win? Can an extra red counter ever stop Red from winning?" Check the position with the solver.

Also change "on this board" to "on that board". The 11×11 board is not drawn, and the only board nearby is the 7×7 on the next page.

### A3. 2–3 Problem 5 positions are drawn too small to play out (page 5)

The four positions use 14 mm hexagons, so counters do not fit. The task, "Can Blue stop Red from winning, however Red plays?", can only be settled by playing continuations. Children would have to copy each position onto the 4×4 board on page 2 and clear it again for the next position. The standard asks for every position "at a size they can work on", and the guidance asks for light bookkeeping.

Fix: draw the four positions at playing size, 24 mm. A 4×4 board is about 150 × 106 mm, so two fit on a page, and the problem takes two pages. Children can then put real counters on the empty hexagons of the printed position. Keep "Write yes or no under each game" and leave space under each board.

The mix of answers is good: two yes, two no, and each yes has exactly one stopping hexagon, so "mark the hexagon" is accurate.

### A4. 2–3 Problem 4 is quick for grades 2–3 (page 4)

Quoted: "Put blue counters on this board so that Red cannot win, even when every other hexagon is red. Use as few blue counters as you can."

A row of five blue counters is the first thing most third graders will try, and it is optimal. Nothing on the page asks for the substantial part, which is why four cannot work. The standard names this case directly: ask for an explanation "why a packing is best". There is also an argument a third grader can find: a blue chain from left to right needs a hexagon in each of the five columns, because each step moves at most one column. It belongs in the guide.

Fix: add "Explain why fewer will not work." and a few writing lines; the page has room.

Optional: add a second 5×5 board with red counters already placed, so the answer is not always 5. One position I checked has red at (0,2), (1,2), (2,2), (3,2) and (4,0), and its fewest-blue answer is 6. For the K–1 version (Problem 7) the current task is the right size; see B1 for its wording.

### A5. 4–5 Problem 5 gives only two prepared boards for the boundary path (page 4)

The path task is good. The two boards have different winners, so the paths end at different corners, and "Where does the path end?" has a real answer. But the conjecture that leads into Problem 6 is that the path always reaches the top-right or bottom-left corner, on any full board. Two printed colourings are two instances chosen by someone else. A child who wants to test the conjecture, or to try to break it, has no board of their own.

Fix: add a third, blank board (4×4 at 16 mm is enough) for the child to colour any way they like before drawing its path. This needs red and blue pencils, which the materials list does not include, so add them. Writing R or B in each hexagon also works, but the boundary is then harder to see.

A worked example of the path is not needed. The organizer sits at this table and can demonstrate the first few sides on a board, which the guidance says is enough when an ordinary demonstration will do.

### A6. Counter size is unstated, and the 7×7 board is smaller than the outline asks (4–5 page 7, all play boards)

The outline asks for hexagons "about 25 mm across (a counter fits inside)". The play boards are 24 mm across the flats, so the largest counter that fits is 24 mm, and the centres of neighbouring hexagons are 24 mm apart. The 7×7 board is 22 mm, so there the limit is 22 mm. Several other weeks in this repository use 25 mm counters. Those would overlap their neighbours on every board here, and by 3 mm on the 7×7.

Drawing the 7×7 at 24 mm does not fit the landscape page with its header and footer: the board would be about 168 mm tall. So the practical fix is to settle the counter: specify counters of 20 mm or less, for example standard 19 mm bingo chips, wherever this week's materials are recorded. Before printing, someone should put real counters on a printed 7×7 and 5×5 board. The physical fit is untested.

## B. Smaller points

1. **K–1 Problem 7 is hard to follow after one hearing (page 6).** "Use as few blue counters as you can so that Red cannot win, even when all the other hexagons are red." This is one 25-word sentence built on a hypothetical. Say the actions in order instead: "Put some blue counters on this board, then fill every other hexagon with red. Use as few blue counters as you can so that Red has no chain."
2. **K–1 Problem 6: the answer depends on how well each child plays (page 5).** "Can Blue stop Red from winning?" leaves out the older bands' "however Red plays". After the centre opening, a K child playing Red who misplays will be "stopped", and the pair will answer yes. After the corner opening, Blue's only good reply is the centre, so a pair that misses it will answer no. Either answer can come out wrong. The adult will have to steer this, which is a reason the K–1 adult needs the answers (see D). There is also nowhere to record the answer. Consider "Can Red always win?" or adding "however Red plays".
   - Optional: a third board with the star at (0,1), in the middle of Red's own top edge. It loses for Red, which is the most surprising of the 3×3 cases.
3. **2–3 Problem 3's closing question is vague (page 3).** "What is different about the hexagon board?" can be answered with "hexagons have six sides". The point is why the checkerboard trick fails on hexagons. Ask "Why can't you do this on the hexagon board?" The child has just tried that in Problem 2.
4. **The colouring instruction needs materials that are not listed.** 2–3 Problem 6 and 4–5 Problem 7 say "Colour those hexagons red on the small board." Write "Put an X on those hexagons on the small board" so that only a pencil is needed. This does not apply to A5, where colouring is the task.
5. **Spelling.** "colour" appears in the rules block on every first page, in 2–3 P6, and in 4–5 P5 and P7 ("coloured edges"). The circle is in Washington State, and the existing student sources in `lowell-math-circle-year-2/source/` mostly use "color". Match that house style.
6. **4–5 order.** Problem 6, the hardest proof in the packet, sits in front of two concrete tasks: the 3×3 openings (P7) and the 7×7 game (P9). The session context puts abstract questions late so that a child who stalls has already done the concrete work. Consider moving the 3×3 openings problem to just after Problem 2 or 3, before the first explanation problem, and keeping it ahead of the A2 precursor and Maya. This is optional; the organizer sits at that table and can skip around.
7. **Page economy (optional).** K–1 pages 3 and 4, 2–3 pages 2 and 4, and 4–5 page 2 each hold one board with roughly half the page blank. That is harmless, but if A3 adds a page to 2–3, the explanation lines from A4 can go in the blank half of page 4.
8. **"Week NN"** in every header and footer is a placeholder from the outline. Fill it in when the week is scheduled.
9. **The 7×7 landscape page uses `/Rotate 90`.** It displays correctly. Check one physical print, because some print dialogs handle rotated pages differently when scaling is set to "Actual size".

## C. What works and should be kept

- The rules block is four plain sentences beside a non-task 6×6 example. The example shows a legal finished game in which Red's winning chain bends and includes a sideways step. That is exactly the misunderstanding young children need to see corrected.
- The edges are labelled RED and BLUE as well as tinted. The red tint is lighter than the blue, so the boards still read in greyscale.
- The square board is a strong contrast. In 4–5 Problem 3 one checkerboard gives "nobody wins" with side contacts and "both win" with corner contacts, which brackets the hexagon case before Problem 4 asks why.
- K–1 gets the same three ideas at small scale: no draws (P2, P3, P5), which opening matters (P6) and fewest blockers (P7). It has as many problems as the other bands.
- In each band the order runs from concrete to explanation: play, then fill, then contrast, then explain.

## D. For the facilitator guide (not for the student pages)

The workflow produces no guide, but these pages lean on adult knowledge more than most weeks do:
- The K–1 volunteer needs to know four things:
  - P2, P3 and P5 cannot be done.
  - How to check a full board for a bending chain.
  - The P6 answers: centre, Red always wins; corner, Blue wins only by taking the centre.
  - The P7 answers: 3 and 4.
- The 2–3 adult needs the puzzle answers and the five winning openings.
- The 4–5 notes need four things:
  - The crossing argument for "not both".
  - Gale's path argument and which corner means which winner.
  - The strategy-stealing argument, including the case where the stolen strategy asks for the hexagon that already holds the extra counter.
  - The outline's advice to teach Chomp first if both weeks are used.
