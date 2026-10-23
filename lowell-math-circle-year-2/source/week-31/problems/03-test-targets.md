+++
id = "w31.test-targets"
title = "Test given targets for blockers"
grades = ["K-1", "2-3", "4-5"]
route = "first"
page = { "2-3" = "same", "4-5" = "same" }
kernel = 'The blockers of (a, b) are the multiples k(a/d, b/d) for k = 1, ..., d - 1, where d is the greatest common factor; the first is the nearest to O.'
+++

## prompt [K-1]
Which circled targets are hidden? Find the blocker nearest O for each hidden target.

## prompt @6.3 [2-3]
Test these targets: (6, 4), (6, 3), (5, 3), (5, 2), (4, 4) and (4, 1). Find every dot between O and each target.

## prompt @6.3 [4-5]
For each target, find the first dot after O on its line and every blocker: (6, 4), (6, 3), (5, 3), (6, 6), (6, 0) and (0, 6).

## figure [K-1]
draw(('dots', 4, 3.2, 4, 2, [], [(4, 4), (4, 2), (2, 4), (3, 3)]), ('dots', 4, 14.5, 4, 2, [], [(4, 0), (0, 4), (2, 2), (4, 3)]))

## figure
draw(('dots', 3, 9.5, 6, 2))

## key [K-1]
\emph{Print guide, p. 2.} First picture: targets (4,4), (4,2), (2,4), (3,3) are all hidden; their nearest blockers are (1,1), (2,1), (1,2), (1,1), respectively. Second picture: (4,0) is blocked first by (1,0); (0,4) by (0,1); (2,2) by (1,1); (4,3) is visible and has no blocker.

## key [2-3]
\emph{Print guide, p. 3.} The requested complete interior lists are below. The target itself never goes in the blocker list.

\begin{tabular}{ll}
Target & All blockers between O and target \\
(6,4) & (3,2) \\
(6,3) & (2,1), (4,2) \\
(5,3) & None \\
(5,2) & None \\
(4,4) & (1,1), (2,2), (3,3) \\
(4,1) & None \\
\end{tabular}

## key [4-5]
\emph{Print guide, p. 4.} For (6,4), first (3,2), only blocker (3,2). For (6,3), first (2,1), blockers (2,1), (4,2). For (5,3), first (5,3) itself, no blockers. For (6,6), first (1,1), blockers (k,k), k=1,...,5. For (6,0), first (1,0), blockers (k,0), k=1,...,5. For (0,6), first (0,1), blockers (0,k), k=1,...,5.
