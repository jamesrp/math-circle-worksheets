# Bellingham Math Circle

Canonical source: [jamesrp/math-circle-worksheets](https://github.com/jamesrp/math-circle-worksheets), branch `main`. The original local `math-circle/` working folder is deprecated and retained as a reference/private archive. Start new work from a fetched clone of this repository. The separate `jamesrp/math-circle` repository is the older Koch viewer.

Downloaded books/reference collections and private classroom records are optional local inputs, preserved outside the published history. See [LOCAL-RESOURCES.md](LOCAL-RESOURCES.md) for availability and the resource manifest. Links to those local inputs require authorized access; a GitHub clone does not include them. Small borrowed writing examples remain in the source as described in [REPUBLISHING.md](REPUBLISHING.md). These AI-assisted activity drafts have digital checks and review records; check each release's stated limits before classroom use.

An activity library for an elementary-school math circle in Bellingham, built around enjoyment, curiosity, and mathematical discovery. We explore logic puzzles, shapes, patterns, games, and questions that invite experimentation and explanation. The purpose is to develop a taste for mathematical thinking, rather than drill school arithmetic.

## Where things live

| Folder | Contents |
|---|---|
| [external-resources/](external-resources/README.md) | Downloaded books, activity collections, and other reference material: our inputs. |
| [lowell-math-circle-year-1/](lowell-math-circle-year-1/README.md) | The organizer's 2025–26 worksheets and shape-subtraction work, preserving their original folders. |
| [lowell-math-circle-year-2/](lowell-math-circle-year-2/README.md) | Our printable worksheets, organized by week, plus combined packets and a separate editable `source/` folder. Start here to print. |
| [plans/](plans/README.md) | Session plans, teaching/source notes, mathematical checks and data, review records, and the use log. |
| [worksheet-workflow/](worksheet-workflow/README.md) | The tested agent workflow for drafting a week's student worksheets: prompt files, outline template, and the prompt builder. |
| `tmp/` | Build files, extracted text, render previews, and other working files. Final worksheets live in the year-2 folders. |

```text
math-circle-worksheets/
├── README.md
├── AGENTS.md
├── external-resources/
├── lowell-math-circle-year-1/
│   ├── lowell-math-circle/
│   └── subtract-shapes/
├── lowell-math-circle-year-2/
│   ├── week-01/ … week-10/    # printable PDFs
│   ├── combined/             # Weeks 2–10 print sets
│   └── source/               # LaTeX, build scripts, notes, and checks
├── plans/
└── tmp/
```

The packets brought to the September meeting are preserved in `lowell-math-circle-year-2/week-01/archive-classroom-2026-09/`. The [classroom review and adopted worksheet guidance](plans/week-01-classroom-review.md) records the resulting revision; the organizer-approved guidance is now in AGENTS.md. The four earliest superseded Week 1 PDFs are kept in `lowell-math-circle-year-2/week-01/archive-v1/`. [Build instructions](lowell-math-circle-year-2/source/README.md) explain how to regenerate current or archived packets without mixing them.

## Background and current plans

The organizer is a parent and math PhD working in industry, inspired by years of judging the UW Math Olympiad and friends' Seattle math circles based on Zvonkin's *Math from Three to Seven*. After running a weekly, hour-long circle for grades 2–3 throughout the 2025–26 school year, the next step is to serve K–5 with a schedule that is sustainable alongside work: roughly ten fall sessions, with a possible ten-session summer circle on Saturdays at WWU to reach more Bellingham families.

The long-term goal is enough varied material for a child to attend twenty weeks a year from kindergarten through fifth grade: about 120 sessions along their path. Themes such as triangular numbers can recur with new questions and greater depth; returning children should not encounter the exact same problems.

Most weeks currently have three rough entry levels: **K–1, 2–3, and 4–5**. These are planning guides, not age restrictions. Week 2 now uses one shared collection, with choices based on interest and prerequisites. Children should choose activities suited to their reading, arithmetic, and readiness for abstraction and proof.

Experience from the first year puts **concrete, hands-on exploration** at the center: manipulatives, time to play with them, and learning by doing before formal explanation.

**Current group, reported September 28, 2026:** ten children, **KK1 / 3333 / 445**, and three adults: the organizer, another mathematician, and one non-mathematician parent. The working arrangement is one adult anchored to each group: the parent with KK1, the other mathematician with the four third graders, and the organizer with the two fourth graders and fifth grader. These are current planning facts, not a reconstruction of attendance at the earlier meeting.

The current [fall plan](plans/fall-k-5-year-a.md) aligns ten weekly themes across K–1, 2–3, and 4–5. Its [activity guide](plans/fall-k-5-year-a-activities.md) supplies concrete activities, including exact puzzles, prerequisites, setup, hints, and checked solutions. Week 2 replaces its three starting packets with a shared collection; the other weeks retain their existing formats. The [private session use log](LOCAL-RESOURCES.md#private-records) tracks which instances children actually encounter. The [original grades 2–3 plan](plans/grades-2-3-year-a.md) also includes a proposed summer sequence.

[Week 1 printable worksheets](lowell-math-circle-year-2/source/week-01/README.md) cover all three grade bands, with a separate facilitator guide, checked solutions, editable LaTeX sources, and rebuild instructions. The revised investigations use the organizer's **21st Century Pattern Blocks** and **Upscale Pattern Blocks**: four pages of easy shape-filling mats for K–1, tiling obstructions and optimal packing for 2–3, and a complete six-tiling flip graph for 4–5. The [research and design rationale](plans/week-01-tiling-redesign.md) connects these questions to undergraduate discrete mathematics and research on tilings. Print at actual size; the nominal small edge is one inch, consistent with the organizer's measurement.

The [Week 1 back-pocket extensions](plans/week-01-extensions.md) add four optional investigations at roughly grades 6–7 reasoning depth, with separate student and facilitator PDFs. They extend matching obstructions, tiling distances, route counting, and random walks; record use only when children actually encounter them.

`AGENTS.md` gives guidance for developing this library.

The [mathematics atlas](plans/atlas/README.md) expands beyond the fall sequence: 63 field dossiers, 231 problem seeds and 90 facilitator planning cards, with explicit prerequisites from concrete play through advanced mathematics. Its research map, review records and print volumes preserve the distinction between surveyed territory, checked examples and unpiloted activities.

The [ten-entry worksheet trial](plans/atlas/worksheet-trial/README.md) develops one random atlas sample into student investigations and a separate teaching key, then assesses which come closest to the revised Week 1 standard. It retains algebra and calculus prerequisites where the satisfying mathematics needs them.

The [remaining eighty worksheet investigations](plans/atlas/worksheet-expansion/README.md) extend that work to the other atlas families, organized into three subject books with separate facilitator guides. The [page finder](plans/atlas/worksheet-expansion/INDEX.md) gives exact print ranges and prerequisite gates for all eighty, with independent mathematical and page reviews, source evidence, and editable builders.

The [September review and implementation record](plans/fall-weeks-01-10-review.md) tracks the follow-up revisions across Weeks 1–10: precise mathematical wording, concrete proof support, a consistent movement break, and explicit stopping points. The [shared divisibility scaffold](plans/coprime-divisibility-scaffold.md) supports the optional general arguments in Weeks 4 and 9.

[Weeks 2–10 print packets](lowell-math-circle-year-2/source/fall-weeks-02-10/README.md) extend the Week 1 design standard across the rest of fall: a shared Week 2 collection, three student levels and optional grades 6–7 investigations for Weeks 3–10, and separate facilitator solutions. The revised activities explore toggle invariants, permutation orders, modular orbits, Latin-square clues, optimal code queries, subtraction games, Nim, billiards, and Euler/postman routes. The [mathematical redesign rationale](plans/fall-weeks-02-10-mathematical-redesign.md) links complete weekly plans, undergraduate topics, primary research references, and the changes from the earlier proposals. All are marked planned until their actual use is recorded.

The [September 27 transfer of classroom guidance](plans/fall-weeks-02-10-classroom-guidance-review.md) revises all of Weeks 2–10: more contrasting concrete attempts, clearer numbered tasks, representations introduced after they have a purpose, common demonstrations, and facilitator proof follow-ups. These v3 revisions are unpiloted. Previous packets are archived separately. Week 2 has since moved to the shared print links below; combined filenames remain the same.

The [Week 2 shared collection](plans/week-02-shared-collection.md) is now the current format: [42 student pages with 50 problems](lowell-math-circle-year-2/week-02/week-02-shared.pdf) and one [adult guide](lowell-math-circle-year-2/week-02/week-02-shared-facilitator.pdf). Start together, then choose making and walking puzzles, state collection, shorter solutions, room drawings, or networks by interest and readiness. Keep three stable adult-led tables and offer only a few pages at a time; page completion does not determine access to a new route. Paper and pencil/eraser or whiteboard tablets suffice, with existing counters optional. This September 28 revision is prepared, not classroom-tested. The [K–1 auxiliary design record](plans/week-02-k1-aux.md) and [visual revision record](plans/week-02-visual-review.md) preserve the earlier stages. All four combined student sets contain the same Week 2 collection, so print those pages only once.

The [September 30 Week 3 revision](lowell-math-circle-year-2/source/week-03/README.md) applies the current Week 2 catalogs’ concise, substantial-problem format: 17 investigations across four entry packets, with methods, hints, and complete proofs in a six-page adult guide. The ten-child preparation plan and combined Week 3 pages are updated; v4 remains unpiloted.

The [October 3 concrete revision record](LOCAL-RESOURCES.md#private-records) responds to the organizer's report on Weeks 1 and 2: pattern blocks went well, while the paper lamp puzzles failed because their rule lived only in the children's heads. Weeks 3–10 were rewritten so that materials or a partner enforce the rules (arrow mats, skip-stars and cipher wheels, snap-cube towers, counter codes behind a folder, take-away and Nim games, floor and grid billiards, and bridges whose counters are picked up when crossed), for fixed KK11 / 3333 / 445 tables with partner play. A [Week 1 encore](lowell-math-circle-year-2/source/week-01-encore/README.md) adds a second pattern-block session. Each week has three student packets and an adult guide; the previous versions are in `archive/` folders. All are unpiloted.
