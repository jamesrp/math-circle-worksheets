# Week 4 redesign: shifts, orbit structure, and perfect shuffles

Revised September 27, 2026 from the September 19 design. **All v3 revisions are unpiloted.** The [print packets](../lowell-math-circle-year-2/source/week-04/README.md) contain 3 K pages, 3 middle pages, 4 upper pages, 3 extra pages, and a 5-page facilitator guide. Previous sources and PDFs are preserved in `archive-before-classroom-guidance-2026-09/`.

## Applying the Week 1 classroom guidance

The evidence is the organizer's [Week 1 report](week-01-classroom-review.md): short investigations needed more concrete examples, unclear continuation actions required rescue, and unfamiliar representations needed their own work. The changes below are design inferences for Week 4, not observations about children doing these tasks. No v3 packet has been reported taught.

- K: record one-hop routes from two starts, then two-hop routes from two starts on a second visible ring. Try a missed landing before three-hop and hidden-turn comparisons.
- Middle: concrete common-shift outputs precede short messages. The +2 routes from A,B,C,D get a whole page and two markings to distinguish their landing sets. Only afterward compare +3 and +5 and test an inverse from four starts.
- Upper: build all +4 loops, reverse them with +8, and compare +3,+6,+5 before organizing the full table. A supplied eighteen-place ring supports transfer examples. Physical routes precede distance/lap records; inverse and commuting-shift experiments remain explicit tasks. The subtraction-strip/gcd proof stays in the facilitator with its additional readiness gate.
- Extra: real shuffle rows and tracks of cards 1,3,7 precede the position map. Draw its loops before comparing against doubling/remainders. Six and sixteen cards receive their own page of construction and comparison; the fixed last card and proof of first return remain explicit in the guide.

Every student page now has the consistent week/topic/level header, v3 footer, and sequential numbered problems with needed diagrams and recording space. Name/date lines, duplicate titles, generic encouragement, standalone rules, and unnumbered continuations are removed. Explanation and general proof opportunities remain in the facilitator; they are invitations after concrete work rather than mandatory writing gates.

**Practical printing:** start with one first page per child (three K, three middle, one upper: seven sheets), plus the facilitator. Keep continuation masters ready and copy selected pages as needed; retain earlier mats when later problems reference them. The extra can remain digital until chosen. Expanded page counts provide time and choices, not a requirement to print or complete every page.

**Current satisfying stops:** K one/two-hop routes; middle two +2 orbits; upper +4/+8 loops; extra eight-card return. Continue the same investigation when that is productive. Introduce each table, loop, or compact record with one replayable example, then let the child use it on more than one case before generalizing.

**Evidence to record next time:** exact problems and instances attempted; what children could replay unaided; where an adult had to demonstrate the task or record again; statements or drawings supporting a conjecture or proof; and what they wanted to continue. Keep observations separate from proposed explanations and revision hypotheses. Track tried / conjectured / checked in cases / proved / supplied, and record v3 IDs only after actual use.

**Teaching-source review for this revision:** reread *Math Circle by the Bay*, preface printed viii–x (deep themes, manipulatives, varied pace, explicit statements, and the limits of predicting lesson duration), and Rozhkovskaya, Lessons 3,7,8 “At the lesson” (attempts and explanation before a table; missed legal moves; copying displacing mathematical work). Those are source observations. The exact staged examples, launch, seven-sheet start, and stopping choices here are our proposals.

## Mathematical destination

Fix a circular ordering. Repeated shifts can split the circle into separate orbits. What controls their number and their length? The children's tables lead to the cyclic-group theorem: shift +k on n positions has order n/gcd(n,k) and gcd(n,k) cycles. The extra converts a physical out-shuffle into modular multiplication and proves its first return time. This adds structure beyond week 3's arbitrary code machines and replaces repeated cipher arithmetic with classification and explanation.

Every additive shift is reversible, even when one orbit skips positions. Coprimality controls visiting all positions from one start, **not** the existence of decoding. Keep this distinction explicit.

| Level / identifier | Prerequisites | Investigation |
| --- | --- | --- |
| K–1 / F04-K-v3 | Match four shapes, count hops 1–3 with support; no reading. | Compare one/two/three-hop routes, infer a whole shift from one match, find an undo. |
| 2–3 / F04-M-v3 | A–J labels; count to 10; follow a single rule. | Decode a short clue, reject incompatible clues, compare +2 and +3 on ten letters, explain disjoint orbits. |
| 4–5 / F04-U-v3 | Counts/multiples to 18 for finite rings; general proof additionally needs division/gcd and adult-supported coprime divisibility. | Infer +4 on 12 positions, compare or classify shifts, distinguish inverse from orbit size; optionally prove the gcd formula with the divisibility scaffold and explain commuting rotations. |
| Extra 6–7 / F04-X-v3 | Track numbered positions; repeated doubling and remainders. | Eight-card perfect out-shuffle, order 3, doubling modulo 7 with final position fixed; predict orders for 6 and 16 cards. |

## Concrete setup and hour

Use the printed rings and one counter per child. Bring pencils, scratch paper, and eight card scraps numbered 0–7 for the extra; another eight permit the 16-card extension. No wheel cutting or brads. A six-picture K extension can use hand-drawn scraps. Use the seven-sheet starting plan above and selected continuations. For seven children and two adults, adult A anchors the youngest triplet, organizer alternates middle and upper, and the fifth grader has a scheduled adult discussion of the conjecture.

- **0–10:** handle the materials freely.
- **10–15:** gather everyone for one concrete legal attempt and its record: Move one hop on the four-shape ring; show a two-hop turn, distinguish the passed-over shape from its landing, and record the landing before taking another turn.
- **15–35:** K one/two-hop starts; middle common shifts then +2 routes; upper +4/+8. Adult A anchors the youngest group; organizer visits middle and upper.
- **35–40:** stand, stretch, reset.
- **40–55:** continue, or choose one next stage when the previous action/record is understood.
- **55–60:** share one attempt or explanation and tidy. These are proposed intervals, not a completion schedule.

Questions and hints: “Which places did you land on, rather than pass over?” “Has the starting point returned?” “Choose an unused start.” “How many total spaces have you moved, and how many full laps?” Read aloud as needed. The whole twelve-row table is optional recording support, not a requirement to copy before progressing. The extra can follow the first orbit investigation if interest points toward cards.


### Later optional destinations and proofs

- **K–1 later destination:** compare one/two-hop routes and find an undo for the hidden turn. **Optional proof:** explain the missed shapes with the two separate loops.
- **2–3 later destination:** decode the clue and compare +2/+3 routes. **Optional proof:** use alternate markings to prove +2 misses half the letters while still having an inverse.
- **4–5 later destination:** explain the +4 and +8 return times on twelve places and show their loops. **Optional proof:** with adult support, use the coprime divisibility scaffold to prove the gcd formula; without that step record the general rule as a conjecture or supplied theorem.

These are choices for the shared hour, not a requirement to finish the packet. The earlier stops above remain complete sessions; choose these later destinations only when useful. Record whether each result was tried, conjectured, verified in these cases, proved, or given as a theorem.

## Checked results and proofs

K ring clockwise is circle, triangle, square, star. One-hop and three-hop rules visit all four; two hops splits into circle/square and triangle/star. Circle→square determines +2, taking triangle→star; +2 undoes itself. A six-position ring is visited fully only by steps 1 or 5 among 1–5.

Middle alphabet A–J: A→D means +3. GDG decodes DAD; BAG encodes EDJ. B→F contradicts this key because B must become E. +2 gives A,C,E,G,I and B,D,F,H,J; alternate markings are invariant. +3 gives A,D,G,J,C,F,I,B,E,H before returning. Full-visit steps are 1,3,7,9. +2 still has inverse +8.

Upper: input 9→output 1 on 12 places determines +4; input 2→6 agrees. Outputs 1,4,10 decode 9,0,6. Its cycles are (0,4,8), (1,5,9), (2,6,10), (3,7,11). For k=0…11, return times are 1,12,6,4,3,12,2,12,3,4,6,12; numbers of cycles are 12,1,2,3,4,1,6,1,4,3,2,1. On 18 positions +6 returns in 3, +5 in 18. The zero rule's first positive return is 1.

**Concrete proof bridge:** for +8 on 12 places, return means 12 divides 8t, or 3 divides 2t. Draw three strips each of length t. Their total 3t is a multiple of 3; if the first two strips 2t are also a multiple of 3, removing them leaves t a multiple of 3. Thus the first positive return is t=3. This proves this numerical case for all t.

**Optional general proof:** return at t means n divides kt. For k>0, divide n and k by d=gcd(n,k), giving coprime n′,k′. The [shared adult-supported scaffold](coprime-divisibility-scaffold.md) proves that n′ divides k′t exactly when n′ divides t: subtract the shorter of strips n′ and k′ repeatedly until both have length 1, and repeat those subtractions on n′t and k′t. These scaled lengths remain multiples of n′, so their final length t is too. Common divisors are unchanged by subtraction and the positive sum decreases, justifying the process. The first return is therefore n′=n/d. Every start has that length, giving d cycles. Handle k=0 separately as the identity. This lemma needs additional adult support; if only the numerical bridge is explained, mark the general rule as conjectured or given as a theorem. +4’s inverse on 12 is +8; +4 then +7 and +7 then +4 both give +11 because addition commutes.

**Extra:** interleave equal halves without reversing, first-half card first. Eight-card rows are 01234567 → 04152637 → 02461357 → 01234567. The old-to-new position map is [0,2,4,6,1,3,5,7]; cycles are fixed 0, fixed 7, (1,2,4), (3,6,5). For positions 0…6, new position is 2x mod 7; position 7 is fixed separately. Iterating multiplies by 2^t. The powers 2,4,8 first have remainder 1 at t=3; following position 1 proves no earlier whole return. Six cards use modulus 5 and return after 4; sixteen use modulus 15 and also return after 4. A larger deck need not take longer.

## Sources, research boundary, and history

- Judson, *Abstract Algebra: Theory and Applications*, [textbook](https://people.hsc.edu/faculty-staff/blins/books/JudsonAbstractAlgebra.pdf), Chapter 4 §4.1, Theorem 4.13, printed pp. 48–49 (PDF pp. 60–61), gives the order-of-a-power formula n/gcd(n,k). Our rings are its additive form.
- Diaconis, Graham, Kantor, [*The mathematics of perfect shuffles*](https://pages.uoregon.edu/kantor/PAPERS/PerfectShuffles.pdf), *Advances in Applied Mathematics*4 (1983),175–196. **§2, Lemma 1, printed p. 177 (PDF p. 3)** proves the out-shuffle order via doubling modulo 2m−1. The main theorem classifies groups generated by in/out shuffles; §4 treats parallel-processing applications. Our extra proves the small return-time case and derives the position formula, not the group classification. No current open-problem status is asserted.
- Downloaded Rozhkovskaya, Lesson 2, problems 2.3–2.7 (`OEBPS/part0012.xhtml`), supplies the shift-cipher entry. Our ring sizes, orbit questions, gcd argument, and shuffle extension are new adaptations. The source was actually read.
- Lowell Handout 6, problem 6.7, and Handout 7, problem 7.8, mention earlier card-ordering solitaire and its ten-card version. Those were read. Perfect out-shuffling is a different explicit operation, not assumed to repeat the earlier task.
- *Math Circle by the Bay*, preface printed pp.viii–x, supports common themes across levels, physical exploration, varied pace, and harder reserves. Our staffing and minute allocations are proposals, not attributed to the book.

`lowell-math-circle-year-2/source/week-04/verify.py` independently checks all shifts on ring sizes 4,6,10,12,18, all printed encodings, the 8-card rows, the general position map for 6,8,16 cards, and their first returns. Record actual step/ring sizes and extra use as F04-K/M/U/X-v3. Later returns can investigate prime versus composite sizes, affine permutations, in-shuffles, or shuffle groups without repeating these small cases. See `lowell-math-circle-year-2/source/week-04/REVIEW.md` for visual QA.
