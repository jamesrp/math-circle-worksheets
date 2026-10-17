# Week 88 final student–guide pair review

Reviewed 17 October 2026 by an independent review agent, after the student revision and metadata-determinism changes. Scope: current eight-page student PDF, six-page facilitator PDF, editable sources, README, SOURCES, checker and builder. Review-only work; no student, guide or PDF edits.

**Disposition: student–guide pair passes digital review. No necessary content or layout corrections found.** Final package QA documentation and ZIP reconstruction remain outside this review; physical rehearsal and classroom use remain untested.

## Exact artifacts and build evidence

- `lowell-math-circle-year-2/week-88/week-88-students.pdf`: 8 pages; SHA-256 `0f7e43d5b07809ca9f117158bc9e30a28782dd63ff688e0f630372a68994b7e4`.
- `lowell-math-circle-year-2/week-88/week-88-facilitator.pdf`: 6 pages; SHA-256 `009c974069ac557256b69ee8b6397d2dcf4f49851e6c6fe704f322118fced96a`.
- Ran `build.py --out tmp/worksheet-runs/week-88-v1/pair-review/rebuilt --work tmp/worksheet-runs/week-88-v1/pair-review/build` using the supplied Python environment and `/Library/TeX/texbin/pdflatex`. The mathematical checker passed, both TeX builds passed the builder's error/overfull checks, and **both rebuilt PDFs were byte-identical to the delivered files**.
- Rendered each delivered page at 1.35× with PyMuPDF and opened all 14 individual PNGs. No clipping, overlap, broken glyphs, malformed circles, missing content or footer collisions observed. All student pages use the consistent shared K–5 header, footer and consecutive Problems 1–11.
- Independent review script and output, build logs, page images and extracted text are exclusively in `tmp/worksheet-runs/week-88-v1/pair-review/`. This independent script does not import the author's checker or data.

## Actual visual coverage: every student page

| PDF page | Content actually inspected | Result |
|---|---|---|
| 1 | Shared diameter/flatness/nonoverlap/ring rules; Problem 1; central circle; result line | Clear action, sufficiently large placement area, readable center and footer. No solution given away. |
| 2 | Problem 2; practical 160 × 112 mm tray; dimensional labels; result line | Whole usable board fits on Letter with margin; boundary, measurements and practical label are clear. |
| 3 | Problems 3–4; changed-size circles; recording spaces | Correct 2:1 relative diameter representation; sketches explicitly distinguished from actual size; ample space between tasks. |
| 4 | Problem 5; both central sizes; both-size requirement; two result lines | Constraint applies to outside disks; sketch label and instruction to use desk mat avoid treating small diagrams as physical mats. |
| 5 | Three-frame radius/center-distance bridge; Problem 6; central disk | Same unequal pair preserved through input, joined radii and 15 + 25 = 40 mm output; labels match and arrows have a clear role. Bridge precedes proof work without revealing six. |
| 6 | Problem 7; 4–3–4 row requirement; 160 × 110 mm exact tray | Clear finite construction and certificate goal; board and exact dimensions legible. |
| 7 | Problems 8–9; 160 × 108 mm exact tray; minimum-height question | Row restriction retained explicitly; height comparison and answer area are clear, with no unrestricted-packing claim. |
| 8 | Problem 10's four return cases and schematic centers; Problem 11 | All four mixed/uniform combinations correctly labeled. General rule question retained; footer clear and lower answer area available. Guide appropriately gates this page. |

The actual PDF drawing coordinates independently give clear interiors approximately 160.001 × 112.001, 160.001 × 110.001 and 160.001 × 108.001 mm on pages 2, 6 and 7 respectively (TeX/PDF rounding under 0.002 mm). The four boundary strips place ink outside those interiors. These are digital measurements, not a printed-material check. Circles use equal horizontal and vertical scale. There are no intended polygon side counts to certify in this packet; the guide's least-gap triangle has three equal sides and the packing sketch has 4–3–4 disks.

## Actual visual coverage: every guide page

| PDF page | Content actually inspected | Result |
|---|---|---|
| 1 | Theorem-first overview, size formula, finite-tray scope and discovery map | States actual sharp facts and limits before solutions; math displays legible; distinguishes construction, conjecture and proof. |
| 2 | Kits, table staffing, page routes, material checks, launch and pacing | All fits on one page; explicitly marks rehearsal untested, gives disk/tray/mat dimensions, allows manipulation before demonstration. |
| 3 | Key for Problems 1–5, tray coordinate table, both mixed witnesses | Complete for asserted claims; numeric witnesses and table legible. Practical tray is expressly an optimization investigation with an eleven-disk lower-bound certificate. |
| 4 | Problem 6 proof, least-gap triangle, equality and five-neighbor contrast | Triangle and labels clean. The guide correctly distinguishes least-angle equality from general nonoverlap. |
| 5 | Problems 7–9 key, exact lower bound, full 4–3–4 picture and hints | Correct eleven-disk illustration; center triangle/altitude visible; row-only boundary repeated. |
| 6 | Optional Problems 10–11 key, mixed angle bounds, sources and use record | Full derivations fit legibly. Positive-radius and congruent-outside assumptions appear; both-size cases remain separate. |

## Independent mathematical verification and keyed answers

The package checker passed, but the following conclusions were separately rederived and checked. Physical approximations were not treated as proofs.

1. **Problem 1: six.** Equal 40 mm disk centers are 40 mm from the middle center. Successive angular gaps are at least 60 degrees; six equally spaced disks attain the bound. Seven would require at least 420 degrees.
2. **Problem 2: eleven demonstrated, no global maximum certified.** Centers `(20,60,100,140)` in the bottom/top rows and `(40,80,120)` in the middle row, at heights `20`, `20+20√3`, `20+40√3`, give pairwise distances at least 40. They fit inside 160 × 112 mm. The guide explicitly declines an unrestricted optimum; this matches the student request to improve a packing and does not present failed searching as proof. This review likewise does not claim the unrestricted maximum is eleven.
3. **Problem 3: nine.** Minimum gap `2 asin(1/3) = 38.942441...°`; ten need 389.424...°. Nine at 40-degree increments fit; shortest outer-center distance is 41.042417... mm.
4. **Problem 4: four.** Minimum gap `2 asin(2/3) = 83.620630...°`; five need 418.103...°. Four right-angle placements have shortest distance `60√2 > 80` mm.
5. **Problem 5: eight around the 80 mm center and five around the 40 mm center**, with at least one of each outside size. Independently evaluated every pair of the guide's exact witnesses: large center with large outer disk at 0° and small outer disks at 50, 90, 130, 170, 210, 250, 290°; small center with large outer at 0° and small outers at 80, 140, 200, 260°. Every outer disk touches the center and every pair is nonoverlapping. Minimum pair clearances are 1.042417... mm and zero (within floating rounding), respectively. All witness disk edges fit a centered 260 mm square mat.
6. **Problem 6: six and yes, every neighboring outer pair touches.** Six gaps each at least 60 degrees sum to 360, forcing equality. A gap over 180 degrees does not invalidate the lower-gap argument. Deleting one disk gives four 60-degree gaps and one 120-degree gap; the regular five-ring gives five 72-degree gaps. Thus the adult flexibility contrast is correct.
7. **Problem 7: yes in ideal geometry.** The same tray coordinates require `40+40√3 = 109.282032...` mm height, leaving 0.717968... mm in the exact 110 mm tray. All 55 pair distances and all edge clearances independently checked.
8. **Problem 8: no for straight rows 4–3–4.** A width-160 row of four diameter-40 disks forces x-centers 20, 60, 100, 140. Every x-coordinate permitted to a middle-row center is at most 20 from one of these. Nonoverlap therefore requires each vertical row separation at least `√(40²−20²) = 20√3`. Adding top/bottom radii gives height exceeding 108. This is not an unrestricted packing proof.
9. **Problem 9: minimum `40+40√3` mm for those rows.** The preceding lower bound is attained by the supplied construction.
10. **Problem 10:** the uniform bounds above apply to Problems 3–4. For mixed large-center rings the least small-small/large-small/large-large gaps are 38.942441...°, 48.189685...°, 60°. Any nine-ring has two gaps incident to a large disk at least the middle threshold and seven others at least the first, requiring 368.976459...°. For a small center, the thresholds are 60°, 70.528779...°, 83.620630...°; any mixed six-ring needs at least 381.057559...°. Larger rings would contain a forbidden-size subring after deleting disks while retaining both sizes. Independently enumerated all 510 binary mixed nine-words and all 62 mixed six-words; their minimum angular sums agree with these proofs. The guide's pair-angle formula follows directly from the cosine rule.
11. **Problem 11:** for positive radii R and r and unlimited congruent outer disks, `floor(π/asin(r/(R+r)))`. The chord bound supplies necessity; equally spaced outer centers supply sufficiency, including the two-disk case when the central disk is very small. The formula must not be applied to mixed radii, and the guide says so. Scaling both radii preserves the ratio and maximum.

## Child purpose, prerequisites and route

The concrete core has meaningful choices: build a ring, improve a tray packing, reverse disk sizes, and compare mixed rings. Tasks do not prescribe a discovery method or turn the investigation into transcription. Result lines are light bookkeeping. Hands, pieces and partner checks externalize the rule.

Guide page 1 supplies a useful prerequisite map: touch/overlap and adult reading at the youngest entry; counting final arrangements for construction work; centers, equal lengths and a whole turn for upper proof work; exact radicals and inverse trigonometry as readiness-dependent adult conversations. Page 2 gives a realistic first route of pages 1–2, then optional changed/mixed sizes, later centers and exact trays. Page 6 retains the richer late mathematics without making it compulsory or treating grade labels as sufficient prerequisites. The general formula is demanding; that is openly gated rather than hidden or deleted.

The whole-group launch gives handling time, contrasts touching/overlapping/separated pieces, lets a child demonstrate legality, and stops before solving a ring. The separate tray demonstration correctly removes the central-touch condition. Staffing, reusable disk quantities, a 260 × 260 mm desk surface, printing, and the need to measure accuracy are stated. Kits support the relevant constructions; cutting many exact circles is appropriately called out as an avoidable weekly burden.

## Necessary fixes and remaining release work

- **No required changes to student pages or facilitator content found.** No new pedagogical restriction is proposed from unpiloted assumptions.
- **Before package completion:** `lowell-math-circle-year-2/source/week-88/README.md`, Rebuild section, links `QA.md`; that file was absent at the time of review. The coordinating author should add the actual final QA record and ensure that its statements match completed checks. README's reference-PDF/portable-package statements should become true in the completed package.
- **Not checked here:** a source ZIP (not yet assembled), rebuild from an extracted ZIP, archive contents, reference-copy synchronization, combined/index synchronization, remote copies, physical printing or disk accuracy, exact physical fit, handling or classroom piloting. A direct source build is not evidence of ZIP reconstruction. The coordinating author owns those remaining packaging checks.

The references in SOURCES were inspected as provenance notes; this review did not reopen the external survey or private pedagogical book and does not claim a fresh independent provenance audit. Mathematical conclusions above stand on the independent elementary checks and arguments.
