# Math review: Week 66 K–1 draft (GGT66-K-v1)

Reviewed: `draft/k-1.pdf` (8 pages, Problems 1–8) and `draft/src/`.

## Verdict

**The K–1 band checks out completely. I found no mathematical problems.** Every printed target, every arrow and every tower matches the intended mathematics. Every fewest-move count is correct. Each "which one" question has a single answer, and each "every way" or "circle every tower" task has the count the page implies.

## How it was checked

I did not import or trust the author's code or comments.

- **What the page shows.** `math-check/parse_tex.py` reads the generated `k-1.tex` coordinates directly. For each target picture it extracts the lamp circles and their fills, the walker glyph's x-position, the home mark, the frame, the record squares, the arrow labels, and the tower cubes with their labels. Every target picture has 7 lamps on equal pitch with the home mark under the middle lamp. Every walker sits exactly over a lamp (integer place). Lit lamps are filled and unlit lamps are open.
- **Draft PDF matches its source.** I recompiled a copy of `k-1.tex` in `math-check/build/`. Its pages match the draft PDF pixel for pixel on all 8 pages, so the parsed coordinates are what is printed. I also inspected every rendered page by eye against the parse.
- **Fewest moves.** `math-check/verify.py` runs breadth-first search from the dark street with the walker at home, on the seven-lamp street (places −3…3) and on a long street (−9…9). The two agree on all 896 seven-lamp targets, so the street's ends never change an answer.
- **Shortest words.** Shortest words were listed by brute-force enumeration. Exact-length counts for Problem 8 come from a separate dynamic-programming count, on both streets.
- **Problems 6 and 7.** For each arrow I checked that the picture at its head is the picture at its tail after that one labelled move.

## Answer key (verified)

Places are numbered from home (0) in this key only. The pages show them by picture.

| Problem | Picture (lit lamps; walker) | Fewest | Notes |
|---|---|---|---|
| 1 | {0}; 0 | 1 | F |
| 1 | none; −2 | 2 | LL |
| 1 | {2}; 2 | 3 | RRF |
| 1 | {−3}; −3 | 4 | LLLF |
| 2 | {2}; 3 / 1 / 0 / −1 | 4 / 4 / 5 / 6 | RRFR, RRFL, RRFLL, RRFLLL |
| 3 | {1,2}; 2 | 4 | RFRF |
| 3 | {−1,2}; 2 | 6 | LFRRRF (right first: 10) |
| 3 | {−3,1}; −3 | 7 | RFLLLLF (left first: 13) |
| 3 | {−2,3}; 3 | 9 | LLFRRRRRF (right first: 15) |
| 4 | {−2,1}; 1 / 0 / −1 / −2 | 7 / 8 / 7 / 6 | for walker at 0, both orders take 8 |
| 5 | {0,1}; 0 | 4 | exactly 2 shortest ways: FRFL, RFLF |
| 5 | {0,1,2}; 0 | 7 | exactly 4 shortest ways: FRFRFLL, FRRFLFL, RFRFLLF, RRFLFLF |
| 6 | left {−2,−1}; −1 → L, R, F | 5 → 4, 6, 4 | most: the R picture (6), unique |
| 7 | left {−1,0,2}; 0 → L, R, F | 9 → 8, 8, 8 | most: the left picture (9), unique. This is a dead end. |
| 8 | {0}; 0, towers 1–4 | 1 | towers that work: 1 and 3 (1 and 5 words); 2 and 4 have none |
| 8 | dark street; 0, towers 1–4 | 0 | towers that work: 2 and 4 (3 and 15 words); 1 and 3 have none |
| 8 | {1}; −1, towers 4–7 | 4 | towers that work: 4 and 6 (1 and 12 words); 5 and 7 have none |

- **Problem 7.** The search independently confirms that the dead ends with fewest ≤ 9 are {−1,0,1}, {−2,0,1} and {−1,0,2}, each with the walker home. Problem 7 uses {−1,0,2}, not the older packet's {−1,0,1}.
- **Record squares.** The largest fewest count on any picture with record squares is 9. Each picture has 12 squares.
- **Problem 8 towers.** The printed towers have exactly 1, 2, 3, 4 / 1, 2, 3, 4 / 4, 5, 6, 7 cubes, matching their numerals.

## Alternative readings and edge cases considered (no change needed)

- **"From a dark street" in Problems 6 and 7.** The arrows show one-move changes. The text says to build each picture "from a dark street", which rules out counting from the left picture. Read as written, with all four pictures (each has its own record squares), the answer is unique in both problems. Only if a reader dropped the left picture from "each picture" would Problem 7 become a three-way tie at 8. The wording does not invite that reading.
- **Problem 5's answer lines.** Both pictures get five lines. That is more than the number of ways (2 and 4), and the lines are the same for both pictures, so they do not signal a count.
- **Pictures that need no lamp or are already built.** Problem 1's picture with no lamp lit can be built (LL). Problem 8's dark-street picture has no tower of 0, and its towers 2 and 4 work (LR, RL, FF, …).
- **The street's ends.** No shortest route or exact-length build needs a step past either end of the seven-lamp street. The counts are identical on the long street.
- **Mirror pictures.** A child who confuses left and right gets the same counts, because every count is symmetric.
- **Cube supply.** No single build needs more than a pair's two dozen cubes; a right-first attempt at Problem 3's 9-move picture uses 15. Standing all four Problem 7 towers at once would take 9 + 8 + 8 + 8 = 33 cubes. The page avoids that by recording counts in the squares, so comparing never needs standing towers.
