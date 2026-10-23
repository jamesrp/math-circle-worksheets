+++
id = "w100.repair"
title = "Repair an impossible set of clues"
grades = ["3-5"]
route = "return"
page = "new"
kernel = "One bad triangle proves a table impossible without saying which clue is wrong; exactly three one-clue repairs work."
+++

## text
% Page 5: all one-clue repairs, with no answer-count scaffolding.
\promptat{0}{0}{193}

## prompt
Start with the clues from Problem 4. Change only A--C from 4 to 2. Can any world fit these clues?

## text
\draw[dashed,black!60,line width=.55pt] (204,1) rectangle (250,22);
\node[font=\fontsize{17}{19}\selectfont] at (227,11.5) {A--C = 2};
\txt{0}{29}{250}{Change exactly one of the ten clues to a different value chosen from 2, 4, 8, so that a world is possible. Find every repair. For each repair, draw a world fitting all ten clues. Explain why your list is complete.}
