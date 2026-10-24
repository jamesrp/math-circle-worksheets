# Source-ZIP sweep

Clean-rebuild sweep of every current portable source ZIP, October 24, 2026, after the October 23 revisions (problem-file conversions, card and critic fixes, the footer sweep and check-script repairs). A current ZIP is any `.zip` under `lowell-math-circle-year-2/source/` outside `archive*/` folders: 143 ZIPs holding 6,074 files. The sweep ran on `origin/main` at 1706100, with the Week 83 fix below.

**How to run.** From the project root, with the tool in [`lowell-math-circle-year-2/source/zip-sweep/zip_sweep.py`](../../../lowell-math-circle-year-2/source/zip-sweep/zip_sweep.py):

```sh
T=lowell-math-circle-year-2/source/zip-sweep/zip_sweep.py
python3 $T contents          # each member against the file it packages now
python3 $T build --jobs 2    # clean rebuild of every ZIP, two at a time
python3 $T links             # index and README links to ZIPs
python3 $T coverage          # print PDFs no ZIP rebuilds
python3 $T report --regenerated week-83-source.zip --organizer 1 1e 2 15 "1 return visit" "2 return visit" "15 return visit"
```

Results go to `tmp/zip-sweep/`. One ZIP: `python3 $T build week-83`. The whole build pass takes about 25 minutes.

**Method.**
- *Contents.* Each member is compared byte for byte with the file it packages now. The 90 ZIPs written by `problem-files/package.py` are checked against `package.py`'s own inclusion rules, so any file that repackaging would add or drop shows up. The problem-file tools copy is reported separately: [problem-files/README.md](../../../lowell-math-circle-year-2/source/problem-files/README.md#a-week-with-an-editable-package) says a ZIP keeps the tools of the day it was packaged and is repackaged when its week changes. The 53 other ZIPs (return visits 1–17, bonus companions 18–51, Week 15 and Week 1e) map `<top>/<path>` to their folder, skipping `archive*/`, ZIPs and build folders. Each ZIP's reference PDFs were matched against the print copies.
- *Clean rebuild.* Each ZIP is extracted into a fresh folder under `tmp/zip-sweep/builds/` and built with the package's own command, read from its README: `python3 build.py` (given `--out` and `--work` when it takes them; 108 ZIPs), `bash build.sh` (the 18 packages of Weeks 11–28) or `sh build.sh OUT` (the 17 return visits). Each build ran in Linux user, mount and network namespaces, with no network and `/home` replaced by an empty folder except the extraction. A build that needed the checkout, another package or a download would have failed. Nothing was installed. The toolchain was TeX Live 2023 (pdfTeX 1.40.25, XeTeX), Python 3.13, ReportLab 5.0.1, pypdf 6.17, PyMuPDF 2.0 and Poppler. The packages' own verifiers were not run. Each verifier compares against the package's reference copies, and those all equal the print copies the sweep compared with.
- *Comparison.* Every PDF a build wrote, apart from reference copies and extra intermediate copies of the same PDF, was matched by name to the committed print PDF. The comparison covers page count, `pdftotext` text with dates masked, and 50-dpi greyscale renders, where a pixel differs if its grey level differs by more than 40. PDFs that were not byte-identical were also compared at 100 dpi, by word positions and vector drawings (PyMuPDF), and against git history: the source commits after the print PDF's last commit.
- *Links.* The script scans the print indexes, `source/README.md` and every week README in `source/` for Markdown links to ZIPs.

**Status.**
- Contents: *ok* means every member is byte-identical to the file it packages, and the packager would add nothing. *regenerated* means the ZIP was stale and this sweep rewrote it.
- Rebuild: *exact* means every PDF is byte-identical to the print copy. *same render* means the same pages and text with no differing pixel at 50 dpi, though the files are not byte-identical. *toolchain* means the same pages and the same text, apart from the spacing and glyph of minus signs, with the same number of vector drawings on every page. The print copy came from a different producer, pdfTeX 1.40.27 (TeX Live 2025) in every case.

**Result.** All 143 ZIPs built, offline and from the package alone, and no rebuilt PDF differs in content from its print copy. Contents: 142 ok and 1 regenerated (Week 83). Rebuilds: 45 exact, 68 same render and 30 toolchain; none failed or differed. Of 414 rebuilt PDFs, 172 are byte-identical, 206 have the same render and 36 differ only by toolchain. All 383 reference PDFs inside the ZIPs are byte-identical to the print copies. So are the 46 approved Week 2 catalog examples in Weeks 29–51 (two per ZIP), checked against `week-02/`. No member is a build intermediate, cache, log, private record or downloaded reference. Links: no broken ZIP link. Two ZIPs, Week 1e and Week 6, were linked from no index or README, only from `plans/intro-audit-followup/README.md`; both are linked now.

**Fixed.**
- **Week 83.** In ff74daa, `editable/README.md` was edited ("8 pages since the October 23 card fixes") after the ZIP had been written, so the ZIP held the older sentence. The ZIP was rewritten with `package.py`: the same 27 member paths, every member now byte-identical to the source, and the tools copy current. Re-extracted and rebuilt, both PDFs are byte-identical to the print copies.
- **Links.** `source/README.md` now links `week-01-encore-source.zip` and `week-06-source.zip`. Week 6's own README names its ZIP in code formatting rather than as a link. It was left as it is: that README is packaged in the ZIP, so editing it would make the ZIP stale.

**Toolchain differences, not drift.** Thirty-six print PDFs in 30 ZIPs were built with pdfTeX 1.40.27 (TeX Live 2025) outside this container: return visits 1–7, 9–13 and 15, bonus companions 18–21 and 24–34, Week 27 K–1, and the Week 1e guide and Grades 4–5 packet. This container's pdfTeX 1.40.25 reproduces all 36 with the same pages, words and drawings, and these differences remain:
- Most show glyph-edge differences only: words move less than 0.3 pt, and 36–1,153 pixels differ at 100 dpi.
- In four PDFs, table rows that combine `p{}` columns with `\arraystretch` are taller in TeX Live 2025, so everything below them moves: Week 30 bonus p. 1 (up to 29 pt), Week 20 bonus pp. 1 and 5, return visit 11 p. 2 and return visit 15 pp. 3–4. On the rendered pages, inspected, the cells, labels and figures are the same; only their vertical positions move.
- In the Week 1e guide (pp. 5 and 8), TeX Live 2025 sets the math minus sign as U+2212, while TeX Live 2023 gives an en dash with wider spacing, so the rest of each such line shifts.

For every one of the 36, git shows that the student source did not change after the PDF's last commit. For 21 of them the package folder did change later, but only in guide sources, or, for Week 27, in the problem-file conversion, which left `k-1.tex` unchanged. These are toolchain differences, not unbuilt revisions. No PDF was rebuilt, since rebuilding here would replace TeX Live 2025 print copies with TeX Live 2023 copies without any change in content. A byte-identical rebuild of these 36 needs TeX Live 2025.

**Not covered.** 414 of the 456 current PDFs in the week print folders are rebuilt from a ZIP. The other 42 belong to weeks with no portable ZIP: Week 1 (7 PDFs), Week 2 (6), and the main packets of Weeks 3–5 and 7–10, including `week-08-materials.pdf`. These build from in-repository `build.sh` scripts and were not checked here.

**Tools copies.** Seventy-two ZIPs carry `problem-files/tools/README.md` and `build.py` from before cd977c0 (the `page_map` key option). That is expected under the repackaging rule above. None of these weeks sets `page_map` (only Weeks 12, 13, 14, 25 and 42 do, and their ZIPs have current tools). Every clean rebuild above used the packaged copies, and the packaged tools also built every problem-file view for Weeks 11 and 52, which were sampled.

**Waits for the organizer.** Nothing that needs a decision, so nothing was added to [ORGANIZER-QUEUE.md](../ORGANIZER-QUEUE.md). Weeks 1, 1e, 2 and 15 were checked and not modified. Their five ZIPs are ok: Week 1e, return visits 1, 2 and 15, and Week 15. Their rebuilds match, with Week 1e and return visits 1, 2 and 15 matching up to toolchain. The only change touching them is the new link to the Week 1e ZIP in `source/README.md`, which is an index, not the week's own files.

| Week | ZIP | Contents | Rebuild | Note |
|---|---|---|---|---|
| 1e | `week-01-encore-source.zip` | ok | toolchain | 2 same render; week-01-encore-facilitator.pdf toolchain: 8743 px at 100 dpi, shifts up to 2.8 pt, minus signs extract as en dashes; week-01-encore-grades-4-5.pdf toolchain: 109 px at 100 dpi, shifts up to <0.1 pt; organizer week: checked, not modified; no index or README linked it; linked from source/README.md now |
| 1 return visit | `week-01-return-visit-source.zip` | ok | toolchain | week-01-return-visit-facilitator.pdf toolchain: 993 px at 100 dpi, shifts up to 0.2 pt; week-01-return-visit.pdf toolchain: 126 px at 100 dpi, shifts up to <0.1 pt; organizer week: checked, not modified |
| 2 return visit | `week-02-return-visit-source.zip` | ok | toolchain | week-02-return-visit-facilitator.pdf toolchain: 961 px at 100 dpi, shifts up to 0.1 pt; week-02-return-visit.pdf toolchain: 37 px at 100 dpi, shifts up to <0.1 pt; organizer week: checked, not modified |
| 3 return visit | `week-03-return-visit-source.zip` | ok | toolchain | week-03-return-visit-facilitator.pdf toolchain: 706 px at 100 dpi, shifts up to 0.2 pt; week-03-return-visit.pdf toolchain: 36 px at 100 dpi, shifts up to <0.1 pt |
| 4 return visit | `week-04-return-visit-source.zip` | ok | toolchain | week-04-return-visit-facilitator.pdf toolchain: 478 px at 100 dpi, shifts up to 0.1 pt; week-04-return-visit.pdf toolchain: 106 px at 100 dpi, shifts up to <0.1 pt |
| 5 return visit | `week-05-return-visit-source.zip` | ok | toolchain | 1 same render; week-05-return-visit.pdf toolchain: 95 px at 100 dpi, shifts up to <0.1 pt |
| 6 | `week-06-source.zip` | ok | same render | 2 byte-identical; 2 same render; tools copy older than source/problem-files; no index or README linked it; linked from source/README.md now |
| 6 return visit | `week-06-return-visit-source.zip` | ok | toolchain | 1 same render; week-06-return-visit.pdf toolchain: 237 px at 100 dpi, shifts up to <0.1 pt |
| 7 return visit | `week-07-return-visit-source.zip` | ok | toolchain | 1 same render; week-07-return-visit.pdf toolchain: 109 px at 100 dpi, shifts up to <0.1 pt |
| 8 return visit | `week-08-return-visit-source.zip` | ok | same render | 2 same render |
| 9 return visit | `week-09-return-visit-source.zip` | ok | toolchain | week-09-return-visit-facilitator.pdf toolchain: 975 px at 100 dpi, shifts up to <0.1 pt; week-09-return-visit.pdf toolchain: 92 px at 100 dpi, shifts up to <0.1 pt |
| 10 return visit | `week-10-return-visit-source.zip` | ok | toolchain | 1 same render; week-10-return-visit.pdf toolchain: 1153 px at 100 dpi, shifts up to 0.1 pt |
| 11 | `week-11/chip-firing-week11-editable-source.zip` | ok | same render | 4 same render; tools copy older than source/problem-files |
| 11 return visit | `week-11-return-visit-source.zip` | ok | toolchain | 1 same render; week-11-return-visit.pdf toolchain: 8475 px at 100 dpi, shifts up to 13.6 pt |
| 12 | `week-12/catalan-bijections-week12-editable-source.zip` | ok | same render | 1 byte-identical; 3 same render |
| 12 return visit | `week-12-return-visit-source.zip` | ok | toolchain | 1 same render; week-12-return-visit.pdf toolchain: 53 px at 100 dpi, shifts up to <0.1 pt |
| 13 | `week-13/route-packing-week13-editable-source.zip` | ok | same render | 1 byte-identical; 3 same render |
| 13 return visit | `week-13-return-visit-source.zip` | ok | toolchain | 1 same render; week-13-return-visit.pdf toolchain: 59 px at 100 dpi, shifts up to <0.1 pt |
| 14 | `week-14/triangulations-week14-editable-source.zip` | ok | same render | 1 byte-identical; 3 same render |
| 14 return visit | `week-14-return-visit-source.zip` | ok | same render | 2 same render |
| 15 | `week-15/nearest-sites-week15-editable-source.zip` | ok | same render | 4 same render; organizer week: checked, not modified |
| 15 return visit | `week-15-return-visit-source.zip` | ok | toolchain | 1 same render; week-15-return-visit.pdf toolchain: 13660 px at 100 dpi, shifts up to 15.5 pt; organizer week: checked, not modified |
| 16 | `week-16/three-color-triangles-week16-editable-source.zip` | ok | same render | 1 byte-identical; 3 same render; tools copy older than source/problem-files |
| 16 return visit | `week-16-return-visit-source.zip` | ok | same render | 2 same render |
| 17 | `week-17/finite-state-memory-week17-editable-source.zip` | ok | same render | 2 byte-identical; 3 same render; tools copy older than source/problem-files |
| 17 return visit | `week-17-return-visit-source.zip` | ok | same render | 2 same render |
| 18 | `week-18/error-correcting-codebooks-week18-editable-source.zip` | ok | same render | 1 byte-identical; 3 same render; tools copy older than source/problem-files |
| 18 bonus | `week-18-bonus-source.zip` | ok | toolchain | 1 same render; week-18-bonus.pdf toolchain: 98 px at 100 dpi, shifts up to <0.1 pt |
| 19 | `week-19/subset-antichains-week19-editable-source.zip` | ok | same render | 1 byte-identical; 4 same render; tools copy older than source/problem-files |
| 19 bonus | `week-19-bonus-source.zip` | ok | toolchain | 1 same render; week-19-bonus.pdf toolchain: 118 px at 100 dpi, shifts up to <0.1 pt |
| 20 | `week-20/averaging-maximum-principle-week20-editable-source.zip` | ok | same render | 1 byte-identical; 3 same render; tools copy older than source/problem-files |
| 20 bonus | `week-20-bonus-source.zip` | ok | toolchain | 1 same render; week-20-bonus.pdf toolchain: 27152 px at 100 dpi, shifts up to 18.8 pt |
| 21 | `week-21/shortest-reflected-paths-week21-editable-source.zip` | ok | same render | 1 byte-identical; 3 same render; tools copy older than source/problem-files |
| 21 bonus | `week-21-bonus-source.zip` | ok | toolchain | 1 same render; week-21-bonus.pdf toolchain: 121 px at 100 dpi, shifts up to <0.1 pt |
| 22 | `week-22/four-point-convex-partitions-week22-editable-source.zip` | ok | same render | 1 byte-identical; 3 same render; tools copy older than source/problem-files |
| 22 bonus | `week-22-bonus-source.zip` | ok | same render | 2 same render |
| 23 | `week-23/sorting-networks-week23-editable-source.zip` | ok | same render | 2 byte-identical; 3 same render |
| 23 bonus | `week-23-bonus-source.zip` | ok | same render | 2 same render |
| 24 | `week-24/nontransitive-dice-week24-editable-source.zip` | ok | same render | 1 byte-identical; 3 same render; tools copy older than source/problem-files |
| 24 bonus | `week-24-bonus-source.zip` | ok | toolchain | 1 same render; week-24-bonus.pdf toolchain: 108 px at 100 dpi, shifts up to <0.1 pt |
| 25 | `week-25/discrete-tomography-week25-editable-source.zip` | ok | same render | 1 byte-identical; 3 same render |
| 25 bonus | `week-25-bonus-source.zip` | ok | toolchain | 1 same render; week-25-bonus.pdf toolchain: 85 px at 100 dpi, shifts up to <0.1 pt |
| 26 | `week-26/polyomino-perimeter-week26-editable-source.zip` | ok | same render | 1 byte-identical; 3 same render; tools copy older than source/problem-files |
| 26 bonus | `week-26-bonus-source.zip` | ok | toolchain | 1 same render; week-26-bonus.pdf toolchain: 92 px at 100 dpi, shifts up to <0.1 pt |
| 27 | `week-27/stable-matching-week27-editable-source.zip` | ok | toolchain | 2 byte-identical; 2 same render; week-27-k-1.pdf toolchain: 139 px at 100 dpi, shifts up to <0.1 pt; tools copy older than source/problem-files |
| 27 bonus | `week-27-bonus-source.zip` | ok | toolchain | 1 same render; week-27-bonus.pdf toolchain: 61 px at 100 dpi, shifts up to <0.1 pt |
| 28 | `week-28/single-vertex-flat-folding-week28-editable-source.zip` | ok | same render | 2 byte-identical; 3 same render |
| 28 bonus | `week-28-bonus-source.zip` | ok | toolchain | 1 same render; week-28-bonus.pdf toolchain: 95 px at 100 dpi, shifts up to <0.1 pt |
| 29 | `week-29/two-length-builders-week29-editable-source.zip` | ok | same render | 2 byte-identical; 3 same render; tools copy older than source/problem-files |
| 29 bonus | `week-29-bonus-source.zip` | ok | toolchain | 1 same render; week-29-bonus.pdf toolchain: 95 px at 100 dpi, shifts up to <0.1 pt |
| 30 | `week-30/two-pan-weight-kits-week30-editable-source.zip` | ok | same render | 1 byte-identical; 3 same render; tools copy older than source/problem-files |
| 30 bonus | `week-30-bonus-source.zip` | ok | toolchain | 1 same render; week-30-bonus.pdf toolchain: 10414 px at 100 dpi, shifts up to 29.3 pt |
| 31 | `week-31/hidden-orchard-week31-editable-source.zip` | ok | same render | 1 byte-identical; 3 same render; tools copy older than source/problem-files |
| 31 bonus | `week-31-bonus-source.zip` | ok | toolchain | 1 same render; week-31-bonus.pdf toolchain: 248 px at 100 dpi, shifts up to <0.1 pt |
| 32 | `week-32/squares-inside-rectangles-week32-editable-source.zip` | ok | same render | 2 byte-identical; 3 same render; tools copy older than source/problem-files |
| 32 bonus | `week-32-bonus-source.zip` | ok | toolchain | 1 same render; week-32-bonus.pdf toolchain: 162 px at 100 dpi, shifts up to <0.1 pt |
| 33 | `week-33/prime-length-necklaces-week33-editable-source.zip` | ok | same render | 1 byte-identical; 3 same render; tools copy older than source/problem-files |
| 33 bonus | `week-33-bonus-source.zip` | ok | toolchain | 1 same render; week-33-bonus.pdf toolchain: 94 px at 100 dpi, shifts up to <0.1 pt |
| 34 | `week-34/symmetry-breaking-week34-editable-source.zip` | ok | exact | 4 PDFs byte-identical; tools copy older than source/problem-files |
| 34 bonus | `week-34-bonus-source.zip` | ok | toolchain | 1 same render; week-34-bonus.pdf toolchain: 107 px at 100 dpi, shifts up to <0.1 pt |
| 35 | `week-35/glide-borders-week35-editable-source.zip` | ok | exact | 5 PDFs byte-identical; tools copy older than source/problem-files |
| 35 bonus | `week-35-bonus-source.zip` | ok | exact | 2 PDFs byte-identical |
| 36 | `week-36/nine-point-world-week36-editable-source.zip` | ok | exact | 4 PDFs byte-identical; tools copy older than source/problem-files |
| 36 bonus | `week-36-bonus-source.zip` | ok | exact | 2 PDFs byte-identical |
| 37 | `week-37/mirror-twins-week37-editable-source.zip` | ok | exact | 5 PDFs byte-identical; tools copy older than source/problem-files |
| 37 bonus | `week-37-bonus-source.zip` | ok | exact | 2 PDFs byte-identical |
| 38 | `week-38/seams-and-cuts-week38-editable-source.zip` | ok | same render | 2 byte-identical; 3 same render; tools copy older than source/problem-files |
| 38 bonus | `week-38-bonus-source.zip` | ok | exact | 2 PDFs byte-identical |
| 39 | `week-39/road-detours-week39-editable-source.zip` | ok | same render | 1 byte-identical; 3 same render |
| 39 bonus | `week-39-bonus-source.zip` | ok | exact | 2 PDFs byte-identical |
| 40 | `week-40/loop-color-certificates-week40-editable-source.zip` | ok | same render | 1 byte-identical; 3 same render; tools copy older than source/problem-files |
| 40 bonus | `week-40-bonus-source.zip` | ok | exact | 2 PDFs byte-identical |
| 41 | `week-41/torus-portals-week41-editable-source.zip` | ok | same render | 2 byte-identical; 3 same render; tools copy older than source/problem-files |
| 41 bonus | `week-41-bonus-source.zip` | ok | exact | 2 PDFs byte-identical |
| 42 | `week-42/fair-results-lopsided-bag-week42-editable-source.zip` | ok | same render | 1 byte-identical; 3 same render |
| 42 bonus | `week-42-bonus-source.zip` | ok | exact | 2 PDFs byte-identical |
| 43 | `week-43/shuffling-picture-cards-week43-editable-source.zip` | ok | same render | 2 byte-identical; 3 same render |
| 43 bonus | `week-43-bonus-source.zip` | ok | exact | 2 PDFs byte-identical |
| 44 | `week-44/copying-bag-week44-editable-source.zip` | ok | same render | 1 byte-identical; 3 same render |
| 44 bonus | `week-44-bonus-source.zip` | ok | exact | 2 PDFs byte-identical |
| 45 | `week-45/visible-hidden-sides-week45-editable-source.zip` | ok | same render | 1 byte-identical; 3 same render |
| 45 bonus | `week-45-bonus-source.zip` | ok | exact | 2 PDFs byte-identical |
| 46 | `week-46/forgetting-boards-week46-editable-source.zip` | ok | same render | 1 byte-identical; 3 same render; tools copy older than source/problem-files |
| 46 bonus | `week-46-bonus-source.zip` | ok | exact | 2 PDFs byte-identical |
| 47 | `week-47/gentle-step-landscapes-week47-editable-source.zip` | ok | same render | 1 byte-identical; 3 same render; tools copy older than source/problem-files |
| 47 bonus | `week-47-bonus-source.zip` | ok | exact | 2 PDFs byte-identical |
| 48 | `week-48/inside-outside-covers-week48-editable-source.zip` | ok | same render | 2 byte-identical; 3 same render; tools copy older than source/problem-files |
| 48 bonus | `week-48-bonus-source.zip` | ok | exact | 2 PDFs byte-identical |
| 49 | `week-49/four-tower-differences-week49-editable-source.zip` | ok | same render | 1 byte-identical; 3 same render; tools copy older than source/problem-files |
| 49 bonus | `week-49-bonus-source.zip` | ok | exact | 2 PDFs byte-identical |
| 50 | `week-50/staircases-and-lengths-week50-editable-source.zip` | ok | same render | 1 byte-identical; 3 same render; tools copy older than source/problem-files |
| 50 bonus | `week-50-bonus-source.zip` | ok | exact | 2 PDFs byte-identical |
| 51 | `week-51/honest-measurement-ranges-week51-editable-source.zip` | ok | same render | 2 byte-identical; 3 same render; tools copy older than source/problem-files |
| 51 bonus | `week-51-bonus-source.zip` | ok | exact | 2 PDFs byte-identical |
| 52 | `week-52-source.zip` | ok | same render | 2 same render; tools copy older than source/problem-files |
| 53 | `week-53-source.zip` | ok | same render | 2 same render; tools copy older than source/problem-files |
| 54 | `week-54-source.zip` | ok | same render | 2 same render; tools copy older than source/problem-files |
| 55 | `week-55-source.zip` | ok | exact | 2 PDFs byte-identical; tools copy older than source/problem-files |
| 56 | `week-56-source.zip` | ok | same render | 3 same render; tools copy older than source/problem-files |
| 57 | `week-57-source.zip` | ok | same render | 1 byte-identical; 2 same render |
| 58 | `week-58-source.zip` | ok | same render | 3 same render; tools copy older than source/problem-files |
| 59 | `week-59-source.zip` | ok | same render | 1 byte-identical; 2 same render; tools copy older than source/problem-files |
| 60 | `week-60-source.zip` | ok | exact | 2 PDFs byte-identical; tools copy older than source/problem-files |
| 61 | `week-61-source.zip` | ok | exact | 2 PDFs byte-identical; tools copy older than source/problem-files |
| 62 | `week-62-source.zip` | ok | same render | 3 same render; tools copy older than source/problem-files |
| 63 | `week-63-source.zip` | ok | exact | 3 PDFs byte-identical; tools copy older than source/problem-files |
| 64 | `week-64-source.zip` | ok | same render | 2 same render; tools copy older than source/problem-files |
| 65 | `week-65-source.zip` | ok | same render | 2 same render; tools copy older than source/problem-files |
| 66 | `week-66-source.zip` | ok | same render | 2 same render; tools copy older than source/problem-files |
| 67 | `week-67-source.zip` | ok | same render | 2 same render; tools copy older than source/problem-files |
| 68 | `week-68-source.zip` | ok | same render | 2 same render; tools copy older than source/problem-files |
| 69 | `week-69-source.zip` | ok | same render | 2 same render; tools copy older than source/problem-files |
| 70 | `week-70-source.zip` | ok | same render | 2 same render; tools copy older than source/problem-files |
| 71 | `week-71-source.zip` | ok | same render | 2 same render |
| 72 | `week-72-source.zip` | ok | same render | 2 same render; tools copy older than source/problem-files |
| 73 | `week-73-source.zip` | ok | same render | 2 same render; tools copy older than source/problem-files |
| 74 | `week-74-source.zip` | ok | same render | 3 same render; tools copy older than source/problem-files |
| 75 | `week-75-source.zip` | ok | same render | 2 same render; tools copy older than source/problem-files |
| 76 | `week-76-source.zip` | ok | same render | 3 same render; tools copy older than source/problem-files |
| 77 | `week-77-source.zip` | ok | same render | 3 same render; tools copy older than source/problem-files |
| 78 | `week-78-source.zip` | ok | same render | 2 same render; tools copy older than source/problem-files |
| 79 | `week-79-source.zip` | ok | exact | 2 PDFs byte-identical; tools copy older than source/problem-files |
| 80 | `week-80-source.zip` | ok | exact | 2 PDFs byte-identical; tools copy older than source/problem-files |
| 81 | `week-81-source.zip` | ok | exact | 2 PDFs byte-identical; tools copy older than source/problem-files |
| 82 | `week-82-source.zip` | ok | exact | 2 PDFs byte-identical; tools copy older than source/problem-files |
| 83 | `week-83-source.zip` | regenerated | exact | 2 PDFs byte-identical; editable/README.md had changed after packaging (ff74daa); rewritten with package.py, same 27 member paths |
| 84 | `week-84-source.zip` | ok | exact | 2 PDFs byte-identical; tools copy older than source/problem-files |
| 85 | `week-85-source.zip` | ok | exact | 4 PDFs byte-identical; tools copy older than source/problem-files |
| 86 | `week-86-source.zip` | ok | exact | 4 PDFs byte-identical; tools copy older than source/problem-files |
| 87 | `week-87-source.zip` | ok | exact | 5 PDFs byte-identical; tools copy older than source/problem-files |
| 88 | `week-88-source.zip` | ok | exact | 3 PDFs byte-identical; tools copy older than source/problem-files |
| 89 | `week-89-source.zip` | ok | same render | 2 byte-identical; 1 same render; tools copy older than source/problem-files |
| 90 | `week-90-source.zip` | ok | same render | 2 byte-identical; 1 same render; tools copy older than source/problem-files |
| 91 | `week-91-source.zip` | ok | exact | 4 PDFs byte-identical |
| 92 | `week-92-source.zip` | ok | exact | 2 PDFs byte-identical; tools copy older than source/problem-files |
| 93 | `week-93-source.zip` | ok | exact | 2 PDFs byte-identical; tools copy older than source/problem-files |
| 94 | `week-94-source.zip` | ok | exact | 4 PDFs byte-identical |
| 95 | `week-95-source.zip` | ok | exact | 3 PDFs byte-identical; tools copy older than source/problem-files |
| 96 | `week-96-source.zip` | ok | exact | 3 PDFs byte-identical |
| 97 | `week-97-source.zip` | ok | exact | 2 PDFs byte-identical |
| 98 | `week-98-source.zip` | ok | exact | 3 PDFs byte-identical; tools copy older than source/problem-files |
| 99 | `week-99-source.zip` | ok | exact | 4 PDFs byte-identical; tools copy older than source/problem-files |
| 100 | `week-100-source.zip` | ok | exact | 2 PDFs byte-identical; tools copy older than source/problem-files |
