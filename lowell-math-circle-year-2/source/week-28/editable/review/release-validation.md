# Portable release validation

2026-10-03 guidance revision. The source ZIP was extracted into a directory whose path contains spaces. The portable build completed with the documented Python dependencies and TeX Live 2025. The complete revised PDFs matched their current references in page count, US Letter media size, extracted text and every page's 100-dpi grayscale pixels. The new unnumbered overview is included in the guide count; older detailed-guide QA records cover the following numbered body.

PASS k-1.pdf: 6 Letter pages; identical extracted text and 100-dpi grayscale pixels.
PASS grades-2-3.pdf: 6 Letter pages; identical extracted text and 100-dpi grayscale pixels.
PASS grades-4-5.pdf: 6 Letter pages; identical extracted text and 100-dpi grayscale pixels.
PASS facilitator-guide.pdf: 17 Letter pages; identical extracted text and 100-dpi grayscale pixels.
PASS: all 35 pages match. Byte differences from timestamps/document IDs are allowed only because content matches.

The container required temporary TeX distribution-search and writable-cache settings outside the package. No runtime formats, fonts, caches, rendered images, logs or environment-specific settings are bundled. A normal working TeX Live or MacTeX installation supplies its own distribution configuration.

Unchanged student PDFs retain the exact preceding-release bytes. Targeted new examples leave student page and numbered-problem counts unchanged. The original long proofs and solutions follow the concise overview. Draft, unpiloted and prerequisite limitations remain in force.
