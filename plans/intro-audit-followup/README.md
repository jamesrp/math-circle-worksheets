# Introduction audit: implemented follow-up

Implemented the eight targeted findings from the [Weeks 1–75 audit](../intro-audit-2026-10-17/README.md): **11 student PDFs and 6 facilitator PDFs**, with current sources, reference copies and eight source ZIPs synchronized. Every revised PDF retains its previous page count. The later investigations and upper-band mathematical substance remain.

| Week and packet | Student pages | Implemented change | Current PDF |
|---|---|---|---|
| 1 encore, Grades 4–5 | 4 | A single cube with faces 1–3 is matched to the same faces in empty corner A after adding that cube. The adult launch uses a real snap cube in the same view. The full-size board and ten recording copies remain; two small copies make room for the bridge. | [Upper packet](../../lowell-math-circle-year-2/week-01-encore/week-01-encore-grades-4-5.pdf) |
| 6, Grades 4–5 | 1–2 | Number guessing starts without unrelated code-game rules. Concise game rules now appear with Problem 2 and its board. Four test rows remain; gaps are closer, with unchanged circle, triangle and score-box sizes. | [Upper packet](../../lowell-math-circle-year-2/week-06/week-06-grades-4-5.pdf) |
| 22, all three bands | 1 | Four labels → two explicit groups → both regions with their shared point circled. The original point/segment/triangle definitions and 12.6 cm working boards remain. The guide demonstrates the same successful split. | [K–1](../../lowell-math-circle-year-2/week-22/week-22-k-1.pdf), [2–3](../../lowell-math-circle-year-2/week-22/week-22-grades-2-3.pdf), [4–5](../../lowell-math-circle-year-2/week-22/week-22-grades-4-5.pdf) |
| 35, Grades 2–3 and 4–5 | 1–2 | The glide demonstration moves from the opening slide-only task to the first glide task. Both working strips remain 6 cm high. Guide packet identifiers are synchronized. | [2–3](../../lowell-math-circle-year-2/week-35/week-35-grades-2-3.pdf), [4–5](../../lowell-math-circle-year-2/week-35/week-35-grades-4-5.pdf) |
| 42 bonus, Grades 2–5 | 3 | “Whole pair fair” becomes an explicit question about all four shape pairs being equally likely. | [Bonus](../../lowell-math-circle-year-2/week-42/week-42-bonus.pdf) |
| 45 bonus, Grades 4–5 | 2 | One shared input—choose 1, prize 2, ticket 2—shows Host A opening 3 and a winning switch, and Host B opening 2 and discarding the prize reveal. Numeric labels stay consistent with the children's table. Guide launch matches. | [Bonus](../../lowell-math-circle-year-2/week-45/week-45-bonus.pdf) |
| 61, Grades 2–5 | 2 | Student rules name concrete actions and the smaller inside corners. The precise hemisphere restriction stays in the adult guide, with an operational check. No target right-angle triangle is supplied. | [Student packet](../../lowell-math-circle-year-2/week-61/week-61-students.pdf) |
| 69, Grades 4–5 | 2 | One complete road triangle demonstrates the comparison: P is one step from the green side and two from blue, so its gap is 1. Line styles distinguish the sides without color. Guide launch matches. | [Student packet](../../lowell-math-circle-year-2/week-69/week-69-students.pdf) |

Optional watchpoints from the audit are unchanged. The separate Weeks 78/80/81/82 and new-activity work were not edited.

## Verification

- Rendered and inspected the revised student pages in every affected band and companion, the changed guide pages, and other pages with rendering differences. Checked paper dimensions and page counts across all 17 PDFs.
- Clean builds from all eight extracted source ZIPs passed. All **124 pages** in the 17 delivered PDFs match those builds in extracted text, paper dimensions and 100-dpi pixels. [Per-page rebuild evidence](clean-rebuild-comparison.json) and [current-file hashes](verification.json) record the result.
- Untouched print PDFs remain byte-identical. The new Week 6 package also reproduces K–1 and Grades 2–3 exactly. Its untouched guide rebuild has existing font/minus-glyph rendering differences; the untouched encore K–1/2–3 rebuilds have drawing-order pixel differences with identical extracted text. Those older print files were retained, and the exact-reproduction claim above is specifically for the 17 revised PDFs.
- Ran the existing mathematical checks for the affected packages: exact convex-region configurations, glide motif/symmetry checks, bonus finite-history enumerations, spherical geometry and covering calculations, and road-triangle kernels. The encore's existing fast check reconstructs the new shaded pictures as exactly one cube and verifies the 20-pile distribution and flip distances; its unrelated exhaustive 4-by-4 placement-game search was not repeated.
- [Targeted checks](verify_introductions.py) independently verify the complete crossing, both host outcomes, both road distances, unchanged Week 6 piece-outline sizes/counts, and unchanged Week 22/35 board dimensions.
- Fixed two build portability issues encountered: Week 6 now resolves the same TeX Gyre Heros fonts by filename; Week 35 preview rendering is optional when Poppler is absent. The encore build fixes Python's hash seed and orders its rhombus rendering so repeat builds are deterministic. New portable builders and ZIPs are supplied for the encore and Week 6.

Previous print PDFs and existing source ZIPs are retained in separate `archive-before-intro-followup/` folders. Original loose source history remains in Git before this follow-up. The old combined fall sets are already archived and explicitly marked obsolete in the collection README; no current combined set incorporates these revised weekly PDFs. No archived combined set was rewritten. No Drive upload was performed.

These changes remain **unpiloted**. Printed material handling, including the closer Week 6 row spacing and the snap-cube viewing demonstration, has not been physically rehearsed.

## Editable packages

[Week 1 encore](../../lowell-math-circle-year-2/source/week-01-encore-source.zip) · [Week 6](../../lowell-math-circle-year-2/source/week-06-source.zip) · [Week 22](../../lowell-math-circle-year-2/source/week-22/four-point-convex-partitions-week22-editable-source.zip) · [Week 35](../../lowell-math-circle-year-2/source/week-35/glide-borders-week35-editable-source.zip) · [Week 42 bonus](../../lowell-math-circle-year-2/source/week-42-bonus-source.zip) · [Week 45 bonus](../../lowell-math-circle-year-2/source/week-45-bonus-source.zip) · [Week 61](../../lowell-math-circle-year-2/source/week-61-source.zip) · [Week 69](../../lowell-math-circle-year-2/source/week-69-source.zip)
