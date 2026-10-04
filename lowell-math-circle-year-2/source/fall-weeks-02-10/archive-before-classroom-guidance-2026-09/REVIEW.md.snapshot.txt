# Weeks 2–10: overall review

## September 20 revision and integration

Implemented the [Weeks 1–10 review](../../../plans/fall-weeks-01-10-review.md), with Weeks 2–4, 5–7, and 8–10 revised by parallel subagents. The coordinator revised Week 1 and shared guides, checked the changed student proof sequences and shared coprime scaffold, updated the use log, and assembled the final print sets. The implementation table in the review maps each recommendation to the resulting change. All activities remain planned.

All 45 individual Weeks 2–10 PDFs were rebuilt. Each week retains **2 / 2 / 3 / 1 / 4** pages, and the five combined PDFs retain **19 / 19 / 28 / 10 / 37** pages. The assembler passed its page-size, text, glyph, bounds, and one-page-extra checks on every individual and combined PDF. A separate integration check compared all 108 appended pages against the current weekly files: both extracted text and uncompressed drawing streams are identical. All nine bookmark destinations in each combined set agree with its contents ranges. The five new September 20 covers were rendered and visually inspected.

Fresh visual checks by the revising agents covered all 36 pages of Weeks 2–4 and all 36 pages of Weeks 8–10, plus the 12 changed pages in Weeks 5–7. The coordinator additionally inspected the revised upper pages for Weeks 5, 6, 9, and 10. The remaining unchanged Weeks 5–7 pages retain their earlier review; they are not claimed as freshly inspected. All changed pages fit without clipping or overlap. No current build has overfull/underfull boxes. Existing Computer Modern size-substitution warnings remain in Week 3 K–1, Week 4 K–1, and Week 6 K–1/middle; their inspected symbols and code labels have no visible defect. Local review records document those warnings.

All nine weekly mathematical checkers and `independent-checks.py` passed. Additional direct checks verified the exact five printed Week 5 alternative cities and three-clue candidates, Week 6 coordinatewise color renaming and score obstructions, and Week 10's new physical loop-splicing example. The coordinator reviewed the general subtraction argument separately from finite computations. Relevant local MSRI teaching passages and Lowell Handout 5's prior counting were reread; new scaffolds and timing choices are identified as adaptations.

Week 1's seven PDFs were also rebuilt separately; all pass the same structural checks, with fresh visual inspection of the three edited PDFs. See its core and extension review records. This yields **57 rebuilt PDFs** for the whole revision, including the five combined sets, with no increase in printing length.

The original September 19 review follows and describes its own validation scope.

Completed September 19, 2026. This is the coordinating agent's review of the nine packets produced by three authoring agents. Each author's review is also saved in its weekly source folder. These materials are **prepared, not taught**; page counts and mathematical checks do not establish classroom pacing or children's readiness.

## Deliverables and scope

There are 45 individual PDFs: five for each of nine weeks. Every week has two K–1 pages, two grades 2–3 pages, three grades 4–5 pages, **one grades 6–7 extra page**, and four facilitator pages. That is 108 distinct weekly pages. Five consolidated, bookmarked print sets add one contents page each: 19 / 19 / 28 / 10 / 37 pages, respectively. The [print index](README.md) links all files, editable sources, detailed weekly plans, and research references.

The active fall plan, activity overview, source-format notes, and use log now agree with these packets. Earlier proposals were archived before replacement. Week 1's files were used as the benchmark and were not edited by this batch. Optional extras have their own activity IDs; planning a page does not mark it as used.

## Mathematics and source review

The coordinator read all nine facilitator guides and compared their student tasks, solutions, and scope. The authoring agents checked primary or author-hosted undergraduate/research sources and recorded titles plus page, theorem, problem, or section references in the weekly plans. Research connections are distinguished from what a child is asked to establish. A conjecture stated in a historical paper is not presented as a verified current open problem.

The coordinator separately consulted the local MSRI books and relevant Lowell handouts. The source-format notes identify the book evidence behind concrete launches and problems that grow toward advanced mathematics; the proposed classroom adaptations are identified as proposals. In particular, Lowell's subtraction-game references are Handouts 2.3 and 3.1–3.3, and prior material is evidence of related preparation, not a complete attendance or use record.

All nine weekly verification programs were run successfully. The coordinator also wrote and ran a separate [independent finite-model check](independent-checks.py), covering cycle-toggle states and complementary press sets, maximum permutation orders, modular orbits and the eight-card shuffle, optimal adaptive binary queries, five-bit separating probes, subtraction positions, three-pile Nim, Wythoff positions, and integer billiard endpoints. These computations supplement the explanations rather than replacing proofs.

Points checked especially carefully:

- **Week 2:** parity is required in each connected component; cycle solutions occur in complementary pairs; the tree argument explains both existence and uniqueness without repeated presses.
- **Week 3:** exhaustive permutation checks agree with the loop/partition proof, including maximum orders 6 for five symbols and 15 for eight.
- **Week 4:** the fixed-step orbit length is `n/gcd(n,k)`; the eight-card out-shuffle has order three under the stated deal convention.
- **Week 5:** all 12 order-three and 576 order-four Latin squares were checked. The five-clue set is irredundant but not minimum; a three-clue set specifies the same target. The extra's entry-clue model is separate from perimeter visibility clues.
- **Week 6:** exact-position binary feedback is the stated game. Identifying a code is distinguished from submitting a final winning query. Optimal worst-case query counts are 2, 3, and 4 for lengths 2, 3, and 4; the adaptive lower-bound argument is stronger than merely counting possible answers.
- **Week 7:** losing-position proofs require both that no move joins two losing positions and that every other position can reach one. Eventual periodicity is not inferred solely from a short table.
- **Week 8:** the three-pile rule is binary XOR, not parity of the total. The counterexample `(1,1,2)` exposes that difference. The Wythoff extra separates a no-move-between-listed-positions argument from the additional completeness claim.
- **Week 9:** reduced side lengths, rather than unreduced side parity, determine the ending corner. Bounce counts omit the final corner. The extra distinguishes missing corners from density of an orbit.
- **Week 10:** connected networks, Euler trails, repeated-edge costs, and the no-self-loop scope are explicit. An independent shortest-walk search confirms the closed/open unit-K4 costs 8/7 and the weighted closed-route optimum 23; examples attain the bounds. The extra optimizes pairings of shortest-path distances, not merely individual roads.

## Print and visual review

The authoring agents rendered and visually reviewed every page. The coordinator independently inspected all 108 weekly pages: 63 core student pages, nine extras, and 36 facilitator pages. Changed pages were rerendered and reviewed after corrections; the final minor Week 3/4 facilitator spacing adjustments were checked by their author. The coordinator also inspected all five final contents pages.

All PDFs are US Letter. Automated checks verify nonempty extractable text, no replacement characters, safe character bounds, and the extra-page limit. LaTeX diagrams remain vector artwork. Final author build logs have no overfull/underfull boxes or LaTeX warnings. Consolidated sets preserve the weekly pages and provide nine week bookmarks; contents ranges include the cover as page one.

Review led to concrete corrections: two extras were compressed to one page; a middle-level overflow was removed; malformed WEEK headers were fixed; writing tables and the weighted-route diagram were enlarged; a misleading Nim conjecture gained a counterexample; the minimum-clue comparison was clarified; “Euler trail” replaced ambiguous terminology; a prior-use reference and obsolete wheel-preparation note were corrected. Contents-page fonts are embedded to avoid viewer-dependent substitution.

## Use in the room

Give one page at a time and start with materials. The packets are menus of investigations, not promises that every task fits an hour. The facilitator guides state prerequisites, timing, launch questions, hints, solutions, and when to offer the extra. Record the actual puzzles used and reasoning reached in the [use log](../../../plans/fall-k-5-year-a-use-log.md), especially when a child continues into a higher level. The six-year library will need further varied sessions and evidence from teaching; this batch is one substantial fall sequence.
