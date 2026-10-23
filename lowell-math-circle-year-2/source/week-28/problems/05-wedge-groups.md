+++
id = "w28.wedge-groups"
title = "Half-turns from seven wedges"
grades = ["2-3"]
route = "first"
page = "same"
kernel = "Groups of wedges that fill a straight angle exactly are the half-turns the closing test needs; organising by the largest piece finds all ten."
+++

## prompt @3.55
Use the seven loose wedges to make half-turns. Find as many different groups of letters as you can; use each wedge at most once in a group.

## figure
wedge_groups()

## key
\textbf{All ten groups:} AG, BG, CF, DF, ABF, ACE, ADE, BCE, BDE, ABCD. Order within a half-turn does not create a new group; A and B remain distinct letters even though their angles agree. Every listed group sums to 180$^\circ$.

\textbf{Completeness:} with G=150$^\circ$ the remaining 30$^\circ$ is A or B. With F=120$^\circ$ and no G, the remaining 60$^\circ$ is C, D or AB. With E=90$^\circ$ and neither F nor G, the remaining 90$^\circ$ is one of A,B plus one of C,D, giving four groups. With none of E,F,G, all of A,B,C,D are needed. This gives 2+3+4+1=10 and covers every largest-piece case.
