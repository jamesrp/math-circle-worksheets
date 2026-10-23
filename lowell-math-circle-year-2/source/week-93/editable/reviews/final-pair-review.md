# Week 93 independent final-pair review

Date: 2026-10-17. Reviewer: fresh `final_pair93` agent, not the writer or reviser. Review-only: no activity source/PDF edits, delegation, commits, or pushes.

## Verdict

**PASS for digital mathematical and visual review of the final corrected pair.** All seven student problems were independently solved; all ten PDF pages were rendered and inspected. No unresolved mathematical, layout, or preparation blocker was found. One minor guide answer-scope clarification was identified and corrected by the coordinator during review; the corrected guide was checked separately. This is not evidence of physical readiness or classroom success: **physical rehearsal untested; all pages unpiloted**.

Final reviewed identities:

- Student PDF: `pdfs/week-93-students.pdf`, SHA-256 `9478fffa7d62bd3f8b0c1a36ddb4b2f815b644d678fe80a0164dab67a8dc6158`.
- Corrected facilitator PDF: `analysis-family/lowell-math-circle-year-2/week-93/week-93-facilitator.pdf` in the coordinator checkout, SHA-256 `4cebc5f351ddb3d76bc4636819a35e4094e0c00fea17af17e2ee694416948d56`.
- The guide snapshot originally supplied here has SHA-256 `7578ff201350fbc06ddc67e39c060dbb844fbcefe1ca8102458c1dc59dee14bf`; it is superseded by the corrected hash above. It was left untouched as review evidence. Final verdict must not be attached to that older hash without noting the resolved clarification.

## Page-level coverage

| PDF/page | Mathematics and task coverage | Visual and practical result |
|---|---|---|
| Student 1 | P1 independently enumerated all whole-tile rectangles of area 24: 1x24, 2x12, 3x8, 4x6. 4x6 minimizes side difference and ratio. Completeness follows because smaller integral side cannot reach 5. | Header/footer consistent. All 24 columns and 20 rows fit; grid is 168x140 mm, hence 7 mm cells. Enough space to draw all four arrangements. Guide correctly says build commercial tiles on table, not on this grid. |
| Student 2 | P2A has a 2x2 missing square after fitting 4x2 and 2x2 pieces; P2B has a 1x1 missing square after fitting 3x2 and rotated 2x1 pieces. Independent cell sets check full piece area, containment, disjointness and square-shaped complement. | Four clear four-sided shapes with matching A/B labels. Actual vector dimensions match 90x30, 60x60, 60x30 and 45x45 mm within .003 mm. Both axes use 15 mm/unit. Labels lie outside cutouts. |
| Student 3 | Complete non-task example: 1x3 -> combined 1+3 -> average 2 -> full 2 by 3/2 rectangle, area 3. P3 updates give [3,4], [4,9/2], [10/3,6], the tightest pairs among the four marked lengths. | Input, intermediate and output are visible and labeled consistently; output really shows both side lengths and area. Rectangles have correct proportions (30x10 and 20x15 mm). Three separate 0–10 number lines fit their endpoint and fraction tasks. Exact fractions versus placement estimates are distinguished. |
| Student 4 | P4 order B,D,A,C; products all 12; widths 4,1,1/14,1/2716. P5 valid bracket 3.46<s<3.47; neither endpoint is exact. Finer endpoints 3.455 and 3.465 also satisfy literal task. | Four distinct 70x20 mm cards, readable fractions, cutting space, and retained original for responses. P4 and P5 have usable answer space. No false scale claim for cards. |
| Student 5 | P6 extra area ((b-a)/2)^2, equality exactly for squares. P7 arbitrary narrowing and finite nonattainment from every positive unequal rectangle follow from gap rule. | Readiness gate explicit. Conceptual rectangle and square are legible, square has equal scaling, and “not to scale” is conspicuous. Both problems have drawing/argument room. |
| Guide 1 | Theorem-first overview checked: positivity, nested enclosure, area invariant, strict unequal case, missing-square identity, geometric contraction, finite nonattainment, fixed squares, and readiness map. | All formulas render, no clipping or collisions. Overview precedes individual solutions. Experiments, explanations and general proof are separated. |
| Guide 2 | Every student-page reference checked. Materials, duplicate pages 2 and 4, grid purpose, exact scale, complete worked update, adult staffing, and 55-minute first route consistent with packet. | Readable paragraphs and practical instructions. Fractions do not imply precision cutting; deferred pages and untested physical fit/timings are explicit. No forced K–1 use. |
| Guide 3 | P1–P3 answer checks match independent results. P2 construction proves shape as well as area. P3 bounds are explicitly limited to marked old/new lengths. | Table and formulas clear; optional hints kept with adults. |
| Guide 4, corrected | P4 exact fractions and width checked. P5 now explicitly accepts finer decimal endpoints and restricts unique hundredth-grid pair to multiples of .01. P6 full general dissection and P7 proof checked. | Corrected page rendered and visually reinspected; added wording fits cleanly. No text overlap or footer intrusion. |
| Guide 5 | Area-36 return example gives 72/13 and 13/2; unequal even though target side is 6. Newton specialization and limits correct. Citation details and pedigree/readiness disclaimers checked. | URL and formulas legible. Physical rehearsal and piloting still marked untested. Final guide pages 1,2,3,5 are pixel-identical to the fully inspected initial guide at the same render resolution. |

All pages are US Letter (612x792 PDF points). Student numbering is consecutive 1–7. No name/date fields, redundant page titles, accidental solution scaffolding, missing glyphs, clipped text, or harmful diagram/label collisions were found. Task-specific proof requests in P4–P7 are central investigations, not mechanical optional prompts appended to every action.

## Independent proof checks and limits

Let 0<a<=b, A=ab, m=(a+b)/2, h=A/m. A positive square side s exists uniquely, and a<=s<=b follows by squaring positive quantities. Area is preserved since hm=A. The identity m²-A=(b-a)²/4 gives h<=s<=m; h>=a follows from 2b>=a+b, and m<=b is immediate. All interior comparisons become strict when a<b.

The general dissection works even for extreme aspect ratios. Put d=(b-a)/2; b=m+d and m=a+d. Cut the original into m-by-a and d-by-a pieces. The first occupies the bottom of the m-square; rotate the other into an a-by-d top strip. The remaining corner is d-by-d. Pieces lie within the target, meet only at boundaries and conserve all original area. At d=0 there is no nonzero strip or hole; the original is already the target square.

The new width is m-h=(b-a)²/[2(a+b)]. Positivity is essential: b-a<a+b requires a>0. For unequal positive sides this is strictly between 0 and half the old width. For n>=1, repeated widths are less than the initial width/2^n; the nested brackets therefore trap s with any prescribed positive tolerance. Positive width persists at every finite move, including rational and irrational target sides. A square stays fixed. Zero or negative sides are outside the setting and cannot inherit these claims. Near the limit, gap_new/gap_old² tends to 1/(4s)>0, which justifies the quadratic-improvement statement for fixed A>0.

The long-side update is b-(b²-A)/(2b)=(b+A/b)/2=m, exactly Newton’s formula for x²-A. Derivative-based theory is not required for the rectangle proof. No global guarantee for arbitrary functions follows.

The optional comparison return question also has a coherent destination: at fixed area A, width d determines a+b=sqrt(d²+4A), so the next width is d²/[2sqrt(d²+4A)], strictly increasing for d>0. Thus a smaller current width gives a smaller next width. The suggested tolerance investigation is feasible: increasingly elongated positive fixed-area starts can take arbitrarily many prescribed finite moves to narrow below a fixed tolerance.

## Resolved finding

The original guide P5 could be read as excluding correct solutions allowed by the student wording “two decimals one hundredth apart.” The pair 3.455,3.465 works: their squared values are 11.937025 and 12.006225. This was a scope clarification, not an error in the intended 3.46,3.47 certificate. The coordinator corrected guide page 4 to accept finer endpoints and limit its uniqueness statement to endpoints that are multiples of .01. The student task needed no alteration. The final corrected page passes review.

## Source and overlap checks

The guide’s specific attribution to Driscoll and Braun, *Fundamentals of Numerical Computation*, [section 4.3](https://fncbook.com/newton/), was checked against equations (4.3.2), (4.3.7), Definition 4.3.2 and the listed smoothness/simple-root/convergence assumptions. The guide accurately treats this as context and derives its positive-side guarantee independently.

The authorized original *Math Circle by the Bay* was SHA-256 verified against `RESOURCE-MANIFEST.tsv` (`84e0277cd94b1e501d153834b7123a72958f8c01b806e7bdfcca012a3191e427`). Printed viii–x/PDF 9–11 supports deep connected themes, manipulatives, independent problem-solving and variable pacing. It does not establish this worksheet’s age fit or classroom success, and the guide correctly says so. No private source was copied into review deliverables.

Actual existing facilitator PDFs for Weeks 20, 48 and 51 were inspected for the cited connection: discrete harmonic averaging, inner/outer area certificates, and guaranteed measurement intervals respectively. These connections are accurate. The broad corpus absence/novelty search and historical workflow provenance were not rerun in this narrow final-pair review; those remain coordinator records rather than newly established review facts.

## Check artifacts and reproducibility

- `independent-check.py`: directly implements definitions and occupancy checks; it does not import or run the supplied checker. Checks all printed arithmetic, 469 exact rational starting rectangles over five updates each (2,345 updates), squares, extreme aspect ratios, area-36 case, actual PDF dimensions, page counts and independent clean TeX builds.
- `independent-check-results.json`: original pair hashes, dimensions and arithmetic results.
- `corrected-guide-check.py` and `corrected-guide-check-results.json`: final corrected hash, unchanged-page pixel comparisons, changed-page coverage, and corrected guide clean build.
- `renders/`: every original PDF page plus corrected guide pages at 1.4x, and extracted text. Every original page was viewed; corrected page 4 was viewed and other corrected pages were verified pixel-identical.
- `independent-build/`: isolated copies and compiler logs. Both original PDFs rebuilt byte-identically; the final corrected guide also rebuilt byte-identically from its matching source using two direct pdfLaTeX passes. No overfull content was reported.

This assignment supplied loose sources rather than the final portable ZIP. I performed clean isolated builds of the supplied sources and matching corrected guide source, but did not claim a final source-ZIP extraction check; package assembly/extraction remains the coordinator’s verification responsibility. No physical printing, cutting, manipulative rehearsal, timing trial or classroom piloting occurred.
