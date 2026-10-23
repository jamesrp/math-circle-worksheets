+++
id = "w13.closing-game"
title = "The closing game"
grades = ["K-1", "2-3"]
route = "return"
kernel = "On the diamond the second player wins by breaking the other branch; on the greedy board the first player wins only by closing the middle arrow first."
+++

## prompt [K-1]
Two players take turns closing one open arrow; whoever leaves no route wins. On each board, would you rather go first or second, and how can you win?

## prompt [2-3]
Two players take turns closing one open arrow. The player whose move leaves no route wins. Decide who can force a win on each board, and explain a strategy.

## figure [K-1]
game_boards(False)

## figure [2-3]
game_boards()

## key
Upper diamond: choose second. Any first move breaks one branch; break the other to win immediately. Lower greedy board: choose first and close AB. This leaves the diamond for the opponent, so break the remaining branch after their move. This is the only winning opening: any other first closure leaves all surviving routes sharing one arrow, which the opponent closes at once.

## hints
Hint: play each opening with roles reversed; ask who can make the last necessary closure, not who closes the most arrows.
