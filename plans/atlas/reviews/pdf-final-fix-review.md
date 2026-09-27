# Consolidated final PDF repair and release review

Completed 25 September 2026 by the designated final PDF fix agent. **Disposition: pass. All three queued PDF findings are resolved; no unresolved PDF defect remains from the independent review reports.**

This was the single consolidated repair round after the independent reviews of the two documents. It changed only the two PDF builders, not the mathematical family JSON or research surveys. The coordinator had already recorded the artifact-operation marker; it was not repeated.

## Final artifacts

| Document | Pages | SHA-256 |
| --- | ---: | --- |
| [Investigation plans](../../../lowell-math-circle-year-2/combined/math-atlas-investigation-plans.pdf) | 188 | d38774e70bf35938891ec9d234735b4f8efc2b85b73c40858c9d526ef7ae845e |
| [Research map](../../../lowell-math-circle-year-2/combined/math-atlas-research-map.pdf) | 82 | 097d939df9b8f534df09de49409ed4c8b7b51d191ba380ff5d3ca26b7fc1b3d5 |

The final machine record is [pdf-release.json](pdf-release.json). It includes artifact and input hashes, all 270 final page-image hashes, source and navigation checks, actual visual-review scope, and the closed findings. The build log, before/after snapshots, parser checks and verification script are in tmp/pdfs/atlas/final-fix/.

## Closed findings

1. **Material mathematical typography, research map page 38.** The renderer now lowers both letters of the single tt index and both xx indices in seeds 35-S01 and 35-S02. Bare subscripts accept consecutive letters; bare exponents still consume one letter, preserving adjacent factors such as x^i y^j. Grouped powers and indices retain their previous behavior. Five focused parser checks passed, including the two PDE formulas, adjacent monomials, grouped exponents, and an underscore-containing filename.

   I inspected the final complete page-38 PNG with the image-view tool. The wave and heat formulas now have correct, readable derivative indices, with no collision or layout regression. A separate PDF glyph-position check found exactly one tt and two xx pairs; both characters in each pair have identical lowered positions and font sizes, below the associated u. I also inspected unchanged research-map page 18 at full size and checked the glyph coordinates: x and y share the normal baseline, while i and j share the raised baseline. The page-18 image is byte-for-byte unchanged.

2. **Optional reciprocal navigation, investigation plans page 1.** The existing words “research map” in the scope paragraph now form an underlined, colored relative link to math-atlas-research-map.pdf. The paragraph's wording remains unchanged. I inspected the final complete page-1 PNG: the link is visible, the scope and attribution text fit cleanly, and no following page shifted. Annotation inspection confirms exactly one new URI link on page 1. The research map's existing reciprocal link to math-atlas-investigation-plans.pdf remains present.

3. **Render-directory maintenance, research-map builder.** Before rasterization, the map renderer now removes only page-*.png files from its own pages directory and contact-*.jpg files from its own contact-sheets directory. A controlled build check planted one stale matching filename in each directory and one unrelated text filename alongside it. The build removed both stale render files and preserved both unrelated files. The verification then removed its own unrelated sentinel files. The final directories contain 82 page PNGs and seven current contact sheets, without stale extra pages.

## Build and source verification

The complete prescribed build command, sh lowell-math-circle-year-2/source/atlas/build.sh, completed with exit status zero. It regenerated the indices and seed queue, built and rendered both PDFs, ran the independent print checker, and completed the structural release check.

- Page counts remain 188 and 82; all 90 families retain their two-page layout.
- The planning PDF passed the maker's per-family source-preservation check and the independent check of 3,108 source strings/URLs, with zero unmatched fields.
- The research map preserves the exact set of 231 seed IDs, all 231 full seed anchors, all 343 additional nonheading survey lines checked by the independent review, and all 81 distinct external survey URL targets.
- No blank pages, unsupported/missing glyph flags, replacement/null/square characters, out-of-page character boxes, raw Markdown-link markers, or raw LaTeX-command flags were reported by the applicable checks.
- All 12 captured mathematical and classification input files have the same hashes as before this repair round, including the three family files, three survey files, map lock, frontier, inventory, seed queue, field coverage and taxonomy. The final PDF metadata reports also agree with the current input hashes.
- The structural release check still records 63 surveyed fields, 231 research seeds, 90 reviewed planning families and primary-family representation for all 60 substantive fields. It does not treat descendants as reviewed or families as classroom-piloted.

## Navigation verification

All outline titles, nesting levels and destination pages were compared between the independently reviewed PDFs and the final PDFs. The plans' 191 outline entries and the map's 75 outline entries are unchanged. All 180 internal link annotations in the plans and all 178 in the map still resolve to the same valid page destinations. This preserves the reviewed indices and field/card navigation.

The existing source and companion URI annotations were also compared by page and target. None was removed or changed. The only added annotation is the new plans-page-1 research-map link. The final plans contain 92 URI annotations; the map contains 111. External website availability was not retested in this production pass.

## Visual-review continuity

The pre-repair artifacts were the exact hashes named in [main-pdf-review-ad-ga.md](main-pdf-review-ad-ga.md), [main-pdf-review-ga-ap.md](main-pdf-review-ga-ap.md), and [research-map-pdf-review.md](research-map-pdf-review.md). Those three reports account for all 270 pages at contact-sheet scale, together with their documented full-page samples and mathematical checks.

Before editing, I captured file and RGB-pixel hashes of every rendered page. After the full rebuild, I compared all 270 final page PNGs:

| Document | Changed pages | Unchanged pages |
| --- | --- | ---: |
| Investigation plans | 1 | 187 |
| Research map | 38 | 81 |

Thus **268 pages are byte-for-byte and RGB-pixel-identical to the independently reviewed versions**. Only the two intended pages changed. I inspected both changed pages as full-page images and additionally inspected unchanged map page 18 as the exponent-regression control. The coordinator independently inspected final plans page 1 and map page 38 and reported clean layouts and correct indices. No additional page changes required further visual inspection.

Current render paths are tmp/pdfs/atlas/plans/pages/page-001.png, tmp/pdfs/atlas/map/pages/page-38.png, and tmp/pdfs/atlas/map/pages/page-18.png. Complete render/contact directories remain under tmp/pdfs/atlas/plans/ and tmp/pdfs/atlas/map/.

## Scope and limits

This release closes PDF production findings against the exact final hashes above. It relies on the separately completed mathematical/editorial reviews and preserves their source-access limitations. It is not a claim of classroom testing, a physical-print trial, exhaustive coverage of mathematics, or fresh verification of every external theorem and website. If either PDF is rebuilt again, its hash and changed-page comparison must be rechecked before carrying this release decision forward.
