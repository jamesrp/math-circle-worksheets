+++
id = "w24.six-of-nine"
title = "Can every advantage reach six of nine?"
grades = ["4-5"]
route = "return"
kernel = "Impossible: no split of 1 to 9 into three decks of three gives each deck at least six of nine pairs against the next."
+++

## prompt
Use cards 1 to 9 once each in three decks of three. Can A win at least six of its nine pairs against B, B at least six against C, and C at least six against A? Find an arrangement, or explain why it is impossible.

## figure
art(pool(list(range(1,10)),7.55,9), decks([('A',[None]*3),('B',[None]*3),('C',[None]*3)],5.75))
