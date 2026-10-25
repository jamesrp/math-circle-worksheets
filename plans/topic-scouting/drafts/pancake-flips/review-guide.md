# Review: Pancake flips facilitator guide, draft v1

## What I checked

- I rendered all six guide pages and all 17 student pages: K–1 has 4, grades 2–3 have 6 and grades 4–5 have 7. I read every page and zoomed in on the launch figure.
- I read the pages' `gen.py` to get the exact signed data for every dark-side drawing, then compared it with the renders.
- I rebuilt the guide from a copy of `draft/src/`. It compiles with no overfull boxes or warnings, and its text is identical to `draft/facilitator.pdf`.
- I re-derived every number, list and flip sequence the guide prints with my own search, `review-guide-check/verify.py` (output in `verify.out`, table check in `table4.py`). I wrote it without using `check_guide.py`. It covers plain stacks up to 7 pancakes and dark-sided stacks up to 6. It enumerates every shortest sort to test each "only by" claim, and it builds the complete tree of break-removing flips for 4–5 Problem 6. All 118 checks pass.
- I compared the guide with the AGENTS.md rules and with the Week 98 model guide.

## Verdict

This is a strong draft. Every printed answer is correct, and every "only", "exactly" and "find all" claim is complete. Every problem number, page number, picture description and page count matches the final PDFs, not an earlier draft. The overview comes before any solution and is genuinely theorem-first:

- the method gives an upper bound of 2n − 3, with a proof;
- breaks give a lower bound, with a proof;
- the sharper break-removing-tree test;
- the worst stacks, labelled as computer facts;
- dark sides;
- a paragraph that separates experiment, conjecture and explanation;
- a map of the bands.

The launch uses a non-task stack (4 3 1 2 5) and has an Input / After one flip / Output figure. I found **no must-fix items**. The should-fix items concern physical materials, preparation time, recording at K–1, staffing, prerequisites and one launch caution.

## Must-fix

None.

- **Correctness:** all answers and claims check (table at the end).
- **Agreement with the pages:** every reference matches. This includes the K–1 renumbering (the six three-stacks are now Problem 1, the decoy row is Problem 4, dark sides are Problems 5–6), the 2–3 order (six-stacks are Problem 3, the method is 4, the four-stack hunt is 5, dark sides are 6–8) and 4–5 Problem 3's stack 3 5 2 1 4.
- **The overview:** it is not vague.

## Should-fix

### S1. The launch, like the printed example, shows half of the method, and the guide does not say so (page 2, "Launch")

The launch flips 4 3 1 2 5 with flip 4 and then flip 2. The printed example does 3 1 2 with flip 3 and then flip 2. Both show "the biggest pancake is on top, so flip it down into its place". That is the second half of the two-flips-per-pancake method, which 2–3 Problem 4 and 4–5 Problem 2 ask children to find. The page review asked that the guide tell adults this. The guide instead says the run "shows no more than the printed example".

That statement is true, but it does not warn the facilitator. The natural narration ("first I get the 4 to the bottom…") states the strategy aloud. The middle frame 2 1 3 4 5 also shows one of K–1 Problem 3's answers (2 1 3 4) sitting on the 5. Any two-flip run has some such middle frame, so this is acceptable.

**Fix:** replace "This stack is in no packet, and the run shows … but not its answer." with:

> "Flip without saying why you chose those flips. This run and the printed example both show the biggest pancake on top being flipped down into place, which is half of the method that 2–3 Problem 4 and 4–5 Problem 2 ask for; do not name that pattern. 4 3 1 2 5 is in no packet."

### S2. Card pancakes hide the order of the stack; recommend foam (page 2, "Per pair")

The guide repeats the outline's "card or 2 mm craft foam".

- **Card:** a stack of thin card circles is about 2 mm tall. From the side nothing can be read. From above, a big pancake hides the smaller ones under it. Only the top face's number shows. After a few flips children cannot see the order they are working with. The guide's status line lists "reading 1 cm size steps from the side" as untested, but the choice of material decides whether that is possible at all.
- **Foam:** 2 mm foam gives a 12 mm stack of six, whose layers and widths show from the side. A card spatula still slides under one foam pancake.

**Fix:** "cut from 2 mm craft foam, not thin card: a card stack is too thin to read from the side, so the order is hidden". Keep the item in the untested list.

### S3. Preparation time is underestimated, and nothing is offered to shorten it (page 2, "Per pair")

The guide budgets "about 40 minutes … numbering and colouring 10". That covers 36 pancakes, 72 numbers, and colouring one face of each in brown marker, then rewriting its number on the brown face. Filling a 4–9 cm circle with marker takes roughly half a minute to a minute, so the colouring alone is 15–25 minutes. Black numbers on brown marker are also hard to read. A parent volunteer with a full-time job should get a realistic figure and a shortcut. Fix it in one of two ways:

- Restate the time as **about an hour the first time** (trace 10, cut 25, number 10, colour 15).
- Or offer a quicker dark face, marked untested:
  - colour a broad stripe or a large scribble across one face instead of filling it; or
  - use brown self-adhesive craft foam with its white paper backing left on, so the backing is the light face (number it there in pen) and the brown foam is the dark face, with no colouring.

Optionally, add a one-page appendix of 4–9 cm circle outlines to cut out and trace, in place of "No template is supplied". The outline's 15-minute figure assumed printed circles.

### S4. The K–1 recording convention is never shown (page 2, launch; page 3, K–1 Problem 1)

The older tables get a recording demonstration: "4 3 1 2 5, flips: 4 2". K–1 Problem 1 instead asks children to write six stacks into dashed slots and a count into each flips box, which is 18 slots and 6 boxes. Problem 6 asks them to draw dark sides. The guide explains only how to shade dark sides. AGENTS.md says to demonstrate unfamiliar recording conventions, and kindergartners' writing is the bottleneck.

**Fix:** add to the K–1 section intro, or to Staffing:

> "Before Problem 1, show once: the top slot is the top pancake; when a stack is sorted, count the tokens into the flips box and clear them. The adult or partner may write numbers a child says."

### S5. No prerequisites are stated (page 1, band map)

AGENTS.md ("Level by prerequisites", "Make activities usable") asks for reading and arithmetic requirements. The guide mentions only that the K–1 adult reads aloud.

**Fix:** add one line to the band map:

> "Prerequisites: K–1, no reading (the adult reads), counting to about 10, writing digits to 6 or dictating them; 2–3, reading two-line problems, adding and doubling to about 20 for the method count; 4–5, comparing neighbours by subtraction, computing 2·20 − 3, and following an argument about every possible flip."

### S6. Staffing ignores the current group and gives the 2–3 adult no job (page 2, "Staffing")

`worksheet-workflow/context.md` describes three adults, one at each table: the parent volunteer at K–1, a mathematician at 2–3 and the organizer at 4–5. The 4–5 table has three children, with the third as referee. The guide says 2–3 and 4–5 "can share a circulating adult". That is fine as a minimum, but it is not the staffing the session will actually have. The 2–3 adult's useful moments go unnamed: hearing method counts in Problem 4, and keeping the pooled list in Problem 5.

**Fix:**

> "With the current group: the 2–3 adult asks for each child's method count in Problem 4 and keeps the shared list in Problem 5; the 4–5 adult listens to Problems 3, 4 and 6 and records the Problem 6 tree. The third 4–5 child checks the whole-block rule and the counts, rotating; a seventh set (42 pancakes) lets all three build in Problems 4–5. With only two adults, 2–3 and 4–5 can share one."

### S7. The pooled layer search needs a movable record (page 4, 2–3 Problem 5; page 5, 4–5 Problem 4)

"Each child follows one first flip, and the table keeps one shared list" means about 30 flips, checking each new stack against a list of up to 21 four-digit codes. AGENTS.md says "Use supplied movable cards when sorting is the mathematics" and "Keep bookkeeping light". Here the mathematics is sorting stacks into layers.

**Fix:** add one sentence and one material line:

> "Give the table a sticky-note pad and three columns, 1, 2 and 3 flips. Each new stack goes on a note in its column, so a repeat is easy to spot. The three stacks nobody can make are the answers."

## Minor

- **M1. Page 1, "Experiments…".** "The worst counts from six pancakes on are computer facts children can only conjecture" overstates the case for six. 4–5 Problem 6 lets children prove that some stack of six needs 7. Only "7 always suffices" rests on the computer fact that five pancakes never need six, as the guide's own 4–5 Problem 2 extension shows. **Fix:** "…and that 7 flips always suffice for six, are computer facts".
- **M2. Pages 1, 4 and 5.** "Table on page 3" refers to the guide's page 3. Every other "page N" in the guide refers to a student page. **Fix:** "the table in the K–1 section (guide p. 3)".
- **M3. Page 2, brevity.** Two sentences are addressed to a reviewer rather than a facilitator: the launch's justification (replaced in S1) and "the outline's 15 minutes assumed printed circles and no colouring". Cut them.
- **M4. Page 1, brevity.** "What children discover, by band" retells nearly every problem. Three lines would do for the band map, plus the prerequisites line from S5.
- **M5. Page 2, "Per pair".** "Or a hand if the whole block turns together" conflicts with every packet's rule "slide the spatula". **Fix:** give every pair a card spatula and treat hands only as a fallback.
- **M6. Page 2, "Per pair".** K–1 pairs should get only pancakes 1–4, or keep 5 and 6 aside, so that "all six ways to stack pancakes 1, 2 and 3" is not cluttered.
- **M7. Page 2, launch.** The sets have dark faces from the start. Add one launch sentence: "The brown sides do not matter until a page says so."
- **M8. Page 2, "A first visit".** The 4–5 first route (Problems 1–4 in 40 minutes) is ambitious. Problem 2 alone can fill the time. Name a cut, for example: "If time is short, do only 2 1 4 3 6 5 in Problem 1, then Problems 3 and 4; Problem 2 can open the return visit."
- **M9. Page 3, K–1 Problem 4 extension.** "Can you find another stack of four that needs four? (There is none.)" sends K–1 children, with the non-mathematician adult, on a search that cannot succeed. The page revision removed exactly this. **Fix:** drop the extension, or keep only "Which stack was hardest?".
- **M10. Page 5, 4–5 Problem 4.** Add a common slip: using plate 6 from the Problem 3 example for stacks of four. Their plate is 5, and 4 on plate 5 is not a break.
- **M11. Pages 4 and 6.** As for K–1 Problem 6, note that 2–3 Problem 7's three blanks are working space for one answer, and that 4–5 Problem 8 has two answers for its three blanks.

## What works and should be kept

- **The overview.**
  - It opens with the model and the convention that "needs" means fewest.
  - It gives the involution and layers argument that makes "find all" answers complete.
  - It proves the 2n − 3 bound, with a stack that attains it and one where the method is not optimal.
  - It proves the breaks bound in a way an adult can follow, and adds the sharper "every flip must remove a break" test.
  - It labels computer facts and source facts honestly.
  - It separates experiment, conjecture and explanation clearly.
- **The four-stack table on page 3.** All 24 stacks are listed by layer, which gives the K–1 parent one place to check any claim. Keep it.
- **The 4–5 Problem 6 tree.** It is complete: 14 nodes and 5 dead ends, and my search finds exactly these branches. The argument for 4 2 3 1 in Problem 4 is at the right size for 4–5.
- **The staffing principle.** "Writing down flips a child calls out is ordinary support; an adult choosing flips means the stack is too big." K–1's "Can you do it with fewer tokens?" before circling is also good.
- **The launch structure.** Children handle the sets, build a sorted tower, see the legal and illegal moves, and see the older bands' recording line. The rule "do not sort a printed stack or repeat a flip" is also right.
- **The dark-side launch at the table.** It uses the printed non-task example 2 1̄ 3 → 1 2̄ 3, and adds the flip-1 sentence and the shading convention.
- **Hints and honesty.** The hints are questions. The status line names the untested physical steps, and the sources paragraph says plainly that nothing was consulted directly.

## Verification table

My search, `review-guide-check/verify.py`. Stacks are read from the top, and a bar means the dark side is up.

| Guide item | Checked result |
|---|---|
| Layers of four | 1, 3, 6, 11, 3; the page 3 table matches stack for stack |
| Method | worst case is exactly 2n − 3 for n = 2–7; 9 on 2 6 5 1 3 4; 8 on 3 6 1 5 2 4, which needs 6 |
| Breaks examples | 1 3 2 (2 breaks, needs 3); 4 2 3 1 (3, 4); 2 1 4 3 6 5 (3, 5); 4 6 2 5 1 3 (6, 7). Breaks never exceed the fewest flips, and only the sorted stack has 0 breaks (n ≤ 7) |
| Maxima | plain, 2–7 pancakes: 1, 3, 4, 5, 7, 8. Dark sides, 1–6: 1, 4, 6, 8, 10, 12. Worst stacks as printed. Dark-side method never exceeds 3n − 2, and attains it for every n from 1 to 6 |
| K–1 | P1: 0, 1, 1, 2, 2, 3; 1 3 2 only by 2 3 2 or 3 2 3. P2: 2, 2, 2, 3; 1 2 4 3 only by 4 2 4. P3: the three stacks. P4: 4, 3, 4, 4 with the printed sequences. P5: 1, 1, 2, 3. P6: 1̄ 2̄ only, by 1 2 1 2 or 2 1 2 1; the list of all eight is correct |
| 2–3 | P1: each shortest sort is unique, as printed. P2: both first flips as printed. P3: 1; 6 (only by 5 4 6 3 4 5); 3; 6 (only by 2 3 6 4 2 3); six breaks each; the method uses 8. P5: the three stacks. P8: 2, 3, 5 (only by 2 3 2 3 2), 6 (both printed sequences, and these are the only two) |
| 4–5 | P1: as printed; 2 1 4 3 6 5 only by 3 5 6 5 3. P3: the chain and break counts 4, 3, 2, 1, 0; only by 2 5 4 3. P4: only 2 4 1 3 and 3 1 4 2 have four breaks; the 4 2 3 1 argument checks. P5: both lists (12 + 8) are exact; every five-break stack needs 5; the 1 5 3 2 4 argument checks. P6: the tree is complete; 2 3 4 2 6 3 2 sorts the stack. P7: 2, 3, 3, 4, 5. P8: the two stacks; the distribution 1, 3, 6, 12, 18, 6, 2; all dark sides up on four pancakes needs 8, the maximum. P9: 16, and the true worst case is 12 |
| Launch | 4 3 1 2 5 → flip 4 → 2 1 3 4 5 → flip 2 → sorted, and appears in no packet. Dark-side example 2 1̄ 3 → flip 2 → 1 2̄ 3 |
| Dark-side drawings | the signs in `gen.py` match the renders and the guide's descriptions in K–1 P5, 2–3 P6 and P8, and 4–5 P7 |
