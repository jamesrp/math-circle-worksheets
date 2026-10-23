+++
id = "w42.changed-bags"
title = "One bag first, another second"
grades = ["4-5"]
route = "return"
kernel = "With different bags the rule is fair exactly when the two bags have the same red fraction."
+++

## prompt @0
Use one bag for the first draw and another for the second. Decide exactly when your rule stays fair in the three cases below.

## figure
changed_bags()

## key
\textbf{First case:} first bag 3R/1B, second 1R/3B gives RB 9/16 and BR 1/16, so unfair. \textbf{Second:} 3R/1B then 6R/2B gives RB and BR each 6/32 = 3/16, so fair; equal color proportions matter, not equal bag size. \textbf{Third:} 2R/2B then 1R/1B gives each mixed order 2/8 = 1/4, so fair. In general the equality p(1-q) = (1-p)q reduces to p = q; positive output additionally requires 0 < p < 1.
