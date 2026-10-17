# Independent mathematical review A: Weeks 85, 86, 87 and 91

Reviewer role: independent mathematics reviewer, not a writer. Reviewed the complete four family drafts and their corresponding claims in the consolidated root overview, with separately derived proofs and an independent Python checker. No author checker was imported. Weeks 88–90 are outside this reviewer's assigned mathematical scope. This report is a planning review; it does not certify finished PDFs, material fit, hardware operation or classroom piloting.

Final disposition: accepted as mathematical planning outlines. All six findings below have been resolved in the final root files, and no mathematical blocker remains within this reviewer's assigned scope. This acceptance does not certify physical hardware, rendered pages or classroom suitability. Original input fingerprints are preserved in `reviewed-input-fingerprints.json`; accepted root-file fingerprints are in `final-root-fingerprints.json`.

## Findings and final disposition

| Finding | Final-file resolution |
| --- | --- |
| M1 | Week 86 P2 retains c as the two-move T2 start and removes the incorrect f bound. |
| M2 | Week 87 P4 gives `(3, 2, 0)` for both challengers 1 and 2. |
| M3 | Week 91 explicitly applies the divisibility argument to `5(R−s)`. |
| M4 | Week 85 specifies a 450 × 400 mm support, centers the mat, discloses the Q-joint counterexample and retains the physical rehearsal gate. The continuous ideal geometry now fits; see below. |
| M5 | Week 87 calls the Black scan an academic-hosted copy. |
| M6 | Week 86 trees use separate 170 × 105 mm apparatus sheets. The three ring boards also have an explicit arrangement. |

The following paragraphs preserve what was found in the earlier drafts and why it mattered.

**M1 — Week 86, Problem 2 solution, incorrect supplementary capture bound; medium.** The draft says tree T2 can be caught within two cop moves from c or f. From f to endpoint a (or e) is three edges: f–c–b–a. A robber placed there and staying forces at least three cop moves. The independently solved game has worst-case bounds c=2 and f=3. Retain c as the two-move start; describe f as three if it is mentioned. The page's main tree-capture task and shrinking-component proof are correct.

**M2 — Week 87, Problem 4 solution, two incorrect keyed vote triples; medium.** With fixed favorites 0, 2, 4, 7, 10 and candidate 4, both challenger 1 and challenger 2 give `(3 for 4, 2 for challenger, 0 tied)`. The draft says challenger 1=(4, 1, 0) and challenger 2=(3, 1, 1). All other listed challenger triples are correct. Correct these two entries and remove the draft instruction to recompute them. Median 4 remains the correct unique universal winner.

**M3 — Week 91, encore Problem 2 proof, divisibility assigned to wrong quantity; medium.** The sentence saying the number of right exits differs from s only by a multiple of 5 is not the deduction from the invariant. Five times that difference, `5(R−s)=S_initial−S_final`, is an integer multiple of 5 lying between −4 and 4. Therefore it is zero and R = s. The theorem and its invariant are correct; fix this sentence so the adult explanation proves the intended claim.

**M4 — Week 85, support-board specification, an ideal joint leaves the proposed board; medium material-geometry finding.** Stable draft half-bars have length 80 mm, anchor O=(40,140), and nominal tracer zone includes T=(110,140). The two simple-rhombus solutions give Q=(110,140±2√(80²−35²)), approximately (110,−3.88) and (110,283.88). Neither Q center fits a 279/280 mm-high supporting board, even before bar-end/width margins. The plan honestly says physical rehearsal is untested, but its proposed support dimensions should accommodate its mathematical poses. A 450×360 mm board with the 432×279 mm joined mat vertically centered is a plausible correction, or restrict/reposition the tracer zone and verify it. This is an exact geometric counterexample to the 280 mm support proposal; it is not a physical test of hardware or accuracy.

**M5 — Week 87, primary-source paragraph, host attribution; low.** The Black article scan lives on Rohit Vaish's researcher site. Call it a researcher-hosted scan rather than an author-hosted copy; Duncan Black is the article author. The original article and page references are otherwise verified.

**M6 — Week 86, page 2 board dimension planning; low before production.** Each tree's supplied coordinates has a 64 mm vertical center span. A 19 mm circle makes at least 83 mm outer height, or 86 mm with 22 mm circles, before labels. Thus the general 170×80 mm board box is too short. Reserve a taller apparatus box or revise the geometry at production. This is separate from the mathematical correctness of the trees. Operational/page review should also reconcile the general “two boards per page” description with page 3's three actual ring boards.

## Earlier target findings resolved in the stable Week 85 draft

The preliminary draft centered the 80 mm arrow at O + (170, 0), extending 10 mm beyond the nominal output zone, and used a triangle vertex at x = 135 with the moved anchor at x = 70, below the proposed minimum anchor distance. The final version centers the arrow at O + (180, 0) and uses triangle vertices (140, 130), (160, 130), (150, 150). Those changes resolve both numeric containment concerns. House and flag coordinates, half-size inverses and 30 mm anchor/15 mm compensating input translations are correct.

The final 450 × 400 mm support also resolves M4. Its centered mat puts O at approximately (49, 200.5). Since OQ is 160 mm, Q's vertical coordinate lies between 40.5 and 360.5 mm. A strip-end/width allowance of √(11² + 9²), about 14.21 mm, still fits the 400 mm height. In the nominal tracer rectangle relative to O, x lies in [70, 120] and y in [−25, 25]. The alternate Q coordinates are `(x ∓ y√(160²/(x²+y²)−1), y ± x√(160²/(x²+y²)−1))`. Their x coordinate is conservatively at least 18.62 mm relative to O; the other joint and pen coordinates remain inside the same board with the strip margin. Straight ideal bar segments lie between these contained endpoints. This continuous geometric check does not test sleeves, spacers, hands, tip offsets, branch changes or actual hardware.

## Coverage and accepted mathematical substance

| Family and task | Independent result |
|---|---|
| 85 shared convention visual | Correctly identifies fixed anchor, controlled tracer and output point without printing a scale recipe. |
| 85 P1 | 30 mm segment copies to 60 mm; 20/15 mm elbow to 40/30 mm; 20×15 mm rectangle to 40×30 mm. |
| 85 P2 and P4 | No legal ideal counterexample to collinearity/2:1 law. Directed-half-bar proof and the alternative similar-triangle proof are valid on the simple parallelogram branch. |
| 85 P3 | All listed house vertices halve correctly, including roof height 17.5 mm. Flag halves and safe ideal reach are valid. |
| 85 encore P1 | Original areas 4, 3, 2 units produce 16, 12, 8 units. Square and triangle dissection proves the scale factor for these examples. |
| 85 encore P2/P3 | Inverse scale 1/2; angle/orientation preserved; distinct fixed anchors shift output oppositely;15 mm input shift offsets 30 mm anchor shift. |
| 86 convention visual and P1 | Placement/timing/stay rules agree. Five/seven paths have optimal center starts and worst-case 2/3 cop moves. |
| 86 P2 | Actual T1/T2 are trees. Greedy unique-path pursuit wins; a component strictly shrinks. The incorrect supplementary f bound was removed under M1. |
| 86 P3 | C4/C5/C6 evasion invariant is valid including stays; triangle is catchable. No claim about every graph containing a cycle is made. |
| 86 P4 | C4 minimum one diagonal; C5 minimum two suitable chords. Every one-chord C5 retracts onto C4. All five single-chord cases and all ten two-chord pairs were checked independently. Only five two-chord pairs win, so accepting a child's pair requires the stated strategy check. |
| 86 P5 | Triangle with three-edge tail is a six-vertex, six-edge cop-win example; C6 is a matching robber-win example. |
| 86 P6 | F1 stated fold sequence is legal. F2 initially permits only b→a or b→c, then leaves C4. Shadow capture sufficiency and no-dominated-vertex evasion necessity are correct with closed neighborhoods and stays. |
| 86 P7 | Stationary blocker plus path chaser catches on every finite cycle under the two-cop turn convention; no general two-cop theorem is claimed. |
| 87 worked visuals and P1/P2 | D/E/F votes and bracket are correct. ABC/BCA/CAB gives the 2–1 cycle. Bye A/B/C respectively wins A/B/C under sincere votes. |
| 87 P3 | ABC/ACB/BAC always elects A. ACB/CBA/BAC reverses the majority cycle and permits all three bye winners. |
| 87 P4 | Winner 4 and uniqueness proof are correct. Ten actual challenger counts checked; the two incorrect entries were corrected under M2. Zero favorite is included as a full voter. |
| 87 P5 | Third favorite with multiplicity strictly beats every distinct challenger when it is offered; repeated favorites and other voters' ties are handled correctly. 100,842 small ideal/challenger cases checked. |
| 87 P6 | For favorites 1, 3, 7, 9, integer weak winners are exactly 3, 4, 5, 6, 7; there is no strict universal winner. All 55 integer pairings checked. Continuous interval proof is valid. |
| 87 P7 | Middle candidate cannot be strictly last for a distance voter. Since each candidate is last on one cycle card, no common line realization exists. |
| 91 both convention visuals | Follow then flip is consistent. Road example 2→1→2→3 ends both cards next-left. |
| 91 first-visit P1 | Seven gives 4–3 or 3–4; twelve gives 6–6. Local count difference at most 1. |
| 91 first-visit P2/P3 | ACB and AECG are uniquely programmed by all-left states. ABC on depth 2 and first outputs AB on depth 3 are impossible. Full depth 3 word is A, E, C, G, B, F, D, H. |
| 91 first-visit P4 | Every eight consecutive inputs visit each leaf once and restore all seven cards, from all 128 initial configurations. The theorem assumes downward edges, complete equal-depth binary tree, persistent switches and one completed chip at a time. |
| 91 encore P1 | At entry 2 on 0…4, all-left word is LRLRLRLR; the two stated paths and state reset are correct. Every particle terminates. Arbitrary bit configurations need not return after a block. |
| 91 encore P2 | Every five inputs at entry s send exactly s right, for every starting state, immediately. Stated all-left words LLLLR, LLRLR, LRLRR, LRRRR check. The local divisibility wording was corrected under M3. |
| 91 encore P3 | A coin can produce XX; an alternating switch cannot. Exactly two six-words versus 64 independent fair-coin words is correct. Optional path probability s/m follows from the harmonic boundary equation; randomness/independence are not inferred from balance. |

## Explicit resolution of the parent concern about arbitrary path states

The exact block claim requires no recurrent-state restriction, burn-in or eventually-periodic qualification. Use vertices 0,…,m, so m counts **edges**, input s satisfies 1≤s≤m−1, endpoints absorb, and every internal card displays its next exit. Each departure preserves moving-chip position+S, where S is the number of next-right cards. Across n finished launches:

`m R + S_final = n s + S_initial`.

A walk cannot be infinite: some internal vertex would be visited infinitely often; alternation would force infinitely many visits to both neighbors and eventually to a sink. Thus the invariant applies to completed launches. For n = m, `m(R−s)=S_initial−S_final`, and the right side has absolute value at most m−1. Integrality forces R = s. The same argument applies from the state at the start of **any** consecutive block.

This does not say every arrow configuration returns after m launches. On 0–1–2–3–4 with entry 1, initial LLR gives LLRL and changes to RLL after four. Immediate exit-count balance holds nevertheless. In contrast, every depth 3 binary-tree state does return after eight because each card receives an even number of visits. The consolidated overview states these distinctions correctly.

Independent checker coverage: m=2,…,8; every 2^(m−1) next-exit configuration; every interior input; first and second m-blocks; potential conservation and discrepancy at every prefix through 2m launches. Total 1,538 path/configuration/input cases. This finite evidence supplements the proof; it is not the proof of all m.

## Sources and claim boundaries

Inspected primary sources: Whitney's MoMath pantograph construction/use paragraphs; Azizi/Chung's game description, tree/cycle examples and fold theorem; Stodder's sincere agenda-setting section; Black's original Section II journal pp. 26–28; Acemoglu's instructor-authored MIT slides 20–23; Holroyd–Propp's rotor definition and §1.1 Theorem 1; Levine's rotor definition and Lemma 1.1, §§1–3. Links and locators are in the family files and `kernel-derivations.md`. Publisher access to the complete Nowakowski–Winkler paper was unavailable to this reviewer; no full-paper audit is claimed. The family itself discloses its limited publisher inspection and supplies the complete elementary arguments.

The binary bundle theorem and fixed absorbing-path potential proof are independently checked elementary specializations; they are not falsely presented as verbatim worksheet examples from the research papers. Levine's 2004 growing occupied interval differs from the fixed absorbing road. Source claims about pedagogy do not certify K–5 suitability. The complete physical pantograph kit remains an untested construction despite valid ideal geometry.

## Reproducibility and remaining limits

Run `python3 independent_checks.py` in this directory. `independent-results.json` records the actual boards, bounds, folds, ballots, programmed words, path traces, score checks, the original pantograph clearance counterexample and the corrected ideal support bounds. Checks use only standard Python, with no author-code imports. `kernel-derivations.md` documents separate primary-source/theorem derivations begun before the writers' drafts were available.

This reviewer accepts the scope: independent K–1 packets are not forced, nontrivial proof work may take another visit, optional folding/score/probability arguments are gated, and randomness is distinguished from deterministic balance. Rehearsal of coaxial hardware and arrows, adult workload, final diagram rendering, clean source-ZIP rebuilds, organizer approval and classroom piloting remain untested or future production steps. Those are honest stated limits rather than mathematical blockers to planning.

## Final accepted file fingerprints

The complete drafts were read before review, and corrected final passages were re-read. The final README route-map addition was also inspected: 7 + 7 + 7 + 7 + 9 + 7 + 7 = 51 planned problem pages, and the mathematical paragraphs remain unchanged. These SHA-256 fingerprints identify the accepted root versions; changes after these hashes require proportionate review.

| File | SHA-256 |
| --- | --- |
| README.md | `aa8c65ed694dfb5637480575a5d6a363808fb710a07ab09e65c70e25c117ffea` |
| week-85-drawing-machines.md | `864de2c3a48527ca633e36ca297797887fd8fe56759ac870bf0b851ad623cf21` |
| week-86-pursuit-and-escape.md | `08a0352b76adf9d79c421f52d59f91f602dc1533cdf36ce1de1168b9be4320c2` |
| week-87-voting-and-agendas.md | `428791518a16c9693260871793c9d24947a46d3bf3dffbafc7e81ab9af69ed8b` |
| week-91-rotor-router-machines.md | `c07a4fc13bd09cfff4815ab84531cc736b0c602f73f9d538121c0343074bead0` |
