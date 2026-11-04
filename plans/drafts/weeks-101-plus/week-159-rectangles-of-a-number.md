# Week 159 (draft plan): Rectangles of a number

**Strand:** number (Numbers). **Deep-math field:** elementary number theory, divisor sums, Mersenne primes. **Status:** draft plan, November 2026. No student pages, guide, review card or pilot.

## The deep idea

Every way to lay n square tiles as a full rectangle is a factor pair, so the rectangles of n list its divisors: 12 gives 1 × 12, 2 × 6 and 3 × 4, so its divisors are 1, 2, 3, 4, 6, 12. A number is perfect when its proper divisors (all but itself) add up to it, as 1 + 2 + 3 = 6 and 1 + 2 + 4 + 7 + 14 = 28; abundant when they add to more (12: 1 + 2 + 3 + 4 + 6 = 16) and deficient when they add to less (every prime, and every power of 2, which misses by exactly 1). The Euclid–Euler theorem says the even perfect numbers are exactly 2^(p−1) × (2^p − 1) with 2^p − 1 prime (a Mersenne prime): Euclid proved these are perfect, and Euler, about two thousand years later, proved every even perfect number has this form. So the doubling sums 1 + 2 = 3, 1 + 2 + 4 = 7, 1 + 2 + 4 + 8 + 16 = 31, when prime, give 6, 28 and 496, while 1 + 2 + 4 + 8 = 15 is not prime and 15 × 8 = 120 is abundant. As of the 2024 discovery of 2^136,279,841 − 1, 52 Mersenne primes, and so 52 even perfect numbers, are known; whether there are infinitely many is open. Whether any odd perfect number exists is one of the oldest open problems in mathematics: none has been found, and Ochem and Rao (2012) proved one would exceed 10^1500 and have at least 101 prime factors counted with repetition. Among 1 to 100 there are 76 deficient, 22 abundant and 2 perfect numbers, and the smallest odd abundant number is 945. Children can discover that rectangles come in pairs except the square one, that primes have one rectangle, that perfect numbers are rare, and (grades 4–5) the doubling pattern behind 6, 28 and 496.

## Sources

Every link was opened and read on the date given; nothing is cited from memory or from a search snippet.

- [Even Perfect Number](https://mathworld.wolfram.com/EvenPerfectNumber.html) — Eric Weisstein, MathWorld. The Euclid–Euler theorem in the form 2^(p−1)(2^p − 1) with 2^p − 1 a Mersenne prime, citing Dickson's History; "All known perfect numbers are even" (read November 4, 2026). The companion [Odd Perfect Number](https://mathworld.wolfram.com/OddPerfectNumber.html) page says it is not known whether any exist and reports a 2026 extension of the lower bound to 10^2200 by Ochem, which I have not checked against a paper (read November 4, 2026).
- [Odd perfect numbers are greater than 10^1500](https://www.ams.org/mcom/2012-81-279/S0025-5718-2012-02563-4/) — Pascal Ochem and Michaël Rao, Mathematics of Computation 81 (2012), 1869–1877. The bound, at least 101 prime factors with multiplicity, largest component above 10^62 (read November 4, 2026).
- [Amateur mathematician discovers the largest known prime number](https://www.smithsonianmag.com/smart-news/amateur-mathematician-discovers-the-largest-known-prime-number-with-more-than-41-million-digits-180985321/) — Smithsonian Magazine, October 2024. 2^136,279,841 − 1, the 52nd known Mersenne prime, found by Luke Durant through GIMPS, 41,024,320 digits (read November 4, 2026).
- Prior use with children: [How many Rectangles?](https://polypad.amplify.com/lesson/how-many-rectangles) — Polypad lesson (grade level not stated, elementary in content). Find every rectangle for a number of tiles; primes give only two (counting turns), squares an odd number (read November 4, 2026). Also [Deficient, Perfect and Abundant Numbers](https://www.mcsoxford.org/wp-content/uploads/2020/05/Comp-3-Perfect-Abundant-and-Deficient-numbers_Worksheet.pdf) — Tim Elton, 2020, a comprehension task classifying 15, finding 28 among 26 to 30 and classifying 945 (read November 4, 2026).

## A kid-friendly way in

Square tiles and a "rectangle gallery". Each pair takes a number card (6, 7, 8, 12, 15, 16, 18, 20, 24, 28, 30, 36), builds every rectangle it can from that many tiles, and traces each onto squared paper for the gallery wall. Then the "short side tower": stack one cube tower for each different side length in the gallery, except the number itself, and stand the joined tower next to a tower of n cubes. Taller, shorter or exactly level sorts the numbers as abundant, deficient or perfect. Prep: 40 tiles and 60 snap cubes per pair, number cards, squared paper; about 15 minutes. Launch (2–3 minutes): build 1 × 6 and 2 × 3 from 6 tiles, ask for more (a turned rectangle is the same one), list the sides 1, 2, 3, 6, stack 1 + 2 + 3 next to 6 and show they are level.

## By band

- **K–1:** build every rectangle from 6, 7, 8 and 12 tiles; notice 7 makes only a line; compare towers for 6 (level) and 8 (short) with an adult helping list the sides.
- **2–3:** build galleries for numbers to 30, share them on the wall, and sort every number as short, level or tall; find the second perfect number (28); which numbers have the most rectangles (up to 50: 36 and 48, with 5 each)?
- **4–5:** why does each rectangle give two side lengths except the square? Look at 6 = 2 × 3 and 28 = 4 × 7 and the doubling sums 1 + 2 = 3, 1 + 2 + 4 = 7; predict the next perfect number from 1 + 2 + 4 + 8 + 16 = 31 (496) and test why 15 fails (120 is abundant). Hear that nobody knows if an odd perfect number exists.

## Checked facts

Computed in `check_number_symmetry_2.py`, `check_week_159()`:

- rectangles of 12 (3), 24 (4), 36 (5, one square); up to 50 the most is 5, for 36 and 48; one rectangle exactly for 1 and the primes (to 200); an odd number of divisors exactly for squares (to 500);
- perfect numbers below 10000: 6, 28, 496, 8128; Euclid's formula gives 6, 28, 496, 8128, 33550336 for p up to 13; 2^11 − 1 = 2047 = 23 × 89;
- abundant numbers to 30: 12, 18, 20, 24, 30; proper divisor sums of 12, 15, 28 are 16, 9, 28; 1 to 100 has 76 deficient, 22 abundant, 2 perfect; the smallest odd abundant number is 945; every multiple of 6 from 12 to 3000 is abundant; 2^k misses by 1;
- the numbers below 100 whose only rectangles are a line and a square are 4, 9, 25, 49; below 30, 24 has the largest excess (36, 12 above itself);
- 120 has proper divisor sum 240; 496 = 31 × 16; 6, 28 and 496 are also 1 + 2 + 3, 1 + … + 7 and 1 + … + 31.

The count of known Mersenne primes and the odd perfect bound are cited to the sources above.

## Nearest existing themes

Week 96 (prime bags) counts divisors as sub-bags of a prime factorisation; Year 1's divisor toggling (lockers left open exactly at square numbers) used the pairing of divisors; Week 32 (squares inside rectangles) is about common divisors of two sides. The rectangle gallery itself is common classroom material and repeats those weeks' representation. What is new is adding divisors rather than counting them, the abundant/deficient/perfect sort, the Euclid–Euler theorem and two genuinely open problems. A reviewer should decide whether this is a full week or a return visit to Week 96; I lean to a full week for grades 2–5 with the gallery as a quick K–1 entry.

## App connection

Numbers region, a "rectangle gallery" family: drag tiles into rectangles until the gallery is complete (the board rejects repeats and turned copies), then a tower-compare step that sorts the number; puzzles: "find a number whose only rectangles are a line and a square" (a prime times itself: 4, 9, 25, 49), "which number below 30 makes the tallest tower above itself?" (24, whose tower of 36 is 12 taller).

## Open questions

- The tower comparison for 24 needs 60 cubes (a joined tower of 36 beside a tower of 24); numbers above 30 should be compared on paper.
- Whether "short side tower" reads as adding proper divisors or invites counting rectangles; the launch should show both lists side by side. Untested.
- Euclid's and Euler's contributions are taken from MathWorld's statement of the theorem; confirm Elements IX.36 and Euler's date from a primary or historical source before the guide names them.
