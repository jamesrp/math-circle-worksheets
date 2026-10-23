+++
id = "w87.repeated-favorites"
title = "Repeated and uneven favorites"
grades = ["3-5"]
route = "first"
kernel = "Repeated favorites are separate voters, and the winner is the middle favorite, not the midpoint or the mean."
+++

## prompt @30
Find a location that beats every other location for each set of five favorites. Voters sharing a favorite still get one vote each.

## figure
''.join(numberline(27, y, 160, fs) + t(20, y-43, r'Winning location: \rule{25mm}{0.3pt}', 100, 11)
        for y, fs in [(110, [0, 0, 0, 8, 10]), (177, [1, 4, 4, 4, 9]), (244, [9, 1, 10, 6, 0])])

## key
For favorites 0,0,0,8,10, the winner is 0. Three different voters at zero each prefer zero to every distinct proposal. Their markers occupy different lanes and their votes remain separate. For 1,4,4,4,9, the winner is 4 for the same three-voter reason. For 0,1,6,9,10, the winner is 6. This last configuration distinguishes the middle favorite from the board midpoint 5 and arithmetic mean $26/5$. Its voters are numbered out of left-to-right order (V4 is at 6), so no voter number points to the winner.

Do not combine coincident favorites into one token or discard a voter at zero. These examples deliberately retain multiplicity. A held adult prompt is to point to each voter's identity and ask which one has not yet voted, without selecting their vote. A tally that contains fewer than five tokens is unfinished, even if the outcome is already forced.
