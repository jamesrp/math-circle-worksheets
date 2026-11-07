# Week 87 K–1 guide — writer report

## Deliverables and scope

- `draft/k1-guide.pdf`: **4 US Letter pages**, W87-K-FAC-v1, pdfLaTeX.
- `draft/src/`: editable `k1-guide.tex`, portable `build.sh`, independent
  `check_guide.py`, and rebuild README. No LaTeX intermediates are in `draft/`.
- Writer stage only. No critic/reviser stage, student-page change, catalog or
  base-guide edit, commit, push, or public write was performed.
- Exact future replacement: **“K–1 route (adult-led)”, page 1**, in
  `lowell-math-circle-year-2/week-87/week-87-facilitator.pdf` (W87-F-v2).
  The new preparation supplements that guide's older-table kits, without
  replacing the older-band overview or solutions.

## Mathematical destination and checks

The theorem-first opening states the fixed-card majority cycle, explains why
the waiting letter wins for those cards, and proves that a letter wins every
three-option knockout iff it beats both rivals (under the stated no-tie,
unchanged-ranking assumptions). The later destination separates “first on two
cards is sufficient” from “first on two cards is necessary”: B can win first on
one card, but cannot win first on none. The latter has a token-grouping proof.

The checker reads actual rankings, targets, problem/page locations and agenda
starts from the final student PDF, with an exact SHA-256 version binding:
`02d7aed95f9d5fb4af5126e710494e54aee9a7f5bd217b551709920e1523ca47`.
It is an independent implementation, not an import or invocation of the
student `verify.py`.

- Final packet is **6 pages, 8 problems**. P1/P2/P3/P4 are on pages 1/2/3/4;
  P5–P6 on page 5; P7–P8 on page 6. Both supplied reviews describe the earlier
  five-page draft, so their old P5–P8 target letters were not used as the key.
- Recomputed every printed ballot, supporter, tally and knockout in the guide.
  DFE/EFD/FED demo gives E over D 2–1, then F over E 2–1; F is the sole possible
  knockout winner, so the demonstration is non-task and does not reveal the
  cycle.
- Enumerated all **9** single-card swaps in final P5. Exactly three make C win:
  V1 ABC→ACB, V1 ABC→CBA, V2 BCA→CBA. Important tally distinction: the middle
  construction makes C beat A **3–0**, not 2–1; the guide states the correct
  individual counts. This was caught and fixed by writer self-checking.
- Enumerated all **216 ordered profiles**. P6 has 68 ordered / 18 unordered
  B-winning profiles; the checker prints the full unordered catalog and checks
  the guide's example. With B first once, exactly the two stated unordered sets
  work: {ABC, BAC, CBA}, {ABC, BCA, CBA}. With B never first, **0 of 64 ordered
  profiles** work. The grouping proof and iff theorem were also checked on all
  profiles.
- The actual materials PDF and `source/week-87/figures.py` confirm the printed
  counts/dimensions: 3 fixed cards at 45×80 mm; 6 option tiles at 28 mm; V1–V3
  vote discs at 18 mm; tally mat 170×90 mm with 54 mm wells; knockout mat
  175×100 mm; 3 blank cards and 18 letter slips at 21 mm. Two K–1 pair kits add
  two copies of materials pp. 1 and 4, plus two p. 2 copies for later builds.

## Visual and build evidence

- Read the final student source; rendered and personally inspected **all six
  final K–1 pages**. Also inspected relevant materials pages 1, 2, 4 and the
  Week 98 model's opening pages; consulted its TeX source for the matching
  sans-serif 11-point format, 0.7-inch margins, paragraph spacing and running
  header/footer.
- Read the full Week 87 base guide and the shared, line and upper student
  packets, the outline, both student reviews, K–1 draft README, source notes,
  root guidance and week-guides brief.
- The final guide was rendered at **140 dpi** and **all four pages personally
  inspected after the final edit**. Header/footer text and page numbers are
  correct; no clipping, collisions, missing glyphs or split problem sections.
- The two-pass build exits on errors, overfull boxes, missing characters or
  LaTeX/package warnings. Final build passed with none. All fonts are embedded.
- Clean-copy reconstruction outside the repository succeeded in
  `/tmp/k1-87-guide-clean-cpvQ5d`: only `src/` and the final student `k-1.pdf`
  beside it were supplied. The checker used the adjacent student PDF (no
  repository dependency), passed, and `pdftotext -layout` output matched exactly.
  The rebuilt PDF was also **byte-identical**, SHA-256
  `3b1f4d06be5afc04f2ccab454e5dd1df7fa0cc1dac1d52824d3ec3cca900ea44`.
- The environment's isolated TeX configuration was sourced externally before
  every compile. It is not embedded in portable `build.sh`. That script
  compiles to `../k1-guide.pdf`, removes build intermediates, then runs its
  checker. Student lookup prefers the folder beside `src/`, then discovers
  `plans/k1-drafts/week-87` via ancestors; no machine-specific fallback exists.
- QA images, text and logs remain under this run's `tmp/`, not in deliverables.

## Student-page risks, missing objects and verification limits

No mathematical error was found in the final student pages. The earlier review
issues are addressed there: final P5 targets C, P6–P8 target B; P2 has the
knockout visual; P7–P8 name first-row constraints and an action. Guide coverage
uses those revised pages, not the old answer key.

Remaining **unpiloted operational concerns**, not required student edits:

1. Week files print D/E/F launch rankings only as small pictures, and print no
   movable D/E/F option tiles. The guide explicitly supplies one table-wide
   set of six temporary **28 mm** scrap labels D,D,E,E,F,F for its physical
   recap, while reading the printed rankings. This is the only additional
   letter-piece set; pencil/scrap for optional records and grouping loops are
   ordinary supplies. The A/B/C task kits are printed by the week files.
2. On P3/P4 the printed cards replace the cut cards; confusing the two sets
   changes votes. The guide tells adults to put away the original cut cards
   and vote directly from the full-size page pictures, without transcription.
3. P3/P4 can require several knockouts and have no agenda record. An adult's
   light waiting-letter/final-winner record is optional; the children retain
   agenda choices. The first-hour route stops with P3, allows P4 only for a
   ready pair, and reserves P5–P8 for another visit.
4. Small empty frames on student pages 5–6 are not slip-sized workboards. The
   guide identifies them as adult pencil records; builds use full-size blank
   cards. Slip-to-row fit and juggling tally/knockout mats need rehearsal.

**Untested with children; physically unrehearsed.** No claim is made about
actual cutting time, print fit, fine-motor handling, token resets, staffing
load, or pacing. The guide labels all preparation times estimates. The local
checkout does not contain the downloaded MSRI book; the recorded Week 87
teaching-source notes were consulted, but no fresh direct-read claim is made
for that book or the research articles. All finite claims here are independently
derived from the owned final pages, not dependent on an unavailable article.

Claude critic findings and revisions: **not yet applicable; writer stage only**.
