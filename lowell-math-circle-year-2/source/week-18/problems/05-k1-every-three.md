+++
id = "w18.k1-every-three"
title = "Every three-counter key for two pictures"
grades = ["K-1"]
route = "return"
kernel = "The three-counter keys that always work are the eight ordered pairs of opposite rows."
+++

## prompt
Find every three-counter key that always tells the two pictures apart; use more paper if needed. Swapping the pictures makes a different key.

## figure
''.join(keyed(.35,y,'triangle','---')+keyed(9.7,y,'square','---') for y in [3.15,6.75,10.35,13.95,17.55,21.15])
