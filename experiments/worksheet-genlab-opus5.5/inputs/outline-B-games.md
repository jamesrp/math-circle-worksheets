Week 7: Take-away games

Mathematical kernels

1. Backward induction. In a take-away game there is a pile of counters; two players alternate removing counters, and each move must remove an allowed number (for example 1 or 2). Whoever takes the last counter wins. Every pile size is either a win for the player about to move or a loss: a pile is losing when every allowed move leads to a winning pile, and winning when at least one move leads to a losing pile. Working up from an empty pile classifies every size. A winning strategy means always moving to a losing pile, and it must answer every possible reply of the opponent, not just the replies you expect.

2. Repeating patterns. With moves {1, 2} the losing piles are the multiples of 3. With moves {1, 3, 4} the losing piles are those leaving remainder 0 or 2 when divided by 7. With moves {1, 3, 5} the game is decided by whether the pile is even or odd. For any finite set of allowed moves the win/lose pattern eventually repeats: each label depends only on a fixed number of earlier labels, and there are only finitely many possible windows of labels (pigeonhole). Changing the rule changes the pattern, and the obvious greedy move (take as many as you can) is often wrong.

3. Beyond win and lose. Sprague–Grundy values (the smallest number not among the values of the positions you can move to) let you play sums of games, such as two piles where each turn you move in one pile. Two piles of the same game with equal values are a loss for the player to move. Research continues on when such patterns repeat; for example, whether every finite octal game is eventually periodic (Guy's conjecture) is still open. Sources: Berlekamp, Conway, and Guy, Winning Ways; Siegel, Combinatorial Game Theory.

Suggested emphasis by level: K–1 plays small games with moves of 1 or 2 and looks for traps; grades 2–3 classify piles under a rule such as {1, 3, 4} and test claimed strategies against every reply; grades 4–5 find and explain repeating patterns and compare what happens when the rule changes.

Materials

Counters (plenty), paper, pencils, and small whiteboards. Children play in pairs or threes.
