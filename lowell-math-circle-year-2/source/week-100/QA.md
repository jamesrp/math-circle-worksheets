# Week 100 verification and readiness

Release date: October 17, 2026. **Prepared for organizer review; unpiloted.** Topic approval authorized production, not approval of the final worksheet or evidence of classroom use. Physical printing, preparation, handling, staffing and timing have not been rehearsed.

## Exact coverage

8 pages for Grades 3–5; 5-page facilitator guide. Each output has a matching current reference copy. Grade labels are approximate prerequisites; no K–1 packet is claimed. Read the guide's entry requirements and first-visit route before choosing pages.

## Independent stages and integration

A fresh writer, adversarial critic, mathematical reviewer and reviser completed the repository's prescribed student workflow. A recorded band-only override used the approved honest levels without changing shared templates. The adult guide was authored separately, opens with actual theorems and limits, and received an independent full student–guide review. Guide authoring is an untested addition to the tested student workflow.

Swapped C/D only in the earlier visible world so it no longer supplies the later reconstruction solution. Hidden clues remain unchanged. Added the complete non-task 1-and-5 remainder-to-distance example; updated final answers, checker transcription and snapshot hashes.

Detailed review reports are retained separately and are not included in this public release. Since October 23, 2026 the student pages' source is the problem files (`week.toml`, `template.tex`, `problems/`); `student/regenerate.py` writes the packet TeX from them, and the conversion changed no page (same text and 100-dpi pixels). The guide's source is still `guide/*.tex`.

## Mathematics

Independent checks cover all 59,049 five-card distance assignments, all 2,471 six-card worlds, the 20 candidate clue repairs, all number pairs/triples/balls, and 15 worst-case query witnesses. The guide proves the general strong inequality, ball and reconstruction claims.

Run `python3 check_math.py`. The standard-library checker writes JSON to standard output and does not mutate the source package. Its finite results support the pictured cases; the guide's arguments establish the general statements. Source citations and boundaries are in [SOURCES.md](SOURCES.md).

## Digital release tests

- Every final student and facilitator page rendered and visually inspected, including labels, board geometry, card counts, worked examples, response space and page numbering.
- Final student–guide mathematics and problem/page references checked together; no unresolved release issues.
- Build rejects TeX errors and overfull boxes; embedded fonts and US Letter page geometry checked.
- The adjacent source ZIP clean-extracted away from the checkout, then rebuilt using only its own sources and documented TeX/Python dependencies.
- SHA-256 equality required among each delivered PDF, reference PDF and clean-rebuilt PDF. The ZIP excludes prompts, borrowed exemplars, downloaded works, raw traces and build caches.

The repository [production record](../../../plans/final-topics-98-100/production/README.md) provides a verification summary and the exact file/page/hash manifest. That relative link is for a repository checkout; an extracted ZIP remains independently buildable without it. Digital evidence does not establish classroom success or physical readiness.
