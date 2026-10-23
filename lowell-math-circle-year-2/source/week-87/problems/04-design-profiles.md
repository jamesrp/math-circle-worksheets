+++
id = "w87.design-profiles"
title = "Design a fixed winner and a waiting-letter winner"
grades = ["2-5"]
route = "first"
kernel = "A letter that beats both others wins every knockout; with three different cards the waiting letter can matter only for ABC, BCA, CAB or its mirror ACB, CBA, BAC."
+++

## prompt @29
Each ranking card must contain A, B and C once. Make three different cards so that the same letter wins every knockout. Make another set of three different cards where changing the waiting letter changes the winner.

## figure
t(18, 68, 'Same winner every time', 180, 10) + cards(29, 77, ['   ']*3, 43, 60, 9) \
+ t(18, 155, 'Different winners', 180, 10) + cards(29, 164, ['   ']*3, 43, 60, 9)

## key
A suitable three-distinct-card profile with one winner for every agenda is $ABC$, $ACB$, $BAC$. A beats B 2--1 and C 3--0. If A waits, it beats the first winner; if A plays first, it wins both of its comparisons. Three different cards cannot share a first choice, since only two rankings start with each letter. The cyclic profile of Problem 1 is already a valid three-distinct-card agenda-dependent example; children may reproduce or relabel it. Every working set uses exactly the cards $ABC$, $BCA$, $CAB$ or $ACB$, $CBA$, $BAC$, in some order. Each card agrees with at most two of the cycle's three winning pairs, and each winning pair needs two cards, so every card agrees with exactly two. ``Is there a different one?'' makes a good return question.

Do not require every child to enumerate all possible profiles. Accept a construction with its checkable pair votes and agenda argument. For a held hint, ask what an option would need to do against each of the other two. Blank ranking cards and movable slips preserve each invented profile without repeatedly transcribing it. If two identical cards appear, remind the child of this task's distinct-card condition; a repeated ranking would still be a legitimate voter in the general model.
