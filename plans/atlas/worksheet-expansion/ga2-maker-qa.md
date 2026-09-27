# GA2 maker PDF review

September 26, 2026. Maker review is complete with no open findings. Independent mathematical/design review is closed in `review-ga2-design.md`. Independent PDF review remains a separate release gate. The activities remain unpiloted.

## Current preview and identity

Current preview: `tmp/pdfs/atlas-remaining/ga2-preview-v2/`.

- `atlas-ga2-student-worksheets.pdf`: 26 pages, including contents and all 25 planned student pages. SHA-256 `ff4b65036d64eb38c047387b4cbee33326950ffabc145692a6dea5fede92e437`.
- `atlas-ga2-facilitator-guide.pdf`: 39 pages, including contents. SHA-256 `2d6e80b3dbbae6c9c4b9d50ab8dd8cf26650da534df8baed228f9b28eccba586`.
- Every page has a rendered PNG, extracted text, contact-sheet placement and bounds/glyph report under `qa/`.

The renderer is `lowell-math-circle-year-2/source/atlas-remaining/ga2.py`; it uses `common.start` and `common.question` for every task. All 50 prompts print exactly once and have full keys and hints. All eight guide extensions have solutions. The one custom guide figure page, page 34, contains the worked two-window and three-window convolution graphs.

Current source/check SHA-256 values:

| File | SHA-256 |
|---|---|
| ga2-data.json | `ac5b5b7963111e7cdb73f20601283f01b8f4a826a3da0bcdd32d593a69207696` |
| ga2.py | `11150480232fe6e1cf9832f1bc4e94e7a4a5f4eae706ddc26aac683aa52fb87d` |
| ga2-checks.py | `8c10a3c929726d09cfb4301440ce82ade9f838f078c0b295ee97b1265e1f4724` |
| ga2-checks-results.json | `baaf69a003a35b7545ec5539de77bc638e6355df4e768917a3cfda832b12c3d6` |

Only the non-rendered batch status was updated after the current build; checks were rerun and their data hash refreshed. No rendered mathematical or pedagogical field changed after v2.

## Actual visual coverage

Every student page 1–26 was inspected at full size in `ga2-preview`. The three repaired student pages 3, 14 and 22 were inspected again at full size in the fresh `ga2-preview-v2` path. Byte comparison of all student PNGs confirms these alone changed. Thus every final student page has full-size inspection coverage, with unchanged pages established by byte identity.

Every guide page 1–39 was inspected on five contact sheets. Comparing all 39 guide PNGs between the first preview and v2 found only page 32 changed; it was inspected again full size. Additional full-size inspection of the current v2 guide covered pages 1, 3, 5, 10, 14, 17, 18, 22, 23, 26, 27, 28, 31, 32, 34, 35, 38 and 39. These include dense derivations, general proof/equality conditions, exact finite-cycle counts, all worked figures, convolution joins, compatibility/sensitivity and source-scope caveats.

Apparent heading collisions on guide 22 and 31 in the multi-image viewer were checked against actual saved bounds and fresh image paths/crops. Headings end at y=118.9 and subsequent text starts at y=125.9; the current image crop visibly confirms the 7-point separation. No shared layout changes were made based on stale or misleading viewer presentation. Brief source-only continuation pages 6, 24 and 29 are intentional and readable, not blank pages.

## Diagram and task fidelity

- GA-09: whole-line sliding profiles and fixed-end axes are distinct; the learner's later curves are blank. Partial-derivative verification is required in the printed gate and tasks. Boundary/initial-value verification now has an explicit work area.
- GA-10: the tent graph has the correct peak and two half-interval conventions. Inverse cards supply legal operations without a precomputed orbit. Cycle inventory uses open workspace, with no three-cycle count cue.
- GA-12: harmonic cards are ungrouped, geometric strips use the correct payment convention, and budgets are learner choices. No finite drawing is presented as the infinite proof.
- GA-13: supplied parabola has no best line or alternating extrema printed on it. Learners can draw candidates and record challenges. The last proof area explicitly serves both general-interval questions.
- GA-14: dials and observation records leave arrows/heights for the learner. Neither the successful extra time nor the final alias classes appear prematurely. Full-arrow observations and height observations remain separate.
- GA-15: sign cards include symbols, fixed coordinate order and correct row/column patterns. The weighted-sum and target records are usable; no worked coefficients appear in student figures. The two-detector ambiguity has open workspace.
- GA-16: the two physical interval strips share a scale; the moving right endpoint is t. Blank graph axes do not mark the true breakpoints. The inverse task defines the first-to-last contact distance. The guide-only trapezoid and piecewise quadratic graphs match the exact formulas and continuity claims.
- GA-17: supplied forcing graphs show x² and 2x−1 correctly; shifted solution graphs remain for the learner. The critical dial, compatibility and sensitivity proofs retain definite integrals as a core prerequisite.

## Maker repairs

1. Student page 3: added a dedicated 60-point verification area after the fixed-end graph for the wave law, boundary conditions and initial data.
2. Student page 14: labeled the shared proof area for tasks 5–6, including the general certificate, endpoint secant and whole residual range.
3. Student page 22 / guide page 32: replaced undefined “positive support width S” with the explicit distance S>0 between first and last contact positions. Root confirmed this preserves the reviewed mathematics and improves the task's meaning.

Between the initial build and v2, these are the only four changed PNGs out of 65. All repairs were inspected under a fresh output path.

## Validation and limits

Both current books report zero blank pages, out-of-page text characters and suspect glyphs. Family IDs, prompt IDs, exact-once coverage, complete keys, planned page counts and contents pagination all pass. Student family starts are 2, 5, 9, 12, 15, 18, 21 and 24; guide starts are 2, 7, 12, 16, 20, 25, 30 and 36.

`ga2-checks.py` passes all eight mathematical groups and schema/printed-key checks: 2,046 exact tent-map programs; strict harmonic/geometric certificates; exact minimax extrema; alias congruences; 625 Walsh arrays and their translations; exact window overlaps and the third-convolution joins; PDE mode identities; and rank-one feedback and sensitivity identities. These finite checks supplement the general proofs in the key; their individual scope is explicit in the results file. Root separately solved every prompt and extension and reviewed all sources and check code.

The proposed pacing and classroom engagement are unpiloted. Original atlas files, the accepted ten trials, other closed batch inputs and shared layout helpers remain unchanged. This author has not written the final combined books. No extra artifact marker was run. The current previews are ready for the assigned independent PDF reviewer.
