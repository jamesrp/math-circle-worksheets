# Mathematical review: Pancake flips draft (pancake-flips-v1)

## How this was checked

- I wrote my own breadth-first search over all stacks, without using the author's `check.py`. It covers plain stacks of up to 7 pancakes and stacks with dark sides of up to 6. A stack is written from the top. For dark sides, a negative number means the dark side faces up, and the goal is 1 2 ... n with every dark side down. Each flip reverses the top k pancakes and, for dark sides, turns each of them over. Each flip undoes itself, so the distance from the sorted stack is the minimum number of flips. I also listed every shortest solution and counted breaks, with the plate numbered n + 1.
- I rebuilt every drawn stack from the TikZ coordinates in `draft/src/*.tex`. That is 51 stacks: 14 in K–1, 22 in grades 2–3 and 15 in grades 4–5. For each one I read the order of the pancakes from top to bottom, the label on each pancake, the number code under the stack, whether width grows with size, which face carries the dark band, and where the spatula sits. **Every diagram matches its intended stack.** Widths grow with size in every stack. The number codes match the drawings. Every dark band is on the face it should be on. In the launch demo the spatula is under 3 pancakes and then under 2: 3 1 2 → flip 3 → 2 1 3 → flip 2 → 1 2 3. In the break example the three red marks sit at 1|5, 5|3 and 4|plate. I also looked at the burnt-pancake stacks at 200 dpi, and the band on each pancake can be told apart from its neighbour's.
- The outline's facts all reproduce:
  - The most flips any stack needs are 1, 3, 4, 5, 7, 8 for 2 to 7 pancakes.
  - With three pancakes, only 1 3 2 needs three flips.
  - With four pancakes, exactly three stacks need four flips: 4 2 3 1, 2 4 1 3 and 3 1 4 2.
  - With six pancakes, exactly two stacks need seven flips: 4 6 2 5 1 3 and 5 3 6 1 4 2.
  - With dark sides, the most flips needed are 1, 4, 6, 8, 10 for 1 to 5 pancakes.
  - Breaks never exceed the minimum number of flips, checked for every stack of up to 7.
  - The two-flips-per-pancake method never needs more than 2n − 3 flips. Its worst case equals 2n − 3 exactly for n = 2 to 7.
  - With dark sides, the simple top-then-turn-then-down method never needs more than 3n − 2 flips, which is 16 for six.

The scripts are in `/tmp/claude-0/-home-claude/d1d23a10-bfbf-5b59-a13a-5f6afdbf2b0f/scratchpad/verify/` (`pancake.py`, `parse.py`).

---

## Problems found

### 1. Grades 4–5, page 5, Problem 5: Problem 3 already answers it (fix this)

> "Problem 5: Find a stack of five pancakes that needs as many flips as you can. Explain why it cannot be sorted in fewer."

On page 3, Problem 3 has the child sort **1 3 5 2 4**, says it has five breaks, and asks the child to explain why five breaks force five flips. The search shows:

- 1 3 5 2 4 needs exactly 5 flips, and its only shortest solution is 3 5 4 3 2.
- 5 is the most flips any stack of five can need. Over all 120 stacks of five, the number needing 0, 1, 2, 3, 4, 5 flips is 1, 4, 12, 35, 48, 20.

So once a child has done Problem 3, Problem 5 is already answered in full: write "1 3 5 2 4" and copy the explanation from Problem 3. Nothing is left to find. Looking for a six-flip stack can only fail, and the child cannot prove that it must. The outline's goal, "find the worst stacks of … five by pooling", is lost.

**Smallest fix (recommended):** change only Problem 3's stack so that it no longer reaches the maximum. Replace 1 3 5 2 4 with **3 5 2 1 4**, both in the text and in the diagram. Change the sentences to "It has four breaks. Explain why a stack with four breaks can never be sorted in fewer than four flips."

- Check: 3 5 2 1 4 has four breaks (3|5, 5|2, 1|4, 4|plate). It needs exactly 4 flips, and its only shortest solution is 2 5 4 3: 3 5 2 1 4 → 5 3 2 1 4 → 4 1 2 3 5 → 3 2 1 4 5 → 1 2 3 4 5.
- It does not reveal any answer to Problem 4. Its bottom pancake is 4, not 5, so it does not contain a worst stack of four sitting on a 5. That rules out choices like 2 4 1 3 5.
- Problem 5 then keeps its wording and becomes a real search. Twelve stacks of five have five breaks, and every one of them needs exactly 5 flips, for example 2 4 1 5 3 and 5 3 1 4 2. Eight more stacks also need 5 flips although they have only four or three breaks.

**Alternative:** keep Problem 3 as it is and replace Problem 5 with "Find a stack of five pancakes with four breaks that cannot be sorted in four flips. Explain why." Seven stacks fit. In 1 5 3 2 4, for example, every first flip (2, 3, 4 or 5) still leaves four breaks, so at least 1 + 4 = 5 flips are needed.

### 2. K–1, page 3, Problem 4: six answer spaces for three answers

> "Problem 4: Find every stack of pancakes 1, 2, 3 and 4 that you can sort with one flip." It has six blank four-slot stacks.

Exactly **three** stacks of four can be sorted with one flip: 2 1 3 4, 3 2 1 4 and 4 3 2 1. The problem comes straight after Problem 2, where six blank stacks matched "all six ways". K–1 children will expect six answers here too and keep looking for stacks that do not exist.

There is also an edge case: is 1 2 3 4 an answer? Under the K–1 rule, sliding the spatula under the top pancake and flipping it is a legal move that leaves the stack sorted.

**Fix:** draw three blank stacks, or four if the organizer wants to leave room for the 1 2 3 4 question. Whoever runs the table should decide in advance whether 1 2 3 4 counts.

### 3. K–1, page 2, Problem 2: the answer depends on reading "needs" as "fewest"

> "Problem 2: Find all six ways to stack pancakes 1, 2 and 3, and sort each one. Circle the stack that needs the most flips."

The intended answer is right and unique: 1 3 2 needs 3 flips. The others need 0 (1 2 3), 1 (2 1 3, 3 2 1) and 2 (3 1 2, 2 3 1). But each "flips" box records the flips the child actually used, and this problem, unlike Problems 1, 3 and 6, does not say "as few as you can". A child who sorts 3 1 2 in four flips will correctly circle the stack with the biggest number in its box, and that is the wrong stack.

**Fix:** "...and sort each one with as few flips as you can. Circle the stack that needs the most flips."

Lower priority: the launch demo (3 1 2, 2 1 3, 1 2 3) and Problem 1 (2 1 3, 3 2 1, 2 3 1) together already show five of the six stacks, and the minimum flips for all five can be read off page 1. The only stack missing is 1 3 2, which is the answer. This may be acceptable scaffolding for K–1. Note, though, that most of "find all six" has already been done for the child.

### 4. Grades 4–5, page 3, Problem 3: "4 on the plate" is not always a break

> "A break is a place where two touching pancakes, or the bottom pancake and the plate, have numbers that are not next to each other, such as 1 on 5 or 4 on the plate."

"4 on the plate" is a break only when the plate is not 5. Problem 4 deals entirely with stacks of four, which sit on plate 5, so there 4 on the plate is **not** a break. A child who takes the example literally will miscount: 1 3 2 4 has 2 breaks, not 3.

**Fix:** "such as 1 on 5, or 4 on plate 6".

### 5. Grades 4–5, page 6, Problem 8: no way to record a stack with dark sides

> "Problem 8: Find a stack of three pancakes with dark sides that needs as many flips as you can."

The only recording rule in the packet is "Write a stack as its numbers from the top", and numbers cannot show which side is dark. The page gives no blank stacks to draw on, so a correct answer has nowhere to go. K–1 Problem 7 handles the same task with "Draw it with its dark sides" and blank stacks.

The answer itself is fine: the most flips needed is 6, and exactly two stacks need it. One is 1 2 3 with the dark side of 1 down and the dark sides of 2 and 3 up. The other is 1 2 3 with all three dark sides up. Neither appears in Problem 7, so nothing is given away.

**Fix:** add "Draw it with its dark sides." and three blank three-slot stacks, as in K–1 Problem 7.

---

## Notes, not errors

- **K–1 Problem 5, page 4.** The problem is correct: exactly three stacks qualify (4 2 3 1, 2 4 1 3, 3 1 4 2), and three spaces are given. But a K–1 child can only report failing to sort a stack in three flips, and the parent volunteer at that table is not a mathematician. Ten of the eleven stacks of four that need exactly three flips have only one three-flip solution. One of them is 1 2 4 3 from Problem 3, whose only solution is 4 2 4 and starts by flipping the whole stack. So children will often name stacks that are actually possible. The parent needs an answer list from the facilitator notes. The student page does not need to change.
- **Launch stack 3 1 2.** It is one of the stacks in K–1 Problem 2 and grades 2–3 Problem 2. The outline chose it, and since it is not the worst stack it gives nothing away.

---

## Answers verified

### K–1

| Problem | Verified answer |
|---|---|
| 1 | 2 1 3 → 1 flip; 3 2 1 → 1; 2 3 1 → 2 |
| 2 | 1 3 2 needs 3 flips, the unique maximum |
| 3 | 4 1 2 3 → 2; 2 3 4 1 → 2; 3 4 2 1 → 2; 1 2 4 3 → 3 (only solution 4 2 4) |
| 4 | Three stacks (see item 2 above) |
| 5 | Three stacks: 4 2 3 1, 2 4 1 3, 3 1 4 2 |
| 6 | Dark sides: 1 (dark up) on 2 → 1 flip; 2 and 1 both dark up → 1; 2 (dark up) on 1 (dark down) → 2; 2 on 1, both dark down → 3 |
| 7 | 1 on 2, both dark up, is the unique stack needing 4 flips. It is not among Problem 6's stacks. |

### Grades 2–3: no problems found

Every problem in this band checks out.

| Problem | Verified answer |
|---|---|
| 1 | 2 3 4 1 → 2; 3 4 1 2 → 3; 5 4 3 2 1 → 1; 5 1 2 3 4 → 2; 4 5 1 2 3 → 3; 1 2 3 5 4 → 3 |
| 2 | 1 3 2 needs 3. Its two possible first flips give 3 1 2 and 2 3 1, and neither can be sorted in one flip. |
| 3 | Exactly three stacks, as in K–1 Problem 5 |
| 4 | Open question. The simple method needs at most 9 flips for six pancakes and 17 for ten (2n − 3), or 10 and 18 without the last-two-pancakes saving. |
| 5 | 6 5 4 3 2 1 → 1; 4 5 6 1 2 3 → 3; 1 2 3 4 6 5 → 3; 2 1 3 4 6 5 → 4 |
| 6 | All seven unsorted stacks of two with dark sides; minimum flips 1, 1, 2, 2, 3, 3, 4 in page order |
| 7 | 3 2 1, all dark down → 5 flips (only solution 2 3 2 3 2). 1 2 3, all dark up → 6 flips (2 3 2 3 2 3 or 3 2 3 2 3 2); this is one of the two hardest stacks of three. |

### Grades 4–5

Problems 1, 2, 4, 6, 7 and 9 are correct. Problems 3, 5 and 8 have the issues listed above.

| Problem | Verified answer |
|---|---|
| 1 | 5 1 2 3 4 → 2; 4 5 1 2 3 → 3; 1 2 3 5 4 → 3; 3 2 1 5 4 → 3; 2 1 4 3 6 5 → 5 (3 breaks; only solution 3 5 6 5 3) |
| 2 | Open question; 2n − 3 gives 9 for six and 37 for twenty |
| 3 | The example 2 1 5 3 4 has 3 breaks and needs 3 flips. 1 3 5 2 4 has 5 breaks and needs 5 flips. The lower-bound claim is true: a flip changes only the pair at the spatula, including the pair between the bottom pancake and the plate when the whole stack is flipped. |
| 4 | Three stacks. 2 4 1 3 and 3 1 4 2 have 4 breaks, so they cannot be done in three. 4 2 3 1 has 3 breaks: only flip 4 removes a break, giving 1 3 2 4, where no flip removes a break. So the explanation is within reach. |
| 6 | No. The stack needs 7 flips; it is one of the two hardest stacks of six. If six flips had to remove six breaks, every flip would have to remove one. Following only flips that remove a break gives 14 positions in total, ending in 5 dead ends, so a child can explain this with an adult. |
| 7 | 3 (dark up) 1 2 → 2; 1 2 3 (3 dark up) → 3; 3 1 2 (all dark down) → 3; 1 2 3 with 1 and 2 dark up → 4; 3 2 1 (all dark down) → 5. None of these needs the maximum of 6. |
| 9 | Open question; the simple method needs at most 16 flips for six. |
