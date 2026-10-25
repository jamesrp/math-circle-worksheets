# Mathematical review: graceful-labels-v1 draft

I checked all three draft PDFs (K–1, 6 pages; grades 2–3, 6 pages; grades 4–5, 8 pages) against the figure sources in `draft/src/figs/`. Everything was recomputed with my own code, not the author's `check.py`:

- **Geometry.** I parsed every network figure's TikZ, rebuilt each graph from the coordinates, and checked dot and link counts, degree sequences and the "cards 0 to m" captions. I also checked that each box sits on exactly one link, that no box is within 0.25 cm of another link, and that no link passes through a dot that is not one of its ends.
- **Labellings.** A backtracking search counted the graceful labellings of every printed network.
- **K–1 readings.** I compared the strict reading of the tower rules with the literal reading of the printed rule.
- **Rulers.** I enumerated the four-counter and five-counter rulers.
- **Parity and loops.** I checked the parity claims, ran a Rosa-type construction for C100 and searched C11 and C12.
- **Trees.** I tested every tree with 7, 8 and 9 dots (11, 23 and 47 trees). All of them are graceful.

## Located problems

### 1. K–1, page 1 shared rule; affects Problem 2 (page 2) and Problems 6 and 7 (page 6)

**Text:** "Put the towers on the dots, never two on one dot. A dot with no tower counts as 0."

**Problem.** Nothing says that only one dot may be empty. Problems 4 and 5 then teach that a tower may stay in the tray. A child can therefore leave a tower out and have two empty dots, which means two dots labelled 0. That reading satisfies the printed rule, but it is not a graceful labelling, because graceful labels must all be different.

**Evidence:** I enumerated with each tower used at most once and any number of empty dots (each counting as 0):

| Problem | Network, towers | Strict (one empty dot) | Literal reading | Extra solutions, e.g. |
|---|---|---|---|---|
| 2 ("Find all the ways") | path of 4, towers 1,2,3 | 4 | **8** | empty–1–3–empty (links 1,2,3; tower 2 unused), empty–2–3–empty, and their mirror images |
| 6 | path of 5, towers 1–4 | 8 | 28 | empty–4–1–empty–2 (links 4,3,1,2; tower 3 unused) |
| 7 | fork, towers 1–4 | 12 | 20 | branch dot 3 with neighbours 1, 4 and empty, and the 4 joined to another empty dot (links 2,1,3,4; tower 2 unused) |

These problems are not affected: 1, 3, 4 and 5. Every solution of each uses exactly one empty dot. So the answers "circle 1 and 2" in Problem 4, "circle 1 and 3" in Problem 5, and centres 0 and 3 in Problem 3 hold under either reading.

**Why it matters.** The answer to "Find all the ways" in Problem 2 changes from 4 to 8. In Problems 6 and 7, children can succeed with a repeated 0, which sidesteps the real constraint: both 0 and m must appear, and all labels must differ. The parent at the K–1 table has no guide to settle the question.

**Smallest fix:** Replace "A dot with no tower counts as 0." with "Leave one dot empty. It counts as 0."

- Every graceful labelling uses 0, so requiring exactly one empty dot matches the mathematics.
- It leaves the answers to Problems 1, 3, 4 and 5 unchanged.
- It restores 4 / 8 / 12 solutions in Problems 2, 6 and 7.

The rules picture already shows a single empty dot, so it fits.

### 2. K–1, Problems 1 and 2 (pages 1–2): the "find all" count is not what the page implies

**Text:** "Make the links measure 1 and 2 with these towers. Find all the ways." Six small recording boards follow. Problem 2 has the same text with towers 1, 2, 3 and again six small boards.

**Evidence:**

- Problem 1 (path of 3, towers 1, 2) has exactly 4 ways: 0-2-1, 1-0-2, 1-2-0, 2-0-1. That is 2 up to mirror image.
- Problem 2 (path of 4, towers 1, 2, 3, with the rule fixed as in item 1) has exactly 4 ways: 0-3-1-2, 1-2-0-3, 2-1-3-0, 3-0-2-1. Again, 2 up to mirror image.

**Problem.** The page offers six boards, so a child who has found all four will look for two more that do not exist. The page also never says whether a mirror image counts as a new way. The non-mathematician adult at this table has no guide.

**Smallest fix:** Print four small boards for each problem, so that mirror images count as different and the child knows when to stop. If the extra boards are meant to stay, then the eventual facilitator guide must give the answer "4 (2 pairs of mirror images)".

### 3. K–1, Problem 3 (page 3) small stars: boxes overlap the dots (diagram only)

**Diagram:** `k_p3_small.tex`, with spoke length 2.25 cm, dot radius 0.72 cm and 0.66 cm boxes.

**Evidence.** On each of the four small stars, the two lower boxes overlap the centre dot and the leaf dot by about 0.04 cm. I computed this from the coordinates and confirmed it in a 150 dpi render. No link line is visible on those two links. The top box clears the dots by only 0.07 cm.

The diagram is still readable as a star with three links, so the mathematics is not wrong. It is the only figure that fails the clearance check.

**Smallest fix:** In `gen.py`, change `star(3, 2.25)` for `k_p3_small` to `star(3, 2.6)`. This gives about 0.1 cm of clearance and still fits within the 5.7 cm row spacing.

### 4. All bands: dot size versus the outline's materials (minor; physical fit untested)

The working dots measure 2.5 cm across in grades 2–3 and 4–5, and 2.7 cm on the K–1 big boards. The outline specifies dot circles about 3 cm across. With 4.1 cm between dot centres, the visible link is 1.6 cm long and the box is 0.8 cm. That leaves only 0.4 cm on each side of the box, so a number card wider than about 3.3 cm would cover the box where children write the difference.

This is not a mathematical error. The fit has not been rehearsed with the actual cards.

**Fix:** Measure a card. If cards are wider than about 3 cm, increase the dot radius toward 1.5 cm and lengthen the links to match.

## Bands that check out

**Grades 2–3:** no mathematical problems found. The answers:

| Problem | Answer |
|---|---|
| P1: paths of 4, 5 and 6 dots | All can be labelled (4, 8 and 24 labellings), for example 0-3-1-2 |
| P2: fork, cards 0–4 | 12 labellings. For example: 0 on the left end, 4 on the branch dot, 1 on the dot below it, and 2 then 3 along the right. The links are 4 on the left, 3 going down, and 2, 1 along the right |
| P2: double star, cards 0–5 | 48 labellings |
| P3: star with 5 links | Centre 0 or 5 only. With any other centre c, a difference of 5 would need a leaf at c ± 5, which lies outside 0–5 |
| P4: loops of 3, 4, 5, 6 | 3 and 4 can be labelled (left-over card 1 or 2, and 1 or 3). Loops of 5 and 6 have no labelling (0 found by exhaustive search) |
| P5: loop of 7 | 168 labellings, for example 0, 3, 4, 2, 6, 1, 7 |
| P6: explanation | 1+…+5 = 15 and 1+…+6 = 21 are odd. Going round the loop, the rises equal the falls, so the total must be even. Equivalently, the number of odd differences must be even, and there are 3 |
| P7: path of 11 | 0, 10, 1, 9, 2, 8, 3, 7, 4, 6, 5 (648 labellings in all) |

All captions match the link counts. The ✓ and ✗ example (1-0-2 against 0-1-2) is correct.

**Grades 4–5:** no mathematical problems found. The answers:

| Problem | Answer |
|---|---|
| P1: path of 6, double star | Both can be labelled |
| P2: path of 11 | The 0, m, 1, m−1, … rule works. I verified it for up to 29 dots; it holds in general because the differences are m, m−1, …, 1 |
| P3: loops of 3–6 | As in grades 2–3 |
| P4: loops of 7 and 8 | Both can be labelled (168 and 384 labellings). The racetrack drawings are genuine 7-cycles and 8-cycles |
| P5: explanation | The parity argument above |
| P6: which loops cannot be labelled | Exactly 9, 10 and 101 (sums 45, 55 and 5151 are odd). The other three can be labelled: 11 (4576 labellings) and 12 (11808) by search, and 100 by Rosa's construction for 4k links, which I verified. So the parity argument settles the whole list |
| P7: four counters | {0, 1, 4, 6} or {0, 2, 5, 6} |
| P7: five counters | No arrangement exists anywhere on the 0–10 strip. A child-level proof: a distance of 10 forces counters at 0 and 10, a distance of 9 forces one at 1 (or 9, by symmetry), and the case analysis for a distance of 8 fails every time. Alternatively, with k counters on odd squares, k(5−k) ∈ {0, 4, 6} distances are odd, but 1–10 contains 5 odd numbers. The example strip (0, 2, 7 → 2, 5, 7) is correct and is not a task instance |
| P8: four and five dots, all joined | Four dots: 0, 1, 4, 6 (48 labellings). Five dots: none, by the same argument as the ruler. In the five-dot drawing every box lies on exactly one link and is at least 0.25 cm from every other link |
| P9: trees with 7–9 dots | All 11 + 23 + 47 trees can be labelled, so the honest answer within this range is "no". The general question is the open conjecture. Check the current Gallian survey before saying so, as the outline asks |

**K–1:** apart from items 1–3, the answers are correct under the strict reading:

- P3: centres 0 and 3 work; centres 1 and 2 are impossible.
- P4: circle towers 1 and 2.
- P5: circle towers 1 and 3. Using all four towers fails because a 4 needs an empty dot.
- P6: 8 labellings.
- P7: 12 labellings.

The tower trays show the right heights (1–2, 1–3, 1–4), and the rules example (towers 4 and 1 → 3; empty and 2 → 2) is correct.
