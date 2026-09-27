# Editor PDF checks

25 September 2026. These checks supplement the independent full-volume PDF review; they do not replace image inspection.

The root editor ran `source/atlas/verify_print.py` against the first complete print builds: 188 investigation-plan pages and 82 research-map pages. All 3,108 checked source strings or URL targets in the family data were present in the investigation book, allowing only whitespace and typographic normalization. Neither PDF had a blank page, character box outside the page, null/replacement glyph, or unexpected black-square character. The maker's per-family checks additionally restrict matches to the correct two-page card rather than the whole book.

A separate source-font preflight found four codepoints absent from Arial Unicode. The plans maker uses a verified fallback font for its angle brackets; the map maker documents explicit mathematical typography mappings. Presence in extracted text alone does not verify a visible glyph, so these are included in the independent page review.

The editor also independently matched all 231 seed-anchor texts from `problem-seeds.json` against the research-map extraction after stripping Markdown and normalizing printed mathematical typography. All were present. This supplements, rather than upgrades, the survey seeds' own review status.

Actually inspected as images by the root editor:

- Research map contact sheet 1, covering pages 1-12: cover, contents, scope, coverage table, section opening and first dossiers. No clipped or overlapping elements observed.
- Research map full pages 27 and 68: dense source register and quantum-theory dossier. Links, source limitations, mathematical text and hierarchy are readable.
- Investigation plans full pages 9, 54 and 158: concrete logic launch, advanced K-theory reasoning and quantum-measurement reasoning. Body, symbols, answers, source-status text, hard prerequisites and footers are readable without overlap.

The two-page participation/reasoning split preserves the full family record. This is a facilitator reference design, not validation of student diagrams or classroom timing. Independent reviewers inspect all contact sheets plus additional full-size pages; their reports record the broader scope and any repair requirements. Final hashes are recorded after the repair/recheck stage.

## Final repaired-page check

After the consolidated rebuild, the root editor separately viewed the final full-page PNGs for research-map page 38 and investigation-plan page 1. Both letters of each derivative subscript are now lowered together, surrounding equations are intact, and the companion-book link is visibly present. Neither page has clipping or overlap. The fix agent's recorded comparison finds the other 268 page images unchanged, preserving the earlier independent visual review. See the consolidated final-fix report and `pdf-release.json` for exact final hashes and comparison scope.
