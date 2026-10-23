+++
id = "w19.four-cards-8"
title = "Could four cards work?"
grades = ["K-1", "2-3"]
route = "return"
kernel = "No: three nested rows cover the deck, so any four cards put two in one row."
+++

## prompt @0.98 [K-1]
Can you choose four cards from this deck without breaking the rule? Show why or why not.

## prompt @0.98 [2-3]
Could four cards from this deck follow the collection rule? Explain why your answer covers every choice of four cards.

## figure [K-1]
deck(D8,2.01,cols=8,s=.69,gap=.20)+line(5.54)

## figure [2-3]
deck(D8,2.05,cols=8,s=.69,gap=.20)
