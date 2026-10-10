# Week 66 (Lamplighter streets): math check

Scope:
- `lowell-math-circle-year-2/week-66/week-66-students.pdf`: one shared Grades 3–5 packet, 4 pages, Problems 1–5. This packet is treated as the band.
- `week-66-facilitator.pdf`: 2 pages.

Sources read: `source/week-66/student/students.tex`, `guide/facilitator.tex`, `MATHEMATICS.md` and the READMEs. I did not run or import the author's checkers (`checks/`, `student/check_math.py`, `guide/check_math.py`). My scripts and their outputs are in [checks/week-66/](checks/week-66/). Checked October 10, 2026.

**Result: every target, answer, word, lower bound and general claim in the packet and guide is correct, and every diagram encodes the state its problem needs. I found 1 problem, minor: the wording of Problem 5 (p. 4) also allows a trivial reading that does not need the dead end.**

## How it was checked

- **`check_math.py`** (output `check_math.py.out`, 58 checks, 0 failures):
  - It runs breadth-first search on the lamplighter graph (a state is walker position plus the set of lit lamps; moves are L, R, F) with no coordinate bound, out to distance 14. It also runs the search on the printed −4…4 street, which has all 4,608 = 9 · 2⁹ states.
  - The guide's formula |S| + min(−ℓ + (r − ℓ) + |p − r|, r + (r − ℓ) + |p − ℓ|) equals the search distance on every state in both searches. The number of states within distance 12 is 4,167, as `MATHEMATICS.md` says.
  - Every move changes the distance by exactly ±1, because the graph is bipartite. So for Problem 5, "harder" and "easier" are the only possibilities.
  - It checks all 10 printed targets on both streets and the three Problem 4 neighbours of the Problem 3 target.
  - It reads the delivered guide PDF and replays all 10 printed shortest words. It checks each word's end state, its length against the search distance, and the walks + flips splits in both tables.
  - It checks every lower-bound sentence in the guide (3, 4, 6, 8 and 4 walks).
  - It lists every dead end up to distance 9 (states where no move increases distance). The P3 target (0, {−1, 0, 1}) at distance 7 is the smallest and is unique at that distance. The next are (0, {−2, 0, 1}) and (0, {−1, 0, 2}) at distance 9.
- **`check_diagrams.py`** (output `check_diagrams.py.out`, 62 checks, 0 failures) reads the vector drawings of the delivered student PDF. For every street it recovers the position labels, the lit lamps and the walker marker. It checks:
  - that circles are round and equally spaced, and that the walker sits exactly over a lamp;
  - that the large lamps are 13.0 mm across, as the guide states.

## Grades 3–5 shared packet (pp. 1–4)

- **Launch demo (p. 1):** the start street has walker at −2 and all lamps off. After R the walker is at −1. After RF lamp −1 is on and the walker is at −1. The drawings are correct.
- **P1 (p. 1):** each diagram decodes to the target the guide lists.
  - A is (1, {1}), distance 2.
  - B is (1, {−1, 1}), distance 5.
  - C is (0, {0, 2}), distance 6.
- **P2 (p. 2):** all three diagrams have lamps −2, 0, 2. The walker is at −2, 0 and 2, giving distances 9, 11 and 9. The text "same lamps on, but the walker ends in different places" is accurate.
- **P3 (p. 3):** (0, {−1, 0, 1}) has distance 7. A valid lower-bound argument is available to children: 3 flips plus 4 walks.
- **P4 (p. 4):** L, R and F from the P3 target give (−1, {−1, 0, 1}), (1, {−1, 0, 1}) and (0, {−1, 1}), each at distance 6.
  - Children need only upper bounds here (6 < 7), together with P3's proof that 7 is the minimum.
  - Every optimal route for every target stays inside the printed street, so the −4…4 edge never matters.
- **P5 (p. 4):** the intended answer, No, is correct: the P3 target is a dead end. See Problem 1 for the wording.

### 1. Page 4, Problem 5 (minor): the question also has a trivial reading that bypasses the dead end

- **Quoted text:** "Can you always make a target harder to reach from all-off at 0 by making one more legal move? Use your results to settle this question."
- **Intended reading:** the guide's key says: "Problem 3 supplies a counterexample covering *every* legal next move … One unsuccessful attempt would not settle an 'always' question; these are the complete alternatives at that state." That is the dead-end question: does every target have at least one move that makes it harder?
- **Other reading:** the sentence also reads naturally as "Does one more move always make a target harder?" That version is settled by any single move that undoes progress, and it needs neither Problem 3 nor Problem 4.
  - From P1 target A (distance 2), F gives distance 1 (`check_math.py.out`).
  - Under this reading, one unsuccessful attempt *does* settle the question, which contradicts the guide's sentence.
  - A child who answers "No, flipping the lamp back off makes it easier" is correct under this reading but has missed the theorem the packet builds toward.
- **Smallest fix:** "Does every target have at least one next move (L, R or F) that makes it harder to reach from all-off at 0? Use your results to settle this question." The guide key can stay as it is.

## Adult guide (pp. 1–2): checks out completely

- **Overview:** the decomposition (number of target lamps plus the shortest walk from 0 that visits them and ends at p) and its two-sided argument are correct. So is the dead-end statement: distance 7, with all three neighbours at distance 6. The scope statements are also true: optimal routes stay inside −4…4, and distance is always measured from all-off at 0.
- **Keys:** every key is correct:
  - the P1 and P4 tables (states, words, walks + flips, totals);
  - P2's 9/11/9 and its words, with the six- and eight-walk bounds;
  - P3's 7, FLFRRFL and its 3 + 4 bound;
  - the remark that appending a letter to the 7-move word gives an 8-letter route for a distance-6 target;
  - P5's "No".
- **General rule:** the formula is correct for all finite S, including S = ∅ and targets entirely on one side of 0. The two-order argument (visit ℓ first or r first) proves it.
- **Launch description:** it matches the printed demo.
