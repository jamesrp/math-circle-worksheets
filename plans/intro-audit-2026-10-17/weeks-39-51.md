# Weeks 39–51 introduction audit

All 52 current student PDFs were inventoried against `WEEKS-11-51.md` and `BONUS-AND-RETURN-VISITS.md`: 39 base packets (all three bands for each of 13 weeks) and 13 released bonus companions. No other current student companion appears in these week folders or relevant index entries. Archives, adult guides and duplicate source reference PDFs were excluded from student coverage. The audit used the parent’s claimed worktree on `audit/introductions-2026-10-17`, canonical origin `git@github.com:jamesrp/math-circle-worksheets.git`. No repository files were changed.

Every current first page was rendered and visually inspected. Every page of all 13 bonus PDFs was visually inspected, including each internal grade-band introduction. Nine additional base pages were visually inspected where the opening or a changed representation needed checking: Week 40 p2 in all bands; Week 41 grades 4–5 p4; Week 42 K–1 pp2–3 and grades 2–3 p2; Week 49 K–1 p2; Week 51 K–1 p4. Total: 87 distinct student PDF pages. `coverage.json` records exact pages; unlisted later base pages were not visually audited. Extracted text supported targeted follow-up, but is not counted as visual coverage.

## Prioritized findings

### 1. Week 45 bonus, grades 4–5, page 2: the host example misses the mechanism children must compare

The opening introduces a fixed initial choice, random prize, independent ticket, informed host’s conditional use of that ticket, blind host, discarded prize reveals, secrecy and stay/switch. The worked picture only shows “choose P, prize R; Host A opens Q.” There is no ticket, no Host B attempt and no displayed stay/switch outcome. A child may understand that an empty door opens yet still use the ticket for Host A when it would reveal the prize, retain Host B’s prize reveal, or not know which remaining choice is “switch.” The adult launch repeats the same partial P/Q/R example (bonus guide p2); it does not explicitly demonstrate the contrasting protocol.

Minimal fix: replace the existing picture with a single unchanged prize/ticket input shown under both hosts, continuing to the open door and result. For example, first choose door 1, prize at 2, ticket 2: Host A must open 3, and switching wins; Host B opens 2, so the trial is discarded. Keep the full six-story enumeration for children. A carefully chosen live enactment can supply this in a session, but the printed protocol should retain the contrast so children can check their own later cases. Severity: moderate procedural clarity concern, not a mathematical error or a reason to remove the investigation.

### 2. Week 42 bonus, grades 2–5, page 3: “whole pair fair” has two plausible meanings

The task asks for one cup giving only two possible pairs and another giving all four, then asks whether fairness at each position makes “the whole pair fair.” A child whose first cup gives square-square and circle-circle equally often can reasonably call the pair fair among its possible results. The intended conclusion uses equal chances across all four ordered pairs, including the two impossible ones; that meaning appears in the adult explanation but is not stated in the child question.

Minimal fix: replace the last question with “Does fairness at each position make all four shape pairs equally likely?” No added diagram or worked solution is needed. A teacher can resolve it with one sentence, but printing the intended comparison avoids a vocabulary dispute. Severity: low; the construction itself is concrete and clear.

## Demo-dependent cases, not recommended as defects

- Week 49 K–1 p1 uses numerals, “gap,” and arrow-tail language rather than pictured cube towers. However, the worked old/new ring is complete, p2 provides large separate old/new working mats, and guide p1 explicitly has children compare towers and build all four new gaps without changing the old ring. The normal prescribed demo supplies the physical meaning. A small tower-pair sketch could improve recall, but numeral format alone is not evidence of failure. Check in piloting whether children independently preserve the old state after the launch.
- Week 51 all base bands p1 relies on real sliding strips with sleeves or cover cards. The guide p1 specifies those materials and demonstrates a legal hidden endpoint and both extremes; the student page illustrates the resulting joins. With the prepared strips, the purpose and legal action are clear. A bare PDF without those materials would not establish the intended activity, but that is a preparation dependency, not a missing packet rule.
- Week 40 all base bands pp1–2 explicitly traces arcs and contrasts valid/invalid crossings. Identifying strands still benefits from a normal cord demonstration. The essential convention is already printed; adding another generic worked example is unnecessary.

## Representative positive examples

- Week 47, all base bands p1: cube stacks → one marker in each column → number row, with allowed and too-large jumps. The visual preserves the physical meaning through the change in representation.
- Week 46, all base bands p1: the same blue-setting instruction acts on both rows, including a slot already blue. It demonstrates the subtle rule rather than merely displaying a typical change.
- Week 44, all base bands p1: draw, return and add a copy are distinct visible stages. Grades 4–5 also introduces marked counter identity before asking for marked histories.
- Week 43 bonus pp2–3: a cut and an insertion have compact input/action/output examples that teach only the operation, leaving the substantial classification to children.
- Week 41 base p1 and bonus p2: a wrap is tied explicitly to arrival in the neighboring copy, preserving the meaning of both representations.

## Limits

These are independent desk-review judgments, not observations of children. No physical procedure was rehearsed, no full mathematical solution audit was attempted, and no packet was rebuilt or edited. No required student opening remains uninspected in Weeks 39–51. Later base pages outside the listed visual checks remain outside this introduction-focused review. The audit does not treat difficult proofs, adult reading or a reasonable physical launch as failures.

## Complete per-PDF coverage

| PDF | Type | Visually inspected pages | Judgment |
|---|---|---|---|
| lowell-math-circle-year-2/week-39/week-39-k-1.pdf | base | 1 | clear |
| lowell-math-circle-year-2/week-39/week-39-grades-2-3.pdf | base | 1 | clear |
| lowell-math-circle-year-2/week-39/week-39-grades-4-5.pdf | base | 1 | clear |
| lowell-math-circle-year-2/week-39/week-39-bonus.pdf | companion | 1, 2, 3 | clear |
| lowell-math-circle-year-2/week-40/week-40-k-1.pdf | base | 1, 2 | clear |
| lowell-math-circle-year-2/week-40/week-40-grades-2-3.pdf | base | 1, 2 | clear |
| lowell-math-circle-year-2/week-40/week-40-grades-4-5.pdf | base | 1, 2 | clear |
| lowell-math-circle-year-2/week-40/week-40-bonus.pdf | companion | 1, 2, 3 | clear |
| lowell-math-circle-year-2/week-41/week-41-k-1.pdf | base | 1 | clear |
| lowell-math-circle-year-2/week-41/week-41-grades-2-3.pdf | base | 1 | clear |
| lowell-math-circle-year-2/week-41/week-41-grades-4-5.pdf | base | 1, 4 | clear |
| lowell-math-circle-year-2/week-41/week-41-bonus.pdf | companion | 1, 2, 3 | clear |
| lowell-math-circle-year-2/week-42/week-42-k-1.pdf | base | 1, 2, 3 | clear |
| lowell-math-circle-year-2/week-42/week-42-grades-2-3.pdf | base | 1, 2 | clear |
| lowell-math-circle-year-2/week-42/week-42-grades-4-5.pdf | base | 1 | clear |
| lowell-math-circle-year-2/week-42/week-42-bonus.pdf | companion | 1, 2, 3 | concern |
| lowell-math-circle-year-2/week-43/week-43-k-1.pdf | base | 1 | clear |
| lowell-math-circle-year-2/week-43/week-43-grades-2-3.pdf | base | 1 | clear |
| lowell-math-circle-year-2/week-43/week-43-grades-4-5.pdf | base | 1 | clear |
| lowell-math-circle-year-2/week-43/week-43-bonus.pdf | companion | 1, 2, 3 | clear |
| lowell-math-circle-year-2/week-44/week-44-k-1.pdf | base | 1 | clear |
| lowell-math-circle-year-2/week-44/week-44-grades-2-3.pdf | base | 1 | clear |
| lowell-math-circle-year-2/week-44/week-44-grades-4-5.pdf | base | 1 | clear |
| lowell-math-circle-year-2/week-44/week-44-bonus.pdf | companion | 1, 2, 3 | clear |
| lowell-math-circle-year-2/week-45/week-45-k-1.pdf | base | 1 | clear |
| lowell-math-circle-year-2/week-45/week-45-grades-2-3.pdf | base | 1 | clear |
| lowell-math-circle-year-2/week-45/week-45-grades-4-5.pdf | base | 1 | clear |
| lowell-math-circle-year-2/week-45/week-45-bonus.pdf | companion | 1, 2, 3 | concern |
| lowell-math-circle-year-2/week-46/week-46-k-1.pdf | base | 1 | clear |
| lowell-math-circle-year-2/week-46/week-46-grades-2-3.pdf | base | 1 | clear |
| lowell-math-circle-year-2/week-46/week-46-grades-4-5.pdf | base | 1 | clear |
| lowell-math-circle-year-2/week-46/week-46-bonus.pdf | companion | 1, 2, 3 | clear |
| lowell-math-circle-year-2/week-47/week-47-k-1.pdf | base | 1 | clear |
| lowell-math-circle-year-2/week-47/week-47-grades-2-3.pdf | base | 1 | clear |
| lowell-math-circle-year-2/week-47/week-47-grades-4-5.pdf | base | 1 | clear |
| lowell-math-circle-year-2/week-47/week-47-bonus.pdf | companion | 1, 2, 3 | clear |
| lowell-math-circle-year-2/week-48/week-48-k-1.pdf | base | 1 | clear |
| lowell-math-circle-year-2/week-48/week-48-grades-2-3.pdf | base | 1 | clear |
| lowell-math-circle-year-2/week-48/week-48-grades-4-5.pdf | base | 1 | clear |
| lowell-math-circle-year-2/week-48/week-48-bonus.pdf | companion | 1, 2, 3 | clear |
| lowell-math-circle-year-2/week-49/week-49-k-1.pdf | base | 1, 2 | clear |
| lowell-math-circle-year-2/week-49/week-49-grades-2-3.pdf | base | 1 | clear |
| lowell-math-circle-year-2/week-49/week-49-grades-4-5.pdf | base | 1 | clear |
| lowell-math-circle-year-2/week-49/week-49-bonus.pdf | companion | 1, 2, 3 | clear |
| lowell-math-circle-year-2/week-50/week-50-k-1.pdf | base | 1 | clear |
| lowell-math-circle-year-2/week-50/week-50-grades-2-3.pdf | base | 1 | clear |
| lowell-math-circle-year-2/week-50/week-50-grades-4-5.pdf | base | 1 | clear |
| lowell-math-circle-year-2/week-50/week-50-bonus.pdf | companion | 1, 2, 3 | clear |
| lowell-math-circle-year-2/week-51/week-51-k-1.pdf | base | 1, 4 | clear |
| lowell-math-circle-year-2/week-51/week-51-grades-2-3.pdf | base | 1 | clear |
| lowell-math-circle-year-2/week-51/week-51-grades-4-5.pdf | base | 1 | clear |
| lowell-math-circle-year-2/week-51/week-51-bonus.pdf | companion | 1, 2, 3 | clear |
