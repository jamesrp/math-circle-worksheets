# Ten random atlas entries, made into worksheets

This trial responds to the organizer's question: can the atlas produce investigations with the depth and discovery of the revised Week 1 sheets? Three authors developed ten entries, exchanged independent mathematical/design reviews, and made student worksheets with separate solutions. The [design brief](DESIGN-BRIEF.md) records the Week 1 benchmark and prerequisite policy.

## What to print

- [Student investigations](../../../lowell-math-circle-year-2/combined/atlas-random-ten-student-worksheets.pdf).
- [Facilitator guide and checked solutions](../../../lowell-math-circle-year-2/combined/atlas-random-ten-facilitator-guide.pdf).
- [Source and rebuilding instructions](../../../lowell-math-circle-year-2/source/atlas-random-ten/README.md).

Use the linked contents or bookmarks to select one investigation. Print US Letter, single-sided, at actual size; supply scrap paper and hand out pages one at a time. Later pages can be another meeting. These are worksheet trials, not a new ten-week sequence or a record of activities already taught.

The student book has **35 investigation pages plus contents**; the facilitator book has **44 pages including contents**. Page numbers below are the printed/PDF page numbers.

| Family | Student pages | Guide pages |
|---|---|---|
| GA-26 | 2–5 | 2–6 |
| GA-29 | 6–9 | 7–10 |
| GA-11 | 10–12 | 11–15 |
| AP-26 | 13–16 | 16–21 |
| AP-23 | 17–19 | 22–24 |
| AP-21 | 20–22 | 25–27 |
| GA-25 | 23–26 | 28–31 |
| AP-07 | 27–30 | 32–38 |
| AP-01 | 31–33 | 39–41 |
| AP-29 | 34–36 | 42–44 |

## Which would I try first?

**GA-25 (roads and courtyards), AP-23 (road choices), AP-29 (prefix codes), and AP-26 (delayed control)** are the strongest first pilots, depending on prerequisites. They have concrete actions, a genuine surprise, and a reason to introduce a new representation or proof. AP-26 requires signed numbers. AP-01 is also strong once fractions and averaging are comfortable.

The calculus sheet is a substantial calculus investigation. Its important question is how to allocate updates and prove a minimum cost at a specified accuracy, rather than merely calculate a recurrence. GA-11 is the least natural fit for a broadly mixed elementary circle: its satisfying payoff really involves algebra and irrational inputs. Retaining that gate is a useful result of the experiment.

| Draw | Family | Satisfying mathematical payoff | Actual gate and assessment |
|---|---|---|---|
| 1 | GA-26 — Can colors detect a knot? | Local coloring rules obstruct untying; changing a crossing destroys the nonconstant coloring. | Three colors and careful over/under tracing. Rich but visually demanding; the all-moves and Reidemeister facts are explicitly supplied. |
| 2 | GA-29 — The disappearing strip | Addresses distinguish retained points; many pieces can have small total length. A separate infinite continuation uses diagonalization. | Fractions and powers for the finite core; infinite sequences and a supplied nested-interval fact for the last page. Good finite core, separate advanced endpoint. |
| 3 | GA-11 — The addition machine | Prove every rational output, then build machines that agree there but disagree on irrational inputs. | Signed fractions, variables, irrational numbers and uniqueness of representation. Strong for a symbolic group; a conditional circle fit. |
| 4 | AP-26 — The controller remembers | A false finish leads to a state graph, a six-step orbit, and a geometric rotation; weaker correction gives contraction. | Signed arithmetic to explore, algebra for every-start proof, fractions/algebra for the optional repair. First-pilot candidate. |
| 5 | AP-23 — Everyone chooses a road | A personal improvement hurts the group; a stable choice differs from the group optimum; ties allow cycling. | Small counts, addition, comparisons and one-player moves. First-pilot candidate with a low arithmetic gate. |
| 6 | AP-21 — Spend the battery? | Different histories share the same future problem; a short backward certificate proves an optimal plan. | Small sums and systematic take/skip reasoning. Promising for children who like planning; backward reasoning is a real gate. |
| 7 | GA-25 — Roads, loops and courtyards | Build a maze, prove the edge count, exchange roads optimally, then reinterpret removed roads as a tree connecting faces. | Tracing, drawing and connectedness; increasingly demanding explanations. Closest to the Week 1 progression through several representations. |
| 8 | AP-07 — Trust a cooling simulator? | Separate stability from accuracy, optimize unequal step sizes, and prove the fewest updates meeting an error target. | **Calculus**, exponentials and algebra; product bound supplied for the final proof. Strong advanced sheet, not an elementary substitute. |
| 9 | AP-01 — Which shore? How long? | Fair prices become a harmonic skyline; a ferry changes duration while preserving every winning chance. | Halves, quarters and first-step averaging. Strong when those ideas are accessible; brief coin play alone misses the payoff. |
| 10 | AP-29 — Shorter message names | Ambiguity motivates prefix trees; classify all four-leaf shapes and prove optimality, then change which shape wins. | Counting weighted lengths and explaining a tree. First-pilot candidate; logarithms are unnecessary for this finite theorem. |

## What changed from an atlas card

The work was not simply typesetting the card's example. The road-choice instance was sharpened so the stable outcome is strictly worse for the group. The maze grew into edge exchange and planar duality. Battery scheduling now uses a few meaningful state comparisons instead of a full table of routine calculations. The walk acquired a ferry that separates hitting probability from duration. The cooling problem now has a genuine optimization and impossibility certificate. Blank diagrams and staged questions leave the important constructions to the learner.

This sample supports the atlas as a source of substantial worksheet material, with significant design work still required between a card and a strong lesson. It does not establish that every family has an elementary version, that every sheet is equally engaging, or that the proposed pacing works in a classroom. The algebra and calculus gates are informative outcomes, not reasons to redraw the sample.

## Sampling and evidence

[sample.json](sample.json) records the original cards, all 90 population IDs, their source-file hashes, the method and seed **12921103429184828756**. It is one uniform sample without replacement, generated with Python's `random.Random(seed).sample` from sorted IDs. The seed was drawn once; there was no redraw or subject/prerequisite filter. No AD entry happened to be selected, and the draw order is preserved in both books.

The three edited data files are [geometry](geometry-data.json), [systems](systems-data.json) and [decisions](decisions-data.json). Their companion design notes explain the investigation arcs. The [review record](REVIEW.md) links independent reviews, exact checks, repairs and page inspection. Claims about classroom appeal remain editorial judgments until piloted. Record actual use in the atlas use log only after a session occurs.
