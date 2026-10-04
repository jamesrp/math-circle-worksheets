# Week 53 fresh revision record

Revision stage only, October 4, 2026. Read the complete writer brief, revision prompt, fresh adversarial review and independent mathematics review, plus the independent audit script/output/geometry evidence. The routing instruction authorizes one combined packet. No facilitator guide, prior content, global index, workflow prompt or remote copy was edited.

## Deliverables and scope

- `students.pdf`: nine US Letter pages, Problems 1–9. Grades 2–5 on pp. 1–4; Grades 4–5 on pp. 5–9. Current review-copy footer id: `W53-networks-v1`.
- `src/`: ten lean original editable files; LaTeX student wording, JSON graph assets, Python diagram builder/compiler/verifiers, README and mathematical/design/provenance notes. The graph geometry and prices are unchanged. No workflow prompts, borrowed exemplar blocks, books, renders, reference PDFs or compiler intermediates are included.
- Build from any copied/extracted source folder with `python3 build.py --output .`, or choose a different writable output directory. The source README lists all TeX/Python dependencies.

Final PDF SHA-256: `253ea85b36d1c6e5fe53e956e26d8254f9befb36281e16f928e6a42db6b0ac09`.

## Review responses

| Review finding | Revision and check |
|---|---|
| F1 / M1, required P8 precision | Replaced “get stuck above” with an open question asking whether a connected purchase without a loop can cost more than the cheapest while no one-link swap makes it cheaper. The one-link swap convention requires the result to connect every place. Retained the positive-price loop question and both concrete purchases. No theorem answer, certificate or search algorithm is printed. |
| F2 / M2, P7 price domain | Now says “Give each link a price of 1, 2, 3 or 4.” Six independently chosen labels permit repetition; no all-values requirement was added. |
| F3 / M3, P5 fixed state/connectivity | Now starts “Starting each time from the printed thick purchase” and requires the result to connect every place. Buying one unused link precedes returning one bought link. The original non-task U/V/W buy-first visual remains, with 6 → 9 → 5 costs. |
| F4 / M4, source spacing | Corrected the main-map minimum to 51.0 mm (p. 6) and p. 8 nearest centers to 37.5 mm. Actual vector measurements are 51.00055 and 37.50047 mm. |

Source notes now record the exact lower-P8 exchange list, the full inverse-price multiplicity count, and the distinction that CD=2 is forced by price rather than by being a graph bridge. They retain assumptions, loop removal, exchange-certificate sufficiency and distinct-price uniqueness proofs; finite tests are distinguished from the arbitrary-map arguments.

## Final mathematical verification

The fresh math reviewer's independent script was rerun against the actual final PDF, without importing writer data, diagram code or verifiers. It reconstructs **all 27 printed graph instances**, including unpriced compact records and both inverse maps' six blank price fields. It checks endpoints, site labels, price numerals/dots and thick purchase membership. All pass. Every fixed weighted graph was independently re-enumerated by connected subsets, spanning trees, legal improving exchanges and path certificates: **152 spanning trees across ten fixed weighted graph types**. The original source verifiers also pass; these are additional evidence, not the only check.

The six-place map retains CD=2, BD=5 and CE=6, and has no graph bridges. Its unique optimum costs 8 and uses AB/BC/CD/DE/EF. The lower P8 cost-14 tree has exactly four improving swaps: **AC→BC (13), AC→CD (13), BD→CD (11), DF→EF (12)**. The top purchase has none. P5's cost-10 input has AC→BC (7), AC→CD (8), AD→CD (9), while its cost-6 input has none. Arithmetic-cheaper AD→BC is excluded because it disconnects D.

All **4,096** inverse-price assignments were independently checked: **1,956 unique** and **2,140 multiple**. Multiplicities/assignment counts are 1:1956, 2:936, 3:768, 4:144, 5:96, 6:96, 8:72, 9:24, 16:4. Positive prices and final connectivity are preserved throughout. Actual final text checks verify the modified P5/P7/P8 prompts, positivity, all grade headers, footer ids and page numbers.

Evidence outside the lean source: `../revision-qa/independent-checks.json`, `independent-output.txt`, `source-math-checks.json`, `final-pdf-checks.json`, `final-text.txt` and `source-inventory.json`.

## Rendered coverage

Every final page was rendered at 108 dpi and visually inspected by the reviser. Headers, footer ids, page numbering, all graphs/prices/purchases, circle geometry, records and workspace pass. No clipping or unwanted overlap was found.

| Page | Status | Graph instances | Specific coverage |
|---|---|---:|---|
| 1 | Already sufficient; final render checked | 5 | Shared X/Y/Z input, paid intermediate (2+4=6) and kept connected record precede P1. Two triangles, dot counts, prices and record memberships are correct. |
| 2 | Already sufficient; final render checked | 4 | Four-place map and three compact records retain AB/BC/AC/CD/AD; prices 1/1/1/2/3 are legible and dot counts match. |
| 3 | Already sufficient; final render checked | 3 | Four-place greedy-trap map and two compact records retain all five links with prices 1/2/3/4/5; workspace is clear. |
| 4 | Already sufficient; final render checked | 4 | Five-place weighted map and three records preserve all eight links; all prices and endpoints remain separate. |
| 5 | Changed student prompt | 5 | Fixed-reference and resulting-connectivity wording is present. U/V/W buy-first worked visual retains costs 6→9→5; two unchanged printed purchases and tables are clear. |
| 6 | Already sufficient; final render checked | 1 | All nine links appear. CD=2 is visibly C-to-D, BD=5 bypasses C, CE=6 bypasses D; no unintended junction is marked. Classification space is clear. |
| 7 | Changed student prompt | 2 | Allowed prices 1,2,3,4 are explicit. Each K4 has all six blank price fields and enough drawing/reasoning space. |
| 8 | Changed student prompt | 2 | Positive-cost loop question and explicit no-cheaper-one-link-swap condition are present. Upper cost-8 and lower cost-14 trees retain all nine available links; CD=2 and bypass links remain visible. |
| 9 | Already sufficient; final render checked | 1 | Distinct labels 1–6 are correct; crossing has no circle and no junction. Square uses equal axis scaling; diagonal prices remain separated. |

All pages also receive the consistent current footer id. Source-only spacing corrections are not counted as student-example changes. Page images and the per-page inspection record are in `../revision-qa/render/` and `visual-inspection.json`.

## Clean rebuild verification and limits

A clean standalone source copy and a separate ZIP extraction were built with the documented `python3 build.py --output .` command from their own source folders. Fresh PyMuPDF comparisons, independent of the authored comparison helper, confirm identical extracted text, Letter dimensions and exact **144 dpi pixel arrays on all nine pages**, for both rebuilds. `../revision-qa/clean-rebuild-checks.json` records commands and per-page hashes; the tested lean ZIP is `../revision-qa/clean-source.zip`. Root can package the same `src/` inventory for release. Final build intermediates remain in `.build/`, outside `src/`.

This is an **unpiloted review copy**. Exact pawn/marker fit, clutter, payment/refund handling, preparation/timing, volunteer operation and classroom suitability remain untested. Source age guidance does not validate the younger adaptation; supported younger access and general proofs are readiness-dependent proposals. No public or remote version is claimed current. Later separate guide authoring/review and organizer review remain outside this student revision stage.


Record note: this is the completed authored stage report. Stage-local render/build
evidence referenced under `tmp/` is historical and is not included in source ZIPs.
Current released-file hashes and actual ZIP-extraction text/dimension/pixel checks
are recorded in `../release-checks.json`; coordinator page coverage is recorded
in `../../final-visual-review.json`. Physical pretests and piloting remain unperformed.
