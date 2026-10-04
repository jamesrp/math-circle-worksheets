# Week 8: Rook moves, Nim, and changing the losing set

Revised September 27, 2026 in response to the [Week 1 classroom review](week-01-classroom-review.md) and the adopted AGENTS.md guidance. **F08-K/M/U/X-v3 are prepared, unpiloted revisions.** No observations about a Week 8 session have been supplied. The previous v2 source and PDFs are preserved separately in the weekly `archive-before-classroom-guidance-2026-09/` directories.

## What changed, and why

Rook and pile games now get repeated equal/unequal trials before a trap map. The board-to-piles correspondence is acted out before use. Three-pile play and the complete six-reply experiment precede grouping counters into binary bundles; several separate bundle records precede the repair algorithm. Wythoff now has concrete play, a full classification grid, and a later greedy-pair record on separate pages.

These changes infer what may help from the organizer's reported Week 1 experience: sufficient contrasting work, explicit actions, and records introduced for a purpose. They are proposals, not claims that these new sequences succeeded with children. Formal generalizations, hints and discretionary proof follow-ups are in the [six-page facilitator guide](../lowell-math-circle-year-2/week-08/week-08-facilitator.pdf); numbered student problems state concrete actions with the space/diagrams needed to perform them.

## Entry points and mathematical work

Grades are approximate. Choose by prerequisites; read aloud, scribe and accept oral or drawn explanations. The additional pages provide flexible continuations, not a one-hour completion quota.

| ID | Pages | Prerequisites | Concrete sequence |
| --- | --- | --- | --- |
| F08-K-v3 | 3 | Adult read-aloud; compare small distances and count to 3; follow and copy a turn. | Immediate win versus center; equal versus unequal board starts; physical matching with two piles. |
| F08-M-v3 | 4 | Short read-aloud instructions; counts to 7; distinguish a played outcome from a forced result. | Eight board starts before mapping; enact slides as pile removals; equal-pile replies; all six first moves from (1,2,3). |
| F08-U-v3 | 5 | Small subtraction and parity; 4/2/1 and then 8 bundles are built, not assumed. | Actual games and counterexamples; six replies before binary; build bundle records; test four cases; repair and design balanced starts. |
| F08-X-v3 | 3 | Organized lists and subtraction; optional calculator/floor/square-root notation supplied at the end. | Four concrete starts; triangular T/W grid through 7; greedy pairs after classified games; separately supplied golden-ratio theorem. |

## Materials, launch, and flexible hour

About 60 counters, five plates or pile areas, pencils, and scraps labeled 1, 2, 4, 8. Reset and reuse the printed counter-sized mats. Middle page 3 reuses its earlier rook board.

**Print a starting set:** page 1 of the appropriate level for each child (3 K–1 + 3 middle + 1 upper = **7 starting sheets**), with one master of each continuation and the optional three-page extra. Copy additional pages as needed and offer one at a time. The complete core packet lengths are 3/4/5 pages; the full roster set would be 26 sheets, but is not the default print instruction. Use US Letter, single-sided, actual size. No activity depends on physical scale calibration.

**Whole-group launch:** After time handling counters, gather at one visible rook board. Demonstrate short and long right/down moves, invite a child to make a legal move, and show recording the start and finish. Reach the star once. Distribute starting pages only after everyone knows the action. Show one corresponding pile action: from rook distances (2,1), slide right one and remove one from a matching 2-counter pile beside a 1-counter pile. State the one-pile removal rule and taking-last wins, without announcing the matching strategy. The full correspondence is investigated later.

**Proposed hour:** 0–10 handle materials; 10–15 short common action-and-record demonstration; 15–35 concrete attempts; 35–40 movement/reset; 40–55 revisit, compare or continue at the child's current stage; 55–60 share one result and tidy. Change this rhythm to fit actual exploration. Parent mainly supports K–1; organizer alternates middle/upper about every five minutes and leaves a specific next attempt. The upper child receives actual adult mathematical conversation. Roles rotate so each child acts.

## Stopping points and proof continuations

| Group | Satisfying stop | Optional facilitator continuation |
| --- | --- | --- |
| K–1 | Two center moves and replies, then contrasting equal/unequal starts. | Match arbitrary equal piles and explain why replies stay legal. |
| 2–3 | An argued board pattern or enacted board/pile correspondence. | Both directions of the equal-pile proof and termination; six three-pile replies if ready. |
| 4–5 | A complete six-reply experiment, or a legal bundle-balancing move. | No move connects balanced states, every unbalanced state can be repaired, and decreasing total forces termination. |

Do not require every table cell, map or page. Demonstrate each unfamiliar record once with the real objects. When a representation is causing copying rather than helping compare attempts, scribe or return to objects. Preserve both construction and explanation; the guide keeps complete arguments so they are available when children are ready.

## Observation plan and reuse

After the session record which exact pages/instances children attempted, what they tried, what needed adult rescue, what they explained and what they wanted to continue. Label adult hypotheses separately from observed behavior. Distinguish a child's explanation from a supplied theorem. Unused stages remain prepared reserves; do not mark a whole printed packet as taught. The existing use log records actual use; this revision makes no new teaching claims.

## Verified mathematical backbone

The rook state is the pair of remaining horizontal/vertical distances. A move reduces exactly one coordinate. Equal pairs are losing: every move breaks equality and every unequal pair can restore equality by reducing its larger coordinate. The total strictly decreases. This establishes both directions and termination.

Three piles change the question. (1,1,1) is winning by removing a pile; (1,1,2), despite even total, is winning by removing the 2-pile. For (1,2,3), each of its six first moves has a response leaving two equal piles and one empty pile; the facilitator prints all six.

For any number of piles, write binary digits and add each column modulo 2. A legal single-pile move changes at least one column, so zero XOR cannot remain zero. If XOR s is nonzero, choose a pile x with a 1 in the highest 1-bit of s, and replace it by x XOR s. All higher bits stay fixed, the highest changed bit drops, and lower bits total less than its value; therefore the pile strictly shrinks. New XOR is zero. This is both a proof and a winning-move algorithm.

Checked upper starts: (2,4,6) and (3,5,6) are balanced; moves (3,4,5)→(1,4,5), (1,5,7)→(1,5,4), (7,10,12)→(6,10,12) restore balance. For any first two piles, the unique balancing third is their XOR.

The extra's sorted losing pairs through 7 are (0,0),(1,2),(3,5),(4,7); greedy rows n=4,5 give (6,10),(8,13). Distinct pairs have disjoint coordinates and distinct differences, so no legal move joins them. That argument alone does **not** prove every outside position reaches the list. The golden-ratio formula is supplied as a known theorem, not inferred from a short table. Extra examples move (2,4)→(2,1), (5,8)→(4,7), (8,12)→(6,10).

## Sources and boundary between class and research

- JRMF, *Rook’s Move Activity Guide*, local PDF pp. 3–6: exact rook rule, losing-position strategy, and Wythoff link. The three-pile sequence is our adaptation.
- Charles L. Bouton, *Nim, a Game with a Complete Mathematical Theory*, *Annals of Mathematics* 3 (1901–02), pp. 35–39. [Primary historical paper hosted at Caltech](https://paradise.caltech.edu/ist4/lectures/Bouton1901.pdf). The paper’s historical binary analysis motivates the connection; the normal-play proof used here is provided independently in the guide.
- Aviezri S. Fraenkel and Udi Peled, *Harnessing the unwieldy MEX function*, *Games of No Chance 4*, MSRI Publications 63 (2015), pp. 77–94. [Primary research chapter](https://library.slmath.org/books/Book63/files/131104-Fraenkel-2.pdf), §1 pp. 77–78 for Wythoff rules, greedy pairs, and the floor formulas; §5 for algorithms for generalized sequences. The activity reaches complementary sequences and computational questions; it does not reproduce that algorithm.

Undergraduate homes: impartial combinatorial games, induction on a decreasing state measure, invariants, binary arithmetic, addition over the two-element field. Historical research is solved mathematics; no claim is made that this classroom problem is currently open.

For pedagogy, re-read *Math Circle by the Bay*, preface printed pp. viii–x (PDF 9–11): common themes with varying depth, manipulatives, explanations, and reserve challenges. Also re-read Rozhkovskaya, Lesson 3 “At the lesson” (`part0013.xhtml`) for attempts before an organizing display; Lesson 7 (`part0017.xhtml`) for verifying legal-move understanding; and Lesson 8 (`part0018.xhtml`) for unequal copying pace. Our preprinted material, adult rotations, and particular task sequence are adaptations, not arrangements reported by those sources. See [lesson-format-source-notes.md](lesson-format-source-notes.md).

## Returning children and future branches

Lowell Handout 2 problem 2.3 and Handout 3 problems 3.1–3.3 (moves 1–3 and 1–5), and Week 7 are related through winning/losing positions. Here arbitrary removal from one pile, simultaneous multiple piles, and XOR are the new representation and argument. The old upper king variant remains an available reserve, and Wythoff moves from an old long-term reserve onto the optional extra. Record exact starts and whether Wythoff was actually attempted. Update the [use log](fall-k-5-year-a-use-log.md) after teaching, recording exactly which packet pages and instances each child encountered; prepared reserves stay untaught. Preserve an oral explanation as a brief adult note when writing is a barrier.

## Verification and outputs

Backward recursion checks 2,197 three-pile positions, 169 two-pile positions and 961 Wythoff positions. Added v3 assertions check the six replies to (1,2,3), three repairs of (4,6,7), balancing third piles and new Wythoff moves. Finite checks support the printed cases; general proofs remain in the facilitator guide.

Run `python3 lowell-math-circle-year-2/source/week-08/verify.py`, then `sh lowell-math-circle-year-2/source/week-08/build.sh`. The five PDFs are written to `lowell-math-circle-year-2/week-08/`; editable TeX sources remain in the weekly source folder and intermediates in `tmp/pdfs/`. The [print index](../lowell-math-circle-year-2/source/week-08/README.md) and [review record](../lowell-math-circle-year-2/source/week-08/REVIEW.md) record final page counts and checks.
