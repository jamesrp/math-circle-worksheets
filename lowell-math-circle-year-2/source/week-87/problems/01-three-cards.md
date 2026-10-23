+++
id = "w87.three-cards"
title = "Is there a letter that beats both others?"
grades = ["2-5"]
route = "first"
page = "same"
kernel = "The cards ABC, BCA, CAB give a majority cycle: A beats B, B beats C and C beats A, each 2 to 1, though every card is a consistent ranking."
+++

## prompt @119
Use these three cards. Is there a letter that wins against each of the other two?

## figure
cards(33, 148, ['ABC', 'BCA', 'CAB'], 43, 62, 9) + space(226, 25)

## key
With cards $ABC$, $BCA$, $CAB$, V1 and V3 choose A over B; V1 and V2 choose B over C; V2 and V3 choose C over A. Every result is 2--1. Keep all three cards visible, including the unused option in each ranking. A voter's favorite being absent does not remove that voter: compare the two options that are actually offered. There is no overall top option in these pair results, even though each individual card has a strict first, second and third choice.

The non-task worked example uses $DFE$, $EFD$, $FED$. When D and E are offered, V1 chooses D and V2/V3 choose E, so E wins 2--1. The fixed cards remain unchanged in the next demonstration: E then meets waiting F; V1/V3 choose F and V2 chooses E, so F wins 2--1. A child who votes for an unavailable F in the first round needs the available pair made explicit, not a new preference card.
