+++
id = "w87.choose-waiting"
title = "Choose who waits"
grades = ["2-5"]
route = "first"
page = "same"
kernel = "On the cyclic cards the letter that waits always wins the knockout, so the agenda alone decides the winner."
+++

## prompt @149
Keep the A/B/C cards from Problem 1. Choose a first pair and a waiting letter so that A wins the knockout. Can you make B win? Can you make C win?

## figure
''.join(t(20, 186+i*22+3, 'Winner '+goal, 30, 11) + box(53, 186+i*22, 52, 17, 'First pair:', 9)
        + box(111, 186+i*22, 39, 17, 'Waiting:', 9) + box(156, 186+i*22, 40, 17, 'Final pair:', 9)
        for i, goal in enumerate('ABC'))

## key
Keep the Problem 1 cards. To make A win, first compare B with C; B wins, then A beats B. To make B win, first compare C with A; C wins, then B beats C. To make C win, first compare A with B; A wins, then C beats A. Thus the waiting option wins each time. These three choices exhaust all unordered first pairs. Reversing the left/right position of a pair changes no ballot under the rule.

Distinguish the first-round loser, first-round winner, waiting option and final winner. The knockout mat retains those states. Reset the movable options between attempts; do not reset or rewrite the preference cards. A child can record just the first pair and final winner. This is an agenda effect under sincere pairwise voting, not evidence that voters changed their minds or voted strategically.
