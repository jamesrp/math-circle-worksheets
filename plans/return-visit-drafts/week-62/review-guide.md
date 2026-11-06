# Review: Week 62 return-visit facilitator guide (W62-RV-FAC-v1), draft v1

I reviewed `draft/facilitator.pdf` (8 pages) and its source against the final student pages: K–1 6 pages, grades 2–3 10 pages and grades 4–5 10 pages. I rendered and read every page of all four PDFs. I also read the outline, both page reviews, the draft's README entry, the base guide W62-FAC-v3, the materials W62-M-v1, and the Week 98 model guide. I did not edit the guide or the pages.

**How I checked.** I wrote `review-guide-check/check62.py` before opening the writer's checker.

- **Boards.** I transcribed every board by eye from the rendered pages. The script also parses every 20 mm working board from the generated TeX (circles, lines, arrow directions, allowed-slot labels) and confirms that it matches my transcription: 17 K–1 boards, 25 grades 2–3 boards and 21 grades 4–5 boards.
- **Lists.** It finds every completion of every allowed-list board by brute force.
- **Moves.** It runs a breadth-first search for every move task and replays every move word the guide prints.
- **Rings.** It enumerates the stuck placements and the move families on rings of 3–8.
- **Invented lists.** It counts the failing two-number assignments on the four "can you make it fail" boards. The eight-card tree is done exactly with a dynamic programme over all 1,679,616 assignments.
- **Arrows.** It finds the fewest headers by brute force and by the longest path, and checks every printed schedule.
- **Orientations.** It enumerates all orientations of both Problem 11 boards.
- **Results.** Output is in `review-guide-check/check62.out`: 0 failures. `label_gaps.py` measures how close the allowed-slot labels of neighbouring boards sit.
- **Writer's checker.** I ran a copy of it in `/tmp` afterwards, and it agrees.
- **Not verified.** I could not check the page locators for [S1] (Pak–Redlich Lecture 4) and [S2] (Lehman–Leighton–Meyer section 10.5.2, pp. 435–438). Those PDFs are not in this checkout, and their hosts were refused from this session.

**Verdict.** This is a correct, carefully matched guide, and I found no must-fix items.

- Every answer and every "find all" list is right, and each list comes with a completeness reason.
- Every problem number, page number, board description and material count matches the final PDFs and the base week's kit. The guide follows the final edition, not the earlier draft the page reviews describe. For example, it has grades 2–3 Problem 4 with A fixed at {1, 3}, and the eleven-problem grades 4–5 sequence.
- The overview states real theorems with their assumptions and short proofs.

The should-fix items are about what the overview says children discover and what each band needs, the physical staging of the launch, how K–1 records moves, the first-hour routes, and length. The guide runs about 5,700 words, against 3,025 for Week 98 and 2,430 for the Week 8 return visit, much of it in repeated proofs.

## Must-fix

None found.

## Should-fix

### 1. The overview says what each band does, not what it discovers, and it omits the move facts the younger bands use (p. 1, "A legal placement can be stuck…" and "Band map and evidence")

- **Activities, not discoveries.** The band map lists activities: "Grades 2–3 adds designing lists, recording a move word and testing stuck rings". Only K–1 gets a discovery ("discovers temporary parking"). AGENTS asks the overview to say what children are meant to discover.
- **Evidence status.** The sentence on evidence is generic: "Experiments suggest rules; displayed obstructions and the arguments above explain them". It does not say which claims stay experimental at which band. For example, at grades 2–3, "the five cards never fail" is a conjecture from failed attempts, and the four-case argument is a grades 4–5 explanation.
- **Missing move facts.** Two facts carry most of the K–1 and grades 2–3 move time, but they appear only in the solutions (pp. 3 and 5):
  - With only the two numbers already in use, no counter on a connected network can move: K–1 Problem 4, upper board. A third number is a parking place.
  - The fewest-move lower bound. Every circle whose target differs must move at least once. When every target is blocked at Start, the first move is a parking move, so one more is needed. Two disjoint swapped pairs need one parking move each.
- **Fix.** Add the two move facts as two sentences to the "stuck" paragraph. Replace "Band map and evidence" with a short "What children discover" paragraph, for example:
  - **K–1:** a circle with one number forces its neighbours; a puzzle can be impossible, and one circle or line shows why; with only two numbers nothing moves, and a spare counter lets two circles swap.
  - **Grades 2–3:** an odd ring with the same two numbers fails, and changing one list rescues it; the six-card network can be made to fail, while the five-card one seems not to (a conjecture at this band); each changing circle costs a move, plus a parking move; only rings whose length is a multiple of three can freeze. Arrows are a continuation.
  - **Grades 4–5:** explain the four joint choices against three blockers, the tree argument and the ring rule. Separate stuck from trapped with the up-count. Show that four numbers free any ring, and that the longest arrow path fixes the fewest headers.
  - Tag each item as experiment, conjecture or explanation.

### 2. Prerequisites and reading demands are missing for grades 2–3 and incomplete for grades 4–5 (p. 1 band map; p. 2 "Preparation and staffing")

- **What the guide gives.** AGENTS asks for reading and arithmetic requirements by level. K–1 has one ("matching numerals 1–4, tracing endpoints and adult reading suffice"). Grades 2–3 has none. Grades 4–5 has "counting and ordered comparison suffice".
- **What the pages ask.** The grades 2–3 rule blocks on pp. 1, 5 and 9 run about 40–60 words each, and children write move words such as `B3 A2 C2 B1`. The outline says an adult reads for grades 2–3. Grades 4–5 Problems 4, 7 and 8 ask a child to hold an argument round a whole ring.
- **Fix.** Add one line per band, for example:
  - **Grades 2–3:** "An adult reads the rule blocks and problem text aloud; children read letters and numerals, count to eight and write a short move word; no multiplication."
  - **Grades 4–5:** "Children can read the problems; read the move and arrow rules aloud once. No arithmetic beyond counting. The demand is following a ring and keeping an invariant. The powers such as 6⁵ in this guide are adult checks only."

### 3. The launch cannot be acted out on the printed visual, and it has no prompt (p. 2, "Whole-group launch")

- **Size.** The guide says to "use the opening non-task A–B visual printed on page 1 of every packet … then act out its three panels". The demonstration circles on page 1 are 13 mm across, and the paw move demonstration's circles are under 9 mm. The kit's counters may be 15 mm, so neither picture holds counters. The base guide launched on "an enlarged hand-drawn non-task network".
- **No words.** The guide gives no words to say. The base guide's launch had a short script.
- **Moves.** Deferring the move convention to the tables is reasonable, but every first route reaches moves within the hour: K–1 Problem 4, grades 2–3 Problem 5 and grades 4–5 Problem 5. Three adults will each introduce moves, on a paw that is too small for counters.
- **Fix.**
  - "On a whiteboard or a sheet in a sleeve, draw two circles about 25 mm across joined by a line, with 1 3 beside A and 2 3 beside B. Use the launch kit's headers and counters. Ask: 'These numbers say which counters A may have. Which could go on A? Then what can B have?' A child places A3, then B2, and the partner touches both ends of the line."
  - Give each table adult the same cue for moves: "Before the first move problem, draw the paw large and replace D's 2 by a 1. The partner checks only D's lines."

### 4. How K–1 records a move route is contradictory (p. 2 route table; p. 3 "Problems 4–8"; p. 2 launch)

- **Two instructions.** The route table says "Adult records a successful route after play; no simultaneous tally is required". Page 3 says "A move word can be dictated to the adult and replayed later".
- **Why it matters.** K–1 Problems 5–7 ask for "as few moves as you can". A pair can only compare attempts if someone writes each move as it happens. Recording "after play" loses the count, or asks a child to remember it.
- **D1 at K–1.** The launch line "the recorder writes D1" does not apply at K–1: the K–1 move demonstration has no move word and no Moves line.
- **Fix.** "At K–1 the adult writes each move as the child names it (letter and number, or one tally mark) on scrap paper. Afterwards the children count the marks and try for a shorter route. The children choose every move." Note that the K–1 move demonstration has no move word.

### 5. The first-hour routes are tight for grades 2–3 and split each band's main contrast (p. 2 route table)

- **Grades 2–3, too much.** "About 20 minutes on P1–3" covers eight boards. Two of them have eight circles, each checked line by line by a partner.
- **Grades 2–3, missing contrast.** The route postpones Problem 4: six cards can be made to fail, five apparently cannot. The outline puts that contrast at the centre of the grades 2–3 list work, and the guide's own Problem 4 note calls it "an attainable construction before the impossible hunt".
- **Grades 4–5, P7 deferred.** The route stops at Problem 6 and sends Problem 7 to "a later visit". Yet the guide's Problem 6 note says to keep that result visible because "the coming five-ring has no entirely stuck placement". The surprise of Problem 7 depends on Problem 6 being fresh.
- **Fix.** These are untested estimates, so the changes should be offered as suggestions:
  - **Grades 2–3:** "P1 (the tree), P2, P3 upper board, P4 upper board, about 25 minutes; then P5, about 15 minutes; the rest as continuations."
  - **Grades 4–5:** "If the trio is ready after P6, go straight to P7 and leave P3 or P4 for later."
  - Mark the minute splits "as far as reached".

### 6. Proofs and checker reports are repeated (pp. 4, 6, 7, 8)

- **Repeated proofs.**
  - The five-card/six-card argument appears three times: overview paragraph 3, then p. 4 ("Why no other type fails" and "Lower board"), then p. 6 (grades 4–5 Problem 2).
  - The ring criterion appears twice: overview paragraph 2 and p. 6 "General explanation".
  - The four-number connection proof appears twice: overview paragraph 5 and p. 7 "Every legal placement on every simple ring…".
- **Checker narration.** The solutions also report the checker:
  - p. 6: "The verifier checks all 6⁵ = 7,776 …", "All 6⁸ = 1,679,616 … pass the independent checker. The proof, not that finite count, gives the general result."
  - p. 7: "The checker finds 30 legal five-ring placements …"
  - p. 8: "The checker examines all 64 orientations …"
- **Repeated disclaimers.** For example, p. 6 Problem 1: "not a claim based on trying several starts"; p. 7 Problem 8: "checking rings of 3–8 only tests instances".
- **Fix.** In the solutions, keep the child-sized explanation and write "(proof: overview)". Put the finite counts into one sentence under "Local adaptation and limits". This frees about half a page for items 1–3.

## Minor

1. **Launch sentence on indirect paths (p. 2).** "For arrows, every arrow must be satisfied; an indirect path also forces earlier/later order even without a direct arrow." In the launch section this reads as something to tell the children, and it gives away part of what Problems 9 and 10 let them find. A placement that ignores a chain always breaks a printed arrow, which the partner check catches. **Fix:** move it to the Problem 9 note as an adult response: "If two cards on one chain share a header, ask the checker to test each arrow on the chain."
2. **Label-proximity note (p. 6).** The K–1 p. 1 warning is right: the star's C label "2" and the square's D list "1 3" sit 6 mm apart on one line. The grades 4–5 note says "especially the bottom row", but on p. 3 the closest labels from different boards are in the top row: upper-left B "1 2" and upper-right E "2 3", 13 mm apart on one line. In the bottom row they are at least 17.7 mm apart. Grades 2–3 p. 2 has the same 13 mm top-row gap. **Fix:** say "top row", or drop the grades 4–5 note, since 13 mm is a mild risk.
3. **Draft-history wording (pp. 4, 6).** "The revised upper board offers …" and "Student page numbers no longer equal problem numbers". **Fix:** "The upper board offers …" and "In this packet page numbers differ from problem numbers:".
4. **Vague hedge on the up-count (p. 1).** "This invariant is not a claim that every pair with equal counts connects on every graph". The up-count is defined only on rings. **Fix:** give the concrete limit instead: "Equal counts are not enough: on the six-ring, 123123 and 231231 both have six ups, and neither can move."
5. **Heading before its example (p. 1).** "Two allowed slots per card need not suffice, even on a two-slot network" is followed by trees and rings, which do not show it. The six-card example that proves it comes a paragraph later. **Fix:** add "(six cards, A and B each joined to C–F, below)" to the heading sentence.
6. **No spare student set (p. 2).** The base print plan includes one spare set; this one prints exactly 42 sheets. **Fix:** "plus one spare of each page in the chosen route".
7. **Why two placements for arrows (p. 2 or p. 5).** The arrow rules ask for cards under headers and a counter on each circle. The page review asked the guide to say why. **Fix:** add one clause: "the counters let the partner check each arrow's two ends on the mat, as in the base week".
8. **Sources heading (p. 8).** Sources sit under the page heading "Grades 4–5: arrows, schedules and source boundaries". **Fix:** give "Sources" its own section heading.

## Checklist results

1. **Correctness: all verified, 0 failures** (see `check62.out`).
   - **K–1.** P1 231, 213, 3121, 1213, each unique. P2: none / 1212, 2121 / none / 1231. P3: 123123 / none. Moves: P4 –, 3; P5 4; P6 7; P7 6; P8 –, 4. Every printed move word replays legally, and every minimum agrees with breadth-first search.
   - **Grades 2–3.** P1 43114322 / none. P2 no, yes (12312, 21321), yes (121212, 212121), no. P3 none / 241133, 243133. P4: 24 of 7,776 fail, all with B = {2, 4} and C–F carrying the four mixed pairs; 0 of 1,296 fail on the five-card board. P5–7: 3, 4, 6, 7, –, 4. P8: only the six-ring, with exactly the six listed strings; rings of 3 and 6 have 6 stuck placements each, rings of 4, 5, 7 and 8 have none. P9: 4 headers, and the schedule is earliest placement. P10: cycle / 5 / 4 / 5.
   - **Grades 4–5.** P2: 0 of 7,776. P3: 0 of 1,679,616. P4: the six strings / 123122, 213211 / 343434, 434343. P5: –, 4. P7: Goal 1 in 5 (E3 D2 C1 B3 A2); Goal 2 unreachable. The five-ring has 30 placements in two families of 15, with 4 and 1 ups, and every placement can move. P8: 4 (B4 C2 B3 E3); rings of 3–7 are one family with four counters. P9: 4. P10: 4 / 5, with both printed schedules. P11: minimum longest paths 3 (64 orientations) and 2 (256, exactly 2 optimal); both witnesses check.
   - **Theorems.** The ring rule holds for every two-number list from 1–4 on rings of 3–7.
   - **Lower bounds.** The guide's lower-bound arguments are valid, including the square's "two separate pairs" argument, which I checked by hand.
2. **Agreement with pages and week: passes.**
   - Problem and page maps (K–1 P4–5 on p. 4, P6–7 on p. 5; grades 4–5 P2–3 on p. 2, P11 on p. 10) match the PDFs.
   - The kit matches W62-M-v1 and W62-FAC-v3: 7 kits; 56 cards, 28 headers, 224 counters, 14 sleeves; 31 × 38 mm cards; a 16 mm dashed key circle (measured); 3 card-stock sheets; 8 markers.
   - The print total of 42 sheets is right, and the staffing matches the base guide.
   - Nothing contradicts the base guide.
3. **Overview: passes with should-fix 1.** It has theorems, assumptions, limits and followable proofs, all before any solution. The discoveries map and the evidence status are thin.
4. **Launch: passes with should-fix 3.** It is brief, uses a non-task instance and gives no theorem or answer. It needs a board large enough for counters, and a prompt.
5. **Usability and age fit.**
   - Preparation time, staffing, roles and the "smaller board rather than demonstrate" rule are realistic and respect the children's choices.
   - Hints are questions.
   - Gaps: should-fix 2, 4 and 5.
6. **Brevity:** should-fix 6.

## The writer's flagged page issues

- **Adjacent labels.** I agree on K–1 p. 1 (6 mm). I disagree that the grades 4–5 p. 3 bottom-row lists are "similarly close": that page's closest pair is in the top row, at 13 mm (minor 2).
- **Arrow caveat.** I agree that "Cards with no arrow between them may share a header" can be misread. The misreading corrects itself, though, because a broken arrow shows at the partner check. I would keep the caveat as an adult response at Problem 9 rather than say it in the launch (minor 1).
- **Older answer keys.** I agree they do not fit the final edition. The guide is keyed to the final pages.
- **Rule retention.** I agree it is untested. The guide states this honestly.

## What works and should be kept

- **The mathematics.** It is correct throughout, and each list comes with a completeness reason. Examples: the four-case table for the six cards, the "C must be 3" reason on the changed five-ring, the forced chain that closes at F, and the six stuck strings with why they account for every start.
- **The overview's proofs.** They are short and an adult can follow them:
  - the tree argument;
  - the ring rule with its "place u last" trick;
  - the stuck-ring "repeats 1, 2, 3" argument;
  - the up-count with a non-task local example (2 1 2 → 2 3 2);
  - the fix-one-card-at-a-time proof for four numbers;
  - earliest placement against the longest path.
  Each states its assumptions: distinct choices, unit time, unlimited capacity, no directed cycle.
- **Impossible answers.** Impossibility is treated as an answer throughout. Examples: "Illegal placements, such as all 1s, are not answers", "The absent fifth header is the intended obstruction", and "do not equate 'I couldn't make it fail' with a proof".
- **Problem 11.** The argument works with arrows (sources and sinks alternate) rather than recalling the first visit's odd-ring answer.
- **The adult's role.** "Children choose placements and moves … If the adult must choose every move, stay with a smaller board rather than demonstrate the solution"; split the four A/B cases between pairs rather than make one child copy a table.
- **Honesty about evidence.** The guide is open about what is unpiloted and physically unrehearsed. Its sources are clearly marked as consulted directly, or as outline context only.
- **Lookup convention.** The alphabetical-string convention for answers is compact and is explained once per band.
