# Week 157 (draft plan): Remainders that repeat

**Strand:** number (Numbers). **Deep-math field:** elementary number theory, multiplicative order, primitive roots. **Status:** draft plan, November 2026. No student pages, guide, review card or pilot.

## The deep idea

Share 1 among 7 by long division and the remainders run 1, 3, 2, 6, 4, 5, 1, so the digits 142857 repeat forever. The reason is a theorem children can act out: each step multiplies the remainder by 10 and keeps what is left after sharing among 7, so the next remainder depends only on the current one, and with only six possible non-zero remainders one must come back (the pigeonhole principle). For a prime p other than 2 and 5 the decimal of 1/p is purely periodic, and its period is the multiplicative order of 10 mod p, the least k with 10^k leaving remainder 1 on division by p; the period always divides p − 1 (Fermat's little theorem, or Lagrange's theorem applied to the remainders 1 to p − 1 under multiplication). The period is p − 1, the most possible, exactly when 10 is a primitive root mod p; below 100 this happens for 7, 17, 19, 23, 29, 47, 59, 61 and 97 (the full-reptend primes). Then the remainders visit every number from 1 to p − 1, so k/p reads the same cycle of digits from a different starting place, which is why 142857 × 2, × 3, …, × 6 are rotations of 142857 and 142857 × 7 = 999999. When the period is shorter the remainders split into several equal wheels: 1/13 has period 6, so its 12 remainders form two wheels of 6, and 1/41 has period 5, so 40 remainders form 8 wheels. All of this is proved. What is open is Artin's primitive root conjecture (1927): 10 should be a primitive root for infinitely many primes, so there should be infinitely many cyclic numbers. Hooley proved it in 1967 assuming the generalized Riemann hypothesis; unconditionally, Heath-Brown (1986) showed there are at most two exceptional primes, yet no single integer is known to be a primitive root for infinitely many primes. Children can discover the repeat, the wheel, the rotating digits and the "period divides p − 1" pattern from a table.

## Sources

Every link was opened and read on the date given; nothing is cited from memory or from a search snippet.

- [Artin's primitive root conjecture: a survey](https://arxiv.org/pdf/math/0412262) — Pieter Moree, arXiv math/0412262 (published in Integers, 2012). Gauss's study of the period of 1/p as the order of 10 mod p; maximal period exactly when 10 is a primitive root; Hooley's 1967 proof under GRH; Heath-Brown's 1986 "at most two exceptional primes"; "There is no known number g for which P(g) is known to be infinite" (read November 4, 2026).
- [A001913: Full reptend primes: primes with primitive root 10](https://oeis.org/A001913) — OEIS. The list 7, 17, 19, 23, 29, 47, 59, 61, 97, …; the cyclic numbers (10^(p−1) − 1)/p (read November 4, 2026).
- Prior use with children: [Expanding Fractions I](https://mathcircle.berkeley.edu/sites/default/files/handouts/2020/Beginners%20I-II_Expanding%20Fractions%20I_0.pdf) — Roy Zhao, Berkeley Math Circle Beginners, spring 2020. Long division of 1/7 by hand, remainder wheels for 7 and 13, the multiplier that moves round the wheel, and the denominator-to-period relationship for 1/37 and 1/41 (read November 4, 2026).
- [Repeating Decimals I](https://archive.mathteacherscircle.org/assets/session-materials/EJohnstonRepeating%20Decimals%20I.pdf) — Math Teachers' Circle session materials (author not named on the page). Remainders 1 to 12 for 13 must repeat; k/7 reuses the 1/7 cycle; 1/41 gives a period of 5 and 8 wheels (read November 4, 2026).

## A kid-friendly way in

Cookie sharing with counters and seven paper plates. Start with 1 "big cookie" traded for 10 counters ("tenths"); deal them round the 7 plates; each plate gets 1 and 3 are left. Trade each leftover for 10 smaller counters (30 counters) and deal again: 4 each, 2 left. Record each round as one card showing "each plate got" and "left over". Within six rounds the leftover is 1 again, and children see that the next round must copy the first. Then the remainder wheel: seven spots labelled 0 to 6 on a paper circle, an arrow from each leftover to the next one. Prep: 60 counters and 7 paper plates per table, a printed wheel with 7, 13 and 17 spots, a record strip; about 15 minutes. Launch (2–3 minutes): deal 10 counters onto 7 plates with everyone watching, write "1 each, 3 left", trade the 3 for 30 and ask the room what happens next.

## By band

- **K–1:** deal 10, 20, 30, … counters onto 7 plates with an adult recording; predict the leftover; notice "we had 1 left before" and that the cards start repeating. Dealing onto 3 plates (always 3 each, 1 left) is a quick first contrast.
- **2–3:** run the sharing for 7 and for 13 plates using the wheel instead of counters once the rule is clear; colour the wheel's path; why must a leftover come back? Find 2/7 and 3/7 by starting the wheel at 2 and 3.
- **4–5:** fill a class table of period lengths for primes up to about 41 (shared among tables); conjecture that the period divides p − 1; explain why 142857 × 3 is a rotation (starting the wheel at remainder 3); discover the shortcut that times 10 then share among 7 is the same as times 3 on the wheel.

## Checked facts

Computed in `check_number_symmetry_2.py`, `check_week_157()`:

- 1/7 digits 142857 repeating, remainders 1, 3, 2, 6, 4, 5, 1 (six rounds before repeating); k/7 for k = 1 to 6 starts the same cycle at remainder k;
- 142857 × m for m = 1 to 6 is a rotation of its digits; 142857 × 7 = 999999; the 1/17 block 0588235294117647 times 1 to 16 also rotates;
- periods for primes 3 to 97 (for example 13: 6, 31: 15, 37: 3, 41: 5, 73: 8); the period divides p − 1 for every prime below 2000 other than 2 and 5;
- full-period primes below 100: 7, 17, 19, 23, 29, 47, 59, 61, 97;
- 1/13 remainders {1, 3, 4, 9, 10, 12} and 2/13 remainders {2, 5, 6, 7, 8, 11}: two wheels of 6; 1/41 repeats 02439;
- on the 7-wheel, times 10 and times 3 give the same remainder; 2/7 reads 285714; at most 60 counters are dealt in one round; among plate counts up to 30 with no factor 2 or 5, only 11 repeats after exactly 2 rounds.

Artin's conjecture and the Hooley and Heath-Brown results are cited to Moree's survey.

## Nearest existing themes

Week 4 (stars and wheels) hops by adding k round n dots, so every hop length gives equal loops; here the wheel step is multiplying, and loops can be shorter than the whole wheel (13 gives two loops of 6). Week 33 (prime-length necklaces) gives Fermat's little theorem by bead rings; the period dividing p − 1 is the same theorem met through division, which could be named as a return visit. Week 97 (square remainders) also lists remainders mod p, but for squaring. Week 3's permutation loops are close in spirit for full-period primes. New here: long division as a machine on remainders, cyclic numbers and an open conjecture.

## App connection

Numbers region, a "sharing machine" family: drag the leftover counters onto a trade-in slot, deal onto plates, and the board writes the digit; puzzles ask "which plate count up to 30 repeats after exactly 2 rounds?" (11) or "start the 7-wheel so the digits read 285714" (start at 2). A wheel-path puzzle (draw the arrows for 13 and count the loops) could share a board with a Week 4 star family.

## Open questions

- Whether 60 counters per table is enough and whether children tolerate six dealing rounds; the wheel may need to arrive after three rounds. Untested.
- Grades 2–3 have not met decimals; the plan keeps "each plate got" as whole counts and the word "decimal" in the guide only. A reviewer should check this framing still reads as division.
- Primes 17 and 19 have 16 and 18 rounds: a whole-class shared wheel may be needed.
