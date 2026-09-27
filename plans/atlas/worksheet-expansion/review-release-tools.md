# Release-tool review

Independent reviewer: `worksheets_geometry`; maintainer: root. September 26, 2026.

Status: **CLOSED for the audit/index implementation.** This is not itself a release approval: the final books must still be built, visually reviewed and passed through the audit.

The reviewer read `audit_release.py` and `build_index.py` independently and identified four weaknesses. Root repaired them; the reviewer reread the edits and closed every finding.

1. Require the exact subject set and both student/facilitator records for each subject, rather than trusting whichever records happen to exist. The audit also requires each book's exact assigned family set.
2. Strip only the standard six-capital-letter PDF subset tag from font names before comparing page bodies. Preserve the actual typeface, size, geometry, characters and colors. A change in a font's embedding subset is not a visual change.
3. Require each contents start to equal the first corresponding body page, and require the actual PDF page count to equal its report, before checking links and bookmarks.
4. Compare every object intersecting the body region, including those crossing its boundary. Decoded image data are hashed when images occur; comparison is not limited to their bounding boxes.

The indexer's relative PDF paths now resolve against the repository root. Its family-span checks and generated relative links were otherwise sound. Both tools parse successfully. The end-to-end index generation and release audit subsequently passed for all eighty families, 497 prompts and six books; see [REVIEW.md](REVIEW.md) and [release-manifest.json](release-manifest.json).

The body comparison excludes the running header/footer and folio. Final contents are new material and require their own visual inspection. It does not replace the independent visual review of the batch page bodies or claim that assembled books received a second full visual pass.
