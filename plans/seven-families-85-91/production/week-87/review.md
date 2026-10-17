# Week 87 adversarial review

Reviewed the actual draft PDFs: `shared.pdf` (3 pages), `line.pdf` (4), `upper.pdf` (2), and `materials.pdf` (5). I rendered and visually inspected all 14 pages, read the writer prompt, and checked exact construction in `draft/src/build.py` and the materials instructions in `draft/src/README.txt`. This is the critique stage only; no draft was edited. Independent mathematical review is separate.

## Verdict

Retain the investigations and their present band/visit distinctions. Revise the line-vote demonstration and two material details before treating the packet as ready for review. There is no basis here for removing the median explanation, four-voter question, or distance-model impossibility problem. There is deliberately no independent K–1 packet; that follows this week's outline.

## Required revisions

### 1. Show one complete multi-voter line comparison before Problem 1

**Location:** `line.pdf`, page 1, both worked strips.

Both strips demonstrate only V1: one nearer-proposal example and a separate equal-distance example. They correctly retain that one voter's input, but neither demonstrates the operation children must immediately perform with five fixed favorites: all five identities stay on the board while five separate vote tokens are distributed among X, Y and Tie, followed by an overall result. The outline expressly asks for fixed favorites and both proposals, each vote including ties, and the final tally. The current page goes directly from a one-token tally to finding a universal winner among eleven locations.

Replace or consolidate these strips into one complete, non-task five-voter comparison. Keep the input unchanged through the intermediate choices and final tally. Include a tied individual vote and show what the aggregate outcome means. For example, favorites 0,1,5,8,10 with proposals X=2 and Y=8 give V1/V2 to X, V3 to Tie, and V4/V5 to Y: a tied vote, 2 to 2, with one voter in Tie. This example does not reveal the task's median. Other verified non-task data are equally suitable. The demonstration should visibly distinguish fixed favorite markers from the vote tokens that move; do not add ongoing distance tables or extra recording demands to the investigations.

### 2. Supply persistent X/Y labels for the tally wells

**Locations:** `materials.pdf`, page 4 top mat and page 5 proposal pieces; `line.pdf`, page 1 rules.

The reusable tally mat has two wells labelled only "Option" and instructs children to put the two current option tiles above them. The card route supplies duplicate A/B/C tiles, so it can do this. The line route supplies exactly one X and one Y piece. Those pieces must remain at the two proposal locations on the number line while the votes are evaluated. Moving them to label the tally wells destroys the reference comparison. The line examples show labelled X/Y wells, but the actual mat does not provide that state without an improvised label or an unstated left-well convention.

Provide a second, clearly identified X/Y label pair for the tally, or a reusable X/Y-labelled tally treatment whose association is explicit. Keep the distinct proposal shapes on the board. Check the completed working state with both proposals still positioned, five fixed favorites visible, and all five vote tokens readable in their destination wells.

### 3. Give the tally tokens real clearance

**Locations:** `materials.pdf`, pages 1 and 4; `build.py`, `materials()`.

The supplied vote tokens are 18 mm circles. Each tally well is 54 mm wide, with three target centers 18 mm apart, at 9,27,45 mm from its left edge. Thus three real tokens exactly touch each other and both well boundaries. Moreover, the printed targets are 17 mm circles, smaller than the tokens. This is a digital fit at exact tangency, not the useful placement clearance requested for a hand-cut classroom material.

Adjust the target arrangement, well dimensions, or piece dimensions so that five votes fit in one well with positive gaps and boundary clearance. Keep all three destinations usable, including five votes for one proposal. Ensure the final printed target outlines match the intended pieces. A compact five-position arrangement or a slightly wider mat can solve this without enlarging every page. Physical cutting and placement remain untested until someone actually rehearses them; retain that qualification.

## Checked and worth preserving

- **Shared page 1:** The complete D/E/F profile remains visible, all three choices for the available D/E pair are explicit, and all three identities appear in the final tally. V3 correctly chooses E when its favorite F is unavailable. The ABC/BCA/CAB investigation is concise and mathematically substantive.
- **Shared page 2:** The D/E/F cards are unchanged across the knockout explanation. The sequence explicitly retains E, brings in waiting F, and puts losers Out. The worked outcomes agree with the displayed profile. Problem 2 lets children control the agenda and has useful result spaces.
- **Shared page 3:** Both profile-design tasks require three distinct rankings, with the fixed-card rule stated once. The blank cards support making and preserving a profile rather than repeatedly transcribing it. Preserve this design work.
- **Line pages 1–2:** The initial profile includes position zero as a voter. The later profiles include three coincident voters at zero, three at four, and an asymmetric distinct profile. These cases expose real distinctions. The duplicate identities are individually printed, and the separate reusable lanes retain their multiplicity.
- **Line pages 3–4:** The median question keeps explanation central. The even-voter route distinguishes never losing from strictly beating every other location and provides room for the interval of weak winners. It is suitable return work, not a reason to compress the earlier concrete comparisons.
- **Upper page 1:** The two profiles provide a genuine comparison between an agenda-independent winner and a cycle. The requested explanation can use pair results rather than a forced enumeration of agendas.
- **Upper page 2:** The conversion example uses one unchanged favorite and three letter locations; the distances 1,3,8 correctly produce D/E/F. The problem explicitly permits arbitrary locations and distinguishes ties from strict rankings, so a finite tick search is not misrepresented as an impossibility argument. Preserve the full common-line model-limit question.
- **Materials pages 1–3:** Fixed and blank ranking cards retain voter and rank labels within their cut boundaries. There are six blank cards and plentiful 21 mm letter slips. The row heights of the 45×80 mm cards permit those slips while retaining rank labels. All six 28 mm option tiles and five 18 mm vote tokens are actually supplied.
- **Materials page 4:** The knockout mat contains first pair, waiter, first winner, final pair, final winner, and Out space. The paired wells are large enough for two 28 mm tiles, and Out has room for both eliminated options. The remaining issue on this page is the tally, not the knockout dimensions.
- **Materials page 5:** The favorite markers are 13 mm across on separate lanes spaced 19 mm apart. Line ticks are spaced 16 mm. The 13 mm X square and 18 mm horizontal diagonal of Y can occupy adjacent ticks without overlapping (0.5 mm minimum edge gap). Coincident favorites remain separately identifiable. Favorite and proposal roles are explicitly separated. Do not replace this with stacked, indistinguishable counters.
- Across all four PDFs, problem numbering restarts consistently within each packet, headers/footers are present, and the rendered text and drawing bounds show no clipped content. The investigations leave room for independent attempts. There is no need to manufacture a fourth shared page simply to satisfy the generic workflow's page-count suggestion.

## Verification limit

This review concerns these 14 draft pages and their supplied materials, not other weeks or a facilitator guide. I checked the displayed worked examples and profile relationships while reviewing, but this document does not replace the separately assigned independent mathematics review. Digital dimensions do not establish cutting accuracy, assembly usability, timing, or classroom success. After revisions, inspect every changed rendered page and rehearse the complete line-vote state with the actual printed pieces before claiming physical readiness.
