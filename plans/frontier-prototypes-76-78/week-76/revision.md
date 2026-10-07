# Week 76 revision record

- Adopted R1: Problem 4 explicitly allows at most one lone tile at each end. Replaced BBAAB with the genuine crop AABB, whose unique pairing leaves one tile at both ends and retains parent A. Updated the checker accordingly.
- Adopted R2: Problem 7 now names the single endless strip made by growing from A.
- Declined findings: none. The independent mathematical review required no corrections. Preserved the four-page, seven-problem structure and the distinction between whole rows and crops.
- Verification: the standard-library math checker passed; the changed AABB case was also checked independently in a generated row. Both direct and clean ZIP-extracted source builds passed without overfull boxes. Rendered and inspected every page of both builds at 130 dpi; all four page images match exactly, with correct diagrams and no clipping or overlaps. Final output: four US Letter pages, 95,388 bytes.
- Sources remain four portable files. No guide, generated formats, external assets, or prompts were added to them. Physical handling, timing, and classroom use remain untested. No commits or pushes were made.
