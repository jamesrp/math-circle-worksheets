# Week 60: Take it or pass, student revision v2

Original editable student worksheet source, revised October 4, 2026 after a
fresh student-page critic and a separate mathematical critic. This package
contains no facilitator guide. Seven US Letter pages, single-sided at 100%.
Problems remain consecutive 1-9. All worksheet wording, ticket instances,
TikZ figures, outcome cards, build code and verification code are locally
authored adaptations; no source prose, figures or exercises are reproduced.
Problem 2 was expanded at revision. Page 1 now checks the compulsory-final
condition before removing a counter after the decision. Footer: `W60-S-v2`.

## Build and verify

```sh
python3 build.py /absolute/path/to/output-directory
python3 check_math.py
python3 check_pdf.py /absolute/path/to/output-directory/students.pdf
```

`build.py` writes `students.pdf` and `.build/` in the specified output directory,
which must be outside source. Mathematical checks use Python's standard library.
PDF checks need PyMuPDF and Pillow, available in the project's
`tmp/bonus-35-51-venv/bin/python`. Required TeX Live components: pdflatex,
article, geometry, fontenc, helvet, TikZ with arrows.meta, fancyhdr, array.
Fonts are TeX Helvetica. No external images, fonts, network or repository files
are needed. All diagrams are editable TikZ in `students.tex`.

`check_pdf.py` checks actual printed cards, counter circles, text bounds,
page labels and problem numbers; renders every page; copies source to a new
directory; creates/extracts a lean source ZIP to another new directory; and
builds both copies. Every page must reproduce identical extracted text, paper
dimensions and rendered pixels. Evidence, renders, ZIP and build intermediates
go below the PDF's sibling `qa/`, outside source. Visual inspection of all seven
final pages was completed at revision. Digital checks do not establish physical
handling or classroom fit.

## Prerequisites and page menu

The core route is **pages 1-3 and 6, Grades 3-5**. Offer page 6 without requiring
the upper proof pages first. Children compare 0,4,6, count two or three turns,
retain an irreversible take/pass decision and keep a fixed rule across several
possible offers. An adult may read and add pooled scores; children make/apply
decisions. Comparisons use totals over equally large collections, without
fractions. Problem 2 asks for possible offers with the same rules and separates
a sample from an exact average. A partner enforces legality. There is no new
K-1 entry or claim of independent third-grade accessibility.

**Pages 4-5 and 7, Grades 4-5**, are readiness-dependent continuation or later
visits. Page 4 requires averaging three/nine equal cases, with fractions or
adult-supported comparison against equal-sized batches of repeated 4s. Page 5
asks for a bound on every legal plan, including memory of passed scores. Page 7
requires fractional continuation averages and a general extra-offer argument.
If average conversion is unfamiliar, establish it with a brief non-target
concrete example before page 4. The worksheet assumes that prerequisite rather
than prescribing the target calculation. Finishing every page is not the goal.

## Preparation and tangible model

Three kits serve the two older tables: two pairs at the four-third-grader table
and a pair/trio with rotating referee at the 445 table. Each kit has an opaque
bag; three indistinguishable-size cardstock tickets 0,4,6 (about 40 by 60 mm);
separate visible distribution reference; three counters (four for Problem 8);
an erasable offer display independent of the bag tickets; TAKE and PASS places;
and pencil/eraser. New bags also need three equal-size tickets. Diagrams are
records, not fit-critical full-size boards.

Set the horizon/counters before drawing. The partner reveals the current offer;
the display copy preserves it while the randomizing ticket is returned and
mixed after every draw. Check the one-counter condition while deciding: that
current offer must be taken, including zero. Remove a counter after deciding.
Taking ends the round immediately; passes cannot be reclaimed. Position diagrams
count current plus possible future offers. Children never choose the next draw.

After initial handling, demonstrate a legal round briefly together. Page 1's
non-target 1,2,5 bag shows input 2/two counters, pass/return/mix/one counter,
then compulsory acceptance of 1. Page 2's 1,3,5 example shows full input 3/1,
early taking of 3 with unseen 1 retained, then score 3. Neither gives an optimal
target rule. Three-number cards use the same convention.

Photocopy pages 2,3,6 onto cardstock and cut dashed borders before use when
cards will move. They supply all nine 0/4/6 pairs, all 27 0/4/6 triples, and all
nine pairs for each new bag 0/3/6 and 0/5/6. Preserve every full word, unseen
tails and repeated accepted scores. Cards in each collection have equal size
and a separate score line. Score Plan A, save its labelled total, clear all
score lines, then score Plan B on the same complete set. Wipeable overlays are
an alternative requiring a physical pretest. Pool a complete table set; an
adult may add totals while children apply each legal decision. No child must
transcribe 27 words or supply an 81-word catalog.

Mixing/fairness, ticket indistinguishability, display handling, irreversible
passes, counter timing, final acceptance including zero, score erasing/reuse,
role rotation, actual staffing and child independence have **not been physically
rehearsed or classroom-piloted**. Rehearse the actual materials before use.
Plan A/B's four-point difference makes a complete checkable set and labelled
saved totals useful; digital checking does not verify handling with children.

## Mathematical/source provenance

`mathematics.md` states the theorem, assumptions, exact task outcomes and revised
Problem 2 counterexamples. `check_math.py` independently enumerates all
deterministic history policies at two/three offers for all three bags. At four
offers it enumerates only 512 current-score/turn policies; backward induction
establishes the bound for all legal policies. It does not enumerate all 2^39
four-offer history policies. Independence, replacement, known distribution,
fixed horizon, no recall/fees and expected one accepted score are essential.

Established mathematics: Thomas S. Ferguson, *Optimal Stopping and Applications*,
Chapter 2: printed p. 2.1 (PDF p. 1) gives finite-horizon backward induction;
section 2.4, pp. 2.7-2.8 (PDF pp. 7-8), distinguishes Cayley's sampling without
replacement and derives Moser's iid common-distribution recursion, equation (6)
on p. 2.8. Source: <https://www.math.ucla.edu/~tom/Stopping/sr2.pdf>. Consulted
locally at `external-resources/new-themes-52-63/week60-61/ferguson-finite-horizon-sr2.pdf`.
The three-ticket examples are original applications, not Ferguson's exercises.
The rank-only secretary objective is different.

Consulted pedagogical precedents and the limits of our adaptations:

- The organizer's *Pattern Block Exercises - Google Docs*, PDF p. 1, starts
  with five minutes of handling then pairs/trios. Our ticket handling, partner
  demonstration and material enforcement are adaptations.
- Laura Givental, Maria Nemirovskaya and Ilya Zakharevich, *Math Circle by the Bay*
  (AMS, 2018), printed pp. viii-x (PDF pp. 9-11), discusses deep mathematical
  context, independent attempts, manipulatives and varied pace/depth. Our core
  and readiness-dependent proof menu is an inference from these principles.
- Natasha Rozhkovskaya, *Math Circles for Elementary School Students: Berkeley
  2009 and Manhattan 2011* (AMS, 2014), Lesson 7, "At the lesson," items 1-2
  (`OEBPS/part0017.xhtml`), records likely missed legal chords and engagement
  with K'nex polygons. Lesson 8, "At the lesson," item 2 (`part0018.xhtml`),
  records copying/coloring delays. Our partner-enforced deadline and supplied
  movable records respond to these observations. Sources do not prescribe or
  validate this ticket activity or our staffing.

Project `REPUBLISHING.md` was read. This portable package excludes workflow
prompts, borrowed style exemplars, third-party book content, reference PDFs and
generated renders. Citations record precedents, not validation or publication
clearance for other project bundles.

Package note: this README records the authored stage. External QA paths and
process-status descriptions are historical; current verification is recorded in
`plans/new-themes-52-63/week-NN/release-checks.json` in the repository. Use the
package root `python3 build.py --out output` to build every delivered PDF.
