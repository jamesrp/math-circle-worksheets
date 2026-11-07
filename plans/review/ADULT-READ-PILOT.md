# Adult cold-read pilot (November 7, 2026)

James opened the K–1 packets for Weeks 24, 34 and 49 and could not tell at a glance what the activity was; Week 36 made sense to him only because he knows Set. This pilot asks whether the student pages fail an adult cold read, and what fix belongs in the worksheet workflow. It is a review of pages, not a pilot with children, and it changes no pages.

## Method

For each of Weeks 24, 34, 49 and 36, plus Week 10 (Bridges, rated strong at every age in the kid-fit sweep) as a control, a fresh subagent saw only that week's three current print band PDFs, rendered at 80 dpi and read page by page. It saw no guide, catalog, review or repository file. It was briefed as a smart parent volunteer who is not a mathematician, handed the packet ten minutes before the session; the Week 36 reader was told it had never played Set and must not use outside knowledge of it. Each reported what the activity is, what to prepare, how to launch Problem 1, what the point is, every place it got stuck (blocking, slowing or minor), and whether it could run the table from the pages alone. I then compared each account with the week's facilitator guide.

The PDFs read are `lowell-math-circle-year-2/week-NN/week-NN-{k-1,grades-2-3,grades-4-5}.pdf` on main at 9b25ad0. For Weeks 24, 34 and 49 these are byte-identical to the K–1 files James opened in `plans/review/kid-fit/pilot/week-NN/`. (Week 36's pilot-folder K–1 differs from the print set; the print set was used.) Full reader reports: [week-24](adult-read/week-24-cold-read.md), [week-34](adult-read/week-34-cold-read.md), [week-49](adult-read/week-49-cold-read.md), [week-36](adult-read/week-36-cold-read.md), [week-10](adult-read/week-10-cold-read.md).

## Results

| Week | Got the activity right? | Could run it from pages alone | Where it failed | Guide fills the gaps? |
|---|---|---|---|---|
| 24 Three random decks | Yes, but only at K–1 page 4 | Only with help | Problem 1 in every band. K–1 page 1 says "bags", "deck" and "game" before any page shows what is in a deck; the 2–3 and 4–5 First pick / Second pick table doesn't say what to record. | Yes: deck contents, 58 cards, how to make them, what to record ("A 4, C 6"), all answers. |
| 34 Hidden turns | Yes, on a second read of page 1 (medium confidence) | Only with help | The core rule. "Make every dot sit on its own color" never says the match must be other than the starting position, so on first read it can never fail. K–1 Problem 3's dot / circle / square marks aren't tied to counters. No hint that K–1 Problem 1 is meant to be impossible. | Yes: counters (8 each of 3 kinds per pair), tracing paper, launch demo, what the marks mean, that the builder cannot win Problem 1, all answers. But the guide opens with "dihedral motion" and "distinguishing coloring". |
| 49 Four towers | Yes (medium-high) | Only with help | K–1 page 1's "extra part" and "old mat / new mat" are undefined; no materials anywhere; nowhere to record move counts. | Yes: 40 cubes per pair, mats, cup and counters, launch, all answers. |
| 36 Making threes | Yes (high); no knowledge of Set needed | Only with help | Logistics, not the rule: where the nine tiles come from, how many sets, how to mark a split on the printed grids. | Mostly: print K–1 page 5 on card stock, one per child plus one, and cut. It gives no convention for marking splits on the grids. |
| 10 Bridges (control) | Yes, in about 30 seconds | Only with help | Only late problems: hexagons and craft sticks appear unannounced in K–1 Problem 7 and 2–3 Problem 8; no answers to check "how can you tell?". | Yes, and it opens in plain words ("1. The idea of the week"). |

What this shows:

- **Every reader could identify the activity, and none could run the table from the pages alone.** That second part is by design: AGENTS.md keeps materials, answers and hints off the student page and in the facilitator guide. The control fails the same way, so "can't run it from the pages" is not the signal.
- **The real signal is whether the core move is clear from page 1.** Week 10's rules paragraph got the reader there in 30 seconds. Weeks 24 and 34 fail at Problem 1 itself, Week 49's K–1 page 1 is slow, and Week 36 is clear. That matches James's reaction to the same pages.
- **The kid-fit revision made Week 24 worse for adults.** Before November 6, K–1 page 1 pictured A's and B's cards and Problem 1 was "Circle the winner in each pair." The reviser put a six-round game first, as the kid-fit review asked, so the game now comes before any page shows what is in a deck. Week 34's confusing rule was already on the page before the revision (v3 page 1 is nearly the same). So the kid-fit stage can introduce adult confusion, and no stage catches it.
- **The guides exist and are good, but they are hard to find and hard to start.** Each week's guide is a separate PDF next to the band packets; the pilot folders James opened hold only band PDFs. The guides for 24, 34, 36 and 49 open with the theorem-first overview AGENTS.md asks for, written for a mathematician ("affine plane F₃²", "dihedral motion"). The practical page (materials, launch, timing) is page 2. Week 10's guide opens with a plain "idea of the week" and a materials table, which is what a parent volunteer needs first.

## Week 24, Problem 1 and the decks

From the [Week 24 guide](https://github.com/jamesrp/math-circle-worksheets/blob/main/lowell-math-circle-year-2/week-24/week-24-facilitator.pdf), pages 1–3:

- **The decks.** Three paper lunch bags labelled A, B, C, each holding three cards: A = 2, 4, 9; B = 1, 6, 8; C = 3, 5, 7. Cards are half index cards with the numeral large and, for K–1, its dots in a ten-frame. One set of three bags per table; about 30 minutes once to make the 58 cards the whole week uses (originals, spares and a few extra values for later problems).
- **The math.** Each deck beats the next in 5 of the 9 possible card pairs: A beats B, B beats C, C beats A. No deck is best (nontransitive dice, with cards).
- **K–1 Problem 1** is a short game that raises the question. Two children each take a deck; each draws one card from their bag, the bigger number wins, a counter goes in the winner's row, both cards go back. Six rounds each of A against B, B against C, C against A. The guide says plainly that a six-round game shows the favoured deck winning only about 45% of the time, so the game can't settle it; Problems 2–4 settle it by counting all nine card pairs.
- **Grades 2–3 and 4–5 Problem 1** is "pick first or pick second": the second picker can always take the deck that beats the first pick. Each row of the table records one game, as a deck letter and rounds won, such as "A 4, C 6".

## Where the guides are

Each week's guide sits beside its band packets:

- [Week 24 guide](https://github.com/jamesrp/math-circle-worksheets/blob/main/lowell-math-circle-year-2/week-24/week-24-facilitator.pdf)
- [Week 34 guide](https://github.com/jamesrp/math-circle-worksheets/blob/main/lowell-math-circle-year-2/week-34/week-34-facilitator.pdf)
- [Week 36 guide](https://github.com/jamesrp/math-circle-worksheets/blob/main/lowell-math-circle-year-2/week-36/week-36-facilitator.pdf)
- [Week 49 guide](https://github.com/jamesrp/math-circle-worksheets/blob/main/lowell-math-circle-year-2/week-49/week-49-facilitator.pdf)
- [Week 10 guide](https://github.com/jamesrp/math-circle-worksheets/blob/main/lowell-math-circle-year-2/week-10/week-10-facilitator.pdf)

The [explorer page](../../explorer/index.html) links each week's guide too.

## Proposed fix

1. **An adult cold-read stage in the workflow.** A fresh agent reads the band PDFs as a parent volunteer, with nothing else, and lists located fixes to the student pages: define a term where it is first used, show what is in a deck or set before the first problem that uses it, say what goes in a record table, state the goal so it can fail. It runs on the draft alongside the other critics, and the reviser addresses it. Since the Week 24 case shows a reviser can add confusion, the same read should also run once on `final/` before the packet goes to James. Draft prompt: [adult-read/critic-adult.draft.md](adult-read/critic-adult.draft.md). It is not wired into `worksheet-workflow/` or `make_prompts.py`.
2. **A one-page adult table card per week, not a box on the student page.** All five readers asked for the same half page: what the activity is in two sentences, materials with counts and how to make them, the one-minute launch, the surprise, and the key answers. A box on page 1 would break the student-page format in AGENTS.md (header, shared rules and numbered problems only), so make it a separate sheet that goes on top of each table's packet. It would be page 1 of the guide, in plain words, with the theorem-first overview after it. Week 10's "idea of the week" and materials table is the model. This is a format change, so it waits for the organizer.
3. **Fix the two weeks that fail at Problem 1** (24, 34) when they next come up, just in time, using their cold-read reports. Not done here.

## Cost

| Week | Pages read | Reader tokens (final context) | Tokens processed, incl. cache reads | Output tokens | Minutes |
|---|---|---|---|---|---|
| 10 | 37 | 163k | 1.53M | 10.6k | 1.8 |
| 24 | 25 | 148k | 1.17M | 7.8k | 1.3 |
| 34 | 17 | 142k | 1.03M | 7.5k | 1.3 |
| 36 | 15 | 139k | 1.02M | 5.8k | 1.1 |
| 49 | 23 | 147k | 1.04M | 8.4k | 1.4 |

About 150k reader tokens per week, roughly a quarter of the ~530k per week of the full kid-fit sweep, and most of it is fixed overhead plus page images. A pass over all 100 print weeks would be about 15M reader tokens (on the order of 110–120M processed, mostly cached reads). Reading only K–1 plus page 1 of the other bands, which is where the launch failures were, would cut that by roughly a third to a half. Not run: like the kid-fit sweep, the cheaper path is to run it just in time on a week before it is printed, and in the workflow for new packets.
