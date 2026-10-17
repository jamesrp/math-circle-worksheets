# Week 91 independent final review

Verdict: PASS for the complete 23-page instructional set. No substantive mathematical, task/solution alignment, or rendered-layout defect requiring a content revision was found. Preserve the upper investigations.

Reviewed read-only in the canonical-repository worktree, branch codex/weeks-85-91, origin git@github.com:jamesrp/math-circle-worksheets.git. All generated review artifacts and the clean copied-source build are outside the repository in this review directory.

## Exact final PDF coverage

Rendered at 90 dpi and individually opened/inspected, including the complete page areas:

- week-91-students.pdf: pages 1, 2, 3, 4, 5, 6 (six pages).
- week-91-return-visit.pdf: pages 1, 2, 3, 4 (four pages).
- week-91-materials.pdf: pages 1, 2, 3, 4, 5, 6, 7 (seven pages).
- week-91-facilitator.pdf: pages 1, 2, 3, 4, 5, 6 (six pages).

No clipped content, overlapping text, missing arrows, mismatched endpoints, broken glyphs, or footer intrusion was found. Materials pages 2–5 are landscape Letter; all other pages are portrait Letter. Student tasks have consecutive numbering (1–7 and 1–6 within their respective packets), consistent headers/footers, concise shared rules, and appropriate diagrams and records.

## Mathematics and task/guide alignment

All student P1–P7 and return P1–P6 have aligned answers and explanations in the guide. Manually checked the guide's pairing and recursive bundle arguments, inverse-order examples, coin support comparison, conservation proof, termination proof, and optional random-walk background argument.

The tree result assumes a complete downward binary tree, one completed counter per launch, next-departure arrows followed then flipped, and persistence between launches. The guide states the unequal-depth/reset limits. Every consecutive full-size block has one exit per leaf and restores the cards; the proof covers arbitrary block-start cards.

Students p4/P4 target AEBFCGDH alternates root halves but forces left-subtree sequence ABCD and right-subtree sequence EFGH, each violating the next-level switch alternation. Guide p4/P5 extra AEDFBGCH has legal left sequence ADBC and illegal right sequence EFGH. Both are genuinely deeper obstructions than a root-half failure, and the guide's stated explanation is correct.

For the path, m is the number of edges, both endpoints absorb, 1 <= s < m is fixed for the block, and every interior switch alternates. During a walk x + S is conserved, where S counts next-right arrows. Telescoping gives mR + S_final = ns + S_initial. At n=m, m(R-s) lies strictly between -m and m, so it is zero. This proves the s-right-per-m claim from every initial state, without burn-in, and at every consecutive block boundary. It does not prove full-state recurrence. The LLR -> RLL -> RLL example with exit blocks 0004 correctly exhibits failure of immediate state return; the packet does not claim persistent changes at all later block boundaries. Finite-path termination is proved independently by propagation of infinite visits toward an absorbing endpoint, so the conservation argument does not assume unproved completion.

Separate reviewer-written enumeration (no imported package verifier) checked all tree states at depths 1, 2, 3 (2, 8, 128), all words unique, full-block balance and exact state restoration, both named deep impossibility witnesses, and all path starts/entries for m=2 through 8 (1,538 cases, three m-blocks each, every sliding m-window and every single-step invariant). All passed; summary in independent-checks.json. The packaged broader verifier also passed during the clean build.

## Materials and operating guidance

Seven paired tree cards and four paired road cards per kit agree with the largest printed apparatus. Printed face dimensions agree with guide p2: tree 18 x 22 mm, road 20 x 20 mm; strips are 15 mm squares; scale bar 50 mm. Guide's three-kit totals correctly multiply the per-kit amounts: 48 counters, 21 tree cards, 12 road cards, three entry markers and three coins. Materials p7 supplies three markers per print; these are harmless extras rather than a shortage. Sixteen counters suffice for each described trial when new trials clear exits as the launch specifies.

Folding paired faces on the vertical middle produces upright NEXT labels when flipped side-to-side. Landscape board labels and branches are clear. Tree card corners slightly overhang the 24 mm switch circles (28.43 mm diagonal); the 20 mm road cards have 28.28 mm diagonals, a slight corner overhang on the 28 mm circles of the five-edge road. No printed instruction requires the rectangle to be contained in the circle; diagrams have sufficient surrounding separation, and the counter is explicitly placed beside the card. This is not a digital defect. Physical printing, cutting, flipping, counter placement, exit-pile handling, and timing remain untested, as stated in the guide and README.

Guide p2 gives concrete whole-group handling and follow/flip demonstration, a complete short-road revisit demonstration, route-specific printing, one kit per pair/trio, adults' roles, and separate resources/staffing for an optional K–1 station. It does not imply an independent K–1 packet. README and guide make multi-visit/readiness boundaries clear. Advanced invariant and termination tasks are optional continuations following two concrete road investigations; no removal or flattening of that substance is justified by this review.

## Source/rebuild and release follow-up

Copied the entire Week 91 source directory to clean-source/ and ran its documented builder with out and work paths in this review directory. Build passed its finite checker, generated-TeX snapshot comparisons, twice-compiled TeX outputs, and overfull-box checks. All four rebuilt PDF SHA-256 values equal the actual reviewed PDFs byte for byte; see rebuild-comparison.json. Thus the reconstructed bytes need no separate visual interpretation.

At review time, source README refers to QA.md, but QA.md is not yet present; reference-pdfs/ is empty, and there is no portable source ZIP in the final Week 91 output directory. These are release-assembly follow-ups for the lead, not PDF content blockers: populate the promised QA/reference outputs, make the portable ZIP, then perform the required extracted-ZIP build and equality check. This reviewer has checked a clean copied source build, not an as-yet-uncreated ZIP extraction. No claim of remote synchronization or classroom piloting is made.

Primary-paper attribution was read in SOURCES.md and the guide but not independently re-audited against the external papers in this final pass; the lead's documented production source check remains the source evidence. All elementary claims used by these tasks were independently checked directly as above.
