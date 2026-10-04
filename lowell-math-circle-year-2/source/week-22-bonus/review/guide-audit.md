# Week 22 independent adult-guide audit

**Verified.** Every overview, actual final P1–6 solution, hint, extension, note, closed-region assumption and source-role claim was independently reviewed. Five rendered guide pages were inspected. `guide-checks.json` records current authority checksums; `guide-independent-check.py` reproduces extra Fraction geometry and line-extension enumeration using only Python's standard library.

| Final task | Independent result |
|---|---|
| P1 minimum supporting dots | Verified T=(4,16/5) lies on none of all 15 joining lines, stronger than merely being on no pair segment. Exactly three dots are needed; the complete eight containing triangles are ABE, ACE, ADE, ADF, BDF, BEF, CDF, CEF. Exact CEF weights 11/25,4/25,2/5 are positive and sum to one, yielding T. |
| P2 one/two/three/four | Verified targets A, midpoint (3,0) of AB, and T need one, two, three respectively. Triangulation by original boundary vertices proves at most three for every target in a finite planar hull; degenerate hulls need one/two extremes. An interior target on a diagonal can need only two. |
| P3 fixed strict separation | Verified AC and BD meet at (4,4) and cannot be strictly separated. AB/CD admit y=4 and all horizontal 1<y<7. The general compact-hull closest-point proof has the correct derivative signs and a strict positive bisector gap. Touching hulls remain inseparable under the strict rule. |
| P4 line groups | Verified all 25 five-label partitions: exactly AD/BE/C and AE/BD/C succeed. All six four-label partitions fail for distinct positions. The middle-singleton/outer-pairs guarantee includes repeated positions. |
| P5 regular hexagon | Verified equal scaling, center (4,4), radius 7/2; among all 90 three-group partitions only AD/BE/CF succeeds. The task requests a witness, so uniqueness is correctly additional adult information. |
| P6 irregular hexagon | Verified strict convexity, singleton exclusion and all 15 pairings. Only AD/BE/CF has all three pairwise crossings. AD/BE meet at (37/9,28/9), but CF at that x has y=179/72, so no common point. All 90 partitions fail. |

The general line extension is proved for r≥2: 2r−1 labels suffice using a middle singleton and r−1 nested pairs; with 2r−2 distinct positions every r-group partition has at least two singleton groups, which cannot meet. Independent enumeration at r=2,3,4,5 finds respectively 1,2,6,24 successful distinct-point partitions above the threshold and zero below. Repeated-location witness checks also confirm every tested ordered case. These are line results; no planar seven-point or general higher-dimensional formula is asserted.

For the printed strictly convex hexagon, target variants at vertices need one, nonvertex boundary-edge points need two, and targets off all pair segments need three. A finite pair-segment arrangement organizes the cases. Hints retain the original full hull, use closed filled regions and insist on a common point in all three groups. The theorem-first overview states the actual guarantees and limits; fixed-table staffing and realistic readiness gates are present.

Attribution is accurate. Current base-guide closed-hull and Radon context matches the cited exclusions. Gallier–Quaintance section 3.5 is identified as recorded context, with no claim of new source-body reading. Math Circle by the Bay Preface vii–x/PDF 8–11 supports the stated teaching context while routes are proposed adaptations.

No unresolved mathematical issue. Marker/tracing registration and classroom procedures remain untested; extracted-source ZIP rebuilding is a separate release check.

## Verification-text refresh

Verified the final status-text revision independently against the saved pre-revision JSON. Only `verification` changed; every other parsed field is identical, including all overview, solution, hint, extension, material, launch and source content. Both new verification paragraphs were read in source and on the rebuilt page 5; that page was rendered and inspected, remains legible, and the guide remains five pages. All 41 JSON prose paragraphs occur in the rebuilt PDF. The packaged `guide-src/guide.json` is byte-identical. The independent guide checker passed again without mathematical changes.

Current guide JSON SHA-256: `d53792961f90517a095314db2a6cb2d89dceb5cf87fd6b4d7884b94c82530700`.

Current guide PDF SHA-256: `a85ab45461a8b486863ed4fb671b7e0313e9066dbcbf5f36b895095ad7979410`.

The inspected release-validation record reports completed passing checks for its recorded reference files; current package synchronization and repeated ZIP validation belong to the root release process. This refresh confirms the new status wording and mathematical identity rather than claiming an additional ZIP rebuild by this reviewer. Physical fit and classroom rehearsal remain untested.
