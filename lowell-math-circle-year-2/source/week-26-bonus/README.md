# Week 26 bonus companion - portable editable release

Three distinct theme-matched encore investigations, in one shared selected-band student companion and a separate adult guide. **Unpiloted.** These are new week-local companion files; the base student packet and base guide are separate. Physical fit, procedures and classroom pacing have not been rehearsed.

Print selected pages single-sided on US Letter at 100% scale. Choose an investigation and an entry route from the guide; the theme may support multiple visits. Finishing every page is not the goal. Readiness is based on reading, arithmetic, representation and reasoning prerequisites.

## Rebuild

Requirements: Python 3.10+, packages in requirements.txt, and a normal TeX Live/MacTeX distribution with pdflatex, TikZ, geometry, fancyhdr, Latin Modern and standard LaTeX packages. No font files or TeX binaries are bundled. Set PDFLATEX to your executable if pdflatex is not on PATH. A complete TeX distribution provides its own normal configuration.

```sh
python3 -m pip install -r requirements.txt
python3 build.py --out build
python3 verify_rebuild.py --out build
python3 math/independent-check.py
```

`build.py` writes both week-26-bonus PDFs and intermediates under the selected output folder, leaving references unchanged. Within the main repository, choose an output folder under tmp/, rather than building beside sources. The package has no required absolute project path. Historical workflow prompts contain original run paths as documentary evidence; builders do not use them.

Edit student-src/bonus.tex (and any included drawing helpers) for student pages; guide-src/guide.json for adult prose. The guide renderer is separate from the tested worksheet workflow. Update mathematical checks deliberately when changing instances. Checks assert this release's finite claims, not arbitrary edits.

## Contents and verification

- student-src/: portable final worksheet sources and their original builder.
- guide-src/: editable guide JSON and standalone ReportLab renderer.
- reference-pdfs/: exact current local output copies, not additional print sets.
- math/: independent finite checker; only its package-relative file paths were adapted.
- review/: adversarial and independent math reviews, final audits, answers and revision evidence. Draft findings are historical; final-audit.md records their resolution.
- workflow/: generated writer/critic/math/revise prompts, local encore-scope override, and outline. The global tested prompt set was left unchanged.

Fresh writer, critic, independent math critic and reviser stages produced the student pages. Actual final student pages and represented examples received independent mathematical audits. Every final PDF page is rendered and inspected; a clean extracted-ZIP rebuild compares all page text, Letter dimensions and 110-dpi pixels. See release-validation.json for the result. PDF bytes may differ with timestamps; displayed content is the comparison.

Source/body attribution and mathematical assumptions are in the guide and outline. Original task constructions, prose, drawings and code are editable local project material; third-party references retain their rights. No source books, fonts, caches, generated build files or external downloads are included.

Current print copies: ../../week-26/week-26-bonus.pdf and week-26-bonus-facilitator.pdf. This release is local only; no Drive upload or publication is claimed. The source ZIP in the parent source/ folder is a portable copy of this directory.
