# Week 1: back-pocket extensions

Prepared September 19, 2026. These optional investigations continue the revised Week 1 tiling activities at roughly a **grades 6–7 reasoning level**. They can serve a younger child ready for the questions. They are alternatives to choose from, not an additional session to complete or a claim about what children have already encountered.

The [print packet and LaTeX](../lowell-math-circle-year-2/source/week-01/README.md#back-pocket-extensions) include four challenge pages, one actual-size board, and a separate five-page facilitator guide with selection advice, gradual hints, complete solutions, and deeper continuations.

## Choose a question by readiness

| ID | Entry question and mathematical product | Readiness / materials | Suggested use |
|---|---|---|---|
| F01-X1 | A board has seven up and seven down cells. Why does it still need four green fillers? Find a packing and a proof using competing partners. | Pair triangle cells; count neighbors; explain a lower bound. Seven small blues, four greens, optional purple. | Student p. 1; 10–20 minutes. |
| F01-X2 | How far apart are two tilings? Encode a 15-rhombus board by words, count 20 states, and derive distances. Equal scores can hide a distance of four. | Read a ribbon, count positions, compare a route with a lower bound. Fifteen small blues and mat, or three R slips and three L slips. | Student pp. 2 + 5; 15–30 minutes. |
| F01-X3 | How many shortest routes connect the extremes? Count 42 by adding predecessor counts, then explain why the recurrence is exhaustive. | Know the nine-move lower bound; organized addition; track a three-number record. Six letter slips, pencil. | Student p. 3; 20–30 minutes. |
| F01-X4 | Do random flips visit each tiling equally often? Experiment, then find amounts unchanged by a sharing rule; change the random rule. | Read a graph; equal chances; halves and thirds for the proof. One counter, die, scrap paper, four identical folded slips. | Student p. 4; 15–25 minutes. |

These timing ranges are planning estimates. For only five spare minutes, pull out one obstruction or pair of words, or ask for a random-walk prediction. Start with objects and a short launch, and stop when the child has an explanation worth sharing. General formulas and return-time algebra are optional. Independent reading is useful but not essential with adult support; no calculus, probability notation, or prior knowledge of matching theory is needed.

The facilitator guide has the detailed launch, hints, solutions, and stopping points. The format draws on *Math Circle by the Bay*, preface printed pp. ix–x (local PDF pp. 10–11), where the authors describe keeping challenging problems ready, manipulatives, revisiting explanations, and varying depth across ages. The exact mathematical tasks and timings here are our adaptations.

## What is new compared with the core hour

**X1 goes beyond the global invariant.** The new connected, hole-free 14-cell board has equal orientation counts, but four named up cells collectively have only two possible down partners. This forces two unmatched ups and, by balance, two unmatched downs. The illustrated five-blue/four-green packing attains the bound. Children can formulate the general lower bound: a group of k ups with only s neighbors forces at least 2(k−s) gaps in a balanced board. Purple cannot improve it because it splits into blues. This is stronger than repeating the three-gap triangular board.

**X2 asks for distances between arbitrary states.** On the 1,3,3,1,3,3 hexagon, words with three R's and three L's encode all twenty tilings. The extreme distance is nine. The pair LRRRLL / RRLLLR has equal inversion scores but distance four, motivating a stronger statistic: sum the absolute changes in positions of the ordered L tokens. A lower bound plus a constructive procedure proves the general distance formula. The core six-state example becomes a family, rather than just a larger list of pictures.

**Returning-child route:** [Lowell Handout 5](../lowell-math-circle-year-1/lowell-math-circle/Math%20Circle%20Fall%202025/Handouts%205.docx), problems 5.5–5.6, already asks for orders of three cookies of each type and paths with three east and three north steps. If recognized, reuse the child's counting argument and move directly to X2's distance questions or X3's counting of routes between tilings. Record the prior counting as recalled, and identify which new question was explored; the saved handout does not establish every child's attendance or mastery.

**X3 counts histories, not configurations.** Shortest routes become increasing histories of left-justified rows in a 3×3 square. The record (x1,x2,x3) counts how many R tokens each L has crossed; the constraints are 3≥x1≥x2≥x3≥0. Each record's route count is the sum of its legal predecessors. There are twenty records but forty-two shortest histories. The two-R/four-L follow-up has fifteen words, fourteen shortest routes, and distance eight. Standard Young tableaux provide an adult continuation; no hook-length formula is needed for the finite proof.

**X4 makes the random rule part of the problem.** It returns to the original six-state graph, so children need not build a twenty-state graph before investigating probability. Choosing legal neighbors uniformly gives degree-proportional visit frequencies. Choosing uniformly among four fixed edge labels, with unsuccessful choices counted as stays, gives uniform visit frequencies. Counting stays and replacing the randomizing slips are explicit. The sharing argument proves stationarity; a short tally is not presented as a proof of asymptotic behavior. Mean positive returns of twelve versus six at A are optional further questions.

## Source trail and limits of attribution

- **Matching:** Oscar Levin, [*Discrete Mathematics: An Open Introduction*, fourth edition, §2.7](https://discrete.openmathbooks.org/dmoi4/sec_matchings.html), especially Theorem 2.7.1. The 14-cell board is our checked construction; the subset-neighbor shortage is the necessary part of Hall's condition. The student proves its elementary lower bound, not the sufficiency theorem.
- **Tilings, lattice paths, and counting:** Alexander Postnikov's [MIT 18.312 course](https://math.mit.edu/~apost/courses/18.312-2005/) includes domino tilings, Hall's theorem, and plane partitions/rhombus tilings in lectures 20–23. The explicit H133 instance, pair of words, and recurrence table are our constructions and calculations.
- **Research continuation:** Saldanha–Tomei, [*An overview of domino and lozenge tilings*](https://arxiv.org/pdf/math/9801111), §3, Theorems 3.1–3.2, describes connectivity and height-based distances for the relevant simply connected regions. The elementary single-ribbon proof here specializes to hexagons with one boundary edge of length one. Do not assume one ribbon encodes every arbitrary lozenge region. The earlier [research notes](week-01-research-level-notes.md) also document Thurston and random tiling dynamics.
- **Random walks:** David A. Levin and Yuval Peres, with contributions by Elizabeth L. Wilmer, [*Markov Chains and Mixing Times*, second edition](https://pages.uoregon.edu/dlevin/MARKOV/mcmt2e.pdf). Example 1.12 (printed pp. 9–10) gives degree-proportional stationarity; Propositions 1.19–1.20 (p. 13) give the return-time relation and detailed balance; Theorem C.1 (pp. 390–391) establishes long-run visit averages without requiring aperiodicity. The finite transition rules, sharing calculation, and hitting-time equations in the packet are worked specifically for our six-node graph.

## Verification and maintenance

`python3 plans/week-01-extension-matching.py` checks adjacency from triangle vertices, connectivity and a simple boundary, maximum matching, every subset's deficit, and the optimal packing. Its companion JSON supplies the drawing geometry.

`python3 plans/week-01-extension-checks.py` independently enumerates the H133 tilings and flips, checks the ribbon correspondence and all pairwise distances, and calculates the route table. The script also checks H(1,a,b) for 1≤a,b≤4. Its JSON supplies the large mat, sample ribbon, and recurrence answers.

Build the two extension PDFs with `sh lowell-math-circle-year-2/source/week-01/build-extensions.sh`. This uses pdfLaTeX and the existing visual style without rebuilding the core packet. Print US Letter, single-sided, 100% / Actual Size. Use only 1× blocks for these mats; the larger Upscale pieces would change the allowed tilings. The six-slip version of X2/X3 remains available when blocks are busy elsewhere.

A reviewer who did not author these extensions independently checked maximum matching, word-graph distances, all recurrence values, stationary distributions, return times, and all ten PDF pages. Incorporated feedback fixed initial page overflow, specified reading down each half of the recurrence table, used written units rather than extra physical counters in the sharing model, and added the exact long-run theorem citation. See [the extension review record](../lowell-math-circle-year-2/source/week-01/EXTENSIONS-REVIEW.md).

Record use as F01-X1, X2, X3, or X4, with the actual subquestions attempted. Preparing or printing an extension does not mark it as taught.
