+++
id = "w42.k1-fair-rule"
title = "A shape rule with equal chances"
grades = ["K-1"]
route = "first"
kernel = "RB and BR have the same chance, so RB gives a square and BR a circle (or the reverse) is fair."
+++

## text @0 size=13
Use three red counters and one blue again. A rule gives each color pair a square, a circle, or no shape. The same color pair always gets the same answer.

## figure
sample_rule(2.7,3.4,2.9)

## prompt @5
Make a rule that sometimes gives each shape and gives them the same chance. Try it on six random pairs.

## figure
rule_board(8)

## text @15 size=13
Use a cross to record no shape.

## figure
answer_box(17)

## key
Use the rule stated above or its shape-swapped version. The six random outputs vary; even no outputs is possible. Do not judge the rule from a balanced or unbalanced sample. If a child proposes a different rule, keep it as a conjecture until the picture check in Problem 3.
