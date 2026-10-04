# Week 9 return visits: revision-stage record

Status: prepared, reviewed, and unpiloted. This revision stage delivers one
seven-page shared student companion, `return-visit.pdf`, packet ID `F09-RV-v1`.
The explicit return-visit brief overrides the workflow harness's generic
three-packet filenames. It contains exactly Problems 1, 2 and 3; the additional
pages remain workspace for those investigations. It is a menu for multiple
visits, with no one-hour completion requirement and no forced K-1 packet.

## Changes and final-page coverage

Both fresh reviewers passed the seven draft pages and their mathematics.
The one student-facing operational improvement has been adopted: page 6 now
opens, “For diagonal paths, move one square across and one square up or down each
step.” Pages 6-7 can therefore be selected independently of the Grades 4-5 loop
pages. The existing crossing convention visual remains before first use.
The final footer and optional PDF check both use `F09-RV-v1`.

| Final pages inspected | Genuine header band | Student change | Preserved substantial task |
|---|---|---|---|
| 1-3 | Grades 2-5 | Final footer; already sufficient otherwise | Find all ordered two-bounce wall words for both finishes; eight 4 by 4 boards per finish |
| 4-5 | Grades 4-5 | Final footer; already sufficient otherwise | Classify all 15 interior starts and find the first return to the starting dot with the original NE direction |
| 6 | Grades 2-5 | Explicit diagonal-step definition and final footer | Trace four contrasting boards, mark distinct interior X locations and compare counts |
| 7 | Grades 2-5 | Final footer; already sufficient otherwise | Invent an integer-grid rectangle with ten crossings on a 12 by 12 workspace |

Every final page was rendered and visually inspected. No text, label, ray,
record line or grid overlaps another element or spills outside the page.
The definition fits without reducing working-board dimensions. No student
formula, hint, extra tally or new numbered task was introduced.

The review's trace-first/count-afterward and shared-case facilitation note is
reserved for adults. The coordinator reported adding it to the separate guide;
this revision stage did not edit or verify that guide. No base material,
AGENTS file or global index was edited.

## Mathematical and actual-output checks

The portable builder runs `check_math.py`, then compiles twice with pdfLaTeX.
Its exact rational/integer checks passed. A separate new
`src/check_independent.py` imports neither supplied checker. It enumerates
unfolded target tiles and orders their exact boundary crossings; reads each
interior state from the straight unfolded NE ray; and intersects maximal
wall-to-wall crossing rays exactly. It also inspects the actual final PDF's
vector grids, dot centers, convention paths and page bands.

- Finish A, S=(1,1), F=(2,3): BL, BR, BT, LR, LT, RL, RT, TB. Finish B,
  S=(1,1), F=(3,3): BR, BT, LR, LT, RL, TB. Same-wall words are absent; actual
  traversal order and corner rejection are checked rather than inferred from
  target reflection alone.
- A, C, E, G, I, K, M, O reach corners. B, D, F, H, J, L, N loop, with first
  full-state return at 24 unit diagonal steps. H's point-only return at step 12
  has SE direction and is not the stopping condition.
- The four displayed crossing counts are 1, 3, 6 and 1. The invention workspace
  has six integer-grid dimension pairs with ten crossings: 3 by 11, 11 by 3,
  5 by 6, 6 by 5, 10 by 12 and 12 by 10. All 144 positive integer width/height
  pairs through 12 were independently checked.
- The actual one-bounce convention path is (1,1) to (4,2) to (1,3), with equal
  angles to the right wall. The actual direction convention dots and outgoing
  rays show NE, NW, SW on the 3 by 3 example. The final crossing visual has two
  transverse rays meeting at the same circled midpoint, one location.
- All sixteen wall-word boards are 4 by 4 at 12.5 mm per square. The loop master
  board is 6 by 4 at 22 mm; both extra boards are 6 by 4 at 18 mm. Its three
  convention grids are 3 by 3 at 7 mm. The four crossing boards are 2 by 3,
  3 by 4, 4 by 5 and 4 by 6 at 12.5 mm; the invention grid is 12 by 12 at
  12.5 mm, 150 by 150 mm. All units have equal horizontal and vertical scale,
  and every bounded board has four sides. Every actual start, finish and A-O
  interior dot was checked against its printed grid.

Evidence within this final folder: `build/math-checks.json`,
`build/independent-checks.json`, `render/pdf-checks.json`, and
`build/rebuild-checks.json`. `src/README.md` documents the build and optional QA.

## Portable-source consistency and limits

`return-visit-source.zip` contains the standalone `src/` folder with its TeX,
portable builder, checkers and README. It was extracted into the separate
`../revision-clean-rebuild/` directory and built there without repository assets.
Both compilation passes and all three checks passed in that extraction. Each of
the seven rebuilt rendered-page SHA-256 hashes matches the inspected final page.
Neither build reported overfull/underfull boxes or LaTeX warnings.

Print single-sided at 100% on US Letter. The mathematical and digital checks do
not establish physical counter fit, ruler/tracing-paper reflection handling,
a floor-grid rehearsal, classroom independence or pacing. Those remain
untested. There are no technical blockers to this reviewable student deliverable.
