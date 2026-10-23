+++
id = "w29.five-seven"
title = "Predict and test the last impossible length for 5 and 7"
grades = ["4-5"]
route = "return"
kernel = 'The last gap for 5/7 is 23; with 5, 7, 11 and 17 from earlier pairs it fits ab - a - b.'
+++

## prompt
Predict the last impossible length for 5-rods and 7-rods, then test your prediction. Compare the answer with your earlier pairs and propose a rule that gives the last impossible length from the two rod lengths.

## figure
draw(('targets', range(19, 32), 3, 7), ('ruled', 8, 5))

## key
\emph{Print guide, p. 4.} Last gap for 5/7 is 23. It is impossible because zero to three 7-rods leave 23,16,9,2, none divisible by 5. A certificate is 24=5+5+7+7, 25=5$\times$5, 26=5+7+7+7, 27=5+5+5+5+7, 28=7$\times$4. Adding 5 covers all later targets. The earlier last gaps 5,7,11,17 and this 23 fit ab-a-b. These examples support a conjecture, not a proof of the formula.
