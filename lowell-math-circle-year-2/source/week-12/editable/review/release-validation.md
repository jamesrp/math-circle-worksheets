# Portable release validation

2026-10-03 visual and mathematical revision (W12 student version 3).

The revised ZIP was extracted into a fresh directory whose path contains spaces. Its build regenerated all four PDFs. The rebuilt files match the reviewed revised references in page count, US Letter media size, extracted text and every page's 100-dpi grayscale pixels. Binary differences from PDF timestamps or document IDs are not displayed content.

PASS k-1.pdf: 6 Letter pages; identical extracted text and 100-dpi grayscale pixels.
PASS grades-2-3.pdf: 6 Letter pages; identical extracted text and 100-dpi grayscale pixels.
PASS grades-4-5.pdf: 6 Letter pages; identical extracted text and 100-dpi grayscale pixels.
PASS facilitator-guide.pdf: 9 Letter pages; identical extracted text and 100-dpi grayscale pixels.
PASS: all 27 pages match. Byte differences from timestamps/document IDs are allowed only because content matches.

All 18 student pages and nine adult-guide pages were rendered and independently inspected. All seven physical-mat overlays were checked with 20 mm endpoint discs; the minimum measured label clearance is 0.631 mm. Independent perfect-matching enumeration verifies Catalan counts through six pairs, fixed-chord cases, the neighbor condition and the new representation examples.

Validation used TeX Live 2025 and its installed packages, with temporary TeX search settings and a format outside the ZIP because this container's home configuration is read-only. No test-environment settings or binaries are shipped. A normal working TeX Live/MacTeX installation supplies those distribution-level settings.

The four reference PDFs are byte-identical to the delivered PDFs. The source ZIP retains the original portable file set with updated generators, generated LaTeX, example checks, physical-layout checks, README, outline, manifest and reviewed references. New scratch reports, logs, render images, caches, dependencies and TeX formats are excluded. Earlier narrative review files are historical project records, not evidence of classroom testing.
