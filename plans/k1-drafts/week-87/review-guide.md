# Review: Week 87 K–1 adult guide, draft v1

I reviewed `draft/k1-guide.pdf` (4 pages) and its source against the final K–1 pages `plans/k1-drafts/week-87/k-1.pdf` (6 pages, 8 problems). I rendered and read every student page and every guide page. I also read the outline, the two page reviews (both describe the earlier five-page draft), the K–1 drafts README entry, the Week 87 guide W87-F-v2 (all six pages) and materials W87-M-v1, and the Week 98 model guide. I did not edit the guide or the pages.

**How I checked.** `review-guide-check/verify.py` reads the card sets from the student PDF itself and then recomputes the guide's claims. I wrote it before opening the writer's `check_guide.py`. It covers:

- every ballot, supporter, count and knockout trace the guide prints;
- all 9 swaps for Problem 5;
- all 216 ordered profiles for the overview's claims and for Problems 6–8;
- the sizes of the materials and the student-page pictures the guide quotes.

Its output is in `review-guide-check/verify.out`: 58 checks, no failures. A copy of the writer's checker, run in `/tmp` with the student PDF beside it, also passes and agrees with mine.

**Verdict.** This is a correct, well-judged guide. I found no must-fix items.

- Every printed answer and list is right, and every "find all" answer comes with a completeness argument.
- Every page number, problem number, card set, board size and material count matches the final PDFs and W87-M-v1.
- The table demonstration replays the printed D/E/F example, a non-task instance, and gives away nothing.
- The overview states real theorems with their assumptions and proofs.

The should-fix items are about:

- what the overview leaves out: a stated destination and the Problem 5 fact;
- the second visit, which has no plan;
- the adult's checking load with two pairs.

## Must-fix

None found.

## Should-fix

### 1. The overview gives no concrete destination, leaves out Problem 5's fact, and defers the build condition (p. 1)

- **The destination is vague.** "Problem 4 and the later card-building problems deepen that contrast" does not tell an adult what children should come away with from Problems 4–8.
- **The two-case fact is missing.** With three voters and three letters only two things can happen: a circle, or one letter that beats both. The overview's "iff" implies this but never says it. Yet it is what makes "Circle each one" in Problems 3–4 either one letter or all three.
- **Problem 5 has no fact in the overview at all.** Its completeness argument on p. 4 is only "checking those nine swaps gives just the three above".
- **The third heading is garbled.** "Being first is sufficient on two cards, not necessary on two" is hard to read. The exact condition for one first place is deferred to the last page.

**Fix:** keep the three theorem paragraphs, and make these changes. I verified each statement in `verify.out`.

- **Add, after the knockout paragraph:** "With three voters and three letters only two things happen. Either the pair votes go round in a circle, and each letter wins exactly when it waits. Or one letter beats both others: it then wins every knockout, so no other letter can win any."
- **Retitle and complete the third paragraph:** "What B needs on the cards. B wins every knockout when it is first on two or three cards. When B is first on exactly one card, it wins only if it is second on both other cards, once under A and once under C. It never wins when it is first on no card." Keep the existing four-places-from-three-cards reason.
- **Add a swap paragraph:** "One swap ends the circle. Swapping two letters on one circle card makes the letter that moved up the only winner (all 9 swaps checked). The reason: moving up never costs a letter a vote, and on these cards every swap that moves a letter up carries it past the letter that beat it, so a 1–2 loss becomes a 2–1 win."
  - On p. 4, Problem 5's completeness then reads: "The working swaps are exactly the ones that move C up: two on V1 and one on V2. V3 already has C first."
- **Replace "What this table reaches" with what children should discover:**
  - Problem 1: the three pair votes go round in a circle, and no letter beats both.
  - Problem 2: on these cards, whoever picks the waiting letter picks the winner.
  - Problems 3–4: on other cards one letter wins wherever it plays. Problem 4 shows this happens even though that letter is first on only one card.
  - Problem 5: one swap breaks the circle.
  - Problems 6–8: B needs two cards with B above A and two cards with B above C.
  - Keep the pointer to the base guide's line overview.

### 2. The visit that holds Problems 5–8 has no plan (p. 2, "One-hour route"; p. 4)

The guide says only "save Problems 5–8 for another visit". Several things are missing.

- **A restart and a building demonstration.** Building from blank cards and slips is the one procedure the K–1 README lists as physically untried, and Problem 5 is where it is first used. AGENTS asks for a demonstration of a new procedure on a non-task instance before its first use.
- **Timings, and which of Problems 5–8 is the core.**
- **Readiness for Problems 7–8.** Only 2 of 20 card sets work in Problem 7, and Problem 8 is an impossibility.
- **The other tables' next visit.** Their next Week 87 visit may be the line visit (W87-F-v2 p. 2: "Treat agenda and line investigations as separate visits"). Its whole-group launch serves nothing on these pages.

**Fix:** add a short "Return visit" paragraph.

- **Restart (3–5 minutes).** Children handle the cut V1–V3 cards again and replay one Problem 1 vote. This replaces the whole-group launch when the older tables are on the line visit.
- **Problem 4 first, if it was skipped (about 10 minutes).** Its "what changed on V2?" comparison with Problem 1 serves as the worked swap, and its target is A, not C.
- **Building demonstration.** On the blank V3 card, put one slip in each row to make CAB beside the cut V3, to show that a slip card votes like a printed one. Point out that a card may not have two Bs, then clear it.
- **Then:**
  - Problem 5, about 15 minutes.
  - Problem 6, about 10 minutes.
  - Problem 7 for pairs who found Problem 6 quickly, with the held hints.
  - Problem 8 as an adult-held conversation with the loops, for ready pairs.
  - Finishing is not the goal.

### 3. The adult's checking load with two pairs (p. 1, "Readiness and status")

- **The load.** "An anchored adult … checks each token against its card." The first route (Problems 1–3) is 15 votes, or 45 token placements, per pair. With two pairs that is about 90 checks, on top of reading every prompt and mat label and keeping the Problem 3 scrap record.
- **What the guide already models.** The table demonstration uses a partner check ("a partner to check the higher offered letter"), but the guide does not carry that over.
- **Fix:** "The partner checks each token as it is placed. The adult checks the count, and asks for a replay only when a result differs from the key."
  - This keeps the children running the votes.
  - "Stagger the first knockout" stays.

## Minor

1. **Knockout procedure (p. 2).** "Move the first winner and waiting tile into Final pair" skips the mat's First winner box. The page 2 visual uses that box (First winner E, then Final pair E F). Write: "The first loser goes to Out and the winner to First winner. Then move it and the waiting tile into Final pair."
2. **Which cards to use (pp. 3–4).**
   - Problem 5 says "Return to the pictured original cards". The Problem 5 pictures are only 27 × 48 mm, and the cut cards were put away in Problem 3. Write: "Take the cut V1–V3 cards out again. Build the replacement on the blank card with the same V label."
   - The Problem 2 hint "return to the unchanged picture" is also unclear, because Problem 2 uses the cut cards. Write: "check the cut cards against the page 1 picture."
3. **Problem 8 loops (p. 4).**
   - The labels "B above A" and "B above C" are words K–1 children cannot read. Label the loops with a spare A tile and a spare C tile instead.
   - "Restore each token to its card before ordinary voting" is unclear, because tokens are not kept on cards. Write: "Put the tokens back by the tally mat afterwards."
4. **Problem 6 (p. 4).** "After testing its two pair votes and explaining the agendas" asks K–1 children for more than the overview's shown explanations. Write: "after both pair votes (B against A, B against C) go to B; pointing to the cards that gave those votes is the explanation."
5. **Colour dots (p. 2).** In Problems 3–4 the voters are printed cards, so dotted tokens would match only the cut cards. If the dots are used, also dot the V labels on student pages 1, 3, 4 and 5. Say that the dots and the cover slips (the Problem 1 hint) are untried; the outline says so.
6. **Status placement (p. 1).** "Readiness and status" (reading, staffing, unpiloted) sits inside the mathematical overview. Move it to p. 2 beside the kit, as in the Week 98 model ("Status" under preparation).
7. **Compact reminder (p. 2).** The displayed input/tally/winner block retells page 1's worked picture, which the adult is pointing at anyway. Drop it, or keep only the tally column.
8. **The demonstration's waiting letter wins (p. 3, Problem 2).** In the printed D/E/F knockout the waiting letter F also wins, but only because F beats both. Add one sentence: "'Waiting wins' may come from the D/E/F example as well. Problem 3 separates a letter that waits from a letter that beats both."
9. **No K–1 observation list (p. 4).** Add: "Record which problem each pair reached; whether partners kept 'the higher of the two on offer' when a card's top letter was absent; slip fit and handling of two mats; and any vote, waiting letter or build the adult chose." Then point to W87-F-v2 p. 6 for the general list.
10. **"Where it goes" (p. 4).** Integration will also need to change these places in W87-F-v2:
    - p. 2 "Prepare three older-table pair kits" (add the two K–1 kits);
    - p. 6 "Print map", which lists only the shared, line and upper packets.

    Name both places, and the Week 87 catalog record.
11. **Packets per pair (p. 2).** "One six-page k-1.pdf" per pair does not say who circles. Add "partners take turns circling", or print one per child.
12. **Checker portability (`draft/src/check_guide.py`).** The brief asked the checker to fall back to `plans/k1-drafts/week-87`. It walks ancestor directories instead. Run from a copy without `k-1.pdf` beside `src/`, it stops with FileNotFoundError (I observed this). Add the named fallback.

## The writer's flagged issues

I agree with all four:

1. **Temporary D/E/F labels.** They are the only object the week files do not print, and two minutes is realistic.
2. **Printed cards on Problems 3–4.** Voting from the printed cards needs the cut cards put away. The guide handles this, but Problem 5's "pictured original cards" now needs the matching instruction to bring them back (minor 2).
3. **Problem 3–4 bookkeeping.** The optional adult scrap record is the right weight.
4. **Frames on pages 5–6.** They are half-size (22.5 × 40 mm) and cannot hold 21 mm slips. "Adult pencil records" is correct.

I also agree that both page reviews describe the earlier draft. I disagree only with the report's view that its separation of "sufficient" from "necessary" is clear: the heading is hard to read, and the exact condition belongs in the overview (should-fix 1).

## Checklist results

1. **Correctness:** every printed answer verified (`verify.out`).
   - D/E/F demonstration: E over D (V2, V3), then F over E, each 2–1. F beats both, so there is no circle.
   - Problem 1: A, B, C, with supporters V1/V3, V1/V2 and V2/V3.
   - Problem 2: B, C, A, then A, B, C.
   - Problem 3: C only. C beats A and B 2–1 with V1/V3, and B beats A 3–0. The traces are right.
   - Problem 4: A only. The traces are right, and Problem 4 differs from Problem 1 only by V2's A/C exchange.
   - Problem 5: exactly V1→ACB, V1→CBA and V2→CBA, with C over A 2–1, 3–0 and 2–1 and C over B 2–1.
   - Problem 6: the example BAC, BCA, ABC works; "B first on two or three cards" always works; 68 of 216 ordered sets work.
   - Problem 7: exactly {ABC, BAC, CBA} and {ABC, BCA, CBA}, 2 of 20 sets, in any order.
   - Problem 8: 0 of 20 sets work.
   - Overview: the "iff" theorem holds on all 216 profiles.
2. **Agreement with the pages and the week:**
   - Pages 1–6 and the problem placement match the PDF.
   - The pictures on Problems 3–4 are full-size 45 × 80 mm cards.
   - Materials sizes all match W87-M-v1: cards 45 × 80 mm, tiles 28 mm, tokens 18 mm, slips 21 mm, card rows 23.3 mm, mats 170 × 90 and 175 × 100 mm, wells 54 mm.
   - Nothing contradicts W87-F-v2: the shared launch, the knockout shown later, the separate line visit, and the "distinct cards" rule kept to the older packet.
3. **Overview:** passes as theorem-first with assumptions, limits and the experiment/conjecture/explanation split. It needs the destination and the facts in should-fix 1.
4. **Launch:** brief, concrete, non-task, and reveals no answer. The second visit has none (should-fix 2).
5. **Usability:**
   - Preparation estimates are realistic and labelled as estimates.
   - The first route stops at Problem 3.
   - The hints are questions.
   - The materials match the pages.
   - Staffing load: should-fix 3.
6. **Brevity:** about 2,400 words over four pages, with no encouragement or padding. The only narration is minor 7.

## What works and should be kept

- **The knockout theorem and its two-line proof** in the overview: "if it beats both, it wins whether it waits or plays first; if it loses to another letter, meeting that letter first eliminates it". Also the explicit assumptions, and "these finite facts do not establish a fairness claim or Arrow's theorem".
- **"Evidence children can give"**: one knockout is an experiment, "waiting wins" is a conjecture about the current cards, and a few failed builds do not prove impossibility.
- **The table demonstration.** It uses the printed DFE/EFD/FED instance with a partner check, and points out that V3 still votes when F is absent. The knockout demonstration comes "Before Problem 2, not before Problem 1". The temporary D/E/F labels are named as the only extra object.
- **The one-hour route.** It stops at Problem 3, offers Problem 4 to ready pairs, and says "Stop earlier if resets still require adult decisions".
- **Problem 3 handling.** Put away the cut cards, vote from the full-size pictures without copying them, and let the adult keep a scrap row per waiting letter.
- **"Let children notice the pattern; do not announce 'waiting wins' first."** Also Problem 3 framed as the counterexample, and Problem 4's "counting first choices alone would miss the result".
- **The Problem 4 / Problem 1 comparison** ("only V2 has exchanged A and C"), which prepares Problem 5 without solving it.
- **Problem 6:** "repeated cards are allowed" (unlike shared Problem 3), and "putting B first everywhere is a valid entry".
- **Problem 7:** the structural completeness argument (the B-first card plus two B-second cards, one under A and one under C), and "Do not hand over the answer after a few random failures".
- **Problem 8's token-in-loops argument**, a physical grouping proof suited to the age, with "Failed builds alone are not the explanation".
- **The page 5–6 frames** identified as adult pencil records, not slip boards.
