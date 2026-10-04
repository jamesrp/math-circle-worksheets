# Week 12 adversarial student-page review

Reviewed the actual `draft/return-visit.pdf` (3 pages), its TeX source, and the supplied PROMPT/CRITIC files. I rendered all three draft pages afresh and inspected each at page scale. I also read every problem in the actual Week 12 base PDFs and the nine-page base facilitator guide, and visually compared the relevant base pairing/path examples and enumeration pages. The explicit shared-collection override takes precedence over the harness's three-band-file default.

## Revision needed

1. **Page 1, Problem 1: make the saved collection recoverable.** The six extra-workspace circles have neither R/B labels nor fixed position numbers, and there is no case identifier linking a record to one of the three source arrangements. A child can successfully make a pairing with counters/strings on a large board, then save a pencil drawing that no longer says which color arrangement it belongs to. This matters particularly for the youngest children, and for the stated goal of finding *every* pairing: a collection must be checkable for duplicates and omissions without relying on memory or an adult reconstructing the cases. Keep the three clear large work boards, but preserve the arrangement identity on the recording boards (for example, print the R/B pattern on small copies grouped with its source). Alternatively, give stable endpoint labels plus a simple case marker that appears on both the large board and its records. Use an adequately sized supply of records for the three cases; the exact counts are 5, 1, and 2. This is a representation/record problem, not a request for a directed enumeration method. The source location is `\blankpair` and its six uses in the lower-right minipage.

## Small points for the reviser to judge

- **Page 3, first route box:** a six-move solution can require six new eight-letter words. Each route rectangle is about 8.7 cm by 3 cm. It is feasible to arrange these in two columns, but a child's natural one-word-per-line record will be cramped. Consider giving the first route more height, since the other starts require only four moves and one move. No prescribed solution method or extra counting table is needed. This is a practical handwriting concern, not a mathematical blocker.
- **Entry gating belongs in the adult companion:** page 2 assumes the U/D diagonal-step convention already encountered in the base middle/upper routes; page 3 relies on that convention plus maintaining a legal card word. This is appropriate return-visit material. For a newcomer, the adult should use the existing base non-task U/D/path example before handing over page 2. There is no need to repeat the complete base conversion investigation in this packet.

## Passes to retain

- **Three honest new investigations.** Page 1 adds a color restriction and compares how an arrangement changes the number of noncrossing pairings. The alternating case intentionally retains all five base six-dot pairings; the two other color orders reduce the collection and make the comparison substantive. Page 2 adds a height restriction and then seeks a counting explanation. Page 3 adds local changes and shortest-distance reasoning. Problem 3 is a deeper continuation of Problem 2, not a fourth claimed investigation. These are different mathematical directions, not numerical variants of the base.
- **Novelty against the actual base.** The base K–1 route counts uncolored pairings, completes fixed chords, and investigates parity and unavoidable neighboring pairs. The base middle route develops the pairing/path bijection and enumerates unrestricted paths and eight-dot pairings. The base upper route develops ordered-tree codes and the Catalan recurrence. The base guide mentions maximum height as an optional statistic, but does not pose bounded-height enumeration or local-swap optimization. None of the new three investigations merely reprints a base problem.
- **Substantial, child-owned goals.** The all-pairings task has three contrasting arrangements; the height-two collection has eight cases and an explanatory continuation; the move task has three distinct distances and asks for a rule. Goals and legal conditions are stated without supplying an enumeration procedure or the intended invariant. No forced K–1 clone of the upper shortest-route question has been added.
- **Reasonable readiness.** Page 1 has a genuine K–1 entry with spoken rules, colored/lettered counters, and strings; no reading or calculation is necessary to start. Full exhaustiveness can remain a readiness-dependent destination. Page 2 needs one-step height tracking and systematic small-case organization; its count-without-drawing continuation is deeper than its concrete entry. Page 3 needs a stable eight-card word, adjacent swaps, and comparing route lengths, but has an elementary entry and does not require formal algebra.
- **Worked new convention.** Page 3's six-step, non-task example is correct and gives input word/path, the marked neighboring D/U cards and their swap, then output word/path. It does not reveal the eight-step target's distance or a complete collection. The highlighted path segments match positions 2–3 in `UDUUDD → UUDUDD`.
- **Visual/layout checks.** All three pages have readable text, consistent headers/footers, consecutive Problems 1–4, no Name/Date fields, no extra activity titles, and no clipped or overlapping content. Circle boards are genuinely circular and the path grids use equal horizontal/vertical scaling. Page 2 has ten usable record grids for eight solutions, so the printed layout does not disclose the count. Page 3's target/start words agree with their plotted paths. The footer ID is consistent on all pages.

## Independent small-case checks

I independently generated noncrossing matchings recursively on six fixed positions, filtered by unlike colors, enumerated legal U/D words under the ceiling, and used breadth-first search under the printed adjacent-swap rule. Results:

| Printed task | Checked result |
|---|---:|
| P1 `RBRBRB` | 5 pairings |
| P1 `RRRBBB` | 1 pairing |
| P1 `RRBRBB` | 2 pairings |
| P2 four U/four D, heights 0 through 2 | 8 paths |
| P3 five U/five D, heights 0 through 2 | 16 paths |
| P4 `UDUDUDUD` to `UUUUDDDD` | 6 moves |
| P4 `UUDDUUDD` to `UUUUDDDD` | 4 moves |
| P4 `UUUDUDDD` to `UUUUDDDD` | 1 move |

No incorrect represented example or impossible printed task was found. This student-page review does not substitute for the separate theorem/proof review or for physical rehearsal. The materials remain unpiloted.

Fresh review renders and extracted base text are in `critic-render/`; base comparison image is `critic-render/base-comparison.png`.
