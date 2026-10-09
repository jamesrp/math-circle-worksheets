# Week 79 revision stage

The fresh revision agent read the writer prompt, the selected-band override, the adversarial review, the independent mathematical review, and all editable student-stage sources. The original draft is preserved. Only `final/src` and revision evidence were changed; the separate facilitator source remains owned by the integration agent.

## Student changes

- Problem 1 now gives six enacted days using cards 1–12 as the concrete first route. Continuing to twelve days using all 24 supplied cards is optional. The equal-count investigation remains open and substantial.
- Problem 2 now asks for a rule for any numbered label, with 3, 6, 10 and 20 as checks/prediction. It preserves the supplied day spaces and does not disclose the transfer-day rule.
- Problems 3–4, the explicit input/add/transfer visual, the 24 unique 30 mm cards, and the two 180 by 96 mm A/B regions are retained. Grades 2–5 entry points remain on pages 1–2; the eventual-membership question on page 3 is Grades 4–5.
- The source README now records the revised scope, first route and separate facilitator ownership.

## Review issues reserved for the guide

The root agent must choose one primary physical state representation (mat or bowls), make the finite-label observation operational without moving cards, qualify the N+1 witness by N≥1 while handling day 0 separately, and restrict the indicator supremum claim to n≥1. These are guide-only issues; no facilitator source was edited in this revision stage.

## Checks

`final/src/build.py` made two fresh five-page PDFs in separate temporary compiler directories; their bytes were identical. The builder rejects TeX overflow. SHA-256: `b924d6631e3567547fab92a9b186c669c1671187d99cadeff6f513a3fe624493`.

All five final pages were rendered with PyMuPDF, reopening the PDF for each page, and visually inspected. All text spans remain inside their page. Ghostscript independently rendered all five pages; each was inspected, and a cropped header composite corroborates every required header. An apparent full-page image-presentation omission was resolved by inspecting the actual header pixels and crop composite; the PDF headers are present.

The writer’s finite checker passes 1,000 days per rule. The independent replay implementation passes 500 days per rule including day 0, all finite membership/count formulas, and the four printed transfer labels. Cutout labels 1–24 and geometry were rechecked against source. These finite checks support examples; the infinite claims depend on the induction and chosen eventual-membership interpretation in the mathematical review.

Evidence: `render-revision/QA.json`, `render-revision/page-1.png` through `page-5.png`, independent `gs-page-1.png` through `gs-page-5.png`, and `headers-corroboration.png`. The duplicated temporary rebuild PDF was removed after byte comparison.

The activity is **unpiloted**. Actual paper cutting, physical fit, card handling and classroom procedure remain **untested**. No commit or push was made by this stage.
