# Week 20 independent adult-guide audit

**Verified after the integer-endpoint clarification.** Every overview, actual final P1–6 solution, hint, extension, note, assumption and source-role claim was independently reviewed. The corrected five-page PDF was inspected. `guide-checks.json` binds current source/PDF/student authority, and `guide-independent-check.py` reproduces extra exact checks using only the standard library.

| Final task | Independent result |
|---|---|
| P1 stopping walks | Verified A=2, B=4, C=3 from first-step equations; terminal-6 probabilities 1/3 and 2/3. Survival after n moves is exactly (1/2)^n on the printed path. Scaling fixed scores 0,6 to 0,3 gives expectations 1,2. Finite trial means are not exact guarantees. |
| P2–3 dynamics | Verified first return 2 for unequal alternating four-cycle states; constants return in one tick. Neighbor-only two-circle values swap; own-and-neighbor gives 3,3 in one tick. Printed three-circle convention 0,3,6 → 3,3,3 agrees with its actual edges. |
| P4 own-value four-cycle | Verified first boards 4,2,4,2; 8/3,10/3,8/3,10/3; 28/9,26/9,28/9,26/9. Exact formula 3±3(−1/3)^t, fixed midpoint and nonzero gap prove approach to 3 without finite equality. Claims are confined to alternating states. |
| P5–6 roughness | Verified all 7 and 49 allowed assignments: unique minima 18 at 3 and 12 at 2,4. Both printed squared-deviation identities hold for all real guesses, including nonmonotone choices. Convention 0–1–3 has score 5. |

The finite-graph stopping proof is correct: reachability gives bounded paths and a uniform positive absorption probability per block. Scores are bounded on the finite set of fixed squares, so expectations exist. The energy proof is correct: each undirected edge is counted once; regrouping the cross term at vertices makes it zero by harmonicity and fixed-boundary differences. Equality requires constant differences on connected components and zero on every component reaching a square. Those anchoring assumptions give uniqueness; unanchored components do not.

The path extension has minimum (B−A)^2/L by summing squared deviations from the common gap. Its integer criterion now explicitly assumes A and B are integers; then all values are integers exactly when L divides B−A. The prior wording admitted, for example, A=B=1/2 with an integer difference but noninteger intermediate values. The correction is present in both JSON and PDF. Independent exact checks cover L=1…8 and integer endpoints −3…3 (392 cases), together with arbitrary comparison paths for the identity. General alternating-pair identities were checked exactly on 100 pairs and the printed sequence through tick 15.

Hints preserve one unchanged BEFORE state, include zero neighbors, avoid rounding and distinguish a sampled score from an expectation. The theorem-first overview and fixed-table staffing are present. Source roles are accurate: current base-guide claims agree; Doyle–Snell is recorded context without a claim of new body reading; Math Circle by the Bay Preface vii–x/PDF 8–11 supports teaching context while proposed pacing is marked as design.

No unresolved mathematical issue. Physical fair-choice, copy-state and fit procedures remain unrehearsed. This audit does not claim the separate extracted-source rebuild.

## Verification-text refresh

Verified the final status-text revision independently against the saved pre-revision JSON. Only `verification` changed; every other parsed field is identical, including all overview, solution, hint, extension, material, launch and source content. Both new verification paragraphs were read in source and on the rebuilt page 5; that page was rendered and inspected, remains legible, and the guide remains five pages. All 39 JSON prose paragraphs occur in the rebuilt PDF. The packaged `guide-src/guide.json` is byte-identical. The independent guide checker passed again without mathematical changes.

Current guide JSON SHA-256: `b46261580125e17d860d396e4f553bdf3a5b55a84103a721dbc82e5056841c1c`.

Current guide PDF SHA-256: `5f8deb8e8d833a0f28652f4c55e9c5e500fdd51ffc9258671d6a278cba937406`.

The inspected release-validation record reports completed passing checks for its recorded reference files; current package synchronization and repeated ZIP validation belong to the root release process. This refresh confirms the new status wording and mathematical identity rather than claiming an additional ZIP rebuild by this reviewer. Physical fit and classroom rehearsal remain untested.
