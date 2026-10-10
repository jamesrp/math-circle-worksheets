# Week 66: Lamplighter streets

**Verdict: keep.** No must: real geometric group theory, every answer right, a theorem-first guide. The should items (P5's wording, a late dead-end problem, counter fit, a K–1 line) wait for the next reviser.

Reviewed October 10, 2026 by Claude, with the math check in [week-66-math.md](week-66-math.md). Packets: week-66-students.pdf, GGT66-S-v1, 4 pages, one shared Grades 3–5 packet, Problems 1–5. Adult guide: week-66-facilitator.pdf, GGT66-FAC-v1, 2 pages. Companions noticed but not reviewed: none exist. Status: unpiloted prototype awaiting organizer review; the source README says "physical preparation and handling have not been rehearsed".

## The mathematics

A state is the walker's position plus the lit lamps; a move is L, R or F. This is the lamplighter group's word metric. From all-off at 0, the distance is the number of lit lamps plus the shortest walk from 0 that reaches both end lamps and stops at the walker. Lamps −1, 0, 1 with the walker at 0 is a dead end: 7 moves, and all three neighbours are 6. The dead ends are exactly the targets with the walker at 0, lamp 0 lit and a lamp lit on each side (my BFS, to distance 13); nothing in the packet states this. A mathematician would enjoy it. P1–P2 build the decomposition, P3 proves a lower bound, P4–P5 reach the dead end.

## Ratings

| | Rating | Evidence |
|---|---|---|
| Mathematics | strong | A real word metric with honest scope; the −4…4 street never binds. The dead end refutes the idea that one more move always costs more. |
| Problems | adequate | Purposeful contrasts: one lamp, both sides, a return home (P1); the same lamps with three endings (P2: 9, 11, 9). Six targets precede P3's explanation. The ending is thin: one dead end, and P5 is one sentence (fix 2). |
| Student pages | adequate | Spec header and footer, no slop, brief rules, a non-task worked visual, large working streets. Faults: fixes 1 and 3. |
| Concreteness | adequate | Counters and a pawn hold the state; a partner flips "only after pointing to the walker's place", which answers context.md's paper-lamp failure. The launch replays the printed RF. Gaps: untested counter fit (fix 4); the launch omits the goal. |
| Correctness | strong | math.md: 120 checks, no error, one wording finding, which I share. My BFS adds that P2's B, (0, {−2, 0, 2}), is also a dead end (11; neighbours 10), unmentioned anywhere. |
| Adult guide | strong | Theorem-first p. 1 with proof, scope and band map; launch, first route, keys with lower bounds, held hints, the general formula. Missing: the dead-end characterization and a K–1 line. |
| Age fit, K–1 | weak | No route, by design ("No forced K–1" in the outline). The guide gives the K–1 parent volunteer nothing, not even "use another activity". |
| Age fit, grades 2–3 | strong | A prediction. An adult reads p. 1's six short sentences; negative numbers are only labels; the arithmetic is counting to 11. P4's build, move, draw, reset is the heaviest demand, and the guide's first route stops at P3. |
| Age fit, grades 4–5 | adequate | P3–P5 suit the organizer's table, but the packet ends at one counterexample, and the general rule is an adult-only "optional extension". |

## Keep

- p. 1: the rules, the partner protocol (the flipper points first; swap between targets), one move word as the record, and the start → R → RF visual.
- P1's three targets and P2's same-lamps, three-endings page.
- P3: "Find a way to convince your partner that fewer moves cannot work." and its Workspace street.
- P4's draw-in boards and its bold "all lamps off, walker at 0".
- Guide: the overview, the launch, the Walks + flips tables, and "A trial with seven moves alone is only an upper bound".

## Fix

1. **should**, p. 4, P5: "Can you always make a target harder … by making one more legal move?" also reads "Does one more move always make a target harder?", which flipping target A's lamp back off (2 to 1) settles with no dead end (math.md item 1). The answer is No either way and an adult can redirect, so not a must. Print "Does every target have at least one next move, L, R or F, that makes it harder to reach from all-off at 0? Use your results to settle this question."
2. **should**, a new p. 5: "Problem 6: Find other targets where L, R and F each make the target easier to reach from all-off at 0. Which targets are like this?", with a large street and six small draw-in streets.
   Key, also for the overview: walker at 0, lamp 0 on, a lamp on each side. P2's B is one; the smallest others are lamps −2, 0, 1 and −1, 0, 2 (9; neighbours 8). Between the end lamps the walk is 2(r − ℓ) − |p|, so a step away from 0 shortens it, and turning lamp 0 off saves a flip.
3. **should**, p. 2, P2: cut "These targets have the same lamps on, but the walker ends in different places." It narrates the diagrams and prints guide p. 2's held hint ("compare only the final walker positions").
4. **should**, guide p. 1, materials: the large circles are 13 mm on 19 mm centres. Two-colour counters are often 2–2.5 cm and would overlap, hiding which lamp is lit; "placed beside a lamp" loses the position. Name a counter of 17 mm or less (or paper squares dark on one side), or print a landscape mat. A prediction until rehearsed.
5. **should**, guide p. 1: say what the K–1 table does. A should, as on the Week 60 card, because the outline authorizes no K–1 packet. A possible route, a prediction: the launch, then P1 and P2 A and C as picture-matching, one cube stacked per move, stacks compared for "fewest".
6. **could**, pp. 1–3: "Start with every lamp off and the walker at 0." repeats three times; state it once in the rules.
7. **could**, pp. 1–3: the working streets print ▼, the walker symbol, at 0; use a home mark.
8. **could**, p. 1: cut "Use the large street for your counters."; the launch shows it.
9. **could**, guide launch: show the goal too, a non-task target reached by a long word and a short one.

## Overlaps

Week 2 also flips lamps for fewest moves (upper P4–P5), but over F₂ with no walker, so order never matters. Weeks 39, 67, 72 and 74 are geometric-group-theory siblings; Week 74's elevator word metric is nearest. None has dead ends or a walker carrying state. No merge.

## App fit

Fit A, size S. themes.md has no row; it should read: | 66 | Lamplighter streets | Walk and flip the lamp underfoot to reach targets in the fewest moves | Distance = lit lamps + shortest covering walk; dead ends | No | A | Tap to walk or flip; Plume's par is the distance; build a dead end | S |

- **Solve.** A dark street with a home mark, a lamplighter and a target card. Tap a neighbouring lamp to walk, the lamp underfoot to flip; the app enforces the rule. Plume's par is the BFS distance, cross-checked by the formula; the certificate for "best", shown after, is the lit lamps plus the walked span as a bar.
- **Instances** where order matters: lamps −1 and 3, ending at −1, take 9 moves going to 3 first and 11 going to the near lamp first. Set ending at home (P2's B, 11) against ending at an end lamp (9).
- **Dead ends.** Light lamps and park the walker so every move makes the street quicker to reach from dark, at 9 moves or more; a wrong state gets back the move that makes it harder.
- **Pitfalls.** No live distance, no typed predictions of the count, short streets. Draw on P1, P2, P4 and the dead ends at 7, 9 and 11; leave P3's proof and P5 to paper. Mr. Hops, the road's frog lamplighter, is the natural keeper once children have played it.

**Decision, October 10, 2026.** Port in this round as **Lamplighter**, a group in Lantern Wires: puzzles on a street, a ring and a grid with the breadth-first distance as the move budget, including the 7-move dead end. The dead-end construction puzzle waits.

## Classroom evidence

None reported. QA.md: "No classroom pilot has occurred." Counters and partner roles are unrehearsed. themes.md lists only Weeks 1, 2 and 15 as taught.
