# Independent PDF review: GA1

Reviewer: AD1 author. September 25, 2026. This review is independent of the maker pass and follows `REVIEW-CONTRACT.md`. The mathematical design review is separately recorded in `review-ga1-design.md`.

## Preview and actual visual coverage

Initial review target: `tmp/pdfs/atlas-remaining/ga1-preview-v3/`.

- Student book: 26 pages, one contents page and all 25 investigation pages. Every page 1–26 was opened and inspected at full size at the rendered 100 dpi.
- Guide: 40 pages. Every page was inspected on all five contact sheets. Pages 1, 4, 10, 13, 15, 18, 22, 27, 28, 29, 32, 33, 34, 36, 37, 38, 39 and 40 were additionally inspected at full size. These cover contents, the shortest-word proof, exact ramp roots, infinite-cover sums/enumeration, root-continuity argument, network equations, complex branches and coordinates, polynomial recurrence/composition, and all dense calculus/extension material. This guide has no separate worked-diagram pages.

All 55 student prompt IDs occur exactly once and their rendered tracked strings match the current data exactly. The guide includes all corresponding solutions and hints and 13 optional extensions. Both v3 build reports record zero blank pages, out-of-page characters and suspect glyphs. These reports supplement the visual reading; they are not used as substitutes for it.

## Findings sent to the owner

1. **Student page 13, GA-04 prompt 6:** the workspace caption “Three legal roots / first return / explanation” reveals the cardinality while the prompt asks the learner to find all legal cube roots. Remove “Three”; “Legal roots / first return / explanation” preserves the useful workspace.
2. **Guide page 18, GA-04 prompt 3 solution:** the worksheet measures the running angle in degrees, but the proof introduces `exp(iθ(s)/2)` without changing units explicitly. State that θ is now measured in radians for this formula, or include the degree conversion. The continuity argument is correct; the representation needs an explicit angular convention.

No other mathematical fidelity, diagram, staging or page-layout findings were found in this PDF pass. Closure will be recorded after inspecting the owner's fresh repaired images and checking which page bodies changed.

## Per-family fidelity checks

- **GA-01, student pages 2–4:** room-fixed axes and reset faces agree with the stated quarter-turn cycles; the marks are tracked as outward directions. Blank word spaces do not impose the optimum length. The planar compass and half-turn line have correct 0/2 centers and room for the ±4 outputs. The guide's one/two-card case split covers all possibilities, and its nonparallel-direction argument tests full orientation.
- **GA-02, pages 5–7:** all heights 0,5,1,4,2,3 repeat correctly, including the seam ramp. Both separation brackets physically span three grid spacings at their respective scales. No equality positions are marked. The proof is deferred to page 6; discontinuous and straight-trail counterexamples remain separate from the continuous circle argument. Guide roots 4/7,8/5,7/3 and heights 20/7,13/5,2 agree with direct affine differences −4+7u, 3−5u, −2+6u.
- **GA-03, pages 8–10:** the point line and rational array carry the needed labels, while interval widths remain learner choices. Assigned cost is distinguished from union length; repeated rationals are allowed. The arbitrary-list rule and proof are visible, with the whole-interval lower bound openly supplied. The displayed sum/tail and enumeration formula are legible and correct; no small finite picture is claimed to prove the infinite result.
- **GA-04, pages 11–13:** both dials have correct degree positions, legality is explicitly doubling modulo one turn, and no root answer is drawn. Running-angle records support reversals and include two records for the two requested routes. The no-jump constraint persists through the continuation. The two minor disclosures/notation findings are listed above.
- **GA-05, pages 14–16:** squares visibly distinguish fixed boundary values from circle averages. The shortcut is a–c and does not run through b. The path and shortcut edge sets give 3,6,9 and 9/2,6,15/2 respectively; guide equations match those exact diagrams. Open design space allows failed attempts, and each-component boundary and finiteness conditions survive in the actual prompts. Uniqueness is proved by differences, not inferred as existence.
- **GA-06, pages 17–19:** two separately labeled Argand grids prevent the false picture of all of C² in one plane. Grid step and real/imaginary axes are explicit; the example coordinates fit. Branch classification, real slices, path constraint and coordinate substitution retain their genuine complex-algebra gates. Guide arithmetic, inverse formulas and nonzero-parameter restriction are clear; the disc condition is now correctly a supplied necessary condition.
- **GA-07, pages 20–22:** the printed unit-circle rays are at 0,60,90,120,180 degrees; cosine is the horizontal coordinate. No cubic coefficients are supplied in the working area. The recurrence, deceptive five-point fit and machine composition have enough space for distinct algebra and proof work. Guide formulas T2=2x²−1, T3=4x³−3x, and T6=32x⁶−48x⁴+18x²−1 match the tasks; the polynomial identity argument extends beyond the cosine interval for the stated reason.
- **GA-08, pages 23–26:** calculus is explicit in contents and on every page. Time/height axes are labeled with no answer curves. The learner chooses waiting time; two separate join-quotient areas preserve the essential differentiability check. The classification retains immediate departure, arbitrary finite waiting and forever zero. The positive-interval chain rule avoids dividing by zero, and the final negative-sign counterexample correctly distinguishes failure of a sufficient hypothesis from nonuniqueness.

## Release scope

The pages offer sufficient objects, rules and working areas for the proposed investigations. Type, headings, footers and mathematical symbols are readable; no actual current heading collisions or clipped diagrams were found. Source/solution material stays in the guide, while student staging is preserved. Prerequisites remain substantive rather than replaced by unrelated elementary tasks.

This pass checks the preview PDFs and the specific claims printed in them. It does not constitute a classroom pilot, print-device calibration, or a new visual review of later assembled books. The editor must verify assembled page-body identity and new contents. Initial v3 hashes are student `2c91085cc7c9d24fb468fea320443e4212f426bdac2d575d4b867d90e8ce1d26` and guide `c1ed949037e04f7f9d6316895fd99c6f52b2785f7090f2a4f447d994cb28872d`.

## Repair closure — approved preview

Both findings are closed in the fresh `tmp/pdfs/atlas-remaining/ga1-preview-v5/` build. I opened student page 13 and guide page 18 at full size under that new path. The workspace now says “Legal roots / first return / explanation,” and the guide correctly writes `exp(iπθ(s)/360)` with θ explicitly still in degrees. The revised formula has the intended half-angle argument in radians. Both pages remain readable and well spaced.

I independently compared SHA-256 hashes of every rendered PNG from v3 to v5. Exactly student page 13 and guide page 18 changed; the other 64 pages are byte-identical to the reviewed pages. Final counts remain 26 student pages and 40 guide pages, with zero reported blank pages, out-of-page characters or suspect glyphs.

Approved current PDF hashes:

- Student: `10ca7eb2a01f9cdd1f9802f59bc4c821127a1803e4f5a0346d708d0c172c9916`.
- Guide: `73a31aaf01177d1b5a0d6b9b51cff2e0c670bbca81028a59396e3034d719a5a3`.

GA1 independent PDF review is complete, with no open findings. This approval covers v5 page bodies and contents, subject to the editor's later assembly identity checks and the unpiloted limitations above.
