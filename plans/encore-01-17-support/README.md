# Verification support for Weeks 1–17 return visits

This directory belongs only to the new return-visit companions. The delivery inventory is [../bonus-weeks-01-17.md](../bonus-weeks-01-17.md); the detailed range inventories record prerequisites, source relationships, new-versus-base distinctions and per-week checks. Base packets and global indexes have separate owners.

All Weeks 1–17 are complete: 51 distinct investigations across 54 numbered problems, 67 student pages, 80 adult-guide pages and 17 portable source packages. [completion-checks.json](completion-checks.json) records the final aggregate checks and the physical/classroom verification limits.

Each week follows its own fresh writer, critic, independent mathematics and revision stages under `tmp/worksheet-runs/encore-week-NN-20261004-v1/`. Adult guides are developed separately, then matched to the actual final student problems. Source packages include the applicable stage reports and portable build instructions. Each coordinator runs an unrelated extracted-source build and compares every delivered page's text and rendered pixels. Trailer IDs may differ while page content is identical.

`release-status.json` records weeks whose full release checks have been reported. File presence alone is not a completed release. `build-inventory.py` additionally requires every mapped numbered problem to appear in the current student PDF. Week 12's Problems 2–3 are one investigation; its four numbered problems count as three investigations.

The following supplemental checks can be run from the repository root:

```sh
python3 plans/encore-01-17-support/independent-small-cases.py
python3 plans/encore-01-17-support/two-bounce-check.py
python3 plans/encore-01-17-support/fourth-label-check.py
python3 plans/encore-01-17-support/audit-source-packages.py
python3 plans/encore-01-17-support/audit-release-snapshots.py
python3 plans/encore-01-17-support/audit-existing-bonuses.py
python3 plans/encore-01-17-support/check-deliverables.py
python3 plans/encore-01-17-support/build-inventory.py
python3 plans/encore-01-17-support/audit-inventory-links.py
```

The final-page script requires PyMuPDF and Pillow; the inventory builder requires PyMuPDF. The other scripts use the Python standard library. In this workspace the PDF environment is `tmp/example-edit-env/bin/python`. The final-page script renders all current PDFs into `tmp/encore-01-17-final-qa/` and checks text bounds, glyphs, footers and suspiciously empty pages. Its results do **not** replace readable visual inspection. Package auditing checks safe ZIP paths, ZIP/editable-file identity and any PDF reference copies against current week-local PDFs; it does **not** execute another rebuild.

`release-snapshots.json` binds each completed release report to the two PDF hashes and its source ZIP hash. Accept a week with `audit-release-snapshots.py --accept-week NN` only after its readable review and extracted build checks. The default audit flags later byte changes that would require renewed review; it does not itself inspect or build anything.

Weeks 1–4 originally passed clean extraction builds in repository `tmp/`, with the build process working from `/tmp`. Root subsequently performed fresh extractions entirely outside the repository and compared every current student/guide page at 1.5x, preserving the released files. The resulting `week-NN-outside-rebuild.json` records supplement the earlier checks. `check-outside-rebuild.py NN` reproduces this optional check and requires PyMuPDF.

The root small-case checks independently cover Latin trades, diagonal conditions, local peaks, necklace classes, three-lamp rings and permutation square roots. The two-bounce checker uses exact rational wall-crossing times. These finite checks supplement general arguments and actual-instance checks in the guides and fresh mathematics reviews; they do not establish every theorem merely by testing small inputs.

Week 16's originally planned center-refinement activity was rejected as already present in base K–1 Problem 4. The replacement permits a fourth interior label while preserving the original three-label boundary. `fourth-label-check.py` independently audits all 256 legal four-label fillings on the three-step mesh, supplies a zero-RBY/three-distinct-triple witness, and records the general pair-door parity argument. Recoloring all fourth labels to each old label gives an elementary alternative proof that all three fourth-label triple types must occur when RBY is absent.

`base-files-snapshot.json` records the initial read-only inventory, including older bonus material. Other authorized tasks may revise base files, so a changed base hash does not attribute an edit to this task. `audit-existing-bonuses.py` separately checks the nine existing Week 1 encore/extensions and Week 2 bonus PDFs against that initial snapshot; exact hashes and results are in `existing-bonus-preservation.json`.

All new companions are unpiloted. Digital layout, mathematical verification and extracted-source rebuilds establish neither physical material fit nor classroom readiness. Material stock, handling procedures and launch timing remain untested. No remote copy, upload, publication, commit or push is claimed.
