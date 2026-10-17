# Weeks 85–91 production status

Complete reviewed student worksheets, theorem-first facilitator guides, editable sources and portable ZIPs. Start with the [shared print/source index](../../../lowell-math-circle-year-2/WEEKS-85-91.md). All are unpiloted and physically unrehearsed; this is not organizer promotion or an adopted calendar. The recovered October 11 plans remain intact as historical planning evidence.

| Week | Family and actual bands | PDF pages: student / materials / guide | Canonical artifact commit | Final review |
|---|---|---:|---|---|
|85|Pantographs: shared 2–5, upper 4–5|8 / 10 / 5|`95a73c3`|[23 pages](week-85/final-pair-review.md)|
|86|Pursuit: shared 2–5, upper 4–5|10 / 3 / 6|`7813201`|[19 pages](week-86/final-pair-review.md)|
|87|Voting: cards 2–5, line 3–5, upper 4–5|9 / 5 / 6|`5241336`|[20 pages](week-87/final-pair-review.md)|
|88|Packing: shared K–5 menu selected by prerequisites|8 / included / 6|`8933ec6`|[14 pages](week-88/final-pair-review.md)|
|89|Discrete calculus: shared K–5 menu selected by prerequisites|11 / 2 / 8|`61cc075`|[21 pages](week-89/final-pair-review.md)|
|90|Sliding number arrays: 2–5, upper continuations|8 / 11 / 9|`76799d3`|[28 pages](week-90/final-pair-review.md)|
|91|Rotor routers: 2–3 tree entry; 4–5 continuations/roads; 2–5 coin comparison|10 / 7 / 6|`6b9a910`|[23 pages](week-91/final-pair-review.md)|

**25 PDFs, 148 pages; seven portable source ZIPs.** All twelve student packets, six separate materials packets and seven guides were rendered and inspected, including every band and variant. Every student packet is newly produced and actually checked; no student coverage is inferred from adult-guide edits. The [release audit](release-audit.json) records PDF sizes/pages/hashes, source archive membership, byte-identical clean-extracted rebuilds, reference-copy agreement and local print-index links. Per-week subdirectories retain fresh critic/math/reviser and final-pair evidence; the guide is a separate authoring/review step.

For the combined release check, install PyMuPDF in addition to the packages' Python 3/pdfLaTeX dependencies, then run from the repository root:

```sh
python3 plans/seven-families-85-91/production/check_release.py . 85 86 87 88 89 90 91 --index lowell-math-circle-year-2/WEEKS-85-91.md --out plans/seven-families-85-91/production/release-audit.json
```

The seven package builders themselves need only Python standard library and the TeX packages listed in their READMEs. They do not need PyMuPDF, private references or network access. The release checker extracts each archive into a fresh temporary directory; build/render intermediates stay under repository `tmp/`.

## Scope, adaptations and remaining practical checks

The [scope/overlap record](SCOPE.md) and [teaching-source evidence](PEDAGOGY.md) document actual current-main calibration, primary-source boundaries and planning recovery from `5ae164a`. The workboard claim was published as `6e0879c`; the 32 authored historical planning/review/check files were recovered in `8bfe422`. Week 83 and older audit-flagged packets are untouched. Completed Weeks 92–97 were inspected for overlap; 98–100 remain another task's reservation.

The shared print index lists the actual changes from tentative plans: additional concrete contrasts, separate routes, corrected physical paper geometry, complete unchanged-input demonstrations, broader material sets and preserved return investigations. No independent K–1 edition is forced. The K–5 menus in 88–89 have concrete younger entry points, not a claim that every page is age-independent.

Week 85 has the strongest remaining material gate: coaxial mounts, branch stability, support and hand clearance require a real working-kit trial. Other weeks still need printing/fit, token/card handling, state retention, resets and procedure rehearsal. None of these physical checks or classroom pilots has occurred. Digital correctness and reconstruction do not certify them. No Drive upload or remote classroom synchronization is claimed. The older combined books remain separate and unchanged.
