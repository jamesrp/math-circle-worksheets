# Week 63 research and provenance

Prepared October 4, 2026. Research/outline only, ready for fresh writer/critic/math-review/reviser stages. Established mathematics is adapted into newly authored tasks and visuals. No physical preparation, procedures or classroom trial has been performed.

## Mathematical source trail

- Alan Frieze, CMU Discrete Mathematics **D14, “Cycles of permutations” / “Derangements,” pp. 2-4**. [Primary PDF](https://www.math.cmu.edu/~af1p/Teaching/DM/D14.pdf), local `external-resources/new-themes-52-63/week62-63/cmu-frieze-D14-derangements.pdf`. Page 2 states no fixed points, the small counts and recurrence. Pages 3-4 divide by whether distinguished n belongs to a 2-cycle or a longer cycle; deleting the reciprocal pair or bypassing n gives reversible constructions. Source pp. 5-6 goes on to a normalized formula and asymptotics; asymptotic 1/e is not needed for this packet.
- Frieze **D16, “Inclusion-Exclusion,” pp. 1-2** and **“Derangements,” pp. 4-6**, with **proof of inclusion-exclusion on p. 7**. [Primary PDF](https://www.math.cmu.edu/~af1p/Teaching/DM/D16.pdf), local `cmu-frieze-D16-inclusion-exclusion.pdf`. Pages 1-2 state the finite-set alternating intersection formula. Pages 4-6 use fixed-point sets with intersection size (n-|S|)! and derive the derangement sum. Page 7 checks each outcome's contribution via indicator products.

These exact pages were visually inspected. The planned card identities, homes, visual convention examples and problem wording are new local authoring, not copies of these slides or book figures. Mathematical notation/formulas express established facts, and source attribution does not imply classroom validation of the adaptation.

## Assumptions, explanations and independent finite verification

Every card and home is distinct and labeled; every row uses each card once. The fixed home strip remains unchanged. Rows are equal exactly when their entries agree position by position; turns, reversals, renaming, and identical-picture merging are not permitted. A fixed point means a card is at its own labeled home, independent of the sequence of swaps used to obtain the row. Sampled shuffles cannot establish a complete count.

`verify.py`, independent of any worksheet builder, exhausts every permutation for n=0 through 5, every specified fixed-home intersection, the reciprocal/longer-cycle recurrence cases, and partial avoidance for n=4. It writes `small-instances.json`; run `python3 plans/new-themes-52-63/week-63/verify.py` from the root. In the row record, the ith entry is the card in home i; interpreting this as the inverse card-to-home permutation preserves fixed points and cycle type.

| n | All rows | Home-free rows | Rows by exactly r home matches, r=0 through n | Inclusion-exclusion signed terms |
|---:|---:|---:|---|---|
| 0 | 1 | 1 | 1 | 1 |
| 1 | 1 | 0 | 0,1 | 1,-1 |
| 2 | 2 | 1 | 1,0,1 | 2,-2,1 |
| 3 | 6 | 2 | 2,3,0,1 | 6,-6,3,-1 |
| 4 | 24 | 9 | 9,8,6,0,1 | 24,-24,12,-4,1 |
| 5 | 120 | 44 | 44,45,20,10,0,1 | 120,-120,60,-20,5,-1 |

The three-card home-free rows are BCA and CAB. The nine four-card rows are BADC, BCDA, BDAC, CADB, CDAB, CDBA, DABC, DCAB, DCBA. For each fixed destination of the distinguished fourth card, there are one reciprocal case and two longer-cycle cases; for the fifth, two and nine respectively. Five-card coverage can therefore be pooled into four groups of eleven, not assigned as 120-row transcription to every child.

For four cards, forbidding only r specified homes gives 18,14,11,9 rows for r=1,2,3,4. In particular, forbidding A at A and B at B gives 24-6-6+2=14, not 12 or 9. Cards C,D may remain home. This is a useful way to expose overlap without introducing the whole alternating formula at once. A specified k-home intersection has (n-k)! rows **including** possible additional fixed homes; replacing that count by !(n-k) would be wrong.

The general inclusion-exclusion explanation is per outcome: an outcome in m bad sets receives net coefficient (1-1)^m, zero for m>0 and one for m=0. The recurrence's two cases are exhaustive/disjoint and reversible. These are general explanations; the code only verifies finite instances. The empty permutation is one adult base case, not a claim that a physical blank card is a participant.

## Actual prior-packet overlap and the new direction

Current `WEEKS-11-51.md` and `BONUS-AND-RETURN-VISITS.md` were read. All current Week 19 and Week 43 base student bands and bonus pages were text-extracted and rendered; related guides were consulted. The targeted evidence, 51 rendered student pages including Weeks 14/33/36, is in `tmp/worksheet-runs/week-62-new-v1/prior-review/`; current source hashes/page ranges are recorded in the sibling audit. This is a targeted comparison, not a new full-library originality audit.

- **Week 19 base** studies subset antichains and chain decompositions; Grades 4-5 **pp. 1-6, Problems 1-8**, maximize collections and contrast maximal with maximum. **Bonus pp. 1-5** adds intersecting families, minimal monotone triggers and forbidding nested triples. These already use finite set cards and overlapping symbols. They do not count a union of bad permutation outcomes through inclusion-exclusion.
- **Week 43 K-1 pp. 1-4** and **Grades 2-3 pp. 1-4** build/order three cards and follow ticket-swap stories. **Grades 4-5 p. 3, Problem 5** forbids self-swaps in a particular two-swap procedure and obtains **BCA and CAB**. Those are also the two three-card derangements, so the concrete entry's rows are reused background, not a new output collection. The new property is “avoid each fixed home,” which is different from forbidding a self-swap in a procedure.
- **Week 43 Grades 4-5 p. 4, Problems 6-7** designs fair four/five-card shuffles. **Bonus p. 1, Problem 1** handles repeated pictures; **p. 2, Problem 2** handles cuts/reversals; **p. 3, Problem 3** handles fair insertion. This already supplies permutation counting, labels, construction stories and inverse arguments. It does not supply fixed-point intersection correction, the nine/44 derangement catalogs, or the distinguished-card derangement recurrence.
- The targeted review also covers Week 14's special coloring, Week 33's ring equivalence, and Week 36's triple constraints. Those do not replace the avoided-home investigation.

**Novelty rests on the combined avoided-place constraint, correcting overlapping bad outcome sets, and the two-case derangement recurrence**, chiefly with four/five labeled cards. Simply repeating all six three-card orders or calling the existing no-self-swap procedure a new shuffle would not qualify. General partial forbidden-place boards are a possible later direction, but their counts require fresh checks; the current recurrence assumes exactly one own-home prohibition per card.

## Pedagogy and prior-year evidence

Actual source: *Math Circle by the Bay*, **Preface printed pp. viii-x, PDF pp. 9-11**, supports manipulatives, independent attempts, explanation and readiness-dependent depth. Actual source: Rozhkovskaya, *Math Circles for Elementary School Students*, **Lesson 3 “At the lesson,” item 1**, EPUB `OEBPS/part0013.xhtml`, describes children first trying a logic task, explaining it, then seeing a table; additional questions were reserved for quicker participants. **Lesson 8 “At the lesson,” item 2**, `part0018.xhtml`, reports differing speeds for copying/coloring and reducing that work.

Our proposed adaptation: let children arrange physical cards first, then sort a supplied small outcome collection, then use its overlap to motivate a record or count. Preserve one fixed reference strip, and distribute five-card cases among pairs. Those specific design choices are inferences, not tested observations. The organizer's actual prior-year **Handouts 2, Problems 2.1-2.2** uses fixed labeled theater seats and placement clues; **Handouts 6, Problems 6.2-6.6** connects arrangements and counting through different representations; **Handouts 8, Problems 8.2-8.3** explicitly asks for mappings behind recurrences. These are relevant local format/representation precedents, not copied task statements.

## Band recommendation and workflow

**Proceed chiefly for Grades 3-5**, with a supported Grades 2-5 opening. Entry needs distinct card/home identity, all-cards-once placement, counting to six, and checking a whole row against unchanged homes. Inclusion-exclusion needs a child to recognize that one outcome can belong to two groups; adults can read and record without making the placement/sorting decisions. Four-card/recurrence work needs reversible constructions and organized case coverage; factorial notation is not a prerequisite. A K-1 home-free trial can be offered only while children retain the rule; do not create a forced independent K-1 packet.

The current session context, October 3, is eleven KK11 / 3333 / 445 children and three fixed anchored adults. `outline.md` follows TEMPLATE.md and leaves numbered task selection to the fresh writer. Generated prompts are unchanged. Root's `../STAGE-ROUTING.md` requests one combined `students.pdf` and honest page headers; full enumeration merits the independent CRITIC-MATH stage. REPUBLISHING.md was read; generated prompts/borrowed style exemplars do not belong in the final portable ZIP. No old/global files were changed.
