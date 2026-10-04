#!/usr/bin/env python3
"""Build the separate adult guide. Requires reportlab and DejaVu fonts.
Run check_geometry.py first. All paths are relative to this file.
"""
from pathlib import Path
import json, math, html
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor, black, white
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import Paragraph
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from fractions import Fraction as F
HERE=Path(__file__).resolve().parent
OUT=HERE.parent/'build'/'facilitator-guide.pdf'
DATA=json.loads((HERE/'board-data.json').read_text())['boards']
AUDIT=json.loads((HERE/'geometry-audit.json').read_text())
# Discover installed fonts; no font binaries or machine-specific project paths are bundled.
import os, subprocess
from reportlab import rl_config
font_names=('DejaVuSans.ttf','DejaVuSans-Bold.ttf','DejaVuSans-Oblique.ttf')
font_roots=[Path(os.environ['DEJAVU_FONT_DIR'])] if os.environ.get('DEJAVU_FONT_DIR') else []
font_roots += [Path(p) for p in rl_config.TTFSearchPath]
try:
    found=subprocess.run(['fc-match','-f','%{file}','DejaVu Sans'],check=True,capture_output=True,text=True).stdout
    if found: font_roots.append(Path(found).parent)
except (FileNotFoundError,subprocess.CalledProcessError): pass
font_roots += [Path.home()/'.fonts',Path.home()/'Library'/'Fonts']
if os.environ.get('WINDIR'): font_roots.append(Path(os.environ['WINDIR'])/'Fonts')
FONT_DIR=next((d for d in font_roots if all((d/f).is_file() for f in font_names)),None)
if FONT_DIR is None: raise FileNotFoundError('Install DejaVu Sans regular, bold and oblique, or set DEJAVU_FONT_DIR to their folder.')
FONTDIR=FONT_DIR
for n,f in [('Body','DejaVuSans.ttf'),('Bold','DejaVuSans-Bold.ttf'),('Italic','DejaVuSans-Oblique.ttf')]:
 pdfmetrics.registerFont(TTFont(n,str(FONTDIR/f)))
pdfmetrics.registerFontFamily('Body',normal='Body',bold='Bold',italic='Italic',boldItalic='Bold')
STYLE=ParagraphStyle('body',fontName='Body',fontSize=10.4,leading=14.25,textColor=black,spaceAfter=6)
SMALL=ParagraphStyle('small',parent=STYLE,fontSize=9.2,leading=12.5)
H2=ParagraphStyle('heading',parent=STYLE,fontName='Bold',fontSize=11.3,leading=15,spaceAfter=5)
PAGES=[]
def page(title,subtitle='',board=None,mode=None,sections=None):
 PAGES.append(dict(title=title,subtitle=subtitle,board=board,mode=mode,sections=sections or []))
def S(label,text):return (label,text)
page('Shortest routes that touch a line','Facilitator guide | Week 21 | Draft and unpiloted | Prepared 3 October 2026',sections=[
 S('Purpose and scope','Help children find a shortest two-leg route and discover why a folded or reflected picture can prove it is shortest. This is the adult companion to the final seven-page packets W21-K-v2, W21-23-v2 and W21-45-v2. Week 21 is an unscheduled library label, not a scheduled meeting. The guide is a separate new production, not a classroom-tested part of the student-page workflow.'),
 S('The mathematical payoff','For two dots strictly on the same side of a straight boundary, reflect the finish dot. A straight line to its reflected image identifies the best contact point, provided that contact is permitted. Folding preserves the finish leg; straightening gives a lower bound for every possible rival. The argument does not depend on numerical measurements.'),
 S('Prerequisites and entry points','K-1: an adult reads aloud; children can point to dot centers, hold a string at a bend, distinguish two straight legs from a curve, and compare pinched lengths. No reading, counting or arithmetic is required. Grades 2-3: add straightedge use, matching reflected points, and explaining equal lengths. Grades 4-5: add reasoning about every possible contact and the difference between finding a candidate and proving it best. Coordinates, square roots, ratios, calculus and measured angles are adult checks only.'),
 S('Preparation for ten children and three adults','Keep three stable adult-led tables, roughly 3 / 4 / 3 children; choose pages by readiness rather than age. At each table place two 60 cm non-stretch strings, two rulers or straightedges, four US Letter tracing-paper sheets, ten blank US Letter sheets, pencils, erasers and removable tape. Total: six strings, six straightedges, twelve tracing sheets and thirty blank sheets. No scissors, mirrors, pegs, protractors or lasers are needed.'),
 S('Printing and a five-minute adult rehearsal','Print student pages single-sided on US Letter at 100% actual size; no fit-to-page scaling. One set per child is 70 pages, but print a small starting selection and keep the rest ready. Each board is 16.8 × 18.2 cm; the horizontal marked segment is 15.6 cm and the vertical one 17 cm. Rehearse pinching a string length and reflecting a dot on a spare sheet. Each adult should try the unequal-height board and read the proof on page 3 before the session.'),
 S('Physical model','The line has zero thickness; a ruler or tape only marks its location. The route touches at one point between the end marks and has no travel along the boundary. Use dot centers, not the edges of circles or pegs. Keep string taut without stretching it. A drawing or string that appears best is evidence for a conjecture, not proof against all other contacts. Coordinates in the key are centimetres from the lower-left corner of the source working region, not the paper edge. They are adult checks; children use folding and drawings.')])
page('A flexible hour and page finder','Use the menu selectively; finishing a packet is not the goal',sections=[
 S('0 to 8 minutes together','Allow 2-3 minutes to handle string and straightedges. Then use a spare board: “Go from this dot to that dot, touching this line once. Make both parts straight. Can we use less string?” Show one legal bend and one illegal path running along the line. Pinch the string at the finish, lift it, and compare used lengths without moving the pinch. Invite a different contact. Do not demonstrate reflection yet.'),
 S('8 to 48 minutes at tables','K-1 entry: Problems 1 and 2, then 3 if children are curious about equal lengths; Problem 4 is the main construction opportunity. Grades 2-3 entry: Problems 1-3; pause for a folding demonstration only when a comparison raises the need. Grades 4-5 entry: Problems 1-3, then choose shared contacts (4), inverse construction (5), restrictions (6), or uniqueness (7). Swap holding, marking and comparing roles. Take a two-minute stand-and-stretch break when attention flags; it can replace a page.'),
 S('48 to 60 minutes','Invite each table to share one route and one reason it works. A child may show a fold, a matching length, a shorter guess, or a proof. Ask “What did the fold keep the same?” or “What would rule out a route we never tried?” Leave time to gather materials. These timings are a suggested menu, not observed classroom pacing.'),
 S('Find the exact solution','Every final numbered problem is covered below. K-1 numbering follows the revised final packet; the earlier review used a different order. The page numbers after each topic refer to this guide.'),
 S('K-1 packet','P1 equal-length routes: page 4. P2 beat two guesses: page 5. P3 reflected partners: page 6. P4 unequal heights: page 7. P5 compare minima: page 8. P6 vertical boundary: page 9. P7 prescribe a contact: page 10.'),
 S('Grades 2-3 packet','P1 compare minima: page 8. P2 reflected partners: page 6. P3 unequal heights and proof: page 7. P4 vertical boundary: page 9. P5 prescribe a contact: page 10. P6 equal minima: page 11. P7 restricted contacts: page 13.'),
 S('Grades 4-5 packet','P1 compare minima: page 8. P2 reflected partners: page 6. P3 unequal heights and proof: page 7. P4 shared best contact: page 12. P5 all possible starts: page 10. P6 restricted contacts: page 13. P7 uniqueness: page 14.'),
 S('When to stop or change direction','A useful stopping point is a child making legal routes independently, spotting a preserved length, constructing a better route, or explaining why all rivals lose. If string handling is the obstacle, the adult holds while the child chooses. If the construction becomes routine, move to an inverse or legality question instead of assigning more similar boards.')])
page('The proof to keep in your pocket','An accessible universal argument; reveal only as needed',board='unequal',mode='proof',sections=[
 S('Make the reflected picture','Call the finish B and its reflection B′. Fold exactly on the boundary and copy B to the other side, or trace the line and B, flip the tracing paper across the line, and align the line and its end marks. Every boundary point M stays in place under the fold. The segment MB lands on MB′, so those lengths are equal.'),
 S('Straighten every competitor','Choose any legal M, including one nobody has tried. Its route length is AM + MB = AM + MB′. A bent route from A to B′ cannot be shorter than the straight segment AB′. Draw AB′ and call its crossing with the boundary M*. At M*, the reflected route is straight, so the original route attains that lower bound. Check that M* is between the permitted end marks.'),
 S('Why this covers all and only the best','A and B′ are on opposite sides, so their straight segment crosses the boundary once. Every rival was included because M was arbitrary. Equality in the Euclidean triangle inequality occurs only when M lies on segment AB′; therefore the best contact is unique. Say to a younger child: “After the fold, every try still uses the same string. This one is straight. Any other try has a bend.”'),
 S('Held hints in three stages','First ask for two or three genuine trials. Then ask what could be copied or folded without changing a length. Only if needed, reflect B and ask for the shortest way to its copy. Wait after each hint. A child who discovers straightening should explain it before an adult names the triangle inequality.'),
 S('Adult-only coordinates','For a horizontal line y = h, let A = (a, h + u) and B = (b, h + v), with u,v positive. Then B′ = (b, h - v), M* has x = (va + ub)/(u + v), and the squared minimum is (b - a)² + (u + v)². These follow by intersecting AB′ with y = h; they are checks, not the student method. Exchange x and y for a vertical line.')])
page('Two different routes with equal length','K-1 Problem 1 | Equal-height board',board='equal',mode='equal',sections=[
 S('Task and entry','Make several A-to-B routes and find two different ones using the same length of string. Prerequisite: compare held string lengths; an adult may do the holding. This task asks for equality, not yet a shortest route.'),
 S('Exact answer','The line is y = 8.7; A = (2.8,13.4), B = (14,13.4). Choose contacts M₁ = (6.4,8.7) and M₂ = (10.4,8.7). The two routes have the same total length: √35.05 + √79.85 cm. More generally, contacts at x = 8.4 - d and 8.4 + d give equal totals whenever 0 &lt; d &lt; 7.8.'),
 S('Why it works without arithmetic','Fold the whole picture on the vertical line halfway between A and B. It swaps A with B and M₁ with M₂. The first leg of one route matches the second leg of the other, and vice versa. Adding the same two pieces in the opposite order gives the same total. Two separate string pieces can make this swapping visible.'),
 S('Held hints','1. Try one contact left of the middle and one right of it. 2. Could the two leg lengths trade places? 3. Help fold the endpoints onto each other, then choose contacts that match under that fold. Keep the second fold distinct from the later fold on the route boundary.'),
 S('Watch for and extend','Equal total length does not mean that each route has equal legs. Close-looking strings may differ because a pinch moved. Accept any verified distinct equal pair. If shortest is asked next, the unique best contact is (8.4,8.7), with minimum √213.8 cm; reflection in the route boundary proves this. Stop after the swapping explanation if that is enough.')])
page('A route shorter than both guesses','K-1 Problem 2 | This is Problem 2 in the revised final packet',board='guesses',mode='guesses',sections=[
 S('Task and entry','Beat the two printed routes, then find the shortest route you can. Prerequisite: make and compare legal two-leg routes. Begin with the printed paths rather than announcing a construction.'),
 S('Exact answer','A = (2.2,12.5), B = (14.4,15.4), and B′ = (14.4,2). Draw A to B′; it meets y = 8.7 at x = 3473/525, about 6.61524. Draw A-M*-B. Its minimum length is √259.09 cm, about 16.09627 cm. Both legs and the reflection lie on the working sheet.'),
 S('Check against the drawn paths','The solid guess touches x = 3.5 and uses about 16.81075 cm. The dashed guess touches x = 11.5 and uses about 17.34708 cm. Both are strictly longer than the reflected construction. Many guesses can beat both; only the straightened crossing is globally shortest.'),
 S('Child-accessible reason','After trying several contacts, copy B across the line with a fold or tracing paper. A route through any contact uses the same amount to reach that copy. The contact where the copied route goes straight loses its bend and is shortest. A K-1 child can show the fold and straight string without saying “minimum” or using the decimal values.'),
 S('Held hints and stopping','1. Move the contact away from each printed guess and compare. 2. Can we change the picture without changing the length of its last piece? 3. Offer a reflected B and ask where a straight A-to-copy string meets the line. Stop with a genuinely shorter route if the child is still exploring; the adult key identifies the exact optimum without making a proof a performance requirement.')])
page('Reflected finish dots always tie','K-1 P3 | Grades 2-3 P2 | Grades 4-5 P2',board='mirror',mode='mirror',sections=[
 S('Tasks and prerequisites','At the same contact, compare A-to-B with A-to-C. K-1 asks whether one can use less string than the other. Grades 2-3 asks whether moving that shared point can make one longer; grades 4-5 asks for every possible contact. Entry: compare two lengths and understand that both routes use the same chosen contact.'),
 S('Exact answer','They are equal for every shared contact M on the drawn boundary. B = (13.5,13.1) and C = (13.5,4.3) are reflected partners across y = 8.7, each 4.4 cm from it. Hence MB = MC and AM + MB = AM + MC. Moving M usually changes both totals, but changes them together; neither beats the other while the contact is shared.'),
 S('A proof children can show','Fold B onto C. M remains fixed because it is on the crease, so the B leg lands exactly on the C leg. Both routes already have the same A-to-M piece. Let a child choose a second M and see that the fold still matches, then ask why any M on that crease would work. The explanation, not a list of measured examples, handles every contact.'),
 S('Held hints','1. Cover the common A-to-M leg; what remains to compare? 2. Could B land on C when the paper folds? 3. Keep M fixed during the fold and trace its two finish legs. For the oldest group, deliberately place M somewhere new after hearing the claim.'),
 S('Important distinction and extension','A and C are on opposite sides. Their route is a legal auxiliary comparison, not an application of the same-side reflection theorem to A and C. The straight segment AC crosses at x = 8751/1010, about 8.66436. At that contact both routes have common minimum √225.22 cm, about 15.00733. Different contacts for the two routes need not give equal lengths; the shared-contact condition is essential.')])
page('Unequal heights and a universal proof','K-1 P4 | Grades 2-3 P3 | Grades 4-5 P3',board='unequal',mode='normal',sections=[
 S('Tasks and prerequisites','All groups find the shortest A-to-B route. Grades 2-3 must explain why no other contact is shorter; grades 4-5 explicitly includes undrawn routes. Entry: reflected lengths from the previous mirror board. A fold-based argument is enough; symbolic geometry is not required.'),
 S('Exact construction and answer','A = (2.3,12.1), B = (14.3,15.5), line y = 8.7. Reflect B to B′ = (14.3,1.9). Segment AB′ meets the line at M* = (6.3,8.7). Draw A-M*-B. The first leg has horizontal and vertical changes 4 and 3.4; the second has changes 8 and 6.8. Their lengths are √27.56 and 2√27.56, so the minimum is √248.04 cm, about 15.74929.'),
 S('Why no rival is shorter','For any allowed M, fold MB to MB′ without changing length. The transformed A-M-B′ route cannot beat straight AB′. At M* it is straight, and M* is inside the marked segment. Thus the lower bound is actually reached. Ask an older child to choose an untested M and explain why the same reasoning applies.'),
 S('Held hints','1. Is the middle of the two feet always best when one dot is higher? 2. Which point could replace B while keeping every finish leg the same length? 3. Draw A to that point and check the crossing. Have the child complete the argument: preserved length, universal lower bound, and one legal route attaining it.'),
 S('Common mistake and extension','The midpoint of the perpendicular feet is x = 8.3, not the optimum x = 6.3. The higher finish dot pulls the contact toward the lower start dot. Do not replace the proof by testing the midpoint and two neighbors. If ready, children can compare the similar triangles: the heights are in ratio 1:2, and so are the horizontal runs. This ratio is optional adult-supported reasoning.')])
page('Which of two shortest routes is shorter','K-1 P5 | Grades 2-3 P1 | Grades 4-5 P1',board='compare',mode='normal',sections=[
 S('Tasks and entry','Find shortest routes from A to B and from A to C, then compare them. Entry: making and comparing routes; this is the older groups’ opening exploration, so let them guess before offering reflections. The two routes may touch different points.'),
 S('Exact answers','With line y = 8.7, A = (2.8,12.8), B = (14,11.7), C = (10.8,16.4). Reflect B to (14,5.7) and C to (10.8,1). The AB contact is x = 658/71, about 9.26761; the AC contact is x = 1646/295, about 5.57966. Both contacts lie inside the permitted segment.'),
 S('Comparison and proof','The AB minimum is √175.85 cm, about 13.26084; the AC minimum is √203.24 cm, about 14.25623. Therefore AB needs less string. Reflecting each finish makes its shortest allowed route a straight segment from A. Those two straight segments can be compared by transferred string lengths. Each is a true minimum by the argument on page 3. For an exact adult check, 175.85 &lt; 203.24, so their positive square roots have the same order.'),
 S('Held hints','1. Let each destination have its own contact; do not force a shared bend. 2. Compare the used portions of string from your best trials. 3. If ready to certify best, copy each destination across the line and find the two straight crossings. A nonreader may point to the shorter reflected segment rather than write an answer.'),
 S('Watch for and extend','Comparing the direct distances AB and AC above the line solves a different problem because the route must touch the boundary. A destination that looks closer horizontally can still require a longer reflected route. Ask whether having the shorter minimum means every AB route is shorter than every AC route: no, a poor AB contact can be longer than an optimal AC route. This distinguishes a minimum from an arbitrary attempt.')])
page('The same idea on a vertical boundary','K-1 P6 | Grades 2-3 P4',board='vertical',mode='normal',sections=[
 S('Task and entry','Find a shortest route for each of AB, AC and BC. Entry: recognize a reflected point and apply the construction to a new orientation. Children may rotate the entire sheet; doing so does not change distances or legality.'),
 S('Exact answers','The line is x = 8.4. A = (3.1,2.5), B = (5.6,9.2), C = (2.2,15.9). Reflect B to (11.2,9.2) and C to (14.6,15.9). Contacts are given by their y coordinate: AB at 2788/405 ≈ 6.88395; AC at 9977/1150 ≈ 8.67565; BC at 2539/225 ≈ 11.28444. All are strictly between 0.6 and 17.6.'),
 S('Lengths and justification','The respective minima are √110.5 ≈ 10.51190 cm, √311.81 ≈ 17.65814 cm, and √125.89 ≈ 11.22007 cm. For each pair, connect the start to the reflected finish, mark its crossing, and turn that finish leg back. The fold keeps the finish leg equal and the straightened segment is shortest, exactly as for the horizontal boards. The word “vertical” adds no new theorem.'),
 S('Held hints','1. Turn the paper until the line looks familiar. 2. Fold the finish dot across this line, not across a horizontal crease. 3. Keep one construction at a time on tracing paper, then overlay the three contact marks. Let children choose whether to use one or several sheets.'),
 S('Watch for and extend','It is easy to reflect C up/down instead of left/right, or to confuse the contact order when three paths overlap. The three separate views avoid overlapping paths. On one board, the contact order from bottom to top is AB, AC, BC. A good stopping point is a child explaining why turning the paper cannot change the answer. For more work, construct the same AB route by reflecting A instead of B and show that the contact agrees.')])
page('Choose the start to prescribe the contact','K-1 P7 | Grades 2-3 P5 | Grades 4-5 P5',board='inverse',mode='inverse',sections=[
 S('Tasks and prerequisites','K-1 makes one start above the line and then another; grades 2-3 draws two distinct starts and their routes; grades 4-5 describes all possible starts and explains why. Entry: the forward reflection construction. For all-starts reasoning, a child should distinguish a line, ray and segment using a straightedge or pointing.'),
 S('Exact examples and complete answer','P = (7.1,8.7), B = (13.4,14.3), and B′ = (13.4,3.1). Draw the ray beginning at P and going away from B′ into the upper half-plane; exclude P itself. Every point on that ray works. Two drawable examples are S₁ = (3.95,11.5) and S₂ = (0.8,14.3). Draw S₁-P-B and S₂-P-B. In adult notation the full ray is S = (7.1 - 6.3t, 8.7 + 5.6t), t &gt; 0.'),
 S('Why every point works and no others do','For any start S on the ray, S-P-B′ is straight and P lies between S and B′. Folding PB′ back to PB gives the universal lower bound, so P is the best contact. Conversely, if a start above the line has best contact P, equality in the straightened triangle inequality forces S, P, B′ to lie on one straight segment in that order. This puts S on exactly that ray. P is excluded because the task requires the start above the line.'),
 S('Held hints','1. Keep P fixed and move only the new start. 2. Where is the copy of B? 3. Place a straightedge through P and that copy; which side of P has possible starts? Let the youngest place dots before discussing all of them.'),
 S('Fidelity and extension','The mathematical ray continues forever; only a portion can be drawn on the supplied sheet. “All the places” refers to the ideal ray, or its visible portion if discussing the sheet. A start on the wrong side of P along the same infinite line does not satisfy the above-line requirement. Challenge a child to put two starts with different shortest lengths but the same contact; S₁ and S₂ already do so.')])
page('Different contacts with equal minimum lengths','Grades 2-3 Problem 6',board='lengthtie',mode='normal',sections=[
 S('Task and entry','Find the shortest A-to-B and A-to-C routes and decide whether one needs less string or both need the same amount. Entry: construct a reflected shortest route and compare straight segments. This board deliberately defeats an assumption that distinct destinations must give distinct minimum lengths.'),
 S('Exact answer','They need the same amount: √164 = 2√41 cm, about 12.80625 cm. A = (3,12.7), B = (13,12.7), C = (11,14.7), with boundary y = 8.7. B′ = (13,4.7), C′ = (11,2.7). The AB contact is (8,8.7); the AC contact is (6.2,8.7). The contacts are different even though the minimum lengths agree.'),
 S('A geometric explanation','The straight reflected segments AB′ and AC′ are hypotenuses of right triangles with horizontal and vertical legs 10 and 8, and 8 and 10. One right triangle can be rotated or flipped to match the other, so its long side has the same length. This explains exact equality without relying on near-equal measured strings or requiring children to know the Pythagorean theorem. Each straightened segment certifies its own route minimum.'),
 S('Held hints','1. Preserve the pinches carefully; a very small observed difference may be handling error. 2. Look at the straight routes to the reflected destinations. 3. Trace the horizontal-and-vertical right triangle for each and try matching them. Show the leg swap only if children need it.'),
 S('Watch for and extend','Do not force the two routes to share a contact; that would be a different comparison from the mirror board. “The string looked the same” is a useful observation, but congruent triangles settle exact equality. Extension: compare this result to grades 4-5 P4, where the contacts agree but the minimum lengths differ. Neither type of equality implies the other.')])
page('Two different journeys share the best contact','Grades 4-5 Problem 4',board='matching',mode='normal',sections=[
 S('Task and entry','Find the shortest A-to-B route and shortest C-to-D route. Decide whether they can touch at the same point. Entry: a reflection construction for each pair and an explanation of why it is globally shortest.'),
 S('Exact answer','Yes. Both best routes touch M* = (6.2,8.7). The first pair is A = (2.2,12.3), B = (14.2,15.9); the second is C = (3.2,12.7), D = (12.2,16.7). Reflect B to (14.2,1.5) and D to (12.2,0.7). Both straight reflected segments cross the boundary at x = 6.2.'),
 S('Why the crossings agree','For AB the start and finish heights are 3.6 and 7.2, a 1:2 ratio, so the crossing is one third of the 12 cm horizontal span from A: 2.2 + 4 = 6.2. For CD the heights are 4 and 8, again 1:2, and one third of the 9 cm span from C gives 3.2 + 3 = 6.2. Similar triangles justify this optional ratio check. Children can instead demonstrate both straightened crossings on one tracing overlay.'),
 S('Lengths are a separate question','The AB minimum is √260.64 cm, about 16.14435 cm; the CD minimum is 15 cm. The same contact does not mean the same route length. Optimality for each follows separately because its reflected route is straight and the shared contact is legal.'),
 S('Held hints and extension','1. Allow each journey its own reflected finish. 2. Draw the two straight connections and compare their boundary crossings. 3. If two marks look nearly equal, trace both constructions or compare the one-to-two height ratios. To extend, fix the contact and one destination and ask where starts can go; this leads naturally to the inverse ray on page 10.')])
page('Restricting the permitted contact region','Grades 2-3 P7 | Grades 4-5 P6',board='restricted',mode='restricted',sections=[
 S('Tasks and entry','First find the original shortest route. Grades 2-3 asks when it remains allowed under new restrictions; grades 4-5 asks when the same route remains a shortest allowed route. Entry: distinguish constructing a best route on the whole marked segment from testing its legality on a smaller segment.'),
 S('Original optimum and exact decisions','A = (2.5,12.7), B = (14.5,16.7), B′ = (14.5,0.7). The reflected crossing is M* = (6.5,8.7), and the minimum is √288 = 12√2 cm, about 16.97056 cm. C-D permits x from 4.5 to 8.2: yes. E-F permits x from 10.2 to 14.9: no. C-F permits x from 4.5 to 14.9: yes. All membership decisions are strict, so including or excluding the named endpoints does not affect these answers.'),
 S('Why the two yes answers remain optimal','Every route in the smaller allowed set was already a competitor in the original problem, so none can be shorter than the original minimum. In C-D and C-F, the old route is still permitted and still attains that lower bound. In E-F it is not a legal candidate at all. The unchanged lower bound need not be attainable there.'),
 S('Held hints','1. Put a fingertip on the old contact; do not move it yet. 2. Mark each allowed interval on a separate tracing copy. 3. Ask whether the fingertip is inside it, then whether removing competitors could make any remaining route beat the old best.'),
 S('Do not add an unsupported claim','Neither final problem asks for the new E-F optimizer. “The reflected crossing is outside, so use the nearest endpoint” needs an additional argument and must not be asserted merely from the reflection picture. This guide stops at the exact yes/no decisions the packets ask. A later extension could investigate that new problem separately after clarifying whether interval endpoints are allowed.')])
page('Can two best contacts exist','Grades 4-5 Problem 7',board='unique',mode='unique',sections=[
 S('Task and entry','Decide whether two different contacts can both give the shortest A-to-B route, and justify the answer for every possible contact. Entry: the universal reflected lower bound and the fact that a genuinely bent Euclidean path is longer than the straight connection.'),
 S('Exact answer','No. The unique contact is M* = (1157/110,8.7), approximately (10.51818,8.7). A = (3.2,15.6), B = (13.7,11.7), and B′ = (13.7,5.7). The minimum is √208.26 cm, approximately 14.43122 cm. This crossing is inside the marked segment.'),
 S('Proof covering all contacts','For any M on the permitted boundary, AM + MB = AM + MB′ ≥ AB′. To tie the minimum, equality must hold. Equality means M is on the straight segment AB′, between its endpoints. That segment joins points on opposite sides of the boundary and has exactly one crossing. Therefore any tied contact would have to be M* itself, contradicting “different.” Any other contact produces a bend and is strictly longer.'),
 S('Held hints','1. Suppose a second contact ties. What must its reflected route look like? 2. Can a bent route have the same length as its straight connection? 3. How many times can this straight segment cross this straight boundary? Ask the child to state which part rules out every other M.'),
 S('Watch for and extend','Two close contacts can look equal with thick pencil dots, a ruler or string. That is a measurement limit, not a counterexample to uniqueness in the ideal model. Equal-length nonoptimal routes do exist, as K-1 P1 shows. The proof is about two contacts both attaining the minimum, not about all route lengths being different. For a final share, contrast those two statements with the equal-height board.')])
page('Extensions and facilitation decisions','Optional adult-led investigations after the printed work',sections=[
 S('Reflect the other endpoint','Question: Reflect A instead of B. Do you get a different best contact? Answer: no. The reflection of segment AB′ is A′B; the boundary is fixed by reflection, so both segments meet it at the same point. This is an exact geometric argument and works on the vertical board too. Prerequisite: understand how a whole segment moves under a fold.'),
 S('Move both dots farther from the line','On an equal-height board, move both dots the same perpendicular distance away while keeping their horizontal positions. The midpoint contact stays fixed by left-right symmetry, but the minimum gets longer. The reflected vertical separation increases while the horizontal separation stays fixed. Use matched right triangles or stretched string to explain why. Do not claim that moving just one dot keeps the contact fixed.'),
 S('Make equal minima deliberately','Keep A fixed, reflect possible destinations, and choose two reflected destinations the same distance from A on the opposite side of the boundary. Their best routes tie if their crossings lie in the permitted segment. Children can hold one string length from A to make two such reflected dots; a compass is unnecessary. Prerequisites: the inverse idea and careful legal-crossing checks. This is a new extension, not an extra numbered student problem.'),
 S('A rigorous replacement for repeated measuring','When a child says “I checked lots of points,” ask “What stays true for one we have not checked?” Invite them to describe the common folded length and the straight lower bound. Do not reject their experiments; experiments suggest the answer and identify the right picture. The proof explains why another unseen trial cannot win.'),
 S('Troubleshooting','If folds drift, trace the whole boundary and both end marks before flipping. If labels are confusing, copy one pair at a time. If the string slips, an adult tapes its start at the dot center while the child controls the contact and pinch. If the route crosses or follows the boundary in an unintended way, return to the two straight-leg rule. Rotating a sheet is allowed; changing the geometric rule is a new problem.'),
 S('Record after actual use','Record which problems children actually tried, what they did before hints, which hint changed their approach, difficulties with pinching or folding, and any conjecture they wanted to pursue. Separate direct observations from guesses about why an activity worked. The 60-minute plan and readiness choices here are proposals; update them after a real session without treating completion speed as mathematical ability.'),
 S('Limits of this guide','The theorem here concerns one contact with one straight boundary and Euclidean length. It does not establish a physical law of light, multiple-bounce behavior, curved-boundary optimization, obstacle avoidance, or routes traveling along a boundary. This week is distinct from periodic billiard investigations. Finite-contact restrictions require a legality check before declaring a reflected route optimal.')])
page('Independent checks and source record','Separate adult-guide production | Verified against the final packets',sections=[
 S('What was checked','All 21 final problem numbers and board assignments were read from the final PDFs and matched to the final source. Drawing coordinates were independently transcribed into rational numbers, then compared to the final source without executing its builder. The check recomputed every assigned reflected optimum, exact squared minimum, permitted crossing, and required reflected point. K-1 P2 is the guesses board and K-1 P3 the reflected-partner board. The student PDFs were not changed.'),
 S('Mathematical checks and their limits','The source package includes check_geometry.py, board-data.json and geometry-audit.json. Checks include exact collinearity and preserved finish distances; both equal-minimum and shared-contact cases; strict restriction membership; two valid inverse starts; equal nonoptimal K-1 routes; and both printed guesses. A 2,001-contact numerical sweep per assigned pair is only a sanity check. The proofs in the guide, not finite sampling, establish optimality over infinitely many contacts.'),
 S('Geometry foundation','Anton Petrunin, Euclidean Plane and Its Relatives: A Minimalist Introduction, arXiv:1302.1630v25, 7 July 2025. Body verified 3 October 2026: §1C, printed p. 10, metric triangle inequality; §5D, printed pp. 39-40, Proposition 5.8 and Corollary 5.10, reflection and distance preservation. <link href="https://arxiv.org/pdf/1302.1630">https://arxiv.org/pdf/1302.1630</link>. The route reduction, exact instances and child-facing explanations are independently derived here from elementary Euclidean facts; the book is an adult reference, not a prerequisite or a claim that it supplies these worksheets.'),
 S('Math-circle teaching source','Natasha Rozhkovskaya, Math Circles for Elementary School Students, AMS / MSRI Mathematical Circles Library. Consulted the repository EPUB on 3 October 2026: “Introduction: Berkeley 2009” and Lesson 1 “Drawing links and knots,” especially “At the lesson.” The introduction describes active adult help. Lesson 1 reports fewer completed drawings than planned and difficulty with a later representation. These are that circle’s observations. Using a short launch, flexible stopping points and delayed hints here is our design inference, not evidence that this reflection session has been piloted.'),
 S('Local fidelity sources','The repository AGENTS.md and README.md supply the concrete-first, prerequisite-based approach and ten-child / three-adult planning context. Week 21 PROMPT.md supplies the theme, material constraints and theorem scope. The independent student review identifies ambiguous earlier wording and a K-1 sequence issue; the final PDFs and final source, rather than draft numbering, are authoritative for this guide. Shared solution pages deliberately cover repeated configurations while naming every final problem.'),
 S('Rebuild and review','Run python3 check_geometry.py, then python3 build_guide.py from the portable facilitator-src directory with ReportLab installed and DejaVu fonts available. The builder writes only the separate facilitator guide; it does not regenerate student packets. Render the PDF with pdftoppm and inspect every page after edits. The readable guide-content.md export and Python source are editable. This guide remains draft and unpiloted pending organizer review and classroom use.')])

# Keep the concluding teaching and verification material on readable separate pages.
old_extensions=PAGES[14]
old_sources=PAGES[15]
PAGES[14]=dict(old_extensions, sections=old_extensions['sections'][:5])
PAGES[15]=dict(title='Use records and verification', subtitle='Keep classroom evidence separate from a mathematical audit', board=None, mode=None, sections=old_extensions['sections'][5:]+old_sources['sections'][:2])
PAGES.append(dict(old_sources, title='Sources and rebuilding', sections=old_sources['sections'][2:]))

def para(c,text,x,y,w,style=STYLE):
 p=Paragraph(text,style);_,h=p.wrap(w,1000);p.drawOn(c,x,y-h);return y-h-style.spaceAfter

def draw_board(c,name,mode,x,y,w,h):
 if name=='vertical' and mode=='normal':
  for i,pair in enumerate(['AB','AC','BC']):
   draw_board(c,name,'vertical_'+pair,x+i*w/3,y,w/3,h-7)
   c.setFont('Bold',9);c.setFillColor(black);c.drawCentredString(x+(i+.5)*w/3,y+h-4,pair[0]+' to '+pair[1])
  c.setFont('Italic',8.5);c.setFillColor(HexColor('#444444'));c.drawCentredString(x+w/2,y-7,'Three separate solution views. Each M* is its pair’s contact; dashed legs are reflected.')
  return
 b=DATA[name];pts={k:tuple(map(float,v)) for k,v in b['points'].items()};axis=0 if b.get('axis')=='v' else 1;line=8.4 if axis==0 else 8.7
 # Same aspect ratio as the student board. Full geometry, smaller adult key only.
 sc=min((w-40)/16.8,(h-18)/18.2);ox=x+(w-16.8*sc)/2;oy=y+4
 def xy(p):return ox+p[0]*sc,oy+p[1]*sc
 def path(ps,color='#222222',width=1.2,dash=None):
  c.setStrokeColor(HexColor(color));c.setLineWidth(width);c.setDash(dash or [])
  p=c.beginPath();p.moveTo(*xy(ps[0]));
  for q in ps[1:]:p.lineTo(*xy(q))
  c.drawPath(p);c.setDash([])
 def dot(label,p,dx=5,dy=5,filled=True):
  xp,yp=xy(p);c.setStrokeColor(black);c.setFillColor(black if filled else white);c.circle(xp,yp,2.1,fill=1,stroke=1)
  c.setFillColor(white);c.rect(xp+dx-1,yp+dy-2,pdfmetrics.stringWidth(label,'Body',9)+2,11,fill=1,stroke=0)
  c.setFillColor(black);c.setFont('Body',9);c.drawString(xp+dx,yp+dy,label)
 ends=[(.6,line),(16.2,line)] if axis==1 else [(line,.6),(line,17.6)]
 path(ends,width=.8)
 for p in ends:
  q=list(p);r=list(p);q[axis]-=.14;r[axis]+=.14;path([q,r],width=.8)
 pairs=list(AUDIT[name])
 if mode and mode.startswith('vertical_'):
  pairs=[mode.split('_')[1]];pts={k:v for k,v in pts.items() if k in pairs[0]}
 contacts=[];refpoints={}
 if mode=='equal':
  for i,t in enumerate([6.4,10.4]):
   m=(t,line);path([pts['A'],m,pts['B']],color='#222222' if i==0 else '#777777',dash=None if i==0 else [4,2]);dot('M'+str(i+1),m,dy=-13)
 elif mode=='inverse':
  r=(13.4,3.1);p=(7.1,line);s1=(3.95,11.5);s2=(.8,14.3)
  path([s2,r],color='#777777',dash=[4,2]);path([s2,p,pts['B']]);path([s1,p],width=1.8);dot('S1',s1,dx=-20);dot('S2',s2,dx=-20);dot('B′',r,filled=False)
 elif mode=='mirror':
  m=(7,line);path([pts['A'],m,pts['B']]);path([m,pts['C']],color='#666666',dash=[4,2]);dot('M',m,dy=-13)
 else:
  for i,pair in enumerate(pairs):
   a,bp=(pts[k] for k in pair);rec=AUDIT[name][pair];m=tuple(map(lambda v:float(F(v)),rec['contact']));r=tuple(map(lambda v:float(F(v)),rec['reflected_finish']));refpoints[pair[1]+'′']=r
   col=['#111111','#777777','#444444'][i%3]
   path([a,m,bp],color=col,width=1.3)
   path([m,r],color=col,width=.9,dash=[4,2]);contacts.append((pair,m))
  if mode=='guesses':
   for t in [3.5,11.5]:path([pts['A'],(t,line),pts['B']],color='#aaaaaa',width=.7,dash=[2,2])
  if mode in ('proof','unique'):
   q=(12.7,line) if mode=='proof' else (7.4,line)
   path([pts['A'],q,refpoints['B′']],color='#aaaaaa',width=1,dash=[1.5,2]);dot('M',q,dy=-14)
  for label,p in refpoints.items():dot(label,p,dy=4 if p[1]<2 else -12,filled=False)
  seen=[]
  for label,p in contacts:
   if any(math.dist(p,q)<.001 for q in seen):continue
   seen.append(p)
   text='M*' if len(contacts)==1 or name=='matching' else label
   if axis==0:dot(text,p,dx=6,dy=-12)
   else:dot(text,p,dx=-9,dy=-14)
 for label,p in pts.items():
  # Matching-board labels are deliberately placed on opposite sides of close points.
  dx=-16 if name=='matching' and label in ['A','C'] else 5
  dy=5
  if name=='matching' and label=='A':dy=-12
  if name=='vertical':dx=-15;dy=4
  dot(label,p,dx=dx,dy=dy)
 for label,v in b.get('marks',{}).items():
  p=(float(v),line);dot(label,p,dx=-3,dy=-14 if label!='P' else 5)
 c.setFont('Italic',8.5);c.setFillColor(HexColor('#444444'))
 if not (mode and mode.startswith('vertical_')):c.drawCentredString(x+w/2,y-7,'Adult solution diagram, reduced scale. Solid routes; dashed reflected legs or trial paths.')

c=canvas.Canvas(str(OUT),pagesize=(612,792))
c.setTitle('Week 21 shortest routes facilitator guide')
c.setAuthor('Bellingham Math Circle')
c.setSubject('Draft unpiloted adult guide for all 21 final Week 21 student problems')
layout=[]
for n,p in enumerate(PAGES,1):
 c.setFillColor(black);c.setFont('Body',8.3);c.drawString(44,763,'BELLINGHAM MATH CIRCLE  /  ADULT GUIDE  /  UNSCHEDULED LIBRARY SLOT 21')
 y=735
 title=Paragraph(p['title'],ParagraphStyle('title',fontName='Bold',fontSize=20 if n==1 else 17.5,leading=23,textColor=black))
 _,hh=title.wrap(524,1000);title.drawOn(c,44,y-hh);y-=hh+9
 y=para(c,p['subtitle'],44,y,524,SMALL)-3
 if p['board']:
  height=184 if p['board']!='vertical' else 194
  draw_board(c,p['board'],p['mode'],44,y-height,524,height);y-=height+21
 for label,txt in p['sections']:
  y=para(c,label,44,y,524,H2)
  y=para(c,txt,44,y,524)
  y-=0
 if y<49:raise RuntimeError(f'Page {n} overflow: bottom {y:.1f}')
 layout.append({'page':n,'title':p['title'],'content_bottom_pt':round(y,2)})
 c.setFont('Body',8.2);c.setFillColor(HexColor('#444444'));c.drawString(44,29,'Week 21  /  Draft and unpiloted  /  Facilitator guide');c.drawRightString(568,29,f'{n} / {len(PAGES)}')
 c.showPage()
c.save()
(HERE/'layout-check.json').write_text(json.dumps(layout,indent=2)+'\n')
(HERE/'guide-content.json').write_text(json.dumps(PAGES,indent=2,ensure_ascii=False)+'\n')
md=['# Week 21 shortest routes facilitator guide','\nDraft and unpiloted. Week 21 is an unscheduled library label.']
for n,p in enumerate(PAGES,1):
 md += [f'\n## Page {n} - {p["title"]}',p['subtitle']]
 if p['board']:md.append(f'\nSolution diagram: {p["board"]}; see build_guide.py and board-data.json.')
 for label,txt in p['sections']:md += [f'\n### {label}',html.unescape(txt)]
(HERE/'guide-content.md').write_text('\n\n'.join(md)+'\n')
print(f'Built {OUT}: {len(PAGES)} pages')
print(json.dumps(layout,indent=2))
