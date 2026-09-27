# AD3 maker QA — independent PDF review handoff

September 26, 2026. Current preview: `tmp/pdfs/atlas-remaining/ad3-preview-r3/`.

The custom module is `lowell-math-circle-year-2/source/atlas-remaining/ad3.py`. Design review is closed in `review-ad3-design.md`, including the explicit AD22 basis orders and the AD20 trace-zero Lie-algebra center proof completion. The earlier author draft is archived under `archived-drafts/`; production uses `ad3-data.json` only.

## Coverage and mathematical fidelity

All 24 planned student bodies plus contents were inspected at full size: **student pages 1–25** in r1. After the first maker repairs, r2 student pages **11, 16, 17, 18, 20** were inspected full size under the new path. Every other student PNG was byte-identical, and all 25 student PNGs in r3 are byte-identical to r2.

All **41 guide pages** were inspected in r2 contact sheets 1–5. Dense mathematics, source/extension pages and figures were inspected full size on guide pages **1, 3, 4, 5, 7, 8, 9, 10, 12, 13, 14, 16, 17, 18, 19, 21, 22, 23, 24, 26, 27, 28, 29, 30, 32, 33, 34, 35, 37, 38, 39, 40, 41**. Final spacing edits changed only guide pages **8, 9, 11, 21, 27, 34, 37**, all freshly inspected at full size in r3; the other 34 guide PNGs are byte-identical to r2. Thus every final page is covered by direct inspection or verified byte identity with the inspected version.

The checker `ad3-checks.py` passes on current data: eight families, 24 planned bodies, 48 keyed prompts, eight solved extensions. The builder confirms every prompt printed exactly once, planned page counts, and zero blank pages, out-of-page characters or suspect glyphs. This finite/mechanical evidence supplements the written proofs and visual pass; the investigations remain unpiloted.

Family-specific maker checks:

- AD17 number line runs −4 through 10, marks only the supplied −3 and 9, and leaves an open round ledger. No five-round scaffold or limit marker leaks the threshold. Exact first-entry inequalities and endpoint cases were read in the guide.
- AD18 coordinate grids use equal x/y scales. The unit input square is dotted, the supplied u/v arrows are solid, and learners complete their own image parallelograms. Guide page 9 shows correct vertices, orientation and areas for k=1 and k=5. The collapse and inverse/Gram proofs agree with these objects.
- AD19 open basis ledgers disclose no answer-sized block counts. The given three block types appear only when the page defines them. Source/target basis recovery, minimal rank, similarity distinction and two-arrow extension remain fully keyed.
- AD20 order diagrams apply the rightmost factor first and now leave a large product/vector workspace. Jacobi columns label expressions but contain no expanded terms. The center key proves both the full-matrix center and the center of the trace-zero Lie algebra using N and C−I/2.
- AD21 inventories retain every name and printed color word, including unused w. No eight-slot answer catalog is supplied. Duplicate tokens and the two universal maps are separate tasks with sufficient record space.
- AD22 O is an actual solid center vertex; its label was moved off the spoke. Available face cards are shown separately from edge selections. Blank student matrices have the explicit vertex/edge/face orders. Guide page 29 has the correct 5×8 and 8×2 boundary matrices and quotient/cap explanation.
- AD23 paired component diagrams explicitly say circles mark basis directions, not elements of finite sets. Complement dimensions stay blank. The guide distinguishes an actual module from a signed formal difference and proves group completion in both directions.
- AD24 one reusable six-position ring and an open catalog leave the answer count undisclosed. Clockwise order and top mark are explicit; reflection is introduced only on the third page. The six turn rows are supplied group elements, not necklace slots. Guide page 40's four representatives and orbit sizes 6,6,6,2 match the proof.

## Repairs during maker review

Concrete prose/math boundary spacing was repaired before rendering and in the final guide pass. The AD20 diagram was narrowed to make room for full products. O's label was offset from a spoke. The AD23 basis-direction caption was added. Root independently reread and closed the additional AD20 trace-zero-center proof sentence. No mathematical instance, answer or family scope changed. Two source-only guide pages are intentionally retained; substantive source evidence was not deleted to meet an arbitrary page count.

## Current identity and status

Student: **25 pages**, SHA-256 `f30bb7353386edd3c442c01d3805ea596155cf2b7c9da7c5cd3119bef7c4d4af`.

Guide: **41 pages**, SHA-256 `e3d481c0bae31b891675b700bca0586ef75b7cf77c28ba79f64f468fa8b592f5`.

Data SHA-256 `6d52e9aa454b444abb055893a74954db9a5b3f6900bb0e6fda31ff2b2b2c4116`.

Module SHA-256 `fff5ee125cd0ca87eec96933fa7a25cf4e33046d6bf84fa844393815cf6f531d`.

Maker pass complete. Assigned independent PDF reviewer: worksheets_geometry. No final combined books written and no additional PDF operation marker run. Independent PDF review and any repair closure remain before assembly.
