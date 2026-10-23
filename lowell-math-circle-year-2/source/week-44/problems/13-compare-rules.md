+++
id = "w44.compare-rules"
title = "Copying against return only"
grades = ["2-3"]
route = "return"
kernel = "Copying ties zero, one and two red draws at $1/3$ each; return only gives $1/4$, $1/2$, $1/4$."
+++

## prompt @0
Compare two rules, both starting with R1 and B1. Which numbers of red draws have the greatest chance after two draws? Give an exact reason.

## figure
two_rules()

## key
\textbf{Copying:} zero, one, two red draws are tied at 2/6 = 1/3 each. \textbf{Return only:} RR, RB, BR, BB are now four equally likely histories, so the totals have weights 1, 2, 1 and probabilities 1/4, 1/2, 1/4. One red draw is most likely in the unchanged bag. Copying increases the chance of repeating the first color.
