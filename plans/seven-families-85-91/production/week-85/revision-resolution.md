# Week 85 revision resolution

Reviser stage completed 17 October 2026. Stable deliverables: `final/shared.pdf` (4 pages), `final/upper.pdf` (4 pages), `final/materials.pdf` (10 pages), editable `final/src/`, and `final/week-85-source.zip`.

## Review findings resolved

1. Both operation examples now use the genuine non-task T elbow (75,-16) -> (100,-16) -> (100,12), with O fixed at the local origin. At display scale 0.245, the T legs are 6.125 and 6.86 mm, with P legs twice those lengths. Smaller joints, thinner pale bars, 0.4 mm dark traces, start dots and offset labels keep partial strokes, completed strokes and current tips distinct. The middle control arrow points to T normally and P in reverse. Normal and reverse grayscale crops were opened and inspected. No theorem text was added.
2. Every A-M identifier moved inside its cut rectangle, clear of path geometry and registration corners. The bridge label also remains inside its border. All thirteen exact cut-border crops were rendered and inspected; text checks confirm every identifier survives. Evidence: `crop-checks.json`, `revision-renders/crops/`.
3. Removed optional G/H/I grids. Shapes and actual-size square/half-square pieces carry the area investigation without a conflicting lattice. All three grid-free inserts were inspected.
4. Shared Problem 4 names the small solid box on F and asks for its outline to be copied. F sits by that inner outline in the student reference. Its black outline is more visible. The exact 40 by 30 mm output target and 20 by 15 mm inverse are unchanged.
5. Upper Problem 3 names the small solid box on L within the numbered task, with a compact matching visual reference. Removed the separate explanatory aside. The exact 30 by 20 mm input box and 60 by 40 mm P path are unchanged.

All eight substantive tasks, copying/inverse-control entry, frame explanation, area, reverse scaling and anchor compensation remain. No activity coordinates changed other than the demonstration. No facilitator guide was edited.

## Final checks actually performed

- Compiled the 4/4/10-page PDFs without overfull diagnostics.
- Individually opened all 18 final page raster renders. The complete page-by-page content record is in `final/src/QA.md`.
- Inspected grayscale operation crops and all A-M cut-border crops. No clipped identifiers, arrow/label overlaps or remaining area grids.
- Reran the portable mathematical checker, including the three enlarged demo poses and exact F/L inverse/forward targets.
- Reran the independent review's calculations against final PDFs with only the new stroke-width matcher and grid-removal diagnostic changes. This is reviser follow-up, not a new independent review. All nine actual mechanism poses were checked. Evidence: `revision-math-recheck.py`, `revision-math-results.json`.
- Packaged only portable source files in `final/week-85-source.zip`, extracted them into `clean-extracted-rebuild`, and built with no repository assets. All three PDF hashes match the delivered PDFs exactly; generated TeX matches the packaged TeX. Evidence: `clean-rebuild-results.json`.
- `final/src/README.md` and `QA.md` describe revision-stage status and actual checks; no stale claim that independent review is still pending remains.

No printing, cutting, physical assembly, mount testing, motion/clearance rehearsal or classroom piloting was performed. The physical prototype gates remain unresolved; no remote upload or release is claimed.
