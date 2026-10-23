# Week 96: Prime bags and divisor builders

**Verdict: keep.** No must: every answer checks, the problems climb from splitting cards to the least number with a given divisor count, and the guide opens with the theorems. The fixes are a K–1 route, a Problem 3 that narrates its picture and presumes a winner where the bags tie, and small repairs.

Reviewed October 23, 2026 by Claude, with math.md. Packets: week-96-grades-2-3.pdf (W96-23-v1, 4 pp., Problems 1–4), week-96-grades-4-5.pdf (W96-45-v1, 5 pp., Problems 1–6). Adult guide: week-96-facilitator.pdf (W96-FAC-v1, 6 pp.). Companions noticed but not reviewed: the guide's gcd/lcm return visit (p. 6). Status: unpiloted review draft awaiting organizer review (source README), after the workflow stages and a pair review on October 17; kits and timing unrehearsed. No K–1 packet, by design.

## The mathematics

Children split number cards into factors until only primes remain, then choose sub-bags of the tokens. Every route ends in the same bag: unique factorization, reached as a conjecture and proved in the guide through Euclid's lemma. Sub-bag values are exactly the divisors, so counts e₁, …, e_r give (e₁+1)⋯(e_r+1) divisors, and the least number with a given count puts the largest counts on the smallest primes (6, 12, 24, 36, 48, 60 for 4, 6, 8, 9, 10, 12). A mathematician would enjoy it. P1 carries uniqueness in both bands; 2–3 P2–P3 and 4–5 P2 the bijection; 4–5 P3–P4 the count; 2–3 P4 and 4–5 P5–P6 the design.

## Ratings

| | Rating | Evidence |
|---|---|---|
| Mathematics | strong | Uniqueness, the sub-bag bijection, the count and least numbers, each met with tokens; minimality gets a finite proof. |
| Problems | strong | Contrasts carry the order: 12 and 18 share a shape; 24 (four tokens) and 30 (three) both give 8; 36, 60, 72 give 9, 12, 12, so equal token counts differ and unequal ones tie. 10,368 forces a rule. 4–5 P1 is quick for fluent children. |
| Student pages | strong | Header, footer, numbering right; no slop or hints. Non-task worked visuals precede both operations (20 → 4 × 5 → {2,2,5}; the shaded selection with 20 ÷ 10 = 2). One narrating sentence (fix 2). |
| Concreteness | adequate | The launch (guide p. 2) builds 4 × 5 with counters, then splits the 4. Tokens hold the bag, each is chosen once, and equal tokens look alike. Splits and products rest on multiplication; arrays appear only as a hint. |
| Correctness | strong | math.md: 167 checks, no error, one wording item (fix 2). I reproduced the divisor lists, the 40, the minima and the first splits. |
| Adult guide | strong | Theorem-first overview with hypotheses, limits and a band map; launch, kit, pacing, full keys, proofs. Gaps: K–1 and divisor testing (fixes 1, 3). |
| Age fit, K–1 | weak | No route, by design: "The younger table needs a separate familiar activity with its adult" (guide p. 2). |
| Age fit, grades 2–3 | adequate | An adult reads two rule blocks with new words (factor, prime, divisor, interchangeable). Cards stay within the 36 counters. Prediction: P2's divisor check needs division with remainders, new in October of third grade. |
| Age fit, grades 4–5 | strong | P1–P3 act on tokens; P4's rule and P5–P6 come late, and the guide makes P5–P6 a return visit. |

## Keep

- The two worked visuals on the non-task 20, repeated in the launch.
- 2–3 P1's four cards, each with two or more first splits, and "Can different routes finish with different prime bags?"
- 2–3 P2's divisor question; the 24-versus-30 pair; P4's "How small can you make the full bag's value in each case?"
- 4–5 P3's three bags "without listing every value", P4's seven 2s and four 3s, P5's "Find all possible token-count patterns", and P6, which permits any primes.
- Guide: the overview, the pattern table and its completeness argument, the 24-against-54 exchange, and "Do not hand over this complete table".

## Fix

1. **should**, K–1, guide p. 2. The K–1 table gets the launch, then "a separate familiar activity". A should, as on the Week 59–62, 76, 80 and 87 cards, since the scope routes this week to Grades 2–5. Add a guide route: "Make 12 counters into a rectangle with at least two rows. Find a different one." Then sort 2 to 20 counters into "makes a rectangle" and "only one row", with the parent scribing. That K–1 sustains this is a prediction.
2. **should**, 2–3 p. 3, P3: "These bags have different numbers of tokens. Which can make more different values by choosing tokens?" The first sentence narrates the picture (neg.md). The question presumes a winner, but both make 8, so a child may hunt for a missing value. I agree with math.md on the tie; its fix, without the first sentence: "Find the complete collection for each bag. Does the bag with more tokens make more different values?"
3. **could**, guide p. 3, 2–3 P2: "To test a divisor, share 18 counters into equal groups of that size; none left over means it divides."
4. **could**, 4–5 p. 3, P4: the box is 3.0 cm for a number and a general rule, with 5 cm blank below; enlarge it.
5. **could**, both p. 1: "Equal tokens are interchangeable" → "Tokens with the same number are the same."
6. **could**, both p. 1: "no factors except 1 and itself" names what the page never calls factors; "a number greater than 1 that cannot split" (math.md, wording only).
7. **could**, 4–5 P5: "A bag with two 2s and one 3 has the same pattern as a bag with two 5s and one 2."
8. **could**, problem bags: tokens are 0.52 cm and nearly touching, against 0.73 cm in the examples; match them.
9. **could**, guide p. 2: "Problem 4 is a return visit" and "later pages held back" keep 2–3's design problem from a quick child; print p. 4 and hold it at the table.
10. **could**, guide p. 2: a printable sheet of 2, 3, 5, 7 circles would replace hand-marking three 20-token kits.

## Overlaps

Week 19's subset cards are the sub-bags of a number with distinct primes; its antichain theorem is absent here. Weeks 4, 9, 29, 31 and 32 reach gcd or lcm by other routes, which the return visit only touches. Week 97 builds on this guide's Euclid's lemma. The year-1 door-toggle puzzle (Handouts 9, Problem 9.1) is divisor parity, deliberately not repeated. No other theme has unique factorization or the divisor count. No merge.

## App fit

No row yet: themes.md stops at Week 82, and decisions.md lists 96 as open. I propose Fit B, size M.

- **Split** (opener). Tap a card and enter a factor; the app rejects non-factors and turns primes into tokens. Buttons for every split would remove the factoring.
- **Collect every value.** Tap tokens; the app multiplies; keep each new value in a tray and claim "That's all" with no visible count, answered by "There's another" when wrong. The tray of sub-bags is the certificate. Draw on 2–3 P2–P3 and 4–5 P2.
- **Design.** Build a bag with exactly k values, then the smallest, from 2, 3, 5, 7, with no live divisor counter. A wrong "Best" gets a smaller bag as refutation. Draw on 2–3 P4, 4–5 P5–P6, and 4–5 P4's 40.

Pitfalls: no typed divisor counts (predict-an-outcome); uniqueness and the rule stay on paper.

## Classroom evidence

None reported. No record in this repository mentions its use; the private use log was not available.
