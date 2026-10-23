+++
id = "w87.agenda-change"
title = "Can the waiting letter change the winner?"
grades = ["4-5"]
route = "return"
kernel = "With three voters and three options the pair results are either a ranking with a letter that beats both others, or a cycle in which the waiting letter wins."
+++

## text @18,29 size=11
Use the shared card-voting rules: each voter chooses the higher of the two available letters. The first winner faces the waiting letter. Cards stay unchanged.

## prompt @52
Can changing the waiting letter change the knockout winner for either set of cards? Explain how to tell from the pair votes, without playing every knockout.

## figure
cards(29, 91, ['ABC', 'ACB', 'BAC'], 43, 52, 9) + cards(29, 160, ['ACB', 'CBA', 'BAC'], 43, 52, 9) + space(226, 25)

## key
The first profile is $ABC$, $ACB$, $BAC$. A beats B 2--1 and C 3--0, so A wins every agenda by the argument in shared Problem 3. The other pair has B beating C 2--1, but its result cannot remove A.

The second profile is $ACB$, $CBA$, $BAC$. B beats A, A beats C, and C beats B, each 2--1. Thus each waiting option can win: first A/C then waiting B; first B/C then waiting A; first A/B then waiting C. The task asks children to use pair votes to explain the possible agenda effect, not merely replay every knockout. In the three-option, odd-voter strict-ranking model, the pair comparisons form either a transitive order with a universal winner or a three-cycle. This observation should not be silently extended to larger menus, where more patterns occur.
