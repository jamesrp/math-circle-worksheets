# Week 23 independent adult-guide audit

**Verified after correcting the P4 trace.** All overview, actual final P1–6 solutions, explicit output rows, hints, extensions, limits and source roles were independently reviewed. The corrected five-page PDF was inspected. `guide-checks.json` binds current source/PDF/student authority; `guide-independent-check.py` reproduces additional finite checks independently with the standard library.

| Final task | Independent result |
|---|---|
| P1 minimum selection | Verified minimum three bars and witness (1,2),(1,3),(1,4). Fewer graph edges leave lane 1 disconnected from another component, which can hold the minimum. General n≥1 minimum n−1 has the same proof; n=1 correctly needs no bars. |
| P2 lower-half selection | Verified all 24 distinct and 256 repeated-value inputs. The final min/max formulas and all four cross-half inequalities are correct. Input 3,4,1,2 → 2,1,4,3 proves the halves need not internally sort. |
| P3 merger | Verified minimum three, exactly two shortest mergers differing by the order of disjoint first bars. All six distinct legal inputs and 100 repeated-value legal inputs per merger sort. Six distinct starts need six successful records; two bars permit at most four. |
| P4 broken promise | Verified 2,1,4,3 and 1,2,4,3 remain unsorted. The corrected extra trace is 1,3,4,2 → 1,3,4,2 → 1,2,4,3 → 1,2,4,3. Three bars cannot sort all 24 distinct starts because 8<24. |
| P5 tagged order | Verified every six-row X/Y table entry and worked 3A,1B,3C → 1B,3A,3C. X reverses the equal pair exactly twice; Y never does. Both value-sorting proofs are valid. |
| P6 stability | Verified adjacent swaps alter relative order only for the swapped pair; equal values never swap. Induction proves preservation for arbitrary machine length, even if values are not fully sorted. Tags are identifiers, not tie-breakers. |

The author corrected the one mathematical trace error found here: the former P4 output 1,3,2,4 was incorrect. Both current JSON and PDF now say 1,2,4,3. No other correction is needed.

The five-bar extension is verified: prepending (1,2),(3,4) establishes the merger promise, hence sorts arbitrary numerical inputs including ties. Independent finite checks cover all 24 distinct orders and 256 assignments on four values. The n-lane selector construction was checked through n=6. Additional adjacent-action checks cover every three-value assignment through five lanes (1,278 actions); the general pair-order proof supplies the unbounded claim. If ties are allowed to swap, one adjacent bar can reverse 2A,2B, so the printed no-swap-on-ties assumption is essential.

The theorem-first overview distinguishes selection, merging and stability. Record-count lower bounds correctly use distinct ranks; correctness separately includes repeated values. Hints retain fixed bar positions and input promises. Explicit fixed-table staffing and oral entry gates preserve children's choices.

Attribution is accurate: current base-guide comparator conventions and reversible-record bounds match cited pages; Liverpool COMP308 Lecture 17 is recorded context without newly read body asserted. Math Circle by the Bay Preface vii–x/PDF 8–11 supports teaching context; physical card/tray routes are proposed adaptations.

No unresolved mathematical issue. Fixed-bar/card/tag procedures remain unrehearsed; extracted-source ZIP rebuilding is a separate release check.

## Verification-text refresh

Verified the final status-text revision independently against the saved pre-revision JSON. Only `verification` changed; every other parsed field is identical, including all overview, solution, hint, extension, material, launch and source content. Both new verification paragraphs were read in source and on the rebuilt page 5; that page was rendered and inspected, remains legible, and the guide remains five pages. All 39 JSON prose paragraphs occur in the rebuilt PDF. The packaged `guide-src/guide.json` is byte-identical. The independent guide checker passed again without mathematical changes.

Current guide JSON SHA-256: `f3b3dd3c0788d87e00d2acc579fe33870322c929e094de98912f10a5b9129343`.

Current guide PDF SHA-256: `2f5ed590868b7c9b94b1a4bcb848a7a92632e621792938442aba17c999f4c368`.

The inspected release-validation record reports completed passing checks for its recorded reference files; current package synchronization and repeated ZIP validation belong to the root release process. This refresh confirms the new status wording and mathematical identity rather than claiming an additional ZIP rebuild by this reviewer. Physical fit and classroom rehearsal remain untested.
