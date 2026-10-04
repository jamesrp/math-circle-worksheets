# Independent adversarial review

## Verdict

The packet is mathematically sound and visually clean. It needs modest editorial revision, principally in K–1, rather than a rewrite. I found no false construction, unsatisfiable construction presented as solvable, incorrect card diagram, clipping, overlap, or missing page. The main concern is whether the youngest children are asked to produce enough mathematical evidence, and whether their short random game obscures the distinction the preceding exact comparisons establish.

I read the brief, rendered the actual deliverable PDFs independently at 85 dpi, and visually inspected all 22 pages: 8 K–1, 7 grades 2–3, and 7 grades 4–5. I checked exact wording in the generated sources and independently enumerated the relevant finite cases. The review concerns these PDFs, not the older render files also present in the draft folder. I did not change the draft.

## Revisions worth making

### 1. K–1, pages 7–8: the impossible tasks need an evidence goal

Both questions end at “Can …?” Neither asks the child to explain a negative answer. In Problem 7, “no” can be obtained from a few unsuccessful arrangements without engaging with the fact that nine decisive pairs cannot split equally. In Problem 8, the same problem is more pronounced: the task is impossible, and failed searching alone is not an explanation. These are precisely the tasks for which the organizer says explanation is the point.

**Recommended revision:** Ask for an arrangement or an explanation of why none works, still in at most two short sentences per problem. An oral explanation or demonstration with cards is entirely suitable for K–1; do not demand written prose. Do not put the parity argument, sorting argument, or a suggested search procedure on the student page.

This matters more than merely increasing the amount of work. The current packet already has enough substantial later problems; these two need a clearer mathematical stopping condition.

### 2. K–1, page 4: connect the six-round game to the exact comparison

Problem 4 asks children to select a deck with more winning card pairs and then play six rounds for each opposing choice. This is mathematically legal, but the only stated goal after selecting the decks is to carry out the trials. It does not ask children to distinguish the outcome of six games from the exact nine-pair comparison. The page is consequently vulnerable to “our better deck did not win, so our count was wrong.”

This is a substantial practical risk, not an unlikely edge case. For any one of the stated favorable matchups, the selected deck wins a majority of six rounds only about **45.3%** of the time; about **30.1%** of six-round sets finish tied. The more favorable deck fails to finish ahead more often than it finishes ahead.

**Recommended revision:** Give the game a question about whether the deck that wins more card pairs must win more of these rounds, or otherwise make disagreement between the two outcomes something the child is asked to examine. Preserve the distinction between counting every possible pair and playing a few rounds. Do not state the answer, increase the sample until it supposedly “proves” the advantage, or add a worked example. Keep the K–1 prompt short.

The grades 2–3 packet addresses this distinction directly and correctly in its Problem 2. There is no corresponding flaw there.

### 3. K–1, pages 1–3: make the recording goal unambiguous, without supplying the method

“Find every pair … and mark the winner” is understandable to an adult, but the only printed objects are six individual cards. Each of these cards belongs to three different comparisons. Marking a printed card as a winner does not by itself record which pair was compared or establish that all nine pairs were covered. An early reader could reasonably circle the largest card or mark individual winning cards and believe the requested output is complete.

There is abundant blank workspace, and leaving its organization to the child is consistent with the brief. I am **not** recommending a prefilled 3-by-3 matrix, numbered comparison list, or nine supplied substeps. The required output can be made explicit in the wording: a record of each different two-card pair with its winner. A child can then choose pictures, numerals, counters, or an arrangement of the real objects.

This is a clarity concern, not a claim that every page needs a recording grid. The adult can currently resolve it, but the stated standard asks the page to pose the task clearly without needing another instruction.

### 4. Both older bands, page 1: replace unexplained “independently” with a concrete action

“Draw independently from each deck” is exact probability language but is not introduced, and the grades 2–3 group may not know what it asks them to do. K–1's “Mix the bags separately” is closer to the requested register and states an executable action.

**Recommended revision:** Express the separate mixing and one draw from each deck concretely, retaining equal likelihood of physical cards and replacement between rounds. Do not weaken the model to equal likelihood of different printed numbers. This is a low-cost wording change; the present mathematics is correct.

## Pacing and usability judgments

- **K–1 Problems 1–3 are thin as separate numbered problems.** Once a child has organized one nine-pair comparison, the next two use exactly the same procedure. A quick child may spend substantially less than five minutes on either of the later pages. They are worthwhile mathematical cases and establish the actual cycle; the objection is to the organizer's per-problem five-minute standard, not to their inclusion. Consider grouping the three related cases as one substantial numbered task, or making the outcome of the three comparisons part of the task. Do not pad them with repetitive instructions or compulsory explanations after every comparison.
- **The complete K–1 packet is not too short.** Problems 5–8 supply genuine extension work. Exhaustive swaps, the impossibility of an equal split, and two-card cycles can readily occupy the remaining time. Do not replace these with easier arithmetic exercises.
- **Grades 2–3 Problem 3 is harder than its wording initially looks.** There are exactly two qualifying arrangements besides the original, so “find two” means finding every remaining solution. This is valid and a reasonable sustained search after the comparison work. Do not casually increase the requested number.
- **Grades 4–5 Problem 2 can occupy much of a session.** There are 90 labeled distributions of the six loose cards before applying the win conditions, and the task asks for a complete list and an explanation of completeness. This is legitimate substantial mathematics, not a defect requiring an algorithmic hint. The adult should be able to stop there without treating the subsequent pages as a checklist.
- **Later impossibility tasks are genuine extensions.** The fourth/fifth-grade packet develops the two-card comparison before asking for a general impossibility explanation. That is a strong sequence. Grades 2–3 and K–1 receive concrete six-card versions instead of an unsupported general theorem, which is appropriate.
- **Blank space is generally appropriate.** It gives children room to organize their own work and is preferable to supplying the mathematical plan. Grades 4–5 page 4 has less writing space than the other pages, but its six-card and four-card diagrams are distinct and there is still room below for numerical results. No layout repair is necessary.

## Mathematical checks

These are review evidence, not material to add to the student pages.

### Shared starting example

With A = (2,4,9), B = (1,6,8), C = (3,5,7), the directed win counts A over B, B over C, and C over A are **(5,5,5) out of 9**. Reverse counts are four and all deck sums are 15. The three-way cycle, equal-total observation, and absence of cross-deck ties are correct.

### K–1

- **Problems 1–4:** The printed deck contents and dot counts match the example.
- **Problem 5:** For replacements 3, 5, 7, 9, A's win counts against B are respectively **3, 3, 4, 5**. Only 9 succeeds. There are no ties.
- **Problem 6:** Exactly five swaps work. Listed as original A card / original B card, they are **2/1, 4/1, 9/1, 9/6, 9/8**. B then wins respectively **5, 6, 9, 6, 5** pairs. The wording is naturally read as each single swap starting from the pictured decks; the adult should not treat it as a cumulative sequence of swaps.
- **Problem 7:** Impossible: all nine pairs are decisive, and an odd number cannot split into two equal whole-number win counts.
- **Problem 8:** Impossible under the stated fair physical-card model. The six different cards ensure no ties.

### Grades 2–3

- **Problem 2:** Correct. Any finite winner-only result sequence has positive probability under either order of the two original decks. No finite streak establishes certainty about which hidden bag has the majority advantage. The replacement rule matters and is present.
- **Problem 3:** Exactly three solutions with 9 in A, 8 in B, and 7 in C, ignoring order inside a deck:
  1. A = (1,5,9), B = (3,4,8), C = (2,6,7), directed counts (5,5,5).
  2. A = (2,3,9), B = (1,6,8), C = (4,5,7), directed counts (5,5,6).
  3. The original example, directed counts (5,5,5).
  Thus exactly two are different from Problem 1, as requested.
- **Problem 4:** Exactly **2 and 4** are valid replacements. A repeated 2 is a second physical card, not a new distinct printed value. The picture and global likelihood rule support the correct interpretation.
- **Problem 5:** Duplicating every physical card produces **20 versus 16 out of 36** in each favorable directed comparison, with the same winning decks. It does not produce merely nine physical outcomes.
- **Problem 6:** Solvable, for example A = (2,4,12), B = (1,6,9), C = (3,5,7). Their totals are 18, 16, 15 and their directed win counts are (5,5,5).
- **Problem 7:** Impossible for the stated six-card set.

### Grades 4–5

- **Problem 2:** The complete list is the same three fixed-maximum solutions given above. The task is feasible and the requested completeness claim is meaningful.
- **Problem 3:** Solvable under the restriction against sharing a printed value between decks. One example is A = (1,4,4), B = (3,3,3), C = (2,2,5), with directed wins **(6,6,5) out of 9**. The restriction says numbers from 1 to 6, not that all six numbers must occur, so this example is valid.
- **Problem 4:** The six-card chances equal those from Problem 1. For the four-card decks, directed counts are **10/16, 7/16, 10/16**; reverse counts are 6/16, 9/16, 6/16. Thus all three pairwise probabilities change, and the B–C advantage reverses. The diagrams correctly show exactly four cards per lower deck and six per upper deck.
- **Problem 5:** A/B splits 2:2, C/D is 3:1, E/F is 4:0, and G/H is 1:3. For sorted two-card decks with no cross-deck equality, one deck wins a strict majority exactly when both its smaller and its larger card exceed the corresponding cards of the other deck. This remains valid if the two cards within a deck have equal values.
- **Problem 6:** One-card and two-card cycles are impossible; three cards per equally sized deck suffice. The global fair-card, independent-draw, no-cross-deck-tie rules correctly delimit the claim. The two-coordinate strict comparison is transitive, so a two-card cycle cannot occur.
- **Problem 7:** Impossible. I enumerated all 1,680 labeled partitions of 1 through 9 into three unordered three-card decks: none meets all three six-win requirements. There are 15 oriented strict-majority cycles overall. There is also a short elementary obstruction: label the deck containing 9 as A without changing the cyclic order. For C to beat A in six pairs, every C card must exceed both of A's other cards. For A to beat B in six pairs, at least two B cards must lie below A's larger non-9 card. Those two B cards then lose to every C card, so B cannot beat C six times. This makes the task defensible as an elementary impossibility problem, rather than one supported only by a computer search.

## Visual and organizer-standard audit

- All three PDFs are US Letter with the expected single-sided page layout.
- All 22 pages have the required one-line week/topic/level header, correctly numbered “Problem N:” label, one-line Bellingham footer, packet identifier, and page number.
- The diagrams use readable numbers and adequately sized blank card faces. Every K–1 dot group agrees with its numeral.
- No content is clipped, collided, or pushed into the footer. I found no overfull/underfull/error warnings in the three final compile logs.
- There are no extraneous activity titles, warm-up/bonus labels, mascots, exclamation marks, praise, answer leaks, prescribed solution steps, or lettered microtasks.
- The K–1 problem statements meet the literal one-or-two-sentence limit, although Problems 4 and 8 carry several clauses and deserve special attention when revising.
- The stronger middle- and upper-band tasks genuinely ask for construction, complete case coverage, comparison, or impossibility rather than routine arithmetic practice.

## Suggested revision priority

1. Add the missing justification goal to K–1's impossible tasks.
2. Make K–1's trial game explicitly engage with the distinction between possible-pair counts and observed wins.
3. Clarify what is to be recorded for each K–1 card pair, without organizing the search for the child.
4. Replace unexplained probability jargon in the older-band global rule.
5. Address the thinness of separate K–1 Problems 1–3 only if it can be done without padding or removing the real extension work.

Keep the successful mathematical content, restrained visual style, plentiful free workspace, and child-owned methods. No mathematical reconstruction or wholesale re-layout is justified by this review.
