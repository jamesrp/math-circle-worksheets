# Week 3: Shuffle machines

Concrete revision of October 3, 2026: F03-K-v5 / F03-M-v5 / F03-U-v5, adult guide F03-FAC-v5. **Unpiloted.** It follows the organizer's report on Weeks 1 and 2 (the October 3 forecast and pivot, a private record: see [LOCAL-RESOURCES.md](../../../LOCAL-RESOURCES.md#private-records)): rules enforced by the materials or by the other player, partner play at fixed KK11 / 3333 / 445 tables, and deeper questions late in each packet.

- [K–1](../../week-03/week-03-k-1.pdf) — 10 pages.
- [Grades 2–3](../../week-03/week-03-grades-2-3.pdf) — 11 pages.
- [Grades 4–5](../../week-03/week-03-grades-4-5.pdf) — 8 pages.
- [Adult guide](../../week-03/week-03-facilitator.pdf) — 11 pages: materials and counts, launch, pairing, answers, hints, and what to record.

October 23, 2026: guide-only corrections from the [review card](../../../plans/review/week-03.md). The floor launch is now one loop, chairs 1 → 2 → 3 → 1, with chairs 4 and 5 on straight arrows, home after 3 switches, so it no longer shows the result that machines can take more turns than they have slots. Spare test mats are K–1 page 10 (no problem text), for 4- and 5-slot machines only; larger machines are traced with a finger. Section 1 now states the facts children can reach, the 4–5 referee may trace loops, and 4–5 Problem 10 lays 52 cards in four rows of 13. `guide-src/check_answers.py` checks the new launch. Student packets are unchanged; the previous guide is in `week-03/archive-before-card-fixes-2026-10-23/`.

Permutations as printed arrow mats. One turn moves every object down its own arrow, then the bottom row slides straight up, so the mat enforces the rule that the old letter-key version left in children's heads. Children count turns until everything is home, find loops, build machines with chosen return times, undo and combine machines, and (grades 4–5) treat perfect card shuffles as machines.

The mat slots are about 1.2 inches, too small for most pattern blocks; the block pictures above the slots are labels. Use snap cubes or other small objects in matching colours (the adult guide gives counts). The whole-group launch uses five chairs and a taped floor arrow map. Two decks of cards for the 4–5 table.

Print US Letter, single-sided, at 100% / Actual Size. Give one page at a time; the packets hold more than an hour, and stopping anywhere is fine.

The student pages were drafted with the [worksheet workflow](../../../worksheet-workflow/README.md) from the outline `worksheet-workflow/outlines/week-03-shuffle-machines.md`: writer, adversarial review and independent math check, then revision. The run record (prompts, reviews, draft and final PDFs) is in `tmp/worksheet-runs/week-03-shuffle-machines-v1/`. The adult guide was written separately from the final pages; its answers are recomputed by the scripts in `guide-src/`.

Rebuild from the repository root: `sh lowell-math-circle-year-2/source/week-03/build.sh`. It builds in `tmp/pdfs/week-03-build/` and copies the four PDFs into `lowell-math-circle-year-2/week-03/`. Requires Python 3 and pdfLaTeX with TikZ and Source Sans Pro. `src/` holds the student pages with their generators and checks; `guide-src/` holds the adult guide and its answer checks, which read `../src`.

The previous version (F03-*-v4 (September 30 concise revision), with its optional grades 6–7 extra) is preserved in [archive/](archive/README.md) with its sources, and its PDFs are in `lowell-math-circle-year-2/week-03/archive/`. Older versions remain in the `archive-before-*` folders here and beside the PDFs.
