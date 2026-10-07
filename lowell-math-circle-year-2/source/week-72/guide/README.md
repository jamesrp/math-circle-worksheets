# Week 72 adult guide

This is the separate guide for the final GGT72-S-v1 student prototype.

## Build

Requires Python 3 and pdfLaTeX with geometry, fontenc, lmodern, amsmath, amssymb, TikZ, array, fancyhdr and hyperref.

From any working directory:

    python3 /path/to/guide-src/check_math.py
    python3 /path/to/guide-src/build.py --out /path/to/output

The builder runs the independent standard-library answer checks, then writes facilitator.pdf and guide-build.log. The source directory is self-contained; it needs no repository files, downloaded references, or machine-specific setup script. The default output directory is the source directory's parent.

The final guide is three letter-size pages. Every page was rendered and visually inspected; no overflow warnings remained. A source-only isolated rebuild from an unrelated working directory passed and matched the delivered PDF's extracted text.

The student source was not modified. Mathematical/print verification does not establish physical readiness or classroom suitability. The prototype is unpiloted, and no physical rehearsal was performed. Source lineage and proof limits are stated in the guide.
