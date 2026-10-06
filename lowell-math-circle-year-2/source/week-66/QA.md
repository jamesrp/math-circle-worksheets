# Week 66: release verification scope

Prepared October 6, 2026 for review. Current IDs: GGT66-S-v1 and GGT66-FAC-v1. 4 student pages; 2 adult-guide pages.

The student packet passed an independent adversarial review followed by a fresh revision. Each final student page was rendered and visually inspected after changes; its standalone builder and mathematical checks were rerun. The adult guide is a separate stage: its author checked the exact final student questions, independently verified its answers, and rendered and inspected every guide page. Reviewer findings and revision decisions are kept with the repository's per-week review record.

The portable build runs the independent kernel/instance checks and the separate student and guide checks. Finite computation supports exact finite claims; universal claims require the assumptions and proofs in MATHEMATICS.md and the guide. The independent draft audit does not automatically certify later changed examples.

The release process extracts the actual source ZIP, rebuilds both PDFs using packaged inputs only, and compares page count, US Letter dimensions, text and every rendered page against the delivered PDFs. The machine-readable result and exact PDF/ZIP SHA-256 values are in the per-week release-checks.json record outside this package. Different TeX/font versions may alter raster appearance or metadata.

Physical preparation, material fit and partner operation have not been rehearsed. No classroom pilot has occurred. These are reviewable prototypes, not a claim of proven age fit or classroom readiness.
