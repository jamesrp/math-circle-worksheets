# Week 96 independent mathematical answer inventory

Checked against both rendered draft PDFs: grades 2–3, four pages, Problems 1–4; grades 4–5, five pages, Problems 1–6. This is mathematical evidence for a later guide, not a facilitator guide or classroom rehearsal. The independent checker uses only Python 3's standard library and never imports or runs the writer's verifier.

## Mathematical basis and proof limits

For every positive integer n > 1, splitting a composite factor into two factors greater than 1 preserves the product and eventually reaches prime factors. The prime multiset is unique. Finite experiments support discovery; the general uniqueness theorem additionally needs Euclid's lemma: if a prime p divides ab, then p divides a or b. For example, when p does not divide a, gcd(p,a)=1, so a Bezout identity up+va=1 multiplied by b proves p divides b. Apply the lemma repeatedly to two prime products, match a prime on both sides, cancel it, and continue. This adult justification is not a reading prerequisite for the student investigation.

A sub-bag of n's prime bag has value d dividing n, because the complementary tokens multiply to n/d. Conversely, if d divides n, factor d and n/d into primes; uniqueness makes d's prime bag a sub-bag of n's. Equal-prime copies are indistinguishable: a bag with e copies of one prime gives e+1 choices for its count, including zero. Thus n = product p_i^e_i has product (e_i+1) positive divisors. Distinct exponent choices give distinct products by uniqueness. The empty bag has value 1 and one sub-bag, itself.

For a fixed pattern of positive exponents, the least number uses consecutive smallest primes with the exponents in decreasing order. Replacing a used prime by a smaller unused prime reduces the number. For p<q and a>b, p^a q^b < p^b q^a, since the quotient is (p/q)^(a-b)<1. Complete multiplicative partitions of the target divisor count therefore give every candidate for the global minimum.

## Page and problem answers

| Band / page / problem | Requested outcome and complete answer reference |
|---|---|
| Both / p1 / shared example | 20 → 4×5 → {2,2,5}; all stages have value 20. |
| 2–3 / p1 / P1 | Two different splitting routes for each of 12,18,24,36. Routes below; each number has one terminal prime bag. |
| 4–5 / p1 / P1 | Different routes for 36,48,60. Routes below; each has one terminal prime bag. The answer to the general uniqueness question is no. |
| Both / p2 / shared example | From {2,2,5}, select one 2 and the 5 to get {2,5}, value 10; 20÷10=2. The unselected 2 is the complement. |
| 2–3 / p2 / P2 | Full divisor collections for 12 and 18 below, six each. Yes, every positive divisor appears. |
| 2–3 / p3 / P3 | 24 and 30 each produce eight values: neither makes more, despite four versus three tokens. Full lists below. |
| 2–3 / p4 / P4 | For 4,6,8 values, minimum bags are {2,3}, {2,2,3}, {2,2,2,3}, with values 6,12,24. Complete pattern alternatives below. |
| 4–5 / p2 / P2 | Full divisor collections for 24 and 30 below, eight each. The sub-bag/complement argument and uniqueness prove exact correspondence. |
| 4–5 / p3 / P3 | 36 gives (2+1)(2+1)=9; 60 gives (2+1)(1+1)(1+1)=12; 72 gives (3+1)(2+1)=12. |
| 4–5 / p3 / P4 | Seven 2s and four 3s give n=2^7·3^4=10368 and (7+1)(4+1)=40 divisors. General count rule above. |
| 4–5 / p4 / P5 | Every token-count pattern for 6,8,9,10,12 divisors appears below. A pattern ignores which distinct primes have its positive counts. Zeros are omitted. |
| 4–5 / p5 / P6 | Least positive numbers for 4,6,8,9,10,12 divisors are respectively 6,12,24,36,48,60; exhaustive pattern proof below. |

## Splitting routes

Each row gives two legal examples; each arrow replaces exactly one composite factor. Braces are multisets, so order does not count. An audit route is a sequence of sorted multiset states; changing the order of independent splits counts as a different state sequence, while swapping equal cards does not. The printed problem does not demand route enumeration or impose this audit convention.

| Number | Route A | Route B | Terminal bag | All audit routes |
|---|---|---|---|---:|
| 12 | 12 → {2,6} → {2,2,3} | 12 → {3,4} → {2,2,3} | {2,2,3} | 2 |
| 18 | 18 → {2,9} → {2,3,3} | 18 → {3,6} → {2,3,3} | {2,3,3} | 2 |
| 20 | 20 → {2,10} → {2,2,5} | 20 → {4,5} → {2,2,5} | {2,2,5} | 2 |
| 24 | 24 → {2,12} → {2,3,4} → {2,2,2,3} | 24 → {4,6} → {2,2,6} → {2,2,2,3} | {2,2,2,3} | 5 |
| 36 | 36 → {4,9} → {2,2,9} → {2,2,3,3} | 36 → {6,6} → {2,3,6} → {2,2,3,3} | {2,2,3,3} | 7 |
| 48 | 48 → {6,8} → {2,3,8} → {2,2,3,4} → {2,2,2,2,3} | 48 → {4,12} → {4,4,3} → {2,2,4,3} → {2,2,2,2,3} | {2,2,2,2,3} | 15 |
| 60 | 60 → {6,10} → {2,3,10} → {2,2,3,5} | 60 → {4,15} → {2,2,15} → {2,2,3,5} | {2,2,3,5} | 11 |

The checker traverses every legal split from each starting number and verifies that every terminal state equals the independently trial-divided prime factorization. Full state routes are in `independent-math-enumeration.json`.

## Complete sub-bag/value inventories

`{}` is the empty bag; each item gives sub-bag → value. These lists count bags of prime values, not distinguishable physical-token selections.

**12 (6 divisors):** {} → 1; {2} → 2; {3} → 3; {2,2} → 4; {2,3} → 6; {2,2,3} → 12.

**18 (6 divisors):** {} → 1; {2} → 2; {3} → 3; {2,3} → 6; {3,3} → 9; {2,3,3} → 18.

**20 (6 divisors):** {} → 1; {2} → 2; {2,2} → 4; {5} → 5; {2,5} → 10; {2,2,5} → 20.

**24 (8 divisors):** {} → 1; {2} → 2; {3} → 3; {2,2} → 4; {2,3} → 6; {2,2,2} → 8; {2,2,3} → 12; {2,2,2,3} → 24.

**30 (8 divisors):** {} → 1; {2} → 2; {3} → 3; {5} → 5; {2,3} → 6; {2,5} → 10; {3,5} → 15; {2,3,5} → 30.

**36 (9 divisors):** {} → 1; {2} → 2; {3} → 3; {2,2} → 4; {2,3} → 6; {3,3} → 9; {2,2,3} → 12; {2,3,3} → 18; {2,2,3,3} → 36.

**60 (12 divisors):** {} → 1; {2} → 2; {3} → 3; {2,2} → 4; {5} → 5; {2,3} → 6; {2,5} → 10; {2,2,3} → 12; {3,5} → 15; {2,2,5} → 20; {2,3,5} → 30; {2,2,3,5} → 60.

**72 (12 divisors):** {} → 1; {2} → 2; {3} → 3; {2,2} → 4; {2,3} → 6; {2,2,2} → 8; {3,3} → 9; {2,2,3} → 12; {2,3,3} → 18; {2,2,2,3} → 24; {2,2,3,3} → 36; {2,2,2,3,3} → 72.

**10368 (40 divisors):** exactly the sub-bags with a copies of 2 and b copies of 3, where 0≤a≤7 and 0≤b≤4. Their values are 2^a·3^b. This Cartesian product is a complete compact inventory; its forty values are 1, 2, 3, 4, 6, 8, 9, 12, 16, 18, 24, 27, 32, 36, 48, 54, 64, 72, 81, 96, 108, 128, 144, 162, 192, 216, 288, 324, 384, 432, 576, 648, 864, 1152, 1296, 1728, 2592, 3456, 5184, 10368.

## All exponent patterns, representatives and minima

For each pattern, use the counts in the listed order for primes 2,3,5. This gives an allowed representative using only those labels and also the least value for that pattern among all primes. The full set of labelled bags for the pattern is obtained by assigning its positive counts to distinct members of {2,3,5}; repeated exponents do not create new assignments. No target here requires more than three distinct primes, because four would force at least 2^4=16 divisors.

| Target divisor count | All positive-count patterns → representative/minimum | Global minimum |
|---:|---|---:|
| 4 | (1,1) → 2·3=6; (3) → 2^3=8 | 6 |
| 6 | (2,1) → 2^2·3=12; (5) → 2^5=32 | 12 |
| 8 | (1,1,1) → 2·3·5=30; (3,1) → 2^3·3=24; (7) → 2^7=128 | 24 |
| 9 | (2,2) → 2^2·3^2=36; (8) → 2^8=256 | 36 |
| 10 | (4,1) → 2^4·3=48; (9) → 2^9=512 | 48 |
| 12 | (2,1,1) → 2^2·3·5=60; (3,2) → 2^3·3^2=72; (5,1) → 2^5·3=96; (11) → 2^11=2048 | 60 |

Completeness: factor the target count into integers at least 2, subtract 1 from each factor, and ignore order. The checker independently obtains the same patterns by enumerating all exponent triples in 0..target−1. Every exponent is in that range since its successor divides the target. For the least-number claims, the checker additionally tests every smaller positive integer by direct divisibility.

## Diagram and boundary checks

Every rendered page was inspected independently. Both splitting examples show 20, then cards 4 and 5, then tokens 2,2,5, with matching product labels. Both selection examples shade exactly one 2 and the 5; the output contains exactly those two tokens, and the repeated unselected 2 remains visible in the intermediate frame. All printed task bags have the stated multiplicities and products: 12={2,2,3}, 18={2,3,3}, 24={2,2,2,3}, 30={2,3,5}, 36={2,2,3,3}, 60={2,2,3,5}, 72={2,2,2,3,3}. All card numerals match their problem text. Tokens and numerical labels are visible and contained in their drawn bags.

Choosing no tokens contributes 1; choosing all contributes n. There is no 1 token and no zero token. Repeated tokens cannot be distinguished to obtain extra values. All starting cards are composite and admit at least two genuinely different first factor pairs, so two routes do not depend on merely reversing factors. Pattern tasks permit repeated labels and do not require every available prime label to be used. P5 explicitly asks for drawings, so the pattern with eleven copies of one prime does not depend on the number of physical tokens supplied. The P4 large-bag count is mathematical; no full 10368-counter array is required.

Reproduce the audit with `python3 independent-check_math.py --json independent-math-enumeration.json`. It uses no third-party modules, PDF libraries or writer-authored code. Finite exhaustive checks establish the listed instances, while the arguments above establish the general statements. Physical materials and classroom use remain untested.
