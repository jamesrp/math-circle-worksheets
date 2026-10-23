+++
id = "w24.fewest-cards"
title = "The fewest cards per deck for a cycle"
grades = ["4-5"]
route = "return"
kernel = "One-card and two-card decks cannot cycle (numbers, and two-card dominance, are transitive), and A, B, C show three cards suffice, so three is the fewest."
+++

## prompt
Can three one-card decks make A win more than half its pairs against B, B against C, and C against A? Can three two-card decks do it? Explain for any choice of numbers. What is the fewest cards per deck that allows this, with all decks the same size?

## figure
art(decks([('A',[None]),('B',[None]),('C',[None])],7.25), decks([('A',[None]*2),('B',[None]*2),('C',[None]*2)],5.1))
