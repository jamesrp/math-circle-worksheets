# Week 53 return-visit guide: reviser report

**Revisions ready; packaging waits for catalog integration.** Final: `final/facilitator.pdf`, **7 pages**, W53-RV-FAC-v2. The original 8-page draft, writer report, Claude review and critic checks remain unchanged. This is a new, untested guide: **untested with children and physically unrehearsed**. No student page, existing guide, catalog file or packaged folder was changed.

The six should-fix findings and all thirteen minor findings are addressed; none is declined. The guide is 4,248 words by PyMuPDF extraction (including recurring headers/footers), about 500 words shorter than the critic's approximate 4,750-word draft count; those counts are approximate and not identical tokenization. It is still substantial because complete answer catalogs, the route certificate and general proofs remain.

## Findings disposition

| Finding | Result |
|---|---|
| Must-fix | None in the critic review. |
| Should 1 | K–1 first route is P1, P2, P4, then P3/P5; grades 4–5 starts P1, P3, P7, then P9/P10. Catalogs may be pooled; later visits are explicitly named. |
| Should 2 | Preparation identifies K–1 newcomers, the limited base-week experience of many third graders, and the repeated maps with their base problem/page references. Optional base print is only p. 3. |
| Should 3 | Overview names band discoveries: first common groups, save/tie/extra optional places, lowest-dearest thresholds, repriced trips, and the explanations/limits. Distinguishes conjecture, complete finite catalogs and general arguments. |
| Should 4 | Shared non-task launch now states the network's goal and the aim to spend as few counters as possible. |
| Should 5 | Parent volunteer anchored to K–1; explicit oral reading/pointing for K–1 P2 and grades 2–3 P3, adult rings on tiny records, pooled six-network catalogs, paraphrase of P10 changes and Lee's claim. Child choices remain central. |
| Should 6 | Removed duplicate grades 4–5 keys for P1/P3/P7, repeated P8 table rows, duplicated overflow advice, and the base guide's transformation proof (now precisely cited to W53-guide-v4 p. 7). Tightened other keys without dropping answers or completeness arguments; flowed keys across seven pages. |
| Minor 1 | Optional-place caveat now includes route, price-list, cost-from-groups, repricing and converse claims. |
| Minor 2 | Says “On all three maps the cheapest network is …”, avoiding a false three-optima reading. |
| Minor 3 | Replaced unclear triangle hint with a direct question about holding the right side fixed. |
| Minor 4 | Grades 4–5 P2 hint asks what is shared/different rather than prescribing product organization. |
| Minor 5 | Spare record maps expressly mean workspace in both six-network catalogs and P4. |
| Minor 6 | Added the non-order-preserving p → 7 − p example: minimum 15 and the previous network ceases to be optimal; independently enumerated in final checker. |
| Minor 7 | Lee's claim is first tested on Sam's cost-9 square purchase (A–B dearest 3 versus direct AB price 1); checked by script. |
| Minor 8 | The five-minute launch includes free handling and fits the sixty-minute timetable. |
| Minor 9 | Names the tight six-place grid and page numbers for tape rehearsal; sleeves/pens explicitly support erasable rings. |
| Minor 10 | Removed optional base p. 4 print; that map is already reprinted. |
| Minor 11 | Headings punctuated and grade labels replace young/middle/upper cross-references. |
| Minor 12 | Source notes map Hu/widest-path, Sedgewick/Wayne exercises and Steiner-tree background to the actual relevant problems; preserve unavailable-originals limits. |
| Minor 13 | Checker pins normalized extracted student text plus exact problem/page maps, rather than PDF metadata bytes. Byte hashes of actual unchanged inputs remain in verification.json. |

## Verification and mathematical checks

Read the outline, repository guidance, final three student PDFs, the draft guide and critic report, and the base Week 53 guide. Rendered and inspected every student page: K–1 **7 pages**, grades 2–3 **6**, grades 4–5 **10** (23 pages total). The guide follows final-PDF numbering: K–1 P1–6 pp. 1–6 and P7–8 p. 7; grades 2–3 P1–2 p. 1, P3 p. 2, P4 p. 3, P5 p. 4, P6–7 p. 5, P8 p. 6; grades 4–5 P1–4 pp. 1–4, P5–6 p. 5, P7 p. 6, P8 p. 7, P9 p. 8, P10 p. 9, P11–12 p. 10. These maps are also checked automatically.

Ran the preserved critic's `review-guide-check/check_answers.py`: every assertion passes. Ran the final portable checker: all finite answer sets, all “find all” lists, threshold groups, complete trip lists/distance certificates, inverse-price formulas (all 512 positive triples 1–8), optional-place contrasts and the cap-10 change barrier pass. The added reversed-price and Lee/Sam examples are recomputed there. General results retain cut, equal-link-count and leaf-count arguments; finite checks do not replace those proofs.

Checked material arithmetic: five 30-counter/10-strip kits plus 15 demonstration counters/four strips = **165 counters, 54 strips**. Verified 33/32-counter side-by-side comparisons exceed a kit, and the printed squared price 36 requires written trial totals. Actual working maps and record maps were visually distinguished; the retained critic's geometry evidence measures working places about 10 mm and spacing at least 40 mm. The non-task launch's 2/3 prices, 0/2/5 trays and XYZ/XYZY trip totals are checked. No physical fit or timing claim is inferred from these digital measurements.

`final/src/build.sh` was run successfully with real pdfLaTeX twice per build: **no compilation errors or overfull boxes**. Rendered and inspected all **7 final guide pages**, including tables, theorem formulas, launch drawing, labels, margins and footer references. No unresolved references or clipped/overlapping content. A clean copy of only `final/src/` and the three final student PDFs was rebuilt **outside the repository**; checker passed there and rebuilt **PDF bytes and extracted text were identical**. Machine-readable hashes/results: `final/verification.json`; checker output: `final/check-output.txt`. Parent coordinator may repeat these checks independently.

## Student-page issues worked around (pages unchanged)

- K–1 P8 leaves positive whole-number invented prices implicit; guide supplies “at least one dot per road.” Its full formula handles unbounded values and rejects the tempting 1,1,6 sum-only answer.
- Grades 2–3 P6 permits strict versus tied readings of “cheapest”; guide accepts the weak tied reading with explanation rather than treating it as a child's error.
- Small duplicate maps are pen-only records, not extra answer counts or counter mats. Adults may record K–1's groups.
- The reused kit cannot hold all conceivable trial purchases or both large comparison piles; written totals/reusing counters are explicit. Working layouts still need physical tape/pawn rehearsal.
- Optional-place problems change the all-place theorem's scope; grades 2–3 P7 is expressly limited to the preceding no-square maps before P8.

No blocker remains for this guide's reviser stage. Packaging, integration, classroom piloting and physical rehearsal remain outstanding.
