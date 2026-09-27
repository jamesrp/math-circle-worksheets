# Mathematics atlas - first edition

This is a research-to-investigation library for expanding the circle across mathematics and prerequisite levels. It starts with substantive adult questions, then finds worthwhile student investigations that preserve a specified piece of the mathematics. It stops where removing a prerequisite would remove the idea.

**The first edition contains 63 field dossiers, 231 surveyed problem seeds, and 90 complete facilitator planning cards.** All 60 substantive top-level MSC fields have at least one primary family; general mathematics, history and education have supporting dossiers. This is breadth across a map, not an exhaustive inventory of interesting mathematics. Seeds and families are not counts of distinct mechanisms, elementary sessions, or classroom-tested activities.

## Start with an investigation

- [Browse all 90 cards](INDEX.md), with mathematical fields and entry prerequisites.
- [How to use the atlas](HOW-TO-USE.md): concrete starting suggestions and facilitation.
- [Prerequisite key and design contract](DESIGN.md): joining, exploring, explaining and proving are separate gates.
- [Prior-use map](prior-use-map.md) and [connections](connections.md): avoid accidental repeats; label intentional revisits.
- [Actual-use log](use-log.csv): empty until a family is actually used.

Each card includes the adult question, exact mathematical anchor, source locator, fidelity limits, prerequisites, materials, preparation, an hour-long menu, launch, learner choices, prompts, hints, a worked example and boundary, extensions, and a satisfying early stop. Cards with substantial algebra, calculus or other advanced gates retain them. The small preparation estimates and session timings are proposals, not pilot results.

## Explore the research map

- [Algebra and discrete mathematics](surveys/algebra-discrete.md): 16 fields and 60 seeds.
- [Geometry and analysis](surveys/geometry-analysis.md): 27 fields and 104 seeds.
- [Probability and applications](surveys/applied-probability.md): 20 fields and 67 seeds.
- [Locked map v1](MAP-LOCK.md), [coverage table](field-coverage.csv), and [future search frontier](FRONTIER.md).
- [All 231 seeds](problem-seeds.csv), [family search table](family-index.csv), and [source register](source-map.csv).

The [pinned MSC source](../../external-resources/math-atlas/README.md) supplies 63 fields, 534 subareas, 5,503 ordinary subject entries and 503 cross-cutting facets. The [full taxonomy](taxonomy.json) preserves all 6,603 nodes. Lower-level entries remain explicitly unvisited: having a top-level family does not certify its descendants. MSC classification-derived tables carry the attribution and license recorded with the source; cited mathematical works retain their own rights.

## Print and review

The two print volumes contain the facilitator plans and the research map, respectively. These are planning books, not detailed student worksheets. Use their contents and bookmarks to select pages rather than printing the entire library.

- [Investigation plans](../../lowell-math-circle-year-2/combined/math-atlas-investigation-plans.pdf).
- [Research map](../../lowell-math-circle-year-2/combined/math-atlas-research-map.pdf).
- [Build and rendering instructions](../../lowell-math-circle-year-2/source/atlas/README.md).
- [Review record](REVIEW.md), including mathematical checks, repairs, PDF review, and limitations.

The separate [ten-entry worksheet trial](worksheet-trial/README.md) tests a single random sample of these cards against the revised Week 1 standard. It provides actual student worksheets, a separate solution guide, prerequisite gates and a candid assessment of which investigations are the strongest first pilots.

The [remaining eighty worksheet investigations](worksheet-expansion/README.md) continue the approved trial across every other family ID. Their student books and separate facilitator guides develop new instances and investigation arcs from the planning cards, with explicit prerequisite gates, full solutions, source evidence and independent reviews. The [worksheet page finder](worksheet-expansion/INDEX.md) gives exact print ranges and teaching assessments. Together the two worksheet projects cover the ninety atlas IDs; they do not exhaust the mathematical frontier.

The underlying [AD](families/algebra-discrete.json), [GA](families/geometry-analysis.json) and [AP](families/applied-probability.json) JSON files are the editable authority for cards; adjacent Markdown views and indices are generated. Run `python3 plans/atlas/build_index.py` after editing. Survey Markdown is edited directly; regenerate its seed queue with `python3 plans/atlas/build_seed_queue.py`. Run `python3 plans/atlas/release_check.py` after the indices and print outputs are current.

Next work should deepen specific unvisited subareas, develop additional genuinely different problems, and pilot the selected worksheets before expanding routine production. A six-year progression still needs scheduling and actual-use evidence; 90 families spanning elementary through advanced mathematics do not establish a 120-session elementary pathway.
