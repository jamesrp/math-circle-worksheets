# Week 173 (draft plan): How long does Snakes and Ladders last?

**Strand:** chance (app region "Chance and machines"). **Deep-math field:** Markov chains, expected value, working backwards. **Status:** draft plan, November 2026. No student pages, guide, review card or pilot.

## The deep idea

Snakes and Ladders has no decisions: where a counter goes next depends only on the square it is on and the roll, so the game is an absorbing Markov chain (Althoen, King and Schilling model the classic board as a 101-state chain, Mathematical Gazette 1993). Write E(s) for the average number of rolls still needed from square s. Then E(finish) = 0 and E(s) = 1 + the average of E over the squares one roll can lead to (after sliding or climbing). On a finite board from which the finish can always be reached, these equations have exactly one solution, the expected game length (proved; it is the fundamental-matrix formula for absorbing chains). Without snakes every move goes forward, so the values can be filled in one square at a time from the finish backwards; snakes make the equations depend on each other and they are solved together. For the 1952 Milton Bradley board (9 ladders, 10 snakes, one die, a roll past 100 leaves the counter where it is) the average is 39.225122 rolls, the figure IBM's Ponder This uses; this plan recomputes it. Three facts children find surprising, all computed here: without the 80 → 100 ladder the average jumps to about 59 rolls; the short snake 56 → 53 makes the game slightly *shorter* (removing it gives 39.239), because from 53 the long snake at 62 is out of reach of one roll; and a new ladder 74 → 81 would make the game *longer* (about 41.46), because it carries the counter past the 80 → 100 ladder. The same effect fits on a tiny strip: on squares 0 to 8 with a coin (tails one step, heads two, reaching or passing 8 finishes) and a ladder 2 → 8, a game averages 153/64 ≈ 2.39 tosses; adding a ladder 1 → 3 raises it to 89/32 ≈ 2.78. Game lengths spread widely and the mean sits above the median; there is no upper limit on a game's length, though games end with probability 1. House rules (extra rolls on a six, bouncing back from 100) change the numbers: one simulation with the six rules reports a mean of 42.7 rolls and a median of 34. Children can discover how much game lengths vary, that the average can be computed exactly by working back from the finish, and that a ladder is not always good news.

## Sources

Every link was opened and read on the date given; nothing is cited from memory or from a search snippet.

- [How long is a game of snakes and ladders?](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/03EFBC49CFB29C48B33AF04A794C7796/S0025557200152283a.pdf/div-class-title-how-long-is-a-game-of-snakes-and-ladders-div.pdf) S. C. Althoen, L. King and K. Schilling, The Mathematical Gazette 77 (March 1993), 71–76. The game as a 101-state absorbing Markov chain and its expected playing time (read November 4, 2026; first-page extract only, the article itself is paywalled).
- [Ponder This, February 2020](https://research.ibm.com/haifa/ponderthis/challenges/February2020.html). IBM Research. The rules with "stay put" on an overshoot and the standard board's expected 39.225122 moves; the challenge asks for a 10-jump board averaging 66.978705 (read November 4, 2026).
- [Snakes and ladders](https://freerangestats.info/blog/2024/08/10/snakes-and-ladders). Free Range Statistics blog, August 10, 2024. The full list of the board's 9 ladders and 10 snakes (matching Althoen et al.), and a 10,000-game simulation with six and bounce-back rules: mean 42.7 rolls, median 34, against 39.2 for the simplified chain (read November 4, 2026).
- Prior use with students: [Monte Carlo Simulation of Chutes and Ladders](https://serc.carleton.edu/teaching_computation/workshop_2019/activities/230840.html). Eric P. Choate, Radford University, SERC; upper-level undergraduates simulate the game and use a six-square version to see why going first matters (read November 4, 2026). No K–5 circle or classroom activity on game length was found (searched NRICH, which has track games for young children but none on game length, and circle handouts for Snakes and Ladders and Chutes and Ladders).

## A kid-friendly way in

Materials per pair: a printed 20-square strip board (squares 1–20 in two rows, start off the board) with ladders 3 → 11 and 8 → 15 and snakes 13 → 5 and 18 → 2 drawn on, a die, a counter, and linking cubes. For 4–5, a printed 9-cell strip (squares 0–8) with a coin. Class materials: a number line from 1 to 25 on the board for game lengths. Prep: print boards, about 15 minutes.

Launch (3 minutes): one child plays a game at the front while the class counts rolls; each roll adds a cube to a tower, and the finished tower goes on the class number line at its height. Rule shown once: reaching or passing 20 finishes.

## By band

- **K–1:** Play many games on the 20-square board, one cube per roll, and line the towers up shortest to tallest. What was the shortest game? Can anyone finish in fewer rolls? Then play with the snakes covered: are the towers shorter?
- **2–3:** Which square is the best one to stand on, and which the worst? Predict, then test by starting games from those squares. Remove one ladder or one snake: will games get longer or shorter, and by how much on the class line?
- **4–5:** On the coin strip, work backwards: from square 7 one toss always finishes; from square 6, half the time one toss, half the time two; keep going to square 0. Then draw a ladder 2 → 8 and recompute. Now add a second ladder 1 → 3: does the game get faster or slower, and why? Extension: the classic board's ladder 74 → 81 makes the game longer; find the reason on a picture of the board.

## Checked facts

- `check_week_173()`: classic board, stay-put rule: 39.225122 rolls; without the 80 → 100 ladder about 58.99; without the 56 → 53 snake 39.239 (longer); with an added ladder 74 → 81 about 41.458 (longer); removing any one of the nine ladders makes the game longer.
- `check_week_173()`: children's board (ladders 3 → 11, 8 → 15, snakes 13 → 5, 18 → 2, reach or pass 20): average about 7.01 rolls, median 6, shortest game 3 rolls with chance exactly 1/12, more than 15 rolls about 3.7%; the bare strip averages about 6.19 and the ladders-only board about 5.26; a seeded 4,000-game simulation agrees.
- `check_week_173()`: coin strip 0–8: working back gives 1, 3/2, 9/4, 23/8, 57/16 from squares 7, 6, 5, 4, 3; with ladder 2 → 8 the game averages 153/64 from square 0; adding ladder 1 → 3 makes it 89/32, longer.

## Nearest existing themes

Week 60 (Take it or pass) works backwards too, but there the player chooses and each step takes a maximum; here nobody chooses and each step takes an average plus one. Atlas AP-01 (a coin-toss walk to two shores) computes winning chances by balancing neighbours and notes that a ferry changes how long the walk lasts; this week makes that duration the main question. Draft 131 (collecting every sticker) adds up stage waits; Week 20 (Averaging) supplies the balancing idea. New here: expected game length as a system of equations on a board, the finish-backwards computation, and non-monotone effects (a ladder that lengthens, a snake that shortens).

## App connection

Region "Chance and machines", possible family "Board builder": a child places one extra ladder or snake on a small board and the machine plays 1,000 games and shows the average. Puzzle 1: "Add a ladder that makes the game longer." Puzzle 2: "Fill in the average number of tosses on each square of the strip, working back from the finish; the machine checks each number." The backward-values display of the "Take it or pass" family could carry Puzzle 2.

## Open questions

- Timing: a game on the 20-square board averages 7 rolls, so a pair can play perhaps 15 games in 20 minutes; is the class line plot dense enough to show the spread and the long tail?
- Whether 4–5 children can handle 9/4 and 23/8, or should work in "out of 16 games" counts instead of fractions.
- Whether to keep the classic-board facts as a guide story only, since checking them needs a computer.
- Rule clarity: "reaching or passing 20 finishes" differs from the home rule many children know (exact landing); the launch must show it.
