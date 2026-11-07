# Review: Week 66 K–1 adult guide (Lamplighter streets), draft v1

I reviewed `draft/k1-guide.pdf` (4 pages) and its TeX source against the final K–1 pages, `plans/k1-drafts/week-66/k-1.pdf` (8 pages). I rendered and read every page of both. I also read the outline, the two page reviews, the draft's README entry, the week's existing guide (`week-66-facilitator.pdf`, GGT66-FAC-v2) and the Week 98 model guide. I did not edit the guide or the pages.

**How I checked.** I wrote `review-guide-check/check.py` before opening the writer's checker. It reads the student PDF's vector drawings directly: for every framed picture it finds the seven lamps, which are filled, the walker's lamp and the home mark, and it counts the cubes in each Problem 8 tower. It then recomputes every answer with breadth-first search on the printed seven-lamp street and on a 13-lamp street, enumerates shortest words by brute force, and computes exact-length reachability. The guide's printed claims are transcribed into the script and compared. Output: `review-guide-check/check-output.txt`. Results:

- Every picture the guide describes matches the final pages (all 29 framed pictures and all 12 Problem 8 towers).
- Every fewest count, shortest word, steps-plus-flips split, walking-order count (Problems 3 and 4), "every way" list (Problem 5: 2 and 4 ways, complete), the two tied Problem 4 words, the Problem 6/7 neighbour arrows and the Problem 8 tower answers are correct.
- The overview's general claims hold on the street: all 896 seven-lamp minima equal the longer street's; the exact counts are exactly d, d + 2, …; lit lamps plus steps from home has the evenness of every route.
- Sizes match the PDF: 20 mm work lamps on 24.0 mm centres, 17 mm pawn spots, 12 record squares (9 mm) per picture, 5 rows of 8 squares per Problem 5 picture.
- I later ran a copy of the writer's checker in `/tmp`; it also passes.

**Verdict.** This is a correct, well-keyed guide that agrees with the final pages and with the week's existing guide. I found no must-fix items. The should-fix items concern what the table practises first, three facts the overview leaves to the solutions, and one hint that is a procedure.

## Must-fix

None found.

## Should-fix

### 1. The table practice teaches the Problem 5 record, not the record used in the first hour (p. 2, "Join the whole-group launch" and its figure)

- **What the guide does.** After the whole-group launch, the K–1 table practises "a two-move record": flip, then step left, recorded as • and ←. The worked figure is labelled "After •" and "After ←".
- **The problem.** That dot-and-arrow record is used only in Problem 5, which the guide's own first route saves for a later visit. Problems 1–4 use a different record: one cube per move, then "Color one square under the picture for each cube in your shortest tower" (page 1 rules). The guide only describes that record in prose ("Record a new best in its squares… erase surplus shading"). It is never demonstrated. AGENTS asks the launch to show "what they are trying to find or record", and asks that a new representation be introduced when it answers a question children have met ("Sequence representations around their purpose"). As written, children meet a second notation in minute 8 and do not use it for the rest of the hour. Page 5 also prints its own dot-and-arrow example, and the guide's Problem 5 paragraph already replays it. So the dot/arrow demonstration happens twice.
- **Fix.** Keep the same non-task moves, but make the practice about the cube tower and the squares:

  > "Back at the K–1 table, practise one try that is not a task: all lamps off, pawn in the spot above the rightmost lamp. Flip there and add a cube; step one place left and add a cube. The lit lamp stays put when the pawn steps. Colour two squares on a scrap strip for the two cubes, then take the tower apart and reset: all lamps off, pawn home. Problems 1–4 record a best try the same way, in the squares under each picture."

  Relabel the figure "Input: no cubes / After a flip: 1 cube / After a step left: 2 cubes", with two shaded squares under the output. Then leave the dot-and-arrow record to the Problem 5 paragraph, which already uses the page's example. Also say "in the spot above the rightmost lamp", not "on the rightmost lamp". The same page says the pawn never covers a counter.

### 2. The overview leaves three facts the pages depend on to the solutions (p. 1, "Mathematical overview")

The overview states the main theorem correctly: required flips plus shortest visiting walk, with the lower bound and the construction. It gives the 9 → 8, 8, 8 dead end and the evenness invariant, and it separates experiment, conjecture and explanation well. But an adult who reads only the overview does not learn what children are meant to discover in Problems 2–7, which are most of the packet and all of the first hour after Problem 1:

- **On a line, what the shortest visiting walk is.** Problems 2–4 are entirely about this. Add:

  > "On a line, the walk must reach the farthest lit lamp on each side of home, one end first and then the other, and then go to the walker's place. The cheaper of the two orders is the shortest walk. If the walker finishes at an end lamp, visit the other end first (Problem 3). Where the walker finishes can make the two orders tie or swap (Problems 2 and 4)."

  Then name these discoveries in "Scope and destination": "In the first hour children find that where the walker finishes, and which end it visits first, change the count."

- **Where the different shortest ways come from (Problem 5).** Add:

  > "A shortest build flips each lit lamp exactly once along a shortest walk. A lit lamp the walk stands on twice can be flipped either time, which is why Problem 5's pictures have 2 and 4 shortest ways."

- **One move changes the fewest count by exactly one.** The overview proves the parity fact but stops before its consequence for Problems 6 and 7. Add:

  > "Since a picture one move away can differ by at most one, and every move changes evenness, each one-move change makes a picture exactly one easier or one harder. Every right-hand count in Problems 6 and 7 is one more or one less than the left-hand count."

  This also gives the adult a quick error check: a tie with the left picture, or a difference of two, means a count is wrong.

Each addition is one or two sentences. The space can come from cutting the repetition listed under Minor.

### 3. One Problem 5 hint is a procedure (p. 3, Problem 5 "Hints")

"Sort the recorded rows by when home is lit, then compare the remaining choices" tells the child how to organise the search, and so reveals the structure of the answer (two independent choices). The criteria ask for hints that are questions. **Fix:** replace it with:

> "When does each of your ways light the home lamp: before the walker leaves, or after it comes back?"

Keep the completeness argument in the solution paragraphs, where it already is. The second hint, "Could you leave this lamp off now and light it when you return?", is close to giving the method. Mark it as the later of the two hints.

## Minor

1. **"Say 'all lamps off,' not 'dark side up'" (p. 1, Per pair).** This reads as if "dark side up" were a possible wording for the reset, yet dark side up means lit. Write: "Dark side up means on, matching the filled circles. To reset, say 'all lamps off' (every counter light side up), and avoid 'dark street'."
2. **Problem 5's printed example is the start of one answer (p. 3).** "It is not either target below" is true, but the example (flip at home, step right) is the first two moves of FRFL, one of the top picture's two ways. Add: "Its two moves begin one of the top picture's ways. That is fine, since the task is to find every way, but replay it to the side and do not continue it." This is a page matter; the guide can only warn.
3. **Legality checks with two pairs (p. 1, Prerequisites and staffing).** "The adult checks legality and resets": one adult cannot watch every flip at two streets at once. Say that the flipper's point-before-flip is the check, and that the adult spot-checks and watches resets.
4. **Erasing shaded squares (p. 2).** "Erase surplus shading if the best gets shorter" is fiddly for kindergartners, and real erasing is untested. Suggest a dot or a single stroke in each square rather than full colouring, or let the adult erase.
5. **Hint wording for K–1.** Problem 4's "Can both visits fit in your route without walking farther than you must?" is adult language. Try "Which lit lamp will you go to first? What if you went to the other one first?" Problem 7's "Are we including the left picture?" would help the adult more with its reason attached: "If only the three right-hand pictures are compared, they tie at 8."
6. **"Avoids retracing the whole street" (p. 3, Problem 3).** The wrong order re-crosses the stretch from home to the finishing end twice, not the whole street (for example, TR 8 = 4 + 2 × 2). Write "avoids walking out to the finishing end and back again".
7. **Launch figure glyphs (p. 2).** The figure uses ▼ for the pawn and the word "home". The pages use a pawn and a house mark. Use the pages' glyphs, so that the adult's sketch and the children's street match.
8. **File name after approval (p. 1, Print and prepare; p. 4, Where it goes).** "`k-1.pdf` from the Week 66 K–1 draft" will be stale once the section is pasted in. Name the approved file, `lowell-math-circle-year-2/week-66/week-66-k-1.pdf`. "Where it goes" could also add one line to the base guide's "What children discover" paragraph pointing to the K–1 section, so the base overview's band map covers K–1.
9. **Repetition and jargon.** These can go, freeing room for should-fix 2:
   - "This guide is for the adult." (p. 1).
   - Problem 7's restatement that the walker is free to move. The overview already says it.
   - The third statement of "record the count and reuse the cubes": it appears on p. 2, in Problem 6 and in Problem 7. Keep Problem 7's 33-cube sentence.
   - Replace "workstreet", "attains that lower bound" and "completeness support" with plain words for a parent volunteer.
10. **Typography (p. 3).** The Problem 5 word lists lack spaces after commas ("FRFL,RFLF").

## Checklist results

1. **Correctness.** Every answer verified by my own code (`check-output.txt`):
   - Problem 1: 1, 2, 3, 4.
   - Problem 2: 4, 4, 5, 6.
   - Problem 3: 4, 6, 7, 9, with wrong-order walks 8, 11 and 13.
   - Problem 4: 7, 8, 7, 6, with left/right-first walks 5/7, 6/6, 7/5, 8/4. The home finish has exactly LLFRRRFL and RFLLLFRR.
   - Problem 5: 4 with FRFL and RFLF; 7 with FRFRFLL, FRRFLFL, RFRFLLF and RRFLFLF. Both lists are complete.
   - Problem 6: 5 → 4, 6, 4; the R picture is the unique most.
   - Problem 7: 9 → 8, 8, 8; a dead end, and the left picture is the unique most.
   - Problem 8: towers 1 and 3; 2 and 4; 4 and 6.
   - Every printed word replays to its picture on the seven-lamp street. No false general claim.
2. **Agreement with the pages and the week.** Problem and page numbers (Problem N on page N), picture positions (TL/TR/BL/BR; left plus top, middle and bottom right), arrow labels, lamp and spot sizes, square counts and Problem 8 tower heights all match the final PDF, not the earlier draft. The kit (nine counters no wider than 17 mm, a pawn, about 24 cubes per pair) matches the outline and the base guide. Nothing contradicts GGT66-FAC-v2: the partner roles, all-off-at-home distance, the dead-end meaning and the reference to its "Mathematical destination" all agree. The replaced paragraph ("K–1 tables.", "Materials and preparation", page 1) is named correctly.
3. **Overview.** It passes: theorem first, with assumptions (line, finitely many lamps, the seven-lamp street changes nothing), a followable lower-bound and construction argument, the parity invariant, and a clear experiment, conjecture and explanation split. It is incomplete for Problems 2–7 (should-fix 2).
4. **Launch.** Brief (5 + 3 minutes), concrete, on a non-task instance. My script confirms that its finishing picture is not a printed target. No theorem or answer is given away. It practises the wrong record (should-fix 1).
5. **Usability and age fit.** Realistic prep (5–10 extra minutes, no cutting). The status is honest. The one-hour route adds to about 51–55 minutes plus transitions, and Problems 5–8 are deferred. Readiness signals are given ("if only the adult can compare the records, return to improving one route"). Hints are mostly questions (see should-fix 3 and minor 5). Reading and recording demands are stated honestly.
6. **Brevity.** At 2,371 words over 4 pages it is denser than padded. It has no encouragement and little narration. A few repeats and jargon terms are listed in minor 9.

## On the writer's flagged issues

I agree with every page risk the writer report names and the guide handles:

- Problem 6/7 arrows show differences, not routes, and every picture is rebuilt from all off at home.
- The left picture counts in "most".
- The 33-cube total for standing towers.
- Twelve squares are capacity, not a hint, and the fifth Problem 5 row does not promise five ways.
- Problem 5 is readiness-dependent.
- The counters, pawn and cubes are not printed.
- Everything is unpiloted.

I disagree on one point. The report presents the table demonstration's dot and left-arrow record as meeting the worked-visual rule, but it is the record for a problem the first visit skips (should-fix 1). I add one point the report does not mention: the page-5 example is the opening of one Problem 5 answer (minor 2).

## What works and should be kept

- **The answer tables.** Lamps, walker, one shortest word, steps plus flips, and fewest, in adult-only H/1L/2R shorthand with a key. They are quick to use at the table and all correct.
- **The Problem 3 and 4 order comparisons.** Both walking counts for each picture are printed, so the adult can confirm a child's slower order without solving it.
- **The Problem 5 completeness arguments.** "The walk must be RRLL; flip 2R at the turn; two independent choices." A five-year-old can check this on the street.
- **The Problem 6/7 operating notes.** The arrows are differences, not routes; the L arrow points right but means a left step; solve afresh from all off; appending a move gives a 10-move attempt, not a minimum.
- **The evenness caution.** "'I can add two' proves possibility, not the impossibility of the other counts", with an object version of the invariant (lit counters plus one cube per step from home) kept optional.
- **The honest status line, the readiness signals, and the explicit "Finishing every page is not the goal".**
