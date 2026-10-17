# Week 95 adversarial review

**Verdict: revise three focused issues, retaining the mathematical scope and two-band design.** The core is substantial and mathematically sound. No K–1 packet is required under the authorized override. The drafts are not ready to describe as fully meeting the worked-convention and closure requirements.

## Review scope and evidence

Read AGENTS.md, README.md, LOCAL-RESOURCES.md, the complete CRITIC.md and PROMPT.md, and the draft source README and verification script. Rendered and visually inspected every page of both draft PDFs, four pages each, at 90 dpi with PyMuPDF. Render evidence is in `critic-render/`. Ran `draft/src/verify.py`: PASS for identities, support ranges, repeated-record feasibility, ratio estimates, exact expectations through N=24, and budget optima 2–24. Independently checked the constructions and distinctions below. Did not edit student sources or PDFs. No physical rehearsal, child piloting, source-book research, or reconstruction from a source ZIP was performed by this critic.

| Packet | Pages checked | Finding |
|---|---|---|
| Grades 2–3 | 1–4 | Complete capture visual; clear identity tasks; printed variation; substantial feasible-overlap work. Clarify closure and constructive versus random trials. |
| Grades 4–5 | 1–4 | Complete capture visual; correct lower bounds, estimates, zero case, and optimization. Missing worked fraction convention; clarify closure. |

## Required revisions

### 1. High: fraction matching has no explicit worked convention before its first use

**Upper p.2, Problem 3.** The diagram presents the actual task's unknown total and the second catch of two marked objects out of six. It does not show what it means to make two marked fractions match. No input → meaningful intermediate representation → output is demonstrated. This is the precise unfamiliar-conversion bridge requested by AGENTS.md and the review brief. The words “marked fraction” and the target drawing assume children can already translate an unknown whole into equivalent proportions. The following page supplies ratio guesses, so an adult may end up explaining the whole operation for them.

Add one small **non-task** worked visual immediately before first use. For example: a second catch of one marked object among three; a whole bag with two marked objects; two equal three-object groups, each with one marked object; six total objects as the rule's **guess**. Label the relationship in matching words or fractions. This should demonstrate what the proposed rule does, without solving record A (6 marked, catch 6, overlap 2), claiming an exact recovered population, or giving a sequence of ratio drills. Retain Problem 3's counterexample construction. It provides the necessary challenge to the guessing rule.

### 2. Medium: “unchanged total” is weaker than a closed unchanged population

**Both p.1 shared rules.** “The keeper keeps the bag's total unchanged” technically permits exchanging individuals between catches while retaining the count. The complete worked visual correctly preserves A–F, and the later tasks repeatedly refer to one unchanged bag, but the activity-wide verbal rule should state the actual assumption.

Replace the count-only condition with a short rule that the **same objects stay in the population throughout the series**, with nothing added, removed, or exchanged except the temporary catches that are fully returned. Do not add a long assumption checklist. Preserve the existing useful rules: equal chance for every group of the chosen size irrespective of marks, keeping each catch out, full first-catch return and mixing, retention through both catches, and clearing marks only before the next round. The sample model is explicitly stronger than merely drawing without looking; the existing equal-group-chance sentence is good and should remain.

### 3. Medium: a possibility task can become a long wait for a rare random sample

**Lower p.3, Problem 5; interaction with p.1 shared rules.** “Try rounds … Can either bag give both an overlap of 0 and an overlap of 3? Use your objects to settle it” follows the blanket rule to draw without looking. The intended result is constructive possibility, but children may reasonably think they must wait for each event to occur randomly. With an eight-object bag and two catches of four, overlap zero has probability 1/70. With sixteen objects, overlap three has probability 48/1820, about 1 in 38. Neither is a reliable classroom waiting task. Failure to see a result is also not evidence of impossibility.

Make explicit that children may **arrange legal catches** to settle possibility, while blind draws are for the sampling trials. This can be a concise local revision to Problem 5; apply the same distinction consistently wherever a child builds a possible record. Keep the requirement that each arranged catch uses distinct objects and that both catches come from the same population. Lower Problem 6 already explicitly says “Arrange catches,” which is the right direction. Do not replace the problem with extra random repetitions or a probability calculation.

## Preserve these strengths

- **Complete shared operation, both p.1:** the visual shows six unmarked identities A–F; A,C captured and marked; both returned into the same six-object population and mixed; C,D,F recaptured while A,B,E remain; C identified as the one overlap. The first-catch and second-catch partitions and marked status are consistent. This meets the complete same-population visual requirement and precedes the first task. Its compact scale is suitable for illustration, not manipulatives; the README explicitly says diagrams are not cutouts.
- **Printed variability, lower p.3:** overlaps 2,1,3,1,2,0 are feasible for either N=8 or N=16. Asking for guesses does not promise certainty. The combined record does not have a uniquely forced answer. Its average overlap 1.5 lies between the model means 2 and 1; do not invent a required averaging argument that “proves” one choice. Keep room for reasoned guesses and discussion of their limitations, without introducing likelihood arithmetic for this band.
- **Printed variability, upper p.3:** the records all fit one unchanged N=18 population, yet the proposed rule returns 36,18,12,18, and no matching total. This is an effective concrete demonstration that an estimate need not equal the truth. The source README honestly identifies both printed series as invented illustrative records, not collected data.
- **Certain bounds versus guesses:** lower Problem 2 has exactly seven observed identities, so 7,8,12,20 are possible and 6 is not. Lower Problem 3 needs ten and has no finite upper bound. Upper Problem 2 needs ten for overlap two and twelve for overlap zero; neither has a finite upper bound without an external cap. Upper Problem 3's guess is 18, while a population of ten is a concrete alternative. These are sharp and purposeful contrasts.
- **Zero overlap:** upper Problem 5 correctly challenges the nonexistent ratio estimate. Finite populations of 12 and 18 both work. Do not replace “No matching total” in the rule column with “infinite population”; the current wording is correct in its column context.
- **Exact late depth:** lower Problem 6's overlap sets are {3,4}, {1,2,3,4}, and {0,1,2,3,4} for N=6,8,12. Inventing an impossible partner record follows naturally. This is concrete extremal/set reasoning, not routine arithmetic.
- **Experimental design:** upper Problems 6–7 specify a feasible population N=24 and budgets at most 24. Under the uniform-subset model the expected overlap is Mn/24; balance maximizes the product. Budget 12 gives 6+6, budget 13 gives 6+7 in either order, budget 20 gives 10+10. An adjacent balancing move increases the product by n−m−1 when n≥m+2. The wording asks for greatest average overlap, not universal estimator quality. Preserve this substantial exact destination. Giving the expectation as an available fact still leaves a meaningful optimization and explanation.
- **Model failure:** upper Problem 8 adds a worthwhile distinction between variation and failed mark retention. Fewer retained observed marks can inflate a positive ratio guess or cause zero overlap. Designing a check is meaningful late work; it need not be completed in the first session.

## Age fit, presentation, and remaining cautions

Both packets have consecutive numbering, consistent headers and footers, no Name/Date fields, no extra titles, and ample usable recording space. All eight rendered pages have legible text and diagrams, with no clipping or overlaps observed. The large white areas are legitimate working space and do not justify adding filler.

Grades 2–3 has an honest concrete core: matching identities, making compatible populations, arranging possible and impossible overlaps. Initial live guesses are exploratory; do not evaluate them as hidden numerical answers. Adult reading and help resetting erasable marks are realistic. The random-versus-constructed distinction above is the main operational risk, not a reason to remove the mathematics.

Grades 4–5 needs multiplication, division/equivalent fractions, and willingness to distinguish possible from typical. Once the fraction bridge is added, the packet retains meaningful choices in counterexamples, reporting uncertainty, allocating catches, and testing mark loss. Problems 6–8 can support a return visit. These are readiness judgments, not child-tested findings. Avoid making every printed page a required one-hour route.

The source README records realistic unrehearsed preparation limits: identical tactile materials, erasable marks, mixing, and reset have not been physically tried. Digital correctness does not establish uniform physical sampling. Keep those limits visible in the later facilitator material; no new facilitator guide is requested in this review stage.
