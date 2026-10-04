# Week 56 independent mathematical review

Reviewed the actual nine-page `draft/students.pdf`, four-page `draft/materials.pdf`, and their actual net coordinates. Direct stage routing gives Grades 2–5 on student pages 1–6 and Grades 4–5 on pages 7–9; no separate K–1 packet is claimed. Independent solutions, proofs, PDF measurements, and code are preserved in `independent-math/math-audit.md`, `solutions.md`, `audit_math.py`, and `audit-results.json`. All thirteen pages were rendered and visually inspected. Physical assembly remains unperformed.

## Located issues

### 1. Grades 2–5, student page 3, Problem 3: closure and convexity are missing from the classification

**Exact text:** “Which groups can close into a pointed corner? Which groups lie flat? Make each group, then draw its gap with the corners laid flat.”

**Evidence:** All six specified groups can lie flat as open fans; indeed the task ends by asking children to lay every group flat. The intended distinction is between closed convex pointed corners and fans whose free sides close flat without a gap. The gaps for 3,4,5,6 triangles and 3,4 squares are 180°,120°,60°,0°,90°,0°. Only the zero-gap cases close flat. Also, without the convex condition, six equilateral triangles can close into a nonconvex pointed cone despite a 360° sum. The independent script constructs six rays with adjacent 60° angles, all above the apex, and verifies the cone is nonconvex.

**Smallest fix:** Replace the first two questions by “Which groups can close into a pointed corner with no dents? Which groups close flat with no gap?” Keep the remainder of the task.

### 2. Grades 4–5 supporting proof, research-notes.md, “Proofs and independent small checks”: deletion can merge with outside

**Location:** `plans/new-themes-52-63/week-56/research-notes.md` (supporting source note, not a student-PDF error).

**Exact text when read:** “Delete edges on cycles, each time merging two bounded regions; E and the number of bounded faces both decrease by 1.”

**Evidence:** The actual student page 7's worked example deletes the tetrahedron's three boundary edges. Each deletion merges a bounded region with the unbounded outside region. In the final deletion from any opened drawing, the final bounded face must merge with outside. Requiring two bounded regions would not allow the reduction to reach a tree. The count change is correct when either sort of region merge is allowed.

**Smallest fix:** Change “two bounded regions” to “two regions, possibly including the unbounded outside region.” Root has stated it will make this source-note correction before packaging; this reviewer has not edited the note.

### 3. Grades 4–5, student pages 7–8, Problems 7–8: the universal claims need polygon-face scope

**Exact text:** Problem 7 asks why the count is constant “for closed convex solids.” Problem 8 asks why “every closed convex solid has the same total gap.”

**Evidence:** A closed convex solid can have a curved surface, such as a ball, for which the polygonal V/E/F decomposition and planar face-corner gaps used here are not defined. The verified arguments apply to finite closed convex polyhedra, or the stated suitable polygonal sphere decomposition. The source notes give this restriction correctly, but the universal printed statements omit it. This is a scope correction, not a failure of the intended Euler/defect mathematics. Page 9's opening already specifies regular polygon faces; consistent wording there would also help.

**Smallest fix:** Use “closed convex solids with polygon faces” in the two universal prompts, or define “polyhedron” briefly and use that term. This agrees with critic R3, read only after completing the independent calculations and initial audit.

## Checked bands and materials

- **Grades 2–5, pages 1–6:** Problems 1,2,4,5,6 pass. Problem 3's computations and figures pass, with the wording correction above required.
- **Grades 4–5, pages 7–9:** All intended calculations and explanations pass, including Euler reduction, total-defect cancellation under the closed sphere assumptions, and (V,E,F)=(12,30,20)/(20,30,12) for the two regular-face cases. The universal prompts on pages 7–8 need the polygon-face scope clarification; the ancillary source-proof wording also needs the correction above.
- **Preparation assets, pages 1–4:** Pass digital mathematical checks. All five nets have correct incidence, consistent vertex labels, paired seam letters, and rigid placements into closed convex solids. All 28 net faces and 16 fan pieces have 30 mm edges in the actual PDF; the ruler is 30 mm and both circles 80 mm. Open-net counts differ correctly from assembled counts. No positive-area flat-layout overlap was found. No physical fold, tape-fit, timing, or piloting claim is made.


Record note: this is the completed authored stage report. Stage-local render/build
evidence referenced under `tmp/` is historical and is not included in source ZIPs.
Current released-file hashes and actual ZIP-extraction text/dimension/pixel checks
are recorded in `../release-checks.json`; coordinator page coverage is recorded
in `../../final-visual-review.json`. Physical pretests and piloting remain unperformed.
