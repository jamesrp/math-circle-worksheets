+++
id = "w87.third-favorite"
title = "Telling the winner without trying every vote"
grades = ["3-5"]
route = "first"
kernel = "Median voter theorem on a line: sorted favorites p1 to p5, voters 3-5 defend p3 against anything to its left and voters 1-3 against anything to its right."
+++

## prompt @30
Put five favorites anywhere on the numbered ticks. Count all five markers, even when some share a place. How can you tell which location beats every other location without trying every vote? Explain why your way always works.

## figure
numberline(27, 103) + space(128, 122)

## key
Sort the five favorites with repeats retained: $p_1\leq p_2\leq p_3\leq p_4\leq p_5$. The third, $p_3$, wins against every distinct proposal q. If q is left of $p_3$, each of voters 3,4,5 is at or right of $p_3$, so moving farther left to q strictly increases their distance. Those three vote for $p_3$. If q is right of $p_3$, voters 1,2,3 supply the analogous three votes. The remaining two votes, including any ties, cannot reverse the majority.

This proof works on a continuous line too, provided the median location is an available option. It does not prove a result for arbitrary rankings, a circle, two-dimensional distance, or a restricted menu excluding the median. Testing every five-favorite multiset on these eleven ticks checks 3,003 arrangements but is not the reason the general theorem holds. Children can demonstrate the two defending groups using favorite markers and a proposal on either side, without algebra. If a child needs a direction, a held prompt is: ``Does the third favorite from the left always beat every different location? Show why, or find a set where it fails.''
