# Week 3 redesign: reversible code machines and maximum return time

Prepared September 19, 2026. The [print packets](../lowell-math-circle-year-2/source/week-03/README.md) replace routine alphabet invention with a finite investigation of permutations. The facilitator PDF gives exact solutions and the full accessible proofs. Prepared, not yet taught.

## The mathematical destination

Repeat the same reversible substitution. When does **every** symbol first return? Can a key on five symbols take longer than five turns? This is the concrete form of permutation order, disjoint-cycle decomposition, and least common multiples. Maximizing the return time on n symbols is exactly Landau's function, a genuine research subject. The worksheet problem is a small proven instance, not a claim of novel research.

Week 3 allows arbitrary bijections; Week 4 will restrict them to fixed circular shifts. Encoding and decoding remain concrete entry points, but the main task is to construct, classify, and prove a maximum.

| Level / identifier | Prerequisites | Investigation |
| --- | --- | --- |
| K–1 / F03-K-v2 | Match shapes, follow arrows, count to three with help; no reading. | Three-shape cycle, inverse decoding, repeated encoding. Then a swap plus a fixed symbol and a deliberately noninvertible key. |
| 2–3 / F03-M-v2 | Letters A–D as labels, count to six; coordinate a one-to-one rule. | Equality patterns survive substitution; compare a 3-cycle+fixed point with two swaps; design order 4 and explain why order 6 is impossible on four symbols. |
| 4–5 / F03-U-v2 | Count/multiples to six; classify all loop partitions and justify completeness. | A 3-cycle plus 2-cycle has order 6. Classify all seven partitions of five to prove the maximum. Compare two overlapping swaps in both orders; their composition has order 3. |
| Extra 6–7 / F03-X-v2 | Common multiples to 15 and cases by largest loop. | Construct an eight-symbol key of order 15 and prove no key is slower; predict and justify g(9)=20. |

## Exact keys, constructions, and proof

K key: circle→triangle→square→circle. The message circle–triangle–circle becomes triangle–square–triangle; backward decoding is unique. Changing to circle↔triangle with square fixed gives whole-key return time 2, although one symbol returns after 1. Collapsing two inputs to square loses information.

Middle P maps ABCD→BCAD; Q maps ABCD→BADC. P sends ABBA to BCCB and decodes CAAC to BCCB. One-to-one substitution preserves both equal and unequal positions, so ABBA cannot become ABCD. P has order 3; Q has order 2. Four-symbol loop partitions 4, 3+1, 2+2, 2+1+1, 1+1+1+1 have orders 4,3,2,2,1. Thus order 6 needs at least five symbols.

Upper maps ABCDE→BCAED, with loops (ABC)(DE). The successive full messages are ABCDE, BCAED, CABDE, ABCED, BCADE, CABED, ABCDE. Cover the supplied partition table first; classify with the A–E cards by largest loop. Largest 5 or 4 leaves one split each; largest 3 leaves 2 or 1+1; largest 2 leaves 2+1 or 1+1+1; largest 1 forces five singletons. The resulting seven partitions give orders 5,4,6,3,2,2,1, proving maximum 6. Uncover the table to compare after explaining why no split was missed. In the second investigation P swaps A/B and Q swaps B/C: P then Q sends ABCDE to CABDE, while Q then P sends it to BCADE. The first composite is (ACB) and has order 3. Disjoint swaps such as A/B and D/E commute; reversing the pipeline Q then P undoes P then Q.

**Why the loop method is exhaustive:** following a finite key eventually repeats. The first repeated symbol must be the start, because a later first repeat would have two different predecessors, forbidden by bijectivity. Remove that loop and repeat. A loop of length a returns exactly at multiples of a; simultaneous return is the LCM.

Extra: 5+3 gives order 15 on eight letters. Upper bound by largest loop: 8→8; 7→7; 6→6; 5→at most 15; 4→at most 12 (4+3+1); largest≤3→at most 6. For nine letters, 5+4 gives 20; cases largest 9,8,7,6,5,4,≤3 give maxima 9,8,14,6,20,12,6. Adding a fixed symbol never lowers g(n), but strict increase fails: g(5)=g(6)=6.

## Practical hour and facilitation

Prepare 18 small shape slips for three K children (two copies of each shape per child); 12 A–D cards for three middle children; A–E for the fifth grader plus F–H in reserve; 13 counters (three per K–1 child and one per older child), paper, pencils. Cards can be hand-lettered scraps. Print 3 K, 3 middle, 1 upper, and 1 extra packet. No full 26-symbol alphabet is needed.

- **0–10:** explore symbol cards and invent a short key.
- **10–15:** show the three-shape cycle. Launch: “What happens if we code the code again?”
- **15–35:** K follows shape keys; middle compares P/Q; upper tests the five-symbol key. Adult A anchors K; organizer visits middle and upper.
- **35–40:** movement/reset break; stand, stretch, and leave the work ready to return to.
- **40–55:** continue with loop classification or an optional proof below; composition and the eight-letter extra are alternatives.
- **55–60:** share a machine and its return time; tidy cards.

Ask where one letter goes next, whether all letters are home, and where two arrows entering the same place would break the rule. Only introduce partitions/LCM after children have followed actual counters. For a child who stalls, use a single loop first, then add a separate swap. Give one page at a time; the third upper page is an alternative direction, not prerequisite work before the extra. Triplets rotate encoder/decoder/checker; the fifth grader gets an adult explanation challenge.


### Satisfying stops and optional proofs

- **K–1 stop:** repeat the three-shape key until all shapes return, then undo a message. **Optional proof:** explain why a key with two inputs sent to the same output cannot be decoded uniquely.
- **2–3 stop:** compare P/Q return times and build a four-turn key. **Optional proof:** classify the five loop-size partitions to rule out a six-turn key on four letters.
- **4–5 stop:** build the 3+2-loop key and explain its first return at six. **Optional proof:** cover the supplied table, organize every partition by largest loop, and prove six is the maximum.

These are choices for the shared hour, not a requirement to finish the packet. At the stop, continue playing or comparing examples if that suits the child. Record whether each result was tried, conjectured, verified in these cases, proved, or given as a theorem.

## Source lineage and prior use

- Judson, *Abstract Algebra: Theory and Applications*, [university-hosted textbook](https://people.hsc.edu/faculty-staff/blins/books/JudsonAbstractAlgebra.pdf), Chapter 5, §5.1, printed pp. 59–63, especially Examples 5.5–5.7 and Theorem 5.9 (disjoint-cycle decomposition). This is ordinary undergraduate algebra made tangible; no group axioms are required of children.
- Deléglise, Nicolas, Zimmermann, [*Landau's function for one million billions*](https://arxiv.org/abs/0803.2160), 2008 arXiv manuscript, [§1.1–1.3, pp.1–3](https://arxiv.org/pdf/0803.2160). The definition of maximal permutation order and its loop-LCM representation is the exact classroom question. The paper studies efficient computation at large n. We prove only our finite cases, not the paper's algorithm or asymptotics.
- Downloaded Rozhkovskaya, *Math Circles for Elementary School Students*, Lesson 2, problems 2.2–2.8 (`OEBPS/part0012.xhtml`), supplies a secret-code entry; those examples include shifts. Our arbitrary bijections and maximum-order investigation are an adaptation.
- Lowell Handout 8, problem 8.1, uses divisibility to distribute apples for possible guest counts 3–6. We revisit common multiples through synchronized loops, with a new extremal question. This source was read; prepared old handouts do not establish that every child encountered it.
- *Math Circle by the Bay*, preface pp.viii–x, supports deep mathematical themes, manipulatives, reserve problems, and explanation. Rozhkovskaya Lesson 3, “At the lesson” item 1 (`part0013.xhtml`) supports attempts and explanation before a table is displayed. The specific keys, hour, and staffing are ours.

`lowell-math-circle-year-2/source/week-03/verify.py` exhaustively checks all permutations for n=4,5,6,8,9 and verifies all printed message traces and compositions. Record F03-K/M/U/X-v2 and the exact keys/loop sizes actually used. Future returns can examine orders for larger n, permutation parity, or sorting by swaps; the week 4 shift restriction is a deliberate immediate progression. See `lowell-math-circle-year-2/source/week-03/REVIEW.md` for visual QA.
