# The worksheet corpus: how it is organized and what "done" means

A product plan by Claude for James, November 3, 2026. Numbers come from [readiness.md](readiness.md), which `python3 catalog/readiness.py` regenerates from the records; rerun it rather than editing figures here. Everything below is a proposal until James says otherwise.

## The answer

**Writing for K–5 is nearly done; proof and packaging have barely started.** The library has 101 themes with pages, theorem-first guides and review cards, 90 atlas families, and 23 more drafts waiting for review. A six-year path of 120 sessions can already be filled from it. But 5 themes have been used with children (3 in the circle), 9 are signed off, and 2 have room plans. By the measure that matters for every goal, a theme that works in a real room, the corpus is about 5% done. More new worksheets would widen the gap, not close it.

## How the corpus is organized

Four layers. The first two exist; the third and fourth are new and are the proposal.

1. **Library.** One store of themes with stable ids (`week-NN` is an id, not a date), each with its band pages, guide, review card and catalog record. Atlas families sit beside the weeks. Drafts sit apart until approved. Nothing is copied out of the library; every other layer is a view.
2. **Strands.** The eight catalog areas, each a prerequisite ladder through the concept map, with three entry levels (K–1, 2–3, 4–5). The same eight strands should drive the app's library regions and ladders and the book's chapters, so a child or adult moves between paper and app by the same map. The six-year path is one walk through the strands.
3. **Collections** ([catalog/collections.toml](../catalog/collections.toml)). A curated list of themes for one use, each with its own bar for done:
   - **Wednesday circle, 2026–27**: this year's sessions, chosen week by week. Done when every session has a room plan, printed packets, a kit under 45 minutes and a use-log line.
   - **Kitchen-table math**: about fifteen light-kit themes for two or three children of different ages and one adult. Done when each has a one-page home plan and has been tried once at home. Home is also where new themes get piloted before the noisier room.
   - **Starter set**: the public front door, twenty themes a stranger can run first. Only taught, signed-off themes qualify, so it fills from the circle collection.
   - **Book, first edition**: five or six themes per strand, chosen after the starter set.
4. **Readiness ladder.** Every theme carries its rung, counted by the report: library → signed off → circle-ready (room plan) → taught → piloted with notes. A collection's done is a rung target for its members. This makes "how far from done" a number that moves each week instead of a feeling.

The [use log](../catalog/use-log.toml) is the record that feeds the ladder, the path and the future worksheet copilot. It did not exist (plans/README linked a file that was never written); it now holds the nine sessions James has reported.

## What done means, with the gap

| Goal | Done means | Today | Gap |
|---|---|---|---|
| Wednesday circle this year | About 20 sessions (if it meets weekly through spring, my assumption), each circle-ready a week ahead and logged afterwards | 6 circle sessions logged, room plans ahead for Nov 4, 11 and 18 | about 18 room plans and use-log lines, one a week |
| Weekend home math | 15 home-table themes with a one-page home plan, each tried once | 3 tried at home, 0 home plans | 15 one-pagers; about 12 home tries |
| Public corpus, K–5 v1 | Starter set of 20 taught, signed-off themes; borrowed-text caveat resolved; a front door (README, explorer, starter PDF) | 0 qualify; 9 signed off; caveat open | about 20 circle sessions of evidence (a school year), plus 2 decisions |
| Breadth, K–5 | Every path session has pages for all three tables; reserves in every strand for a second cycle | 55 of 82 path week-sessions have K–1 pages; games, logic, networks and counting have no reserves | 27 K–1 entries (7 drafted); 4 strands' reserves (12 themes drafted) |
| Review | Nothing waits on James for more than two weeks | 23 drafts and the organizer queue waiting since October 23–25 | one triage pass |
| Grades 6–8 | Not started, by design | 0 | after the starter set |

The binding constraint is the room, not the writing: one circle meets about 20 times a year, so evidence accumulates at one theme a week. The plan therefore points everything at making each Wednesday count (room plans, use log, quick revision from what happened) and at home sessions as a second, faster pilot lane.

## What I did today (November 3)

- [catalog/use-log.toml](../catalog/use-log.toml): the seven reported sessions, with sources. Week statuses are unchanged: "piloted" still needs a classroom report.
- [catalog/readiness.py](../catalog/readiness.py) and its output [readiness.md](readiness.md): the ladder counts by area and by path year.
- [catalog/collections.toml](../catalog/collections.toml): the four collections above as proposals.
- [Draft triage](review/DRAFT-TRIAGE.md) of the 23 drafts waiting on James: 8 adopt now, 10 pilot at home first, 5 hold. Only the 12 new themes can help this year; the return visits and K–1 sets belong to weeks not yet taught.
- A Codex brief, [plans/briefs/readiness-and-collections.md](briefs/readiness-and-collections.md), and its work-board line: validate the new files in `build.py` and show rung and collection in the explorer and CATALOG.md.

## Backlog, in the order I'd do it

Items 1–3 package existing work; 4–6 make new content and wait for James's yes. Item 2 is done.

1. **Room plans one week ahead**, for the circle collection's next sessions: after November 4, bridges (Week 10) on November 18 (no school November 11) and, tentatively, stars and wheels (Week 4) after it. James will probably end the school circle after fall quarter (November 5) and move to informal home sessions, so the circle collection shrinks to the fall and the home-table collection grows. Weeks 5 and 7, first agreed, turned out to be taught on October 21 and are kept as reference plans. James picks each week.
2. **Review triage of the 23 drafts**: done, [DRAFT-TRIAGE.md](review/DRAFT-TRIAGE.md). Its four "adopt now" new themes (Towers from either end, Poisoned cookie, Hidden armies, Hex) are all games, the area the circle has least of.
3. **Use-log habit**: the Wednesday and Friday check-ins add a line after each session; a monthly pass moves taught themes up the ladder and revises from what happened.
4. **Home plans** for the kitchen-table collection, starting with Poisoned cookie, Hex and Pancake flips as home pilots of drafts, and Weeks 7 and 8 (games).
5. **K–1 entries** for path Years 4–6 (27 sessions lack them; 7 drafted).
6. **The book and grades 6–8**, after the starter set has members.

## Decisions

- **November 3, 2026 (later): the pause on new weeks is reverted.** James: near-term circle content is enough, but he wants background progress toward "an entire math corpus up to some level of granularity". New themes are researched and kept as draft markdown plans for weeks 101+ in [plans/drafts/weeks-101-plus/](drafts/weeks-101-plus/README.md): the deep idea, linked sources, a kid-friendly activity idea, bands and an app link, with no student pages or guides until a week is chosen. Room plans, home plans and the review queue keep priority for the circle; the drafts sit below the library on the readiness ladder. Grades 6–8 stay after the starter set.
- **November 3, 2026: pause on new content** (superseded the same day by the entry above). James agreed (a thumbs-up on the report that asked both questions) to pause new themes and grades 6–8 until about twenty sessions have been taught, and to spend the effort on room plans, home plans and his review queue. Drafts already written stay in review; nothing new is scouted or drafted until the pause lifts.
- **November 3, 2026: next room plans.** James agreed to Week 5 (Tower cities, deduction from view clues), Week 7 (take-away games) and Week 10 (bridges) as the room plans after November 4, in that order.
