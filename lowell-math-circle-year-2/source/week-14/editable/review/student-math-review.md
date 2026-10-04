# Independent mathematical review

## Grades 2–3, page 7, Problem 7: automatic backtracking shortcut

**Exact text:** “Change the first filling into the second using as few flips as you can. Find another route with a different number of flips.”

**Intended outcome:** The minimum is 3 flips, followed by a genuinely different route. A 4-flip route exists.

**Evidence:** Write a filling as its set of internal diagonals. The printed start is S = {BD, BE, BF}, and the target is T = {AC, AD, AE}. Independent enumeration and breadth-first search give the shortest route

S → X = {AE, BD, BE} → Y = {AD, AE, BD} → T.

As written, the second request is automatically satisfied by S → X → S → X → Y → T, a legal 5-flip route made just by undoing and redoing the first flip. This extension works for any nonempty route and removes the need to investigate alternative routes. This is a task loophole, not an incorrect count or impossible diagram.

**Smallest fix:** Add “without visiting any filling twice” to the second sentence. The revised task is feasible: S → {BE, BF, CE} → {AE, BE, CE} → {AC, AE, CE} → T has 4 flips and no repeated filling.

No other mathematical or diagram errors were found in grades 2–3.

## K–1

All six problems and their diagrams check out completely.

## Grades 4–5

All seven problems and their diagrams check out completely.
