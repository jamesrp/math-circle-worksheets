# GA3 independent PDF review

Reviewer: root, independent of PDF maker `expand_ga1`. September 26, 2026.

Status: **CLOSED — approved for final assembly.** All mathematical and layout checks below pass. The sole independent caption finding is repaired and verified under a fresh path.

## Actual inspection coverage

- Read all 26 student pages at full size from `tmp/pdfs/atlas-remaining/ga3-preview-v3/qa/student/pages/`, including its contents page and all 25 investigation pages.
- Inspected all 42 guide pages on the five contact sheets from the immutable `ga3-preview-v2` path.
- Inspected these 27 v2 guide pages at full size: 3, 4, 5, 7, 8, 9, 11, 12, 13, 15, 16, 18, 19, 22, 23, 26, 27, 28, 30, 31, 33, 34, 35, 38, 39, 40, 42. These cover dense formulas, proofs, extensions and worked diagrams.
- Independently compared all v2/v3 PNG bytes: the only guide change is page 41, and that v3 page was inspected full size. The other 41 guide page images are identical. The five changed student pages 14, 16, 20, 24, 25 were included in the complete v3 student pass.
- Read the v3 reports: 26 student pages, 42 guide pages, exactly 50 printed student tasks, no blank pages, no out-of-page characters and no suspect glyphs. These mechanical checks supplement the actual visual inspection.

## Family findings and evidence

- **GA-18, student 2–4:** The landscape preserves the exact 2:1 horizontal widths, has the correct open/closed endpoint markers, and does not mark an optimal constant. Rule definitions and the rectangle interpretation are readable. The parameter table does not preallocate the unknown case count, and separate proof/design workspaces are ample. Guide weighted-loss and variance formulas are intact.
- **GA-19, student 5–7:** The derivative requirement is explicitly a calculus core. The common graph scale supports honest comparisons rather than rescaling every curve to look large. The exact target, quantifiers, norm change, nonattainment and integration questions remain legible and have separate workspaces. The guide's integral and norm symbols render correctly.
- **GA-20, student 8–10:** The time/position axes and signed range are correct. Initial diagrams show only required endpoints; the later required waypoint is exactly (1,4), with no optimal schedule preprinted. The finite-schedule and calculus stages have distinct gates. The guide's quadratic identities, equality conditions and waypoint extension are readable. The font-safe integral-over-[0,T] notation retains the intended interval.
- **GA-21, student 11–13:** The reflection boards have equal coordinate scale, correct A/B and legal mirror endpoints, and room to construct B′ and the crossing. The shortened interval and strict-convexity tool are explicit. Guide page 18 correctly separates the full-mirror optimum (4,0) from the constrained endpoint (2,0), with dashed reflected lines and distinct actual routes. Labels and endpoint conventions are clear.
- **GA-22, student 14–16:** Both supplied coordinate boards match their exact data. No hull, diagonal or common point is supplied prematurely. The arbitrary-arrangement grid permits new choices; the later degeneracy and affine-certificate proofs have substantial space. The moved C labels are distinct from the y-axis labels. Guide convex weights and signed-dependence formulas are intact.
- **GA-23, student 17–20:** The route arrows run A→B→C→A and are explicitly identified as route directions, leaving the carried-arrow outcomes for the learner. The frame values and empty transport ledger are readable. The variable-longitude drawing is marked schematic, and the four-page sequence preserves the spatial/vector and trigonometric gates. Guide page 30's actual corner vectors, tangent-plane return arrows and signed orientation agree with the proved map; answers remain in the guide.
- **GA-24, student 21–23:** Closed endpoints, the Y junction and the joined figure-eight have clear connection conventions, while the two disjoint loops visibly remain separate. Learners choose deletion points; no component count is disclosed by the layout. Circle and ellipse share a true coordinate scale with horizontal semiaxis doubled. The one requested repair replaces the implementation detail “1 unit = 35 points” with a plain statement that both pictures use the same coordinate scale.
- **GA-27, student 24–26:** The three unshaded closed squares, U/D labels and chosen-crossing board preserve the intended choices. The component/route proof and calculus/Hessian continuation are distinct. Worked guide page 41 clips the regions to the square, shades the correct sides, retains the joining origin at level zero and draws an attaining route through a=1/2. Moved y labels no longer compete with level headings. Boundary inclusion and the distinction from a general Morse theorem are explicit.

No missing object, answer leak, misleading geometry, clipped symbol or unusable proof workspace was found. Reviewed source/gate pages distinguish mathematical verification from unpiloted classroom claims. Awaiting the fresh caption page and unchanged-page comparison before final closure.

## Repair closure and accepted preview

Accepted report: `tmp/pdfs/atlas-remaining/ga3-preview-v4/qa/build-report.json`. The independent reviewer inspected the fresh student page 23 at full size: the caption now reads “Both pictures use the same coordinate scale.” The circle/ellipse geometry is unchanged. An independent byte comparison found exactly that one changed PNG among all 68 pages; the other 67 match v3. Fresh mechanical checks remain clean at 26 student / 42 guide pages. All findings are closed.

Student SHA-256: `bccc9ee0ebeb73ebd5f7c414bf8ae9c13a3a0db20679e9cfa2fa68cca4c67ebc`.

Guide SHA-256: `42a82b45dba9f2a13686e004149c68f97fce14096d5549263350a634dd9df357`.

This record covers reviewed preview bodies and the stated page inspections. The final assembled contents and body-identity audit are separate release steps.
