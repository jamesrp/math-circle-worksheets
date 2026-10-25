# Review: Week 98 K–1 draft (W98-K-v1), `draft/k-1.pdf`, 9 pages

## How I checked

- I rendered all 9 pages (70 dpi) and looked at each one. I measured pages 1 and 2 at 10 px/mm: working squares are 30.0 mm and the left margin is 12 mm. The widest rows (P3's record column and P6's third board) end about 203 mm from the left edge, which leaves about 13 mm on the right. Nothing overflows or overlaps, and the LaTeX log has no overfull boxes.
- I re-enumerated every answer the pages depend on with my own script (`review-work/verify.py`), separate from the writer's `check.py`. I also tested two likely K–1 misreadings of the rule: "exactly two neighbours" and "corners count".
- I compared the problem list with the older bands' Week 98 problems (`lowell-math-circle-year-2/source/week-98/student/*.tex`) to check for overlap.

## Verdict

This is a strong draft. It follows the brief closely, has nine substantial pages of real K–1 mathematics in plain short sentences, and stays clean of headings, encouragement and hints. Every printed start does what the pages need. One rule-wording problem should be fixed before release, because a literal reading of it breaks the kernel-2 boards. Three sequencing or clarity problems are worth fixing, and the rest are polish.

## Mathematics: all correct

| Page | Claim the page depends on | Checked result |
|---|---|---|
| Rules | ✓ picture (1,2),(2,1) gives the centre. ✗ picture (1,1),(3,3) does not | Correct. Both boards stop there: the ✓ board at the 2×2 block, the ✗ board at once |
| P1 | 2 seeds on 2×2: 6 placements, only the 2 diagonal pairs fill | Correct. Side-by-side pairs stop at 2. The 8 record boards do not give away the count of 6 |
| P2–P4 | Fewest seeds: 3 on 3×3, 4 on 4×4, 5 on 5×5 | Correct (14/84, 130/1820, 1615/53130 fill) |
| P5 | Strips 1×3, 1×4, 1×5, 1×6 need 2, 3, 3, 4 | Correct. Minimal starts: {1,3}; {1,2,4} and {1,3,4}; {1,3,5} only; {1,2,4,6}, {1,3,4,6} and {1,3,5,6} |
| P6 | Two-wide boards 3×2, 4×2, 5×2 need 3, 3, 4 | Correct (10, 8 and 48 minimal starts) |
| P7 | A grows to 4, B is already stuck, C grows to 6 (two rows), D fills | Correct. If corners are counted, all four boards fill, so the page catches the diagonal mistake (most clearly on B) |
| P8 | Seeds that can come off alone: bent three on 2×2 → only the corner; four corners → all 4; three corners + centre → (1,1) and the centre; middle-edge four → none (each removal stops at 6) | Correct. The four boards give the contrasting counts 1, 4, 2, 0 |
| P9 | From the top row plus the left column, the seeds that can come off are (1,1), (1,2) and (2,1). The routes end at (1,2),(1,3),(2,1),(3,1) with 4 seeds (every seed needed) or at three corners with 3 seeds | Correct. There are exactly two endings, so the answer to "a different number?" is yes, 3 or 4 |
| Kit | Counters: 5×5 from 5 seeds uses 5 + 20. The largest board on P8 uses 4 + 5. P9 uses 5 + 4 | Fits the 6 + 20 per pair. See the seed-colour note under Could fix |

The finish does not depend on the order of growth on any printed start (200 random orders each), so a finish recorded as "filled" or "stuck" belongs to the seeds alone.

## Must fix

### 1. The rule says "two squares", and a literal "exactly two" reading breaks Problem 8

Page 1 says: "A square gets a counter when two squares next to it, not corner to corner, have counters." The outline's rule says *at least two*. The older Week 98 pages, which are worked at the next tables after the same launch, say "at least two squares sharing its sides". The writer copied the guide's spoken one-liner, which leaves this out.

The difference matters on these pages. Under an "exactly two" reading:
- P8 board 4 (middle-edge four) never gets its centre, because the centre has four filled neighbours from the start. It stops at 8 of 9, so the board that shows "every seed needed" looks stuck before any seed is removed.
- P8 board 3 (three corners and the centre) stops at 7 of 9. The squares (1,2) and (2,1) each have three filled neighbours.
- P8 board 2 (four corners) stops at 7 or 8 depending on the order of growth. That contradicts kernel 3, the property that makes "filled or stuck" a property of the seeds.

So three of P8's four boards would read as non-starters. A K–1 child who has only ever seen two-neighbour additions in the launch and the ✓ picture can easily form the "exactly two" rule.

Fix: write "A square gets a counter when **two or more** squares next to it, not corner to corner, have counters," and keep "Your partner points to two of them before each new counter." If the reviser wants a picture to carry it as well, a three-neighbour ✓ case would do. The words alone are enough.

## Should fix

### 2. Problem 7 is the most accessible task in the packet, but it comes seventh

P7 asks children to grow four printed 3×3 starts. It asks for no choosing, no hunting and no recording, and board B (the middle row) is exactly where a child who counts corners goes wrong. That makes it the natural first contact with the rule after the launch. The brief asks for "filled or stuck with very few seeds" as the entry, and says the first problems should let every child start doing something right away. Instead, P7 comes after five hunts for the fewest seeds, two of them hard: only 1 in 14 random four-seed starts fill a 4×4. A K–1 child who stalls on P3 or P4 may never reach it, and the adult finds the diagonal mistake late.

Recommendation: move P7 to Problem 1, or to Problem 2 just before the 3×3 hunt, and renumber. It reveals no answer: board D is a 4-seed fill, not the 3-seed minimum, and board C is a near miss. This also puts the printed-counter convention, which matches the rule pictures, before the dot convention used on P8 and P9.

### 3. Problem 8 does not make clear that each seed is tested alone

The text is "Put seeds on the dots. Ring each seed you can take off while the others still fill the board." The task means: take one seed off, grow the board, then put that seed back before testing the next. Nothing says to put it back, and P9, which comes right after, asks for removals that add up. On the four-corners board a child who does not put the seed back gets "yes" for the first corner and then "stuck" for every other corner, which is the wrong answer. Even read correctly, "ring each seed you can take off" on that board ends with all four ringed, which a child can read as "all four can come off".

"The others" does imply it, but the reader is a non-mathematician parent with no K–1 guide, reading once to a 5-year-old. The phrase that a seed comes off *by itself* is part of what the task is, not a hint about how to do it. Possible wording (two sentences): "Put seeds on the dots. Ring each seed that can come off by itself, so that the other seeds still fill the board."

### 4. Problem 9 is too long for a K–1 read-aloud

P9 has 40 words in three sentences. Every other problem has 13 to 21 words in one or two sentences, and the standard asks for one or two short sentences. The task has to state the procedure (removals that add up while the board keeps filling) and then the real question ("a different number?"), so it cannot be very short. It can still lose words. Example (about 33 words, and it still asks for the drawing): "Put seeds on the dots. Take them off one at a time while the board still fills, and draw what is left when none can come off. Can you end with a different number?" As in P8, the reviser should check that "take off one at a time" cannot be read as "take off any you like".

## Could fix

### 5. The ✓ under the left rule picture can be read as "this board fills"

Both rule pictures are drawn as complete 3×3 boards with thick outer borders. In that format the ✓ and ✗ look like verdicts on the whole board. In fact the ✓ board stops at the 2×2 block, 4 of 9, so it is stuck. The words "filled" and "stuck" are the children's main judgment all session. Options: draw the patches without a thick outer border so they read as parts of a board, put the mark beside the dashed circle rather than under the board, or both. Optionally, make the ✗ case one side touch plus one corner touch, such as counters at (1,1) and (2,1) with the target (1,2). That is the mistake K–1 children are most likely to make, more than a target touched only at two corners.

### 6. Problem 3 (and partly Problem 4) is close to a problem the older tables do

The 2–3 and 4–5 packets both have "What is the smallest number of seeds you can use to fill a 4-by-4 board? Find three different starts using your best number." K–1 P3 says "Fill this board with as few seeds as you can. Draw the seeds each time it fills.", on a 4×4 with four record boards. That is the same task. P4 (fewest on 5×5) overlaps with the 4–5 Problem 3, though K–1 uses counters rather than pencil. The brief lists these problems as ones not to copy. It also asks K–1 to do "the fewest seeds on growing boards, where the run 2, 3, 4 invites a prediction", so some overlap is sanctioned and the tables do not mix. The reviser or organizer should decide whether that is acceptable. If not, the K–1 version could be made its own by its framing, for example a guess before the 4×4 as well as the 5×5, rather than by removing the run.

### 7. The rules leave out two facts the older pages state

"Counters stay put" and "There are no squares outside the board" appear in the outline and on the older pages' rules. P5 depends on the second: the end squares of a strip must be seeds *because* nothing lies beyond them. On a printed strip this is probably obvious, and leaving it out keeps the read-aloud short. It is a judgment call. If anything is added, "Counters stay put" is the more likely K–1 problem, since children slide counters.

### 8. Kernel 3 is not asked anywhere

The outline allows kernel 3 to be "noticed during the other work or asked late", so leaving it out is permitted. The older "same seeds, two orders" problem must not be copied. If a late K–1 question is wanted, P8 already has two children growing the same seeds, so a single question could fit there. Low priority.

### 9. P5, P6 and P8 cannot be loaded all at once with one pair's seed colour

The seed counts per page are 12 for P5 (all four strips), 10 for P6 and 15 for P8, against 6 seed-colour counters per pair. Growth counters always suffice. A K–1 pair that hears "Fill each strip…" and starts on every board will run out of seeds partway. The adult will steer them one board at a time, and the record boards on P5 and P6 let them clear and move on. This needs no change on the page. It should go in whatever K–1 notes go with the packet.

### 10. Smaller points

- **Recording wording.** P2 and P3 say "Draw the seeds each time it fills", while P5 and P6 say "and draw the seeds". The P2/P3 wording asks for every filling start, including 6- or 9-seed fills, which pulls against "as few as you can". "Draw the seeds when it fills" or the P5 wording would keep the record focused.
- **Spelling.** The page uses "colour", following the brief. The Week 98 student pages used at the other tables say "neighbors", and the guide says "colors". Match the house spelling, which looks like US for student pages.
- **Two conventions for starts.** P7 prints counter-sized grey circles, while P8 and P9 print small dots with "Put seeds on the dots." Both work, and the dots are better for resetting after a removal. If P7 moves to the front (item 2), the difference is harmless. If it stays seventh, consider using the dot convention there too.
- **P6 spacing.** P6's three working boards are only 5.5 mm apart. This is legible, but the gap between the 3×2 and 4×2 boards is tight for K–1 hands moving counters. The space below the 3×2 and 4×2 boards could absorb a slightly wider gap, for example by shrinking the record boards' offset.
- **No explanation prompt.** The packet asks for no explanation anywhere. That is defensible for K–1. If the reviser wants one place where explanation is the point, P5 (why the end squares of a strip must be seeds) is the most K–1-explainable impossibility in the packet. It could be a short closing question on that page rather than a hint.

## Keep these strengths when revising

- **P1** (every way to place 2 seeds on 2×2) is an excellent entry. It is complete, small and checkable, and it sets the diagonal-versus-side contrast that later pages depend on. Eight record boards for six answers do not give away the count.
- **The run of fewest seeds** (P2 3×3, P3 4×4, P4 "Guess…" for 5×5) is followed by **P5 strips** (2, 3, 3, 4) and **P6 two-wide boards** (3, 3, 4). Together they make a well-chosen contrast. The n-by-n pattern stops working, the end squares of a strip are forced, and 2×4 needs no more than 2×3.
- **P8's four boards** have deliberately different answers (1, 4, 2, 0 seeds that can come off). The middle-edge four sets up kernel 2 against the three-seed fills children found on P2.
- **P9** uses the outline's newly worked start (top row and left column), not the older bands' start, and reaches both endings, 3 and 4 seeds.
- **Printed dots under the counters** on P8 and P9 make resetting after a removal easy, and the records hold seeds only.
- **Format** follows the standard: the header and footer are exact, there are no headings, Name/Date fields, encouragement, exclamation marks or dashes used for asides, and diagrams are not narrated. Working boards are 30 mm and record squares 15–16 mm. The extra record boards are not labelled as problems.
- **The counter budget** was respected throughout: every board's growth fits in 20 counters.

## Status

Nothing here has been tried with children. The checks were mathematical and digital only. Neither the kit fit (25 mm counters on 30 mm squares) nor the partner's two-finger check has been tried at K–1, and whether K–1 children hold on to the rule for a session is still a prediction, as the guide says.
