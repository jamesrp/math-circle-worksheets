# Week 73 revision record

Status: independently reviewed prototype awaiting organizer review, unpiloted. One shared Grades 4–5 student packet, four US Letter pages. The fresh reviser used the completed independent critic and mathematical reviews; this is not a new writer or guide stage.

## Review decisions

- Addressed critic 1: Problem 2 now asks which O positions survive **your tests**, preserving the experimental nature of ruler measurements. Exact all-pairs questions remain in Problems 3–4.
- Addressed critic 2: the checking partner explicitly tests pairs to find the largest stretch. The score remains the largest stretch **found**, rather than a falsely certified maximum.
- Addressed the minor Problem 2 operation-order note: the partner places O before the instruction to join it to the corners.
- Retained the deliberate flat five-pin opening, original fan model, child-controlled placements and pair choices, convention examples, whole-sheet map challenge, side constraints, diagonal proof obligation, and open target invention. Critic 3's pacing concern is recorded for the separate adult stage; no redesign was warranted.
- Addressed critic 4 through precise prerequisite and measurement limits in final/src/README.md. No proof hints or all-pairs solution were added to the student pages.
- No substantive review finding was rejected. Untested physical operation is an explicit limitation, not grounds to remove sound mathematics.
- Normalized the source README status and all four page footers to GGT73-S-v1.
- Strengthened the local checker to rational squared-distance regression tests and labeled finite sampling honestly. The portable builder is unchanged and has no absolute dependency.

## Verification

The local checker passes for 361 exact pin placements, the squared-distance identity, both printed target rectangles, and target-invention examples. Independently reran check73() and stretch_checks() from the independent mathematical review, including its 225 placements and 224 off-center midpoint failures. Reviewed the universal boundary, squared-distance and tangent-disk arguments against the unchanged final mathematical tasks.

Built final/students.pdf with the repaired cloud TeX environment. Rendered all four final pages at 110 dpi and visually inspected each: shared physical scale, rectangle/square proportions, fan labels, midpoint convention, answer space, headers and GGT73-S-v1 footers are correct; no overflow, overlap or clipping was found. Copied only final/src to an isolated temporary directory, rebuilt there from an unrelated current directory with --out PATH, and checked exact extracted-text and four-page raster identity. Logs and machine-readable independent results are in final/qa.

## Required handoff to the separate adult author

- Paper unit is 0.94 inches and the grid is quarter-unit. O=(1.25,1) produces only about 0.735 mm excess on the midpoint witness; arbitrarily nearer points give arbitrarily smaller discrepancies. Measurement cannot certify the unique exact position. Do not require exact answers from ruler noise.
- Transition when the five-pin tie is noticed rather than requiring many more placements. Its mathematical role is the failure of sparse measurements.
- Separate three levels: observed candidate, exact midpoint argument within the affine-fan family, and whole-sheet upper/lower proof over all pairs and maps. Later all-pairs work must handle diagonal displacements; reserve geometric or squared-distance support for the adult.
- Dot/strip/ruler and midpoint operation at 100% print scale remain unrehearsed. Organizer review and classroom pilot remain outstanding.

No guide, publication, source ZIP, or release copy was produced in this stage.
