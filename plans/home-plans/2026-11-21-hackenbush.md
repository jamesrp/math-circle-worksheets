# Home plan: Hackenbush

Weekend of November 21 and 22, 2026 (James picked it November 21), at the kitchen table: James with Jay, Rose and perhaps a third child. **Untried:** nobody has played this plan yet, and every time is a guess. It is a home version of [Week 83, Hackenbush balances](../../lowell-math-circle-year-2/source/week-83/README.md), on paper instead of snap cubes, with picture boards and a way in for Rose. Print the [starting positions](2026-11-21-hackenbush-positions.pdf) in colour (page 3 of the printable). Every fact below is checked by [src/hackenbush_check.py](src/hackenbush_check.py).

## At the table

- Blue chops one blue segment, Red one red segment. Whatever is no longer joined to the ground falls: cross it out. No segment to chop on your turn: you lose.
- Before every board: "Who do you think wins if Blue starts? If Red starts?"
- Rose's wins as Blue: towers, chop from the top; tree, chop the trunk; house, chop a wall, then the other.
- Boards where whoever moves first loses: 5 (BR + BR + R); any board beside its colour swap; house + RBB (red at the ground, two blue on top).
- What things are worth: B 1, BR ½, BRR ¼, the tree ⅛, the house ¼, Sticks (board 4) −½.
- Stop on a high point: Rose chopping a trunk and watching everything fall, or Jay's "it's worth half."

## The mathematics, for you

**The game.** Red-blue Hackenbush, normal play. A board is a picture of blue and red segments, some touching the ground. Blue chops one blue segment, Red one red segment, taking turns; every segment that is no longer joined to the ground through other segments is removed. A player with no move loses. Each turn removes a segment, so games end and nobody draws. A stalk is written bottom to top: BR is a blue segment on the ground with a red one on top.

1. **Theorem (every board is a number; Conway, *On Numbers and Games*, 1976, and Berlekamp, Conway and Guy, *Winning Ways*, cited, not rechecked).** Every red-blue board has a value that is a number. Positive: Blue wins whoever starts. Negative: Red wins whoever starts. Zero: whoever moves second wins, so whoever moves first loses. Separate boards played side by side (each turn, chop in any one of them) add. The value is the simplest number strictly between Blue's best chop and Red's best chop. *Limits:* this is for red and blue only; green segments, which either player may chop, give values that are not numbers. "Worth" means moves of advantage, not number of segments.
2. **Whole moves.** A blue segment standing alone is worth 1: a spare move for Blue. A one-colour tower of n is worth n, as long as its owner chops from the top; chopping lower throws away your own moves. So a blue tower beside a red tower: the taller wins, and equal towers mean whoever moves second wins (checked up to 4 each).
3. **Half a move.** BR is worth ½: one BR beside an R loses for Blue (board 4), and two BR beside an R balance (board 5). Why board 5 balances, every case: if Blue chops a BR at the ground, Red chops the other red top, leaving B + R with Blue to move; if Red chops the lone R, Blue removes a whole BR; if Red chops a red top, Blue removes the other whole BR. In each case the other player runs out first. BRR is worth ¼, so BRR + BRR + RB balances while BR + BR + RB is a Blue win.
4. **Pictures.** A blue trunk with red leaves on top is worth ½, ¼, ⅛, … for 1, 2, 3, … leaves (checked to 5): the tree is ⅛. Red has three segments to Blue's one and still loses, because every red segment needs Blue's trunk; Blue wins by chopping the trunk at its first turn, and that is Blue's only winning chop. The house (blue walls; red ceiling and roof) is worth ¼: chopping one wall drops nothing, since the other wall holds the house up, and Blue wins by chopping the walls.
5. **Reading any stalk (Berlekamp's rule).** Count the first run of one colour as whole moves; after the first change of colour each segment is worth half the one below, plus for blue and minus for red. BBRB = 1 + 1 − ½ + ¼ = 1¾. The checker confirms the rule on all 126 stalks of 1 to 6 segments.
6. **Balancing.** A board beside its colour swap always balances: the second player copies each chop on the other board. To balance a board worth v, add one worth −v: house + RBB, tree + RBBB.

**What children might find.** By experiment: which colour wins, and that some boards are lost by whoever starts. As conjectures: "more segments wins" (false on the tree and the house), "chop low to knock their pieces down", "two of these beat one of those". As explanations: copying on a colour swap, and the every-case reply for board 5, which proves it balances. That BR is exactly half, and that values add, is what the balances suggest; the general theorem is cited, not something play can prove.

## Materials and setup (5 minutes)

- The positions page, printed in colour; 2 or 3 copies, since a played board is crossed out. Or redraw a board on scrap paper: a long ground line first, and a dot at every joint so segments are easy to count.
- Paper and two markers, blue and red. A pencil or any dark pen for the ground line and the crossing out helps; without one, cross out with your own marker.
- A chop: a big X through one segment of your colour. Then everyone looks for what fell and crosses it out too. Saying "Timber!" is allowed.

## The route

Each part stands alone. Stop after any of them and pick up anywhere next time.

**1. Launch (3 minutes).** Draw a ground line and one stalk: blue, red, blue, bottom to top. "Blue can only chop blue. Red can only chop red. If a piece isn't joined to the ground any more, it falls." Have Red chop the red segment, and ask "What falls?" (the blue above it). Cross it out. Then Blue chops the bottom blue: everything falls. Say only whether a chop is allowed and what falls. *Watch for* chopping the other colour, and leaving fallen pieces on the board.

**2. Rose's part (5 to 10 minutes).** Rose is Blue and plays you, or Jay plays Red against her (he will find he can't win, which is Move 3's puzzle).

- *Two towers (board 1).* Blue has 3, Red has 2. If she chops her bottom segment, her whole tower falls and she runs out first. Let that happen once if it does, then: "Which one could you chop so you keep the others?" Chopping from the top wins whoever starts.
- *The tree (board 2).* "Red has three pieces up there. Can you knock them all down?" Chopping the trunk wins at once, whoever starts. If she starts, she wins on her first chop; if you start, chop a leaf, and her trunk chop wins.
- *The house (board 3).* "Chop a wall. Does the house fall?" (No: the other wall holds it up.) Then the other wall: everything falls, and Red has nothing left.

*Rose's moment:* she plays the tree or the house as Blue against Jay or the third child and wins by knowing where to chop, or she draws a board ("make a picture, Red is the roof") for the older children to play. *Stop* when she would rather draw pictures than play them.

**3. Who wins? (10 minutes).** Jay and the third child, against each other or you, on boards 1 to 3. Each board twice, once with each colour starting. Before each: "Who do you think wins?" To find: Blue wins all three whoever starts, though Red has more pieces on the tree and the house. Hint if asked: "What happens to Red's pieces if the trunk goes?" *Watch for* "whoever has more pieces wins."

**4. Whoever moves first loses (10 to 15 minutes).** Board 4 (Sticks), then board 5 (More sticks), each with both starters. "On which board does whoever moves first lose?" To find: board 4 is a Red win either way; board 5 loses for whoever starts. Then: "Why? Can you answer every first chop?" (The three replies are in the mathematics, item 3.) Then: "Make your own board where whoever moves first loses" on board 6 or scrap paper, and test it by playing both starts. Hint if asked: "What if each piece had a twin in the other colour?"

**5. Half a move (open, for Jay).** "One blue segment is one move for Blue. What is BR worth?" Board 4 says less than 1 (it loses to an R); board 5 says two of them make exactly 1. So BR is half a move. Then, if keen:

- "What is BRR worth?" Test BRR + BRR + RB. (A quarter: it balances.) And BR + BR + RB? (Blue wins: RB is worth −½, not −1.)
- "What is the tree worth?" (⅛: three leaves, halving each time.) "Draw one small stalk next to the house so whoever moves first loses." (RBB, worth −¼.)
- Reading a stalk from the bottom: whole moves, then halves, quarters, eighths, as in Berlekamp's rule above. "Draw a stalk worth 1¾." (BBRB.)

**When to stop.** On a high point (Rose's trunk chop, Jay's "BR is half"). Next time, start at Move 4 or 5.
