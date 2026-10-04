# Week 19 independent adult-guide audit

**Verified.** Current guide maps the actual final Problems 1–8, including P6's single-symbol-removal definition. Every overview, solution, hint, extension, note, readiness limit and source-role claim was read independently. Rendered guide pages 1–5 were inspected. Current source/PDF and student-authority checksums are in `guide-checks.json`; the portable standard-library `guide-independent-check.py` reproduces the additional finite checks.

| Final task | Independent result |
|---|---|
| P1–3, pairwise sharing | Verified maxima 4 and 8 by complete complement partitions and attaining stars. The three-symbol maximum without a common symbol is uniquely AB, AC, BC, ABC. The alternative eight-card witness printed in the guide is pairwise intersecting with no common symbol. |
| P4–5, triggers | Verified both ten-card catalogs, and the unique necessary two-trigger minimum B, AC. Having incomplete pieces of different triggers is insufficient. |
| P6, arbitrary promised rule | Verified all 168 upward-closed four-symbol rules. Stopping on every single-symbol removal is equivalent to inclusion-minimal under upward closure. Finite descent gives a minimal card inside every working card. Empty/no-working cases and differing trigger sizes are correct. |
| P7–8, no nested triple | Verified maxima 6 and 10 and exact one-time chain coverage, with lengths 4,2,2 and 5,3,3,1,3,1. The unique three-symbol maximum and two four-symbol maxima agree with exhaustive 256/65,536-family checks. |

The additional four-chain extension is verified independently over all 256 three-symbol families: maximum 7, exactly two maximum families, obtained by omitting the empty card or ABC. There are six four-card chains, each containing both endpoints. Redundant triggers B, AB, AC give the same rule as B, AC on all sixteen cards. The complement counterexample ABC/ABD → D/C is correct. The general intersecting bound requires n≥1, now explicit in the overview and extension; the n=0 deck is outside that claim.

Hints preserve the intended rules: pairwise versus whole-family intersection, inclusion-minimal versus smallest cardinality, and nested pairs versus triples. No hint assumes a false theorem or invalid intermediate step. The theorem-first overview states finite versus general scope, prerequisites and proposed return routes; the fixed-table staffing paragraph is present.

Attribution is accurate. Current base guide pp. 3–4 and 11 supply the referenced certificates and recorded Stanley context. The companion explicitly says the Stanley body was not newly read. Math Circle by the Bay Preface vii–x (local PDF 8–11) supports interaction, manipulatives and continued themes; the proposed routes are identified as adaptations rather than observed outcomes.

No unresolved mathematical issue. Physical fit, card preparation and classroom procedures remain untested; this audit does not claim an extracted-source rebuild.

## Verification-text refresh

Verified the final status-text revision independently against the saved pre-revision JSON. Only `verification` changed; every other parsed field is identical, including all overview, solution, hint, extension, material, launch and source content. Both new verification paragraphs were read in source and on the rebuilt page 5; that page was rendered and inspected, remains legible, and the guide remains five pages. All 39 JSON prose paragraphs occur in the rebuilt PDF. The packaged `guide-src/guide.json` is byte-identical. The independent guide checker passed again without mathematical changes.

Current guide JSON SHA-256: `798f3e554acf5ef37724597e6f00d95e17545f931ad6198972e5f46b55096e33`.

Current guide PDF SHA-256: `6afdf711cd662f9bdbafd5b271360f3feff034356da8bbd4d120cbbb40909602`.

The inspected release-validation record reports completed passing checks for its recorded reference files; current package synchronization and repeated ZIP validation belong to the root release process. This refresh confirms the new status wording and mathematical identity rather than claiming an additional ZIP rebuild by this reviewer. Physical fit and classroom rehearsal remain untested.
