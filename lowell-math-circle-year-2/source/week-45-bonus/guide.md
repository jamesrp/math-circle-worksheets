# Mathematical overview

Choose one of RR,RB,BB uniformly, keep that SAME card, and independently choose L/R faces with replacement for each of two clues. There are 3*2*2=12 equally likely histories. Red-red retains four RR histories and one RB history, so P(RR | red-red)=4/5. Red-blue retains exactly the RB/L-then-R history, so the card is RB with certainty; blue-red likewise forces RB. Blue-blue retains four BB and one RB history, giving BB chance 4/5. One red clue alone gives RR chance 2/3, so repeated evidence about the same object changes its posterior. Selecting a fresh card for each clue is a different experiment. The face tickets, orientation process and card identity must be hidden; knowing that the two red clues came from L then L would change the retained sample space.

In the three-door game, the first choice is fixed as door 1; the prize is uniform and independent of a uniform ticket 2/3. Host A knows the prize, always opens an unchosen empty door, and uses the ticket to break a tie only when both unchosen doors are empty. Switching wins in four of six equal histories, or 2/3; staying wins 1/3. Host B blindly opens the ticket's door. Conditioning on opening empty discards two histories and retains four: switching and staying each win in two, or 1/2. Before conditioning, blind switching wins 2/6, with 2/6 discarded. Only the opened empty door is public; prize placement, the prize-choice ticket and host ticket remain secret. The advertised clue is an empty opened door; the host's knowledge and tie rule are mathematical data, not optional story detail.

The noisy reporter chooses a uniformly hidden identity from R1,R2,R3,B and an independent uniform report ticket H1,H2,F. H1/H2 report true color, F flips it. A blue report has five compatible histories: three hide red and two blue. Thus red is the better guess, with chance 3/5, even though the reporter is honest in two thirds of all rounds. A red report has six true-red histories and one true-blue, giving red chance 6/7. With four equal report tickets, h honest and 4-h flipping, blue-report hidden weights are h for blue and 3(4-h) for red. They tie exactly when h=3. Reliability and conditional accuracy are different quantities. Keep the true counter identity and reporting ticket secret, showing only the R/B report. All claims use the stated prior identity multiplicities, independent ticket choice, and only the report as public information.

Grades 2-3 can reconstruct and filter twelve same-card histories. Grades 4-5 can compare host protocols and reverse-design a reporter. K-1 can match two faces and act a repeated clue while an adult sorts cases, but tracking a hidden object plus independent face tickets is not a compulsory younger version. Concrete table experiments generate data; complete equal-weight stories explain the exact conditional claims. No undergraduate prerequisites are needed.

# Materials, readiness, and flexible route

Per pair: RR,RB,BB equal-size opaque two-sided cards plus one separate GB demonstration card, marked L on the chart-left face and R on the chart-right face; identical covers for marks; a folder screen; two opaque cups; three equal-size door cards labeled 1,2,3; one prize token; counters R1,R2,R3,B; and fourteen equal-size paper tickets. Ticket sets are kept separate: three card-choice tickets RR/RB/BB, two face tickets L/R, three prize tickets 1/2/3, two host tickets 2/3, three reporter tickets H1/H2/F, plus one blank for the four-ticket design. Cups can be reused between investigations after an explicit reset. A pencil, one small initial-choice marker, two blank Letter sheets for explanation records, and three student pages complete the kit.

For eleven KK11 / 3333 / 445 children: five kits, twenty two-sided cards (five are non-task demonstrations), fifteen doors, five prize tokens, twenty source counters, seventy tickets, ten cups and five folder screens, five initial-choice markers and pencils; add two blank Letter sheets per kit (ten sheets) for returned-visit records or spoken count explanations. Use an existing small counter or scrap-paper marker on door 1. Cups can be reused/reset between investigations; three anchored adults at the fixed tables supervise hiding/resetting. The upper third child rotates as the host or history checker. Print five shared companions, or eleven selected recording pages. The tables are pencil record space; no physical counter-fit guarantee is claimed.

Check before use that cards have equal thickness and no show-through, covers conceal face marks identically, and the guesser cannot observe tickets or orientation. Door tickets must be drawn independently of prize placement. Host A privately checks prize placement; Host B must not peek, and the partner verifies blind ticket execution after the reveal. Reporter privately sees the true color but exposes only its R/B report. Distinguish two modes explicitly. For complete-story construction, choices can all be public: children select legal stories, enact them, and check the table. For hidden guessing rounds, use the screens/covers to expose exactly the stated clue, while keeping tickets/identities/placement/turning hidden. A publicly constructed example is not a guessing round. These tabletop checks have not yet been performed.

Launch together (4-6 minutes): handle two-sided cards openly first. On the separate GB card, choose L, show G, replace the face ticket, choose R, show B; keep the same card. Match input, intermediate tickets and two outputs to the printed visual. Restore the three target cards and hide choices. Do not give the 4:1 result. For the host page, use the printed P/Q/R demonstration: choose P, prize R, informed host opens Q, leaving P and R closed. Keep an initial-choice marker at P in both input and output (the printed black dots mark it); prize placement is public for this demonstration but secret in guessing rounds. For the reporter, show the printed non-target red-report example: hidden B plus F produces report R. These teach protocols without filling their full target catalogs.

A first return may spend 20-30 minutes on same-card evidence and stop after one exact filter. Host protocols and the reporter can each support a separate 20-35 minute return. Some children may prefer acting six complete door stories to calculating ratios. Adults may read and write children's spoken records, while children choose and check legal actions. Leave the general formula or independence analysis for readiness-dependent discussion. Finishing all three pages in one hour is unnecessary.

# Problem 1 (page 1)

The complete two-clue grid, rows card and columns face tickets, is:

| Card | L,L | L,R | R,L | R,R |
|---|---|---|---|---|
| RR | RR | RR | RR | RR |
| RB | RR | RB | BR | BB |
| BB | BB | BB | BB | BB |

Each face ticket is a fresh independent choice; its identity, the face marks and all turning stay hidden during guessing. Every cell has chance 1/12. Red-red: four cells in the RR row and one in the RB row, so RR is best at 4/5. Red-blue: only the RB row, L,R column, so RB is certain. Do not count surviving card TYPES as equally likely. Repeating the same face ticket is allowed and necessary in the experiment. It does not mean the card is reselected.

Hint only if needed: physically orient the same card twice for each table cell, retaining the row marker. Extension: n consecutive red clues give 2^n RR face-ticket sequences versus one RB sequence, so RR chance 2^n/(2^n+1). Prove by adding one more independent L/R choice, or construct the next finite grid. Mixed colors force RB at every length. This is an optional depth route within the same investigation.

New versus base: base Week 45 studies one visible face, changed face-ticket subsets and information leaks. This keeps one hidden object across multiple fresh clues and updates card-type evidence, not another single-face ticket-removal puzzle.

# Problem 2 (page 2)

The six equally likely prize/ticket histories and outcomes are:

| Prize | Ticket | Host A opens | A winning bet | Host B opens | B result |
|---:|---:|---:|---|---:|---|
| 1 | 2 | 2 | stay | 2 | stay |
| 1 | 3 | 3 | stay | 3 | stay |
| 2 | 2 | 3 | switch | 2 | discard |
| 2 | 3 | 3 | switch | 3 | switch |
| 3 | 2 | 2 | switch | 2 | switch |
| 3 | 3 | 2 | switch | 3 | discard |

For guessing, reveal only the opened empty door, never either choice ticket or prize placement. For A, switching wins whenever initial choice 1 was wrong, which has chance 2/3. Drawing a ticket even when it is ignored makes all six history rows explicit and equal-weight. For B, the two prize-revealing rows do not belong to the conditioned empty-clue sample space. Four remain, giving two switch and two stay wins. Neither bet is better there.

Hints: leave the initial-choice marker on door 1; enact each prize/ticket pair and mark a discarded blind round immediately. Ask why an ignored ticket still represents a possible equal-weight history. Extension: condition on specifically door 3 opening empty. Under A, prize 1 has one compatible ticket history and prize 2 two, giving switch chance 2/3. Under B, prize 1 and prize 2 each have one, giving 1/2. Another extension changes A's tie rule to always open 2 and asks whether the specific-open-door conditioning changes; the overall switching rate remains 2/3. State any changed tie rule before analyzing it.

New versus base: the base compares explicit orientation mechanisms on RR/RB/BB. This introduces an informed versus blind clue producer and conditioning on a reveal being empty, with discarded rounds and distinct complete host histories.

# Problem 3 (page 3)

Complete reports:

| Counter | H1 | H2 | F |
|---|---|---|---|
| R1 | R | R | B |
| R2 | R | R | B |
| R3 | R | R | B |
| B | B | B | R |

For guessing, reveal only the report, never the hidden counter identity or H/F ticket. Each cell has chance 1/12. A blue report retains R1/F,R2/F,R3/F,B/H1,B/H2. Red is the better hidden guess at 3/5; blue is 2/5. The reporter's 2/3 honesty does not equal P(true blue | report blue). The rare true blue starts with less prior weight.

For four report tickets, choose three honest and one flipping. There are sixteen equal hidden-counter/ticket histories. Blue reports then have three honest B histories and three flipped R histories, giving a tie. Completeness: with h honest tickets, blue histories weigh h and red histories 3(4-h); equality implies 4h=12, so h=3, and both classes are positive. Any placement of the one flipping ticket works. No guessing from finite trials is needed.

Hints: fill each actual report first, then retain just blue-report cells; do not treat “reported blue” as known blue truth. Extension: choose r red and b blue source counters and derive the honesty/flip ratio needed for a balanced blue report. The equation b*h=r*f has concrete equal-history meaning; fractions and Bayes notation are optional adult summaries. A perfect reporter has no false reports but can give conditional certainty; a zero-honesty reporter gives the opposite color certainly.

New versus base: base face clues are truthful visible colors produced by different choices. This clue can be false under an explicit reporting mechanism, and children redesign reporting reliability to balance a posterior against unequal prior multiplicities.

# Sources, checks, and use record

Original finite-history extensions of the current Week 45 model. Base bibliography names Brian Mintz, Dartmouth Graduate Student Seminar (Fall 2022), *Probability Paradoxes: Eleven Enlightening Examples*, as background. No specific exercise from those slides is attributed to this draft; same-card, host and reporter counts are independently derived here. Pedagogy consulted: *Math Circle by the Bay*, Preface pp. viii-x (PDF pp. 9-11), deep themes, manipulatives and flexible timing; the chosen encore designs are our inference. Week 1 encore and old extensions were read as models for substantive return visits.

`student/verify.py` enumerates every twelve-cell repeated-clue and reporter history, all six histories for both hosts, the worked examples and every four-ticket honesty count. The independent mathematics review confirmed every conditional count and redesign. All three final student pages were rendered and individually inspected after revision, including the information rules and non-task diagrams. Portable verifier and extracted-source byte-identical rebuild pass. **Unpiloted; hidden orientation, opacity, mixing, door execution and report-ticket physical pretests remain unperformed.**

Record date/adult, investigation actually used, procedure retained without rescue, selected histories, experiment/conjecture/explanation, questions and where to resume. One theme, three investigations; no prior use is claimed.
