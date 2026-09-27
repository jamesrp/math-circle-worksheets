# AD2 maker PDF review

Date: 2026-09-26. Author: expand_ad1. Mathematical/design review is independently closed in `review-ad2-design.md`; this is the separate maker production pass. Independent PDF review remains required. Activities are not classroom-piloted.

Current preview: `tmp/pdfs/atlas-remaining/ad2-preview-r4/`.

- Student: `atlas-ad2-student-worksheets.pdf`, 26 pages (contents plus 25 investigation pages), SHA-256 `ee798c22c0197a5c1d85ecc63b876ccb9d0361bfe262ea7c1994087b507b28f9`.
- Guide: `atlas-ad2-facilitator-guide.pdf`, 36 pages including contents, SHA-256 `9a493e822cd74385de6d320ea3d5023c2c86906fd3231ec786df0179d7051b33`.
- Eight families AD-09–16; 49 student prompts printed exactly once; eight answered guide extensions. Complete prompts are read from the approved data through `common.question`.
- Exact author checker and independent design-review checker both pass. Build reports show no blank pages, out-of-page text or suspect glyphs. All 62 final pages rendered at 100 dpi.

## Actual inspection coverage

Every student page 1–26 was inspected individually at full size in r1. The changed student pages 18,20,21,25 were individually reread in fresh r2; page 8 was individually reread in fresh r4. Every r2 student PNG is byte-identical to r3; r4 changes only page 8. Thus every current student page is covered by a full-size inspection, without pretending unchanged pages received a separate redundant pass.

Every guide page was inspected on r1 contacts (all 37 pages), then every page of the final 36-page layout on all four r3 contact sheets. Full-size guide coverage in final page numbering: 1,4,7,8,9,11,12,15,16,17,18,20,21,22,23,25,26,27,29,30,31,33,34,35,36. Earlier full-size reads through page18 used r1 PNGs: those body pages are byte-identical in r3. Later listed pages were viewed directly from r3. Every guide PNG is byte-identical between r3 and r4.

## Family-specific diagram and use checks

- AD-09: both numbered clock faces have the correct cycles; no initial answer is marked. The candidate matrix includes all 4×6 pairs with axes matching `(a,b)`. Repair and general-solver ledgers have no answer-count rows.
- AD-10: counters can be arranged or drawn freely. Forward and reverse machines are supplied in the staged text; the iteration ledger does not suggest how many steps reach the threshold. The guide retains positive-integer descent and its base case before claiming completeness.
- AD-11: four visible coefficient cards agree with the definitions. The two blank product tables are separate and contain only headers, so inverses and collisions remain discoveries. Distinct input reports, constant affine machines and the rule-A failure are fully keyed.
- AD-12: the actual unit segment can be copied using a compass. The semicircle uses diameter parts in ratio 1:√2, a perpendicular at their junction and an unknown height; it supplies a legal square-root scaffold, not a purported cube-root construction. Positive-volume and degree-theorem gates remain explicit.
- AD-13: initial corner crosses are at (3,0),(2,1),(1,3),(0,4); the axes continue beyond the drawing. Student plots have no survivor shading. The guide's two worked grids show eight original survivors and the two freed positions after moving (2,1) right; the common-kernel monomials agree with the diagram and exact check.
- AD-14: the flow now includes every arithmetic stage: z, z², z²+1, z−2, and their final product. Every node has blank ordinary/ε coefficient cells. Arrows follow the exact dependencies and neither 16 nor the derivative rule appears before the intended later stage.
- AD-15: both drawings use equal coordinate scale and y-semiaxis 1/√2. Only B is marked, with its exact coordinate in the introduction; no solution secants or second intersections appear. The exceptional point/infinite slope and cubic counterexample remain visible tasks.
- AD-16: residue plots have exactly five coordinate labels each way and no smooth curve. No affine-point count or nine-slot orbit appears prematurely. Projective normalization, nonsingularity and tangent-formula hypotheses are supplied at the correct stage. The final four equation panels correspond to four explicitly requested equations, not to a hidden solution count.

## Maker repairs and final identity

The initial build caught the metadata string `ad 2`; it is corrected to `ad2`, and status now accurately records design closure. Mathematical prompts, solutions and instances were unchanged during rendering.

R1→r2 changed only student pages18,20,21,25: added the explicit square node, removed a conic-label collision, and widened the orbit column. All 37 guide PNGs were unchanged. R2→r3 left all 26 student pages identical and moved the worked staircase certificate onto the page holding its proof, reducing the guide from37 to36 pages; final guide contents and the affected guide pages were inspected. R3→r4 changed only student8 to print the four supplied coefficient cards above the tables; all other61 PNGs are byte-identical. The new page was inspected full size and fits cleanly.

No shared helpers, closed batch inputs, original atlas cards, prior-ten outputs or final combined books were edited. No additional artifact marker was run.

## Independent-review repair, r5

The reviewer found one overly broad sentence in the custom guide22 caption. It now says that among monomials whose shifted images survive, those images are distinct. This correctly allows zero images while preserving the no-cancellation proof. The main key was unchanged. Fresh preview is `tmp/pdfs/atlas-remaining/ad2-preview-r5/`; maker reread guide22 full size. PNG comparison: only guide22 changed; the other61 pages are byte-identical to r4. Counts and mechanical checks remain26/36 and zero issues. Student hash remains `ee798c22c0197a5c1d85ecc63b876ccb9d0361bfe262ea7c1994087b507b28f9`. Guide hash: `193aa2d05a07b213b95df368378d32166df13be3f81affee1cc24eae3b47906a`. Awaiting reviewer closure.
