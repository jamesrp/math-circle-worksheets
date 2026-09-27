# Independent PDF review: research map

Reviewer: investigation-plan PDF maker, reviewing the other maker's research-map PDF. Date: 2026-09-25. Review is read-only: no PDF, builder or survey source was edited.

Reviewed artifact: `lowell-math-circle-year-2/combined/math-atlas-research-map.pdf`, 82 pages.

SHA-256: `2634dbb7ac3b6c0f5190fd6ce08b98c3d25f9a6f3dd341d5bcfa2483fae33994`.

The maker confirmed that `tmp/pdfs/atlas/map/pages/` and all seven contact sheets were rendered from this exact PDF and that no rebuild was underway. The page-map hash matches the independently computed file hash. All eight recorded source hashes match their current files.

**Disposition: one material mathematical-typography repair is required before publication.** The remaining coverage, navigation, source-caveat and layout checks described below pass. This is a PDF-production review, not renewed proof of every survey theorem or validation of classroom suitability.

## Required repair: complete derivative subscripts on page 38

Affected page: **38**, field 35, seeds **35-S01 and 35-S02**. Source: `plans/atlas/surveys/geometry-analysis.md`, line 93. Renderer: `math_text()` in `lowell-math-circle-year-2/source/atlas/build_research_map.py`.

The source contains:

- `u_tt=c²u_xx` in 35-S01;
- `u_t=u_xx` in 35-S02.

The renderer's bare-index pattern accepts a single letter. It therefore moves only the first t or x into subscript and leaves the second on the baseline. This visually changes the second-derivative notation into something resembling a first derivative multiplied by t or x. It is not an omitted character, so alphanumeric preservation checks pass despite the error.

**Exact required result:** both letters of `tt` and `xx` must occupy the same subscript position. Rendering the complete literal strings `u_tt` and `u_xx` is also an acceptable unambiguous fallback. Do not silently typeset a prefix of an index. The heat equation should read u with subscript t equals u with subscript xx; the wave equation should read u with subscript tt equals c² times u with subscript xx.

The complete affected set found in the three survey sources is **one `u_tt` and two `u_xx`**, all on this page. Other multi-letter strings following underscores occur in filenames or URL targets and do not represent mathematical indices in the printed paragraphs. Parenthesized multi-character indices, such as `L_(y')`, use the separate grouped branch and are not affected by this finding.

Repair the renderer, rebuild the PDF and rerender at least page 38. Verify both glyph baselines visually at full size and check the final PDF hash, page count, source preservation and navigation again. If pagination changes, regenerate all contact sheets and page references. No mathematical source edit is required. At the coordinator's request the maker was told to hold edits until the single consolidated final PDF-repair round.

## Coverage and text preservation

Independent results are saved in [research-map-pdf-independent-checks.json](research-map-pdf-independent-checks.json), separate from the maker's own structural report.

- **82 pages**; the shortest page contains 771 extracted characters, so there are no accidental blank pages.
- **All 63 field codes** in the pinned taxonomy appear as actual PDF bookmarks. Their code set was compared directly with `taxonomy.json`, not inferred from a printed count. The independent JSON records every code and destination page.
- **All 231 seed IDs**, with exact set equality against `problem-seeds.json`.
- **All 231 full seed anchors** found in normalized PDF text, not merely their headings.
- **343 additional nonheading survey lines** found in normalized PDF text across all three surveys. Lines containing the aggregated geometry “Anchors” paragraph were handled by the separate seed check. Survey headings are represented by the field-bookmark/contents checks.
- **81 distinct external Markdown URL targets** in the three surveys are all present as PDF URI annotations. The entire book contains 111 URI annotations, including repeated citations and front-matter links.
- The map-lock, snapshot counts and frontier are present. The cover and reading guide distinguish 63 field dossiers, 231 research seeds and 90 developed families. Page 6 explicitly identifies fields 00, 01 and 97 as support dossiers, leaves the 6,540 descendant rows individually unvisited, and disclaims exhaustive coverage and classroom evidence.

Normalization removed markup/URL targets, folded Unicode compatibility characters and ignored nonalphanumeric differences. This is useful completeness evidence but cannot certify mathematical punctuation, signs or subscript placement. The required page-38 finding demonstrates that limitation; rendered mathematical pages were checked separately rather than treating text preservation as a sufficient test.

## Navigation

The actual PDF contains **75 outline destinations**, including all 63 field headings. The contents occupies pages 2-5; the reading guide, map lock, three parts, source register and frontier have appropriate destinations.

I inspected **178 internal link annotations** and found no internal array destination referencing a missing PDF page. The field bookmark code set equals the official top-level code set. Printed contents numbers were compared against the page map on contact sheets, including the transitions to geometry/analysis (page 29), probability/applications (page 58), and frontier (page 80). No discrepancy was found.

Source-register links and inline references remain available; the companion-plan link is present. This review verified annotation targets structurally rather than manually clicking every link in a PDF viewer. It did not reopen all external websites, so current network availability of every cited URL is not certified.

## Visual inspection

All seven contact sheets were inspected, covering **every page from 1 through 82**. The pages show consistent margins, intact headings and footers, stable page numbering, legible field identifiers, and no accidental blank or isolated-overflow pages. Giving each field a new page leaves deliberate open space on shorter dossiers; this improves field-level browsing and is not a missing-content symptom.

Full-size PNGs inspected:

| Page | Reason and result |
| --- | --- |
| 6 | Dense scope text, MSC attribution and coverage table; readable, table fits and caveats remain explicit. |
| 17 | Finite-field symbols, polynomial quotient, radicals and degrees; readable supported notation, with the documented double-struck-F fallback retaining the finite-field meaning. |
| 22 | Lie/Jordan/octonion notation and source cross-references; operations and parentheses are intact. |
| 27 | Dense inspected-source register; titles, locators and differing evidence claims remain legible and within margins. |
| 38 | PDE formulas; found the required multi-letter subscript repair above. Exponential, minus, Greek xi and other surrounding symbols are present. |
| 47 | Functional-analysis theorem hypotheses and higher prerequisites; clean layout and complete lines. |
| 66 | Optics hypotheses, concrete entrances and failed-access caveat; clean and fully visible. |
| 81 | Three-column frontier table; complete cell text, readable wrapping, no clipping or row overlap. |

The maker's missing-glyph, page-boundary and raw-markup checks were also inspected. They reported no unsupported glyphs, replacement characters, raw Markdown links, raw LaTeX commands or out-of-bounds characters. These reports are consistent with the inspected images, apart from the semantic subscript-placement defect that such checks do not detect.

## Source evidence and review limits

The PDF preserves screening-stage limitations instead of turning them into verified-theorem claims. Page 27, for example, says the Euler item was inspected through metadata and a content summary, not original-paper text. Page 66 retains the failed original PDF access and distinguishes the inspected exposition from later family checks. Page 6 explains why retained survey references to future work are historical research-stage statements even though family review has since occurred. This is an effective safeguard against reading every survey source entry as a fully checked continuation.

The publisher attribution, license link, no-endorsement statement, and distinction between classification-derived content and cited mathematical works are present. The frontier preserves the need for further model, prerequisite and source work, along with the difference between a broad atlas and a 120-session elementary route.

No claim is made that all 82 pages were read word by word at full magnification, every source was revisited, or every research anchor was re-proved during this PDF review. Every page was visually inspected at contact-sheet scale, eight selected pages were inspected at full size, and automated source-content checks cover the entire volume. The one required repair must be closed against the final rendered PDF before this review can support release.
