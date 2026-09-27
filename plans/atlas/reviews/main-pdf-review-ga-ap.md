# Main PDF review: GA-13–GA-36 and AP-01–AP-30

Reviewer: geometry/analysis agent, independently of the PDF builder. Completed 25 September 2026.

**Decision: pass for the assigned scope. No PDF correction is requested from this review.** The PDF and builders were treated as read-only. This is visual and mathematical-text preservation review, not classroom validation.

## Artifact and scope

- PDF: lowell-math-circle-year-2/combined/math-atlas-investigation-plans.pdf
- SHA-256: 1088821a593918a3c4080a44a7d123791f694c4b4ae96cbeada722d2305073b1
- Total length: 188 pages.
- Assigned cards: GA-13–GA-36 and AP-01–AP-30, 54 cards.
- Assigned pages: **81–188 inclusive, 108 pages**.
- Every card occupies two pages: participation/launch on the odd page, facilitator reasoning on the following even page.
- Page map: tmp/pdfs/atlas/plans/page-map.json.
- Read-only source/navigation check results: main-pdf-ga-ap-checks.json.

The hash was checked again after visual inspection and remained unchanged.

## Visual inspection actually performed

I used image-view tools to inspect **all seven assigned contact sheets**, contact-06.png through contact-12.png, in tmp/pdfs/atlas/plans/contacts/. Together they cover every assigned page from 81 through 188.

I also used image-view tools on **56 complete individual page PNGs** at their rendered full-page resolution:

- Every facilitator-reasoning page from **82 through 188, inclusive, at increments of two**: all 54 assigned cards.
- Participation pages **157 and 185**, specifically checking the repaired quantum scaffolding and prefix-decoding gates.
- Page 138 was additionally reopened individually to confirm its heading and confidence-interval source presentation.

Thus each assigned mathematical topic received a full-page visual inspection, beyond its contact-sheet inspection. All assigned participation pages were seen in contact sheets; the two repair-sensitive participation pages were also examined individually. I did not inspect every participation page individually at full size.

The renderer supplied 90-dpi page PNGs. The visible body text, small source blocks, mathematical symbols, headings, and footer numbers were legible at the displayed full-page size. No higher-resolution physical print test was performed.

## Visual findings

No clipping, overlapping text, stranded heading, blank content page, unexpected third-page continuation, or content crossing the footer was observed within the assigned scope. The two-page structure is consistent, including long titles on pages 102, 114, 122, 128, 144, 152, 157, and 158. Source blocks remain on their reasoning pages, and the body/source/footer hierarchy is clear.

Formula-heavy pages inspected include minimax inequalities (82), Walsh signs and coefficients (86), the integral equation (90), function-space norms (94), piecewise-C¹ energy reasoning (96), spherical transport (102), knot-coloring identities (108), Cantor coding (114), Laplace expressions (122), circle means (126), Snell derivatives (152), quantum vectors/projectors (157–158), proper time (162), and feedback/observability formulas (180–182). Mathematical minus signs, inequalities, arrows, superscript digits, Greek letters, integrals, and infinity glyphs remained visible. The angle-bracket fallback in AP-13’s normalized intensity expression on page 154 rendered as readable brackets, without missing-glyph boxes.

The output retains plain-text mathematical conventions such as slash fractions, caret powers, and underscore indices where present in the source. These were checked for fidelity, not silently converted into new mathematical notation.

There were **no flagged pages** from the maker’s geometry/glyph report or the coordinator’s independent print checks requiring a separate defect follow-up. The complete assigned range was nevertheless visually inspected.

## Source-text preservation

An independent comparison checked **2,032 source text leaves and source URLs** across all 54 assigned cards against their mapped PDF pages and annotations. There were:

- Zero missing or altered normalized source text leaves.
- Zero missing source-URL annotations.
- No source cards omitted.

Comparison normalized whitespace, Unicode compatibility characters, and the documented prose-dash conversion. It did not treat a finite visual sample as proof that every character rendered; the image checks separately assessed actual glyph appearance.

The maker’s broader source-preservation and glyph reports and the coordinator’s report also had zero source-field or geometry flags. These reports were treated as corroboration, not a substitute for the image inspection.

## Repair-sensitive checks

The latest reviewed wording is preserved, including:

| Card | PDF pages checked | Preserved clarification |
|---|---:|---|
| GA-20 | 95–96 | Continuous piecewise-C¹ competitors; finite partition; fundamental theorem applied piecewise; continuity at joins |
| GA-22 | 99–100 | Planar Radon cases include collinear and boundary configurations |
| GA-28 | 111–112 | Bisection bounds; AP-06 Newton-cubic reuse explicitly identified |
| GA-29 | 113–114 | Finite closed covers may be enlarged to open covers with arbitrarily small extra length |
| GA-36 | 127–128 | Explicit centered affine contraction and error bound; existence remains distinct from convergence |
| AP-03 | 133–134 | Permutation-mechanics source scope distinguished from the independent sharp-null design proof |
| AP-05 | 137–138 | NIST repeated-sampling interpretation; five-error construction distinguished from the handbook’s t interval |
| AP-15 | 157–158 | One-transition scaffolding; recorded Z outcomes distinguished from equal final unconditional mixed states |
| AP-17 | 161–162 | Author-hosted Tong source and proper-time equation locator |
| AP-25 | 177–178 | Missing enabling reactants distinguished from timing-dependent claims |
| AP-28 | 183–184 | Padding proof extends length-four impossibility to every shorter length |
| AP-29 | 185–186 | Prefix-free immediate decoding distinguished from general unique decodability |
| AP-30 | 187–188 | Correct current split and no-www source URL with precise Ohm-law locator |

All source and status limitations remain visible, including the fact that these are plans with checked instances and have not been classroom-piloted.

## Navigation and links

The PDF has 191 outline entries. For this assigned scope:

- All **54 participation bookmarks** point to the participation pages in the supplied page map.
- All **54 reasoning bookmarks** point to the corresponding reasoning pages.
- Every assigned participation page appears among the front-matter index’s internal targets.
- The first eight PDF pages contain **180 internal link destinations**; none referenced an invalid page.
- All assigned source URLs appear exactly in link annotations on their card pages.
- Printed page numbers seen in the rendered images match the page-map numbering.

External URLs were checked for preservation against the approved source JSON; this PDF review did not re-fetch every linked website. Prior source-retrieval limitations remain documented in the mathematical reviews and the individual cards.

## Handoff

No change to the main PDF is requested for pages 81–188. If the designated fix agent rebuilds the document for findings from another reviewer, rerun the source/navigation checks against the rebuilt PDF and inspect any changed assigned pages. This pass applies specifically to the hash recorded above.
