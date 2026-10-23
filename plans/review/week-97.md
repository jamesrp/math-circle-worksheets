# Week 97: Square remainders

**Verdict: keep.** No must. Every answer, card and proof checks, the problems run from primes to composites to proof, and the guide opens with the theorems. The fixes are a K–1 route, an objects-level picture for the prime proof, and one slop sentence.

Reviewed October 23, 2026 by Claude, with math.md and card_checks.py. Packet: week-97-students.pdf (W97-35-v1, Grades 3–5, 6 pp.). Adult guide: week-97-facilitator.pdf (W97-FAC-v1, 6 pp.). Companions noticed but not reviewed: the guide's optional square/nonsquare product visit (p. 6) and the band-views menu. Status: unpiloted; the source README calls it a review draft awaiting organizer review. No K–1 packet, by design.

## The mathematics

Squaring a side n and removing bundles of m leaves a remainder that depends only on n's remainder, so sides 0 to m − 1 show every output; cutting m-wide strips off the square proves it (P5). For an odd prime p, two sides share an output exactly when they are equal or sum to p, because p divides (x − y)(x + y), so there are (p + 1)/2 outputs counting 0 (P1, P2, P6). Composites break the pairing: with 8, output 1 hides four sides; with 9, output 0 hides three; with 15, outputs 1 and 4 hide four each (P3, P4). A mathematician would enjoy quadratic residues found with counters, with Euclid's lemma doing visible work.

## Ratings

| | Rating | Evidence |
|---|---|---|
| Mathematics | strong | Quadratic residues, periodicity by area, the prime pairing and where composites break it, each provable. |
| Problems | adequate | Six substantial problems in a good order. P1–P4 repeat one action (square, bundle, sort) as the arithmetic grows; P4 is fifteen remainders up to 196. |
| Student pages | strong | Spec header and footer, rules once, a non-task worked example before first use, large work boxes, square facts printed. One slop sentence (fix 3). |
| Concreteness | strong | Counters enforce the bundle size and the stopping rule; the launch (guide p. 2) uses p. 1's nine counters. From P4, printed facts replace counters. |
| Correctness | strong | math.md finds 0 problems in 51 cards, every inventory and every proof. I agree; its one note is weaker than stated (fix 9). |
| Adult guide | strong | Theorem-first with hypotheses and limits; complete inventories, launch, timings, hints; finite checks kept apart from proofs. Gaps: fixes 1, 2. |
| Age fit, K–1 | weak | No route: "The younger table needs a separate familiar activity with its adult" (guide p. 2). |
| Age fit, grades 2–3 | adequate | The adult reads; squares up to 64 counters suit third graders. P4 is mostly arithmetic for them and P5–P6 mostly beyond them, fine late (prediction). |
| Age fit, grades 4–5 | strong | P3–P4's comparisons, P5's strips and P6's conjecture suit this table; the organizer can carry the proof. |

## Keep

- p. 1: input 3 in one picture, 9 = 4 + 4 + 1, output 1; "until fewer than one bundle's worth remain"; the bundles-of-4 table, which shows both readings and no bundle-5 answer.
- P2's secret game, "Your partner must name every possible input", and "Among outputs that occur".
- P3's 7, 8, 9 contrast, and P4's 15, where zero is alone as at a prime yet outputs 1 and 4 hide four.
- P5's "an explanation that also works for squares too big to build"; P6's "Count output 0 too" and its 8, 9, 15 check.
- Guide: the overview, the inventories, the 100 = 70 + 21 + 9 strip diagram, the first-route timings, and "A guess is complete when it names every allowed input".

## Fix

1. **should**, K–1, guide p. 2: "The younger table needs a separate familiar activity with its adult." The K–1 table has no route and watches a launch it will not use. A should, as on the Week 83 and 87 cards, because the outline says "no forced K–1/2–3 variants". Fix, in the guide: after the launch, build squares 1 × 1 to 5 × 5 and put each in groups of 3: "Can a square leave 2?" (1, 1, 0, 1, 1: never.) Then groups of 4 (never 2 or 3). The parent reads and records. That K–1 manages it is a prediction.
2. **should**, guide p. 5, "Why the pairing is exact": the only route is x² − y² = (x − y)(x + y), algebra at a table of counters. Add the picture: take a 2 × 2 corner off a 5 × 5 square, and the L left, 21 counters, re-forms as a 3 × 7 rectangle, three bundles of 7, so 5 and 2 share an output. The L is always (x − y) by (x + y); with bundles of 7 it is whole bundles when it is empty or a side is 7, and the prime lemma says only then. It gives the 4–5 table P6 with objects.
3. **should**, p. 1: "We compare outputs to find which square inputs they can hide." Talk about the activity (neg.md); the bundles-of-4 sentence already shows what "hide" means. Delete it.
4. **could**, P3: "Can output 0 ever hide more than one input?" is answered on p. 1 (inputs 0 and 2). Move it to the guide.
5. **could**, P5: delete "Try larger squares, then"; the cards invite it.
6. **could**, P3: replace the three "use inputs" clauses with "Use bundles of 7, 8 and 9, each with inputs from 0 to one less than the bundle size", as P6 does.
7. **could**, P3: "lets a secret input hide among the most possibilities" turns "hide" round; say "has an output that hides the most inputs".
8. **could**, P4: print the multiples of 15 to 195 if third graders stall on 169 and 196 (prediction; the critic raised it too).
9. **could**, guide p. 2: say to print pp. 5–6 together. math.md notes p. 6 lacks 11² to 14² for the size-15 check, but p. 5 prints them and the guide pairs P5 with P6.
10. **could**, guide p. 1, "Discovery and readiness": name what children find: two inputs per nonzero output at 3, 5, 7 and 11, three or four at 8, 9 and 15, nothing new past m − 1.

Fixed October 23, 2026, after converting the week to problem files: shoulds 1–3 and coulds 4–7, 9 and 10 (checked in `source/week-97/checks/card_fixes_2026_10_23.py`, including the counters picture's dots); could 8 deferred.

October 23, 2026, later the same day: could 8 made in the guide, not on the student page, because the multiples are help for a child who stalls and the stall is a prediction. The Problem 4 key (guide page 4) tells the adult to write the multiples of 15 up to 195 where the table can see them if 169 or 196 stalls a child: 169 is 4 more than 165, 196 is 1 more than 195 (W97-FAC-v3; the student packet is unchanged). Unpiloted.

## Overlaps

Week 4 adds around a ring rather than squaring; Week 33 contrasts prime and composite lengths through Fermat. Week 96 proves the lemma P6 needs, so this week sits best after it. Weeks 6 and 94 identify unknowns from answers. No other theme takes squares modulo m. No merge.

## App fit

Not in themes.md yet. I propose Fit B, size M, a small new family.

- **Operation.** A square of counters; the child lassoes bundles of m, and the app refuses a wrong size or an early stop. A warm-up, not a solve.
- **Sort.** Drag side cards 0 to m − 1 into leftover bins and press "That's all"; the app checks. An empty bin, once every card is placed, certifies "cannot occur". Leftovers come from lassoing, not a tap, and bins show no slot counts.
- **Tell them apart**, or a Signal Lanterns group. Choose bundle sizes from 2 to 12 whose leftovers tell sides 0 to 15 apart; the app shows two sides that still collide. One size never works, since it pairs x with m − x; of the 55 pairs only 10 and 11 work (card_checks.py). Budget the tries.

Pitfalls: if the app computes every leftover, sorting becomes tapping; no predict-the-leftover rounds; P5 and P6's proofs stay on paper. Draw on P1, P3, P4 and P6's composite check.

## Classroom evidence

None reported. The source README says "Unpiloted; physical preparation, actual-size printing, adult procedures and timing have not been rehearsed."
