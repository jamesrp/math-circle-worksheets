# Week 201 (draft plan): Two prime towers make every even tower?

**Strand:** number (Numbers). **Deep-math field:** additive number theory (Goldbach's conjectures, parity, evidence versus proof). **Status:** draft plan, November 2026. No student pages, guide, review card or pilot.

## The deep idea

Goldbach's conjecture (from Christian Goldbach's correspondence with Euler) says every even number greater than 2 is the sum of two primes. It is open. What is known is of three kinds. Checked by computer: Oliveira e Silva, Herzog and Pardi (Mathematics of Computation, 2014) verified it for every even number up to 4 × 10¹⁸, and their counts of "minimal" Goldbach partitions agree closely with the Hardy–Littlewood predictions. Proved: the weak (ternary) conjecture, that every odd number greater than 5 is a sum of three primes, by Harald Helfgott in arXiv preprints of 2013 ("The ternary Goldbach conjecture is true", December 2013), using the circle method. Elementary and provable by children: an odd number is a sum of two primes exactly when it is 2 more than a prime, because two odd primes make an even number, so one of the two must be 2 (so 11 and 17 are not sums of two primes, while 13 = 2 + 11 is); and the strong conjecture would imply the weak one, since an odd n ≥ 9 is 3 plus the even number n − 3. The number of ways tends to grow (100 = 3 + 97 = 11 + 89 = 17 + 83 = 29 + 71 = 41 + 59 = 47 + 53, six ways; 90 has nine), but not steadily (98 has only three), and growth in examples is not a proof: the gap between "true for every case anyone has checked" and "proved" is the honest lesson. Checked here: every even number from 4 to 10,000 is a sum of two primes, and for every one of them a prime below 175 can serve as the smaller part (173 is needed only for 7426); every odd number from 7 to 2001 is a sum of three primes; the numbers below 20 that are not sums of two primes are 1, 2, 3, 11 and 17 (NRICH's "Little Goldbach"). Children can find two-prime splits, notice that the number of splits grows, prove the odd-number rule and the "strong implies weak" step, and learn that a famous statement can be checked to 4 × 10¹⁸ and still be unproved.

## Sources

Every link was opened and read on the date given; nothing is cited from memory or from a search snippet.

- [Empirical verification of the even Goldbach conjecture and computation of prime gaps up to 4·10¹⁸](https://www.ams.org/journals/mcom/2014-83-288/S0025-5718-2013-02787-1). Tomás Oliveira e Silva, Siegfried Herzog and Silvio Pardi, Mathematics of Computation 83 (2014), 2033–2060. Abstract: the even conjecture verified to 4 × 10¹⁸, the odd conjecture to 8.37 × 10²⁶ as a consequence, minimal partitions matching Hardy–Littlewood (read November 4, 2026).
- [The ternary Goldbach conjecture is true](https://arxiv.org/abs/1312.7748). H. A. Helfgott, arXiv:1312.7748, December 30, 2013 (v2 January 2014). Every odd integer greater than 5 is a sum of three primes, by the circle method and the large sieve (read November 4, 2026).
- Prior use with children: [Little Goldbach](https://nrich.maths.org/6239). NRICH, ages 11 to 14. How many whole numbers below 20 cannot be written as a sum of two primes (read November 4, 2026).
- Prior use with children: [Goldbach's Conjecture](https://byrdseed.com/goldbachs-conjecture). Byrdseed (a site for teachers of gifted students), no grade stated. Students test even numbers for a counterexample; companion question on three primes (read November 4, 2026).

## A kid-friendly way in

Prime towers. Before the session, snap cube towers of heights 2, 3, 5, 7, 11 and 13 in one colour each ("special towers": towers that cannot be laid out as a rectangle of 2 or more rows, as Week 96 and draft 159 would say), several of each. An even target tower (4 to 26) is built in another colour. The task: stand two special towers side by side to match the target exactly. Prep: about 20 minutes of snapping, or print strips on 1 cm squared paper instead. Launch (2 to 3 minutes): show that 7 cannot be made a rectangle and 6 can, so 7 is special and 6 is not; then match a 10 tower with 3 + 7, and ask whether there is another way.

## By band

- **K–1:** match even target towers from 4 to 14 with two special towers each, laying the pair beside the target; find a second way for 10 and 14. Then an odd tower, 11: can two special towers make it? Counting and comparing heights only; no reading.
- **2–3:** the class chart: every even number from 4 to 50 as two primes, with a list of the primes below 50 provided. Which numbers have the most ways? Is there an even number that cannot be done? Then odd numbers: which can be made from two primes, and what do all those pairs have in common?
- **4–5:** prove the odd rule (one prime must be 2, so n − 2 must be prime). Prove that if every even number were two primes, every odd number from 9 up would be three primes. Then the evidence question: the class chart up to 100, the "ways" count for 90, 98 and 100, and what "checked to 4 × 10¹⁸" does and does not prove. Extension: three primes for odd numbers up to 51 (the weak conjecture, proved in 2013).

## Checked facts

Computed in `check_symmetry_number_3.py`, `check_week_201()`:

- every even number from 4 to 10,000 is a sum of two primes; for each, the smaller prime can be chosen at most 173, and 173 is needed only for 7426;
- ways (unordered): 1, 1, 1, 2, 1, 2, 2, 2, 2 for 4, 6, …, 20; 6 for 100 (starting 3 + 97); 3 for 98; the most below 100 is 9, for 90;
- towers 2, 3, 5 and 7 make every even number from 4 to 14 as a pair; 16 needs a bigger prime;
- 1, 2, 3, 11 and 17 are the numbers below 20 that are not sums of two primes; an odd number up to 199 is a sum of two primes exactly when it is 2 more than a prime;
- every odd number from 7 to 2001 is a sum of three primes.

Cited, not computed: the verification to 4 × 10¹⁸ and Helfgott's proof.

## Nearest existing themes

Week 96 (Prime bags) builds numbers from primes by multiplying and proves unique factorization; here primes are added, and there is no uniqueness (10 = 3 + 7 = 5 + 5). Draft 159 (rectangles of a number) supplies the "cannot be a rectangle" picture of a prime; draft 158 (squares from two squares) asks the parallel question "which numbers are a sum of two squares?", where the answer is a proved theorem, a useful contrast with Goldbach's open one. Draft 108 (hailstone numbers) is the library's other open problem with huge computer checks; the two share the lesson about evidence and proof, so they should not sit in the same term. New here: additive questions about primes, the parity proof for odd numbers, and the strong-implies-weak argument.

## App connection

Numbers. A "Prime pairs" family: an even tower stands on the board; drag two prime towers beside it to match. Puzzles: "Find all three ways for 22"; "Which odd tower can two prime towers make?"; "Find the even number below 60 with the most ways". The Prime bags family (Week 96) already has prime tokens to reuse.

## Open questions

- K–1 cannot tell which towers are prime; the supplied special towers make it a matching game. Check that the "cannot be a rectangle" launch is understood or skip it at K–1.
- Is the class chart to 50 too much listing for 2–3? Pooling by tables should keep each child to a few numbers.
- Wording for open problems: say "nobody has found a proof" without suggesting the children should find one.
