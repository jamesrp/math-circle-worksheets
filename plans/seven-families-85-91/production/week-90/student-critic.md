# Week 90 adversarial student-packet review

Reviewed 2026-10-17 by a fresh critic, independently of the writer. Scope: `draft/students.pdf` (7 pages, Problems 1–8), `draft/materials.pdf` (11 pages), generated TeX and builder, actual reserved Week 90 plan, current AGENTS guidance and generated outline. This is a review only; no draft source or PDF was edited. The separate mathematical-review stage should independently verify the full catalogs and guide claims.

## Verdict

Revise before release. The operation itself is well taught and the packet has substantial mathematics. Preserve the diagram conventions and most of the design. The most material loss is the planned constructive preimage investigation: the draft replaces it with a large catalog of repeated forward trials. Two short wording repairs are also needed to ensure that the central comparison concerns labels and to avoid a misleading five-label/three-label target reference.

## Required revisions

1. **Restore a constructive target-shape task without removing the rich catalog option (student page 4, Problem 4).** The actual reserved plan asks children to arrange 1–5 in an increasing skew board so that sliding reaches each of the three target shapes `(3,2)`, `(3,1,1)`, `(2,2,1)`. The draft supplies all sixteen starts and asks for both orders on every one. This gives useful pooled finite verification, but removes the child's design/search problem and makes the central five-label route 32 deterministic forward runs. Sorting supplied cards and proving their completeness do not replace designing a preimage. Retain the B catalog as a later pooled investigation, and restore a distinct numbered constructive task with a blank B start and the three actual target silhouettes. Give the guide a first route that does not require completing the catalog before children can construct or invert. This is preserving an authorized rich direction, not compressing the packet into one hour.

2. **Make the label comparison explicit at first whole-order comparison (page 3, Problem 3; page 4, Problem 4).** The launch asks about shapes, P1 asks which outlines agree, and P2 explicitly sorts outlines. P3 then asks whether the finished “arrangement” changes, and P4 whether there are “two different answers” before returning to outline sorting. A child can reasonably continue checking only silhouettes. The mathematical destination is equality of the full labeled array. A short phrase such as “the outline or any number's position” is sufficient; it asks the question without printing the result. In the catalog task, distinguish comparing the two runs of a single start from grouping different starts by outline.

3. **Repair the B-target reference (page 5, final sentence).** Immediately above are four explicit targets containing three numbers. “Can two different B starts reach exactly the same target? Use the B catalog to decide” can mean one of those displayed targets. B starts contain five numbers, so that reading makes the answer trivially no for the wrong reason. Ask whether two B starts can have exactly the same finished *five-number arrangement*, or give a separately identified five-label comparison. The question is worthwhile: in these B cases distinct starts have distinct labeled outputs, contrasting with D's collisions. Do not lose that contrast, and do not imply that differing labels on one outline count as the same answer.

## Operational improvements and guide requirements

- **Allow pooled D coverage (page 3).** “Finish each of the six D starts twice” currently assigns twelve full rectifications to every pair. The reserved plan explicitly allows division of the six cards. Retain the complete finite question while making sharing cases available, as P4 already does. The guide should allow one unchanged D start with two orders as an initial multi-hole route; the full six-case catalog is a continuation. These are unpiloted age-fit hypotheses, not claims that the activity cannot work.
- **Save the first labeled output before resetting.** There is no requirement for a move tally, which is good. The guide should identify one concrete record (a single final-board sketch on a blank grouping card or adult whiteboard) before rebuilding the unchanged start card. P3's single ruled line is not a visual comparison board. The separate blank grouping cards can serve this purpose; no extra simultaneous tally is needed. Show the volunteer how the record is used, and keep this scaffolding with adults rather than filling student pages with procedural directions.
- **P5's dashed zones are too small to function as card mats.** A supplied start card is 80 × 66 mm; each outlined target zone on page 5 is 77 × 75 mm and contains its diagram. Two targets have two D preimages each. Even one card is wider than its zone. “Beside” can mean the table, so this is not a mathematical blocker, but the dashed boxes visually suggest containment. Remove them, explicitly treat this as tabletop sorting in the guide, or provide separate target/group cards of a usable size. Do not shrink the catalog cards to solve this at the cost of legibility.
- **Record preparation by first route.** Materials contain four board inserts, a piece sheet, five catalog sheets, and a grouping-card sheet. A first one-hole visit needs only the A board, square demonstration board, piece kit and A cards; the larger catalogs should not make every first visit an eleven-sheet preparation exercise. Three gray pieces suffice for all supplied inner masks despite the old plan's five-gray-piece inventory. Eight loose dark pieces provide ample spares. State this deliberate simplification in the guide, and state that cutting/handling remains untested.
- **Retain the stronger late routes.** Reverse single slides (P6), failure of the larger forward rule (P7), and local proof questions (P8) are substantive and belong in the finished collection. P8's three claims are closely related invariants, not unrelated filler. Guide pacing should make proof readiness-dependent while preserving it. General confluence needs its actual assumptions and attribution in the guide; small catalogs establish their finite cases, not the global theorem.

## What works and should remain

- Page 1 gives the concrete purpose first, followed by a complete same-input slide: hole/2 over 1/3, then 1 moves up, then 3 moves left and the exit is covered. This teaches the unfamiliar operation without solving any A task.
- Gray diagonal hatching, dark crosshatching and an open ring distinguish missing inner squares, outside cells and the sole active hole in grayscale. The materials match the student convention.
- Page 3's four-frame bridge keeps the two unchosen gray squares unchanged, shows the whole lower-corner slide and actual exit covering, then opens the next legal corner. The rule says exactly when a gray square is eligible and requires finishing one slide before opening another.
- Page 6 reuses one unchanged non-task example and explicitly shows the marked original corner S and exit E, reopening E, a meaningful reverse intermediate, and restoring gray at S. The reverse rule uses the larger *immediate* up/left numbered neighbor and has an explicit stopping condition. It does not claim full rectification uniquely determines a start.
- Reset cards stay unchanged. The separate working boards have 30 mm square cells, and number/mask pieces are 26 mm square. At 100% print size there is useful clearance. The 26 mm ring and separate small S/E markers are workable on paper in principle; actual cutting/handling is not established by this review.
- Student questions are concise and substantive, with ample whitespace and no Name/Date, motivational filler or repeated page titles. Numbering is consecutive. Grade 2–5 labeling is an honest prerequisite band; a fabricated K–1 version would weaken the work.
- A supplied five-card catalog with a completeness question retains serious finite reasoning even though the number of cases is disclosed. The B and D catalogs make case coverage checkable and avoid asking children to transcribe all starts.

## Page-by-page visual coverage

I independently rendered both actual PDFs with PyMuPDF at scale 1.3 and opened every rendered page. Render files are in `critic-render/`.

| PDF/page | Inspected content | Result |
| --- | --- | --- |
| students 1 | Full forward example, three A starts, final grids | Clear; all labels and terminal dark square correct in the shown operation. |
| students 2 | A sorting/completeness question, blank shape, six workspace grids | Clear, no overlap. |
| students 3 | Four-state missing-mask bridge, D cases, reset wording | Clear visual distinction; label comparison and pooling wording need revision. |
| students 4 | B catalog question, representative starts, blank B shape | Clear layout; restore constructive target route. |
| students 5 | Four labeled D targets and sorting zones | Clear targets; B question ambiguity and physical card-zone fit noted above. |
| students 6 | Four-state reverse example, A2/A4/B4, boundary-marker rule | Clear; S/E remain legible, full reverse operation consistent. |
| students 7 | Larger-rule counterexample and local invariants, workspace | Clear and substantive. |
| materials 1–4 | A, B, D, and square-example board inserts | Individually viewed; outer masks match their shapes; calibrated 30 mm grids. |
| materials 5 | Five numerals, three gray pieces, eight dark pieces, ring, S/E | All pieces present and distinct; no overlap or clipping. |
| materials 6 | A1–A5 cards | All five diagrams and card labels legible. |
| materials 7 | D1–D6 cards | All six permutations present visually, with correct diagonal masks. |
| materials 8 | B1–B6 cards | All six diagrams and labels legible. |
| materials 9 | B7–B12 cards | All six diagrams and labels legible. |
| materials 10 | B13–B16 cards | All four diagrams and labels legible. |
| materials 11 | Six blank grouping cards | Clear, useful external record. |

Repeated headers/footers initially appeared partly omitted by the tool's image display. This was **not a PDF defect**: isolated header crops render normally, and all eighteen header pixel arrays match exactly at 2× scale. PDF text extraction also includes the headers. Do not make a layout change to compensate for that display artifact.

This review is not a classroom pilot, physical rehearsal, final-guide review, independent exhaustive math check, or source-ZIP rebuild. Those checks remain with the subsequent workflow stages.
