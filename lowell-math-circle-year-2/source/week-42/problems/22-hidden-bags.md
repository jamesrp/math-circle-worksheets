+++
id = "w42.hidden-bags"
title = "Every fixed bag with both colors"
grades = ["4-5"]
route = "return"
kernel = "For r red and b blue drawn with return, RB and BR each have chance $rb/(r+b)^2$: von Neumann's rule works for every fixed bag with both colors."
+++

## prompt @0
Keep your rule for these bags. Does it work for every fixed bag containing both colors, even if its contents are hidden? Explain your answer.

## figure
bags([(0,3,'RRRRRBB',''),(10,3,'RRRBBBB','')],(7.3,5))

## key
Both bags work: five red/two blue has 10 RB and 10 BR outcomes among 49; three red/four blue has 12 and 12 among 49. In general a fixed bag with r red and b blue has rb outcomes of each mixed order among (r+b)$^2$ equally likely identity pairs. The bag contents need not be known, but both r and b must be positive and the draws must follow the stated mechanism.
