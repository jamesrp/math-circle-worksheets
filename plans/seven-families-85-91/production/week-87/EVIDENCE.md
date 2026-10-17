# Evidence map

Fresh writer87 → critic87 → math87 → revise87 stages ran separately in the isolated week87-stages checkout. The coordinator separately authored the guide; the root independently reviews the final student–guide pair. `math-audit/` and `revision-audit/` preserve stage-specific code and compact results; their original relative paths describe the generated workflow run and are historical. Render images, raw logs and private resources are excluded.

For a reproducible check of the published material geometry, run `check_final_pdf_geometry.py` with Python and PyMuPDF from any working directory. It locates the canonical Week87 PDFs relative to this repository and verifies actual PDF vectors without importing the builder. `final-pdf-geometry.json` records measurements and hashes. The portable package itself needs only standard-library Python and TeX.

The final release audit, unlike the earlier student-only stage audit, includes the separately authored guide and all five PDFs. Physical assembly, cutting, placement and classroom testing remain untested.
