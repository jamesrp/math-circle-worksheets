# Week 87 K–1 guide revision

**Revisions ready; packaging deferred.** `final/k1-guide.pdf` is **5 US Letter pages**, identifier `W87-K-FAC-v2`. This is a fresh reviser session, separate from the writer and critic. Original draft, reviews, reports and review-check evidence are preserved; student pages, existing guides, materials and catalog records are unchanged. All three should-fix findings are fixed. Eleven minors are fixed; minor 12 was already implemented and its reported failure did not reproduce. No must-fix or should-fix finding was declined.

## Finding dispositions

Numbers refer to the preserved `review-guide.md`.

| Finding | Disposition and evidence |
|---|---|
| Should 1 | Overview now states the cycle-or-fixed-winner dichotomy, exact one-B-first condition, and the one-swap theorem with its vote-change explanation. The garbled heading is replaced by “What B needs on the cards.” Discoveries are named for Problems 1–8 and mapped to the older tables and the separate line visit. P5 completeness is structural: exactly the three swaps moving C up. All nine swaps and all 216 ordered profiles are rechecked. |
| Should 2 | Added a timed return route on guide p. 4: 3–5-minute restart instead of an unrelated line launch, P4 if skipped (about ten minutes), non-task CAB slip-building demonstration with input/first-slip/output visual, P5 about fifteen minutes, P6 about ten, and readiness-dependent P7/P8. One A/C swap in P4 prepares the procedure without solving the C-target task. Completion is optional. |
| Should 3 | The partner checks tokens as placed. The adult checks the count and requests a replay when it differs from the key; the adult no longer promises to check every ballot for two pairs simultaneously. First knockouts remain staggered. |
| Minor 1 | Knockout procedure explicitly routes the first winner through First winner, the loser to Out, then the winner and waiting tile to Final pair; final loser and winner are also routed. |
| Minor 2 | P5 restores the cut V1–V3 set, uses the blank card with matching V label, and puts only the replaced original aside. P2's hint checks those cut cards against student p. 1. |
| Minor 3 | P8's loops use spare A and C tiles as readable labels; adult explains the support meaning. Tokens return beside the tally mat afterwards. |
| Minor 4 | P6 accepts both pair votes going to B, with pointing to the supporting cards as the explanation, rather than requiring an abstract agenda explanation. |
| Minor 5 | Optional color dots also go on student V labels on pp. 1, 3, 4, 5. Dots and covers are explicitly untried. No student PDF is changed. |
| Minor 6 | Reading/staffing/unpiloted status moved from the overview to p. 2 with preparation. |
| Minor 7 | Removed the repeated input/tally/output block; the actual printed demonstration is the visual reminder. The new p. 4 visual demonstrates the previously missing building procedure. |
| Minor 8 | P2 notes that D/E/F may also suggest “waiting wins,” but F beat both; P3 separates these reasons. |
| Minor 9 | Added an observation list: reached problem, voting with unavailable top choice, slip/two-mat handling, adult-chosen votes/waiting letters/builds; retained pointer to base p. 6. |
| Minor 10 | Later integration notes name base p. 2's three older kits, p. 6 Print map, and the Week 87 catalog record, alongside replacing the obsolete p. 1 adult-led route. No integration performed. |
| Minor 11 | Partners take turns circling on their one shared six-page packet. |
| Minor 12 | **Already sufficient; finding not reproduced.** The supplied `draft/src/check_guide.py` already walks ancestors looking specifically for `plans/k1-drafts/week-87/k-1.pdf`. Running the revised checker from `final/src/`, with no `k-1.pdf` beside it or in `final/`, successfully found and checked the repository student file. A clean detached copy also finds the adjacent student PDF. No redundant fallback was added. |

## Mathematics, references and materials

Rendered and read all **six final student pages**, all **six base-guide pages**, all **five materials pages**, and all four original draft-guide pages. Verified the final student map: P1 p. 1, P2 p. 2, P3 p. 3, P4 p. 4, P5/P6 p. 5, P7/P8 p. 6. Student PDF hash remains `02d7aed95f9d5fb4af5126e710494e54aee9a7f5bd217b551709920e1523ca47`.

`final/src/check_guide.py` passes. It reads actual final student card profiles/agenda starts and recomputes every printed answer. It verifies all nine P5 swaps and their upward-moving sole winner; the moved letter passes its previous defeating rival, turning that pair loss into a 2–1 win. All **216** ordered profiles satisfy the cycle-or-fixed-winner dichotomy and the beat-both iff theorem. The complete B-winning catalog is **68 ordered / 18 unordered profiles**. P7's two unordered sets and P8's zero no-B-first solutions are unchanged. No numerical answer was changed. New overview facts have elementary arguments as well as finite checks.

The preserved independent critic checker was rerun without modification: **58 checks, zero failures**, including PDF-extracted profiles and digital dimensions. One pair's kit is correctly counted as three fixed 45 × 80 mm cards, six 28 mm option tiles (two each A/B/C), three 18 mm V1–V3 tokens with V4/V5 set aside, one whole materials p. 4 (170 × 90 mm tally mat, 175 × 100 mm knockout mat, 54 mm wells), and, for later problems, three blank cards/eighteen 21 mm slips from p. 2. Nine slips are used at once; remaining slips are spares. Two K–1 pairs require two copies each of materials pp. 1/4, plus p. 2 for building. Printed card rows are about 23.3 mm; fit is digital only. Temporary six D/E/F labels remain adult-made, not falsely claimed as printables.

## Build and visual QA

`bash final/src/build.sh` succeeds, rejects errors, overfull boxes, LaTeX/package warnings and missing characters, and ends with the checker. The final guide has five pages so the new restart/building demonstration and later proof conversations have readable space. Every final page was rendered with **Poppler pdftoppm** and inspected: headers/footers, table fit, mathematical symbols, construction diagram, margins, section transitions and page numbers are legible with no clipping or overlaps. Student, base and materials pages were also inspected using Poppler; PyMuPDF was used only as a supplementary initial renderer/text reader.

A clean copy of only `final/src/` plus the unchanged student `k-1.pdf`, outside the repository under `/tmp`, rebuilt successfully; the checker passed and **PDF bytes and extracted text matched exactly**. Rendering/build/recheck scratch is outside the repository in `/tmp/k187-qa`. No absolute machine paths are embedded in portable source.

Final guide SHA-256: `668ee9f3a8e19a29242b0a8f0ed3e7513b85c143e3c91f4d6387df827d71690b`.

## Student-page issues and limits

No mathematical student-page error was found. The adult guide works around the half-size frames on pp. 5–6 (22.5 × 40 mm, too small for 21 mm slips) by using them only for adult pencil records, and uses the real cut cards instead of P5's 27 × 48 mm pictures. P3/P4 full-size card pictures replace the cut cards while voting; repeated identical rankings are still separate voters. The second visit's line-launch mismatch is handled by a K–1 restart. Two-mat handling, tight slip fit, optional dots/covers, cuts, resets and timings remain untested.

The existing base guide's “no independent K–1 packet” route, preparation, print map and catalog must be synchronized only in later packaging. **Untested with children and physically unrehearsed.** Mathematical/digital verification does not establish classroom independence, physical fit or readiness. No private source was needed or newly consulted for this bounded revision. Packaging and integration remain deferred pending the separate catalog task.
