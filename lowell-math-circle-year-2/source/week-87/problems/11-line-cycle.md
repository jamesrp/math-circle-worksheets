+++
id = "w87.line-cycle"
title = "Can one line produce the cycle?"
grades = ["4-5"]
route = "return"
kernel = "On a line the middle candidate is never a voter's strict last choice, so the cyclic cards, which put each letter last once, cannot come from distances."
+++

## text @18,29 size=11
A nearer letter ranks higher; equal distances make a tie, not a strict ranking. In this problem letters and favorites may be anywhere on a straight line.

## figure
t(18, 49, 'Fixed locations', 65, 9) + numberline(23, 72, 52, [1], [('D', 0), ('E', 4), ('F', 9)], True) \
+ t(89, 49, 'From the same favorite', 59, 9) + t(90, 61, r'D: 1 step\\E: 3 steps\\F: 8 steps', 50, 11) + card(159, 49, 'DEF', 'V1', 25, 47)

## prompt @110
Could these three cards come from distance choices on one line? Put A, B and C at different places and choose a favorite for each voter, or explain why it cannot be done.

## figure
cards(29, 142, ['ABC', 'BCA', 'CAB'], 43, 44, 9) + numberline(23, 210, 170) + space(225, 26)

## key
No. Put the three distinct candidate locations in order $\ell<m<r$. For any voter favorite p at or left of m, the rightmost candidate r is strictly farther away than m. For any p at or right of m, the leftmost candidate $\ell$ is strictly farther away than m. At least one extreme is therefore farther from p than the middle candidate; m cannot be that voter's strict worst choice. This holds for arbitrary real positions and favorites, including favorites outside the candidate interval.

The cards $ABC$, $BCA$, $CAB$ each put a different candidate last. Whichever candidate occupies the middle would have to be strictly last for one of the voters, contradicting the preceding fact. Coincident candidates or tied distances cannot rescue a strict ranking. The worked conversion on the student page shows how one fixed favorite produces a ranking; failed experimental placements alone would not prove impossibility. This gives a concrete limit of the nearest-location model, not a judgment about people's preferences.
