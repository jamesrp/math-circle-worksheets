# Week 3 redesign: reversible code machines and maximum return time

Revised September 27, 2026 from the September 19 design. **All v3 revisions are unpiloted.** The [print packets](../lowell-math-circle-year-2/source/week-03/README.md) contain 3 K pages, 3 middle pages, 4 upper pages, 3 extra pages, and a 5-page facilitator guide. Previous sources and PDFs are preserved in `archive-before-classroom-guidance-2026-09/`.

## Applying the Week 1 classroom guidance

The evidence is the organizer's [Week 1 report](week-01-classroom-review.md): short investigations needed more concrete examples, unclear continuation actions required rescue, and unfamiliar representations needed their own work. The changes below are design inferences for Week 3, not observations about children doing these tasks. No v3 packet has been reported taught.

- K: send three messages and decode a fourth before repeated single-symbol turns. The loop drawing now records a familiar sequence. A second key contrasts a swap with a fixed shape, before the optional information-losing key.
- Middle: several encodings/decodings and a child-built key establish the operation. Full-message P/Q trials precede arrow loops. Build each four-letter loop arrangement physically before testing a six-turn attempt and adding a fifth letter.
- Upper: compare a five-loop with a 3+2 key through full message traces, then build 4+1,2+2+1,3+1+1 keys. Mark simultaneous returns with counters before classifying by largest loop. The classification table is blank until children organize cases. Noncommuting and disjoint compositions receive a separate page with explicit intermediate rows and undo tests.
- Extra: build and compare 8,4+4,6+2,5+3 loops before the maximal-order table. Largest-loop cases at least 4 use leftover partitions; loops of size at most 3 use a common-return bound instead of a long copying exercise. Nine-letter examples and the five/six-letter plateau have their own later page.

Every student page now has the consistent week/topic/level header, v3 footer, and sequential numbered problems with needed diagrams and recording space. Name/date lines, duplicate titles, generic encouragement, standalone rules, and unnumbered continuations are removed. Explanation and general proof opportunities remain in the facilitator; they are invitations after concrete work rather than mandatory writing gates.

**Practical printing:** start with one first page per child (three K, three middle, one upper: seven sheets), plus the facilitator. Keep continuation masters ready and copy selected pages as needed; retain earlier mats when later problems reference them. The extra can remain digital until chosen. Expanded page counts provide time and choices, not a requirement to print or complete every page.

**Current satisfying stops:** K send/decode messages; middle P/Q and four-turn construction; upper 5 versus 3+2 comparison; extra 15-turn construction. Continue the same investigation when that is productive. Introduce each table, loop, or compact record with one replayable example, then let the child use it on more than one case before generalizing.

**Evidence to record next time:** exact problems and instances attempted; what children could replay unaided; where an adult had to demonstrate the task or record again; statements or drawings supporting a conjecture or proof; and what they wanted to continue. Keep observations separate from proposed explanations and revision hypotheses. Track tried / conjectured / checked in cases / proved / supplied, and record v3 IDs only after actual use.

**Teaching-source review for this revision:** reread *Math Circle by the Bay*, preface printed viii–x (deep themes, manipulatives, varied pace, explicit statements, and the limits of predicting lesson duration), and Rozhkovskaya, Lessons 3,7,8 “At the lesson” (attempts and explanation before a table; missed legal moves; copying displacing mathematical work). Those are source observations. The exact staged examples, launch, seven-sheet start, and stopping choices here are our proposals.

## The mathematical destination

Repeat the same reversible substitution. When does **every** symbol first return? Can a key on five symbols take longer than five turns? This is the concrete form of permutation order, disjoint-cycle decomposition, and least common multiples. Maximizing the return time on n symbols is exactly Landau's function, a genuine research subject. The worksheet problem is a small proven instance, not a claim of novel research.

Week 3 allows arbitrary bijections; Week 4 will restrict them to fixed circular shifts. Encoding and decoding remain concrete entry points, but the main task is to construct, classify, and prove a maximum.

| Level / identifier | Prerequisites | Investigation |
| --- | --- | --- |
| K–1 / F03-K-v3 | Match shapes, follow arrows, count to three with help; no reading. | Three-shape cycle, inverse decoding, repeated encoding. Then a swap plus a fixed symbol and a deliberately noninvertible key. |
| 2–3 / F03-M-v3 | Letters A–D as labels, count to six; coordinate a one-to-one rule. | Equality patterns survive substitution; compare a 3-cycle+fixed point with two swaps; design order 4 and explain why order 6 is impossible on four symbols. |
| 4–5 / F03-U-v3 | Count/multiples to six; classify all loop partitions and justify completeness. | A 3-cycle plus 2-cycle has order 6. Classify all seven partitions of five to prove the maximum. Compare two overlapping swaps in both orders; their composition has order 3. |
| Extra 6–7 / F03-X-v3 | Common multiples to 15 and cases by largest loop. | Construct an eight-symbol key of order 15 and prove no key is slower; predict and justify g(9)=20. |

## Exact keys, constructions, and proof

K key: circle→triangle→square→circle. The message circle–triangle–circle becomes triangle–square–triangle; backward decoding is unique. Changing to circle↔triangle with square fixed gives whole-key return time 2, although one symbol returns after 1. Collapsing two inputs to square loses information.

Middle P maps ABCD→BCAD; Q maps ABCD→BADC. P sends ABBA to BCCB and decodes CAAC to BCCB. One-to-one substitution preserves both equal and unequal positions, so ABBA cannot become ABCD. P has order 3; Q has order 2. Four-symbol loop partitions 4, 3+1, 2+2, 2+1+1, 1+1+1+1 have orders 4,3,2,2,1. Thus order 6 needs at least five symbols.

Upper maps ABCDE→BCAED, with loops (ABC)(DE). The successive full messages are ABCDE, BCAED, CABDE, ABCED, BCADE, CABED, ABCDE. Classify with the A–E cards by largest loop before showing the facilitator solution table. Largest 5 or 4 leaves one split each; largest 3 leaves 2 or 1+1; largest 2 leaves 2+1 or 1+1+1; largest 1 forces five singletons. The resulting seven partitions give orders 5,4,6,3,2,2,1, proving maximum 6. Compare with the facilitator table after explaining why no split was missed. In the second investigation P swaps A/B and Q swaps B/C: P then Q sends ABCDE to CABDE, while Q then P sends it to BCADE. The first composite is (ACB) and has order 3. Disjoint swaps such as A/B and D/E commute; reversing the pipeline Q then P undoes P then Q.

**Why the loop method is exhaustive:** following a finite key eventually repeats. The first repeated symbol must be the start, because a later first repeat would have two different predecessors, forbidden by bijectivity. Remove that loop and repeat. A loop of length a returns exactly at multiples of a; simultaneous return is the LCM.

Extra: 5+3 gives order 15 on eight letters. Upper bound by largest loop: 8→8; 7→7; 6→6; 5→at most 15; 4→at most 12 (4+3+1); largest≤3→at most 6. For nine letters, 5+4 gives 20; cases largest 9,8,7,6,5,4,≤3 give maxima 9,8,14,6,20,12,6. Adding a fixed symbol never lowers g(n), but strict increase fails: g(5)=g(6)=6.

## Practical hour and facilitation

Prepare 18 small shape slips for three K children (two copies of each shape per child); 12 A–D cards for three middle children; A–E for the fifth grader plus F–I in reserve; 13 counters (three per K–1 child and one per older child), paper, pencils. Cards can be hand-lettered scraps. Use the seven-sheet starting plan above and selected continuations. No full 26-symbol alphabet is needed.

- **0–10:** handle the materials freely.
- **10–15:** gather everyone for one concrete legal attempt and its record: Keep an input message visible, follow the three-shape key one position at a time, build the complete output row, then explain that the next turn uses that row.
- **15–35:** K messages; middle messages then P/Q; upper five-loop versus 3+2. Adult A anchors the youngest group; organizer visits middle and upper.
- **35–40:** stand, stretch, reset.
- **40–55:** continue, or choose one next stage when the previous action/record is understood.
- **55–60:** share one attempt or explanation and tidy. These are proposed intervals, not a completion schedule.

Ask where one letter goes next, whether all letters are home, and where two arrows entering the same place would break the rule. Only introduce partitions/LCM after children have followed actual counters. For a child who stalls, use a single loop first, then add a separate swap. Give one page at a time; the fourth upper page is an alternative direction, not prerequisite work before the extra. Triplets rotate encoder/decoder/checker; the fifth grader gets an adult explanation challenge.


### Later optional destinations and proofs

- **K–1 later destination:** repeat the three-shape key until all shapes return, then undo a message. **Optional proof:** explain why a key with two inputs sent to the same output cannot be decoded uniquely.
- **2–3 later destination:** compare P/Q return times and build a four-turn key. **Optional proof:** classify the five loop-size partitions to rule out a six-turn key on four letters.
- **4–5 later destination:** build the 3+2-loop key and explain its first return at six. **Optional proof:** organize every partition by largest loop before showing the solution, and prove six is the maximum.

These are choices for the shared hour, not a requirement to finish the packet. The earlier stops above remain complete sessions; choose these later destinations only when useful. Record whether each result was tried, conjectured, verified in these cases, proved, or given as a theorem.

## Source lineage and prior use

- Judson, *Abstract Algebra: Theory and Applications*, [university-hosted textbook](https://people.hsc.edu/faculty-staff/blins/books/JudsonAbstractAlgebra.pdf), Chapter 5, §5.1, printed pp. 59–63, especially Examples 5.5–5.7 and Theorem 5.9 (disjoint-cycle decomposition). This is ordinary undergraduate algebra made tangible; no group axioms are required of children.
- Deléglise, Nicolas, Zimmermann, [*Landau's function for one million billions*](https://arxiv.org/abs/0803.2160), 2008 arXiv manuscript, [§1.1–1.3, pp.1–3](https://arxiv.org/pdf/0803.2160). The definition of maximal permutation order and its loop-LCM representation is the exact classroom question. The paper studies efficient computation at large n. We prove only our finite cases, not the paper's algorithm or asymptotics.
- Downloaded Rozhkovskaya, *Math Circles for Elementary School Students*, Lesson 2, problems 2.2–2.8 (`OEBPS/part0012.xhtml`), supplies a secret-code entry; those examples include shifts. Our arbitrary bijections and maximum-order investigation are an adaptation.
- Lowell Handout 8, problem 8.1, uses divisibility to distribute apples for possible guest counts 3–6. We revisit common multiples through synchronized loops, with a new extremal question. This source was read; prepared old handouts do not establish that every child encountered it.
- *Math Circle by the Bay*, preface pp.viii–x, supports deep mathematical themes, manipulatives, reserve problems, and explanation. Rozhkovskaya Lesson 3, “At the lesson” item 1 (`part0013.xhtml`) supports attempts and explanation before a table is displayed. The specific keys, hour, and staffing are ours.

`lowell-math-circle-year-2/source/week-03/verify.py` exhaustively checks all permutations for n=4,5,6,8,9 and verifies all printed message traces and compositions. Record F03-K/M/U/X-v3 and the exact keys/loop sizes actually used. Future returns can examine orders for larger n, permutation parity, or sorting by swaps; the week 4 shift restriction is a deliberate immediate progression. See `lowell-math-circle-year-2/source/week-03/REVIEW.md` for visual QA.
