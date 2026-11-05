# Home plan: poisoned cookie (Chomp)

Weekend of November 7 and 8, 2026, at the kitchen table: James with Jay, Rose and perhaps a third child. **Untried:** nobody has played this plan yet, and every time is a guess. It comes from the [poisoned cookie draft](../topic-scouting/drafts/poisoned-cookie/) but drops its worksheets, bite card and labelling tables, which turn the game into recording. Print the [boards](2026-11-08-poisoned-cookie-boards.pdf). Every fact below is checked by [src/chomp_check.py](src/chomp_check.py).

## The mathematics, for you

**The game.** Cookies fill a rectangle; the bottom-left one is poison. On your turn, choose any cookie and eat it with every cookie above it, to its right, or both. Whoever has to eat the poison loses. "3 by 4" means 3 rows and 4 columns; "row 2, column 3" counts from the poison, which is row 1, column 1. Each bite eats a cookie, so games end and nobody draws: every board is a win or a loss for the player about to move.

1. **Theorem (strategy stealing; Gale, 1974, as cited in the draft).** On every rectangle bigger than one cookie, the first player can force a win. *Proof.* If not, eating only the top-right cookie loses, so the second player has a winning answer. But every bite eats the top-right cookie too, so the first player could have made that answer as the first move, leaving the same board. Contradiction. *Assumptions:* the game ends, no draws, and one cookie lies in every bite, which holds exactly for rectangles. *Limits:* it names no bite, and other shapes can lose for the mover.
2. **Explicit strategies.** One row: eat everything but the poison. Squares: bite row 2, column 2, leaving an L with equal arms, then copy each bite on the other arm; an L with equal arms always loses for the mover. Two rows: a "step" (top row one shorter than the bottom) always loses for the mover. On a full 2-row board eat the top-right cookie; after each reply, if the rows are equal eat the top-right cookie, and if the top row is two or more shorter, cut the bottom row to one longer than the top.
3. **Elsewhere, only search.** Winning first bites, found by computer, each the only one on its board: 2 by anything, the top-right cookie; 3 by 3 and 4 by 4, row 2, column 2; **3 by 4, row 2, column 3** (leaves rows of 4, 2, 2); 3 by 5, row 3, column 4; 3 by 6, row 2, column 4; 4 by 5, row 3, column 3; 4 by 6, row 2, column 3. Uniqueness is a computation for these sizes, not a theorem, so don't promise it. Your answers on 3 by 4 if a child bites elsewhere first (their bite → yours, row then column): 1,2 → 2,1; 1,3 → 3,2; 1,4 → 2,2; 2,1 → 1,2; 2,2 → 1,4; 2,4 → 2,3; 3,1 → 2,4; 3,2 → 1,3; 3,3 → 2,3; 3,4 → 2,3. No simple rule is known even for three rows (Zeilberger, 2001, also cited from the draft and not rechecked). A tempting three-row pattern fits 3 by 4 to 3 by 8 and fails at 3 by 9 (only winning bite: row 3, column 7).
4. **Trap boards** (lose for the player to move): the poison alone; the little corner (the poison, one cookie to its right, one above); any two-row step; any L with equal arms; rows of 2, 2, 1; rows of 4, 2, 2. A board and its flip (rows turned into columns) always win or lose together.

**What children might find.** By experiment: first is better on rectangles, second on the little corner, steps and equal Ls. As conjectures: "bite next to the poison on squares", "keep the top row one shorter". As explanations: copying and the step reply, which work at every size. Strategy stealing settles every rectangle, which no amount of play can, and still names no move.

## Materials and setup (5 minutes)

- The two board pages at 100% (check the 10 cm bar). Squares are 30 mm, a little bigger than the draft's 25 mm, so a US quarter (about 24 mm) or a small square cracker about 2.5 cm across fits. Big board 4 by 6; small page: a 1 by 5 train, 2 by 2, 2 by 3, and an L with arms of 3.
- About 30 cookies (counters, coins, cereal, chocolate chips, small crackers) and a cup each. The green face is the poison. **Mess-free:** what you bite goes in your cup. **Real food:** eat what you bite except the poison; a chocolate bar that breaks into a grid is a board by itself, with one corner piece as poison.
- Nothing to write with. The only record is optional: a sticky-note arrow on a bite that wins.
- Sit side by side, facing the same way, so "up and to the right" means the same to everyone; across the table, turn the board to whoever is biting.

## The route

Each move stands alone. Stop after any of them and pick up anywhere next time.

**1. Launch (3 minutes).** Fill two rows, 5 columns, on the big board. "The green one is poisoned. Put a finger on any cookie: it goes, and so does every cookie above it and to its right. Whoever has to eat the poison loses." Bite row 1, column 3: six cookies go. Rebuild; a child bites the top cookie in column 2, and only the top row from there goes. Two children play one game. Say only whether a bite is allowed. *Watch for* bites that take cookies below or to the left.

**2. Rose's boards (5 to 10 minutes).** The older children play each other on the big board, choosing sizes, while Rose plays you. Play honestly: if she misses the winning bite, win, and offer a rematch at once.

- *The train (1 by 5).* "Can you make me eat the poison?" She goes first and can find the big bite: everything but the poison.
- *The little corner (2 by 2).* She goes first. Only the top-right cookie wins: it leaves the little corner, and whichever cookie you eat, she eats the other. Use her name for it, then ask "On the little corner, would you rather go first or second?"
- *2 by 3.* The same first bite wins, and after any reply she can make the little corner or leave just the poison.
- *Copy-cat (the L).* You go first. If she makes the arms match after every bite, she wins. Hint only if asked: "Can you make the arms the same?"

*Rose's moment:* she goes first against Jay or the third child on 2 by 2 or 2 by 3, or builds the little corner and says "You go first", and wins because she knows something. Her jobs between games: build every board, choose its size, ask "first or second?" She can also team with an older child against you and make the bite they agree on. *Stop* once she has won by knowing, or would rather build.

**3. First or second? (10 minutes).** The older children challenge you. Before each new board shape ask "Would you rather go first or second?"; they choose, you take the other seat. Going first on a rectangle, use the bites above; going second, play your best, and after a loss ask "Was there a bite that would have beaten me?" Slip in trap boards (a step such as 5 and 4, the little corner, an equal L), where second is right. Don't explain. *Watch for* "you always win when you start" and "it depends on the shape". If someone says "first always wins", offer a step board. Hint if asked: "Look at my first bite."

**4. Square and two-row challenges (10 to 15 minutes).** Jay and the third child go first.

- "Beat me on 3 by 3, then 4 by 4." To find: the bite diagonally next to the poison, then copying. If asked: "What shape was left after my first bite?" If keen: "Would it work on a 10 by 10?"
- "Beat me on 2 by 6." To find: keep the top row one shorter. If asked: "What did the board look like each time I handed it to you?" Then: "Which two-row boards would you rather go second on?"
- *The odd one, 3 by 4.* Neither trick works; the answer is row 2, column 3. If Jay asks for a rule: nobody knows one for three rows.

**5. Invent your own (open).** "Build a board where you'd rather go second, then make me go first." Check it by playing honestly. Children may also change a rule (two poisons, poison in the middle, bites that take only a row or a column). Play those, but the facts above cover only the usual game.

**6. Optional puzzle: the stolen win (5 to 15 minutes).** Once Jay or the third child believes first always wins on rectangles, offer it once: "I can prove the first player wins on every rectangle bigger than one cookie, without knowing the move. How?" Hints only if asked, one at a time: (1) "Suppose I start by eating only the top-right cookie." (2) "If that's a bad bite, you have a winning answer. Find it on 3 by 4." (Row 2, column 3.) (3) "Could I have made your answer as my very first bite?" (Yes: every bite eats the top-right cookie anyway, so the board left is the same.) (4) "So either my top-right bite wins, or your answer does." Then, if there's energy: "Does it work on the little corner or an L?" (No: no cookie lies in every bite there, and they lose for the mover.) "Does it tell you where to bite on 3 by 5?" (No.) Hex, if it comes later, uses the same argument.

**When to stop.** On a high point: Rose's win, or a trick someone found. Also when games turn into "again, again" with nobody choosing. Next time, start at Move 3 with a new board, or at Move 5.

## How it went

(Add a dated line after the weekend.)
