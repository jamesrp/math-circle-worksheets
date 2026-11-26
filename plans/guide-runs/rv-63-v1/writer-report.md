# Week 63 return visit writer report

## Delivered

- `draft/facilitator.pdf`: **8 US Letter pages**, pdfLaTeX, required W63-RV-FAC-v1 header/footer.
- `draft/src/`: portable TeX, `build.sh`, independent `check_guide.py`, pinned student manifest, complete catalog data, and build notes. No TeX intermediates or machine-specific setup are included.
- Writer stage only. No critic/reviser stage, no student edits, no public writes, no commits.

The theorem-first overview states and explains minimum swaps `n - loops`, exact-length parity, the minimum swaps to empty all homes, double-counted home marks and pairs, exact-match piles and their alternating zero/one difference, and compatible-forbidden-spot inclusion-exclusion. Each of the final 30 numbered student problems is covered with answers, reasoning and held hints. It distinguishes finite experiments from complete searches and general explanations.

## Final inputs and differences from earlier reviews

I rendered and personally inspected all **21 final student pages**: K–1 5 pages / Problems 1–8, middle 6 / 1–9, upper **10 / 1–13**. The old reviews concern upper 9 pages / 1–12. The final four-card grids are Problem 12 on page 9; the five-card grids are Problem 13 on page 10. The guide keys those final pages, not the obsolete answer-map.

I read the final sources, outline, both student reviews, draft README, base guide and all three base-material pages; I visually inspected the materials and the style-model opening pages, and read the Week 8 model guide and Week 98 guide sources. The final middle Problem 9 now asks for 8, 6 and impossibility of 5, not the older minimum question. Final K–1 Problem 5 includes the equality answer. No mathematical error was found on the final student pages.

## Mathematical checks

The new checker imports neither the student generator nor its verifier. Its transcription is bound to final student PDF SHA-256 values, and it verifies each page's problem map. It independently checks:

- breadth-first distances over all **152 permutations for 2–5 cards**, against `n - loops`;
- exact-length reachability for lengths 0–7, including permitted repeated swaps;
- every printed shortest swap witness, task loop, launch row and grid conversion;
- home marks, marks per letter, pairs, exact-match piles, and zero/one differences;
- complete hardest-row and forbidden-board catalogs, including actual catalog presence in the guide PDF;
- all **1,820** four-spot boards: possible allowed counts `0, 4, 6, 7, 8, 9`, with frequencies `8, 324, 384, 576, 504, 24`;
- all four strip/ring grid coefficient lists by nonclashing subset enumeration, permutation filtering, alternating sum, and the chain recurrence.

`tmp/checker-final.txt` records PASS. In particular, upper five-card hardest rows number 24, the other 20 home-free rows require 3 swaps, and strip/ring catalogs give 16/13 rows.

## Build and visual checks

The final PDF was rendered and every one of its **8 pages personally inspected**. Typography, complete tables, labels, catalog entries, header/footer placement and page transitions are clean; no clipped or overlapping content was found. Two-pass compilation reports **zero errors, warnings or overfull boxes** in the retained final log under `tmp/compile/`. The source builder itself rejects overfull boxes.

A clean copy outside the repository at `/tmp/w63-rv-guide-clean-M3UMRc` contains only `src/` and the three student PDFs before building. It rebuilt using the same portable `build.sh`, resolved its adjacent PDFs rather than the repo fallback, and passed the checker. `pdftotext -layout` is identical, and the rebuilt PDF is also byte-identical:

`f2d387dabc83febb89982f875151631a7ddf01b9b00ce73b7002515ba85035f4`

The runtime TeX workaround was sourced before compiling but is deliberately absent from the portable source. QA, renders and logs remain in `tmp/`, not in the deliverable source.

## Risks and limits

- **Unpiloted and physically unrehearsed.** Card fit under crossed-out pictures, 12 mm-or-smaller counters on the miniature A–C outcomes, handling, home-printer contrast, cutting time and pacing are not established by digital checks. The guide says so.
- K–1 Problem 5 needs **six small counters per young table**, which no base PDF prints. The base kit has sticky dots, not these counters. The guide lists them and an adult-supported pencil-circle alternative. Its non-task U–X launch is drawn, since the kit prints only A–E cards.
- Middle pages 5–6 are reference boards, not card-placement mats. The guide explicitly prevents placing 30 × 40 mm cards there; it uses outcome filtering. Only K–1 pages 4–5 and upper pages 7–8 carry the actual-size new placement homes.
- Two middle pairs share one cut deck and one uncut marking sheet. The guide staggers swap/marking work and makes sorting a shared table task.
- Middle Problem 9's maximum and no-five claim are backed by exhaustive computer coverage; the guide does **not** pretend that displaying the seven coefficient triples is itself a child's completeness proof. This remains readiness-dependent extension work. Upper grid and recurrence work is likewise saved for later visits when needed.
- Relevant private pedagogy books are absent. I used the base source notes' exact passage pointers and labeled that consultation indirect. Frieze's D14 pp. 2–4 and D16 pp. 1–2, 4–7 were opened directly. Other outline bibliography is explicitly listed as not directly consulted, with unverified page locators not invented.

No supplied student page was altered to address these issues. Claude's independent guide critique is still the next stage.
