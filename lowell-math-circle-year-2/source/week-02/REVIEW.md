# Week 2 shared collection: review record

Prepared September 28, 2026, after the organizer approved a shared collection. **Unpiloted.** This record describes author and independent review, not observed classroom success. Previous review records and all seven preceding PDFs are preserved in `archive-before-shared-collection-2026-09-28/`.

## Scope and classroom decisions

The new student PDF is **42 US Letter pages, 50 problems, F02-S-v1**. The unified adult guide is **16 pages, F02-S-FAC-v1**. Everyone shares an initial pair-move demonstration. Five groups of pages provide exploration, state collection, shorter solutions, drawing, and networks; they are choices, not a linear completion requirement. No grade labels remain on student pages.

The ten-child roster KK1 / 3333 / 445 and three adults remain the basis for staffing. Stable tables keep adult coverage manageable, while adults offer pages by the next useful action and readiness. The parent receives scripts, simple successful examples, stopping points, and drawing alternatives. Paper/pencils/erasers or whiteboard tablets suffice; existing counters remain an option. No construction accessories were added. Guide page 1 supplies the print recipe and hour; page 2 supplies the complete page finder.

The preceding concrete activities and mathematics are retained. Four-lamp boards now share one diamond orientation. The earlier advanced network packet is expanded from three dense pages to eight pictured investigations with local working mats. The two longer ring investigations retain numbered continuations. A tie between unrestricted move lists is explicitly allowed in Problem 24, while the non-tie claim for the five-ring is restricted to complementary reduced solutions.

## Mathematical checks

- `verify.py`: exhaustive edge subsets on cycles 4–7 confirm all and only even targets, two complementary reduced solutions per reachable target, and worst minimum floor(n/2). Disconnected component examples and all 32 even targets on the printed tree pass, along with the bridge, path, and forced-choice examples.
- `plans/verify-week-02-shared.py`: runs the independent graph/room model against the shared JSON data. Five graph classifications, nineteen concrete target checks, and ten exact-rational room constructions pass. An independent state-space BFS checks reachability and minimum moves; one-light walks retain the one-light condition at every step. Planar face traversal, area/Euler checks and symbol enumeration check rooms, including corner-only non-adjacency and the T-map requiring three symbols.
- A separate reviewer checked every adult-guide solution, printed target, page mapping, complement/closure case, cut count, and room argument. The component table includes its added all-OFF and BC examples. Problem 42 stops after three walls even when used with a larger group.

The guide distinguishes a failed attempt from a proof, and setting a starting picture by hand from reaching it through legal moves. Proofs use endpoint counts, path cancellation, components, cycle complements, forced decisions and tree cuts; formal notation and independent writing are not prerequisites.

## Layout and integration checks

All 42 student pages were rendered and visually inspected across their component PDFs. The final changed Problem 24 page was re-rendered at higher resolution. All 16 guide pages were rendered and reviewed; an independent source review additionally checked their mathematics and classroom directions. Working boards are blank so dots can be erased; only target miniatures contain permanent ON states. Page 15 distinguishes a saved all-OFF state from an unused record. Selected-road diagrams remain visually distinct from lamp-state diagrams.

`assemble-shared.py` checks US Letter geometry, text bounds, header/footer IDs, no obsolete grade/name/date labels, exact page-to-problem mappings, all 50 problem numbers, and the 42-page total. The guide receives the same geometry/text checks. The TeX components compile to 8, 12 and 8 pages without overfull boxes; the ReportLab exploration/drawing component contributes 14 pages. Five PDF bookmarks match the adult page finder.

The five combined Weeks 2–10 files use the shared student PDF for every Week 2 student section and the shared guide for the Week 2 facilitator section. Their covers explain this and discourage duplicate Week 2 printing. Grade distinctions remain for Weeks 3–10. Assembly regenerates contents ranges and bookmarks and checks every page. Current filenames and links point to the shared outputs; earlier separate packets are kept only in the archive.

Editable sources and mathematical data remain separate from output and render intermediates. Renders and check reports are under `tmp/pdfs/week-02-shared/` and the guide render folder; canonical mathematical results are in `plans/week-02-shared-checks.json`.

## What remains to learn in the room

Record exact pages and targets used, unprompted legal moves, successful replay of records, room counting, explanations, frustration or repeated adult rescue, and what children wanted next. Record page choices across tables and whether the parent could use the guide without leaving their table. Separate observations from hypotheses. Unused pages remain reserves for future variations; a mathematically checked and printed activity is not yet classroom-tested.
