# Week 189 (draft plan): Guessing your own hat

**Strand:** logic (Codes and logic). **Deep-math field:** coding theory, probability by counting, cooperative games. **Status:** draft plan, November 2026. No student pages, guide, review card or pilot.

## The deep idea

Ebert's hat game (Todd Ebert's 1998 PhD thesis; popularised by Sara Robinson in the New York Times, 2001): n players each get a red or blue hat by a fair coin; each sees every hat but their own; with no signals, all at once, each player says a colour or passes. The team wins if at least one player guesses and nobody guesses wrong. The key fact is a balance that no strategy can escape: a player's own hat is independent of what they see, so over all 2^n equally likely hat rows, every strategy makes exactly as many right guesses as wrong ones (proved; checked here over every strategy for two and three players). The team cannot make guessing more accurate; it can only arrange where the guesses fall. A good strategy spreads right guesses thinly (one right guess in each winning row) and piles wrong guesses together (everyone wrong in the same few rows). Since a losing row holds at most n wrong guesses, wins are at most n times losses, so the chance of winning is at most n/(n + 1) (proved by this count). Three players: pass if the two hats you see differ; if they match, guess the other colour. The team wins in the 6 rows with a 2-to-1 split and loses only in the 2 single-colour rows, where all three are wrong: 3/4, which meets the bound, and an exhaustive search confirms nothing does better. For n = 2^k − 1 players a Hamming-code strategy (number the players 1 to n; treat the rows whose red players' numbers have binary XOR 0 as "codewords"; guess only when your hat could make the row a codeword, choosing the colour that would not) wins with chance 1 − 1/2^k: 7/8 for seven players (checked: 112 of 128 rows). The bound n/(n + 1) is reached exactly when a perfect one-error-correcting code exists (Paterson and Stinson, citing the standard argument); for other n the best strategies come from covering codes, and in 2001 the optimum for every n was reported unknown. Children can discover the 3/4 strategy, that "everyone always guesses" wins only 1/8, and, at 4–5, the balance argument for why 3/4 cannot be beaten.

## Sources

Every link was opened and read on the date given; nothing is cited from memory or from a search snippet.

- [Why Mathematicians Now Care About Their Hat Color](https://barry.ece.gatech.edu/6602/handouts/hatcolor.pdf) — Sara Robinson, The New York Times, April 10, 2001, course handout copy (read November 4, 2026). Ebert's 1998 thesis as the origin, the three-player strategy and 3/4, the Hamming-code strategy with 1 − 1/2^k for 2^k − 1 players, and that optimal strategies for all n were then unknown.
- [Yet Another Hat Game](https://www.combinatorics.org/ojs/index.php/eljc/article/download/v17i1r86/pdf) — Maura B. Paterson and Douglas R. Stinson, Electronic Journal of Combinatorics 17, #R86, 2010 (read November 4, 2026). The 6/8 count; "the six correct guesses occurred in six different cases, while the six incorrect guesses were squeezed into two cases"; 1 − 1/(n + 1) attained only when a perfect code exists.
- [A Hat Trick of Hat Puzzles](https://www.quantamagazine.org/a-hat-trick-of-hat-puzzles-20160309/) — Pradeep Mutalik, Quanta Magazine, March 9, 2016 (read November 4, 2026). A general-audience version with a pass option and the link to Hamming codes.
- Prior use with children: [Teamwork Puzzles](https://sites.math.washington.edu/~mathcircle/circle/files/26sp-week21.pdf) — UW Math Circle, Week 21 (level not stated) (read November 4, 2026): the guess-or-pass game played in a circle of three students with hats placed by the instructor (Problems 11 and 12). [Junior hat problems](https://bpb-us-e2.wpmucdn.com/sites.wustl.edu/dist/b/4012/files/2023/02/2013-10-20-junior-hat_problems.pdf) — Math Circle at Washington University in St. Louis, October 20 (read November 4, 2026): a two-player guess-or-pass game and other hat problems. No K–5 use was found.

## A kid-friendly way in

Play first, then turn chance into counting. Three players wear Week 84's headbands with a red or blue card; an adult draws each card from a bag behind their backs. On "one, two, three" each player holds up a red card, a blue card or a white "pass" card. Tables play ten rounds with no plan, then plan a rule together. Then the counting tool: a deck of the 8 "hat row" cards (three faces, all colourings), which children sort into win and lose piles under their rule, and on which they put a green dot for every right guess and a red dot for every wrong one. Prep: 3 headbands and 12 colour cards per table, a bag, and the printed 8-card hat-row deck per table; about 20 minutes. Launch (3 minutes): two volunteers play the two-player game in front of the room; the room watches that "both guess" often loses and asks whether passing can help.

## By band

- **K–1:** Two players, then three: play, and with an adult, sort the 8 hat-row cards under the rule "always guess red" and under the team's own rule. Count the win pile with cubes. No reading.
- **2–3:** Find a three-player rule that wins as many of the 8 rows as possible. Dot every right and wrong guess on the cards. Do some rules make more right guesses than wrong ones? Tables pool their best scores (6 of 8 is the record).
- **4–5:** Explain why no rule wins 7 of 8: right and wrong dots always balance, each losing row holds at most 3 red dots, so wins are at most 3 times losses. Then seven players: an adult hands out the Hamming numbering as a recipe and the table checks a few rows (the full 128-row count is the facilitator's).

## Checked facts

All in `check_logic_3.py`, function `check_week_189()`:
- Three players with the pass-if-different rule: 6 wins of 8 rows; 6 right and 6 wrong guesses, the wrong ones all in the two single-colour rows.
- Exhaustive search over every guess-or-pass strategy: best 2 of 4 rows for two players and 6 of 8 for three; in every strategy right guesses equal wrong guesses.
- Seven players with the Hamming rule: 112 of 128 rows, 7/8, with 112 right and 112 wrong guesses; 3/4, 7/8 and 15/16 equal n/(n + 1) for n = 3, 7, 15.
- All three always guessing: 1/8.
- Cited, not computed: optimality of the Hamming strategy for all n = 2^k − 1 and the perfect-code condition (Paterson and Stinson); the 2001 status of other n (Robinson).

## Nearest existing themes

Week 84 (Public knowledge) uses the same headbands, but there children deduce their colour round by round from announcements; here no one can know their colour and the question is a team's odds. Week 18 (Hidden changes) teaches distance-3 codes directly, and the seven-player strategy is exactly a perfect one-error-correcting code, so the 4–5 seven-player step repeats Week 18's mathematics and should be framed as a return to it rather than taught afresh. The topic-scouting README set aside "Hat-colour parity strategies" because of Week 84 and Week 18; this plan answers that by centring a different idea: the balance of right and wrong guesses, the counting bound n/(n + 1), and the 8-card sort that gives K–1 an entry. Week 6 (Code breaking) shares the "count all the cases" move. New: a cooperative game whose whole strategy is where to put the inevitable wrong guesses.

## App connection

Codes and logic region, possible family "Hat team": three (later seven) faces on the board; for each view a player can have, the child taps red, blue or pass; Play runs all 8 rows and colours the win and lose rows, with right and wrong guesses as dots. Puzzles: "Win 6 of the 8 rows"; "Can any rule win 7?" (a counter shows right and wrong dots always equal); "Make a rule that loses in only one row" (impossible for three). Week 84's "Who knows" family could share the headband art.

## Open questions

- Do K–1 children understand that the 8 cards stand for all the ways the bag could deal, or does the card sort feel unrelated to the game? Rehearse the bridge from play to cards.
- Simultaneous guessing is easy to break by peeking at a teammate's card; a reveal on "three" behind folders may be needed.
- Is the 4–5 balance argument (every guess is right exactly half the time over the 8 cards) graspable from the dotted cards alone?
- Whether the seven-player step belongs here or in a Week 18 return visit.
