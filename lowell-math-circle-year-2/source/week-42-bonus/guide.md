# Mathematical overview

For independent replacement draws from one unchanged two-color bag with red chance p, all three words containing exactly one R have equal weight p(1-p)^2; all three containing exactly two Rs have equal weight p^2(1-p). Assign the three output shapes bijectively within each of those sets and skip RRR/BBB. Then each output has weight p(1-p), so conditional on output each has chance 1/3 when 0<p<1. A convenient rule is to use the position of the lone color. Total output rate is 3p(1-p). The six mixed words need not have equal weights; equal-class pairing, rather than counting six words as equally likely, is essential.

The student rule states independent equal-counter draws, replacement, and a fixed composition. Independence is a modelling assumption: mixing is intended to approximate it; equal marginal chances alone do not establish it. Physical mixing has not been certified.

The base two-draw extractor gives BR a square and RB a circle. When four draws are split into two pairs, retain every existing output (possibly two). If both pairs were skipped, RRBB and BBRR have equal probability p^2(1-p)^2. Recycling them into opposite shapes adds equal output weight. RRRR and BBBB still skip. The expected number of outputs per four-draw block rises from 4p(1-p) to 4p(1-p)+2p^2(1-p)^2. This is an expectation of output count, not a probability of an output or a claim that the emitted sequence is independent. In the balanced two-counter bag, the SAME sixteen four-draw histories produce 16 versus 18 outputs in total. Counting on different sample spaces would not compare yields fairly.

Fair individual positions do not determine a joint distribution. Four equally likely tickets SS,SS,CC,CC give each position S/C chances 1/2, but only SS and CC occur. Tickets SS,SC,CS,CC give all four pairs chance 1/4. The first construction has perfect dependence; the second has independence. Fair marginal tallies from finite random trials do not prove either exact fact.

Grades 2-3 can construct and sort the three-way word rule or shape-pair tickets. Grades 4-5 can explain universal fairness and recycling efficiency. K-1 can match shape-pair tickets and act the two output positions with adult reading, but the three-draw polynomial comparison is not a forced K-1 task. These are three different investigations, not separate counts for different bag sizes.

# Materials, entry, and pacing

Per pair: one opaque cup/bag, four equal-feel counters (three R, one B), eight small output tokens of each of square/circle/triangle, a blank 160-by-40 mm paper strip divided into four 40-by-40 mm positions labelled 1, 2, 3, 4 (optional because the printed word boxes can hold the record), pencil, eight equal-size 70-by-30 mm blank paper tickets, and three student pages. Keep one R/one B in the cup for Problem 2's exact sixteen-story comparison. Identity labels R1,R2,R3,B and optional 60-by-25 mm paper slips (one identity word per slip) permit checking the 256-history model without randomly testing it. Children can pool the labeled cases by first draw; no one needs to transcribe 256 rows. The printed word boxes are records, not counter-placement boards.

For eleven children at KK11 / 3333 / 445: five kits (two pairs, two pairs, one upper pair with rotating checker), five bags, twenty source counters, forty tokens of each shape, forty blank tickets, five strips and pencils. Three anchored adults read and operate only the hiding/reset conventions; children choose mappings and sort cases. Print five shared three-page companions, or eleven selected record pages if each child wants a separate design. Page 3 is a design record: transfer the designs to eight 70-by-30 mm tickets rather than cutting unequal surrounding page areas. Fold all tickets alike or use identical backs, keep the cups opaque, and draw without looking with equal-chance mixing as the model. Ticket uniformity requires equal size and hidden draws; cutting and mixing have not been physically rehearsed.

Shared launch, 4-6 minutes: handle counters first. Show a non-task replacement draw record RB, explicitly return and mix between the two draws, and show that reversing the order changes the word. Demonstrate a whole three-draw record without choosing an output rule. On p2, the non-recycling example BRRB becomes BR | RB, then square and circle; both existing outputs are kept. Let children choose the new recycling rule. In the ticket investigation, show a ticket with left circle/right square, read the two positions, replace and mix. Do not introduce independence as a synonym for fairness.

A return visit can spend 15-25 minutes on Problem 1 or Problem 3. Reserve Problem 2 for a separate 20-35 minute visit if recording two existing outputs is taxing. A complete equal-weight explanation is a strong stopping point. The youngest table can retain familiar base pair play or inspect physical shape-pair tickets. Grade labels refer to prerequisites, not exclusion by age.

# Problem 1 (page 1)

One valid rule: lone color in position 1 gives square, in 2 circle, in 3 triangle. Thus RBB and BRR give square; BRB and RBR give circle; BBR and RRB give triangle. RRR and BBB skip. The student target is universal over every fixed bag containing both colors. With a sample 3R/1B labeled bag, all 64 identity triples are equally likely. Each output has 12 histories; 28 skip. With R/B equally likely, each output has two of eight stories and two skip. With 2R/1B, each output has six of 27 identity histories and nine skip.

For an unknown fixed bag, the three one-red words can be reassigned among shapes in any order, and independently the three two-red words can be reassigned. Each shape must receive one word from each class if the rule is to work for every p. The student need not characterize all such assignments. The singleton-position rule is one easy pairing argument.

Hints only if needed: put the one-red words side by side and ask what they have in common in the drawing chances; do the same for two-red words. A three-red/one-blue trial is evidence, while a position-permutation preserves exact word weight. Extension: investigate what fails if the bag changes between draws or draws are dependent. Such extensions are not counted separately.

New versus base: base Week 42 has deterministic two-shape outputs from ordered pairs, bag efficiency and replacement variations. This investigation constructs a genuinely three-way output from length-three composition classes.

# Problem 2 (page 2)

Assign RRBB an extra circle and BBRR an extra square; switching these names also works. The rule acts only when both original pairs skipped. RRRR/BBBB still give none. No first-stage success is thrown away. For every fixed p, the two recycled words each have weight p^2(1-p)^2.

For the balanced two-counter bag the 16 supplied words are equally likely. Basic output totals: square 8, circle 8, overall 16. Recycled: square 9, circle 9, overall 18. Basic per-block counts are zero in 4 words, one in 8, two in 4; recycling changes two of the zero-output words to one-output words. It does not create more than two outputs per block.

For 3R/1B, use 256 equally likely identity histories: each basic shape occurs 96 times across all retained pair positions; each gets 9 additional recycled outputs, hence 105 each, total 210. Compare 192/256 with 210/256 outputs per block, not with a different-size history set. No claim of maximally efficient extraction or independence is made.

Hints: among the four both-skipped words, which two have equal R/B totals? Give those to opposite shapes. Ask whether RRBB and BBRR have equal chance even when reds are common. Extension: pair two skipped four-draw blocks to recycle again, maintaining an explicit disjoint-block rule; keep this only as a readiness-dependent next visit.

New versus base: base compares two-draw response rates by changing bag contents. This keeps a fixed bag and recovers information from skipped pairs while retaining successes.

# Problem 3 (page 3)

Cup 1 can hold SS,SS,CC,CC. Cup 2 can hold SS,SC,CS,CC, where S is square and C circle. Both have two S and two C in each position. Cup 1's mixed pairs are impossible; Cup 2 has one ticket for each pair. Therefore marginal fairness does not imply whole-pair fairness. Other valid Cup 1 examples use SC,SC,CS,CS. Children may draw larger physical versions of the blank tickets if preferred; letters accompany shapes in adult records.

Hints: sort once by the left shape, once by the right, then sort by the whole pair. Extension: design a four-ticket selector with fair positions and three possible pairs; it is impossible with four equal tickets because the counts of SS and CC must agree, and the counts of SC and CS must agree. Keep this as an optional exact argument, not another required child page.

New versus base: the base stresses fair two-output rules and independence assumptions on source draws. This asks whether two fair output positions themselves imply an independent fair pair, using designed joint distributions.

# Source and verification record

Original extensions of the current Week 42 finite-history model. The base source is Levin, Peres and Wilmer, *Markov Chains and Mixing Times*, Appendix B.2, printed p. 312 (PDF p. 328), von Neumann unbiasing; the new selectors and finite comparisons are independently derived. Pedagogy: *Math Circle by the Bay*, Preface pp. viii-x (PDF pp. 9-11), deep themes, manipulatives, independent work and flexible duration; these particular encore designs are our inference. Week 1 encore sources were read as a layout/return-visit model.

`student/verify.py` checks all printed words, exact weighted identity histories for four contrasting bags, all output counts, equal composition classes, and the two ticket constructions. The separate independent mathematics review confirmed the exact models and ticket support possibilities. All three final student pages have been digitally rendered and individually inspected after revision; the verifier and standalone extracted-source rebuild pass. **Unpiloted; counter, ticket and cutting/mixing procedures have not been physically pretested.**

Record date/adult, selected investigation, prerequisite readiness, mapping or ticket designs, experiment versus exact argument, any confusion, and next starting point. One theme, three investigations; actual use remains unrecorded.
