# Bellingham Math Circle

An activity library for an elementary-school math circle in Bellingham, built around enjoyment, curiosity, and mathematical discovery. We explore logic puzzles, shapes, patterns, games, and questions that invite experimentation and explanation. The purpose is to develop a taste for mathematical thinking, rather than drill school arithmetic.

## Where things live

| Folder | Contents |
|---|---|
| [external-resources/](external-resources/README.md) | Downloaded books, activity collections, and other reference material: our inputs. |
| [lowell-math-circle-year-1/](lowell-math-circle-year-1/README.md) | The organizer's 2025–26 worksheets and shape-subtraction work, preserving their original folders. |
| [lowell-math-circle-year-2/](lowell-math-circle-year-2/README.md) | Our printable worksheets, organized by week, plus combined packets and a separate editable `source/` folder. Start here to print. |
| [plans/](plans/README.md) | Session plans, teaching/source notes, mathematical checks and data, review records, and the use log. |
| `tmp/` | Build files, extracted text, render previews, and other working files. Final worksheets live in the year-2 folders. |

```text
math-circle/
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

Activities will have three rough entry levels: **K–1, 2–3, and 4–5**. These are planning guides, not age restrictions. Children should choose activities suited to their reading, arithmetic, and readiness for abstraction and proof.

Experience from the first year puts **concrete, hands-on exploration** at the center: manipulatives, time to play with them, and learning by doing before formal explanation.

The current [fall plan](/Users/jamespfeiffer/math-circle/plans/fall-k-5-year-a.md) aligns ten weekly themes across K–1, 2–3, and 4–5. Its [activity guide](/Users/jamespfeiffer/math-circle/plans/fall-k-5-year-a-activities.md) supplies concrete activities for all thirty group sessions, including exact puzzles, prerequisites, setup, hints, and checked solutions. The [session use log](/Users/jamespfeiffer/math-circle/plans/fall-k-5-year-a-use-log.md) tracks which instances children actually encounter. The [original grades 2–3 plan](/Users/jamespfeiffer/math-circle/plans/grades-2-3-year-a.md) also includes a proposed summer sequence.

[Week 1 printable worksheets](/Users/jamespfeiffer/math-circle/lowell-math-circle-year-2/source/week-01/README.md) cover all three grade bands, with a separate facilitator guide, checked solutions, editable LaTeX sources, and rebuild instructions. The revised investigations use the organizer's **21st Century Pattern Blocks** and **Upscale Pattern Blocks**: four pages of easy shape-filling mats for K–1, tiling obstructions and optimal packing for 2–3, and a complete six-tiling flip graph for 4–5. The [research and design rationale](/Users/jamespfeiffer/math-circle/plans/week-01-tiling-redesign.md) connects these questions to undergraduate discrete mathematics and research on tilings. Print at actual size; the nominal small edge is one inch, consistent with the organizer's measurement.

The [Week 1 back-pocket extensions](/Users/jamespfeiffer/math-circle/plans/week-01-extensions.md) add four optional investigations at roughly grades 6–7 reasoning depth, with separate student and facilitator PDFs. They extend matching obstructions, tiling distances, route counting, and random walks; record use only when children actually encounter them.

`AGENTS.md` gives guidance for developing this library.

The [mathematics atlas](plans/atlas/README.md) expands beyond the fall sequence: 63 field dossiers, 231 problem seeds and 90 facilitator planning cards, with explicit prerequisites from concrete play through advanced mathematics. Its research map, review records and print volumes preserve the distinction between surveyed territory, checked examples and unpiloted activities.

The [ten-entry worksheet trial](plans/atlas/worksheet-trial/README.md) develops one random atlas sample into student investigations and a separate teaching key, then assesses which come closest to the revised Week 1 standard. It retains algebra and calculus prerequisites where the satisfying mathematics needs them.

The [remaining eighty worksheet investigations](plans/atlas/worksheet-expansion/README.md) extend that work to the other atlas families, organized into three subject books with separate facilitator guides. The [page finder](plans/atlas/worksheet-expansion/INDEX.md) gives exact print ranges and prerequisite gates for all eighty, with independent mathematical and page reviews, source evidence, and editable builders.

The [September review and implementation record](/Users/jamespfeiffer/math-circle/plans/fall-weeks-01-10-review.md) tracks the follow-up revisions across Weeks 1–10: precise mathematical wording, concrete proof support, a consistent movement break, and explicit stopping points. The [shared divisibility scaffold](/Users/jamespfeiffer/math-circle/plans/coprime-divisibility-scaffold.md) supports the optional general arguments in Weeks 4 and 9.

[Weeks 2–10 print packets](/Users/jamespfeiffer/math-circle/lowell-math-circle-year-2/source/fall-weeks-02-10/README.md) extend the Week 1 design standard across the rest of fall: three student levels, one optional grades 6–7 investigation per week, and separate facilitator solutions. The revised activities explore toggle invariants, permutation orders, modular orbits, Latin-square clues, optimal code queries, subtraction games, Nim, billiards, and Euler/postman routes. The [mathematical redesign rationale](/Users/jamespfeiffer/math-circle/plans/fall-weeks-02-10-mathematical-redesign.md) links complete weekly plans, undergraduate topics, primary research references, and the changes from the earlier proposals. All are marked planned until their actual use is recorded.
