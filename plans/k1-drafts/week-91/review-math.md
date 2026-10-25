# Math review: Week 91 K–1 draft (F91-K-v1), draft/k-1.pdf, 7 pages

Reviewer: independent math critic. Verification script: `review-math-verify.py` (in this run folder). It does not use the author's `check.py`. It models the cards as "show the next exit, follow, then flip", never resets them within a trial, and enumerates every start: 2 for the one switch, 8 for the four-exit tree, run up to 48 counters. Coin results come from listing all 2^7 toss orders. I confirmed that `draft/src/k-1.tex` is exactly what `build.py` produces and that `draft/k-1.pdf` is identical to `draft/src/k-1.pdf`. I rendered all seven pages and checked them against the kit (`week-91-materials.pdf` pp. 1–2): X is the left exit and Y the right; A, B, C, D run left to right with A and B under the left card.

## Verdict

**K–1 is mathematically correct.** Every intended answer is right. Each "cross out" problem has at least one possible and one impossible picture, and every possible picture really can be made. Every diagram matches its text: dot counts, counter totals, exit letters, numbered exits, tree shape and the one-move sequence. No trial needs more than the kit's 16 counters (the largest needs 10). I found one moderate problem (Problem 3) and two minor ones (Problems 8 and 5). None makes a page wrong. Because this packet has no facilitator guide, the parent volunteer will be checking answers without a key, and that makes the first two matter more.

## Located problems

### 1. Moderate: K–1, page 3, Problem 3, second question

Text: "Can 7 tosses put 5 counters on X and 2 on Y?" There are five recording rows of 7 boxes.

The intended answer is yes. The coin can make any order, which is the contrast with Problem 2, where X5 Y2 from 7 counters is impossible for the switch. But children answer this by tossing, and the target is rare:

- P(exactly 5 X and 2 Y in one 7-toss trial) = 21/128 ≈ 16.4%. On average a pair needs about 6.1 trials to see it once.
- P(seen at least once in the 5 printed rows) = 1 − (107/128)^5 ≈ **59%**. So about **41%** of pairs who fill every row never see it. Those pairs have evidence for "no", which is the switch's answer, and the coin–switch contrast is lost.

(The first question, "two counters in a row on the same exit", is safe: 126 of the 128 toss orders contain a repeat.)

Smallest fix: ask about the split in either direction. This still contrasts with Problem 2, because the switch can never make 5 and 2 either way from 7.

> Can 7 tosses put 5 counters on one exit and 2 on the other?

This gives P = 42/128 ≈ 32.8% per trial and ≈ **86%** within the 5 rows. If the organizer wants to keep "X and Y" exactly, the alternative is 10 or more rows (≈ 83% at 10). Either way, the adult notes should say the answer is yes even when the tosses never show it: the coin can make any order, for example X X X X X Y Y.

### 2. Minor: K–1, page 6, Problem 8

Text: "Draw every way to set the three cards so that the first counter lands on C." There are three blank compact trees.

The answer is **2 ways**: top card ↘, right card ↙, and the left card either way (RLL and RRL in top/left/right order; my enumeration of all 8 starts finds no others). The page has three trees. For a "draw every way" task, that suggests to a K–1 child, and to an adult without an answer key, that a third way exists.

There is also a second reading that changes the count. The first counter never touches the left card. A child who leaves that card blank, or says "it doesn't matter", has found the real structure and will report **1** way. The text's "set the three cards" makes 2 the literal answer, so an adult needs to know that both readings are correct thinking.

Smallest fix: keep the wording. Make sure the adult notes give "two ways: the left card can point either way because the first counter never reaches it". Then either keep the third tree as spare space on purpose, or label it as extra space so it does not suggest a third answer. Do not drop to two trees, because that gives away the count.

### 3. Minor (optional): K–1, page 4, Problem 5

Text: "Set the three cards on the board with exits A, B, C and D, draw your starting arrows, and send four counters. Can two of the four counters land on the same exit?" There are six blank trees.

The answer is no, and it holds from all 8 starts. The first four counters give ACBD, ADBC, BCAD, BDAC, CADB, DACB, CBDA, DBCA. Every window of four consecutive counters, up to counter 48, also hits all four exits. The page records only 6 starts. A quick pair who want to settle "can" by trying every start runs out of trees two short, and the page does not suggest there are 8 starts. The answer from six trials is right but not exhaustive.

Smallest fix: none needed on the page if the adult notes say there are 8 starts and the answer is no for all of them. If space allows, 8 trees (four rows of two compact trees) would let a pair check every start.

## Checked and correct (answer key, for the reviser and the adult)

- **Shared rules and one-move picture (p. 1):** the start panel shows ↙ with the counter waiting beside the card. In the move panel the counter is in the left exit and the card is still ↙. In the flip panel the card is ↘. This matches follow-then-flip. The exits are blank, so no task's letters are used.
- **P1:** the starts give XYXYXYXYXY or YXYXYXYXYX, so two in a row is impossible from either start.
- **P2:** X2 Y1 (3 counters): ↙ only. X3 Y3 (6): either arrow. X2 Y3 (5): ↘ only. **X5 Y2 (7): impossible.** X5 Y4 (9): ↙ only. **X3 Y5 (8): impossible.** The answers are the same if the counter label is ignored and counters are sent until the piles match.
- **P3:** two in a row: yes. 5 X and 2 Y: yes (see item 1).
- **P4 (card):** counters 5 and 7 land where counter 1 did; counters 8 and 4 land on the other exit, from either start. **P4 (coin):** for each k, exactly half of all toss orders put counter k on counter 1's exit, so it cannot be predicted.
- **P5:** never (see item 3).
- **P6 (6 counters):** A2 B1 C2 D1: LLL or RLL. **A2 B2 C1 D1: impossible.** A1 B2 C1 D2: LRR or RRR. **A1 B1 C2 D2: impossible.** The only reachable piles are (1,2,1,2), (1,2,2,1), (2,1,1,2) and (2,1,2,1).
- **P7:** B first to two (at counter 5): LRL (BCAD…) or LRR (BDAC…). B last to two (at counter 8): RLL (CADB…) or RLR (DACB…). Both are possible.
- **P8:** RLL and RRL (see item 2).
- **P9:** A then D: LLR only. **D then C: impossible.** C then B: RRL only. **B then A: impossible.** (Two exits under the same lower card can never come first and second.)
- **Diagrams:** the dot counts in P2 and P6 match the printed totals and the text (every P6 picture sums to 6). The numbered exits in P9 are A1/D2, D1/C2, C1/B2 and B1/A2, as intended. Circles for drawing arrows measure 18 mm (21 mm in P2), and the PDF is not scaled.
