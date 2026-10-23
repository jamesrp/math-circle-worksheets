+++
id = "w87.four-voters"
title = "Four voters: never losing is not winning"
grades = ["3-5"]
route = "return"
kernel = "With four voters at 1, 3, 7, 9 every location in [3, 7] never loses, yet none beats all others."
+++

## prompt @30
Use just four voters, with these favorites. Find every location that never loses against another location. Is there any location that beats every other one?

## figure
numberline(27, 110, 160, [1, 3, 7, 9]) + numberline(27, 157) + space(182, 68)

## key
Exactly the tick locations 3,4,5,6,7 never lose. No location strictly beats every other location. To see the first assertion, take x between 3 and 7. Against any proposal left of x, voters at 7 and 9 favor x, so x has at least two votes and cannot lose among four voters. Against any proposal right of x, voters at 1 and 3 defend x in the same way. Two distinct proposals both inside $[3,7]$ split the four votes 2--2. Hence none of those locations strictly beats all others.

A tick below 3 loses to 3: the voters at 3,7,9 all prefer 3. A tick above 7 similarly loses to 7, supported by voters at 1,3,7. This excludes all outside ticks and proves completeness. The same argument gives the whole closed interval $[3,7]$ if all real locations are available. There are still winning comparisons elsewhere; ``no universal strict winner'' does not mean every comparison ties.

Remove both the fifth favorite marker and its vote token. Changing only one creates a different, inconsistent procedure. Let children preserve several tied comparisons before asking for an explanation of all the weak winners.
