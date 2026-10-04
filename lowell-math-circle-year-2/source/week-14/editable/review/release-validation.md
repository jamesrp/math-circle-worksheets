# Release validation

Regular-polygon-board revision prepared October 3, 2026, from the regular-hexagon and explicit-continuation revision. Draft and unpiloted.

PDF page counts are unchanged: K–1 6, Grades 2–3 8, Grades 4–5 7, facilitator guide 13. The student packets contain 6, 7, and 7 distinct problems respectively, totaling 20. Grades 2–3 page 8 remains explicitly marked as Problem 7 continued and supplies nine extra recording hexagons, for 17 recording outlines across the two Problem 7 pages.

All 171 student working and recording boards are now regular polygons: 63 pentagons, 92 hexagons, 3 heptagons, and 13 octagons. The guide has 54 already regular polygon boards. The 79 previously stretched student pentagons, heptagons and octagons now use one physical coordinate scale, fitting inside their former layout boxes. The 92 student hexagons and all guide boards retain exactly their former coordinates. All labels, diagonal sets, and recording copies are preserved.

Six intentional general convex quadrilaterals remain unchanged: four small AC-to-BD student flip examples and two local close-ups in the guide's fan-distance proof on page 11. Triangles and quadrilaterals formed inside a triangulation need not be regular. The source geometry checker now covers every regular board and all six general examples.

Physical PDF-vector checks cover all 225 regular boards, with equal sides and the expected interior angles within rounding tolerance. Maximum side spread is 0.0113 point and maximum interior-angle error is 0.0167 degree. All six general examples have exactly their previous PDF vertex coordinates. The shared generator was also tested on triangle through dodecagon outlines in 40 combinations of polygon size and bounding-box proportions.

The 14 changed pages were rendered and inspected: K–1 1, 2, 4, 6; Grades 2–3 1, 2, 4, 5; Grades 4–5 1, 3, 5, 6, 7; guide 2. All other 20 pages are pixel-identical to the preceding release, including the theorem-first guide overview and both Problem 7 pages. Student text and problem topology are unchanged. The guide's only wording change says that all student polygon boards are regular. Mathematical enumeration and distance checks still pass.

Independent geometry and page review passed. The source ZIP was extracted into a separate directory whose path contains spaces and rebuilt through its top-level build.sh. verify_rebuild.py passed all reference hashes, page counts, Letter page sizes, extracted text, and every page's 100-dpi grayscale pixels across all 34 pages. PDF timestamps or object identifiers may differ without affecting displayed content.

The portable package requires the normal TeX dependencies listed in README.md. Local sandbox TeX search-path overrides and format files are kept outside the ZIP. No absolute workspace paths or downloaded runtime files are required by the source.

Earlier student-review and facilitator-review records and the regular-hexagon geometry report are historical. The current scope and geometry are described here and in README.md and regular-polygons-geometry-checks.json.
