# Week 76 adult guide verification

## Deliverables

- `final/facilitator.pdf`: four US Letter pages, 189,840 bytes, footer identifier F76-FAC-v1.
- `final/guide-src/`: exactly `facilitator.tex`, `build.py`, `check_math.py`, and `README.md`.
- Final PDF SHA-256: `e5094cf9256fa6da6b9dcc416fae260b2c65f3b7a7d3b7521582263e5e4c7393`.

## Scope and authored conclusions

The guide was written only after reading the final student PDF and inspecting all four rendered student pages. The prompt's single-packet prototype addendum controls: one Grades 3–5 packet, no invented K–1 route. The main route uses the existing three-child grades 4–5 table and its organizer; an optional two-pair third-grade route retains its own mathematician. The K–1 adult stays anchored with a separately chosen activity.

The guide opens with the actual substitution fixed point, pair invariant, four local bans, five-tile synchronization, and exact failure of eventual periodicity before preparation, timing or individual answers. It distinguishes whole generated rows from crops, necessary local tests from global membership, finite checks from proof, and adult proof support from children's own explanations. Problems 1–4 are the proposed core; 5–6 are further work, and 7 may be a return visit. Each problem has a complete solution, ordered hints, and an appropriate stopping route. Material and print counts include spares. No classroom outcome is claimed.

The important final-instance distinction is explicit: ABBAABBA is a genuine crop but not a complete generation from A. Its appearance in Problems 3 and 4 is consistent. The second forged periodic strip is ruled out with the finite ten-tile certificate ABBAABBAAB, whose forced decoding gives forbidden ABABA. Neither a clipped edge nor failure to decode a crop all the way to A is used as a rejection.

## Mathematical verification

`check_math.py` was written independently from transcriptions of final student examples; the student checker and review answers were not used as an answer source. It checks the printed convention examples, generated row and all six triples, all four whole-row decoding histories, every admissible left/right lone-tile choice for the four crops, finite forged-strip certificates, and the optional fallback's single-tile modifications. The script also checks the material and printing arithmetic.

For positive and negative crop membership, the checker computes the exact bounded factor language through length 10 by substitution closure, rather than treating absence in a long sampled prefix as proof. The parent-cover argument behind this bounded closure is documented in the script. All twelve genuine length-five factors have exactly one immediate pairing. The infinite theorem is proved analytically in the guide with an odd-period seam contradiction and even-period halving; it is not attributed to the finite computation.

The owned research note was consulted for scope and provenance. Swan, Offner and Allouche–Shallit's author-hosted URLs were opened to check the reference lineage. The guide and README give human-readable URLs. No reference PDFs or borrowed artwork are packaged.

## Build and visual checks

- PDF authoring marker ran successfully once before authoring.
- Both the original source build and a ZIP-extracted standalone source build passed the checker and two pdfLaTeX runs. The builder fails on overfull boxes; none were reported.
- The package was extracted without sibling student sources or workflow prompts. It builds using only its four authored files, Python standard library and the documented TeX packages. The minimal host's external TEXMF/TEXFORMATS setup was supplied through environment variables; it is not bundled or hard-coded.
- Every final guide page was rendered at 120 dpi with Poppler and visually inspected. Text, formulas, table, header/footer and page transitions are readable, with no clipping or overlaps.
- Every page of the standalone rebuild produced a PNG byte-identical to the corresponding final guide page.
- Source package contains no fonts, runtime format dumps, third-party papers, raw tool output, stage prompts or original-machine paths.

## Unchanged student inputs and remaining limits

The final student PDF remains SHA-256 `58da69e16b1c4f3b5cf637a655efd340939c107cde8176baf6c2a768416d928a`. All four files under `final/src/` were checked against their initial hashes and remain unchanged.

Physical rehearsal and classroom piloting are unperformed. The guide calls for a real-material rehearsal before use. Independent guide review and publication belong to the coordinator; this stage made no commits or pushes and did not edit student pages or run another workflow stage.
