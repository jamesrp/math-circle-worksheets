> Historical pre-shared snapshot. Current Week 2 is the [shared collection](../README.md). The build scripts in this archive write only to the matching PDF archive; their paths have been adjusted for this folder.

# Week 2: Pair switches and cheapest repairs

Revised September 27, 2026, applying the [Week 1 classroom guidance](../../../../plans/week-01-classroom-review.md). **All v3 revisions are unpiloted.** The [weekly plan](../../../../plans/week-02-redesign.md) distinguishes source lessons, classroom evidence from Week 1, and design proposals for this week. Previous sources and PDFs are preserved in their separate `archive-before-classroom-guidance-2026-09/` folders.

## September 28 K–1 companion and current room plan

**Current roster: KK1 / 3333 / 445 (ten children), with three adults.** The parent anchors K–1 using the new script; the other mathematician anchors the four third graders; the organizer anchors grades 4–5. The [auxiliary plan](../../../../plans/week-02-k1-aux.md) supplies the current K–1 route and help handoff. The original K–1 core remains a reserve. No auxiliary activities have been reported taught.

- [K–1 auxiliary: lamp adventures, shape drawing, and room making](../../../week-02/archive-before-shared-collection-2026-09-28/week-02-k-1-aux.pdf) — **14 pages / 24 problems**, F02-K-AUX-v1. Solo boards, partner puzzles, six/eight/nine-lamp networks, invented graphs, shape drawing, room counts, and two-/three-mark map puzzles.
- [K–1 auxiliary parent guide](../../../week-02/archive-before-shared-collection-2026-09-28/week-02-k-1-aux-facilitator.pdf) — **8 pages**, F02-K-AUX-FAC-v1. Short launch script, five-page default route, management of three children, numbered diagram keys, solutions for every problem, optional deeper questions, and source notes.

**Suggested K–1 printing:** three copies each of auxiliary pages **1, 2, 3, 10, 11** (15 sheets); show only one page at a time. Page 9 can replace a room page if closed-shape drawing needs practice. Other pages are reserves: select likely ones before class or show a master and draw the board on a tablet. Do not rely on a printer during the meeting. The parent can read the guide digitally or print it separately.

**Supplies:** pencils with erasers, or whiteboard tablets with their usual markers/erasers. Small erasable dots are the lamp states; all large working boards are printed blank so every ON mark can be erased. Existing two-sided counters are optional. Drawing pages also work with ordinary pens. No construction pieces, ruler, colored pens, cutting, or new accessories are required. Older groups need **31 two-sided counters plus spares** (four per third grader, five per upper child).

The auxiliary is a separate choice library; it is **not inserted into the combined K–1 packet**. Start the older children on their current core page 1. Ten initial sheets means three auxiliary starts, four middle starts, and three upper starts. The six-page main facilitator is now F02-FAC-v5: current staffing on page 1, core proofs on pages 2–5, and middle/upper visual-task notes on page 6.

## Core print files

- [K–1](../../../week-02/archive-before-shared-collection-2026-09-28/week-02-k-1.pdf) — 3 pages, F02-K-v3. Adjacent/opposite pairs, undoing, several odd targets, then one changed switch.
- [Grades 2–3](../../../week-02/archive-before-shared-collection-2026-09-28/week-02-grades-2-3.pdf) — **8 pages, F02-M-v4**. One investigation per page, local working mats, pictured targets, before/after trials, drawn paths, and a collection recorded on rings.
- [Grades 4–5](../../../week-02/archive-before-shared-collection-2026-09-28/week-02-grades-4-5.pdf) — **12 pages, F02-U-v4**. Local mats and pictured targets; selected-road diagrams for complements; two modeled first-edge decisions before independent forced-choice trials.
- [Optional extra, roughly grades 6–7](../../../week-02/archive-before-shared-collection-2026-09-28/week-02-extra-grades-6-7.pdf) — 3 pages, F02-X-v3. Disconnected targets, a bridge, overlapping paths, then a concrete tree and cut counts.
- [Facilitator](../../../week-02/archive-before-shared-collection-2026-09-28/week-02-facilitator.pdf) — **6 pages, F02-FAC-v5**. Whole-group launch, prerequisites, flexible hour, stopping choices, full proofs, solutions for added examples, source lineage and observation prompts.

Print US Letter, preferably single-sided and Actual Size. Grade labels are approximate; the auxiliary needs no independent reading. Pointing, adult reading and scribing are valid entry points. Use the September 28 printing and materials guidance above in place of the earlier seven-child arrangement.

The shared sequence allows handling materials first, then one brief whole-group legal attempt and demonstrated record, before different starting tasks. Later representations are introduced after the concrete comparisons that give them a purpose. The mathematical explanations remain in the guide for adult conversation when children are ready.

## Middle and upper: September 28 visual revision

The [visual revision record](../../../../plans/week-02-visual-review.md) explains the organizer's printed-page feedback and the proposed shared collection. **This pass keeps the three sets and their mathematics.** The shared, ungraded collection is a proposal to discuss before implementing.

Middle Problems 1–8 are on pages 1–8 respectively. Upper Problems 1–3 are on pages 1–3; Problem 4 on pages 4–5; Problem 5 on page 6; Problem 6 on pages 7–8; Problems 7–10 on pages 9–12. Page counts provide working space and visible references, not a requirement to complete more content. Start with page 1; select later pages after children can replay the rule. Keep middle pages 2–3 and upper page 2 handy for initial target experiments. Pointing and adult recording can replace handwriting.

Every physical investigation now has a local working mat. Middle Problem 4 explicitly permits setting up the one-ON experimental start by hand. In Problem 7, check “saved” beneath a recorded ring, including the all-OFF state, to distinguish it from an unused ring. In upper Problems 4–5, thick roads show presses while dark lamps show states. Problems 6–8 model a first decision and include the closing-lamp check. In Problem 9, the second list uses the lines omitted from the first, so it is a genuinely different line set rather than a reordering.

The prior middle/upper v3 packets and core facilitator v4 are archived under `archive-before-visual-revision-2026-09-28/`, alongside matching output and combined-output archives.

## Build and check

Run `sh lowell-math-circle-year-2/source/week-02/build.sh` from the repository root. The build runs `verify.py`, compiles all five core TeX files twice, and copies PDFs to `lowell-math-circle-year-2/week-02/`. Intermediates stay in `tmp/pdfs/week-02-build/`. It then runs `build-k1-aux.sh` for the two separate auxiliary PDFs. Core builds require Python 3 and the existing pdfLaTeX/TikZ setup. The auxiliary uses the bundled Python with ReportLab; set `AUX_PYTHON` to another Python with ReportLab if needed.

To rebuild only the auxiliary, run `sh lowell-math-circle-year-2/source/week-02/build-k1-aux.sh`. Editable builders are `build-k1-aux.py` and `build-k1-aux-guide.py`; diagrams and exact instances live in `plans/week-02-k1-aux-data.json`. Its independent checker, `plans/verify-week-02-k1-aux.py`, verifies reachability, one-light walks, room counts and mark assignments, saving results beside the plan.

The previous main facilitator is preserved in `archive-before-k1-aux-2026-09-28/` under both source and printable folders. The prior combined facilitator is likewise archived. Rebuild only the combined core facilitator with the bundled Python and `lowell-math-circle-year-2/source/fall-weeks-02-10/assemble.py --level facilitator`.

The independent mathematical checker covers all retained example targets, paths, complements and closure cases; v4 changes their presentation, not their solutions. [REVIEW.md](REVIEW.md) records rendered-page QA and its limits. Record only activities actually encountered in the shared [use log](../../../../plans/fall-k-5-year-a-use-log.md), with exact examples and whether results were tried, conjectured, checked in cases, proved or supplied.
