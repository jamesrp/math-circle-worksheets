Week 87 revised student packet. Unpiloted.

Build with Python 3.11 or later and pdflatex with TikZ/lmodern:
  python3 build.py --out ../rebuilt --work ../rebuild-work
  python3 check_math.py
Since October 23, 2026 the wording and drawings are in the problem files
(../problem-files/ in the ZIP; lowell-math-circle-year-2/source/week-87/ in the
repository); build.py assembles them with the problem-file tools. The builder
uses Python's standard library only, creates its LaTeX in --work,
and produces shared.pdf (3 pages), line.pdf (4), upper.pdf (2), materials.pdf (5).
Two TeX passes are required and run automatically. PDF dates/trailer IDs are
suppressed; SOURCE_DATE_EPOCH fixes other time inputs. No external assets.

Routes override the generic three-grade-band workflow filenames.
shared: grades 2–5 readiness; card ranking and one-token-per-voter counts.
line: grades 3–5 readiness; unit distances on a common line, five voter identities,
ties, repetition. This is a separate visit; begin with its complete first-page example.
upper: Problem 1 continues the card visit after shared Problem 2 (October 23,
2026); Problem 2 is return work after the line conventions are familiar. The
second page explicitly demonstrates conversion from distances to a strict ranking.
There is deliberately no independent K–1 packet; the guide has an adult-led
K–1 route. Adults may read or record.

Materials are per pair: three fixed cards, six blank cards, 36 small letter slips
(18 per blank-card page), six option tiles, five vote tokens, five favorite
markers, X/Y proposals, separate X/Y tally labels, tally mat, knockout mat, and line board. Keep fixed
ranking cards visible. Favorite markers remain on the five separate lanes;
move vote tokens to tally wells. Use four favorite markers and four vote tokens
for line Problem 4. Cut only the indicated cards/pieces, not working mats.
Print US Letter at 100%; page 1 has a 100 mm scale check. Card 45x80 mm;
option tile 28 mm; vote token diameter 18 mm; favorite diameter 13 mm;
line spacing 16 mm; separate X/Y tally labels 23x23 mm;
tally mat 170x90 mm and wells 54x54 mm; each well has five 18 mm targets
in a quincunx; separate 30x30 mm label slots fit 28 mm option tiles or
23 mm X/Y labels with clearance; 2 mm minimum boundary clearance and 4.627 mm minimum
inter-token clearance;
knockout mat 175x100 mm, whose boxes are at least 5 mm wider than the tiles they hold. Digital geometry checked, physical cutting, fit,
procedure rehearsal, timing and classroom use remain untested.

Mathematical basis: Week 87 outline and reviewed planning record
plans/seven-families-85-91/week-87-voting-and-agendas.md, referring to Duncan
Black (1948) Section II pp.26–28, James Stodder (2005) classroom Condorcet game,
and Acemoglu MIT 14.770 slides 20–23. Writer used supplied plan, not copied
worksheet pages or external image assets. check_math.py checks every printed
profile, agenda, finite line example, all 3003 five-favorite multisets and each
opponent on the board. These exhaustive finite checks do not replace the
universal middle-voter or middle-candidate arguments. No facilitator guide is
part of this stage.

Revision: all nine investigations retained. Line page 1 now demonstrates the
unchanged favorites 0,1,5,8,10 with X=2 and Y=8; choices X,X,Tie,Y,Y
give a 2-2 tied vote with one tied voter. Favorite markers and proposal
markers stay on the board while the separate vote tokens enter the tally.
The reusable tally has five positively spaced positions in every well,
including Tie. Physical cutting, placement and classroom use remain untested.
