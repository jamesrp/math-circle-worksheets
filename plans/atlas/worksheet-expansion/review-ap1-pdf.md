# Independent AP1 PDF review

Reviewer: GA1 author. September 25, 2026. PDF review is closed with no outstanding findings after fresh-path repair inspection.

## Files and actual coverage

Reviewed `tmp/pdfs/atlas-remaining/ap1-reviewed-preview/atlas-ap1-student-worksheets.pdf` (25 pages) and `atlas-ap1-facilitator-guide.pdf` (39 pages). Read the maker QA note, page data, exact keys and the closed independent design-review record for alignment. Author files were read-only; findings were sent to the author for repair.

Every student page **1–25** was inspected at full size, including the contents and all 24 investigation pages. Every guide page **1–39** was inspected on all five contact sheets. Guide pages **5, 8, 17, 18, 22, 23, 27, 28, 32, 33, 35, 36 and 38** received full-size inspection, including every worked figure and the dense probability, calculus and spring calculations.

Initial student hash: `1f8f039ae1ee15ebf289dcc229627cc0f45a34ab3b11ba436d87c17c67d7e3f4`.

Initial guide hash: `caa99357f79d95d74a8a7cc639fd80570e429cfb9aea861fa279e1daad3d1f83`.

## Findings sent for repair

1. **AP-04, student pages 9–10 and corresponding guide intros:** page 8 asks learners to invent their own World 1 and World 2, but the next page calls the fixed `1,1,1,1,5,5,5,5` population “the first world.” A learner's first world need not contain four 5s. Introduce this explicitly as a new supplied population, then continue with it.
2. **AP-06, student page 14:** the two blank nodes with arrows in both directions disclose the two-cycle before learners predict and prove distant iterates. Replace them with a neutral forward iteration record or empty construction area. The calculus, plot and key are correct.
3. **AP-05, guide page 17, prompt 3 solution:** the first shortest interval is printed and stored as `[−2,X+1]`; it must be `[X−2,X+1]`. The missing X destroys the claimed translation-invariant rule. This was confirmed directly in the JSON, not inferred from an image alone. The author reports repairing the expression and adding a direct printed-key consistency assertion to the exact checker.
4. **Answer-count scaffolds:** AP-10 student page 24 has exactly four boxes before the learner classifies the possible spring responses; AP-05 page 12 has exactly two candidate axes before the learner finds all shortest intervals. Replace these with an open trial area or a record that does not imply the final count. The editor independently raised the AP-10 issue. AP-10 page 25 may retain two boxes because its prompt explicitly requests two constructions. The author also elected to remove AP-03's ten preprinted complement-pair slots, avoiding a cue to the twenty-assignment total; the repaired page 5 must be included in closure inspection.

The author accepted these findings. No further issues were found in the full pass. Closure below must record fresh-path inspection rather than merely the author's report of repair.

## Per-family fidelity and usability

| Family | Student pages | Independent PDF observations |
| --- | --- | --- |
| AP-02 | 2–4 | Labeled counters preserve six equally weighted initial outcomes; the two 3×3 grids retain order and replacement. Tickets A, B1, B2 remain distinct. The guide's RR shading marks four A cells and one B cell, yielding 4/5, and other cells have the correct ordered colors. Blank student tables leave the posterior counts to the learner. |
| AP-03 | 5–7 | Six score cards agree with the supplied values; complement records keep each sum with its triple. The three-coin tree has exactly the eight legal one-per-pair histories and no numerical sums printed. One- versus two-sided reporting and the changed assignment law are stated explicitly. The neutral-workspace repair should preserve room for a complete organized list. |
| AP-04 | 8–10 | Hidden identifiers and learner-selected values are visible as different roles. The two-draw value grid and unfilled FULL/RESTRICTED distributions accommodate masses 1/4,1/2,1/4 versus a point mass. Equal 4+4 and unequal 2+6 blocks match the averaging/weighting questions. The fixed-population wording needs the repair above. |
| AP-05 | 11–13 | Five separate error strips preserve a fixed secret with moving intervals, and instructions require learners to label their chosen scales. Width is correctly distinguished from the number of integer dots. The ten error/coin cells support the exact half-coverage audit, while the impossible realized interval is explicit. The printed key typo and the two-row count cue require repair. |
| AP-06 | 14–16 | The cubic plot has the correct roots, sign, extrema and scale; exact arithmetic is required where a plot cannot decide the safeguard. The central-half acceptance rule and sign-bracket update are usable as written. The two update records are sufficiently detailed and blank. Calculus remains a visible core prerequisite. The supplied two-cycle graphic needs neutralization. |
| AP-08 | 17–19 | Both labeled outgoing transitions are supplied in the intentionally flawed test machine. Empty input and the start/YES convention are explicit. The three-room construction and pairwise-suffix table leave transitions and distinguishing words blank. The two-condition design space does not supply six states. In the guide, R cycles each row and B exchanges rows in both directions; only (0,0) accepts. Crossings are edges, not additional rooms. |
| AP-09 | 20–22 | Three springs, two masses, common positive direction and separate rest-coordinate scales match the force law. Neither modal shape is preprinted. The two-piece sum diagram records a decomposition, not a second physical copy of the mechanism. Static algebra and the calculus continuation are visibly separated. Full-size differentiation and nonreturn arguments agree with the two modal frequencies and initial data. |
| AP-10 | 23–25 | Series shows the massless connector; parallel shows common guided bars and only the total load, preserving the force/extension investigation. The guide drawings have the intended three-leaf series/parallel trees, correct stiffnesses 3,1/3,3/2,2/3 and extensions 2,18,4,9 under load 6. Its four-spring constructions each have stiffness 1. The recursive permitted class and resource count are explicit. Only the classification workspace count needs repair. |

The guide preserves the delayed hints and full proofs. In particular, its safeguards establish a shrinking bracket rather than unguarded Newton convergence; the normal-mode page distinguishes near-returns from exact recurrence; and the spring completeness argument covers the explicitly recursive class. The rendered source URLs and prerequisite lines are readable. No additional clipped label, missing required object, incorrect adjacency, crossing-created state, or overflow was found.

## Evidence and limits

The initial reports show zero blank pages, zero out-of-page text characters and zero suspect glyphs in both PDFs. The builder reports all 51 student prompts exactly once with complete corresponding keys. These mechanical results did not catch the missing X; direct reading of the actual guide did.

This is an independent PDF review, not a second complete design/source audit. The separate `review-ap1-design.md` records the independent solution review of all 51 prompts and eight extensions. The present pass independently checked each rendered mathematical object against its task and recalculated the principal values used by the worked diagrams. Classroom engagement and timing remain unpiloted. No claim is made about a later final assembled book until the editor verifies reviewed-body identity and the new contents.

## Repair closure

All findings are closed in `tmp/pdfs/atlas-remaining/ap1-final-review-fixes/`. I independently compared every page PNG against the initial reviewed preview. Only student pages **5, 9, 10, 12, 14 and 24**, and guide pages **8, 9, 10, 11, 13, 14 and 17** changed. All other 51 page PNGs, including both contents pages and all worked guide figures, are byte-identical to the pages reviewed above.

Every changed page was reopened at full size under the fresh path. The student spaces now leave the number/structure of solutions open: AP-03 uses an organized-pair area, AP-05 one shared offset scale, AP-06 a forward x0→x1→x2→x3 record, and AP-10 an open network-trial area. AP-04 explicitly introduces and then continues with the supplied population. The guide now prints `[X−2,X+1]` and its AP-03/AP-04 descriptions agree with the new student pages. AP-03's changed paragraph length repaginated its guide body across pages 8–11; all four pages were read full size with no stranded heading, clipping or missing content.

The final preview retains 25 student pages and 39 guide pages, with zero blank pages, out-of-page characters or suspect glyphs. I re-ran the updated exact checker with its result-file write captured in memory to keep author files read-only; it passed, including the new printed-interval assertion.

Current student SHA-256: `27906dd427dfcf4c5b6eecf5f43d2b640575893cb1c6b771c5a91477e1f16ed9`.

Current guide SHA-256: `b1298ca1cd7828fcd248b7fa48c39c99635dfa655502d3223442bee9bc63ebe3`.

**AP1 is approved for assembly from this repaired preview.** The final editor checks must still preserve the reviewed page bodies and verify the newly assembled contents.
