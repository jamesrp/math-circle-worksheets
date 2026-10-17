# Week 96 independent adversarial review

## Verdict

**Accept the mathematical design; no blocking defect found.** This is a substantive investigation sequence, with a concrete beginning and worthwhile continuations. I recommend two small wording clarifications below, not a redesign or reduction in mathematical ambition. There is no K–1 packet, as required by the run-specific scope override. Advanced pages may span return visits.

I read `PROMPT.md` and the scope override, independently rendered and visually inspected all four pages of `draft/grades-2-3.pdf` and all five pages of `draft/grades-4-5.pdf`, read the source builder and verification script, and independently checked the numerical cases. Review images are in `critic-renders/`. I did not edit the drafts, write a guide, or restart the workflow. The coordinator subsequently requested explicit checks of the word “factor” and finite token supplies; those assessments are included below.

## Recommended small clarifications

**Upper page 4, Problem 5:** change “using 2, 3 and 5” to “using any of 2, 3 and 5” or “using only the labels 2, 3 and 5.” The intended reading is an available set of labels; it is not a requirement that every bag contain all three primes. A literal all-three interpretation makes the 6-, 9-, and 10-divisor targets impossible, since a bag with three distinct primes has a divisor count divisible into three factors each at least 2. The earlier examples and token-pattern example make the intended reading recoverable, so I regard this as a modest robustness improvement rather than a blocker. The same clarification is harmless in lower Problem 4.

**Both page 1 openings:** the first sentence uses “factors” before it is defined, and the definition of prime uses it again. The adjacent worked product makes its meaning inferable, but knowing multiplication need not include knowing this vocabulary. I recommend “A number card can split into two whole numbers greater than 1 that multiply to its value. These numbers are its factors.” This states the legal action directly and preserves the brief prime definition. This is a useful accessibility edit, not a reason to add a separate exercise or new page.

**Finite supplies:** no token-stock contradiction is currently present. Lower Problem 4's largest single-prime pattern needs seven identical tokens, within the eight available 2 tokens; its minimum constructions need fewer. Upper Problem 4 uses seven 2s and four 3s, also within supply. Upper Problem 5 explicitly says “Draw,” so its eleven-identical-token pattern is feasible without extra physical stock. Upper Problem 6 asks for numbers and explicitly allows any primes, so it is not restricted to the kit. If field testing suggests children carry the physical stock limit into drawings, a brief permission to repeat labels would help. I would not add stock rules preemptively: they would add reading to resolve a limitation the printed task does not impose.

## Page-by-page coverage

| Packet/page | Evidence and assessment |
|---|---|
| 2–3 / 1 | The non-task example visibly moves from 20 to 4 × 5 to the tokens 2, 2, 5, with both products labelled 20. Multiplication is explicit, so the objects cannot reasonably be mistaken for additive counters after the launch. The legal splitting rule excludes 1, and prime is defined. Four contrasting cards, each with two splitting routes, provide sustained work; 18 really does have two routes, via 2 × 9 and 3 × 6. Recording areas can hold either drawings or compact card routes. |
| 2–3 / 2 | The second non-task example shows the unchanged full bag, the shaded choice, and the resulting bag. The product 2 × 5 = 10 and the exact quotient 20 ÷ 10 = 2 connect a choice to a divisor. The empty choice and full choice are explicitly legal. The two repeated-prime cases, 12 and 18, give enough concrete work to encounter duplicate choices before a larger comparison. |
| 2–3 / 3 | The 24-versus-30 comparison is purposeful: four tokens with a repetition and three distinct tokens both produce eight values. Asking which makes more does not assert that one must. Complete catalogs are substantial and leave organization to children. Large work areas support loose cards or drawings. |
| 2–3 / 4 | Inverse construction plus making the value small is a genuine extension, not more factoring practice. The 4-, 6-, and 8-value targets can be attacked experimentally with the existing token supply. The phrase “How small can you make…” permits progressively better constructions without demanding a universal minimality proof from every child. |
| 4–5 / 1 | The same successful explicit splitting bridge precedes 36, 48, and 60. The final uniqueness question is open and does not print the theorem as a procedure. This task is concrete for children with multiplication/factor-pair knowledge; it is not made suitable merely by a grade label. |
| 4–5 / 2 | The selected-sub-bag bridge is present before use. Two catalogs of eight values contrast repeated and distinct factors. “Exactly the set of divisors” asks for both directions and completeness in these specific cases; a child can check all factor pairs without already knowing a general uniqueness proof. |
| 4–5 / 3 | 36, 60, and 72 distinguish equal token counts, different repetition patterns, and equal divisor counts. The no-full-list goal directs attention to counting structure while leaving the method open. Problem 4 extends to seven 2s and four 3s, then asks for a rule for any prime bag. The numerical answer alone is brief once the rule is known, but formulating and justifying the general rule gives this numbered problem substance. Retain that explanation request. |
| 4–5 / 4 | Finding every token-count pattern is a substantial classification task. The prose example defines equivalence under relabelling primes and does not prescribe exponent factorization. Drawing rather than building is appropriate here: a valid 12-divisor pattern has eleven identical tokens, exceeding the supplied eight 2 tokens. The page does not require eleven physical 2 tokens. Five work areas are adequate for representative bag drawings, with the supplied whiteboard available for exploratory work. See the wording recommendation above. |
| 4–5 / 5 | This is a strong culmination: least values with an explanation excluding all smaller numbers. The earlier classification supplies a reason for this question, rather than an unexplained leap to optimization. Allowing any primes makes the global question explicit. It is demanding continuation material and should remain so; the scope expressly allows return visits. |

## Mathematical checks and proof limits

Independently enumerated positive divisors and sub-bag products agree:

| Bag value | Number of different positive divisors |
|---|---:|
| 12, 18 | 6 each |
| 24, 30 | 8 each |
| 36 | 9 |
| 60, 72 | 12 each |
| 2^7 × 3^4 = 10368 | 40 |

For upper Problem 5, the complete positive exponent patterns, ignoring prime names and order, are:

- 6 divisors: (5), (2, 1).
- 8 divisors: (7), (3, 1), (1, 1, 1).
- 9 divisors: (8), (2, 2).
- 10 divisors: (9), (4, 1).
- 12 divisors: (11), (5, 1), (3, 2), (2, 1, 1).

Three available prime labels suffice: four distinct primes already produce at least 16 divisors. The least values for counts 4, 6, 8, 9, 10, 12 are respectively 6, 12, 24, 36, 48, 60. These were independently checked by integer enumeration below 100; for these specific minima that checks every smaller positive integer. A structural explanation assigns the largest exponents to the smallest primes and compares the finite patterns. The printed tasks leave this discovery to the children.

Matching splitting experiments do not prove unique prime factorization. The pages do not explicitly claim that they do. Likewise, an empirical counting pattern is not yet a general argument: the product rule counts independent choices of how many copies of each prime to take, and uniqueness of prime factorization ensures those choices have different products. A general explanation that every divisor is a sub-bag uses the same factorization structure. These are mathematical limits to preserve during adult discussion, not reasons to insert a theorem or proof scaffold on the student pages. A facilitator guide is outside this stage's scope.

## Practical and presentation assessment

- Both packets have consistent headers and footers, consecutive problem numbering, ordinary task wording, and generous work areas. All nine rendered pages are free of clipping or overlaps. I found no overfull, underfull, or warning messages in the supplied LaTeX logs.
- The examples use legible numbers and explicit multiplication. Gray selection marks are visible in the render and are accompanied by the resulting selected bag; color is not needed. Physical print contrast has not been tested.
- Reading is concentrated in the two short rule introductions. Thereafter the tasks are one or two sentences, apart from the necessary pattern-equivalence explanation. An adult can read these aloud while children retain the mathematical work. This is consistent with prerequisites-based selection, not an assertion that every child in either printed grade band is ready.
- The intended concrete materials are useful: small-number arrays can check the lower packet; cards and labelled prime tokens support selecting and comparing bags. Large upper values do not require hundreds of counters. The upper eleven-token bag in Problem 4 fits the listed supply. Prepared tokens and the multiplication reference must actually be available at the session; the PDFs are student pages, not a complete preparation kit.
- There is no forced simultaneous tallying or transcription. Children may construct one catalog at a time and pool/check it. Twenty reusable cards per pair suffice for the specified single catalogs; the pages provide additional record space.
- A short whole-group material demonstration remains necessary, as in the brief. The printed examples support it. No classroom rehearsal, physical material-fit check, or child piloting was performed in this review.
- The sources contain `pdfinfoomitdate=1` and `pdftrailerid{}`. I inspected but did not run the supplied rebuild verifier, because it rewrites the draft. Consequently this review does not independently certify byte-identical or extracted-package rebuilding; that remains a revision/delivery verification responsibility.

## Optional concerns that should not trigger redesign

The proof and pattern-classification demands of upper Problems 4–6 may exceed a particular child's present readiness. That is an unpiloted readiness question, not a demonstrated grade-fit failure. The preceding concrete core remains available, and the accepted scope allows later visits. Do not remove the classification/minimality work merely to make the entire packet finishable in one hour.

The lower packet's fourth problem can occupy a long investigation through competing constructions; a child who already knows the divisor formula could finish it quickly. That is a reason to choose the upper continuation by prerequisites, not to add routine cases or printed scaffolding to the lower packet.
