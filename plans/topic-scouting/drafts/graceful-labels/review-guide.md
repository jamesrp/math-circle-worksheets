# Review of the facilitator guide: Graceful labels, draft v1

I reviewed `draft/facilitator.pdf` (6 pages) and its sources `draft/src/facilitator.tex` and `solutions.tex` against the final student pages. I rendered all 23 student pages (K–1, 7 pages; grades 2–3, 7 pages; grades 4–5, 9 pages) and all 6 guide pages, and looked at the launch figure at 200 dpi. I also read the outline, both page reviews and the Week 98 model guide.

My own checks are in `review-guide-check/`:

- `check.py` regenerates the page figures from a copy of the pages' `gen.py`, so the networks are the ones actually drawn. It then enumerates every graceful labelling, checks each labelling and count the guide prints, enumerates both ruler problems, runs Rosa's construction for n ≤ 1000, checks all 200 trees with 2–10 dots, runs the caterpillar rule on 3000 random caterpillars, and computes card and cube clearances from the drawn coordinates. Output: `check-output.txt`.
- `launch_and_rosa.py` checks the parts of the launch picture against the K–1 tasks and tests a one-line proof idea for the loop construction. Output: `launch_and_rosa-output.txt`.

## Verdict

This is a strong guide. Every answer it prints is correct, and every "find all" list and count is complete. It matches the final pages: problem numbers, page numbers, the descriptions of the pictures, board sizes and material counts all agree. The overview is theorem-first and gives proofs. It is honest about what the arguments do not cover (six dots, the tree conjecture), and it separates experiment, conjecture and explanation. The guide has one must-fix: the launch picture contains two of the answers to K–1 Problem 1. That is the very reason the guide gives for not using the pages' ✓ example. The other findings are small.

## Must fix

### 1. The launch shows two answers to K–1 Problem 1 and one case of K–1 Problem 6 (pages 2–3, launch paragraph and figure)

The launch attempt puts the empty dot at the top of the triangle, the 1-tower and 2-tower on the two lower corners, and the 4 on the tail. The adult measures the two links at the empty dot as 1 and 2. Read as a row of three dots, the 1, the empty dot and the 2 form 1–0–2, with links 1 and 2. That is an answer to K–1 Problem 1 ("Make the links measure 1 and 2 with these towers. Find all the ways"). The row 1–2–0 along the bottom and right side is another answer. The guide itself bans the pages' ✓ example "because it is one of K–1 Problem 1's answers", yet its own launch shows the same picture.

The triangle also carries 0, 1, 2 with links 1, 1, 2. That is exactly the "3 left over" case that K–1 Problem 6 asks children to rule out. See `launch_and_rosa-output.txt`.

**Fix.** Keep the network (a triangle with a tail, which is on no page) and change the attempt. Leave the tail dot empty, and join it to the 1-tower. Put the 3 and the 4 on the other two corners of the triangle, so the 4 sits between the 3 and the 1:

- links: tail 1, 1 to 3 is 2, 3 to 4 is 1, 4 to 1 is 3;
- the one step to show: "the 3 is two cubes taller than the 1";
- the record: "1, 2, 1, 3: two 1s and no 4" ✗.

I checked this version. None of its rows of three dots answers K–1 Problem 1, its triangle (1, 3, 4) is not a Problem 6 case, and its rows of four dots are not Problem 2 cases. Change the launch materials line to towers of 1, 3 and 4 and cards 0, 1, 3 and 4, and redraw the three panels to match.

## Should fix

### 2. The overview gives no proof idea for the "can be labelled" half of the loop theorem (page 1)

"Why yes" names Rosa's labelling, the zigzag that skips one high label, and then says only that "our script checked it … up to 1000 links." Nothing tells an adult why it works. One sentence does, and I verified it for every n ≤ 1000. Suggested addition: "Along the loop, the zigzag's links run down from n but jump over exactly one length, and that length equals the last label, so the closing link back to 0 supplies it (loop of 8: links 8, 7, 6, 5, 3, 2, 1, then 4 − 0 = 4)."

### 3. The extension to other networks needs its "in one piece" assumption (page 1, loop theorem)

"The proof needs only a walk using every link once and coming home, so it also rules out any network whose dots each touch an even number of links." Such a walk exists only for a network in one piece. The conclusion is still true for a network in several pieces, but only if the argument runs on each piece separately. Week 10's catalog note records a correction for exactly this missing hypothesis. Fix: write "any network in one piece whose dots each touch an even number of links (or each such piece in turn) when 1 + ⋯ + m is odd".

### 4. Several problems have no hint, and two hints give away the method (pages 3–6)

The brief asks for one or two hints, phrased as questions, for each problem. Six problems have none: K–1 Problem 6, Grades 2–3 Problem 8, and Grades 4–5 Problems 1, 6, 7 and 9. Suggested questions:

- K–1 Problem 6: "Can the 3 stay in the tray? Which two pieces could make a 3?"
- 2–3 Problem 8: "Which two squares could make the distance 5?"
- 4–5 Problem 1: "Where can the 5 go?"
- 4–5 Problem 6: "Which of these totals do you already know? Is there a quick way to add 1 to 100?"
- 4–5 Problem 7, five counters: "With counters on 0 and 10, where could a distance of 9 come from?"
- 4–5 Problem 9: "Which card must be next to the 0?"

Two hints hand over the construction: 2–3 Problem 6's "Could you start like a path, 0, 7, 1, 6, …, and leave out one card?" and 4–5 Problem 5's "go round the loop with a path labelling". Mark both as last resorts, after "Which two cards must be neighbours?" Do the same for the general hint "Which two numbers must be at the ends of the longest link?" (page 3), which states the overview's central lemma.

### 5. The Grades 4–5 materials contradict the staffing (page 2)

"Grades 4–5, per pair and per third child: a set of cards 0 to 10 each (two sets) … The table needs two card sets and five counters." The staffing paragraph makes the third child a rotating checker, not a second worker, and five counters is one set. A volunteer cannot tell what to pack. Fix: "4–5 table (a pair and a rotating checker): one card set for the pair and a spare so the checker can test a claim without disturbing the board; five counters no wider than 1.5 cm, reused for both strips."

### 6. Mark 6 and 9 on the number cards (page 2, Materials and preparation)

The cards are square, so children will turn them. A 6 read as a 9, or a 9 as a 6, silently produces wrong differences on the 11-dot path, the loops of 7 and 8, the four-dot network and the five-dot network. Add "underline 6 and 9" to the card-making sentence.

## Minor

7. **Card fit at an angle (page 2, Status and Materials).** The 2.4 cm figure is right only for a card kept square to the page (the 5-link loop is tightest at 2.41 cm). A card turned to its worst angle clears every box only up to 1.95 cm on the 6-link loop, 2.00 cm on the 5-link loop and about 2.1 cm on the 5-dot zigzag, the 3-link loop and the tree with two joined middles. The recommended 2.2 cm card can therefore cover a box corner by 1–2 mm. Suggested wording: "about 2 cm clears every box at any angle; up to 2.4 cm if kept square." The 2 cm snap cube clears every K–1 board at any angle (2.22 cm or more), as the guide says.
8. **Band map (page 1).** "Label or cross out loops of 3 to 7 links" does not match the pages. Grades 2–3 Problem 5 asks children to label or cross out loops of 3 to 6 links; Problem 6 asks only that the 7-link loop be labelled. Suggested wording: "loops of 3 to 6 links, then one of 7".
9. **Prerequisites (page 1, band map).** Grades 2–3 gets only "subtraction within 10" and Grades 4–5 gets nothing. Add the reading and writing each needs (the three-sentence shared rule, which an adult can read; written explanations in 2–3 Problems 4 and 7 and in 4–5 Problems 2, 4 and 6) and the 4–5 arithmetic (sums such as 1 + ⋯ + 101, found by pairing).
10. **Brevity.**
    - Cut the sentences that narrate the page layout: K–1 Problem 1 "The page has seven boards…"; 2–3 Problem 4 "The big board and three small stars give room…"; 2–3 Problem 8 "One big strip and three small ones…"; 4–5 Problem 7 "Board sizes: …", which repeats Materials.
    - "Unpiloted" appears on page 2 and again on page 6; keep one.
    - In Sources, replace the notes about the agent's process ("could not be reached from this environment, and this checkout holds only the JRMF index page") with "Not re-read for this guide; check the current edition of Gallian's survey before saying the conjecture is open."
    - Give `check_guide.py` its permanent location once the week is filed.
11. **Layout (pages 2–3).** The launch text says "the attempt below", but the figure falls at the top of page 3. Keep the two together, or say "at the top of page 3".
12. **Conjecture caveat (page 1).** A sentence would help an adult who searches online. Ringel's tree-decomposition conjecture was proved for large trees in 2020 (Montgomery–Pokrovskiy–Sudakov; Keevash–Staden). The graceful tree conjecture, which would imply it, was still open as far as I know. Treat this as my suggestion, not a source check, and verify it before printing.
13. **Launch logistics (page 2).** "Let children hold the towers and cards for a minute" leaves open which pieces: the guide lists only one launch set for eleven children. Say "each table's own towers or cards".

## Checked and correct (no change needed)

- **K–1:**
  - Problem 1: 4 ways (1-0-2, 2-0-1, 0-2-1, 1-2-0).
  - Problem 2: 4 ways, and the guide's completeness argument holds.
  - Problem 3: 8 ways. Problem 4: 12 ways, and the guide's example is valid on the drawn fork.
  - Problem 5: middles 0 and 3, 6 ways each. Problem 6: towers 1 and 2 can be left over.
  - Problem 7: towers 1 and 3 can be left over, and the guide's argument that the 2 cannot be is right.
  - Problem 8: the middle is empty or the 4-tower, 24 ways each.
- **Grades 2–3:**
  - Problem 1: paths have 4, 8 and 24 labellings. Problem 2: 648.
  - Problem 3: the fork has 12, the tree with two joined middles 48. Problem 4: the middle is 0 or 5.
  - Problem 5: the 3- and 4-loops can be labelled (left over 1 or 2, and 1 or 3); the 5- and 6-loops have no labelling.
  - Problem 6: 168 labellings, 1 in 240 arrangements. Problem 8: {0,1,4,6} and {0,2,5,6}, with a valid case argument.
- **Grades 4–5:**
  - Problem 5: 168 and 384 labellings (1 in 240 and 1 in 945).
  - Problem 6: exactly 9, 10 and 101 can be shown impossible. The printed labellings for 11, 12 and 100 links (skipping 75) are valid.
  - Problem 7: no five-counter ruler; the case argument and the "17 versus 18" shortcut both hold.
  - Problem 8: the four-dot network has 48 labellings; the five-dot network has none.
  - Problem 9: 60 labellings for the spider and 144 for the caterpillar; the caterpillar rule held on 3000 random caterpillars.
- **Overview claims:**
  - Rosa's construction labels every loop with remainder 0 or 3 for n ≤ 1000.
  - All 1, 1, 2, 3, 6, 11, 23, 47 and 106 trees with 2 to 10 dots can be labelled.
  - The odd-count values k(5 − k) ∈ {0, 4, 6} hold. For six dots, k(6 − k) can equal 8, so "neither proof covers six" is right.
- **Agreement with the pages:**
  - Problem and page numbers match: K–1 Problems 3 and 4 share page 3; 2–3 Problems 6 and 7 share page 6.
  - Page counts are 7, 7 and 9. Tray contents match each problem.
  - Strip squares are 2.5 cm (0–6 strip) and 1.7 cm (0–10 strip).
  - The printed trees' 1.2 cm dots are too small for cards, as the guide says.
  - Nothing is keyed to the earlier draft.
- **Launch network:** the triangle with a tail is on no page.

## What works and should be kept

- **The overview.** It is the right model:
  - It states the rule and the "longest link joins 0 and m" lemma, which explains five problems across the bands, and the flip symmetry.
  - It proves the impossible loops twice, by the climbing count and by odd/even.
  - It gives two proofs for the five-dot network and says honestly that neither reaches six dots.
  - It states the tree conjecture with a check-the-survey caveat.
  - It has a clear experiments/conjectures/explanations paragraph and a band map.
- **The K–1 adult support.** The plain-words key ("the tallest tower always stands next to the empty dot") suits a non-mathematician parent. The staffing line draws the right boundary: writing for a child is ordinary support, while choosing tower placements is a signal to go back to a shorter path. The warning to watch for two empty dots and the note on mirror images settle the questions the parent would otherwise face.
- **Child-level arguments.** The third-grade route for the parity proof, with its held prompt and the follow-ups "Does this show the 3- and 4-loops can be labelled?" and "Which loop is the next one it rules out?". The ruler shortcut in 4–5 Problem 7 (17 versus 18). The step-by-step caterpillar rule, and the note that a tree a child cannot label is a candidate, not a counterexample.
- **Honest status and preparation.** Clearances computed from the drawings, with an untested caveat. A realistic preparation time. Exact cube and card counts, matched problem by problem to the trays. A "What to record" list that separates what adults chose from what children chose.
- **First-visit routes.** Concrete routes for each band, which keep the impossible loops in the first hour and save the long searches for a return visit.
