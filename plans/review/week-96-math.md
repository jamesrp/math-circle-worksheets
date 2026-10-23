# Week 96 (Prime bags): math check

Scope:
- `lowell-math-circle-year-2/week-96/week-96-grades-2-3.pdf`: 4 pages, Problems 1–4. The shared splitting rules and the 20 → 4 × 5 → {2,2,5} example are on p. 1; the token-choosing rules and the shaded-token example are on p. 2.
- `week-96-grades-4-5.pdf`: 5 pages, Problems 1–6. It has the same two rule blocks and examples on pp. 1–2.
- `week-96-facilitator.pdf`: 6 pages.
- There is no K–1 packet, and the README says so.

I read the sources `source/week-96/student/grades-2-3.tex`, `grades-4-5.tex`, `guide/facilitator.tex`, `README.md`, `QA.md` and `SOURCES.md`. I did not run or import the package's `check_math.py`. The three delivered PDFs are byte-identical (SHA-256) to `source/week-96/reference-pdfs/`, and their text layers carry the same numbers as the sources. I rendered every page at 80 dpi and looked at each one. My scripts and their outputs are in this run folder, for `plans/review/checks/week-96/`. Checked October 23, 2026.

**Result: every printed bag, value, example, answer and guide statement is mathematically correct, and every problem has the intended answer. I found 1 problem, minor. Grades 2–3 Problem 3 asks "Which can make more different values?" about two bags that both make exactly 8.**

## How it was checked

- **`check_math.py`** (output `check_math.py.out`, 129 checks, 0 failures). It reads the cards and bags from the LaTeX sources and confirms the same values appear in the PDF text.
  - **Splitting routes.** It enumerates every legal route for 20, 12, 18, 24, 36, 48 and 60. A legal step splits one composite card into a × b with a, b ≥ 2. Every route from each start ends in one bag. The number of distinct split sequences is 2, 2, 2, 5, 8, 17 and 11, and every card has at least two different first splits.
  - **Guide routes.** It parses all 12 routes in the guide. Each arrow splits exactly one card into two factors at least 2 with the right product, and each route ends at primes.
  - **Sub-bag values.** For every printed bag it takes all 2^k selections of token positions, compares the set of distinct products with the divisors found by trial division, and compares the result with the guide's lists.
  - **Counts.** τ(2^7·3^4) = 40 by trial division, 2^7·3^4 = 10,368, and τ(32) = 6.
  - **Count patterns.** For each target 4, 6, 8, 9, 10 and 12 it compares three sets: the multiplicative partitions of the target, a brute-force search over 2^a 3^b 5^c, and the patterns of every integer below 5000 (any primes). The least value of each pattern is checked against the guide's table.
  - **Least numbers.** It finds the least n with each divisor count by direct search, both over all n and over n built only from 2, 3 and 5.
  - **Guide arithmetic.** It checks the gcd and lcm of 24 and 36, 12·72 = 24·36, and the 24 against 54 comparison.
  - **Token kit.** It checks that every set of bags one page shows together fits the guide's kit of eight 2s, six 3s, four 5s and two 7s.
  - **Page references.** It checks every "Problem N, page P" heading and internal page reference in the guide, and the consecutive problem numbers in both packets.
- **`check_diagrams.py`** (output `check_diagrams.py.out`, 38 checks, 0 failures). It reads the tikz coordinates from the sources.
  - Every printed bag's tokens multiply to its "value" label, sit inside the bag outline, and do not overlap (gap 0.06 cm).
  - The p. 1 example reads card 20 → 4 × 5 → bag {2,2,5}, with captions 4 × 5 = 20 and 2 × 2 × 5 = 20.
  - In the p. 2 example, the middle bag is the same {2,2,5}. Its shaded tokens are 2 and 5, which match the right bag "value 10". The unshaded 2 matches the caption 20 ÷ 10 = 2.

## Grades 2–3 (pp. 1–4): correct except item 1

- **Opening rules and example (p. 1).** The example is correct. Token order and identical tokens are handled as the mathematics needs.
- **P1.** Bags: 12 = {2,2,3}, 18 = {2,3,3}, 24 = {2,2,2,3}, 36 = {2,2,3,3}. Each card has at least two genuinely different routes. 12 and 18 have exactly two each (2 × 6 or 3 × 4; 2 × 9 or 3 × 6), so "find two" is achievable without counting a reordering as new. Different routes never finish with different bags, as intended.
- **Rules and example (p. 2).** The empty bag is 1, and choosing all tokens gives the full value. The example is correct.
- **P2.** 12 gives 1, 2, 3, 4, 6, 12 and 18 gives 1, 2, 3, 6, 9, 18. Each list is exactly the divisors, so the answer to "Does your collection contain every divisor?" is yes for both.
- **P3.** 24 (four tokens) gives 1, 2, 3, 4, 6, 8, 12, 24. 30 (three tokens) gives 1, 2, 3, 5, 6, 10, 15, 30. Both make 8 values. See item 1.
- **P4.** With labels 2, 3 and 5:
  - 4 values: least 6 = {2,3}. Other patterns: {p,p,p}, least 8.
  - 6 values: least 12 = {2,2,3}. Other: {p^5}, least 32.
  - 8 values: least 24 = {2,2,2,3}. Others: 30 = {2,3,5} and 128.
  - The minima are the same when any primes are allowed, and all three minimal bags fit the kit.

## Grades 4–5 (pp. 1–5): checks out completely

- **P1.** 36 = {2,2,3,3}, 48 = {2,2,2,2,3}, 60 = {2,2,3,5}. There are 4, 4 and 5 distinct first splits. No number has two finished bags.
- **P2.** 24 → 8 values and 30 → 8 values, exactly the divisors. A finite check of 1–24 and 1–30 is enough to explain "exactly" for these two values.
- **P3.**
  - 36 → 9 (3 · 3).
  - 60 → 12 (3 · 2 · 2).
  - 72 → 12 (4 · 3).
  - In each case the counting rule agrees with the full enumeration.
- **P4.** Seven 2s and four 3s give 8 · 5 = 40 divisors of 10,368. The general rule is the product of (count + 1). It gives 1 for the empty bag, which is right.
- **P5.** All 13 patterns are realizable with only 2, 3 and 5, because no target needs four primes (2^4 = 16 > 12):
  - 6: (2,1) and (5).
  - 8: (1,1,1), (3,1) and (7).
  - 9: (2,2) and (8).
  - 10: (4,1) and (9).
  - 12: (2,1,1), (3,2), (5,1) and (11).

  The page's convention example ("two 2s and one 3, or two 5s and one 2, have the same pattern") is pattern (2,1) both times. Patterns (9) and (11) need more 2s than the kit's eight, and the page says "Draw".
- **P6.** The least numbers are 6, 12, 24, 36, 48 and 60. They are the same with any primes and with only 2, 3 and 5.

## Adult guide (6 pp.): checks out completely

- **Overview (p. 1).** Every fact is true and stated with the right hypotheses:
  - unique factorization for n > 1;
  - divisors p₁^a₁ ⋯ p_r^a_r with 0 ≤ aᵢ ≤ eᵢ;
  - complement = quotient;
  - τ(n) = ∏(eᵢ + 1), with the empty bag for 1;
  - least value for a pattern puts the largest exponents on the smallest primes;
  - finite search over patterns.

  The overview also separates experiment from proof, and its "what children discover" claims are true. One example: 24 has four tokens and 30 has three, yet both have 8 divisors.
- **Launch (p. 2).** 4 rows of 5 counters, 4 × 5, then 2 × 2 × 5. Selected 10 times unselected 2 gives 20. Both are correct.
- **Answers (pp. 3–5).**
  - All 12 routes are legal, one split per arrow.
  - All inventories match the enumeration: 12, 18, 24, 30, 36, 60 and 72.
  - 2–3 P2's "with or without the 3, then zero, one or two 2s" organization gives 2 · 3 = 6.
  - The 2–3 P4 minima are right, and so is the 4–5 P3 and P4 counting, including the check that five 2s give six divisors, not 5 and not 2^5.
  - The pattern table is complete and each least value is right: 6, 8, 12, 32, 30, 24, 128, 36, 256, 48, 512, 60, 72, 96 and 2048.
  - "12 = 12, 6·2, 4·3, 3·2·2 and no other" is right.
  - The minimality argument is right: complete pattern list, consecutive smallest primes, and the exchange (p/q)^(a−b) < 1. So is the 24 against 54 illustration.
- **Proofs (p. 6).**
  - Termination is correct.
  - The Euclid's-lemma proof via up + va = 1 is correct.
  - The cancellation proof of uniqueness is correct. It applies the two-factor lemma repeatedly to a longer product, which is standard.
  - The sub-bag bijection is correct, including the warning that labelled selections overcount.
  - The gcd and lcm extension is correct: 12 = 2^2·3, 72 = 2^3·3^2, 12·72 = 24·36 = 864, by min + max = sum.
- **Page references.** Every problem's page reference and every internal page reference is correct (checked by script).

### 1. Grades 2–3, p. 3, Problem 3 (minor): the question assumes one bag makes more values, but the two bags tie

- **Quoted text:** "Problem 3: These bags have different numbers of tokens. Which can make more different values by choosing tokens? Find the complete collection for each bag." The bags shown are {2,2,2,3} "value 24" and {2,3,5} "value 30".
- **Evidence.** The 24 bag makes 1, 2, 3, 4, 6, 8, 12, 24. The 30 bag makes 1, 2, 3, 5, 6, 10, 15, 30. That is 8 and 8 (`check_math.py.out`: "strictly more for one bag? False"). The guide's answer is "Both have eight values", and it calls the problem "a deliberate contrast". So the intended answer is "neither", which the question as worded does not allow for. A child who correctly finds 8 and 8 may think a value is missing and keep searching, or may report the bag with more tokens. The guide protects the adult from marking the child wrong, but nothing on the page protects the child.
- **Smallest fix:** keep the bags and the contrast, and make the question open: "Problem 3: These bags have different numbers of tokens. Does the bag with more tokens make more different values by choosing tokens? Find the complete collection for each bag."

**Not counted (correct as printed, or wording only):**
- **Factor and prime definitions (both bands, p. 1).** The page says "A number card can split into two whole numbers greater than 1 that multiply to its value. These numbers are its factors." It then defines a prime as "a number greater than 1 with no factors except 1 and itself". If the first sentence is read as a definition, 1 and the number itself are never "factors", so the exception names things the page does not call factors. Both readings pick out exactly the same primes, and so the same answers, so this is wording only. If the page is touched, "a number greater than 1 that cannot split" says the same thing in the page's own terms.
- **Guide P5 hint "first separate bags with one distinct prime label from those with two".** It is a starting hint and does not claim to cover everything. The table beneath it includes the three-label patterns (1,1,1) and (2,1,1).
- **Kit fit.** 2–3 P1 needs exactly the kit's eight 2s and six 3s if all four final bags stay out at once, and 4–5 P1 needs exactly eight 2s. Both fit. Patterns (9) and (11) in 4–5 P5 exceed the kit, and both the page ("Draw") and the guide allow drawn tokens. The 36 counters cover the 2–3 array hint (largest card 36). They do not cover arrays for 48 or 60, but the 4–5 guide does not suggest arrays.
