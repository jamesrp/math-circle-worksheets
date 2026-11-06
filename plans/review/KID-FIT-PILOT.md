# Kid-fit pilot: ten weak-page weeks through the reviser

November 6, 2026. James asked on November 6 to try the kid-fit stage on existing weeks before any wider sweep ("Sounds good! Go ahead on this"). This is the result. Nothing here has been used with children.

**Adopted, November 6, 2026.** James approved adopting the revised weeks the same day. All ten are now the current print set: the band PDFs are the approved candidates (byte-identical), and each week's facilitator guide, key, band views, editable package, source ZIP, README and catalog record were updated to match. Each guide was renumbered and gained this summary's adoption notes: Week 24's new page says a short game shows the stronger deck winning outright only 45% of the time over 6 rounds and 52% over 10, and that the cycle shows by counting pairs; the materials gaps in Weeks 12, 16, 24 and 49 are filled; Week 25's identical boards are called extra workspace; Week 22's K–1 board 2 tells the adult to show the one-dot move. The replaced files are in each week's `archive-before-kid-fit-2026-11-06/`. Every packet and guide rebuilds from its extracted source ZIP. The PyMuPDF-based `verify_revision.py` scripts could not run in this environment (PyMuPDF not installed); exact text and 100-dpi pixel comparisons stand in for them. Some older dated check scripts (October 23 card-fix verifiers, `plans/review/checks/week-22/` and `week-34/`) describe the previous pages and will now fail by design. The six activity questions below stay open for James. The candidate copies under `plans/review/kid-fit/pilot/` are kept as the record of what was approved.

## Verdict

The reviser reliably fixes pages that a cold reader calls weak. All seven weak pages became workable, and no page got worse. But the gains are modest, a level of noise in the critics is clear, and adopting each week costs more than the pages themselves. **Don't run the remaining weak-page weeks as one sweep.** Run the stage just in time on weeks that are about to be taught or given a room plan, with a math check and a human look before adoption. See [Recommendation](#recommendation).

## Method

- **Weeks:** 12, 14, 16, 22, 24, 25, 33, 34, 36 and 49. Each one was rated in [KID-FIT-REVIEW.md](KID-FIT-REVIEW.md) as a good or workable activity with a weak page somewhere, K–1 first, spread across strands. All are problem-file weeks with all three bands. Taught or scheduled weeks (3, 5, 7, 10, 86) and weeks without pages (138) were left out.
- **Stages,** each a fresh agent that did not see the others' work except as below:
  1. A cold kid-fit critic (`worksheet-workflow/stages/critic-kids.md`) on the current print PDFs and source. It rated activity and page per band and checked the K–1 bar.
  2. The reviser, on the page only, with the critic's review. It edited `problems/`, `figures.py` and `week.toml` and rebuilt the band PDFs. No general adversarial review or math critic ran, so the reviser answered the kid-fit review alone.
  3. A second cold kid-fit critic on the revised PDFs. It did not see the first review or rating.
- **Outline:** each run's outline was built from the week's catalog record and the first two pages of its facilitator guide.
- **Checks:** every revised packet rebuilds from its source with 0 differing pixels (`compare.py`). The re-raters rendered and read every page. Nobody rehearsed the materials.

## Ratings before and after

Ratings are activity / page. A dash means no change. The K–1 bar ("children who read almost nothing manage the core move with only the parent volunteer") was not met in any week, before or after.

| Week | K–1 | Grades 2–3 | Grades 4–5 |
|---|---|---|---|
| 12 Catalan bijections | workable/weak → strong/workable | — (strong/workable) | workable/workable → strong/workable |
| 14 Polygon triangulations and flips | workable/weak → workable/workable | — (strong/workable) | strong/workable → strong/strong |
| 16 Three-color triangles | — (workable/workable) | workable/weak → workable/workable | — (strong/workable) |
| 22 Meeting regions | workable/weak → workable/workable | — (strong/workable) | — (strong/workable) |
| 24 Three random decks | workable/weak → workable/workable | — (strong/workable) | — (strong/workable) |
| 25 Row and column shadows | — (workable/workable) | — (strong/workable) | workable/workable → strong/strong |
| 33 Prime-length necklaces | — (workable/workable) | — (strong/workable) | — (strong/workable) |
| 34 Hidden turns | workable/weak → workable/workable | workable/workable → strong/workable | strong/workable → strong/strong |
| 36 Making threes | — (workable/workable) | — (strong/workable) | — (strong/workable) |
| 49 Four towers and differences | workable/weak → workable/workable | — (strong/workable) | — (strong/workable) |

- **Weak pages:** 7 before, 0 after. These were K–1 in 12, 14, 22, 24, 34 and 49, and grades 2–3 in 16.
- **Page ratings:** up in 10 of 30 band-pages and down in none. Eight of the ten weeks gained at least one page rating. Weeks 33 and 36 did not change.
- **Strong pages:** 0 before, 3 after (14, 25 and 34 grades 4–5).
- **Activity ratings** rose 5 times though the reviser was told to leave activities alone. Two of those rises are arguably real changes: Week 16's K–1 hiding game and Week 12's K–1 reorder. The other three (12 and 25 grades 4–5, 34 grades 2–3) come from a different critic reading an unchanged activity. Treat a one-level move as within the noise.

## The clearest before and after

**Week 22, K–1, Meeting regions.** Before (9 pages, page weak): five rule sentences and a four-panel key up front. Then two "find every split" problems on nine and six small boards, where every printed position was an exact on-the-line case. The first critic's minute-by-minute child "most likely never reaches the game on page 7", which was the best thing in the packet. After (6 pages, page workable): the opening key shows the one move (join two letters in blue, the other two in red, see whether they cross). The placing game moved up to Problems 2 and 3, and the degenerate cases moved to the end. The re-rater called Problems 1, 2, 3 and 5 "short and pictorial, and a child can act on them after one hearing". It still found two weak late pages (Problems 4 and 6), and it noted that the inside-the-triangle answer needs a move the K–1 key does not show.

## What the critics disagreed on

Cold critics are not stable. Three re-raters asked to undo the first critic's main fix:

- **Week 33:** move the 32-card sort back ahead of the five-bead question.
- **Week 14:** restore "lines may not cross".
- **Week 36:** use fewer record boards on the grades 2–3 splits problem, where the reviser had added six at the first critic's request.

One re-rater caught a real mistake. **Week 24's** first critic made "play the game first" its top K–1 fix. But a 6- or 10-round game cannot reveal a 5-to-4 edge. I checked: the stronger deck wins the match outright only 45% of the time over 6 rounds and 52% over 10. The cycle shows only by counting the pairs. So the revised K–1 page leads with a game that will usually not show the surprise. That needs a decision before Week 24 is adopted.

## New problems the revisions introduced

All are small, but each is a reason not to adopt without a look.

- **Week 25, grades 2–3:** the "continued" page for Problem 5 is four identical copies of a board with no instruction.
- **Week 14, K–1 Problem 5:** the boards are about 1.3 inches across, with grey lines to "erase".
- **Week 16:** the older bands' Problem 1 now uses counters, but the materials list names counters for K–1 only.
- **Week 49:** the K–1 cup and counters are not in the materials list. The grades 4–5 doubled start needs 36 of the 40 cubes.
- **Week 24, grades 2–3:** the hidden-bag letters are not in the materials list.
- **Week 12:** the 20 cm strings conflict with the "stay inside the circle" rule on the smaller circles.
- **Page counts** grew in some weeks (Week 49 went from 5/5/6 to 7/8/8) and shrank in others (Week 22 K–1 went from 9 to 6).

## Questions for James about the activities

The critics raised these. They are activity choices, so the reviser left them alone.

- **Week 12:** grades 4–5 never use the strings. Keep that, or give them a string problem?
- **Week 22:** cut or defer the K–1 dots-in-a-row problem? Would a pegboard with rubber bands help for the younger bands?
- **Week 24:** keep the K–1 two-card impossibility argument? Lead K–1 with the game or with counting pairs (see above)?
- **Week 34:** should K–1 go beyond the 3- and 4-rings, up to the eight-ring?
- **Week 49:** can K–1 run whole moves, or should they work with one step?
- **Week 36:** are K–1 children ready to track shape and fill together? A shapes-only start is a fallback.

## Cost of adopting a revised week

The reviser renumbers problems, so each adopted week also needs these:

- **Facilitator guide:** every revised week's guide refers to the old numbering. In Week 12, `check_guide_copy` fails on one rewritten key sentence, and in Week 25 on 31.
- **Other copies:** print PDFs, source ZIP, editable package and catalog record, per the version-consistency rules.
- **Week 33:** its existing `guide-keys.pdf` already failed to compile before this pilot. The band packets are fine.

None of that has been done. Adoption is James's call.

## Token cost

About 30 agents ran, at roughly 155k to 213k tokens each, which is about 5.3M tokens in all, or about 530k per week. The kid-fit review rated K–1 weak or skip in 96 of 209 weeks (drafts included), and many more weeks have a page rated below their activity in some band. At this rate a sweep of 50 weeks would cost about 26M tokens, and 100 weeks about 53M, before any guide updates. James named spending lots of tokens on low value as the near-term trapdoor.

## Recommendation

1. **No full sweep.** Ten weeks show that the stage works, and more of the same won't teach us anything new.
2. **Run it just in time.** Use the stage on weeks about to get a room plan or be taught, such as the Dec 9 pick or a home weekend. A kid's actual reaction is worth more than a second critic's.
3. **Add a math check to the reviser.** At about 50k extra tokens per week, it would have caught Week 24 before the re-rater did.
4. **Have James spot-check two weeks first:** Week 22 (clearest gain) and Week 24 (the questionable game-first fix). If those look right to him, the rest can be adopted as they come up.
5. **Fix the critic's noise before scaling.** One way is to give the critic concrete anchors for each rating level from this pilot's before and after pages. Then a re-rater's "undo this" can be told apart from a real regression.

## Files

- Candidate packets: `plans/review/kid-fit/pilot/week-NN/`. Each has `k-1.pdf`, `grades-2-3.pdf` and `grades-4-5.pdf`, the changed source files under `src/` (problems, figures and `week.toml`), `before-review-kids.md` and `after-review-kids.md`. The source folders drop into `lowell-math-circle-year-2/source/week-NN/` and build with `source/problem-files/build.py`.
- The run folders, with prompts and full agent output, are in `tmp/kidfit-pilot/` (gitignored, local to this session).
