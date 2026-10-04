# Catalan facilitator guide

Draft and unpiloted adult guide; library slot 12 is not a calendar commitment.

Run `python3 check_math.py` then `python3 build_guide.py` from this directory. Dependencies: reportlab and a DejaVu Sans system font (fallback Helvetica). Output: ../facilitator-guide.pdf (8 US Letter pages).

The independent checker generates all perfect matchings before filtering crossings; it does not import the student generator. It checks counts 1,1,2,5,14,42,132 and reversible tree/pairing maps, fixed-pair completions and the neighbor claim. `math-checks.json` preserves the full enumerations.

QA 2026-10-03: final student sources/PDF text and all 18 student-page renderings reviewed; final guide rendered at 70 dpi and every page individually inspected. All 18 numbered student problems covered, diagrams checked against exact codes. No student files edited. The guide is 8 pages with no observed clipping, overlap or missing glyphs. `qa/` retains the inspected images.
