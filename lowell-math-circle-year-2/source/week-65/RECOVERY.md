# Week 65 source recovery — October 6, 2026

This is a newly packaged recovery of the authored Week 65 v2 sources. It is not the lost original ZIP or a recovered Git commit. The original PDF/ZIP bytes and local commit objects were not found after the cloud restart.

## What was restored

All textual source inputs in the original 16-file portable package were restored from complete retained authored text and exact recorded edits. No missing mathematical or layout code was silently rewritten.

- The guide's complete initial LaTeX and all later edits were replayed. Final facilitator.tex is 21,888 bytes, matching the retained final size. Its build.py, verify_geometry.py, verify_routes.py and README also match their retained sizes (813, 5,602, 1,424 and 1,471 bytes).
- The complete student builder and all v2 edits were replayed. The intermediate 23,270-byte count preceded 44 bytes of hyphenation control and the 19-byte “in both directions” addition. Final pre-cleanup size was 23,333 bytes. Applying the documented one-trailing-space cleanup gives the canonical 23,332-byte build.py. The final student README was fully retained.
- The independent mathematical reviewer's complete original 226-line checker was recovered. Its retained first 100 and final 87 lines matched the reviser's fragments byte-for-byte. Four recorded v2 replacements restore the canonical 10,327-byte checker. The 39-line gap was filled from the original authored text, not newly invented logic.
- The root build wrapper, manifest, README, original QA record and provenance note were restored from full authored text and recorded edits.

After the initial recovery snapshot was made, the original 16-file source manifest was recovered. Fifteen files match its retained SHA-256 values exactly. The remaining student/build.py matches the retained original hash after reversing the one documented trailing-space cleanup; its current content is the final cleaned form. The included original-source-hash-corroboration.json records both checks. This authenticates the source content without claiming recovery of the missing original PDF, ZIP or Git object bytes.

## What was regenerated

students.tex, checks.json and independent-checks.json are regenerated outputs from the restored exact builders/checker. They are distinguished from literal text recovery. All built-in and independent mathematical checks pass again.

Both PDFs have been newly generated from the restored sources. They again have six student pages (86,265 bytes) and seven adult pages (117,167 bytes), matching the historical page counts and sizes, but their binary hashes differ from the lost originals. No claim of original PDF-byte recovery is made. New rendering and print-scale checks remain distinct from the historical Oct 5 review.

The original QA.md is preserved as historical documentation of the October 5 release. It does not, by itself, establish equivalence between the newly generated PDFs and the lost original binaries. This recovery bundle contains the current portable source inputs plus this note and a new inventory; no downloaded artwork, private reference books or credentials are included.

## Remaining limits

The original Git objects, original ZIP bytes and original PDF bytes remain unavailable. Some broader repository review records and rendered caches are not part of this recovered portable package. The activity remains unpiloted; physical print/counter rehearsal and classroom testing were never performed.

Later verification on October 6 rendered and inspected all 13 regenerated pages and checked clean extracted-source rebuilds against the regenerated final PDFs. Those pages match in text, dimensions and pixels; no comparison to unavailable original PDF/raster bytes is claimed.
