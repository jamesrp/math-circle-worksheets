# Week 109 (draft plan): Sharing loaves the Egyptian way

**Strand:** number (Numbers). **Deep-math field:** elementary number theory, algorithms. **Status:** draft plan, November 2026. No student pages, guide, review card or pilot.

## The deep idea

An Egyptian fraction writes a fraction as a sum of different unit fractions (numerator 1), as scribes did in the Rhind Mathematical Papyrus (about 1550 BCE), whose opening table gives 2/n for odd n from 5 to 101. Theorem (proved): every fraction a/b between 0 and 1 has such a representation. The greedy method, described by Fibonacci in 1202 and rediscovered by Sylvester in 1880, takes the largest unit fraction 1/d not exceeding the current remainder and repeats. It always stops, because subtracting 1/d with d = ⌈b/a⌉ leaves (ad − b)/(bd) and ad − b < a: the numerator strictly drops (a monovariant), so there are at most a terms, and the denominators strictly increase, so no piece repeats. Greedy is not the shortest or the tamest: 5/121 = 1/33 + 1/121 + 1/363, yet greedy produces five terms, the last with a 25-digit denominator. The splitting identity 1/n = 1/(n + 1) + 1/(n(n + 1)) shows representations are never unique, and for odd n = 2m + 1 gives 2/n = 1/(m + 1) + 1/(n(m + 1)) in two pieces. Open: the Erdős–Straus conjecture (1948) that for every n ≥ 2, 4/n = 1/a + 1/b + 1/c with positive whole a, b, c. It has been checked by computer for all n up to 10^17 (Salez 2014) and, per a 2025 preprint, for primes up to 10^18; no proof is known. Children can discover that fair sharing with whole and unit pieces always works, that their chosen method must stop, and that different sharings of the same amount exist.

## Sources

Every link was opened and read on the date given; nothing is cited from memory or from a search snippet.

- [Egyptian Fractions](https://fibonacci-numbers.surrey.ac.uk/Fractions/egyptian.html) — Ron Knott's Fibonacci pages, University of Surrey. The loaf-sharing story (5 loaves for 8 workers as 1/2 + 1/8), the greedy method attributed to Fibonacci with the example 521/1050 = 1/3 + 1/7 + 1/50, and puzzles pitched at ages 8–10 (read November 3, 2026).
- [Algorithms for Egyptian Fractions](https://ics.uci.edu/~eppstein/numth/egypt/approx.html) — page on David Eppstein's UC Irvine site (the page names no author). Why greedy terminates: the numerator decreases and denominators increase (read November 3, 2026).
- [Further verification and empirical evidence for the Erdős-Straus conjecture](https://arxiv.org/html/2509.00128v1) — Mihnea and Dumitru, arXiv 2509.00128, 2025. Verification for primes up to 10^18 and the earlier 10^17 bound of Salez (2014) (read November 3, 2026).
- Prior use with children: [NRICH "Egyptian Fractions"](https://nrich.maths.org/1173) — ages 11–14. Rhind papyrus 2/n table for odd n from 5 to 101, the splitting identity and the two-piece 2/n method (read November 3, 2026).

## A kid-friendly way in

Share paper "loaves" (paper strips or paper plates) fairly among paper "workers", with the Egyptian rule that each worker's share must be made from pieces of different sizes, each piece being "one of k equal parts" of a loaf. Children fold and cut: 3 loaves for 4 workers is half a loaf plus a quarter each; 2 loaves for 3 workers is a half plus a sixth. A set of fraction strips (halves, thirds, quarters, sixths, twelfths) lets them test sums by laying pieces end to end against a whole strip. Prep: copy fraction strips on card, cut 30 paper loaves; about 20 minutes. Launch (2–3 minutes): share 3 loaves among 4 volunteers with real folding, showing first the "cut every loaf into quarters" way and then the half-plus-quarter way, and ask which the Egyptians would accept.

## By band

- **K–1:** physical sharing only: 2 loaves for 3, 3 for 4, 5 for 6 (half plus third). Fold and cut, then check by stacking each worker's pieces on one whole loaf.
- **2–3:** which twelfths can be built from one each of 1/2, 1/3, 1/4, 1/6 and 1/12 strips? (All of 1/12 to 11/12.) Then 4 loaves for 5 workers and 9 for 10; compare shares found by different tables.
- **4–5:** the greedy rule as a machine; why it always stops (track the numerator); 5/121 as a surprise; one-line challenge "write 4/n as three unit fractions" for n up to 20, with the news that nobody can prove it always works.

## Checked facts

Computed in `check_number.py`, `check_week_109()`:

- greedy expansions: 3/4 = 1/2 + 1/4; 4/5 = 1/2 + 1/4 + 1/20; 5/8 = 1/2 + 1/8; 2/5 = 1/3 + 1/15; 3/7 = 1/3 + 1/11 + 1/231; 9/10 = 1/2 + 1/3 + 1/15; 521/1050 = 1/3 + 1/7 + 1/50; 5/121 in five greedy terms ending with 1/1527612795642093418846225;
- loaf identities 2/3 = 1/2 + 1/6, 3/5 = 1/2 + 1/10, 5/6 = 1/2 + 1/3, 9/10 = 2/3 + 1/5 + 1/30, 2/7 = 1/4 + 1/28;
- the splitting identity for n < 200 and the two-piece formula for odd n < 200;
- the numerator monovariant and the at-most-a-terms bound for every a/b with b < 60;
- all eleven twelfths are sums of distinct strips from 1/2, 1/3, 1/4, 1/6, 1/12;
- a three-term 4/n exists for every n from 2 to 120 (e.g. 4/7 = 1/2 + 1/15 + 1/210).

- 5/121 = 1/33 + 1/121 + 1/363.

Cited, not computed: the papyrus table range and the 10^17 and 10^18 verification bounds. The historical dates (Fibonacci 1202, Sylvester 1880, Erdős–Straus 1948, Rhind about 1550 BCE) are standard but were not confirmed in the pages read here; check them before a guide.

## Nearest existing themes

Week 58 (fair division) is about fairness between people with different values; here all pieces are valued by size and the question is representation. Week 29 (two-length builders) and Week 30 (two-pan weight kits) also ask which totals a kit of sizes can make. New here: unit fractions, a terminating algorithm proved by a monovariant, and an open conjecture with a hands-on statement.

## App connection

Numbers region, a new family "loaf sharing": drag unit-fraction pieces onto workers' plates so every plate matches, with distinct sizes per plate; puzzles: "share 4 loaves among 5 using the fewest cuts" or "make 7/12 from different strips". A greedy-machine puzzle could show the remainder shrinking step by step.

## Open questions

- Cutting accuracy: folded thirds and fifths are hard for young children; pre-scored loaves may be needed. Untested.
- Whether reading fractions in written form is needed at all in 2–3, or strips alone suffice.
- Whether the 4–5 "why it stops" argument is reachable with strips, or needs written fractions.
