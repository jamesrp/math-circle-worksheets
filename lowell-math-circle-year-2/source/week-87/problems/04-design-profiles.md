+++
id = "w87.design-profiles"
title = "Design a fixed winner and a waiting-letter winner"
grades = ["2-5"]
route = "first"
kernel = "A letter that beats both others wins every knockout; with three different cards the waiting letter can matter only for ABC, BCA, CAB or its mirror ACB, CBA, BAC."
+++

## text @18,29 size=11
Each ranking card must contain A, B and C once. Keep each set of cards unchanged while trying its knockouts.

## prompt @48
Make three different cards so that the same letter wins every knockout. Make another set of three different cards where changing the waiting letter changes the winner.

## figure
t(18, 82, 'Same winner every time', 180, 10) + cards(29, 91, ['   ']*3, 43, 60, 9) \
+ t(18, 165, 'Different winners', 180, 10) + cards(29, 174, ['   ']*3, 43, 60, 9)

## key
A suitable three-distinct-card profile with one winner for every agenda is $ABC$, $ACB$, $BAC$. A beats B 2--1 and C 3--0. If A waits, it beats the first winner; if A plays first, it wins both of its comparisons. The cards need not have identical first choices. The cyclic profile of Problem 1 is already a valid three-distinct-card agenda-dependent example; children may reproduce or relabel it, or invent another and test their claim.

Do not require every child to enumerate all possible profiles. Accept a construction with its checkable pair votes and agenda argument. For a held hint, ask what an option would need to do against each of the other two. Blank ranking cards and movable slips preserve each invented profile without repeatedly transcribing it. If two identical cards appear, remind the child of this task's distinct-card condition; a repeated ranking would still be a legitimate voter in the general model.
