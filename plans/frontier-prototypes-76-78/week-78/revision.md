# Week 78 revision record

Date: 2026-10-07. Scope: fresh REVISER stage only, one shared Grades 4-5 student
prototype. The run-local addendum controls. Sources were copied from `draft/src/`
to `final/src/`; the draft was left unchanged. No guide, additional grade-band
packet, workflow rerun, delegation, commit, or push was made.

## Review findings and disposition

1. **Adopted: guarantee unequal-width/height southwest/northeast intersections.**
   Problem 1 keeps two child-chosen trials at junction A=(4,4). The two lower
   grids now prescribe A=(2,2), B=(6,5), and A=(2,2), B=(5,6). Their intersections
   are respectively (3,2) and (2,3), so both the east-arm and north-arm singleton
   mechanisms are encountered before the general argument. All four grids retain
   the draft's 7.8 mm unit spacing. Problem 2's northwest/southeast and three
   shared-ray examples are unchanged. No intersection classification or method
   has been printed as a hint.
2. **Adopted: concrete continuation beyond the grid.** Problem 6 now begins with
   the explicitly supplied junctions A=(2,7) and B=(10,5). Its 0-8 grid plots A;
   the blank area to its right permits extension to B and the meeting (10,7).
   The prescribed meeting is outside the grid. Both junction coordinates are
   stated, rather than leaving the child to infer missing cropped information.
   The question then retains the no-miss and overlap-classification arguments.
   This adds no page and does not reduce grid sizes.
3. **Adopted: reject finite cases with missing expectations.** `checked_pairs`
   checks list lengths before pairing the opening minimum-tie examples, all
   printed intersection pairs, both inverse lists, and the new fixed trials.
   The off-grid pair has an explicit exact expected intersection and a cardinality
   check. A mutation test appended one unmatched case to each of the five lists;
   every test raised the named coverage error. Original data were restored in
   memory after each test; no mutant source was retained.
4. **Mathematical review accepted.** The independent math review found no error
   in the draft. Its all-real arguments and ordinary set-intersection meaning
   remain intact. The new finite cases were checked with exact unbounded-ray
   intersection calculations, not by a grid crop.

No recommendation was declined. The suggested finite examples were added without
turning the all-case questions into worked solutions. No claim is made that
finite checks prove the general theorem.

## Verification

- `python3 final/src/check_math.py` passes all explicit finite examples, 2,401
  ordered junction-pair regressions, inverse constructions, half-grid least-tie
  checks, and common-shift checks. The builder reruns this checker.
- `python3 final/src/build.py --out final` completes using Python's standard
  library and the declared TeX dependencies. No system TeX changes or extra
  packages were needed.
- `final/students.pdf`: four US Letter pages, 139,104 bytes, below 200 KB.
- The final LaTeX log has no overfull/underfull boxes, warnings, missing characters,
  or errors. The extracted text has Problems 1-7 in order and the expected header,
  footer, packet ID, and page numbers.
- Rendered all four final pages at 130 dpi into `final/render/page-1.png` through
  `page-4.png` and visually inspected each. Page 1's new dots and labels are at
  the checked coordinates; the minimum-tie convention remains legible. Page 2
  retains all four contrasts and explanation space. Page 3 retains the inverse
  constructions and three equal-scale locus grids. Page 4 has the exact off-grid
  junction information, ample right-side extension space, and both late general
  questions. No clipping, overlaps, malformed rays, missing glyphs, or unequal
  axis scaling were found. Headers and footers are clear on every page.
- Copied only the five portable source files into `final-portable-check/src/`
  and rebuilt into its separate `out/` directory. Extracted text matched the
  final PDF exactly. All four 130 dpi PNGs matched the visually inspected final
  PNGs byte for byte. This rebuild's LaTeX log was also clean.
- `final/src/` contains only `README.md`, `build.py`, `check_math.py`, `data.py`,
  and `students.tex`. It has no external assets, downloaded papers, workflow
  prompts, or build intermediates. The README preserves prerequisites, portable
  build instructions, primary-source relationship, and limitations.
- Final PDF SHA-256:
  `4460ba48641f9ece9ba163f296d53ff23c1b34a6681acba17b6b7797719f7c46`.

Physical printing, pencil handling, light-grid reproduction, timing, and
classroom use remain untested. The packet is digitally checked and unpiloted.
