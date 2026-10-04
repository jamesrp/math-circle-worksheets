# Route packing facilitator guide

Separate adult guide, draft and unpiloted. Library slot 13 is not a scheduled meeting.

Run `python3 check_math.py` and `python3 build_guide.py` here. All file paths are relative to __file__. Python dependencies: reportlab; DejaVu Sans optional with Helvetica fallback. Output: ../facilitator-guide.pdf, 9 US Letter pages.

Final student mapping: K-1 has 6 pages / Problems 1-6; grades 2-3 has 7 pages / Problems 1-6 (page 6 is an unnumbered clean recording copy); grades 4-5 has 7 pages / Problems 1-7 (page 2 is an unnumbered clean recording copy; Problems 6-7 share page 7).

Independent exact reconstruction and exhaustive search did not run/import the student generator. It enumerates simple directed routes, edge-disjoint collections, minimum closures, all game states, relevant cut partitions and residual reachability. The revised coupled trap has nine routes, two maximum collections, and the unique augmentation s-B-A-C-E-D-t with cancellations AB and DE. Full results are math-checks.json.

QA 2026-10-03: all 20 final student-page renderings reviewed against source definitions. Adult PDF rendered at 70 dpi; all nine final pages individually inspected after pagination repair. No observed clipping, overlap, missing arrows or glyph defects. Exact numbered keys cover all 19 student problems. No student pages were changed. qa/ preserves renders.
