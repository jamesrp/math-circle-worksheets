#!/usr/bin/env python3
"""Portable editable ReportLab source. Run python3 build_guide.py."""
from pathlib import Path
from fractions import Fraction
import json, math
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import Paragraph
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from check_math import DATA, EXPECTED, RESULT, solve, splits
ROOT=Path(__file__).resolve().parent
OUT=ROOT.parent/'build'/'facilitator-guide.pdf'
# Optional open fonts; standard built-in PDF fonts provide a portable fallback.
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
fontdir=FONT_DIR
if (fontdir/'DejaVuSans.ttf').exists():
 pdfmetrics.registerFont(TTFont('Guide',str(fontdir/'DejaVuSans.ttf')))
 pdfmetrics.registerFont(TTFont('GuideBold',str(fontdir/'DejaVuSans-Bold.ttf')))
 pdfmetrics.registerFontFamily('Guide',normal='Guide',bold='GuideBold',italic='Guide',boldItalic='GuideBold')
 F='Guide';FB='GuideBold'
else:F='Helvetica';FB='Helvetica-Bold'
C=canvas.Canvas(str(OUT),pagesize=(612,792))
C.setTitle('Week 22 Meeting regions facilitator guide')
C.setAuthor('Bellingham Math Circle')
BLACK=colors.HexColor('#20252b'); BLUE=colors.HexColor('#224d6c'); RED=colors.HexColor('#9b4938'); LIGHT=colors.HexColor('#d8e5ed'); GRAY=colors.HexColor('#68737c')
W=508;LEFT=52;page=0;y=0;layout=[]
styles={
 'body':ParagraphStyle('body',fontName=F,fontSize=10.1,leading=14.2,textColor=BLACK,spaceAfter=6),
 'small':ParagraphStyle('small',fontName=F,fontSize=8.6,leading=11.7,textColor=BLACK),
 'lead':ParagraphStyle('lead',fontName=F,fontSize=11.6,leading=16.3,textColor=BLACK),
}
def p(text,style='body',x=LEFT,width=W,gap=6):
 global y
 q=Paragraph(text,styles[style]);ww,hh=q.wrap(width,700)
 if y-hh<48:raise RuntimeError(f'Page {page} overflow at {text[:70]} y={y} h={hh}')
 q.drawOn(C,x,y-hh);layout.append((page,text[:55],round(y-hh,1)));y-=hh+gap

def h(text):
 global y
 y-=6;C.setFillColor(BLACK);C.setFont(FB,12);C.drawString(LEFT,y-12,text);y-=25

def start(title,kicker):
 global page,y
 if page:C.showPage()
 page+=1;y=699
 C.setFillColor(GRAY);C.setFont(F,8.3);C.drawString(LEFT,754,'BELLINGHAM MATH CIRCLE  /  WEEK 22  /  ADULT GUIDE')
 C.setFillColor(BLACK);C.setFont(FB,19);C.drawString(LEFT,720,title)
 C.setFillColor(GRAY);C.setFont(F,8.7);C.drawString(LEFT,701,kicker)
 y=680
 C.setFillColor(GRAY);C.setFont(F,8);C.drawString(LEFT,29,'Draft and unpiloted  |  Unscheduled library week  |  Final v3 student packets')
 C.drawRightString(560,29,str(page))

def note(label,text):p(f'<b>{label}</b> {text}')
def secproblem(title,source,gate):
 h(title);p(f'<b>Student page{source}</b> <b>Gate:</b> {gate}',style='small')
def hull(points):
 pts=sorted(set(tuple(float(x) for x in p) for p in points))
 if len(pts)<3:return pts
 def cross(o,a,b):return (a[0]-o[0])*(b[1]-o[1])-(a[1]-o[1])*(b[0]-o[0])
 lo=[];hi=[]
 for q in pts:
  while len(lo)>1 and cross(lo[-2],lo[-1],q)<=0:lo.pop()
  lo.append(q)
 for q in pts[::-1]:
  while len(hi)>1 and cross(hi[-2],hi[-1],q)<=0:hi.pop()
  hi.append(q)
 return lo[:-1]+hi[:-1]

def diagram(key,split,x,top,size=148,title=None,show_meet=True,points=None,locus=False):
 """Draw exact affine copy of 12.6 cm board; top includes caption."""
 data=points or DATA[key]
 C.setFillColor(BLACK);C.setFont(FB,9)
 C.drawString(x,top,title or (split.replace('|',' | ') if split else 'No successful split'))
 by=top-18-size;scale=size/12.6
 def xy(p):return x+float(p[0])*scale,by+float(p[1])*scale
 C.setStrokeColor(colors.HexColor('#c8ced2'));C.setLineWidth(.4);C.setDash();C.rect(x,by,size,size,fill=0)
 if locus:
  a=data['A'];b=data['B'];m=(b[1]-a[1])/(b[0]-a[0]);ends=[(0,a[1]-a[0]*m),(12.6,a[1]+(12.6-a[0])*m)]
  C.setStrokeColor(colors.HexColor('#bacbd8'));C.setLineWidth(4);C.line(*xy(ends[0]),*xy(ends[1]))
 if split:
  for gi,g in enumerate(split.split('|')):
   hs=hull([data[k] for k in g]);C.setStrokeColor([BLUE,RED][gi]);C.setLineWidth(1.6);C.setDash([4,2] if gi else [])
   ps=[xy(q) for q in hs]
   if len(ps)==1:C.circle(*ps[0],3.6+gi,stroke=1,fill=0)
   elif len(ps)==2:C.line(*ps[0],*ps[1])
   else:
    path=C.beginPath();path.moveTo(*ps[0])
    for q in ps[1:]:path.lineTo(*q)
    path.close();C.setFillColor(LIGHT if gi==0 else colors.HexColor('#f1ddd5'));C.drawPath(path,stroke=1,fill=1)
  if show_meet:
   pts=solve(data).get(split,[])
   if len(pts)>1:
    C.setDash();C.setLineWidth(5);C.setStrokeColor(colors.HexColor('#cdba73'));C.line(*xy(pts[0]),*xy(pts[-1]))
    # Repaint centerline: width here is only a visible marker of a common segment.
    C.setStrokeColor(BLACK);C.setLineWidth(.5);C.line(*xy(pts[0]),*xy(pts[-1]))
   elif len(pts)==1:
    xx,yy=xy(pts[0]);C.setDash();C.setStrokeColor(BLACK);C.setLineWidth(1);C.circle(xx,yy,4.8,stroke=1,fill=0)
 # Display each ideal location once; coincident labels remain identifiable.
 groups={}
 for label,pt in data.items():groups.setdefault(tuple(pt),[]).append(label)
 for pt,labels in groups.items():
  xx,yy=xy(pt);C.setDash();C.setFillColor(BLACK);C.circle(xx,yy,1.75,stroke=0,fill=1)
  lab=', '.join(labels);C.setFont(FB,8.6)
  # Stagger all-collinear labels above; other labels clear endpoints.
  dx,dy=3,5
  if float(pt[1])>9:dy=5
  if float(pt[0])>10:dx=-pdfmetrics.stringWidth(lab,FB,8.6)-4
  C.drawString(xx+dx,yy+dy,lab)
 C.setDash();return by

def row(diagrams,size=148,gap=30):
 global y
 n=len(diagrams);total=n*size+(n-1)*gap;x=LEFT+(W-total)/2;top=y
 for i,d in enumerate(diagrams):
  if len(d)==2:key,split=d;title=None
  else:key,split,title=d
  diagram(key,split,x+i*(size+gap),top,size,title)
 y=top-18-size-14

def line_gallery(key,winlist):
 global y
 data=DATA[key]; pts={k:(v[0],6.3) for k,v in data.items()}
 # Retain line order but deliberately flatten diagonal U2 for this tiny gallery.
 if key=='U2':pts={k:(v[0],6.3) for k,v in data.items()}
 for i,s in enumerate(winlist):
  top=y;x=LEFT+(i%2)*263
  # custom wide low board preserving exact one-dimensional order
  bw=244;bh=55;by=top-22-bh;sc=(bw-26)/12.6
  def xy(q):return x+13+float(q[0])*sc,by+26
  C.setFillColor(BLACK);C.setFont(FB,10);C.drawString(x,top,s.replace('|',' | '))
  for gi,g in enumerate(s.split('|')):
   q=sorted([pts[k] for k in g]);C.setStrokeColor([BLUE,RED][gi]);C.setDash([4,2] if gi else []);C.setLineWidth(2)
   if len(q)==1:C.circle(*xy(q[0]),4,stroke=1,fill=0)
   else:C.line(*xy(q[0]),*xy(q[-1]))
  C.setDash();C.setFillColor(BLACK)
  for k,q in pts.items():
   xx,yy=xy(q);C.circle(xx,yy,1.6,fill=1,stroke=0);C.setFont(F,9);C.drawCentredString(xx,yy+10,k)
  if i%2 or i==len(winlist)-1:y-=100

def truth_table(keys,names):
 global y
 p('<b>All seven unordered splits</b> (yes/no columns are exhaustive).','small')
 widths=[180]+[(W-180)/len(keys)]*len(keys)
 vals=[['Split']+names]
 for s in ['A|BCD','AB|CD','AC|BD','AD|BC','ABC|D','ABD|C','ACD|B']:
  vals.append([s.replace('|',' | ')]+['yes' if s in EXPECTED[k] else 'no' for k in keys])
 for ri,r in enumerate(vals):
  rh=20;x=LEFT
  for j,(v,w) in enumerate(zip(r,widths)):
   C.setFillColor(colors.HexColor('#e7ebee') if ri==0 else (colors.HexColor('#f6f7f8') if ri%2==0 else colors.white));C.setStrokeColor(colors.HexColor('#d9d9d9'));C.setLineWidth(.4);C.rect(x,y-rh,w,rh,fill=1,stroke=1)
   C.setFont(FB if ri==0 else F,9);C.setFillColor(BLACK);C.drawString(x+8,y-13,v);x+=w
  y-=rh
 y-=10

start('Meeting regions facilitator guide','Week 22  |  Planar convex partitions  |  Prepared 3 October 2026')
p('Help children make two filled stretched-band regions from four labeled points, then ask whether every placement can be split successfully. The answer is yes. Three points do not give the same guarantee.','lead')
note('Status and scope.','This is a separate adult-guide draft for the finalized student v3 packets. It is unpiloted and belongs to an unscheduled activity-library slot. Opening student pages now include the E-J region key. Timings below are planning choices, not classroom evidence.')
h('Use this guide at the table')
p('Begin with materials and a short shared demonstration (guide pp. 2-3). Offer a few pages at a time. Keep the answer galleries, seven-split checklist, and proof cases with the adult until children need them. A child may enter another band by readiness.')
p('<b>Notation:</b> AB | CD means one group contains A and B, and the other contains C and D. Each label occurs once. Reversing the two groups gives the same split. In the diagrams, the first group is solid blue and the second dashed rust; pale fill shows a triangle. A colored ring shows a singleton; an additional black ring marks a shared point. Gold marks a shared segment. Color is optional: solid/dashed and labels carry the meaning.')
h('Student packet and guide finder')
p('<b>K-1: 8 student pages, F22-K-v3.</b><br/>P1 on student p. 1 -> guide p. 5; P2 on pp. 2-3 -> p. 6; P3 on pp. 4-5 -> p. 7; P4 on p. 6 and P6 on p. 8 -> p. 8; P5 on p. 7 -> p. 9.')
p('<b>Grades 2-3: 8 student pages, F22-23-v3.</b><br/>P1 on student p. 1 -> guide p. 10; P2 on pp. 2-3 -> p. 11; P3 on p. 4 and P4 on pp. 5-6 -> p. 12; P5 on p. 7 and P6 on p. 8 -> p. 13.')
p('<b>Grades 4-5: 11 student pages, F22-45-v3.</b><br/>P1 on student p. 1 -> guide p. 14; P2 on pp. 2-3 and P3 on p. 4 -> p. 15; P4 on pp. 5-6 -> p. 16; P5 on pp. 7-9 -> p. 17; P6 on p. 10 -> p. 18; P7 on p. 11 -> p. 19.')
p('Common mathematical tools are on p. 4. Extensions, fidelity limits, and pilot notes are on p. 20. Source verification and reproducibility notes are on p. 21.','small')

start('Preparation and a concrete launch','Allow about 15 minutes of adult preparation before the session')
h('Prepare three tables')
p('At each table: two distinct A-D marker sets (eight movable markers), four Letter tracing sheets, two pencils or crayons, a ruler, an eraser, ten blank sheets, and removable tape. Give the two groups different colors or solid/dashed hatching. Keep spare tracing paper nearby for the multi-answer problems.')
p('Print single-sided on US Letter at 100 percent. Each full work board is 12.6 cm square. The 5.35 or 5.7 cm record boards preserve answers; they do not replace the large manipulation board. Three copies in a row on K-1 P2 are available spaces, not a promised answer count.')
p('For the current ten-child arrangement, one packet per child means 3 K-1, 4 middle, and 3 upper packets (89 student sheets total). A lower-paper option is one packet per pair plus blank/tracing paper: 2 of each band, 54 sheets. Adults should decide before printing; no child needs to finish every page.')
p('Read the answer key for your starting tasks, try a filled triangle containing a singleton, and check that both labels remain visible when stacked. Adults can draw a tiny cross for a center. Coordinate arithmetic in this guide is only an exact adult audit; children need none.')
h('A three-minute whole-group launch')
p('<b>First let children handle the markers.</b> Then place A, B, C, D at the four corners of a rough rectangle. Say: "Use every label once. Make two groups. Draw the smallest stretched-band region for each group. Find a point that belongs to both."')
p('Make one legal attempt, such as AB | CD along two opposite sides, and ask a child whether a point is shared. Allow another child to move one label to the other group or try a different grouping. Keep this an action demonstration, not a list of proof cases.')
p('Use the printed E-J key: E gives its point; F and G give the closed segment, including its endpoints; H, I and J give the lightly filled triangle, including its edge and interior. The interior cross marks a location, not another group label. Keep this key visible while children build their own regions.')
note('Say explicitly.','"Touching counts. Use the centers of the marks. Swapping the two group colors does not make a new split." Two labels may intentionally share a location, but both labels must still be used.')
note('Physical safety and accuracy.','No pins or stretched rubber bands are needed. If used, adults manage them. A rubber loop around one peg is not a small disk, and a loop around two pegs is not a thin rectangle. These are ideal points and segments.')

start('Flexible hour menu and prerequisite gates','Choose by observed readiness  |  No reading or arithmetic race')
h('A possible hour')
p('<b>0-5 minutes:</b> handle markers; make and change groups.<br/><b>5-8:</b> shared action launch.<br/><b>8-25:</b> work on a first fixed configuration and preserve a solution.<br/><b>25-28:</b> optional movement reset; children stand at four imaginary points and name two groups.<br/><b>28-50:</b> continue the chosen route, a construction, or a placement game.<br/><b>50-57:</b> share one surprising success or failed attempt.<br/><b>57-60:</b> save a picture and clear the table.')
p('The group-work budget is about forty minutes. A productive problem may occupy most of it. Offer a route change if energy drops; do not impose the next representation merely because time has passed.')
h('Three starting routes')
p('<b>Concrete meeting route:</b> K-1 P1, then P2 or P3, then P4 or P6. Use P5 when children are ready to compare all three-label splits. Adult reads aloud and records dictated groups. Stop after a child can build a legal split and identify an actual shared point.')
p('<b>Complete-search route:</b> middle P1, P2, then P3 or P4; P5 and P6 can continue another day. Stop after a complete list with a sensible reason, or a pair of constructions with no common winner.')
p('<b>Guarantee route:</b> upper P1, P3, then P4 and P5 as needed before P6-P7. P2 is useful preparation for degenerate cases. Stop after a justified conjecture if a full case argument is premature; distinguish it from a proof.')
h('Gates that matter')
p('<b>Entry:</b> recognize four labels, place each in exactly one nonempty group, and identify a point on a segment or in a filled region. Reading can be supplied orally; counting only to four is needed.<br/><b>Enumeration:</b> keep two attempts separate, recognize a color-swapped duplicate, and compare a short list.<br/><b>Universal explanation:</b> understand "every arrangement," a counterexample, an exhaustive case split, and why a boundary case still counts. No coordinates, fractions, algebra, or formal convexity vocabulary are prerequisites.')
note('Help only as needed.','Wait for attempts first. Ask a diagnostic question, offer the first held hint, then pause again. The second hint can reveal a useful smaller search. Give a worked split only when the action itself is still unclear.')
note('Common trouble.','An outline-only triangle misses interior points; shade it. A thick stroke makes a near miss look successful; use centers and a ruler. An unused D makes an illegal split; physically sort all four markers. Six record spaces do not mean six answers.')

start('Adult mathematical tools','Keep the catalog and proof categories off the student boards')
h('What a region means')
p('A group\'s convex hull is the smallest filled convex set containing its point locations. A point and a segment count as regions. With three collinear labels, the hull is the segment from the two outside locations, including the third. Repeated locations do not thicken the hull.')
h('Why there are seven candidate splits')
p('For four labeled points, group sizes are 1 + 3 or 2 + 2. There are four choices of singleton, and three ways to pair all labels. Thus there are seven unordered candidates. This is a completeness tool for the adult, not a required student procedure.')
p('<b>Singleton candidates:</b> A | BCD, B | ACD, C | ABD, D | ABC.<br/><b>Pair candidates:</b> AB | CD, AC | BD, AD | BC.<br/>Our answer tables write A in the first group, so B | ACD appears as ACD | B, for example.')
h('Three quick tests')
p('<b>Point versus triangle:</b> the singleton must lie in or on the other hull. Being near an edge is insufficient.<br/><b>Segment versus segment:</b> the closed segments must cross, touch, or overlap. Crossing the infinite supporting lines beyond their endpoints is insufficient.<br/><b>All points on a line:</b> replace each group by the interval from its leftmost to rightmost point. Two intervals meet exactly when they share a point.')
h('Why a general-position example has one answer')
p('For a convex quadrilateral, a singleton lies outside the triangle of the other three, and the two pairings of opposite boundary edges are disjoint. Only the pairing of opposite corners crosses. For a triangle with a fourth point strictly inside, only the inside singleton works: every outside vertex is outside the other triangle, and a segment from an outside vertex to the interior point cannot reach the opposite side.')
p('That last segment stays in the triangle\'s interior after leaving its starting vertex. The opposite side is part of the boundary, so the segment cannot meet it. These observations check all four singleton and three pairing possibilities, without relying on a picture alone.')
h('Existence and uniqueness are different')
p('Four labels always permit at least one successful split, but there need not be just one. The full proof, including collinearity and coincidence, is on guide p. 18. A single successful example does not establish a guarantee. A single failed split does not establish an impossible arrangement.')
p('The exact rational audit uses separate point-in-triangle and segment-intersection tests for all seven candidates. It does not import the student checker. Its finite stress test supplements the geometric proof; it cannot replace the proof.','small')

start('K-1 Problem 1','Student p. 1  |  Three different positions of D')
p('<b>Gate:</b> use all four labels once and find a point shared by two filled regions. Read the task aloud. Keep A, B, C fixed and move only D to one cross at a time.')
row([('K1_1','AD|BC','Upper-right cross: AD | BC'),('K1_2','ABC|D','Inside cross: ABC | D'),('K1_3','AC|BD','Left cross: AC | BD')],148,29)
p('<b>Exact answer:</b> each of the three placements has exactly the one split shown. The outside placements form convex quadrilaterals; their opposite-corner pairs cross. At the middle placement, D is strictly inside triangle ABC, so D | ABC works even though D is on none of the triangle\'s sides.')
note('Shared points.','On the outside placements, mark the actual crossing of the two drawn segments. At the inside placement, mark D itself. The circled point belongs to both regions in each diagram.')
note('Held hint 1.','"Can a group have just one dot? What is that dot\'s region?" Use only if the child rules out 1 + 3 grouping.')
note('Held hint 2.','For an outside placement: "Could both regions be straight segments?" Let the child choose which labels to pair.')
note('Reasoning and check.','The general-position argument on guide p. 4 rules out all other candidates. The three successful sets are {AD | BC}, {ABC | D}, and {AC | BD}; color-swapped drawings are duplicates.')
note('Listen for.','A child may say "they do not touch" when D is inside the triangular outline. Ask whether the whole filled triangle includes D. Do not change the rule to boundary-only contact.')
note('Extension and stopping point.','After two successful placements, ask a partner to choose a new D location. This leads directly to P4. Stop when the child can demonstrate a shared point without adult rescue; uniqueness is adult background here.')

start('K-1 Problem 2','Student pp. 2-3  |  All successful splits at three boundary placements')
p('<b>Gate:</b> distinguish a new grouping from a color swap and preserve separate attempts. The record page has three copies of each placement; only two successful splits exist for each.')
row([('K2_1','AB|CD','D on AB: AB | CD'),('K2_1','ABC|D','D on AB: ABC | D'),('K2_2','AD|BC','D beyond B: AD | BC')],126,42)
row([('K2_2','ACD|B','D beyond B: ACD | B'),('K2_3','AC|BD','D on AC: AC | BD'),('K2_3','ABC|D','D on AC: ABC | D')],126,42)
p('<b>Complete lists:</b> between A and B: AB | CD and ABC | D (shared point D). Beyond B: AD | BC and ACD | B (shared point B). On AC: AC | BD and ABC | D (shared point D). Each has exactly two.')
note('Why no others.','The middle point of the collinear triple can stand alone opposite a triangle; or it can be paired with the off-line point opposite the two endpoints. Every other split separates the hulls. Check the seven adult candidates if a child asks whether the list is complete.')
note('Held hints.','First: "Which point is between two others?" Then: "Can that point be alone? Can it be in a two-dot group instead?" Keep each success on its own record board; do not fill every space.')

start('K-1 Problem 3','Student pp. 4-5  |  The printed order is A, D, C, B')
p('<b>Gate:</b> treat every group on a straight line as a segment or point; recognize equivalent splits. The labels are deliberately not in alphabetical spatial order.')
line_gallery('K3',['AB|CD','AC|BD','ABC|D','ABD|C'])
p('<b>Exactly four successes:</b> AB | CD, AC | BD, ABC | D, and ABD | C. The first two share the full segment from D to C. The third shares only D, and the fourth shares only C.')
p('On this board D = (4.5, 6.3) and C = (7.5, 6.3), so the common segment of the two pairing solutions has length 3 cm at actual size. Measuring it is not required.')
h('A complete child-accessible explanation')
p('A or B alone cannot reach the other group because each is an outside point. C or D alone lies in the segment spanned by the other three, so both singleton choices work. Of the three pairings, AB | CD and AC | BD have overlapping intervals. AD | BC leaves a gap between D and C, so it fails. That checks all seven possibilities.')
note('Held hint 1.','"If three dots lie on one straight line, what is their stretched-band region?" Let the child cover it with a ruler or a strip of tracing paper.')
note('Held hint 2.','"Could a middle dot be a group by itself? What happens if an end dot is by itself?" If needed, keep the two successful pairings alongside the two singleton answers.')
note('Record without overload.','The six small boards are optional record spaces. A dictated label grouping beside a single clear picture is enough. Do not draw four overlapping answers on the large work board.')
note('Extension.','Swap two labels while leaving the locations fixed. The number stays four, but the written winning splits may change. A child can predict the new label strings and then check them.')

start('K-1 Problems 4 and 6','Student pp. 6 and 8  |  Placement games')
secproblem('Problem 4 with A, B, C fixed',' 6.','find and record one successful split for a chosen D placement.')
p('<b>Answer:</b> yes, the responding player can always succeed. The fixed ABC is a noncollinear triangle. If D is inside or on it, ABC | D works. Outside, the appropriate opposite-corner pairing may work; in an outside triangular-hull case an original vertex can be the inside point instead. A point on an extended side can also make an original vertex the middle of a collinear triple.')
p('Do not tell children that "outside means pair diagonals" in every case. For example, if D is far enough beyond A, A may lie inside BCD, so A | BCD is the useful split. Use the exhaustive rule on guide p. 18 if the adult is unsure.')
secproblem('Problem 6 with every point movable',' 8.','the same legal-split action, plus patience with a partner\'s placement.')
p('<b>Answer:</b> yes again. No arrangement of four labeled planar points defeats every split. This remains true on one line and at repeated locations. Children can test a conjecture through play; they need not produce the full proof to participate.')
row([('INNER','ABC|D','Inside singleton'),('OUTER','AC|BD','Crossing pairs'),('CONTACT','ABC|D','Boundary contact')],140,35)
note('Held hint 1.','"Could one point already belong to the region made by the other three?" Ask only after a real attempt, and allow the child to choose the singleton.')
note('Held hint 2.','"Try making two straight regions." If labels coincide, ask what happens when those two labels are put in different groups.')
note('Adult proof and game care.','Use guide p. 18 for all arrangements. Take turns placing, grouping, and checking. A slow response is not evidence of an impossible placement. Allow deliberate coincidences with both labels visible; do not enforce an unannounced general-position rule.')
note('When to stop.','Save one attempt that first looked impossible. Let its maker explain the eventual shared point. Return to a fixed board if placement freedom overwhelms the child.')

start('K-1 Problem 5','Student p. 7  |  Every possible place for C')
p('<b>Gate:</b> with three labels, understand that one group must be a singleton and the other a segment. This revised problem asks for a whole set of positions, beyond the three printed tests.')
row([('K5_1','AB|C','Middle cross: AB | C'),('K5_2','AC|B','Right cross: AC | B'),('K5_3',None,'Upper cross: impossible')],148,29)
p('<b>Full answer:</b> C may be anywhere on the entire horizontal line through A and B, restricted to the square. Include the portions left of A and right of B, and include coincidence with A or B. No point off that line works.')
p('<b>Exact locus:</b> A = (2.5, 5.6), B = (8.8, 5.6). Thus C = (x, 5.6) with 0 &lt;= x &lt;= 12.6. Coordinates are adult checks measured from the board\'s lower-left corner; children can draw the full line with a ruler.')
h('Why these are all the positions')
p('For three distinct collinear locations, one is in the middle. Put that label alone, and the other two make a segment containing it. If C is left of A, use A | BC; if C is between A and B, use AB | C; if C is right of B, use AC | B.')
p('If C = A, both A | BC and AB | C work. If C = B, both AC | B and AB | C work. Coincident labels stay distinct labels. If C is off line AB, the three points form a triangle. Each of the three splits isolates a vertex that is not on the opposite side, so every split fails.')
note('Held hint 1.','"Does C have to be the dot that is alone?" This challenges the common guess that only segment AB works.')
note('Held hint 2.','"Try C beyond A. Which of the three dots is in the middle now?" Then let the child test an off-line point and use the three singleton choices.')
note('Extension and evidence.','Ask a partner to put C just above the line, then exactly on it. Judge centers, not the thickness of the marker. Record the entire horizontal trace as the answer rather than only the successful crosses.')

start('Grades 2-3 Problem 1','Student p. 1  |  Four placements, including exact boundary contact')
p('<b>Gate:</b> shade a filled triangle, draw closed segments, and mark a genuine common point. One success per cross is required; the boundary cross has two possible answers.')
row([('M1_1','AD|BC','Upper-right: AD | BC'),('M1_2','ABC|D','Interior: ABC | D')],166,55)
row([('M1_3','AB|CD','On AB: AB | CD'),('M1_4','AB|CD','Below AB: AB | CD')],166,55)
p('<b>All successful sets by cross:</b> upper-right {AD | BC}; interior {ABC | D}; on AB {AB | CD, ABC | D}; below AB {AB | CD}. At the on-AB cross, either answer meets at D. At the interior cross, the shared point is D. The remaining crosses meet at the drawn segment crossing.','small')
note('Proof check.','The off-boundary examples have no three collinear and use guide p. 4. The on-AB cross is D = (6, 2.5), exactly halfway along A = (2, 3) to B = (10, 2). It is a real contact case. D = (6, 1) is below AB, so the last crossing is not at D.')
note('Held hints.','First: "Can a point be a region?" Then, if needed: "What happens when you pair the dots across the outside shape?" Do not require an exhaustive list on this launch page.')

start('Grades 2-3 Problem 2','Student pp. 2-3  |  The printed order is A, D, B, C')
p('<b>Gate:</b> compare complete lists without color-swapped duplicates. The record page supplies six blank copies so children can organize their own search.')
line_gallery('M2',['AB|CD','AC|BD','ABC|D','ACD|B'])
p('<b>Exactly four:</b> AB | CD and AC | BD share segment DB. ABC | D shares D. ACD | B shares B. The shared segment runs from (4.6, 6.3) to (7.8, 6.3), length 3.2 cm at actual size.')
h('Exhaustiveness')
p('The outside labels are A and C, so A | BCD and ABD | C fail. The two inside labels D and B may be isolated, giving ABC | D and ACD | B. Among pairings, AB | CD and AC | BD have overlapping intervals. AD | BC has a gap from D to B and fails. These are the four singleton choices and three pairings, with no duplicates.')
note('Held hint 1.','"How can you tell whether a drawing you already have is being counted again?" Let children invent a recording system before offering label strings.')
note('Held hint 2.','"What sizes can the two groups have?" If the child proposes 1 + 3 and 2 + 2, use those as their own way to organize the search, rather than handing over the seven-item list immediately.')
note('Why line order matters.','Do not reuse K-1 P3\'s label answer list. Both boards have four winners, but their two inside labels differ. Checking the geometry is more reliable than remembering a string.')
note('Extension.','Keep the line but change unequal gaps, then ask whether any successful split changes. As long as the left-to-right label order and distinctness remain the same, the success list stays the same: interval overlap depends on order, not distance.')

start('Grades 2-3 Problems 3 and 4','Student pp. 4-6  |  Shared segments and incompatible answer sets')
secproblem('Problem 3 a whole segment',' 4.','distinguish a point, a segment, and a triangle with positive area.')
p('<b>Construction:</b> on one horizontal line put A, B, C, D in that order at x = 2, 4, 8, 10 and y = 6. Use AD | BC. Their common region is all of BC, a positive-length segment.')
row([('LINE','AD|BC','P3: the whole segment BC'),('INNER','ABC|D','P4 first arrangement'),('OUTER','AC|BD','P4 second arrangement')],137,39)
p('<b>Filled triangle is impossible:</b> a partition of four labels has group sizes 1 + 3 or 2 + 2. At least one group has at most two labels, so its hull is a point or a segment. The intersection is a subset of that hull and cannot contain a nondegenerate filled triangle. A narrow triangle still has positive area; line thickness cannot supply it.')
note('Held hints for P3.','First: "Could both regions lie on the same straight line?" Then for the impossibility: "How many labels can the smaller group contain?"')
secproblem('Problem 4 no split works for both','s 5-6.','compare complete success sets for two arrangements, not just two chosen successes.')
p('<b>First:</b> A = (2,2), B = (10,2), C = (2,10), D = (4,4). Only ABC | D works. D is strictly inside ABC because x &gt; 2, y &gt; 2, and x + y &lt; 12.<br/><b>Second:</b> A = (2,2), B = (10,2), C = (10,10), D = (2,10). Only AC | BD works, at (6,6).')
p('The complete success sets {ABC | D} and {AC | BD} are disjoint. The uniqueness proof on guide p. 4 and the full seven-split table on p. 17 verify the stronger requirement. Simply displaying different successful splits would not by itself show that no other split works for both.')
note('Held hints for P4.','First: "Keep both arrangements visible. Can your successful split from one work in the other?" Then: "Could you make an arrangement with only one success?" Keep the geometric construction idea in reserve.')

start('Grades 2-3 Problems 5 and 6','Student pp. 7-8  |  A three-point locus and the four-point game')
secproblem('Problem 5 three points',' 7.','reason through three singleton-versus-segment possibilities.')
# Manual diagram row, with second showing whole exact sloping locus.
diagram('M5',None,LEFT+35,y,160,'Printed triangle: no split works')
diagram('M5',None,LEFT+292,y,160,'All successful C positions',points={'A':(2,3),'B':(10,4)},locus=True)
y-=192
p('<b>Printed configuration:</b> impossible. The three candidates are A | BC, AB | C, and AC | B. Each leaves a triangle vertex off its opposite segment. This covers every legal split.')
p('<b>All new positions of C:</b> the entire line through A and B inside the box, including beyond both endpoints and at A or B. In adult coordinates it is y = 11/4 + x/8, from (0, 11/4) to (63/5, 173/40). The exact board side is 12.6 = 63/5.')
p('For three distinct collinear points isolate whichever is in the middle; at C = A or C = B separate the coincident labels. Off the line, each singleton lies away from its opposite segment, so no split succeeds. This proves both inclusion and exclusion, not just a set of sampled positions.')
note('Held hints for P5.','First: "Does C have to be alone?" Then: "What are all three possible choices for the single dot?" Ask about the two extensions if only segment AB is recorded.')
secproblem('Problem 6 four-point challenge',' 8.','build a legal split for a partner\'s example and distinguish a failed attempt from impossibility.')
p('<b>Answer:</b> four always suffice. The responder has a successful split for every placement, including collinear and coincident ones. Use the complete proof on guide p. 18 as the adult key. Any four-point drawing claimed impossible can be checked against the seven candidate splits.')
note('Held hints for P6.','First: "Can one dot be inside the other region?" Then: "Could two segments cross or overlap?" If no three lie on a line, look at the outside boundary. Keep the full case argument back until children seek a guarantee.')
note('Share.','One example that first looked impossible plus its successful split is a useful stopping point. Call "always works" a conjecture until the group has covered every kind of placement.')

start('Grades 4-5 Problem 1','Student p. 1  |  Four exact placements')
p('<b>Gate:</b> identify a shared point using filled hulls and ideal centers. A complete catalog is unnecessary here, but the adult should know where a second answer exists.')
row([('U1_1','AD|BC','Upper-right: AD | BC'),('U1_2','ABC|D','Interior: ABC | D')],166,55)
row([('U1_3','AB|CD','On AB: AB | CD'),('U1_4','AC|BD','Left: AC | BD')],166,55)
p('<b>Complete success sets:</b> {AD | BC}, {ABC | D}, {AB | CD, ABC | D}, {AC | BD}, in the order shown. At the interior point the shared point is D. At the boundary point both winners share D. The other two winners share the actual diagonal crossing.','small')
note('Exact boundary check.','A = (2,2), B = (10.5,3), and D = (6.25,2.5) is their midpoint. The left cross D = (1,6) is outside ABC and not on AC. General-position uniqueness and the boundary argument explain the counts 1, 1, 2, 1.')
note('Held hints.','First: "Which hull includes a dot without its being a corner?" Then: "Try both group-size patterns." Ask for an actual common point rather than a visual impression that the figures are close.')

start('Grades 4-5 Problems 2 and 3','Student pp. 2-4  |  Enumeration and a placement challenge')
secproblem('Problem 2 the sloping line','s 2-3.','recognize collinearity independent of page orientation; organize a complete list.')
p('<b>Printed order:</b> A, C, B, D along the diagonal. The small gallery below is rotated flat to make the order easy to compare; no point order changes.')
line_gallery('U2',['AB|CD','AD|BC','ABD|C','ACD|B'])
p('<b>Exactly four:</b> AB | CD and AD | BC share segment CB, from (5,6) to (8,9). ABD | C shares C; ACD | B shares B. The shared segment has length 3 times the square root of 2 cm; no length calculation is needed.')
p('<b>Completeness:</b> endpoints A and D cannot stand alone successfully; middle points C and B can. Pairings AB | CD and AD | BC overlap, while AC | BD leaves a gap. Thus the other three candidates, A | BCD, ABC | D, and AC | BD, fail.')
note('Held hints for P2.','First: "Which locations are the two ends?" Then: "How many singleton choices and pairings are possible?" Do not sort the labels alphabetically along the line.')
secproblem('Problem 3 challenge an opponent',' 4.','test, record, and distinguish a conjecture from a guarantee.')
p('<b>Answer:</b> the opponent can always find a successful split. There is no defeating four-point arrangement. The complete constructive strategy is on guide p. 18; it works for arbitrary placements, not only the printed instances.')
note('Held hints for P3.','First: "Does any dot lie in the region of the other three?" Then: "If all four are outside corners, what happens to the opposite-corner pairs?" If labels line up or coincide, ask about the exact point or segment shared.')
note('Keep the problem open.','Do not distribute the adult case checklist yet. Save attempted counterexamples as evidence for P6. If a child finds a success for each challenge, invite the partner to change the arrangement in a genuinely different way.')

start('Grades 4-5 Problem 4','Student pp. 5-6  |  Coincident A and D are still separate labels')
p('<b>Gate:</b> distinguish a label from its location. Stacking A and D preserves both labels; it does not replace them by one item.')
row([('U4','A|BCD','A | BCD'),('U4','AB|CD','AB | CD')],151,61)
row([('U4','AC|BD','AC | BD'),('U4','ABC|D','ABC | D')],151,61)
p('<b>Exactly four for the printed board:</b> all four splits shown, each sharing the location A = D = (3,3). They are precisely the ways to put A and D into different groups, up to swapping group names. Assign B and C independently to either side to obtain four choices.','small')
p('<b>Why the remaining three fail:</b> in AD | BC the location A = D is off segment BC. In ABD | C, C is off segment AB. In ACD | B, B is off segment AC. The three distinct locations form a noncollinear triangle.','small')
p('<b>General answer:</b> yes, a success always exists when any two labels coincide. Put one of that pair alone and the other with the remaining labels; both hulls contain their common location. The other points may lie anywhere or also coincide. The exact count need not remain four: if all four labels share one location, all seven splits work.','small')
note('Held hints.','First: "Can A and D belong to different groups even though they share a place?" Then: "Where would both regions have to contain a point?" Keep the mark centered and both label names readable.')

start('Grades 4-5 Problem 5','Student pp. 7-9  |  Revised requirement: different unique successes')
p('<b>Gate:</b> distinguish exactly one successful split from having found only one. Both first arrangements must have one winner, and their winning splits must differ. A mere translated copy does not meet the revised condition.')
row([('INNER','ABC|D','First: only ABC | D'),('OUTER','AC|BD','Second: only AC | BD'),('LINE','AD|BC','Third: four successes')],143,34)
p('<b>Reproducible constructions:</b> first A(2,2), B(10,2), C(2,10), D(4,4); second A(2,2), B(10,2), C(10,10), D(2,10); third A(2,6), B(4,6), C(8,6), D(10,6). All lie inside the supplied board. Children may make other correct examples.')
truth_table(['INNER','OUTER','LINE'],['First','Second','Third'])
p('For the first example D lies strictly inside ABC, and the common point is D. For the second, the two diagonals meet at (6,6). The uniqueness arguments on guide p. 4 rule out the other six splits in each. In the third, AC | BD and AD | BC share BC, ABD | C shares C, and ACD | B shares B.')
note('Held hint 1.','"How could you check that there is no second answer?" Ask for a systematic list before revealing a new geometry.')
note('Held hint 2.','"Can your two drawings have different group sizes in their only successful split?" This suggests a meaningful contrast without prescribing coordinates.')
note('Assessment.','A valid solution supplies three arrangements, checks the two different one-element success sets, and shows more than one winner for the third. For the printed request to explain the number, an exhaustive check is stronger than displaying only two winners.')

start('Grades 4-5 Problem 6','Student p. 10  |  A complete proof for every arrangement')
p('<b>Gate:</b> a reason must cover unseen placements. The following cases are an adult proof key. Invite children to organize their own examples before sharing this organization.')
row([('U4','A|BCD','Repeated location'),('CONTACT','ABC|D','Three on one line')],133,77)
p('<b>1. Repeated location.</b> If two labels share a location, put one alone and all other labels together. Both hulls contain that location. This also covers three or four coincident labels.','small')
p('<b>2. Distinct locations with a collinear triple.</b> Of those three locations, one is between the other two. Isolate that middle label. The hull of the remaining three contains the segment joining the two endpoints, hence contains the middle point. The fourth location can be anywhere. This includes all four collinear.','small')
row([('INNER','ABC|D','Triangle outside boundary'),('OUTER','AC|BD','Four outside corners')],133,77)
p('<b>3. Distinct locations and no collinear triple.</b> Their convex hull has either three or four corners. It cannot have one or two without collinearity, and there are only four points. With three corners, the remaining point is strictly inside their triangle; isolate it. With four corners, pair opposite corners. The diagonals meet inside the quadrilateral: opposite corners lie on opposite sides of either diagonal\'s supporting line, so the two closed diagonal segments cross.','small')
p('<b>Conclusion:</b> every arrangement is in one of these cases; in each, every label is used exactly once in two nonempty groups, and an actual shared point is identified. Thus every four-label planar arrangement has a successful split. Boundary contact is enough; positive area is never promised.','small')
p('<b>Held hints:</b> "What kinds of examples have we not covered?" Then, only if needed: "Could labels coincide? Could three line up? How many outside corners remain otherwise?" A list of many experiments remains evidence for a conjecture, not the universal proof.','small')

start('Grades 4-5 Problem 7','Student p. 11  |  The smallest guaranteed number is four')
p('<b>Gate:</b> separate "some arrangement works" from "every arrangement works." Use a counterexample to disprove a guarantee, and the previous proof to establish one.')
row([('U7','A|BC','A | BC fails'),('U7','AB|C','AB | C fails'),('U7','AC|B','AC | B fails')],148,29)
p('<b>The printed three points have no successful split.</b> Each of the three legal splits is drawn. A singleton is a triangle vertex, and the other hull is the opposite closed side. No vertex lies on its opposite side. These three possibilities exhaust the 1 + 2 group sizes.')
p('<b>Exact noncollinearity check:</b> A = (2,3), B = (10.3,4), C = (4.8,10.1). The determinant (B - A) cross (C - A) equals 5613/100, which is positive and nonzero. The printed triangle is genuinely noncollinear. Children can use its visible geometry; determinants are adult audit only.')
h('Why four is the sharp threshold')
p('<b>Four:</b> every arrangement works by the complete argument on guide p. 18.<br/><b>Three:</b> the printed noncollinear triangle is one arrangement that fails, so three cannot guarantee success.<br/><b>Two:</b> take two distinct locations. The only split puts one point in each group; their hulls are disjoint.<br/><b>One:</b> no partition into two nonempty groups exists.')
p('Thus four is the smallest positive number guaranteeing a successful split in the plane. Some three-point arrangements do work, such as a collinear triple, and two coincident labels work too. Those examples do not establish a guarantee for every arrangement.')
note('Held hint 1.','"How many possible ways can we split three labels into nonempty groups?" Let children draw all three before declaring impossibility.')
note('Held hint 2.','"To show that three does not guarantee success, must every three-point arrangement fail?" One clear counterexample is enough. Then check two and one to justify the word smallest.')
note('Extension.','Ask whether five or more points always work. Choose four, make a successful split, then add each remaining label to either group. Hulls can only grow, so the old shared point remains. This is a short extension of the four-point proof.')

start('Extensions and fidelity limits','Keep extensions optional and matched to prerequisites')
h('Ready-to-use extensions with answers')
p('<b>How much overlap?</b> Gate: compare dimension and group sizes. Ask whether four labels can ever give positive-area overlap. Answer: no, by the smaller-group argument in middle P3. Five can create a shared segment between a triangle and a segment; six can create positive-area overlap using two overlapping triangles. No claim of a universal guarantee is intended for these constructions.')
p('<b>One-dimensional threshold.</b> Gate: middle points and the meaning of always. Restrict all positions to a line. Three labels always work: isolate the middle of three distinct locations, or separate coincident labels. Two distinct locations fail. The sharp threshold on a line is three.')
p('<b>Maximum number of successes.</b> Gate: the seven-case catalog. Seven is an upper bound because there are only seven splits. It is attained when all four labels coincide. For four distinct collinear locations exactly four work, independent of spacing. General-position examples have exactly one.')
p('<b>Prescribed partition.</b> Gate: construction and counterexample. Could one fixed label split work for every placement? No. The inside-triangle example has only ABC | D; the square example has only AC | BD. Their disjoint answer sets already disprove a universal fixed split.')
h('What this session faithfully claims')
p('The mathematical payoff is the planar four-point convex-partition theorem, including its sharp threshold. The exact planar proof, fixed-instance checks, and uniqueness examples support that claim. The sequence does not establish higher-dimensional Radon theory, Tverberg\'s theorem, algorithms for arbitrary point clouds, or fractional-coordinate methods as child prerequisites.')
p('The guide diagrams are scaled answer diagrams, not full-size replacement student boards. Color, a visible line width, and rings are display conventions, not mathematical area. A shaded triangle always includes its boundary. Labels, rather than distinct locations, are partitioned.')
p('The finalized student revisions add record spaces, broaden K-1 P5 to every C position, and require different unique successes in upper P5. The earlier reviews assessed the preceding draft. This guide rechecked the final coordinates and new construction condition; review evidence is not a classroom pilot.')
h('After the first use')
p('Record which problems children actually used, where adults had to restate the action, whether filled hulls and singleton regions were understood, whether recording boards helped, and whether upper P6 reached a proof or a conjecture. Keep observations separate from guesses about causes. Revise pacing only after evidence; do not label this sequence classroom-tested merely because the mathematics was checked.')

start('Sources and verification','Source roles, exact audit, and portable editable files')
h('Verified mathematical source')
p('Jean Gallier and Jocelyn Quaintance, <i>Aspects of Convex Geometry</i>, author-hosted version dated 9 October 2025, section 3.5, Theorem 3.10 and Figure 3.10, printed pp. 75-77. Verified from the theorem and proof body on 3 October 2026.<br/><link href="https://www.cis.upenn.edu/~jean/combtopol.pdf" color="#224d6c">https://www.cis.upenn.edu/~jean/combtopol.pdf</link>')
p('The source gives Radon\'s theorem in arbitrary finite dimension and illustrates the planar four-point cases. It supplies adult mathematical context. This guide\'s elementary planar case proof, coincidence handling, all student-instance answers, and construction checks were worked out directly. The unverified Hug-Weil citation from older planning material is not used as evidence.')
h('Teaching context actually consulted')
p('Natasha Rozhkovskaya, <i>Math Circles for Elementary School Students</i>, "Introduction: Berkeley 2009," in the locally held MSRI/AMS book. That introduction describes adult assistance for each child and active parent involvement in the elementary circle. It supports the use of close adult help; it does not report a trial of this convexity activity.')
p('Repository AGENTS.md, README.md, the Week 22 activity prompt, the general and mathematics reviews, and the final v3 sources and PDFs were read. These supply the actual group, student-page conventions, materials, and revision history. The proposed timing, held hints, route choices, and stopping points are facilitator design suggestions, not claims extracted from the source book.')
h('What was checked independently')
p('A separate exact-rational checker examines every unordered split of all 27 fixed, three-point, and construction configurations. It uses direct point-on-segment, point-in-triangle, and segment-intersection predicates rather than importing the student hull checker. It records exact shared-point or shared-segment endpoints. It also checks 6,561 labeled placements on a 3 by 3 test grid, including coincident points, as a stress test.')
p('The new inside-triangle and square witnesses each have one successful split and those splits differ. All three collinear boards have four successes with their own label orders. The final student page counts are 8, 8, and 11. The universal existence claim rests on the complete proof on guide p. 18, not on the finite tests.')
h('Editable source and rebuild')
p('The companion facilitator-src folder contains build_guide.py (editable text and drawing source), check_math.py, geometry-results.json, student-input-manifest.json, checks.txt, README.md, and build.sh. Run ./build.sh from that folder with Python 3, ReportLab, pypdf, and Poppler installed. It writes the guide one level above and renders review images locally.')
p('The final guide was rendered and every page visually inspected. The student PDFs were read and rendered for matching only; no student page or source was changed by this separate guide step. SHA-256 hashes in the input manifest identify the exact matched student PDFs.','small')
C.save()
(ROOT/'layout-check.json').write_text(json.dumps({'pages':page,'lowest_text_baseline':min(v[2] for v in layout),'text_blocks':len(layout)},indent=2)+'\n')
print(f'Wrote {OUT} ({page} pages)')
