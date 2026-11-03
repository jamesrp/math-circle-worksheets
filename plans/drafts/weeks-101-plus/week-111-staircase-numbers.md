# Week 111 (draft plan): Staircase numbers

**Strand:** number (Numbers). **Deep-math field:** elementary number theory, partitions. **Status:** draft plan, November 2026. No student pages, guide, review card or pilot.

## The deep idea

A staircase number (in the literature, a polite number) is a sum of two or more consecutive positive whole numbers, such as 9 = 4 + 5 = 2 + 3 + 4. Theorem (Sylvester, with Franklin, American Journal of Mathematics, 1882): a positive whole number is a staircase number exactly when it is not a power of 2, and the number of ways to write n as such a staircase equals the number of odd divisors of n greater than 1. The proof is a pairing that children can see with rods. A staircase of odd length k balances around its middle step, so n = k × (middle) and k is an odd divisor of n. A staircase of even length k pairs its steps from the outside in (first with last, second with second-to-last), each pair adding to the same odd number, so n = (k/2) × (odd pair total) and that pair total is an odd divisor of n. Conversely each odd divisor d > 1 gives exactly one staircase (as a length if d is small enough to fit, otherwise as a pair total), so the count matches. A power of 2 has no odd divisor above 1, so it has no staircase: 1, 2, 4, 8, 16, 32, 64 are the only failures up to 64. Below 100 the most staircases any number has is 5 (for 45, 63, 75, 90 and 99). Children can discover the failures experimentally, conjecture "powers of two", and explain the odd-length case by evening out a staircase into a rectangle. Everything here is proved; nothing is open.

## Sources

Every link was opened and read on the date given; nothing is cited from memory or from a search snippet.

- [Polite number](https://en.wikipedia.org/wiki/Polite_number) — Wikipedia, secondary pointer. States the characterization, politeness as the number of odd divisors above 1, and gives the Sylvester and Franklin 1882 reference and Mason 1912 (American Mathematical Monthly) (read November 3, 2026).
- [A001227: Number of odd divisors of n](https://oeis.org/A001227) — OEIS. Comment by Henry Bottomley (2000): also the number of partitions of n into consecutive positive integers, counting the one-term sum (read November 3, 2026).
- Prior use with children: [NRICH "Summing Consecutive Numbers"](https://nrich.maths.org/node/62188) — ages 11–14. Which numbers are sums of consecutive integers, which have several, and an extension proving 2^n cannot be (read November 3, 2026). Also the [NRICH Consecutive Sums poster](https://nrich.maths.org/sites/default/files/thumbnails/content-id-7999-NRICH-poster_ConsecutiveSums.pdf) asking "Which numbers can be written in more than one way?" (read November 3, 2026).

## A kid-friendly way in

Build staircases from Cuisenaire rods or snap-cube towers: steps of heights 2, 3, 4 stand side by side and make 9. Each table gets a target list (1 to 20) and tries to build each number as a staircase of two or more steps going up by one, recording wins on a shared class chart. Odd-length staircases can be "evened out" by moving cubes from the tall end to the short end to make a rectangle, which is the explanation in object form. Prep: one set of rods or 100 snap cubes per table, a large 1–30 chart on the board; about 10 minutes. Launch (2–3 minutes): build 9 as 4 + 5 and as 2 + 3 + 4 with big cubes, show that 3 + 5 is not a staircase (it skips a step), and ask tables to fill the chart.

## By band

- **K–1:** build staircases with two steps (always an odd total) and three steps from cubes, and post them on the chart; notice which numbers on the chart nobody can build.
- **2–3:** fill the chart from 1 to 30; which numbers have no staircase, which have two or three? Make a prediction for 32 and 40 and test it.
- **4–5:** why a three-step staircase is three times its middle (even it out); why a power of 2 can never work; match each staircase of 15 (7 + 8, 4 + 5 + 6, 1 + 2 + 3 + 4 + 5) to an odd divisor (3, 5, 15) and look for the rule that counts staircases.

## Checked facts

Computed in `check_number.py`, `check_week_111()`:

- for every n from 1 to 512, the number of staircases equals the number of odd divisors above 1, and is zero exactly for powers of 2;
- the non-staircase numbers up to 64 are 1, 2, 4, 8, 16, 32, 64 (up to 20: 1, 2, 4, 8, 16);
- 15 = 1 + 2 + 3 + 4 + 5 = 4 + 5 + 6 = 7 + 8; 9 has two staircases; 30 has three;
- below 100 the maximum number of staircases is 5, reached by 45, 63, 75, 90, 99;
- every odd 2m + 1 is m + (m + 1); three-step staircases give exactly the multiples of 3 from 6;
- the pairing: tagging each staircase by its length (if odd) or by 2n/length (if even) gives each odd divisor above 1 exactly once, for every n from 3 to 299.

## Nearest existing themes

Year 1 Handouts 1 used figurate numbers, and Week 89 (growing shapes and totals) proves 1 + … + n = n(n + 1)/2 with two staircases; those staircases start at 1, while here they may start anywhere and the question is which totals occur. Week 54 (partitions and rebuilding) uses the split n = 2^a × odd in Euler's odd-distinct bijection, and Week 96 (prime bags) counts divisors; the new theorem here is the odd-divisor count and the power-of-2 obstruction. The grades 2–3 plan notes that triangular numbers were less engaging for one group; the open-ended chart hunt is meant to be the draw, not the sequence. Overlap with Week 89 is real in materials, so the guide should avoid re-proving the triangle formula.

## App connection

Numbers region, a "staircase builder" family: drag blocks into consecutive steps to hit a target, or prove a target impossible by filling the chart; puzzles: "build 21 in three different ways", "which of 24, 28, 32 has no staircase?" Could share a board with an existing block-stacking family if one exists.

## Open questions

- Whether children read "consecutive" reliably; the launch's 3 + 5 non-example is meant to cover this. Untested.
- Rod sets top out at 10, so staircases for numbers above about 30 need cubes or drawings.
- Whether 4–5 reach the odd-divisor count in one session or need a return visit.
