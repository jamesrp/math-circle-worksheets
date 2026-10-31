# Review: Week 81 K–1 adult guide, draft v1 (W81-K-FAC-v1)

I reviewed `draft/k1-guide.pdf` (4 pages) and its source `draft/src/k1-guide.tex`. I read it against the final K–1 pages `plans/k1-drafts/week-81/k-1.pdf` (7 pages), the outline, both page reviews, the drafts README entry, the week's adult guide (W81-FAC-v2, 4 pages) with its shared packet W81-S-v3, and the Week 98 model guide. I rendered and read every page of the guide and of the K–1 pages, and the shared packet's board page; I read the rest of the shared packet and the week's guide as extracted text. I did not edit the guide or the pages.

**How I checked.** I wrote two scripts in `review-guide-check/` before opening the writer's checker.

- `parse_pages.py` reads the final student PDF directly. It finds every bucket outline and every filled dot, and lists the start pictures page by page (`parse_pages.out`). (Three curved arrows on p. 1 also pass its outline filter. They hold no dots.)
- `solve.py` is a separate solver for the one-each rule. It recomputes every value the guide prints: winners, unique winning moves, Problem 5's moves and replies, the splits for 4, 5 and 6 counters, every possible game length, board maxima, the launch start (3, 2) and the bucket-3 tree. It asserts each one. It also checks the overview's general claims:
  - the second player wins exactly when every bucket is even, for one bucket up to 12, two up to 8 each and three up to 5 each;
  - the winning move from any other start is unique and is the one described;
  - the length range from a + b + c to a + 2b + 4c;
  - a + 2b + 4c falls by 1 to 4 on every move.

  All assertions pass (`solve.out`).
- I measured the shared board (three 56 × 139 mm buckets with 5 mm gaps, 86 × 40 mm Supply and Removed boxes) and the sixteen 39 × 27.5 mm cards from the PDF vectors.
- Afterwards I ran a copy of the writer's `check_guide.py` in `/tmp`. It also passes.
- pdflatex is not installed here, so I could not compile. In the rendered PDF nothing overflows or overlaps.

**Verdict.** The guide is correct, keyed to the final pages, and consistent with the week's guide. I found no must-fix items.

- Every printed answer agrees with my solver.
- Every problem number, page number and start order matches the final PDF, not the reviewed draft. Examples: Problem 1's order is 2, 5, 3, 6, 4, 7, 11, 10. The three-bucket winning-move task is now Problem 10. Problem 11's maxima are 6, 7 and 12. Problem 12 starts from (2, 2, 2).
- The overview is theorem-first, with assumptions and limits.

The should-fix items are about what children are meant to discover and say, and how the table runs when one adult has two pairs.

## Must-fix

None found.

## Should-fix

### 1. The overview does not say concretely what K–1 children discover, or which problems carry each idea (p. 1, "Destination and evidence")

- **What the guide says:** "K–1 reaches the week's paired-position strategy through play, then explores growth and finite game length." The only child-level explanation is "A child can show the idea with pairs and one leftover." AGENTS asks for what children are meant to discover and a brief map. WRITER.md asks for the explanation a five- or six-year-old could give with the objects. The Week 98 model has a "What children discover" paragraph that does this.
- **What is missing:** a one-line problem map, and the child's own words for the copy argument.
- **Fix:** Replace the first sentence of "Destination and evidence" with something like this:
  - "Problems 1–5: with one bucket, an even number means the second player wins. With two buckets, the second player wins exactly when both buckets make pairs, by doing the same move to the same bucket. The first player wins by making pairs first.
  - Problems 6–7 use that rule to find every such start, or to show there is none.
  - Problems 8, 9 and 11 (cooperative): never refilling gives the shortest game. Each bucket-2 counter can give one extra turn, and each bucket-3 counter three. The board grows by at most one per bucket-3 take.
  - Problem 10 makes pairs with three buckets. Problem 12 asks why every game ends."
- **Add the child's version of the copy argument:** "Whatever you do, I do the same thing to the same bucket, so every bucket is in twos again. There is always a move left for me, so you run out first."
- **Change the opening claim** "Exactly the all-paired starts favor the second player" to "are exactly the starts where the second player can always win". "Favor" reads as a tendency, not a certainty.

### 2. The table demonstration shows one move but not what children are trying to find or record (p. 2, "At the table, two minutes")

- **What the guide does:** The demo on (3, 2) is a good non-task instance, and both endings are shown. It stops after one move.
- **What it leaves out:** Nobody, here or in the week's common launch, shows how a game ends or what "Circle who wins" means. Problem 1 needs both straight away. AGENTS asks the launch to show "what they are trying to find or record".
- **Fix:** Add one sentence after the endings. "Cover buckets 2 and 3 and put one counter in bucket 1 (not a printed start). The first player takes it, nothing is left, and the second player cannot move, so the first player wins; point to where '1st' and '2nd' are circled in Problem 1." This takes about 30 seconds and reveals no Problem 1 answer.
- **Also say where the refill comes from.** The demo text never says that the refill comes from Supply. The student picture shows Supply going from 3 to 2.

### 3. The bucket-3 rule gets no concrete demonstration (p. 4, "Switch the goal explicitly")

- **What the guide says:** "revisit student p. 1's tree from (1, 0, 2)". The first-hour route saves Problems 8–12 for a later visit. That visit therefore needs its own short launch, and the four-way tree is the most abstract picture in the packet.
- **Fix:** "At the start of the visit for Problems 8–12, uncover bucket 3, set up (1, 0, 2) on the board and let children make each of the four endings with counters from Supply, resetting between them; then say that in Problems 8, 9 and 11 the partners work together." (1, 0, 2) is not a task start, and none of its four results is an answer.

### 4. What the rest of the table does while one child plays the adult (p. 2, "A first hour"; p. 3, Problem 4)

- **What the guide says:** It wisely says to rotate challengers "rather than playing every child through every combination while the others wait". The route reads "15 minutes selected Problem 4 games or Problem 5".
- **What it leaves out:** It never says what the other three children do while the only adult plays one challenger. The writer's report flags the same risk.
- **Fix:** "While the adult plays one child (whose partner checks the moves), the other pair works on Problem 5 or replays chosen Problem 2 starts against each other. Swap after two games. A good subset is (4, 2) with the child first and then with the adult first; save (3, 4) for a child who has explained the copy."

### 5. "Where it goes" would leave a stale sentence in the week's guide (p. 4)

- **What the guide says:** Replace "only the paragraph beginning 'K–1, adult-led, after the launch'" on p. 2 of W81-FAC-v2.
- **The problem:** That guide's overview on p. 1 also says "K–1 has an adult-led route on page 2." It would then be wrong. A four-page section also cannot sit in that paragraph's place in the middle of "Materials and common launch".
- **Fix:** "After approval, replace the p. 2 paragraph beginning 'K–1, adult-led, after the launch' with a one-line pointer to this section, and change the p. 1 overview sentence 'K–1 has an adult-led route on page 2' to name the K–1 pages (W81-K-v1) and this section."

### 6. Two solutions lack the reasoning a child might give (p. 2, Problem 2; p. 4, Problem 12)

- **Problem 2** gives no child reasoning beyond "Paired buckets support the copying argument from the overview".
  - **Fix:** For (2, 2), use the copy sentence from item 1. For (1, 1): "take from bucket 2 and put one in bucket 1; now there are two in one bucket, like Problem 1's 2, and the other player goes first."
- **Problem 12's** explanation is in adult terms ("only finitely many bucket-2 takes are possible").
  - **Fix:** Add a child version. "Bucket 3 never gets new counters, so after two takes it is empty for good. Then bucket 2 never gets new ones, so it empties too. Then bucket 1 only goes down. Every bucket runs out, one after another." Keep the adult sentence and the 14-move check after it.

## Minor

1. **The shortest-game step does not follow (p. 1).** "Thus the shortest game has a + b + c moves" does not follow from a + 2b + 4c falling by at least one; that gives only the longest. **Fix:** "Every move removes exactly one counter and every starting counter must go, so the shortest game has a + b + c moves (never refill). Because a + 2b + 4c falls by at least one, and by exactly one when every refill is made, the longest has a + 2b + 4c." Problem 8 already gives the right reason.
2. **Wrong word in Problem 4 (p. 3).** "whose only winning start is (3, 4) → (2, 4)" should say "only winning first move".
3. **Notation comes late (p. 3).** "Key notation" comes after (a, b) has been used on pp. 1–2. It also says "Each arrow below", but only one arrow follows. **Fix:** Move the (a, b) sentence to the top of the solutions on p. 2 and drop the arrow sentence.
4. **Repetition.**
   - Emptying Removed is said four times: the overview's last sentence, the launch, Problem 8 ("Reset Removed before each trial") and Problem 11 ("Count Removed, not counters still in play"). The student rule already says it too. Keep the launch sentence and cut the others.
   - "Join the common launch" repeats the rule limits ("No same-bucket or higher-numbered refill is legal. Supply is not a fourth bucket; Removed is not a refill supply."). One clause is enough.
   - "Paired buckets support the copying argument from the overview" (Problem 2) adds nothing once item 6 is fixed.
5. **Demo picture (p. 2).**
   - The six buckets are equally spaced, so they read as one row. Only the titles group them.
   - **Fix:** Widen the gaps between panels, and add an arrow from "Set up" and an "or" between the two results, as on student p. 1. Show Supply, or write "Supply: 3 / 3 / 2" under the Removed counts.
6. **Recording demands (p. 2, "Prerequisites and staffing").**
   - Problems 8, 9 and 11 ask children to write numerals up to 12 in boxes.
   - Problems 5 and 6 ask for up to seven small two-bucket drawings with up to six dots.
   - The guide mentions dictation but not numeral writing. **Fix:** Add "Children write numbers up to 12 in the boxes of Problems 8, 9 and 11, or the adult writes what they say."
   - "Pairing is learnable here" is cryptic. Use "Children need not know 'even'; pairing counters is how they see it."
7. **Packets (p. 1, "Per pair").** "Print all seven pages of k-1.pdf" per pair leaves open whose page a pair writes on in Problems 3 and 5, which say "you" and "your partner". **Fix:** Say "one packet per child, the pair plays on one board", or name who records on a shared packet.
8. **Counter fit (p. 1).**
   - "Test fit first" should name the binding case. Problem 1's 11 counters must lie flat in one 56 × 139 mm bucket.
   - Counters of 20 mm fit two across and six down, which is 12 places. Counters of 25 mm give only 10.
   - **Fix:** "test that 11 counters fit in one bucket."

## Where I agree or disagree with the writer's report

- **Optional refills, Supply and Removed kept apart, resets.** I agree. The guide handles all three well.
- **Problem 4 can monopolise the one adult.** I agree. The route still doesn't say what the others do (should-fix 4).
- **Problem 6's five slots.** I agree, and the guide's "spare recording space" note is right.
- **Small answer buckets and close labels, "notably Problem 9".** I partly disagree. At print size the three Problem 9 starts are well separated with clear 1–2–3 labels. Drawing comfort in the 16 × 22 mm answer buckets is a fair untested concern.
- **Problem 12 allows 14 moves.** I agree, and the guide correctly asks for an argument, not a count.
- **No mathematical error on the final pages.** I agree; my solver confirms every answer.

## What works (keep it)

- **Correct, final-keyed answers.** Every answer agrees with an independent solver. The tables are generated from the writer's recomputation, and the start orders follow the final PDF exactly. The guide does not carry over the reviewed draft's numbering or its (3, 3, 3) start.
- **A real theorem-first overview.**
  - It explains why the copy is legal: the chosen even bucket had at least two counters.
  - It shows the winning move to pairs is unique under the one-each rule.
  - It gives a followable termination and length argument, a + 2b + 4c, and states that the bounds depend on the cap and do not carry over to the upper table's uncapped game.
  - It separates experiment, conjecture and explanation, and does not repeat the older bands' destination.
- **Consistent with the week.** The launch, kit (shared board p. 2, about 30 counters plus a reserve, covered bucket 3) and one-adult staffing match W81-FAC-v2. The cap-one longest-game formula agrees with its p. 4 formula (7 from (1, 1, 1)). The guide restates "the bucket on its left" as "bucket 1", which kindergartners can follow.
- **The launch instance.** (3, 2) is not a task start, matches student p. 1, and neither shown move is the winning move (2, 2).
- **The adult play card for Problem 4.** It covers every later position. It is honest that a paired position on the adult's turn has no guaranteed win, and it says "do not manufacture a win".
- **Completeness arguments.** Problem 5 (one choice from bucket 1, two from bucket 2), Problem 6 (whole pairs shared between two buckets) and Problem 7 (one counter always left over) each explain why the list is complete. The note that each Problem 5 row restarts from (2, 2) heads off a likely slip.
- **Explanations of the length questions.** Problem 9 shows the board grows by at most one per bucket-3 take, and Problem 11 counts the extra turns each counter can earn. Both are explanations, not just numbers.
- **Hints and pacing.** Every hint is a question. The first hour adds up to 60 minutes, defers Problems 6–12 by readiness, says "Finishing every page is not the goal", and asks the adult to record who chose the moves.
- **Honest status.** It says the activity is unpiloted, lists what is physically unrehearsed, and marks the prep time as an estimate.
