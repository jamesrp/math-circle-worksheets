# Week 158 (draft plan): Squares from two squares

**Strand:** number (Numbers). **Deep-math field:** number theory, Diophantine equations, involutions. **Status:** draft plan, November 2026. No student pages, guide, review card or pilot.

## The deep idea

Which totals can be built as two square arrays of tiles, such as 25 = 3 × 3 + 4 × 4? Up to 20 the totals 3, 6, 7, 11, 12, 14, 15 and 19 never work. Two facts organise the answer. First an obstruction anyone can prove with tiles: grouping the tiles of a square into fours leaves 0 over (even side) or 1 over (odd side), so two squares leave 0, 1 or 2 over and a total that leaves 3 (3, 7, 11, 15, 19, …) is impossible. Second, Fermat's two-squares theorem: an odd prime is a sum of two squares exactly when it leaves remainder 1 on division by 4 (5, 13, 17, 29, 37, 41, …), and then in only one way. The full rule for any whole number n is that each prime factor leaving remainder 3 on division by 4 must appear an even number of times (so 45 = 9 × 5 works as 36 + 9, but 21 = 3 × 7 does not); such numbers thin out, a vanishing proportion of all numbers (Landau and Ramanujan). The famous modern proof is Zagier's one-sentence proof (1990, condensing Heath-Brown's 1984 argument): a "windmill" for p is a central x × x square with four identical y × z rectangular arms, so x² + 4yz = p. The windmills come in pairs under one clever re-drawing (an involution), with exactly one windmill left unpaired, so their number is odd; swapping every windmill's arms from y × z to z × y is another pairing, and because the count is odd some windmill must be its own swap, with square arms y × y, and then p = x² + (2y)². For 13 the windmills are (x, y, z) = (1, 1, 3), (1, 3, 1), (3, 1, 1) and the symmetric one gives 13 = 3² + 2². Proved: everything above. Checked here on small cases: the windmill pairing for primes up to 97. Children can discover the never-works list, the "leave 3 after fours" obstruction, and (grades 4–5) build every windmill of 13 or 29 tiles and find the square-armed one.

## Sources

Every link was opened and read on the date given; nothing is cited from memory or from a search snippet.

- [Windmills of the minds: an algorithm for Fermat's Two Squares Theorem](https://arxiv.org/pdf/2112.02556) — Hing Lun Chan, arXiv 2112.02556 (CPP 2022). Zagier's one-sentence proof (1990) as a condensed version of Heath-Brown's 1984 proof; windmills as a central square with four identical rectangular arms, x² + 4yz; Spivak's 2007 geometric reading of the Zagier map (read November 4, 2026).
- [Zagier's "one-sentence proof" of Fermat's theorem on sums of two squares](https://leanprover-community.github.io/mathlib4_docs/Archive/ZagierTwoSquares.html) — Lean mathlib archive. The two involutions on x² + 4yz = p: the piecewise one with exactly one fixed point, and the swap (x, y, z) to (x, z, y) (read November 4, 2026).
- [A001481: Numbers that are the sum of 2 squares](https://oeis.org/A001481) — OEIS. The list from 0 to 64; the characterisation by primes 3 mod 4 to even powers; count below N asymptotic to a constant times N/√(log N) (read November 4, 2026).
- Prior use with children: [Sum of Squares game lesson plan, lower level](https://hiddenfigures.osu.edu/sites/default/files/2022-09/lesson_plan_-_svager_lower_level.pdf) — Ohio State lesson built around Thyrsa Frazier Svager's thesis, grades 3–7, about 90 minutes. Children race to match two square cards to number cards 1 to 50 and look for patterns in the misses (read November 4, 2026). Also [Sum of Two Squares discovery task](https://www.mcsoxford.org/wp-content/uploads/2020/05/9-Sum-of-Two-Squares_Worksheet.pdf) — Tim Elton, 2020, age not stated: write 1 to 40 as sums of two squares and look for a pattern in the failures (read November 4, 2026).

## A kid-friendly way in

Square tiles (or snap cubes laid flat) and a 1–50 class chart. Each pair builds two squares of any sizes (a single tile is a square; "no second square" is allowed and marked differently), counts the total and colours that square of the chart, keeping a photo or sketch of the build. Prep: about 100 tiles per pair, a large 1–50 chart and two marker colours; under 15 minutes. Launch (2–3 minutes): build a 3 × 3 and a 4 × 4 square side by side, count 25, colour 25; ask whether 25 can also be made another way (5 × 5 with no second square) and whether every number can be coloured.

## By band

- **K–1:** build squares of side 1, 2, 3 and 4 and pairs of them; count totals with an adult and colour the chart; notice the small numbers nobody can make (3, 6, 7).
- **2–3:** fill the chart to 50; which numbers have two different builds (25, 50)? Sort the never-works numbers into piles of 4 tiles and see what is left over; predict whether 43 and 47 can work.
- **4–5:** prove the "3 left over" obstruction by grouping each square's tiles in fours; test which primes work (5, 13, 17, 29, 37, 41 do; 3, 7, 11, 19, 23 do not); build every windmill of 13 tiles and of 29 tiles (centre square, four equal rectangle arms, counting a 1 × 3 arm and a 3 × 1 arm as different) and find the one with square arms. A further question for a return visit: 5 = 1 + 4 and 13 = 4 + 9, and 65 = 5 × 13 = 1 + 64 = 16 + 49.

## Checked facts

Computed in `check_number_symmetry_2.py`, `check_week_158()`:

- totals up to 50 that are a sum of two squares with 0 allowed (A001481), and the 18 that use two non-empty squares; the failures up to 20 are 3, 6, 7, 11, 12, 14, 15, 19;
- a square leaves 0 or 1 after grouping in fours; no number leaving 3 is a sum of two squares (checked to 2000);
- every odd prime below 3000 is a sum of two squares exactly when it leaves 1 after fours, and then in exactly one way; 13 = 4 + 9, 29 = 4 + 25;
- up to 50 only 25 and 50 have two builds; 45 = 36 + 9 works while 21, 43 and 47 do not; 5, 13, 17, 29, 37, 41 work and 3, 7, 11, 19, 23 do not;
- 25 = 0 + 25 = 9 + 16; 50 = 1 + 49 = 25 + 25 is the first total with two builds from two non-empty squares; 65 = 1 + 64 = 16 + 49;
- Zagier's map is an involution on the windmills of every prime 5 to 97 that leaves 1 after fours, with the single fixed point (1, 1, (p − 1)/4); the arm swap has exactly one fixed point and it gives p = x² + (2y)²; 13 has 3 windmills and 29 has 5.

## Nearest existing themes

Week 97 (square remainders) studies which remainders squares leave mod m; the "fours" obstruction here is its mod-4 case put to work on a new question. Week 96 (prime bags) supplies the factorisations the general rule needs. Week 111 draft (staircase numbers) is the nearest plan in format: a chart hunt for which totals are buildable, with an obstruction. The concept diophantine-equations is used only by atlas families (AD-10, AD-15, AD-16), not by any week; this would be its first week. Week 163 draft (arrow multiplication) is the natural sequel: 5 = (2 + i)(2 − i).

## App connection

Numbers region, a "two-square builder" family: drag two squares from a tray onto a target pad to hit a number, or press "impossible" and show the leftover after grouping in fours; puzzles: "make 50 in two different ways", "which of 41, 43, 45 cannot be made?", and for older players "build all windmills for 29 and find the one with square arms".

## Open questions

- The Fermat date and Euler's first proof are standard history but were not confirmed from a page read here; confirm before the guide states them.
- Whether "0 allowed" (one square alone) confuses the chart; the launch's 25 = 5 × 5 is meant to settle the convention. Untested.
- Windmill building needs 29 tiles per attempt and careful orientation; a printed windmill outline may be needed. The pairing itself is facilitator material, not a student task.
