# Week 95 (Count the unseen): math check

Scope:
- `lowell-math-circle-year-2/week-95/week-95-grades-2-3.pdf`, 4 pages, Problems 1–7.
- `week-95-grades-4-5.pdf`, 4 pages, Problems 1–8.
- `week-95-facilitator.pdf`, 5 pages.

Sources read: `source/week-95/student/build.py`, `guide/facilitator.tex`, `build.py`, `README.md`, `QA.md`, `SOURCES.md` and `revision-response.md`. I did not run or import the package's `check_math.py` or `student/verify.py`. All 13 pages were rendered at 80 dpi, and the diagrams again at 200 dpi, into `render/` in this run folder. Checked October 23, 2026.

**Result: every answer, bound, probability and proof in the packets and guide is correct. I found 3 problems, all minor. None of them is a wrong answer:**
1. Visible permanent letters can give away the hidden total in the live game.
2. One shared rule has a reading that would forbid arranging any overlap.
3. One demo label reads like "second catch".

## How it was checked

- **`check_math.py`** (output `check_math.py.out`, 58 PASS, 0 failures). Standard library only, exact fractions.
  - **Set facts.** Enumerates every first/second catch pair for N ≤ 10 and checks the overview's overlap range max(0, M+n−N) ≤ R ≤ min(M, n). Also checks that a record fits exactly the bags N ≥ M+n−R.
  - **Mean overlap.** Enumerates second catches to confirm E(R) = Mn/N for N ≤ 12. For N = 24 it uses a subset-counting DP, checked against brute force for N ≤ 12. This gives exact means for every split in Problems 6–7. It also checks the design theorem for all N ≤ 24 and budgets s ≤ N.
  - **Every task.** Exact overlap distributions for N = 8 and N = 16 with catches of 4. The guide's per-round choices and the 1.76 likelihood ratio. Every construction the guide gives. The ten-object counterexample. The 18-object fit and the smallest bag of 12 for the five-round record. 22.5 and 21. The bias example N = 6, M = 4, n = 3, whose mean guess is 34/5. Lost marks can only lower the detected overlap (enumerated for N = 6).
  - **Letter shortcut.** The probability that permanent letters reveal N in the live game (Problem 1 below).
- **`check_diagrams.py`** (output `check_diagrams.py.out`, 0 failures) reads the delivered PDFs with PyMuPDF. For each card it finds the printed letter and whether a dot lies inside it, then checks:
  - The six-object demo on p. 1 of both bands, panel by panel (start, bag after catch 1, catch 1 before and after marking, mixed bag, bag after catch 2, catch 2, overlap ring), against the panel captions.
  - Dots on exactly B, D, E in Grades 2–3 Problem 2, and none in Problem 3.
  - The Grades 4–5 Problem 3 example (A*, B, C → A*, B, C | D*, E, F) and its circle diagrams: 6 of 6 marked in the bag, 2 of 6 in the second catch, circles round.
  - Every printed table value, the headers, the footers and consecutive problem numbers.

Both scripts find the repository by walking up from their own location, so they run from `plans/review/checks/week-95/` as well as from this run folder.

## Problems found

### 1. Live game: permanent letters can reveal the hidden total (both bands, p. 1, Problem 1; guide p. 2)

- **Text.** Grades 2–3 Problem 1: "The keeper hides 8 to 20 objects. Catch 4, mark and return them, then catch 4 again. Play three rounds with the same objects. Choose a guess before the keeper reveals the total." Grades 4–5 is the same with 12 to 24 objects and catches of 6.
- **Guide p. 2.** "Each kit has 24 identical flat counters … Permanent small identities A–X in a corner help the identity puzzles and later retention test."
- **Problem.** Neither page nor guide says which letters the keeper hides. The p. 1 demo models the natural choice, a run A, B, C, …. With a run, the highest letter caught is a lower bound on N. It equals N as soon as the last object turns up in any of the six catches. Children can then read the total straight off the letters, and the overlap-based guess that Problem 1 is about becomes unnecessary.
- **Evidence (`check_math.py`).** P(last letter caught in 3 rounds) is exact: the probability that an object misses one catch, by enumeration, raised to the sixth power.

  | Band | N = 8 | N = 12 | N = 16 | N = 20 | N = 24 |
  |---|---|---|---|---|---|
  | Grades 2–3 (catches of 4) | 0.984 | 0.912 | 0.822 | 0.738 | — |
  | Grades 4–5 (catches of 6) | — | 0.984 | 0.940 | 0.882 | 0.822 |

- **Shuffled letters still give a bound.** The number of distinct letters seen across the three rounds is a valid lower bound on N. Its expectation is 7.88 at N = 8 and 11.81 at N = 12 (Grades 4–5). The guide's Problem 4 note, "Do not add union sizes across rounds: the table does not tell us which identities were shared between rounds", does not hold in the live game, where the letters do show this.
- **Smallest fix.** Add one sentence to the guide's launch or keeper role: "For Problem 1, shuffle all 24 objects and count off the hidden ones, so the letters are not a run A, B, C, …." Optionally add: "Distinct letters seen across rounds are also a correct lower bound; welcome that reasoning if it appears." Using unlettered counters for Problem 1 would remove both effects.

### 2. "Use distinct objects in each catch" can be read as forbidding any overlap (both bands, p. 1, shared rules; guide p. 2)

- **Text.** "To show a record is possible, you may arrange catches: use distinct objects in each catch, from the same bag." The guide repeats it: "A legal arranged catch still uses distinct objects from the same population."
- **Problem.** The intended meaning is that no object appears twice within one catch. "Distinct objects in each catch" also reads as "each catch uses different objects from the other". Under that reading no arranged round can have an overlap, and several tasks become impossible to arrange:
  - Grades 2–3 Problem 5: overlap 3.
  - Grades 2–3 Problem 6: every possibility for bags 6 and 8, whose overlaps are {3, 4} and {1, 2, 3, 4}. Zero is impossible there (`check_math.py`).
  - Grades 4–5 Problem 2: record A, overlap 2.
  - Grades 4–5 Problem 3: the ten-object counterexample.

  The demo shows a shared object, so many readers will get it right. But this sentence is the only rule for arranged catches.
- **Smallest fix.** "To show a record is possible, you may arrange catches by hand from the same bag; no object appears twice in one catch." Make the matching change on guide p. 2.

### 3. Demo label "catch 2" sits on the arrow into the first catch (both bands, p. 1, shared demo diagram)

- **Diagram.** The arrow from "Start: six unmarked objects" down to "First catch: A, C" is labelled "catch 2". Source: `node[midway,right,font=\scriptsize]{catch 2}` in `DEMO`.
- **Problem.** It means "catch two objects", the same idiom as "Catch 4" in Problem 1. But in a diagram whose other panel is headed "Second catch: C, D, F", it reads as "catch #2" attached to the first catch. Nothing else in the diagram is wrong: `check_diagrams.py` confirms every panel's cards, dots, bag captions and the overlap ring.
- **Smallest fix.** Relabel it "catch 2 objects", or drop the label, since "First catch: A, C" already says it.

## Checked and correct

- **Grades 2–3 (pp. 1–4).** Correct apart from items 1–3.
  - P1: every overlap 0–4 is possible for all N in 8–20.
  - P2: shared B, D, E. The smallest bag is 7. Of the listed totals, 7, 8, 12 and 20 are possible; 6 is not.
  - P3: the smallest bag is 10, and there is no largest.
  - P4: each overlap is possible for both 8 and 16. The likelihood choices per round are 8, 16, 8, 16, 8, 16.
  - P5: both bags give overlaps 0 and 3, using the guide's construction.
  - P6: overlaps are {3, 4} for a bag of 6, {1, 2, 3, 4} for 8, and {0, …, 4} for 12.
  - P7: overlaps are {2, 3, 4} for a bag of 7. "4 versus 0" works for bags 6, 7 and 8.
- **Grades 4–5 (pp. 1–4).** Correct apart from items 1–3.
  - P1: every overlap 0–6 is possible for N in 12–24.
  - P2: smallest bags are 10 and 12, with no largest.
  - P3: the example guess is 6, the record-A guess is 18, and a ten-object bag fits.
  - P4: the guesses 36, 18, 12, 18 and "none" are right. A bag of 18 fits every record. The minimum bag is 12.
  - P5: bags of 12 and 18 both give overlap 0.
  - P6: 6 + 6 is the unique best split, with mean 3/2. The supplied formula is exact for every split.
  - P7: budget 13 gives 6 + 7 or 7 + 6 (7/4). Budget 20 gives 10 + 10 (25/6). For every budget 2–24 the best split is ⌊s/2⌋ and ⌈s/2⌉.
- **Guide.** Correct apart from the two sentences cited in items 1 and 2.
  - The overview's facts and hypotheses: the overlap range, the lower bound with no upper bound, E(R) = Mn/N without independence, the ratio estimate (undefined at 0, biased), and the balancing theorem with its limits.
  - Every answer, hint and construction on pp. 3–5, including 1/70, 1.76, 22.5, 21, the products 11–36, the combinatorial proof of the mean, the mark-loss monotonicity, the false union bound at N = M = n = 6, and the bias example 34/5.

  One remark for adults, which is not an error. In Grades 2–3 Problem 4, the guide says the six rounds "weakly favor 16" (correct, ratio 1.7595). A child who instead matches the mean overlap 1.5 gets 16/1.5 ≈ 10.7, which is nearer 8, and the per-round votes tie 3–3. The guide already says to accept any reasoned choice.
