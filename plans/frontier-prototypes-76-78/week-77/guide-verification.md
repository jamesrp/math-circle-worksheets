# Week 77 adult-guide verification

Completed 2026-10-07. Separate adult-guide writer stage only. No student pages,
student sources, other weeks, commits, pushes, or publication steps were changed.

## Final deliverables

- final/facilitator.pdf: four US Letter pages, F77-FAC-v1, approximately 120 KB.
- final/guide-src/facilitator.tex
- final/guide-src/build.py
- final/guide-src/check_math.py
- final/guide-src/README.md

The source folder contains exactly those four portable files. It contains no
downloaded source paper, borrowed figure, external font, runtime dump, workflow
prompt, raw tool report, or dependency on the student source folder.

## Control material and scope

Read PROMPT.md and its single-packet addendum, GUIDE.md and its guide addendum,
the mathematical research note, and the final five-page student PDF/source.
Rendered and inspected all five final student pages. The final source/PDF,
including new Problem 6, controlled the answer key. Earlier draft reviewers'
answers and the student's checking script were not used to compute the key.

The guide opens with exact assumptions, boundary monotonicity and uniqueness,
hole count versus persistence, and the fan distinction. It preserves a
prerequisite-led Grades 4-5 route for the current three-child target table.
The organizer remains at that table, with a pair plus rotating referee.
Other tables need their separately planned activities; no younger route is
invented. The guide includes exact target-table printing, tiles, strips, tokens,
stage cards, spares, the physical fit test, a concrete launch, stopping points,
hints in order, and an evidence-sensitive after-session record.

## Independently checked finite mathematics

check_math.py was written afresh from the final printed boards. It enumerates
edge subsets with even vertex incidence and all subsets of available faces,
computing boundaries by symmetric difference. It does not import student
code/comments, prior reviews or a persistence library.

- The introductory non-loop cancellation leaves XZ.
- P1: exactly three nonempty loop edge sets on the divided square. ABC and ACD
  rims can each die with their own tile; only the outer rim survives either
  single filling.
- P2: all four edge-order/tile-order schedules checked. Exactly three kill the
  saved first loop first at 8; AC first followed by ABC at 5 kills it at 5.
  All four count sequences are 0,1,2,1,0.
- P3: all four schedules checked with the final board's CDE triangle labels.
  Filling the first-closed triangle at 5 or 8 gives the two histories despite
  the same counts and final board.
- P4: all four possible one-item moves checked. AC to 3 and ABC to 5 are the
  only legal changes, and both create two holes at a finished stage.
  AC to 5 and ABC to 3 violate the face-boundary arrival requirement.
- P5: finite monotonicity checks on all nested fan face sets pass. The guide
  separately proves the universal claim by retaining the same cancellation
  witness in every later stage; it is not inferred from this finite check.
- P6: all 256 edge subsets and 16 face selections were available to enumeration.
  Exactly four loop edge sets meet the first condition. All six pairs and all
  24 filling orders were checked. Only the two five-edge loops permit either
  strict disappearance order. Both exhibited orders give deaths at fillings
  3 and 4 in opposite order. Pairwise differences of all four eligible loops
  are boundaries of the initially filled ABO/BCO tiles.
- Interval answers were independently recovered from inclusion-map ranks, via
  cosets of earlier cycles modulo later boundaries. This checks actual maps,
  not just dimensions or a visual naming rule. All P2/P3/P4 interval answers
  pass, including tied stages and omitted zero-length bars.
- The restricted square interval formula was cross-checked on 84 finite
  schedules including tied face/diagonal times. Its general validity is
  established by the guide's explicit basis argument, not by those tests.

## General proofs checked separately

1. Monotonicity: any face selection witnessing a zero loop remains available
   in later growing complexes, independently of planarity.
2. Planar filling uniqueness: a nonempty finite selected union has an exposed
   outside boundary edge, so its mod-2 boundary is nonzero. Two different
   fillings would contradict this after symmetric difference.
3. Count formula: graph cycle-space dimension is E-V+C; injectivity of the
   planar face-boundary map makes the F filled-face relations independent.
4. Restricted square barcode: R=P+Q, with the first-filled triangular rim as
   the new basis direction. The old direction lasts until the later filling;
   the new direction ends at the earlier filling. Equal times contribute no
   positive-duration interval.
5. Fan completeness/reversibility: each triangle has an exclusive outer edge,
   which forces its membership in a filling. Survival under either next fill
   forces both lower tiles into the required set, leaving exactly four upper
   choices. Nested required sets cannot reverse their completion order;
   precisely the two middle sets are incomparable.

The guide explicitly limits the model to legal growing planar boards, treats
a tied batch as one stage, preserves each saved edge list, distinguishes a
general saved loop from a barcode generator, and does not infer signal/noise
or a general stability theorem from this packet.

## Build, rendering and portability

- Compiled successfully with the standard-library build.py.
- Four pages, all expected headers/footers, no overfull TeX boxes.
- All fonts are embedded Type 1 subsets; no bitmap fallback or missing glyphs.
- Rendered every final page at 110 dpi and visually inspected each page.
  No clipping, overlaps, broken formulas, table collisions or page spill found.
- Created a temporary ZIP of only the four guide-source files. Extracted into
  a separate temporary folder with only a guide/ directory, no student/
  sibling, and ran its builder from /tmp after removing TEXMF, TEXFORMATS,
  and TEXINPUTS environment overrides.
- The extracted-source builder independently discovered the installed TeX
  distribution and initialized its own temporary format. It had no dependency
  on the original run runtime or any hard-coded absolute source path.
- All four rebuilt page PNGs were byte-identical to the final guide's PNGs.
- Student PDF and all four student-source hashes remained unchanged.

Source lineage: Edelsbrunner, Letscher and Zomorodian, *Topological Persistence
and Simplification* (2002), Section 2 (PDF pages 2-3), Section 3 (PDF pages 4-6),
https://pub.ista.ac.at/~edels/Papers/2002-J-04-TopologicalPersistence.pdf .
This primary source was independently opened to verify its setting and section
scope. Classroom examples, schedules, fan construction and elementary proofs
are original teaching constructions.

## Limits

The digital answer, build and layout checks do not establish physical handling,
material fit, classroom pacing or observed learning. Physical rehearsal and
classroom piloting remain explicitly unperformed. Independent final-pair review
and publication are coordinated by the parent.

## Final hashes

86d65e917d1b11f04e107921a26189a68cc777a03b53f65c9d9d1021fd6775fc  final/facilitator.pdf
2a5e965b676cc2a023d8ad6066831bcc94583a756b73fa59896f2caf4b6c6552  final/guide-src/README.md
bf5dfe0ad9306c07a6cf55dc66cf4ed1316ff425deb7442f716fdd47785c7142  final/guide-src/build.py
e4d688772d7eba5e902c724c8128da83fef3d27d18d61fc1dcb491dc97785179  final/guide-src/check_math.py
a82042614fca50187e359020d748f390caa031b597d04d01eac9985a8d2c6066  final/guide-src/facilitator.tex
e27735de07fee5b65d5f8ea1be06e260f4724a12ca039e10bd8b8d704a4d4787  final/students.pdf
9072e65da0d2bec8f29c0289e2bf6345aa3331d5a8d6cfe54ad516038ec859bc  final/src/README.md
35b3f6da08a7c3e3acdf26a8e1a3b3969213215721e1965c47a54e4689663537  final/src/build.py
6aef2987698fa8222393a9d21b1e4563da0a1b250eec0b8d4f95918ba1f20084  final/src/check_math.py
35b74fc7b3802a7a5bd1f0a77527eedea1b0ac89c3cccd60793c24d2e1d70756  final/src/students.tex
