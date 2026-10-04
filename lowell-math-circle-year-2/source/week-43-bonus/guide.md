# Mathematical overview

A uniform permutation of A1,A2,B1,B2 induces a uniform picture word after number labels are hidden. Every picture word has exactly 2!2!=4 labeled orders: choose which A identity occupies each A position and which B identity occupies each B position. There are 24 labeled orders and six picture words, each with chance 1/6. More generally, multiplicities m1,...,mk give n!/(m1!...mk!) picture words, each with the same label-permutation multiplicity. This result assumes the physical labeled cards are uniformly shuffled; covering labels does not make an arbitrary chooser uniform.

A cut preserves clockwise neighbor order. Any sequence of cuts is a rotation. From ABCD the reachable rows are exactly ABCD,BCDA,CDAB,DABC. A uniform random cut from 0,1,2,3 gives each card a fair first position but only four of the 24 full orders. Allowing whole-row reversal gives the eight dihedral rows, still not all orders. ABDC is impossible under both rules: in either permitted cyclic direction A's neighbors remain B and D, while in ABDC its cyclic neighbors are B and C. Reversal adds possibilities; no probability for choosing reversal is implicitly assumed.

A uniform three-card shuffle followed by an independent uniform choice of one of four insertion gaps gives a uniform four-card shuffle. Deleting D from a final row identifies the unique old ABC order, and D's location identifies the unique gap. Thus the six old rows times four gaps are 24 equally likely stories, in one-to-one correspondence with all 24 final orders. Repeating this construction inserts card n+1 uniformly in one of n+1 gaps and preserves uniformity. Fair gap choices alone cannot repair a biased old shuffle.

Grades 2-3 can make the six picture rows and the cut/reversal catalog with physical cards. Grades 4-5 can explain equal label multiplicities, a cyclic-order obstruction and insertion's unique predecessor. K-1 can enter by matching repeated pictures or making cuts after adult demonstration, but full uniform-history claims are readiness-dependent. Experiments expose examples; complete generation and invertible constructions establish exact fairness and completeness.

# Entry, materials, and flexible pacing

Per pair: four equal-size cards with pictures square A1,A2 and circle B1,B2, four other equal-size cards A,B,C,D (reuse the base A/B/C cards), four equal-size 25-by-40 mm cut tickets numbered 0,1,2,3 (relabel these 1,2,3,4 for insertion), a cup, eight removable number covers, a pencil and three student pages. Plain 25-40 mm cards are sufficient; the page-1 models are 25.4 mm squares. Record cells are pencil space rather than exact card-fitting mats. For the cut example, use a fifth spare small row WXYZ made on scrap paper if needed; no bought kit required.

For eleven KK11 / 3333 / 445 children: five paired kits, forty working cards, twenty tickets, five cups, forty small covers and pencils; three anchored adults. The upper third child can be chooser/checker, rotating. Print five shared companions or eleven selected record pages. For exact picture fairness, provide extra scrap rows so children can pool different labeled orders without every child listing 24. Use the entire four-ticket set for each random draw: return the chosen ticket, reset the full set and mix before the next cut or insertion. Choose an insertion gap with a fresh draw independent of the old row; the chooser must not use that row to favor a gap. Uniform ticket size and hidden drawing are modelling preparation, not a certified physical random mechanism. Make covers that reveal the picture while hiding only the number; physical cutting, concealment and fit remain untested.

Launch together (4-6 minutes): let children rearrange cards freely. Show a same-picture swap of A1/A2: the labeled row changes while the picture row does not. Let one child move the front two cards W,X of WXYZ to the end, leaving YZWX, matching the printed cut visual. Before Problem 3, use XY plus new Z: point to three gaps, insert Z into the middle, obtaining XZY. The printed XY visual numbers the three marked gaps left to right, with gap 2 precisely between X and Y. Keep all old relative orders. These examples teach the procedures without giving the main catalogs or bijection.

A first visit may use 15-25 minutes on pictures and 15-25 on cuts. Insertion can be another 20-30 minute visit. First require independent rearrangement and a recoverable row record. The cyclic invariant and general insertion proof belong after concrete cases. Do not demand completing every page. Youngest pairs may explore repeated-picture rows or continue base card activities while older groups pursue exact chance.

# Problem 1 (page 1)

All picture words: AABB,ABAB,ABBA,BAAB,BABA,BBAA. Each has four labeled orders. For AABB they are A1A2B1B2, A1A2B2B1, A2A1B1B2, A2A1B2B1. The same independent A-label and B-label swaps work for any picture pattern. Each target's four preimages are disjoint; every labeled order produces exactly one picture word, proving completeness and equal weight. Children can explain with physical swaps rather than factorial notation.

Hint only if needed: keep the picture positions fixed while exchanging the same-picture cards. Extension: use A1,A2,A3,B1 to get four picture rows with six labelings each, or three A and two B to study a different multiplicity. These variants are extensions within this one investigation, not additional counted investigations.

New versus base: base Week 43 uses distinct A/B/C cards and ticket-swap algorithms, then extends those algorithms to four/five distinct cards. Repeated pictures introduce many labeled histories for each visible row and the distinction between physical identity and picture outcome.

# Problem 2 (page 2)

Cuts only: ABCD,BCDA,CDAB,DABC. Cuts plus reversal add DCBA,CBAD,BADC,ADCB. These are all possibilities because rotating an order after rotating it is another rotation; reversing a rotation is a rotation of the reversed order. Children may deliberately choose any legal cut/reversal while assembling the reachable catalog; random tickets are needed only to study the first-card chances. One cut of each size constructs every rotation. A reversal followed by each cut constructs the four new rows.

ABDC is absent under both operations. A ring arrangement exposes the invariant: cuts select a new beginning on the same clockwise ring; reversal changes the direction, while each card's two neighbors remain unchanged. Even with fair first card, orders ADBC,ABDC,ACBD and many others never appear, so the full 24-order distribution is not uniform. In this task a fair full shuffle means all 24 orders have equal chances, not merely each first card.

Hints: join the ends of the row as a ring; identify A's two neighbors. Extension: for five distinct cards, cut-only reaches five rows and cut/reverse ten. A random cut after a uniform shuffle preserves uniformity; it cannot make a fixed row into a uniform shuffle. This distinction avoids treating cuts as useless in every context.

New versus base: base tests biased full shuffles and ticket-swap histories. This examines a subgroup of physically achievable orders and a fair marginal statistic that hides severe global restrictions.

# Problem 3 (page 3)

Targets: ABCD comes from ABC, gap 4; DACB from ACB, gap 1; BDCA from BCA, gap 2; CBAD from CBA, gap 4. Gaps are numbered left to right, with gap 1 before the first old card and gap 4 after the last. The worked XY/Z example has its three gaps in the same convention.

Each final order has exactly one story: remove D and remember its position. Conversely every old row and gap makes one final order. The revised student rule explicitly asks for all six old rows equally likely and an independent gap draw. Reset and mix the full four-ticket set for each random insertion. Six uniform old rows and four independent uniform gaps yield 24 equal histories, so each final order has chance 1/24. This is an elementary reversible-construction proof. Children need not copy all 24 rows to establish the general result.

Hints: cover or remove the new D in a target, then rebuild it. Extension: insert E after a uniform four-card shuffle; deleting E gives a unique predecessor among 24*5=120 equal histories. Ask what remains biased if the ABC chooser favors ABC. Do not use the old three-swap rule, which the base has already shown is biased.

New versus base: base upper Problems 6-7 design fair Fisher-Yates ticket-and-swap shuffles for four/five cards. This is a different incremental insertion algorithm and an explicit unique-deletion proof, not a renumbered swap algorithm.

# Sources, verification, and use record

Original extensions of the current Week 43 card model. The base's Fisher-Yates source provides context, but no downloaded exercise was copied. Pedagogy consulted: *Math Circle by the Bay*, Preface printed pp. viii-x (PDF pp. 9-11), deep themes, manipulatives, independent work and flexible duration. The return-visit design is our inference. The Week 1 encore and older extensions were inspected to preserve substantial return work while avoiding their themes.

`student/verify.py` exhausts 24 labeled orders, verifies all six multiplicities, computes cut/reversal closure, checks the printed cut example, and verifies all 24 insertion histories plus every printed target. The independent mathematics review confirmed every catalog, multiplicity and target, and supplied a dependent uniform-marginal counterexample that supports the added independence assumption. All three final student pages were rendered and individually inspected after revision; the portable verifier and extracted-source rebuild pass. **Unpiloted; card concealment, cutting, mixing and physical handling have not been pretested.**

Record date/adult, investigation used, matching/order readiness, actual catalogs and explanations reached, confusion, and where to resume. One theme, three investigations, no prior use claimed.
