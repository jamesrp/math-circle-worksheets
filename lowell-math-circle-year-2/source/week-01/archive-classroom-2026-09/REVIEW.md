# Week 1 revision review

## September 23, 2026: K–1 shape-filling replacement

Replaced the two-page shop/flip packet with **four pages, ten full-size mats, eight distinct outlines**, F01-K-v3. Tasks stay at easy filling, a second filling, or a single allowed block type. The existing grades 2–3 packet is the route to harder work. Updated the core facilitator guide (still five pages), preparation counts, current plans, print notes, and use log.

`plans/week-01-k1-shape-checks.py` verified exact triangular-cell areas, lattice-aligned boundaries, full-edge connectivity, and complete nonoverlapping tiling witnesses. Arrow = two chevrons; star = three chevrons; long hexagon = five blues; mountain = nine greens. Both paired shapes admit distinct fillings by changing piece types. Generated student outlines and adult solution pictures share the checked geometry.

Recompiled only K–1 and the core facilitator PDF. All nine pages were rendered and visually inspected; no clipping or overlap. Final builds have no LaTeX warnings or overfull/underfull boxes. PDF checks confirm four/five US Letter pages, readable text inside safe margins, and physical dimensions for all ten student outlines at a one-inch small edge. Student text contains no shop, trade, or flip instructions. Other grade-band and extension PDFs were not rebuilt.


## September 22 student-sheet revisions

At the organizer's request, the grades 2–3 sheet no longer gives the up/down coloring hint, the repeated-attempts question, the repeated green-filler task, or the takeaway about allowed pieces. The similar purple-to-blue replacement hint and the suggestion to use rows also stay with the facilitator. Open explanation prompts remain, with more drawing space. The side-four extension now asks about gaps, and the final optional comparison defines green fillers where they are needed.

Grades 4–5 now has a nine-board drawing page between the full-size opening mat and the supplied six-card list. It asks children to record distinct tilings without revealing the number. The original upper pages are unchanged apart from pagination. The facilitator guide reserves hints for stalled discussion and updates the page handoff instructions; the print count is now 19 student sheets for the current roster.

Recompiled only the two edited student packets and the core facilitator guide: **3 / 4 / 5 pages**, all US Letter. All 12 pages were rendered and visually inspected. The builds have no LaTeX warnings or overfull/underfull boxes; text is nonempty, has no replacement glyphs, and stays inside safe page margins. Extracted text confirms the requested removals and preservation of the three original upper pages except page numbers. Geometry and mathematical instances are unchanged. K–1, paper rhombi, and optional extension PDFs were not rebuilt or edited.

## September 20 implementation of the sequence review

The facilitator now calls the six-card list supplied until the ribbon completeness argument is established; the upper student page also makes that distinction. Each group has a satisfying stop and an optional explanation/proof continuation. The hour explicitly includes movement/reset and tidy time. The probability heading is now “Two random-flip rules.” Related changes in the extension guide identify Lowell Handout 5, problems 5.5–5.6, and let returners reuse the counting before moving to distances or routes.

All five core PDFs and both extension PDFs were rebuilt. The coordinator rendered and inspected every page of the three edited PDFs (13 pages total: upper 3, core facilitator 5, extension facilitator 5). Pagination remains unchanged, with no clipping or overlap. All seven Week 1 PDFs pass the assembler's US Letter, nonempty-text, replacement-glyph, and safe-character-bounds checks. Core and extension build logs contain no LaTeX warnings or overfull/underfull boxes. Mathematical instances and diagrams were unchanged; the earlier mathematical verification below remains historical, not a claim of a fresh independent enumeration for this wording revision.

The original September 19 review follows.

Reviewed September 19, 2026. A fresh subagent with no inherited conversation history read the project guidance, revised plans, research notes, and LaTeX, and visually inspected all **14 PDF pages**. It found no mathematical blocker. The earlier eleven-page review is preserved with the first draft in `archive-v1/`.

## Feedback incorporated

1. **Reuse the K–1 materials:** the first version implied simultaneous hexagon fillings despite allocating only three blues. The student page now asks an adult to trace the first joins, then explicitly reuses those pieces in the second outline.
2. **Correct the research citation:** Wilson's local-chain definition and symmetry argument are in §5.2, especially PDF p. 13; local-chain mixing is in §5.6. The notes no longer attribute these to §5.3, which concerns a different chain.
3. **Strengthen the purple investigation:** middle page 3 now asks whether purple can improve T3's gap bound, where replacement by two blues is a useful argument. Pink then changes the answer on T2. The facilitator guide and activity plan give the two distinct optima on T3: three green fillers, or five total blocks when purple is allowed.
4. **Align the launch:** both the activity guide and facilitator packet now begin the shared constrained work by trading a purple piece.

The fresh reviewer separately checked the added five-block construction and its lower bound. The final facilitator diagrams illustrate both six-block and five-block fillings.

## Independent mathematical checks

- The chevron decomposes into two blues/four greens; the pink pair fills T2 with the manufacturer's stated geometry.
- T2 has the up/down obstruction; T3 needs at least three gaps; the side-n construction attains exactly n green fillers. Replacing purple by two blues preserves the obstruction and gap count.
- A separate perfect-matching enumeration found exactly six H122 tilings. Direct three-rhombus hexagon-flip checks found exactly AB, BC, BD, CE, DE, EF.
- The ribbon classification is exhaustive, and its inversion statistic gives the four-flip lower bound. The graph gives matching routes and rules out all odd-length returns.
- Independent enumeration of monotone 2×2 arrays with entries 0–2 confirmed twenty tilings of the side-two regular hexagon.
- Exact rational first-step equations confirmed mean positive return times 12,4,6,6,4,12 under uniform legal flips, and six under uniform choice of four centers with failed attempts counted as stays.
- The cited Saldanha–Tomei theorem numbers, simply connected hypotheses, and height-distance normalization were checked against the author manuscript.

The repository's separate verification script also passes: six states, six edges, diameter four, twenty larger-hexagon tilings. Its geometry drives the TikZ diagrams; the facilitator packet includes mathematical explanations independent of computation.

## Final PDF checks

All five sources were rebuilt with pdfLaTeX after the changes. The builds have no LaTeX warnings or overfull/underfull boxes. Final page counts are **2 / 3 / 3 / 5 / 1**, all US Letter (612×792 PDF points). All fourteen pages were rendered and visually inspected; updated pages were inspected again after the final edits. Text and diagrams are legible, with no clipping or overlap, and extracted text stays inside safe page margins.

Emitted PDF paths confirm 72-point one-inch calibration and unit edges. The designer's one-inch description and organizer's approximate measurement support that nominal scale; they do not resolve 25 mm versus 25.4 mm for an individual batch. Print at Actual Size and compare a physical small block with the calibration line. The 2× and 3× green triangles are also physical templates for the middle boards.

These are prepared activities, not a record of teaching. Core tasks use 1× pieces; scaling, Hall's obstruction, and probability remain optional reserves.
