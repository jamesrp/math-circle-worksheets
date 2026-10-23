# Week 67: release verification scope

Prepared October 6, 2026 for review. Current IDs: GGT67-S-v2 and GGT67-FAC-v2 (October 23, 2026 card fixes). 5 student pages; 3 adult-guide pages.

**October 23, 2026.** The student pages are now problem files; the v2 changes are checked by `review/verify_card_fixes_2026_10_23.py` and recorded in `review/card-fixes-2026-10-23.md`. Every changed page of both PDFs was rendered and inspected, and a clean rebuild from the extracted ZIP matches every page's text and 100-dpi pixels. The rest of this note describes the October 6 v1 release.

The student packet passed an independent adversarial review followed by a fresh revision. Each final student page was rendered and visually inspected after changes; its standalone builder and mathematical checks were rerun. The adult guide is a separate stage: its author checked the exact final student questions, independently verified its answers, and rendered and inspected every guide page. Reviewer findings and revision decisions are kept with the repository's per-week review record.

The portable build runs the independent kernel/instance checks and the separate student and guide checks. Finite computation supports exact finite claims; universal claims require the assumptions and proofs in MATHEMATICS.md and the guide. The independent draft audit does not automatically certify later changed examples.

The release process extracts the actual source ZIP, rebuilds both PDFs using packaged inputs only, and compares page count, US Letter dimensions, text and every rendered page against the delivered PDFs. The machine-readable result and exact PDF/ZIP SHA-256 values are in the per-week release-checks.json record outside this package. Different TeX/font versions may alter raster appearance or metadata.

Physical preparation, material fit and partner operation have not been rehearsed. No classroom pilot has occurred. These are reviewable prototypes, not a claim of proven age fit or classroom readiness.
