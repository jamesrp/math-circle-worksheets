# Independent AD1 PDF review

Reviewer: AP1 author. September 25, 2026. Review is closed; both wording repairs passed fresh-path inspection.

## Actual coverage

Reviewed `tmp/pdfs/atlas-remaining/ad1-preview-r2/`: 26 student pages (contents plus 25 investigation pages) and 40 facilitator pages. Every student page 1–26 was inspected at full size. All five guide contact sheets were inspected, covering all 40 pages. Guide pages 1, 13, 16, 19, 24, 25, 26, 28, 30, 34, 38, 39 and 40 were also inspected at full size, covering the contents, all five worked-figure sections and dense proof/extension pages.

Read the full data and keys, relevant renderer logic and maker QA. Author files were read-only; the author owns repairs. Initial student SHA-256: `8c12b9ac4409aa8d0f3586f45d21f18eed13e64b4f0c657129ce9b95f5fd546b`. Initial guide SHA-256: `eb5bf10c42352f916e4a16ad5e8d3b2f39ae6225002fa5610c887dba5e028ca6`.

## Findings

1. AD-02, student page 5, prompt 2: “without trying all sixteen words” prematurely gives the total and minimum complete-list size asked in prompt 4 on page 6. Replace it with “without searching through every possible word.” The open collection area itself preserves discovery.
2. AD-06, student page 20, prompt 6: “lattice” is not defined on the three student pages. Add “every pair has both JOIN and MEET” as its meaning. The existing diagrams and preceding operations are correct.

The author accepted both. No further findings arose in the full pass. Fresh-path rereading is required for closure below.

## Mathematical objects and usability

| Family | Student pages | Checked observations |
| --- | --- | --- |
| AD-01 | 2–4 | R/B letters and circle/square outlines remain distinguishable without color. Four-type panels support a complete certificate. The first minimal world needs RC and BC; later promises force BS and forbid RS. Empty-world and negation tasks have real construction space, without preprinting their witnesses. |
| AD-02 | 5–7 | Supplied four rows match the data. The protected diagonal gives 1000, differing from its own row at every matched position. First-page choice is open; the next page deliberately supplies the diagonal method after exploration. Infinite indices are visibly gated and the schematic matrix does not pretend to list actual infinitely many bits. Only the premature count needs removal. |
| AD-03 | 8–10 | All sixteen distinct subsets appear. The initial deck does not group the six optimal pairs as a ready solution. The later six-chain proof scaffold is a staged certificate, with seven-card obstruction explicitly requested. Worked chains cover 16 cards exactly once, with lengths 5,3,3,3,1,1. Forced A leaves the nonempty BCD deck and a maximum of four including A. |
| AD-04 | 11–13 | X has edges 12,13,34 and code (1,3); Y has 13,23,24 and code (3,2). Numbered circles are the only vertices and the supplied Y is not falsely crossed. Blank decoding records track surviving labels and remaining suffix. Worked (4,4,2) ledger yields 14,34,24,25 and degrees 1,2,1,3,1. The guide’s inverse proof uses absent labels and residual degree, not just example matching. |
| AD-05 | 14–17 | Five-road drawing and dashed trace templates match AB,BC,CD,DA,AC. Twelve trial frames do not cue the eight final answers. The six-road overpass explicitly excludes an intersection vertex. The eight worked trees are distinct: four omit AC, four contain it. Closures preserve 4 trees for AC and 3 for a perimeter edge; the six-road graph has 16 trees. Matrix page is separately gated and states the theorem as supplied. Both printed 3×3 minors have determinant 8, while full L is singular. |
| AD-06 | 18–20 | Set cards and intermediate-result boxes make the nested recipes performable. The five-element diamond has every pair’s operations, but a,b,c give L=a versus R=0. The six-element drawing has incomparable upper bounds r,s for p,q and matching lower-bound failure. Crossings are not tile circles. Redrawing permits an added r<s comparison to remain upward. The only missing student definition is lattice. |
| AD-07 | 21–23 | Rules visibly preserve tokens and stop only when no new token is available. The two histories from {a,d} and the open minimal-generator area support choices. The complete subset deck supports finding the seven closed sets. Positive-premise intersection and order independence are correctly distinguished from the final removal-rule counterexample. |
| AD-08 | 24–26 | Clockwise arrows, ring labels and addition table agree modulo four. Independent representative choices are explicit. Three-bag repair layouts are supplied starting instances, not final answer counts. All final partitions are left to an open record. The guide’s singleton/parity/all partition classification, E/O addition table and f(0)=f(1)=0, f(2)=f(3)=1 failure witness match the tasks. The modulo-six extension has four subgroup/coset partitions with its advanced gate stated. |

All required instructions, supplied data and work regions are present. The mathematical classification and proof tasks remain more than routine table filling. AD-01, AD-03 and AD-05 offer especially concrete entry points; AD-04 decoding and AD-06 nested operations require patient facilitation. The infinite and determinant pages retain actual prerequisites rather than an elementary substitute.

No clipped text, displaced label, accidental diagram vertex, incorrect operation arrow or unreadable dense formula was found. Student labels and body text remain legible at the intended size. Blank-page, bounds and glyph reports are supporting checks only. This is PDF fidelity and usability review, not a substitute for the separate independent design/source audit, nor a classroom pilot. Final assembled books need editor identity/contents checks.

## Repair closure

Both findings are closed in `tmp/pdfs/atlas-remaining/ad1-preview-r3/`. I independently compared all 66 rendered page files with r2: only student pages 5 and 20 and guide pages 7 and 29 changed; the other 62 PNGs are byte-identical to the reviewed pages. I reopened all four changed pages at full size under the new path. The premature count is removed, lattice is defined accurately, and the extra line leaves ample diagram and writing space. No new clipping, flow error or mathematical change appeared.

Current student SHA-256: `616160d8c15ca1c8dff1ca21e504c00d1f3954a9b82595629ce22ee144da14f3`. Current guide SHA-256: `a82799ea8592cb34f45785d324144e7009edd98b5c8cf9212053b06972eefaaa`. Counts remain 26 student and 40 guide pages.

**AD1 is approved for assembly from r3.** This approval covers the specified page-body inspection and unchanged-page identity, with the final editor’s assembly and new-contents checks still required.
