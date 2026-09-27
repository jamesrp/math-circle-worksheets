# GA4 independent PDF review

Reviewer: expand_ad1. Date: 2026-09-25. Status: closed and approved for assembly from `ga4-preview-r4`; no remaining PDF findings. No author data, module or PDF was edited by this reviewer.

## Actual coverage and identity

Reviewed `tmp/pdfs/atlas-remaining/ga4-preview-r3/`:

- Every student page 1–25 at full size: contents and all 24 investigation pages.
- Every facilitator page 1–34 on all four contact sheets.
- Additionally inspected facilitator pages 1,3,4,8,9,11,12,13,16,17,18,20,21,24,25,26,28,29,30,32,33,34 at full size. These include all worked figures/tables, dense symbolic derivations, general theorem statements and the discontinuous-map extension.
- Original page PNGs are 100-dpi Letter renders. Inspected actual page images, not solely extraction or layout reports.
- Independently checked that all 48 planned student prompt strings occur once in the printed-task record, with exact family/prompt identities. Eight guide extensions are present and answered.
- Recomputed both PDF SHA-256 hashes and checked them against the maker report. Student: `56e8f4b59c4e31669d8fd13ed18898968c5e9c82a2378699e99347ff9769617c`; facilitator: `79d8d33d6d0925715465a1b265dba0641a726b58721c53590d62d1ca36220a27`.
- Mechanical reports show 25/34 pages, no blank pages, no out-of-page characters and no suspect glyphs. These supplement visual review.

## Findings sent to the owner

1. **GA-30, first student page (PDF page 5), prerequisite label.** The page asks for an exact length in prompt 2. Its local gate currently says only “paper construction and length comparison.” Add the Pythagorean theorem explicitly, consistent with the contents and full guide. The owner independently noticed the same issue; this reviewer agrees. This is a gate clarity repair, not a diagram or solution error.
2. **GA-35, prompt 6 key (facilitator PDF page 29), general theorem domain hypothesis.** “Every C² harmonic function has its center value as every contained circle mean” should explicitly require the closed disk bounded by the circle to lie in the open domain. Containing the circumference alone is insufficient. The source evidence already says “contained-ball hypotheses”; bring the actual key sentence into agreement. The finite quadratic classification and all rendered numerical averages are correct.

No other repairs were found. The owner will produce a fresh path, and this reviewer will reread changed pages and compare unaffected PNGs before closing.

## Family-specific mathematical and visual fidelity

- **GA-28 (student 2–4).** Four comparisons are a stated budget rather than an answer-count scaffold. The adversary may delay its consistent interior choice; the worksheet leaves test points blank. The midpoint bracket [11/8,23/16], midpoint error 1/32 and seven-test width threshold agree with the key. The cubic sends 0→1→0 with nonzero derivative denominators; the separate bracket [−2,−7/4] is correctly keyed. The numbered timeline supports both tests without printing the retained bracket. Calculus is marked on the Newton continuation.
- **GA-30 (student 5–7, guide 9).** The paper rectangle has the intended 6:4 geometry, with A at the lower seam and B halfway around the upper rim. Spare-copy cutting and edge-to-edge joining without overlap are explicit. The repeated map uses equal units and copies −9,−3,3,9 at height four. The guide drawing marks precisely the two length-five lifts and retains the longer copies; its integer bound handles unseen copies. Endpoint offset zero and the tie at three are correctly handled. The local gate is the only repair requested here.
- **GA-31 (student 8–10, guide 13).** All four original closed interval endpoints match their numbers, preserving singleton intersections. The planar working grid is blank and supplies the correct clipped square. In the guide, x+y=−1 runs from (−2,1) to (1,−2), the southwest triangle is shaded, and all pair witnesses are at the claimed coordinates. The disconnected point sets show dots rather than filled intervening segments. The endpoint certificate and its same-interval exception are correctly keyed.
- **GA-32 (student 11–13, guide 18).** Seam arrows distinguish matching and reversing identifications. U/L labels and the three-lane caption specify which left lane the right edge meets; they do not preprint component counts. Workspace permits tracing the whole seam journey. The guide correctly separates connected components, boundary loops, annulus/Möbius type and physical linking. The three-lane cycle table and general m-lane count agree with the stated rule. Ordinary strips, tape and scissors suffice; a successful physical cut is not required for the proof.
- **GA-33 (student 14–16).** The two-start plot has numeric axes and a separate vertical label, with room to sketch trajectories. The forcing plot has a named vertical quantity and upper scale. The candidate, improper-integral definition, integration-by-parts endpoints and real s>0 restriction are legible. The key retains −a, verifies the recovered solution directly and proves uniqueness with an integrating factor. The changed input gives te^(−t), whose peak is correctly tied to equality of input and loss. No solution curve is preprinted.
- **GA-34 (student 17–19).** The chosen-height table is an explicit three-choice experiment; its blank cells do not reveal answers. The before/after panels show the same singular time without drawing a spurious connecting branch. Positive, zero and negative starts are explicitly requested and keyed separately. General times 1−2^(−n), reciprocal transformation and finite-time obstruction agree; the extension retains p>1 and positive solutions. The calculus gate is visible from contents onward.
- **GA-35 (student 20–22, guide 30).** The initial circle is centered at (1,2) with radius two on equal-scale axes; the open cardinal points mark given sample locations without giving values. The rotated cross and 45-degree configuration match their definitions. The polynomial coefficient classification is A+C=0, and the quartic averages are correctly separated as 0,1/4,1/8. The actual integral and Laplacian question retain the advanced gate. Only the quoted general harmonic theorem needs the closed-disk hypothesis clarified.
- **GA-36 (student 23–25).** Blank unit-square plots show y=x as a reference and leave the machine graphs to students. The four-update ledger follows the stated request. The interval endpoints and q∈[−1,1] range are explicit. Four iterations are the exact uniform .01 guarantee for the contracting affine map; reflection provides the correct nonconvergent comparison. The q=−1,0,1 cases and excluded-endpoint example are complete. The discontinuous extension displays both branches and all inequalities correctly in the actual PDF, despite a lossy HTML-stripping artifact in the bounds report's plain-text field.

Contents entries point to the actual family starts in both books. Body text and guides are readable with adequate margins; no overlapping text, clipped labels or blank spill pages were found. This report covers these preview bodies and contents, not any future assembled edition. Classroom preparation, timing and engagement remain unpiloted.

## Repair closure at fresh r4 path

Both findings are closed. Independently compared every PNG in `ga4-preview-r4` against r3: only student page 5 and facilitator pages 6 and 29 changed; the other 56 pages are byte-identical. Opened all three changed PNGs at their new absolute paths and inspected them at full size. The student prerequisite and matching guide repetition now explicitly require the Pythagorean theorem. The harmonic key now explicitly requires the circle's closed disk to lie in the open domain. Both repairs remain readable with clean layout.

Current approved preview: `tmp/pdfs/atlas-remaining/ga4-preview-r4/`. Counts remain 25 student and 34 facilitator pages. Fresh reports have no blank, out-of-page or suspect-glyph findings. Independently recomputed hashes:

- Student: `9eaf359c88bb1d058fc98d22a71a8d81e6d7941b26f17694f727a425f785b77f`
- Facilitator: `59fce68c895a1d5762ad8199de55b19a190a86f274ceb506855a876ae1849d0e`

The earlier full-body pass plus this exact unchanged-page comparison and full-size repair pass covers the current preview. Approved for final assembly subject to the editor's final-body identity and new-contents checks.
