# Week 90 revision stage

Fresh reviser, 2026-10-17. Read PROMPT.md, REVISE.md, critic review, independent mathematical review, draft sources and rendered PDFs. Explicit shared Grades 2–5 override retained: final/students.pdf (8 pages, 9 consecutive problems) and final/materials.pdf (11 pages). No forced K–1 packet. No guide authored in this stage.

## Changes and exact final mapping

| Student page | Final problem | Former problem | Content |
|---|---|---|---|
| 1 | 1 | 1 | Complete forward example; A1/A3/A5 outline comparison, unchanged. |
| 2 | 2 | 2 | Five A starts, outline groups and completeness, unchanged. |
| 3 | 3 | 3 | Full next-corner bridge unchanged. Six D starts may be shared. Whole-order comparison explicitly asks about the outline and the position of any number. |
| 4 | 4 | New restored route | Construct an increasing B start using 1–5 for each of three actual five-cell target outlines: (3,2), (3,1,1), (2,2,1), left to right. A blank B start and three extra blank B workspaces are provided. No catalog witness is printed here. |
| 5 | 5 | 4 | All sixteen B cards retained as a pooled investigation, with both first-corner choices for each card, explicit full labeled-output comparison, outline classification and completeness. |
| 6 | 6 | 5 | Four labeled D targets and preimages retained. Misleading too-small dashed card mats removed; cards retain their original size. B comparison explicitly concerns a finished five-number arrangement. |
| 7 | 7 | 6 | Complete recorded reverse example, A2/A4/B4 trials, unchanged except numbering. |
| 8 | 8 | 7 | Larger-forward-rule counterexample search, unchanged except numbering. |
| 8 | 9 | 8 | Label conservation, increasing order and termination, unchanged except numbering. |

New construction witnesses independently checked against the fresh math review's enumerator: B8 reaches (3,2), B3 reaches (3,1,1), B1 reaches (2,2,1). The new task preserves search and design; it neither requires the full catalog first nor supplies a solving procedure.

## Guide handoff

- Route directly from a successful one-hole trial through one D start with both full orders into Problem 4 construction when ready. Full D/B catalogs remain optional pooled continuation; rich reverse, counterexample and local-proof routes remain available for return visits.
- Before a reset, save one labeled final board on a blank grouping card or adult board, then rebuild from the unchanged start card. Compare that saved board with the second result. Keep this optional record scaffold in the adult guide.
- Problem 6 is tabletop sorting: place cards near the four target diagrams or corresponding grouping cards. No promise of fitting cards into a printed page zone remains.
- Materials pages unchanged: 1 A board; 2 B board; 3 D board; 4 square worked-example board; 5 piece kit (five numbered 26 mm squares, three gray, eight dark, one ring, S/E); 6 A1–A5; 7 D1–D6; 8 B1–B6; 9 B7–B12; 10 B13–B16; 11 six blank grouping cards. Board cells remain 30 mm and catalog cards 80 × 66 mm. A first visit need not prepare all eleven material pages.
- General rectification independence remains a theorem under ordinary skew, distinct increasing-label assumptions, attributed in the guide; finite catalogs prove only their finite instances. Recorded single-slide reversal requires actual S/E endpoints and final state, not arbitrary markers.

## Verification

Copied draft/src to final/src and revised the generator, then rebuilt both matching TeX/PDF outputs. Builder now compiles twice so even a fresh build resolves TikZ page anchors without warnings. Final logs have no LaTeX warnings, overfull boxes or underfull boxes.

Ran unchanged independent check_math.py successfully; saved output in final/independent-math-results.json. This covers 49 catalog full rectifications and 317 small standard skew starts / 465 complete corner sequences, including each step's order and label invariants and exact single-slide reversal. Restored target shapes use already verified B outcomes; the three witnesses above were rechecked separately.

Rendered all 8 student and 11 material pages at 1.3× with PyMuPDF into final/render/ and opened every PNG individually. All diagrams, numbers, masks, target silhouettes, examples, whitespace and page numbering are legible and free of overlap/clipping. All 19 header crops are pixel-identical at 2×; the image tool's omission of repeated header/footer content on some displayed images is a display artifact, not a PDF defect. All eleven material pages are pixel-identical to the reviewed draft. Machine-readable verification and stage PDF SHA-256 values are in final/revision-checks.json.

This is digital verification only: unpiloted, physical cutting/handling not rehearsed. Final student/guide pair review, source packaging and clean ZIP reconstruction remain with the coordinator/publication workflow.
