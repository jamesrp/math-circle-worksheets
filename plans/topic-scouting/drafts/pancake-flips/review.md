# Review: Pancake flips, draft v1

Reviewer stage. I rendered all 16 pages at 80 dpi, looked at each one, and zoomed to 170–200 dpi on the demo strip, the breaks diagram and every burnt-pancake row. I read `draft/src/gen.py` and rebuilt the packet from a copy of the sources in a scratch folder: it compiles cleanly with no overfull boxes, and the rebuilt text matches the draft PDFs. I checked every stated stack, count and claim with my own breadth-first search, written separately from the author's `check.py`. The answer table is at the end.

## Overall verdict

The packet is close to the organizer's standard. Headers and footers are consistent. It has no titles, encouragement, hints, Name/Date fields or lettered sub-steps. Problems are short and concrete. The worked visual for the flip notation (3 1 2, flip 3, 2 1 3, flip 2, 1 2 3) is correct and uses the launch stack. Every stated fact is true. Each band has enough work: K–1 has 7 problems on 4 pages, 2–3 has 7 on 5, and 4–5 has 9 on 7.

The problems that need revision are about design, not correctness:

1. A 4–5 problem that an earlier problem already solves.
2. A K–1 task that asks children to certify an impossibility, at the table staffed by the non-mathematician parent.
3. The 2–3 order, which asks for the general method before the concrete six-stack practice.

There are also smaller issues with recording space and notation.

## Major issues

### M1. Grades 4–5, Problem 5 is answered by Problem 3 (pages 3 and 5)

Problem 3 has children sort **1 3 5 2 4** and explain why five breaks force at least five flips. That stack is one of the 20 worst stacks of five. It needs exactly 5 flips, and 5 is the maximum for five pancakes. Problem 5 then asks: "Find a stack of five pancakes that needs as many flips as you can. Explain why it cannot be sorted in fewer." A child who finished Problem 3 can copy 1 3 5 2 4 and its explanation. The hunt the outline intended ("find the worst stacks of four and five by pooling") disappears.

Fix, in one of two ways:

- **Change Problem 3's task stack** to one whose break count is tight but that is not a worst case. Examples: **2 5 1 3 4** or **5 3 1 2 4**, each with 4 breaks and needing exactly 4 flips. Change its sentence to match ("It has four breaks. Explain why a stack with four breaks can never be sorted in fewer than four flips."). Problem 5 then remains a real hunt, in which children apply breaks to build a five-break stack.
- **Or keep Problem 3 and recast Problem 5** so it asks something Problem 3 does not answer. One option: "Find a stack of five pancakes with fewer than five breaks that still needs five flips." Eight such stacks exist, for example 1 3 2 5 4, with 3 breaks and needing 5. Problem 1's 2 1 4 3 6 5 (3 breaks, needs 5) already hints that breaks are not the whole story. This is harder to explain, so it suits the end of the packet.

### M2. K–1, Problem 5 asks for a certified impossibility (page 4)

The problem reads: "Find a stack of pancakes 1, 2, 3 and 4 that cannot be sorted in three flips or fewer."

- 11 of the 24 four-stacks need exactly 3 flips, and only 3 stacks need 4 (4 2 3 1, 2 4 1 3, 3 1 4 2). A kindergartner who fails to sort a stack in three has shown nothing about it. "Cannot" is a statement about every sequence of up to three flips, which can be as many as 39 sequences.
- The K–1 adult is the parent volunteer, who is not a mathematician. They cannot judge a child's candidate without an answer key, and the facilitator guide is a separate, untested step.
- The outline's K–1 emphasis is the three-pancake stack that needs three flips, which Problem 2 already covers. The four-stack worst case was assigned to 2–3 and 4–5.

Fix: keep the four-stack worst case in K–1, but make it something children can act on and check. For example, "Sort each stack with as few flips as you can", with large drawings of 4 2 3 1, 2 4 1 3 and 3 1 4 2 and one 3-flip decoy such as 2 1 4 3 (1 2 4 3 is already in P3), each with a flips box. The adult needs only the target counts (4, 4, 4, 3). Alternatively, "Which of these stacks needs the most flips?" with the same four drawings. The open "find one that cannot" version can stay as an adult-led extension in the guide.

### M3. Grades 2–3: concrete six-stacks come after the general method, and the hardest search comes first (pages 2–4)

The current order is P1 (sort given 4- and 5-stacks), P2 (worst three-stack), P3 (find all four-stacks that need 4), P4 (a method for any six-stack, and for ten), then P5 (sort four given six-stacks).

- The standard says a child meets an idea in concrete cases before generalizing. P5 is the concrete six-stack work, but it comes after P4 asks for a method for any six-stack. **Swap P4 and P5.**
- P3 is the hardest exhaustive task in the band and blocks the way to the method question. The outline lists that question first in the 2–3 emphasis ("find a method that always works and say how many flips it can need"). Children who stall on P3 never reach it. Consider the order P1, P2, the six-stacks, the method, then the four-stack hunt, then burnt pancakes. Stopping anywhere would still be fine.
- P5's stacks are all patterned: 6 5 4 3 2 1 (needs 1), 4 5 6 1 2 3 (3), 1 2 3 4 6 5 (3), 2 1 3 4 6 5 (4). None of them is genuinely mixed up, so none pushes a child toward a method that always works. Replace one or two with scrambled stacks, for example **3 6 1 5 2 4** or **5 2 6 3 1 4**, each needing 6 flips with 6 breaks. Keep 6 5 4 3 2 1 or 1 2 3 4 6 5 for contrast.

## Moderate issues

### m1. K–1, Problems 1 and 2 overlap almost completely (pages 1–2)

P1's stacks are 2 1 3, 3 2 1 and 2 3 1. P2 asks for all six three-stacks. Of those six, three are in P1, one (3 1 2) is the demo, one is already sorted, and only 1 3 2 is new. Also, 2 1 3 is the demo's middle frame, so the demo has already solved P1's first stack on the page. P1 needs 1, 1 and 2 flips, which is probably under five minutes even with building.

Options:

- Make P2 the first problem. Finding and sorting all six stacks is a good opening with objects.
- Or keep a warm-up but replace 2 1 3 with a four-stack such as 4 3 1 2 (2 flips), so the warm-up does not use up P2's cases. Avoid 4 3 2 1, 3 2 1 4 and 2 1 3 4, which are P4's answers, and the stacks already in P3.

### m2. K–1 recording slots are too small for kindergarten handwriting (pages 2–4)

The dashed blank slots in P2, P4 and P5 are 0.8 cm tall. Those in P7 are 0.9 cm, and P7 also asks children to shade a dark side inside them. Kindergartners write digits about 1.5 cm tall. Pages 1 and 2 are each half empty, so there is room to make the slots at least 1.3–1.5 cm tall and the flips boxes about 1.3 cm. The dashed rectangles also share edges, which draws a doubled dashed line between slots. A small gap between slots would look cleaner.

### m3. No way to record a burnt stack (grades 4–5 P8 and P9, page 6; grades 2–3 P6 and P7)

The rules give a code only for order ("its numbers from the top"). Grades 4–5 P8 ("Find a stack of three pancakes with dark sides…") and P9 ask children to report burnt stacks but give no notation and no outlines. K–1 P7 gets blank outlines, but the older bands get only blank space. Either:

- add three or four blank three-slot outlines to 4–5 P8, as K–1 P7 has, or
- print a code under each burnt drawing in the first burnt problem of each band, so the convention is shown before it is needed. For example, mark dark-side-up pancakes with a bar or underline.

The side-view convention, where a band on the top edge means the dark face is up, is new and is never shown in action. A single non-task worked flip would make it explicit, together with the fact that a flip turns each pancake's dark side over as well as reversing the order. This matters most for the K–1 adult. One example is three pancakes 2 1̄ 3, flip 2, giving 1 2̄ 3, a state that appears in no task. Keep it beside the first burnt problem, not in the opening rules.

### m4. Grades 2–3, Problem 7: unclear wording and a steep jump (page 5)

- "Sort these stacks of three **in the same way**" could mean the same method as Problem 6. Write "so that every dark side ends facing down, with as few flips as you can."
- The two stacks are 3 2 1 with all dark sides down (needs 5) and 1 2 3 with all dark sides up (needs 6). The second is one of only two burnt three-stacks that need 6, the maximum. Going straight from two-stacks to the hardest three-stacks gives no middle ground. Add one or two easier three-stacks first, for example the 2-flip and 3-flip stacks from the 4–5 P7 row, or accept it knowingly as a late challenge.

### m5. Grades 2–3, Problem 6 hands over the whole enumeration (page 5)

All seven unsorted two-pancake burnt stacks are drawn as routine sorts, needing 1, 1, 2, 2, 3, 3 and 4 flips. K–1 P7 and 4–5 P8 instead let the child look for the hardest stack. Consider giving four of the seven, as K–1 P6 does, and adding "Find the stack of pancakes 1 and 2 that needs the most flips." Then finding the cases is the child's work and the worst case (1 and 2 both dark side up, 4 flips) is a discovery.

### m6. Grades 4–5, Problem 3: wording of the break definition (page 3)

- The text "have numbers that are **not next to each other**" can be confused with physical adjacency, because touching pancakes are next to each other. "Numbers that differ by more than 1" is unambiguous and within 4–5 arithmetic.
- The text "such as 1 on 5 or **4 on the plate**" comes before the picture. 4 on the plate is a break only because that example's plate is 6. Tie it to the picture, for example "such as 1 on 5, or 4 on the plate in the stack below".
- The three red markers sit on the right edge at the top and bottom of the wide pancake 5, so they can read as marking pancake 5 rather than two gaps. A short red tick in the gap itself, or markers clearly centred on each gap, would show that a break is a place between two things.

## Minor issues and wording

- **"needs as many flips as you can"** (K–1 P7, 4–5 P5 and P8) mixes subjects. "Find the stack … that needs the most flips" is plainer. 2–3 P2 already uses that form.
- **K–1 P6** starts "Now each dark side must end facing down." Dark sides have never been introduced to K–1 children. "Each pancake has a dark side. Sort each stack so every dark side ends facing down, with as few flips as you can." is still within two sentences.
- **Burnt drawings:** where a dark-down band sits directly on a dark-up band, the two merge into one thick stripe. Examples are the fifth stack in 2–3 P6 (1 down on 2 up) and 2–3 P6 #4. The outlines separate them, but a 1–2 mm gap between pancakes in burnt drawings would make clear which band belongs to which pancake.
- The modal verb is inconsistent: 2–3 P4 says "your way **could** need" and 4–5 P2 says "your way **can** need". This is harmless, but pick one.
- The K–1 rules say "slide the spatula". The materials allow hands or a stiff card. If tables use hands, the wording should cover that, for example "slide the spatula (or your hand)". Or make sure every table gets a card spatula.
- `Week NN` and the `NN-…-v1` ids are placeholders, as in the outline. Set them when the week number is assigned.
- `draft/src/` contains exploration scripts, `__pycache__` and `.aux`/`.log` files. Drop them when the packet moves into `lowell-math-circle-year-2/source/`.

## Outside the pages, for the facilitator guide and materials

- **Shared demo:** 3 1 2, flip 3, 2 1 3 shows "flip the biggest to the bottom", which is half of the two-flips-per-pancake method. The outline chose this launch stack, so I am not asking for a change, but the guide should know that the demo shows this step.
- **Burnt pancakes at every table:** K–1 and 2–3 now use burnt pancakes, although the outline assigned them to 4–5. That works mathematically at a smaller scale, but every pair needs sets with one coloured face. If those are the same sets used for plain sorting, children will see dark faces during the earlier problems, and some K–1 children may assume the dark side already matters. When pancakes are stacked, only the top face is visible, so checking dark sides means lifting the stack.
- **Physical rehearsal is needed and has not been done:** flipping a block of 5–6 foam or card pancakes with a card spatula or by hand; whether K–1 hands can flip a block of four as one unit; and whether 1 cm size steps are easy to read from the side.
- **4–5 P3:** 1 3 5 2 4 has exactly one 5-flip solution, flips 3 5 4 3 2, and every flip in it removes a break. Children who sort it by trial will usually take 6–8 flips. The adult should know that 5 is reachable.
- **4–5 P6:** the answer is no; 4 6 2 5 1 3 needs 7 flips. The argument is about the right size for this table. In a 6-flip solution every flip would have to remove a break. Following only break-removing flips gives a tree of 14 positions with 6 dead ends and no sorted stack.
- **4–5 P4:** breaks prove 2 4 1 3 and 3 1 4 2 need 4 flips, since each has 4 breaks. 4 2 3 1 has only 3 breaks and needs the neighbour argument: all three of its one-flip neighbours (2 4 3 1, 3 2 4 1, 1 3 2 4) need 3. Completeness comes from working outward from the sorted stack. This is the richest problem in the band.

## Verification table (independent BFS, stacks read from the top)

Maximum unburnt flips for 2–7 pancakes: 1, 3, 4, 5, 7, 8. Burnt maximum for 1–5 pancakes: 1, 4, 6, 8, 10. Worst stacks: 1 3 2 for three; 4 2 3 1, 2 4 1 3 and 3 1 4 2 for four; 20 stacks for five; 4 6 2 5 1 3 and 5 3 6 1 4 2 for six. Worst burnt stacks: 1 and 2 both dark up for two; 1 down, 2 up, 3 up and all three up for three. Breaks never exceed the fewest flips for any stack of up to 7. The largest-to-top-then-down method never exceeds 2n − 3 for 2 to 7 pancakes. Every outline fact checks.

| Band | Problem | Stacks → fewest flips |
|---|---|---|
| K–1 | P1 | 2 1 3 → 1; 3 2 1 → 1; 2 3 1 → 2 |
| K–1 | P2 | six stacks; only 1 3 2 needs 3 |
| K–1 | P3 | 4 1 2 3 → 2; 2 3 4 1 → 2; 3 4 2 1 → 2; 1 2 4 3 → 3 |
| K–1 | P4 | 2 1 3 4, 3 2 1 4, 4 3 2 1 (three stacks; six slots printed) |
| K–1 | P5 | 4 2 3 1, 2 4 1 3, 3 1 4 2 |
| K–1 | P6 (burnt) | 1 up, 2 down → 1; 2 up, 1 up → 1; 2 up, 1 down → 2; 2 down, 1 down → 3 |
| K–1 | P7 (burnt) | 1 up, 2 up → 4 (unique; not in P6) |
| 2–3 | P1 | 2 3 4 1 → 2; 3 4 1 2 → 3; 5 4 3 2 1 → 1; 5 1 2 3 4 → 2; 4 5 1 2 3 → 3; 1 2 3 5 4 → 3 |
| 2–3 | P2, P3 | 1 3 2 (3 flips); the three four-stacks above |
| 2–3 | P4 | 2n − 3 method: 9 for six, 17 for ten (answers vary with method) |
| 2–3 | P5 | 6 5 4 3 2 1 → 1; 4 5 6 1 2 3 → 3; 1 2 3 4 6 5 → 3; 2 1 3 4 6 5 → 4 |
| 2–3 | P6 (burnt) | 1, 1, 2, 2, 3, 3, 4 in printed order |
| 2–3 | P7 (burnt) | 3 2 1 all down → 5; 1 2 3 all up → 6 |
| 4–5 | P1 | 5 1 2 3 4 → 2; 4 5 1 2 3 → 3; 1 2 3 5 4 → 3; 3 2 1 5 4 → 3; 2 1 4 3 6 5 → 5 (3 breaks) |
| 4–5 | P3 | example 2 1 5 3 4: 3 breaks, needs 3; task 1 3 5 2 4: 5 breaks, needs 5 |
| 4–5 | P5 | maximum is 5 (20 stacks; 12 have 5 breaks) |
| 4–5 | P6 | 4 6 2 5 1 3: 6 breaks, needs 7, so it cannot be done in 6 |
| 4–5 | P7 (burnt) | 3 up, 1 down, 2 down → 2; 1 down, 2 down, 3 up → 3; 3 1 2 all down → 3; 1 up, 2 up, 3 down → 4; 3 2 1 all down → 5 |
| 4–5 | P8 (burnt) | maximum 6: 1 down, 2 up, 3 up, or all three up |

The drawn stacks match their printed codes, and the dark-band positions match the source signs in every burnt row. The spatula positions in the demo match flip 3 and then flip 2. The break markers in the 2 1 5 3 4 example mark exactly the three breaks.
