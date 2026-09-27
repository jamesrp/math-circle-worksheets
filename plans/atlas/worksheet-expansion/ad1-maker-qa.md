# AD-01–08 maker PDF review

September 25, 2026. Maker review complete; independent design review is closed in `review-ad1-design.md`. Independent PDF review remains a separate release gate.

## Current preview and exact coverage

The current preview is `tmp/pdfs/atlas-remaining/ad1-preview-r2/`:

- `atlas-ad1-student-worksheets.pdf`: 26 pages, one contents page plus all 25 planned student pages.
- `atlas-ad1-facilitator-guide.pdf`: 40 pages, including contents.
- `qa/student/` and `qa/facilitator/`: full 110-dpi page renders, contact sheets, extracted text and build reports.

Student PDF SHA-256: `8c12b9ac4409aa8d0f3586f45d21f18eed13e64b4f0c657129ce9b95f5fd546b`.

Guide PDF SHA-256: `eb5bf10c42352f916e4a16ad5e8d3b2f39ae6225002fa5610c887dba5e028ca6`.

All student pages 1–26 were inspected at full size in the initial `ad1-preview/`. Repaired pages 1, 3, 6, 10, 11, 14, 20 and 21 were inspected again at full size under the fresh `ad1-preview-r2/` path. SHA-256 comparison of every page PNG confirms these are exactly the changed student images; every other current page is byte-identical to the previously inspected image. Thus all current student page bodies are covered by the visual pass without claiming a second full pass.

All 40 current guide pages were inspected on the five fresh contact sheets. Current guide pages 1, 13, 16, 19, 24, 25, 26, 28, 30, 34, 38, 39 and 40 also received full-size inspection, covering contents, every worked diagram, the long inverse proof, determinants, the advanced theorem explanation, closure proof and quotient classification. The shared guide changes that removed repeated verification-only paragraphs are included in this fresh pass.

## Repairs made and visually closed

1. Removed exact-count workspace cues: two counterworld mats in AD-01, sixteen pattern strips in AD-02, three chain strips in the AD-03 continuation, two minimum-generator mats in AD-07. Open work areas now leave the number of objects/results to the learner.
2. Replaced the exactly-eight AD-05 catalog frames with twelve unnumbered reference frames; learners choose which to use. All diagrams retain the supplied five-road graph without printing any selected tree.
3. Drew the supplied AD-04 Tree Y without crossings; added removed-leaf records for both examples and an explicit numbered-circle vertex convention. The worked five-label guide tree is also planar and matches the ledger.
4. Changed AD-06's one-comparison repair workspace to permit moving/redrawing tiles so comparison arrows can point upward. Prompt 6 now explicitly allows either direction between r and s, with the corresponding proof unchanged.
5. Rebuilt contents and guide after the editor's shared pagination changes. All final contacts and the new contents page were rechecked.

The AD-06 wording is a representation clarification: the same two repairs were already proved and checked. The AD-04 vertex convention clarifies the existing graph task. No new mathematical instance or weakened proof was introduced during production.

## Mathematical fidelity and usable diagrams

- AD-01: four object types remain labeled for monochrome printing; worlds have room for witnesses; the four-type certificate and empty red-class issue are preserved.
- AD-02: four-bit words/positions are legible, the method is on a later page, and the finite boundary has no pre-counted answer scaffold. Infinite-sequence work has a separate prerequisite gate.
- AD-03: all sixteen subset cards are present once; empty and full cards are distinguishable; the chain certificate appears only in the guide. Forced-card work has open organization space.
- AD-04: both supplied edge sets and all labels match data; only numbered circles are vertices; the decoder is staged after the first communication attempt. Repeated code entries and changing survivor sets remain explicit.
- AD-05: perimeter and diagonal are distinct, all four labels remain in every frame, the added-diagonal crossing is not a vertex, and the determinant page is visibly optional/advanced. The eight guide trees match the two-case classification.
- AD-06: all upward arrows and absent comparisons match the two orders; set recipes are printed beside the work; the guide diamond gives every intermediate operation. Repair space does not force a false horizontal comparison convention.
- AD-07: all rules and token types remain visible, separate runs can be recorded, and no minimum-generator answer count is suggested by the workspace.
- AD-08: the addition ring and table use the same four residues; learner partitions are blank, parity is not announced before the task, and guide partitions/table agree with the complete classification.

## Verification and limits

The renderer is `lowell-math-circle-year-2/source/atlas-remaining/ad1.py`, using `common.start` and `common.question`. The build records all 50 student prompt IDs exactly once; every prompt has its solution and hints, and all eight optional extensions are solved. The current build reports zero blank pages, zero out-of-page text and zero suspect glyphs in either PDF. The exact mathematical checker was rerun successfully after the production edits: eight families and 50 prompts, with the exhaustive finite checks documented in `ad1-design.md` and `ad1-checks-results.json`.

These mechanical and finite checks support the written arguments; they do not certify every visual property or replace general proofs. Classroom engagement, timing and preparation remain unpiloted. No final combined book was written by this author and no additional artifact marker was run. Independent PDF review and editor assembly checks remain pending.

## Independent-review repairs: current r3 preview

The independent reviewer identified two wording issues. AD-02 prompt 2 now says “without searching through every possible word,” preserving the later discovery of the complete list size. AD-06 prompt 6 now defines a lattice as a diagram in which every pair has both JOIN and MEET. Both have been repaired in data and rebuilt under `tmp/pdfs/atlas-remaining/ad1-preview-r3/`.

I inspected the four changed images at full size: student pages 5 and 20, and guide pages 7 and 29. All are clean. Byte comparison of every PNG confirms all other 62 pages are identical to r2. Counts remain 26 student pages and 40 guide pages; blank/bounds/glyph checks and the exact mathematical checker pass. The current PDFs have hashes:

- Student: `616160d8c15ca1c8dff1ca21e504c00d1f3954a9b82595629ce22ee144da14f3`.
- Guide: `a82799ea8592cb34f45785d324144e7009edd98b5c8cf9212053b06972eefaaa`.

The independent reviewer has been sent this fresh path for closure. Earlier coverage statements remain valid through the checked page-image identity; r3 supersedes r2 as the current preview.
