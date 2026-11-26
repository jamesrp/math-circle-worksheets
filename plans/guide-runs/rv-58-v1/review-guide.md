# Review: Week 58 return-visit facilitator guide (Fair division), draft W58-RV-FAC-v1

I reviewed `draft/facilitator.pdf` (8 pages) and its sources against the final student pages: K–1 (5 pages), grades 2–3 (6 pages) and grades 4–5 (6 pages). I rendered and read every student page and every guide page. I also read the outline, both page reviews, the draft's README entry, the base week's guide (W58-guide-v4, 9 pages) and materials file (W58-materials-v3, 8 pages), and the Week 98 model guide. I did not edit the guide or the pages.

**How I checked.** I wrote my own checks in `review-guide-check/` before opening the writer's checker. The trains were read from the rendered pages and matched against the page generator's lists. Everything is exact, using Python fractions.

- **`check_trains.py`** tests every printed train against every set of gaps and every way of putting the pieces in two trays. It also covers:
  - all 70 orders of four reds and four blues;
  - all 790 trains a K–1 pair can build from six reds and four blues;
  - every even-count train up to 10 cards by brute force, and up to 14 cards by the half-window test.
- **`check_cuts.py`** solves:
  - the strip on a 0.5 mm grid, with cards A and B and with the K–1 colour-only rule;
  - the X Y Z exact halves with one and two cuts on a 0.5 mm grid, plus the algebra;
  - the marking game in all six orders, giving every mark, taker, the nine observer values and every envy relation;
  - all 120 orders of the Problem 7 card row;
  - the two-red marking cuts.
- **`measure_rows.py`** measures the printed rows on the student pages.

The outputs are in the matching `.out` files. Afterwards I copied the writer's `check_guide.py` and `checked-tables.tex` to `/tmp` and ran them; they pass. pdfLaTeX is not installed here, so I could not check the compile log. The rendered pages show no overflow, clipping or footer collisions.

**Verdict.** The mathematics is correct and complete, and I found no must-fix items.

- Every printed train answer is right, and every uniqueness claim holds. That includes the two minimum gap sets for grades 2–3 Problem 2 row 6, (2, 7) and (3, 8).
- The 60/180 mm strip answer, the 25/75/125 mm X Y Z answer and the determinant 576 are right.
- All six marking games are right, both rounds' marks, all 54 observer values and the full envy column.
- The 5.5 half point, the 50/3 and 100/3 mm two-red cuts, and the counts 36/34 and 790 = 441 + 179 + 170 are right.
- Problem and page numbers match the final PDFs, not an earlier draft.
- Materials agree with W58-materials-v3 and do not contradict W58-guide-v4.
- The launch is a non-task instance and gives nothing away.

The should-fix items are about four things:

- how the panel game and the hour actually run;
- what children are meant to discover;
- one piece of background theorem the overview leaves out;
- length. At 4,709 words the guide is about 55% longer than Week 98 (3,025) and nearly twice the Week 8 return-visit guide (2,430).

## Must-fix

None found.

## Should-fix

### 1. The overview omits the general two-taste fact that the train window proves (guide p. 1; also p. 6, grades 4–5 Problem 3)

- **What the guide says:** The overview proves the train case and the colour-uniform strip ("half of each colour gives half the value to every taste that is additive and uniform within each colour"). On p. 8 it then sets aside "general necklace … theorems".
- **What is missing:** The outline's headline for kernel 1 is that two people never need more than two cuts, whatever their tastes, proved by the same sliding window. It also gives the k-tastes, k-cuts statement as literature background. An adult at the 4–5 table who hears "what if someone likes the left end of the red better?" has no answer. The guide also never says that the X Y Z result is the tight case of that general statement.
- **The printed question is fine:** For grades 4–5 Problem 3 as printed, the guide's answer is right. "Cards with any other numbers" are still uniform within each colour, so the same 60/180 cuts work for everyone, and the half-of-each-colour argument is enough. I agree with the writer on that point.
- **Fix:** Add two or three sentences to the overview.
  - **The continuous window:** Slide a piece that A values at exactly half from the left end to the right end. It ends as the complement of where it started, so B's value of it passes through half. That piece takes at most two cuts. The train proof is the whole-card version of this argument.
  - **Background, labelled as literature and not checked here:** k tastes on a row never need more than k cuts (Hobby–Rice; necklace splitting, Alon–West). So X Y Z's three cuts are as bad as three tastes can be.
  - **Keep the boundary:** No page asks for this.
  - **Also add a clause on X Y Z:** "adding the three equal-value conditions shows each tray holds half of every panel", so the overview's three-cut claim can be followed without turning to p. 6.

### 2. "Discovery and band map" describes activities and prerequisites, not discoveries or demands (guide p. 1)

- **What the guide says:** "Here children seek exact equality for both observers, minimize cuts, and separate a guaranteed share from a desirable outcome. K–1 matches colours and counts to six, with adult reading…" The only line on evidence is "Experiments suggest a rule; a full small catalogue or an argument establishes it."
- **Why it falls short:** AGENTS asks for what children are meant to discover, separated into experiment, conjecture and explanation, with an honest account of reading and recording demands. None of the K–1 or 2–3 destinations appears here.
- **Fix:** One line per band. For example:
  - **K–1 discoveries:** a train whose halves do not match can still be shared by lifting out a middle piece, and nobody finds a train that needs three places. These are experiments; the second may become a shared conjecture.
  - **2–3 discoveries:** one cut works exactly when the front half matches (experiment, then a checkable rule). No even train needs three cuts (conjecture; the window is an optional explanation). A and B's strip needs two cuts (recalling the first visit's 80 and 160 mm). The marking game gives everyone 4 but someone still wants another piece (experiment).
  - **4–5 discoveries:** the window explanation, the three-cut proof for X Y Z, why the game guarantees a third and is only a floor, and the two-split-card bound.
  - **Demands:**
    - an adult reads the train rules, and reads the 2–3/4–5 marking-game paragraph aloud;
    - 2–3 Problem 3 needs millimetre measuring and halves of a panel worth 3;
    - each 2–3 game has one quarter-panel mark (already noted on p. 5);
    - drawing 8- to 12-card trains in boxes is a real recording load for K–1 and 2–3, so the adult may scribe after the child builds.

### 3. The launch never shows the recording or states the goal (guide p. 3, "Launch together")

- **What the guide says:** "Point to the chosen gap, move both intact pieces into trays, and compare colour counts…" That is good, and it rightly withholds the two-cut trick.
- **What is missing:** AGENTS asks the launch to show "what they are trying to find or record". Every band's first problem asks children to draw a line at each place (K–1) or mark cuts (2–3, 4–5), and to use as few as possible. Neither appears in the launch.
- **Fix:**
  - Have two children build RBRBRR and do the split.
  - Then draw the bar in that gap on a sketch, as the page's example shows.
  - Then say the goal once: "share each train pulling it apart at as few places as you can".

### 4. The hour has no per-problem timing, and preparation has no single print list (guide p. 2)

- **Timing:** The guide gives the hour's split (5/5/35/5/10) and a first route per band, but no minutes per problem. The base guide and Week 98 both give rough ranges. Add them for each band's first route. For example:
  - K–1: Problem 1 about 15 minutes, Problem 2 about 15–20.
  - Grades 2–3: Problem 1 about 10, Problem 2 about 10–15, then Problem 3 or the first panel game for about 15.
  - Grades 4–5: Problem 1 about 15, Problem 2 about 10, Problem 3 about 15.
  - Mark all of these as estimates.
- **Print list:** "Consumables for all later tasks" mixes the first hour with later visits, and the counts are spread over four paragraphs. A volunteer has to add them up: five extra p. 1 for trains, one more p. 1 for Problem 8, up to 11 extra p. 5 (12 panel sets less the base set), one p. 4, crayons. Add one short table, "Print beyond the base kit", with two columns:
  - **First hour:** five unmounted p. 1, crayons, and only if the middle table plays the panel game, one p. 4 plus four p. 5.
  - **Later visits:** the rest.
  - Base the 20–30 minute estimate on the first-hour column.
- **Fewer panel sets:** Suggest recording panel games on the actual-size page rows (finding 5) and cutting physical panels only for the first game. That cuts the panel-set budget substantially.

### 5. The panel game needs a short run sheet, and the guide never says which page diagrams are actual size (guide pp. 2, 5, 7)

- **What the pages draw:** I measured the final PDFs (`measure_rows.out`).
  - The red and blue strips are drawn at 168 mm for 240 mm, about 70%. The guide says so correctly ("Student strip pictures are schematic").
  - Every X Y Z row is printed at actual size, 150 mm with 50 mm panels: grades 2–3 pages 5–6 and grades 4–5 pages 3–4.
  - The grades 4–5 Problem 7 card row is actual size too: five 25 mm cards, 125 mm.
- **What the guide says:** Nothing tells the adult that children can measure marks directly on the printed panel rows, or lay the real cards along the Problem 7 row (the page says "Lay the goods cards touching in this row"). A reader of "Student strip pictures are schematic" may assume all the diagrams are.
- **What else is missing:** The marking game is new to every band and has two rounds of marks. Beyond "read the panel-game's printed first-round example at its table", the guide does not say how a round runs physically.
- **Fix:** Add a four- or five-line run sheet under grades 2–3 Problems 5 and 6, and cite it from grades 4–5 Problem 5:
  - Lay the three panels in the printed order beside the page row.
  - Each recipient, using only their own three-person card, marks the page row with their initial.
  - The referee names the leftmost mark, and the taker's piece is cut (or just bracketed on the row) and goes in their tray.
  - The other two mark again from the new left end with a second initial.
  - The last person takes the rest, then everyone checks all three trays with their own card.
  - Also state that the panel rows and the Problem 7 row are actual size, and that the 2–3 game uses all four children, so both pairs stop their pair work together.

### 6. Label every solution heading with its band (guide pp. 4–8)

- **What the guide does:** It switches between "Grades 2–3", "middle", "Grades 4–5" and "upper". Several subheadings carry no band: on p. 6, "Problem 3 on student page 2" sits under "Upper exact halves…"; on p. 8, "Problem 7 on student page 5" and "Problem 8 on student page 6" sit under "Upper card continuations…".
- **Why it matters:** Problem numbers repeat across bands, and Problem 3 is a strip task in both 2–3 (p. 5) and 4–5 (p. 6). An adult flipping for "Problem 3" can land in the wrong band.
- **Fix:** Use "Grades 2–3" and "Grades 4–5" throughout, in every section title and every problem subheading, as Week 98 does.

### 7. Length: cut process notes, revision history and padding (whole guide)

The guide is at the 8-page ceiling and runs 4,709 words. Findings 2–5 add material, so make room with cuts that lose nothing a facilitator needs:

- **Revision history**, which an adult who never saw the earlier draft cannot use:
  - p. 4: "the printed rule now says straight across" (write "the page says straight across") and "The revised prompt is a partner game".
  - p. 8: "Earlier answer keys were not treated as final-page authority. The numerical instances and this checker were derived afresh." Also the list of structure models consulted.
- **Padding:**
  - p. 1: "Other pencil marks are not cuts"; "A zero-total person can take the empty prefix; the bound is still valid"; "These are complete allocations: nothing is discarded".
  - p. 3: "Row numbers below count down the page and are not additional problem numbers"; "All three packets print this example before Problem 1".
  - p. 7: "All six orders are listed, since three distinct panels have 3! = 6 orders"; "The envy column is complete, not just one example per game"; "Brackets here describe lengths; shared endpoints carry no value".
- **Adult enumerations a K–1 volunteer does not need:**
  - p. 4: the 1/16/16/1 class breakdown for K–1 Problem 3. Keep "34 of 70; one place works exactly when the first four cards hold two reds".
  - p. 4: the 790/441/179/170 census for K–1 Problem 5. Keep the window argument.
  - p. 6: the determinant sentence, which repeats the elementary proof just given.
- **Materials table (p. 2):** It restates the base guide's card sizes. A one-line pointer to W58-guide-v4 p. 3, plus the additions table from finding 4, would be shorter.

## Minor

1. **K–1 Problem 3 example (p. 4).** "RRRRBBBB is one example; do not supply it before children invent their own". But RRRRBBBB is already printed as K–1 Problem 2 row 5, so a maker can copy it. Say instead: "Problem 2 row 5 is one such train; if a maker copies it, ask for a different one."
2. **Grades 4–5 Problem 4, last sentence (p. 6).** "This proves the panel fractions and cut positions, not that only one physical arrangement of halves in trays is allowed" is cryptic. Say what is meant: on a row, the three cuts at 25, 75 and 125 mm with alternating pieces are forced, apart from swapping trays. If the panels are treated as separate pieces, any choice of one half of each panel per tray works.
3. **Grades 4–5 Problem 6 qualification (p. 7).** "Values must remain nonnegative, additive and uniformly divisible within panels" is stricter than the theorem. Uniform density is not needed; value that builds up continuously along the row is enough, as the overview says. Write "nonnegative, additive and divisible with no value stuck at a point".
4. **Hints that are instructions (p. 5).** "Now keep that same card and check all three trays" is a direction. Use a question: "Which card are you using for all three trays?" Also, "pause the game and return to one-panel halves" is unclear. Name the action, for example "redo the page's Y-panel example with a real panel".
5. **Upper table: pair or trio (p. 2).** The upper table is called "the upper pair" for materials and "the upper trio" for refereeing. Say once that it is three children with one pair kit, as in the base week ("one pair and a rotating referee"). For the panel games all three are recipients and the adult referees.
6. **Procaccia provenance (p. 8).** The guide says the chapter was "consulted online" and adds §13.3.2 (pp. 4–5), which the base guide does not cite. The host was blocked from this environment, so I could not verify that reference. Keep the claim only if the section was actually re-read; otherwise cite it through the base guide's consulted range (§§13.2–13.3.3, pp. 1–6).

## Where I agree or disagree with the writer's report

- **Flagged page risks 1–8:** I agree with all eight and with how the guide handles them.
  - The quarter-panel warning for the 2–3 games is correct: A, B and C mark at 112.5 mm in XZY, YXZ and ZYX respectively.
  - The "whatever values the cards give" qualification is a useful catch (but see minor 3).
- **Item 5, "strip pictures are schematic":** Correct but incomplete. The panel rows and the card row are actual size (should-fix 5).
- **Item 7, upper Problem 4:** I agree in substance; the guide's sentence needs rewording (minor 2).
- **Leaving out the continuous two-knife theorem:** I agree it is not needed to answer grades 4–5 Problem 3 as printed. I disagree that the overview should leave it out entirely (should-fix 1).
- **Procaccia "consulted online" and "no overfull boxes":** I could verify neither here. The rendered pages are clean, and the writer's checker passes.

## Checklist results

1. **Correctness:** every printed answer agrees with my checks (`check_trains.out`, `check_cuts.out`).
   - K–1 trains: Problem 1 is 1, 2, 1, 2, 1, 1. Problem 2 is 2, 1, impossible, 1, 2, 1, 2.
   - Grades 2–3 Problem 2: 2, 2, 1, 2, impossible, 2, 1.
   - Grades 4–5 Problem 1: 2, 1, 2, 2, 1, 2.
   - Strip: one cut cannot work (A's exact cut is at 80 mm, B's at 160 mm); two cuts at 60 and 180 mm are the only two-cut answer.
   - X Y Z: no one- or two-cut answer; three cuts at 25, 75 and 125 mm.
   - Marking game: both takers get exactly 4 in every order. The last person gets 11 (XYZ, YZX, ZXY) or 8 (the other three). The envy lists match.
   - Problem 7: the half point is always strictly inside a red card.
2. **Agreement with pages and week:** every problem number and student page number matches the final PDFs. The materials sizes and pages match W58-materials-v3, and nothing contradicts W58-guide-v4: same kit, staffing pattern, scissors held by adults, uniform value across the whole square, and A/B cards kept apart from the three-person cards.
3. **Overview:** It states real theorems with assumptions and followable proofs, before any solution. It is weak on discoveries and on the experiment/conjecture/explanation split (should-fix 2) and on the general background theorem (should-fix 1).
4. **Launch:** brief, concrete, on the printed non-task example RBRBRR (which appears in no task), and free of the two-cut idea. It is missing the recording action and the goal (should-fix 3). The 30 mm scrap example is a neutral non-task instance.
5. **Usability and age fit:** The status is honest and the staffing respects children's choices. The materials match the pages' needs, including six reds and four blues per pair, crayons and paper reds for Problem 8. Missing: per-problem timing, a first-hour print list, the panel-game run sheet and the actual-size note (should-fix 4 and 5).
6. **Brevity:** too long (should-fix 7).

## What works and should be kept

- **The overview's train theorem.** The half-length window, "first and last windows are complements, so the red count must pass through half", and "one cut works exactly when the first half already has half of each colour" are clear, correct and usable at three levels.
- **The complete marking-game tables (p. 7).** Both rounds' marks, every observer's three values and every envy relation make Problem 5 checkable at a glance. Keep the note that the target stays 4, "not a third of the remainder".
- **The 2–3 quarter-mark paragraph (p. 5).** It names the 112.5 mm mark, says why it does not change the outcome, and says not to pretend it is a half-panel point.
- **The grades 4–5 Problem 6 qualification (p. 7).** A fixed target of 4 fails when totals change; the three-panels-worth-8 counterexample shows it. This protects the adult from a false general statement on the page.
- **The completeness and uniqueness statements.** These include the two minimum gap sets in 2–3 Problem 2 row 6 and the 36/34 criterion for four reds and four blues.
- **The elementary X Y Z argument.** Sum the three equations, then compare with each one. A grades 4–5 child can follow it.
- **Practical cautions.**
  - Put the two-person A/B cards away before the panel game.
  - Strip pictures are schematic; measure the real strip.
  - Never cut a sturdy card; use an unmounted replacement for whichever red is cut.
  - Odd trains are "impossible", not "three cuts".
  - If an adult must choose the marks, pause.
- **The honest status line and "After use" note.**
