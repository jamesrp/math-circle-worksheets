+++
id = "w05.u-puzzle-for-a-partner"
title = "A puzzle for a partner with few numbers"
grades = ["4-5"]
route = "return"
page = "new"
+++

## prompt
Build a city behind a folder, out of your partner's sight. Write some of its numbers around an empty grid so that your city is the only one that fits, using as few numbers as you can. Your partner solves the puzzle and then tries to find a second city that fits the same numbers.

## figure
close(gap(0.2) + pic(place([D.city(4, 1.2, boxes=True) for _ in range(4)], 2, 9.0, 8.4)))
