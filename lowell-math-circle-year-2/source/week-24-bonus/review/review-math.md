# Week 24 independent mathematical review

Scope: the actual four-page `draft/bonus.pdf`, shared Grades 2–5. Read PROMPT.md and CRITIC-MATH.md, independently transcribed the printed decks/tasks, inspected all four rendered pages, and ran `independent-check.py`. The script uses no writer checker or answer data. Exact enumeration is in `checks.json`.

## Located edge case

Grades 2–5, page 4, Problem 4: “Then make another label bag with any number of A, B, C slips.” Zero slips is literally an allowed number, but an empty bag cannot supply a label or have the requested average points. Smallest fix: “Then make another nonempty label bag using A, B, C slips.” Zero copies of an individual label must remain allowed; pure strategies are part of this task.

## Explicitly verified tasks and representations

- Page 1, Problem 1 asks for all replacement triples and the most frequent champion. All 27 have distinct values. A and B each win 10, C wins 7. Per-card champion counts are A `(0,1,9)`, B `(0,4,6)`, C `(1,2,4)`. The joint winner is a valid outcome of the question. The three printed decks and 27 recording rows match this model.
- Page 2, Problem 2 asks for every ordered first/second-card pair and its sum. There are exactly nine equally likely pairs per deck. Multiplicities are A `{4:1,6:2,8:1,11:2,13:2,18:1}`, B `{2:1,7:2,9:2,12:1,14:2,16:1}`, C `{6:1,8:2,10:3,12:2,14:1}`. Each printed table has nine rows and the repeated deck diagrams match page 1. Reverse orders are distinct outcomes; equal sums are not uniform.
- Page 3, Problem 3 asks for all four-card outcomes, points, and the superior expectation. Among 81 outcomes per pairing, A/B has wins `(37,44)` and 0 ties; B/C has `(39,38)` and 4 ties; C/A has `(39,38)` and 4 ties. Expected points respectively are `(74/81,88/81)`, `(82/81,80/81)`, `(82/81,80/81)`. The higher-expectation players are B, B, C. The printed pair order and win/tie columns match these answers.
- Page 4, Problem 4 asks children to choose a concealed label mixture and evaluate it against the three pure opponents. Pure A has payoff row `(1,10/9,8/9)`, B `(8/9,1,10/9)`, C `(10/9,8/9,1)` against A/B/C. The A/B/C bag earns exactly one expected point against each, and any equally populated bag does too. Separate copies make the same-label comparison independent; each pure self-comparison has three ties in nine outcomes. With the nonempty-bag correction above, arbitrary child-designed bags have well-defined answers.
- Page 4, Problem 5 asks whether any mixture beats one expected point against every pure opponent. No: each pure payoff row sums to 3, so every mixed row does too. For proportions `(a,b,c)`, the expectations are `1+(c-b)/9`, `1+(a-c)/9`, `1+(b-a)/9`. All three cannot exceed 1; all three being at least 1 forces `a=b=c`. This supplies a general certificate, beyond the script's check of every label-count triple of total size 1–12.

No other located mathematical defect. These are theoretical results under independent uniform replacement draws, not guarantees from a finite sequence of games. Mixing, concealment and physical rehearsal remain untested.
