+++
id = "w31.predict"
title = "Predict the first dot and the blockers of far targets"
grades = ["4-5"]
route = "return"
kernel = 'The first dot of (a, b) is (a/d, b/d) and there are d - 1 blockers, d the greatest common factor; (12, 8), (15, 10), (21, 14) all lie on the ray of (3, 2).'
+++

## prompt
Predict the first dot and number of blockers for (12, 8), (15, 10), (21, 14), (25, 15) and (13, 8). Explain a rule that works for any target with whole-number coordinates.

## figure
draw(('ruled', 2.6, 4), ('grid', .8, 8, 25, 15, .7), ('ruled', 20.6, 4))

## key
\emph{Print guide, p. 4.} Targets (12,8), (15,10), (21,14) all have first point (3,2) and respectively 3,4,6 blockers. For (25,15), first (5,3), four blockers. For (13,8), first (13,8), zero blockers. The rule applies to every nonzero whole-coordinate target; O itself has no direction and is excluded. The extra grid on that page runs to (25,15) at 7 mm, so each of these targets can be checked with thread; about 20 cm reaches the farthest.
