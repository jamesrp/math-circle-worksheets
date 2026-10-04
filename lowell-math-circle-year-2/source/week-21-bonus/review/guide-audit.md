# Week 21 independent adult-guide audit

**Verified.** All overview, actual final P1–5 solutions, practice images, hints, extensions, legal-region assumptions and source roles were independently reviewed. Five rendered guide pages were inspected. Current guide/student checksums are in `guide-checks.json`; `guide-independent-check.py` reproduces additional exact extension checks without external mathematical data.

| Final task | Independent result |
|---|---|
| P1 lower then upper | Verified image (7,−7), contacts (11/5,1),(29/5,7), minimum √136 units = 20√136 mm. Both contacts lie on the actual finite walls. |
| P2 upper then lower | Verified image (7,17), contacts (19/7,7),(37/7,1), minimum √232 units. P1 is shorter. Unfolding preserves each leg; triangle equality fixes unique contacts in either order. |
| P3 closed windows | Verified unrestricted contact (3,1) is excluded. Best legal candidates are (2,1),(5,1), with lengths √5+√41 and 4√5. Since 41<45, the left candidate is the unique winner. Strict convexity proves monotonic increase away from the unrestricted contact and covers every allowed point. |
| P4 rectangle | Verified unique lower route of length 4+2√5 versus upper 4+2√8. Local straightening removes free-space/edge-interior bends; loop removal and visible-corner enumeration cover all routes. Eight simple visible-corner paths were checked. |
| P5 mid-height | Verified exactly two geometric shortest routes, each 9 units = 180 mm; outer legs are exactly 5/2. Eight visible-corner paths were checked. Adding redundant straight-leg points does not produce another geometric route. |

The practice path is correctly retained as a broken, nonoptimal path; both reflections preserve every squared leg length. For a strip of positive height H with endpoints strictly inside, the two unfolded vertical magnitudes are 2H+hA−hB and 2H+hB−hA. Their squared difference is 8H(hA−hB), proving the printed tie/direction rule; finite wall contacts must still be legal. This was additionally checked in 63 rational cases.

The rectangle extension is verified for its stated equal-outside-distance family: common-height endpoints tie exactly at mid-height; below it lower wins and above it upper wins. Eleven exact heights on the printed rectangle were checked. The open-window warning is also correct: replacing [1/2,2] by [1/2,2) leaves the smaller global infimum √5+√41 unattained despite a closed second window.

All hints respect contact order, finite-wall legality, closed-window bounds, and the change to legal obstacle-boundary travel. The theorem-first overview and fixed-table staffing are present. Source roles are accurate: base-guide single-wall and restricted-window material agrees; Petrunin sections 1C/5D are recorded context rather than newly read body; Math Circle by the Bay Preface vii–x/PDF 8–11 supports the described teaching context, with routes clearly proposed.

No unresolved mathematical issue. String handling, scale, tracing and classroom procedures remain unrehearsed. Extracted-source ZIP rebuilding is a separate release check.

## Verification-text refresh

Verified the final status-text revision independently against the saved pre-revision JSON. Only `verification` changed; every other parsed field is identical, including all overview, solution, hint, extension, material, launch and source content. Both new verification paragraphs were read in source and on the rebuilt page 5; that page was rendered and inspected, remains legible, and the guide remains five pages. All 40 JSON prose paragraphs occur in the rebuilt PDF. The packaged `guide-src/guide.json` is byte-identical. The independent guide checker passed again without mathematical changes.

Current guide JSON SHA-256: `a8aa47bbc9aeece8178941196b79d190234fc3042517cf3545e34104287fe26c`.

Current guide PDF SHA-256: `5f39108f7168bf51c3aeb0c41fd26b0687033f21c443c169c400f65cdfcf632e`.

The inspected release-validation record reports completed passing checks for its recorded reference files; current package synchronization and repeated ZIP validation belong to the root release process. This refresh confirms the new status wording and mathematical identity rather than claiming an additional ZIP rebuild by this reviewer. Physical fit and classroom rehearsal remain untested.
