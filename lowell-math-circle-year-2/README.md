# Lowell Math Circle — year 2

Start here to print. Current PDFs are organized by week; editable files and build instructions are in [source/](source/README.md). Session plans and the use log remain in the top-level [plans/](../plans/README.md).

Print US Letter, single-sided, at 100% / Actual Size. Give one page at a time and keep facilitator solutions separate. Grade bands are entry points; extras are optional. These are prepared materials; actual use and classroom feedback are recorded separately in the use log.

## Weekly print packets

| Week and preparation notes | K–1 | Grades 2–3 | Grades 4–5 | Optional extras | Facilitator |
|---|---|---|---|---|---|
| [1. Tiling, impossibility, and flips](source/week-01/README.md) | [PDF](week-01/week-01-k-1.pdf) | [PDF](week-01/week-01-grades-2-3.pdf) | [PDF](week-01/week-01-grades-4-5.pdf) | [PDF](week-01/week-01-extensions.pdf) | [PDF](week-01/week-01-facilitator.pdf) |
| [2. Switches and lamps](source/week-02/README.md) | [PDF](week-02/week-02-k-1.pdf) | [PDF](week-02/week-02-grades-2-3.pdf) | [PDF](week-02/week-02-grades-4-5.pdf) | [PDF](week-02/week-02-extra-grades-6-7.pdf) | [PDF](week-02/week-02-facilitator.pdf) |
| [3. Repeating secret machines](source/week-03/README.md) | [PDF](week-03/week-03-k-1.pdf) | [PDF](week-03/week-03-grades-2-3.pdf) | [PDF](week-03/week-03-grades-4-5.pdf) | [PDF](week-03/week-03-extra-grades-6-7.pdf) | [PDF](week-03/week-03-facilitator.pdf) |
| [4. Around the ring](source/week-04/README.md) | [PDF](week-04/week-04-k-1.pdf) | [PDF](week-04/week-04-grades-2-3.pdf) | [PDF](week-04/week-04-grades-4-5.pdf) | [PDF](week-04/week-04-extra-grades-6-7.pdf) | [PDF](week-04/week-04-facilitator.pdf) |
| [5. Tower cities](source/week-05/README.md) | [PDF](week-05/week-05-k-1.pdf) | [PDF](week-05/week-05-grades-2-3.pdf) | [PDF](week-05/week-05-grades-4-5.pdf) | [PDF](week-05/week-05-extra-grades-6-7.pdf) | [PDF](week-05/week-05-facilitator.pdf) |
| [6. Code-breaking with guarantees](source/week-06/README.md) | [PDF](week-06/week-06-k-1.pdf) | [PDF](week-06/week-06-grades-2-3.pdf) | [PDF](week-06/week-06-grades-4-5.pdf) | [PDF](week-06/week-06-extra-grades-6-7.pdf) | [PDF](week-06/week-06-facilitator.pdf) |
| [7. Take-away games](source/week-07/README.md) | [PDF](week-07/week-07-k-1.pdf) | [PDF](week-07/week-07-grades-2-3.pdf) | [PDF](week-07/week-07-grades-4-5.pdf) | [PDF](week-07/week-07-extra-grades-6-7.pdf) | [PDF](week-07/week-07-facilitator.pdf) |
| [8. Rooks and piles](source/week-08/README.md) | [PDF](week-08/week-08-k-1.pdf) | [PDF](week-08/week-08-grades-2-3.pdf) | [PDF](week-08/week-08-grades-4-5.pdf) | [PDF](week-08/week-08-extra-grades-6-7.pdf) | [PDF](week-08/week-08-facilitator.pdf) |
| [9. Bouncing paths](source/week-09/README.md) | [PDF](week-09/week-09-k-1.pdf) | [PDF](week-09/week-09-grades-2-3.pdf) | [PDF](week-09/week-09-grades-4-5.pdf) | [PDF](week-09/week-09-extra-grades-6-7.pdf) | [PDF](week-09/week-09-facilitator.pdf) |
| [10. Bridges and delivery routes](source/week-10/README.md) | [PDF](week-10/week-10-k-1.pdf) | [PDF](week-10/week-10-grades-2-3.pdf) | [PDF](week-10/week-10-grades-4-5.pdf) | [PDF](week-10/week-10-extra-grades-6-7.pdf) | [PDF](week-10/week-10-facilitator.pdf) |

Week 1 also has an [extension facilitator guide](week-01/week-01-extensions-facilitator.pdf) and [optional paper rhombi](week-01/week-01-extra-rhombi.pdf). The [classroom snapshot](week-01/archive-classroom-2026-09/) preserves the pre-September-27 packets. Its four earlier draft PDFs are preserved separately in `week-01/archive-v1/`; use the current PDFs above unless deliberately revisiting that [archived design](source/week-01/archive-v1/README.md).

## Combined Weeks 2–10 packets

These have contents pages and week bookmarks. They do not include Week 1.

- [K–1](combined/fall-weeks-02-10-k-1.pdf)
- [Grades 2–3](combined/fall-weeks-02-10-grades-2-3.pdf)
- [Grades 4–5](combined/fall-weeks-02-10-grades-4-5.pdf)
- [Optional grades 6–7 extras](combined/fall-weeks-02-10-extra-grades-6-7.pdf)
- [Facilitator guides and solutions](combined/fall-weeks-02-10-facilitator.pdf)

## Editing and rebuilding

The [ten random atlas investigations](../plans/atlas/worksheet-trial/README.md) are a separate worksheet trial: [student book](combined/atlas-random-ten-student-worksheets.pdf) and [facilitator guide](combined/atlas-random-ten-facilitator-guide.pdf). They range from concrete networks and games to calculus, with explicit prerequisites. They are not assigned to weeks; use the contents to print a selected investigation.

The [remaining eighty investigations](../plans/atlas/worksheet-expansion/README.md) continue that library across algebra/discrete mathematics, geometry/analysis, and probability/applications. Each subject has separate student and facilitator books; the [page finder](../plans/atlas/worksheet-expansion/INDEX.md) links all six PDFs and gives exact ranges and prerequisites for selected investigations. [Expansion build instructions](source/atlas-remaining/README.md) describe their editable sources and review workflow.

The [mathematics atlas](../plans/atlas/README.md) adds two separate facilitator planning books: [investigation plans](combined/math-atlas-investigation-plans.pdf) and [research map](combined/math-atlas-research-map.pdf). These cover many prerequisite levels and are not weekly student packets. Use their page contents and bookmarks to print selected investigations. [Atlas build instructions](source/atlas/README.md) describe their separate data-driven builders.

Edit the LaTeX under `source/week-NN/`, then run that folder's build script. It writes to the corresponding `week-NN/` print folder and leaves compilation files in the project's `tmp/` folder. Rebuild combined packets after changing an individual week. See [build commands and dependencies](source/README.md).

Downloaded originals belong in [external-resources](../external-resources/README.md); the organizer's 2025–26 material stays in [year 1](../lowell-math-circle-year-1/README.md).
