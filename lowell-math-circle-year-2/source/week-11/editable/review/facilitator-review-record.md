# Chip firing facilitator guide

Draft and unpiloted. Week 11 is an unscheduled library slot.

- Output: `../facilitator-guide.pdf` (9 US Letter pages).
- Editable content: `build_guide.py`, generated `facilitator-guide.tex`.
- Rebuild: `bash build.sh` from this directory or by full path.
- Independent mathematics: `verify.py`, `checks.json`, `verification.log`. The verifier does not import worksheet code. It branches through every legal successor for all assigned starts; each has a unique final state and firing-count vector. It also checks repeated additions and both batch orders.
- Visual QA: all 9 pages rendered at 90 dpi and inspected individually on 2026-10-03. No clipping, overlap, missing glyph, or overflow found. Build log has no overfull/underfull/missing-character warnings.
- Source fidelity: all 18 final numbered problems have keyed answers; source provenance and scope limits are printed on page 9. Student PDFs and their sources were not edited.

Final student PDF SHA256 values used for this guide:
- k-1.pdf: 4a55bb44287a884f5f4dafd5846e0294328dee8e372bab4285fc9ef6b9ab1655
- grades-2-3.pdf: 723d922cc4ccc580b8d430b14f0663c6058f9c226471f1cca820ac484dd54f04
- grades-4-5.pdf: 2c78307cabd03983e513b8de35ee90d9d7f8d25251fe85f207278a2f10366c01
