+++
id = "w24.two-card-cycle"
title = "Three two-card decks from 1 to 6"
grades = ["K-1", "2-3"]
route = "return"
kernel = "Impossible: two-card decks with no shared number win by beating smaller with smaller and larger with larger, which cannot go round a cycle."
+++

## prompt [K-1]
Can these six cards make three two-card decks where A wins more pairs than B, B more than C, and C more than A? Show a way, or show why it cannot be done.

## prompt [2-3]
Use cards 1 to 6 once each to make three two-card decks. Can A win more pairs than B, B more than C, and C more than A? Find an arrangement, or explain why there is none.

## figure [K-1]
art(kpool(list(range(1,7)),7.9), kdeck('A',[None]*2,6.35,2.65), kdeck('B',[None]*2,4.95,2.65), kdeck('C',[None]*2,3.55,2.65))

## figure [2-3]
art(pool(list(range(1,7)),7.7), decks([('A',[None]*2),('B',[None]*2),('C',[None]*2)],5.95))
