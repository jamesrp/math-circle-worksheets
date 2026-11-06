# Review: Week 53 return-visit facilitator guide (W53-RV-FAC-v1), draft v1

I reviewed `draft/facilitator.pdf` (8 pages) and its source against the final student pages: K–1 (7 pages, Problems 1–8), grades 2–3 (6 pages, Problems 1–8) and grades 4–5 (10 pages, Problems 1–12). I rendered and read every page. I also read the outline, both page reviews, the return-visit README entry, the base Week 53 guide (W53-guide-v4) and the Week 98 and Week 8 return-visit model guides. I did not edit the guide or the pages, and I did not run `build.sh`.

**How I checked.** I wrote `review-guide-check/check_answers.py` before opening the writer's checker. It transcribes every map from the rendered pages and brute-forces every link subset, simple route and trip. Its output is in `check_answers.out`: 80 checks, all passing.

- **Fixed maps.** It recomputes every cost, every "find all" list, the group thresholds, lowest-dearest routes, trips before and after repricing, and the guide's shortest-distance table for 4–5 Problem 8.
- **Free-choice and stuck-purchase problems.** It checks the K–1 Problem 8 family against brute force for spoke prices 1–12, the 2–3 Problem 6 rule, and a breadth-first search over buy, return and swap changes for 4–5 Problem 10, with caps of 8, 9 and 10.
- **General claims.** It tests the overview's claims on several hundred random small maps: the route fact, one shared price list, cost = Σ(c_k − 1), repricing, and the r − 2 bound.
- **Geometry.** `measure_maps.py` measures place sizes and spacing in the PDFs. On every working map the places are 10 mm across (squares 9.2 mm) and at least 40 mm apart, as the guide says.

Afterwards I ran a copy of the writer's `check_guide.py` in `/tmp`, and it passes.

**Verdict.** This is a correct, carefully scoped guide. I found no must-fix items.

- **Answers.** Every printed answer and every "find all" list is right, and each list comes with a completeness argument.
- **Numbering.** Problem and page numbers follow the final PDFs, not the earlier drafts the reviews describe.
- **Overview.** It opens with real theorems and proofs an adult can follow: lowest-dearest routes and the converse, the group counts with the price list and cost formula, repricing, and the limits that optional places set.
- **Scope.** It keeps the no-squares scope straight, including 2–3 Problem 7 against Problem 8.
- **Launch.** It uses a non-task line and gives nothing away.

The should-fix items concern the first-hour route, returning against new children, and length.

## Must-fix

None found.

## Should-fix

### 1. The one-hour routes leave out kernels the outline makes central for K–1 and 4–5 (p. 2, "Staffing and one hour")

- **K–1.** "Young first route: P1–3; later P4–6". The outline's K–1 emphasis has two parts: opening links by price (kernel 1), and paying for a network with and without the optional place, comparing the two piles (kernel 3). The route covers only kernel 1, and P1 is the base week's Problem 2 map. The square comparison is the most concrete new idea for this table.
- **Grades 4–5.** "P1–4, then one of P5–6" is all kernel 1. Trips (kernel 2) and the stuck star purchase (kernel 3), which the outline names as core 4–5 explanations, are put off to "later". P2 and P4 are both full catalogs of the same kind.
- **"Later" is ambiguous.** It can mean later in the hour or on another visit.
- **Fix:**
  - K–1: use P1, P2, P4, then P3 or P5 if time allows.
  - Grades 4–5: use P1, P3 and P7, then P9 or P10. Pool P2's six networks across the trio, or save P2 and P4 for a later visit.
  - Write "on a later visit" where that is meant.
  - If the writer prefers a kernel-1-only first hour, say so as a deliberate choice and name the visit that covers trips and squares.

### 2. The guide does not say which children are new or which maps repeat the base week (pp. 2–3)

- **Who is new.** The outline says most K–1 children will not have met Week 53, and that many 2–3 children met only the base pages 1–4, so the swap test cannot be assumed. The guide never says either.
- **Repeated maps.** Several maps are base-week maps:
  - K–1 P1 is base Problem 2 with the same prices.
  - 4–5 P4 is base Problem 4.
  - 2–3 P5, 4–5 P8 and 4–5 P9 (bottom) use the base six-place map from Problems 6 and 8.
- **Fix:** Add two or three sentences under "Print and prepare" or the K–1 heading:
  - Name these repeats, so adults expect remembered answers. The new question on each map (rings, a shared price list, trips) is the point.
  - Say that the shared launch is a first introduction for most K–1 children.
  - Then drop the suggestion to print base p. 4, which 4–5 P4 already reprints (see Minor 10).

### 3. The band map says what each band compares, not what it should notice (p. 1, "Discovery and evidence")

- **What the guide says:** "K–1 compares reachable groups and optional-place payment piles … Grades 2–3 compares dearest links, sums and invented prices … Grades 4–5 connects catalogs to proofs". Each line names an activity, not a destination. The theorems above it are good, but a parent reading only this paragraph does not learn what to listen for.
- **Fix:** Give each band one discovery and one conjecture it might state, for example:
  - **K–1:** "The pawn first crosses from A to F at 3 dots, and no cheapest network on that map avoids a 3. A square can save, tie or cost extra."
  - **Grades 2–3:** "The smallest dearest link between two places is the price at which they first share a ring. Adding to every price keeps the network but can switch the trip."
  - **Grades 4–5:** why both of these hold, and where they break once there are squares.
  - Use the word "conjecture" once: a pattern seen on one map is a conjecture until the cut argument explains it.

### 4. The launch never states the goal (p. 2, "Whole group")

- **The problem:** AGENTS asks the launch to show "what they are trying to find or record". The X–Y–Z line shows buying, paying, tracing and refunds, but no sentence says what a network is for or that cheaper is better. The base guide's launch says it aloud: "Can your traveler reach every circled place on the roads you bought?"
- **Fix:** Add one spoken line after "Buy YZ": "A network lets the pawn walk between every circled place on bought roads. On your maps, try to pay as few counters as you can." The two-link line still has no optimization question, so nothing is given away.

### 5. Reading and recording loads are not located, and the K–1 adult's role is thin (pp. 2–3)

- **What the guide says:** "read or scribe without choosing links". It does not say where the load falls.
- **Long reading:** K–1 P2 is three lines; 2–3 P3 is four; 2–3 P4 and 4–5 P7 define trips. 4–5 P6, P10 and P12 are dense; Lee's sentence in P12 is the hardest in the packet.
- **Recording:** K–1 P2 asks for groups ringed on four small record maps with places about 5 mm across. 2–3 P1 and 4–5 P2 ask children to draw six networks.
- **The K–1 adult:** The base guide puts the parent volunteer at K–1, and that adult gets the most technical K–1 notes, such as "min(x + y + z, x + y + 4, x + 8)".
- **Fix:** Add two or three sentences under "Staffing":
  - The adult reads K–1 P2 and 2–3 P3 once while pointing to the small pictures.
  - At K–1 the child points to each group and the adult may draw the ring.
  - The adult paraphrases P10's "change" and Lee's claim before the trio starts.
  - Pool the six networks across the pairs.
  - Name the parent volunteer at the K–1 table, as the base guide does. Put the bold K–1 answers first and the adult derivations after them; they already mostly are.

### 6. The guide is longer than its models and repeats material (pp. 2, 5–8)

- **Length.** It runs about 4,750 words, against 3,026 for Week 98, 2,440 for the Week 8 return-visit guide and 4,380 for the whole base Week 53 guide.
- **P12 (p. 8).** It re-proves the base week's local-to-global sufficiency argument almost word for word: base guide p. 7, "Take any competing tree … Repeat". The writer brief said not to re-explain first-visit mathematics.
- **Restated answers.**
  - 4–5 P1 and P3 restate 2–3 P2 and P3.
  - 4–5 P7 restates 2–3 P4.
  - The first three rows of the 4–5 P8 table repeat 2–3 P5.
  - The counter-overflow advice appears on p. 2 and again on p. 5.
- **Fix:**
  - **P12:** Keep the one-line reduction ("the unused link f is itself a route, so Lee's condition is the exchange certificate") and cite base guide p. 7 for the rest.
  - **Grades 4–5:** Cross-reference the 2–3 entries for P1, P3 and P7 the way 4–5 P2 already does. Keep only the squared row and the trip certificate in 4–5 P8.
  - **Counters:** Drop the p. 5 repeat.
  - This should bring the guide to about 7 pages without losing any answer or proof.

## Minor

1. **Overview, optional places (p. 1).** "The preceding all-place price-list, repricing and converse claims do not extend to optional places" leaves out two claims that also fail on the 4–5 P9 maps.
   - **The route fact:** on the spokes-3 star, the cheapest network AB, BC gives the A–C route a dearest link of 4, but ASC has 3.
   - **Cost from groups:** the groups predict 9 there, but the cheapest network costs 8.
   - **Fix:** Write "the route, price-list, cost-from-groups, repricing and converse claims".
2. **2–3 Problems 4 and 5 (p. 5).** "All three cheapest networks are AB, BC, CD" reads as if the map had three cheapest networks. Write "On all three maps the cheapest network is AB, BC, CD", and the same for Problem 5.
3. **2–3 P1 hint (p. 4).** "Can two pairs share different triangle choices?" is unclear. Use "If you keep the right side the same, how many ways can you join A, B and C?"
4. **4–5 P2 hint (p. 6).** "Organize the records by what changes near A, then … near E" prescribes the organizing method and reveals the product structure. Ask "Which links are in every one of your networks? Where do your networks differ?"
5. **Spare record maps (pp. 4, 6).** The "spare record maps are workspace" note appears only for K–1, where there are 4 boards for 3 answers. The note matters more for 2–3 P1 and 4–5 P2 (8 boards, 6 answers) and for 4–5 P4 (6 boards, 3 answers). Repeat it once there.
6. **4–5 P8's general question (p. 7).** It asks which changes *can* change the cheapest networks. The guide gives only changes that cannot. Add one that can: replacing every price p by 7 − p makes the cheapest networks cost 15, and none of them is AB, BC, CD, DE, EF (checked). This shows that keeping the order of prices is what matters.
7. **4–5 P12 (p. 8).** Anchor Lee's claim on a map before the proof. On P5's square, the cost-9 network BC, CD, DA fails Lee's test for A and B: its route A–D–C–B has dearest link 3, while the link AB has 1 (checked). That is exactly why Sam's single number is weaker than Lee's condition.
8. **Launch timing (p. 2).** "Whole group, about 5 minutes after free handling" does not fit inside the schedule's "5 handling/launch" slot. Make the slot 7–8 minutes, or say the 5 minutes includes handling.
9. **Materials (p. 2).**
   - "Place strips on the tightest map you will use" does not name the map. Name it, for example the six-place grid on 2–3 p. 4 or 4–5 p. 7.
   - The kit's sleeve and dry-erase pen have no stated use. Either say what goes in the sleeve, such as a working map for erasable rings, or drop them.
10. **Optional base print (p. 2).** Base p. 4 is the same map as 4–5 P4. Offer only base p. 3 (the trap map), or say that p. 4 is for K–1 and 2–3 only.
11. **Headings and band names (pp. 4, 6, 8).**
    - Add the missing commas: "Grades 4–5: routes, groups and general claims", "Upper continuations, explanations and sources".
    - The cross-references say "young/middle/upper" while the pages and headings say K–1, 2–3 and 4–5. Use the grade labels throughout.
12. **Sources (p. 8).** Say which problems use which source:
    - lowest-dearest routes (2–3 P2–3, 4–5 P1, P3, P6): Hu and the widest-path article;
    - Sam (4–5 P5): Sedgewick and Wayne, Web Exercise 1;
    - repricing (2–3 P7, 4–5 P8): Exercise 1;
    - squares (4–5 P9–P11): the Steiner tree article.

    AGENTS asks for problem references when material is adapted.
13. **Checker robustness (`draft/src/check_guide.py`).** It pins each student PDF by SHA-256. If the pages are rebuilt with identical content but different bytes, such as a new creation date, `build.sh` fails. Pin the extracted text or the problem-to-page map instead.

## Checklist results

1. **Correctness:** every printed answer is verified (`check_answers.out`).
   - **K–1:**
     - P1: 4, three networks.
     - P2: AB/C/D/EF, then ABC/DEF, then one group; A and F join at 3.
     - P3: 9, two networks; no network avoids a 3 or 4.
     - P4 and P5: 8 and 6, 8 and 9, 8 and 8 (three ways using S, six overall).
     - P6: 12 (four ways) and 8 (unique).
     - P7: 6 (unique); 10 with no squares and 9 with one.
     - P8: the family (1, 3, z ≥ 4), (2, 2, z ≥ 4), (2, 3, 3), and the 1, 1, 6 trap.
   - **Grades 2–3:**
     - P1: 9, six networks.
     - P2 and P3: lowest dearest links and first common rings 2, 2, 4, 4; group counts 6, 3, 2, 2, 1.
     - P4: networks 3, 6, 9; trips ABCD (3), then AD (5 and 6).
     - P5: 8 / 18 / 16, with trips {ABCDEF, ACDEF}, {ACDF} and {ABCDEF, ACDEF}.
     - P6: c = a + b + 1.
     - P7: no, no.
     - P8: 8 and 6; 8 and 9.
   - **Grades 4–5:**
     - P4: 6, three networks, prices 1, 1, 2, 2.
     - P5: costs 7, 7, 7 and 9.
     - P8: squared prices give 14 and ABCDEF; all four distance rows are right.
     - P9: three, six and two ways at 8.
     - P10: no with a cap of 8 or 9; a cap of 10 works through 10 → 8 → 6.
     - P11: 6, S and T, bound 2.
     - P12: Lee is right.
2. **Agreement with the pages:** all problem and page numbers, the 7/6/10 page counts, place sizes and spacing, the 165 counters and 54 strips, and the 33 and 32 overflow totals match. Nothing contradicts the base guide: its exchange certificate, kit and W53-guide-v4 reference agree.
3. **Overview:** it passes on theorems, assumptions, limits and proofs. The band map's discoveries are thin (Should-fix 3).
4. **Launch:** it is brief, concrete, on a non-task instance, and gives away no theorem or answer. It lacks a spoken goal (Should-fix 4).
5. **Usability and age fit:**
   - The preparation estimate and the status are honest.
   - Hints are mostly questions.
   - The materials match the pages, and no page needs cutting.
   - The routes, the new-child context and the reading loads need work (Should-fix 1, 2 and 5).
6. **Brevity:** see Should-fix 6.

## The writer's flagged issues

I agree with all five items in `writer-report.md`:

1. invented prices need an explicit "positive, whole" convention (K–1 P8, 2–3 P6);
2. the strict and tied readings of 2–3 P6;
3. the kit cannot pay every trial purchase, including the 33 and 32 totals and the price-36 road;
4. square maps break the all-place theorems, so 2–3 P7 is scoped before P8;
5. spare record maps are not answer counts.

The guide handles each one well.

I disagree with one claim in the report: that each band has "a manageable one-hour route". The routes are manageable, but for K–1 and 4–5 they leave out kernels the outline treats as core (Should-fix 1). The report does not mention returning against new children or the length, both of which I raise.

## What works and should be kept

- **The overview's proofs.** The cut proof of the lowest-dearest route fact and its converse fit in four sentences. So does the derivation of n − c_k links priced at most k, which gives the shared price list and cost = Σ(c_k − 1). The note that the threshold-3 pause still counts is worth keeping.
- **The no-squares scoping.** The guide keeps it consistently: 2–3 P7 against P8, the 4–5 P6 "Limit" line, and the overview's closing caveat.
- **Complete keys.** Each "find all" list has a short completeness argument:
  - the "three tree forms" for the star maps;
  - 3 × 2 for the six networks;
  - the shortest-distance labels, which prove that no cheapest trip is missing.
- **K–1 Problem 8.** The complete answer family, the 1, 1, 6 trap and the remark "say 'at least one dot per road'".
- **2–3 Problem 6.** The guide accepts the tied reading without rejecting the child.
- **4–5 Problem 10.** The answer is exact: no with a cap of 8 or 9, with the explicit 10 → 8 → 6 chain, and the note that a swap is one atomic exchange.
- **4–5 Problem 11.** The leaf-count argument, with the warning that one map shows the bound can be reached but does not prove it.
- **Honest operations.** The counter-overflow arithmetic, the price-36 warning, "Opening means marking every eligible link; no payment total is requested", the status paragraph, and sources that separate what the outline cited from what was consulted.
