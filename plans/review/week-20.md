# Week 20: Averaging and the maximum principle

**Verdict: keep.** There is no must. Every answer checks, and the tasks reach a real theorem in every band. The five should items can wait for the next reviser.

Reviewed October 10, 2026 by Claude. Packets: week-20-k-1.pdf (GA20-K-v3, 7 pp.), week-20-grades-2-3.pdf (GA20-23-v2, 6 pp.), week-20-grades-4-5.pdf (GA20-45-v3, 7 pp.). Adult guide: week-20-facilitator.pdf (25 pp. plus a route note, p. 26). Companions noticed but not reviewed: week-20-bonus.pdf (W20-BON-v1, 5 pp.) and its guide. Status: unpiloted (guide pp. 1–2, source README), revised October 4.

## The mathematics

Squares hold fixed values, and each circle must equal the average of its neighbours, all at once: the discrete Dirichlet problem. Children reach the maximum principle (2–3 P3, 4–5 P2–P3) and its equality case, in which a tie spreads until it reaches a square (2–3 P4, 4–5 P4). They also reach uniqueness when every place reaches a square (2–3 P5, 4–5 P1 and P5) and constant values on boards with one square or none (K–1 P6–P7, 2–3 P6, 4–5 P6 with 5 × 5 = 25 fillings). The last idea is that whole numbers can fail (4–5 P7). A mathematician would enjoy it: chasing the biggest value to a square is a real proof a nine-year-old can give.

## Ratings

| | Rating | Evidence |
|---|---|---|
| Mathematics | strong | One theorem whose hypotheses are tested from both sides: boards with squares against boards without, whole numbers against fractions. |
| Problems | strong | Two to four contrasting boards per problem. In 4–5 the bound gets two boards (P2) before its proof (P3), and uniqueness gets three (P1) before its proof (P5). 2–3 P3 and P4 pair a no-peak question with one where a tie is allowed. The K–1 order is off the guide's route (fix 2). |
| Student pages | adequate | Headers and footers are right, with one or two sentences per problem and no method in the tasks. Boards are sized for cubes (K–1 nodes 3 cm) or for writing. Recording slots and fraction cards give answers away (fixes 1, 3), and captions repeat the rules (fix 4). |
| Concreteness | adequate | Guide p. 3: a 4-minute shared launch with squares of 0 and 6 cubes. K–1 sharing mats make the division physical. Older bands work in numbers a partner can recheck; only the adult stops a child fixing one circle at a time. The cube procedure is unrehearsed. |
| Correctness | strong | math.md checks every answer, count and diagram in all bands and the guide. Three page references are wrong (fix 5). |
| Adult guide | strong | Theorem-first overview with hypotheses and limits (p. 1), adult proofs (p. 4), launch, timing and routes (pp. 3, 26). Each problem has answers, a completeness argument, held hints and an extension. |
| Age fit, K–1 | adequate | The adult reads one or two sentences per problem, and up to 10 cubes are shared into two or three piles. Copying stacks without touching the reference stacks takes several steps, and P2's linked circles ask more still (a prediction); the guide defers P2. |
| Age fit, grades 2–3 | strong | Sums up to about 20 are divided by 2 or 3, with cubes on hand. The P2 and P5 trees are guess-and-check, and explanations wait for P3, P5 and P6. |
| Age fit, grades 4–5 | strong | P3 and P5 read formally ("finitely many shapes and lines"), but the organizer sits at this table. Signed differences (P5) and thirds (P7) are optional. |

## Keep

- Squares are fixed and circles average, told apart by shape. "Including empty shapes" makes 0 a neighbour (K–1 rules, p. 1 example).
- The one-unchanged-board check (K–1 p. 2, 2–3 p. 2, 4–5 p. 1). Copied piles never replace the reference stacks.
- K–1: the inverse builds in P3–P4, the impossibility in P5, and the constant boards in P6–P7.
- 2–3 P3 with P4, and 4–5 P4's middle square against its branching circle: the clearest picture of where equality stops.
- 4–5: P5's two identical boards, P6's 5 against 25, and P7's four boards.

## Fix

1. **should**, K–1 P3, P4 and P7 (pp. 3, 4, 7): ten, eight, and six per board, one recording board per answer. That gives away knowing you have them all, and guide p. 7 says "Do not announce the total of ten before the search". math.md lists the match as a pass; I read it as the finding. Print two or three spare boards on each page.
2. **should**, K–1 order: linked circles are P2, but guide pp. 3 and 26 go P1, then P3 or P4, and return to P2 "only when children can keep both circle stacks fixed", so the parent volunteer must skip a page. Move that page and its example after P4; renumber packet and guide.
3. **should**, 4–5 P7 (p. 7): the cards are exactly the missing values 1/2, 1/3 and 2/3, so two boards become matching. Add cards that fit no board (1/4, 3/4), or print unshaded bars in halves, thirds and quarters.
4. **should**, K–1 pp. 1–2, 2–3 p. 2, 4–5 p. 1: the captions repeat the opening rules under the pictures. They are "Both square stacks stay. Use two mats, even for 0.", "Check both circles on the same board. Keep all four stacks." and "Check both circles on this same unchanged board." Cut them and keep the visuals.
5. **should**, guide pp. 9, 16 and 18 send the adult to "page 3" for the equal-gap and uniqueness arguments, which are on p. 4 (math.md Problem 1; agreed). Fix the three strings in facilitator-src/content.py.
6. **could**, 4–5 P1: "Try to find a second filling" assumes one exists; "Is there a second filling…?" would match P5.
7. **could**, 2–3 p. 2: third graders may know "÷" better than "(2 + 4)/2" (a prediction).
8. **could**, guide p. 3: "eight edge strips" and "a seventh place on the largest board" fit no task, and nothing says how the K–1 P4 cards are made.
9. **could**, the guide's footers count 25 pages, and p. 26 has a different header.

## Overlaps

Week 47 (gentle-step landscapes) also fills free places between fixed clues and bounds them by extremes, under a step rule instead of averaging; it might share a height board in the app. Week 11 (chip firing) uses anchored graphs for a different theorem. No merge.

## App fit

Fit B, size M, as in themes.md, but "animated relaxation" should not be the solve: watching values settle is the prediction play children liked less. A plain neighbour-only tick also swaps 0 and 6 forever on a four-cycle without squares (bonus P2–P3), so any animation needs the own-and-neighbour rule.

A child taps a circle to raise or lower its stack, and each circle lights when it equals its neighbours' average. With every circle lit live, a unique filling becomes hill-climbing, so make the solve inverse or design:

- Choose square cards so a circle hits a target, finding every way (K–1 P3–P4); the child claims "done" and the app checks, with no slot per answer.
- Change one square so a circle rises by 2 (2–3 P1).
- Pick endpoints so every circle is whole (4–5 P7).
- Decide which circles can tie the largest square (2–3 P4, 4–5 P4).

The certificate for "can't" is the chase: from a highest circle, every neighbour is forced equal until a square breaks the chain. Avoid isolated circles, and keep fractions to a marked mode.

**Decision, October 10, 2026.** Port, in Wave 7 (sets and numbers), with inverse and design goals only: choose square values so a circle hits a target, change one square to move a circle, pick endpoints so every circle is whole, and decide which circles can tie the largest square, with the chase from a highest circle as the "can't" certificate. No animated relaxation as the solve. Tracked in the app's [decisions.md](https://github.com/jamesrp/small-math-adventure/blob/main/docs/plan/decisions.md).

## Classroom evidence

None reported. The guide and source README call the theme unpiloted, a library slot not yet scheduled.
