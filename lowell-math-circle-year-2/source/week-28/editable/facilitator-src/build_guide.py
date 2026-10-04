#!/usr/bin/env python3
"""Portable Week 28 adult guide. Requires reportlab and system DejaVu fonts."""
from pathlib import Path
import math,json,subprocess,sys
from functools import partial
from reportlab.pdfgen.canvas import Canvas
from reportlab.platypus import SimpleDocTemplate,Paragraph,Spacer,PageBreak,Table,TableStyle,Flowable
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
ROOT=Path(__file__).resolve().parent
subprocess.run([sys.executable,str(ROOT/'check_math.py')],check=True)
D=json.loads((ROOT/'independent-checks.json').read_text())
from portable_fonts import font_directory
fontdirs=[font_directory('DejaVu Sans',['DejaVuSans.ttf','DejaVuSans-Bold.ttf','DejaVuSans-Oblique.ttf'],'DEJAVU_FONT_DIR')]
for tag,file in [('Body','DejaVuSans.ttf'),('Bold','DejaVuSans-Bold.ttf'),('Italic','DejaVuSans-Oblique.ttf')]:
 found=next((d/file for d in fontdirs if (d/file).exists()),None)
 if not found:raise RuntimeError('Install DejaVu Sans fonts or add their directory to fontdirs')
 pdfmetrics.registerFont(TTFont(tag,str(found)))
pdfmetrics.registerFontFamily('Body',normal='Body',bold='Bold',italic='Italic',boldItalic='Bold')
W=518
styles={
 'title':ParagraphStyle('title',fontName='Bold',fontSize=21,leading=25,spaceAfter=12),
 'h':ParagraphStyle('h',fontName='Bold',fontSize=15,leading=19,spaceAfter=10),
 'sub':ParagraphStyle('sub',fontName='Bold',fontSize=11,leading=14,spaceBefore=9,spaceAfter=5),
 'body':ParagraphStyle('body',fontName='Body',fontSize=10.1,leading=14,spaceAfter=8),
 'small':ParagraphStyle('small',fontName='Body',fontSize=8.5,leading=11.5,spaceAfter=6),
 'cell':ParagraphStyle('cell',fontName='Body',fontSize=9,leading=12),
}
story=[]
def p(text,style='body'):story.append(Paragraph(text,styles[style]))
def h(text):p(text,'sub')
def page(title):
 if story:story.append(PageBreak())
 p(title,'h')
def table(rows,widths=None):
 rr=[[Paragraph(str(x),styles['cell']) for x in row] for row in rows]
 t=Table(rr,colWidths=widths,repeatRows=1,hAlign='LEFT')
 t.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),colors.HexColor('#e8edf1')),('GRID',(0,0),(-1,-1),.4,colors.HexColor('#ccd1d5')),('VALIGN',(0,0),(-1,-1),'MIDDLE'),('LEFTPADDING',(0,0),(-1,-1),7),('RIGHTPADDING',(0,0),(-1,-1),7),('TOPPADDING',(0,0),(-1,-1),6),('BOTTOMPADDING',(0,0),(-1,-1),6)]))
 story.append(t);story.append(Spacer(1,8))
class Disks(Flowable):
 def __init__(self,items,cols=4,r=34,height=None):self.items=items;self.cols=cols;self.r=r;self.width=W;self.height=height or math.ceil(len(items)/cols)*(2*r+54)
 def draw(self):
  c=self.canv;cw=W/self.cols;rh=self.height/math.ceil(len(self.items)/self.cols)
  for i,it in enumerate(self.items):
   x=cw*(i%self.cols+.5);y=self.height-rh*(i//self.cols+.5)+2;r=self.r
   rays=it.get('rays',[0,90,180,270]);labs=it.get('labels','');sectors=it.get('sectors')
   if sectors:rays=[sum(sectors[:j]) for j in range(len(sectors))]
   c.setStrokeColor(colors.black);c.setLineWidth(.8);c.circle(x,y,r)
   for j,a in enumerate(rays):
    z=math.radians(a);c.line(x,y,x+r*math.sin(z),y+r*math.cos(z))
    c.setFont('Body',7);c.drawCentredString(x+(r+9)*math.sin(z),y+(r+9)*math.cos(z)-2,str(j+1))
    if labs:
     lx=x+.63*r*math.sin(z);ly=y+.63*r*math.cos(z);c.setFillColor(colors.white);c.rect(lx-5,ly-5,10,11,stroke=0,fill=1);c.setFillColor(colors.black);c.setFont('Bold',10);c.drawCentredString(lx,ly-3,labs[j])
   c.circle(x,y,1.3,fill=1)
   c.setFont('Bold',9);c.drawCentredString(x,y-r-22,it.get('title',''))
   if it.get('added') is not None:
    z=math.radians(it['added']);c.setLineWidth(2);c.setDash(3,2);c.line(x,y,x+r*math.sin(z),y+r*math.cos(z));c.setDash()
class LayerDiagram(Flowable):
 def __init__(self):self.width=W;self.height=160
 def draw(self):
  c=self.canv;ox=90;scale=2.35;yy={3:36,4:66,1:96,2:126};interval={1:(0,30),2:(-30,30),3:(-30,120),4:(0,120)}
  for s in [3,4,1,2]:
   a,b=interval[s];c.setLineWidth(2);c.line(ox+scale*(a+30),yy[s],ox+scale*(b+30),yy[s]);c.setFont('Body',9);c.drawString(15,yy[s]-3,'Layer S'+str(s))
  joins=[(-30,2,3,-1,'r3 V'),(0,4,1,-1,'r1 M'),(30,1,2,1,'r2 V'),(120,3,4,1,'r4 V')]
  for a,s,t,side,label in joins:
   x=ox+scale*(a+30);ya,yb=sorted([yy[s],yy[t]]);c.setLineWidth(1)
   path=c.beginPath();path.moveTo(x,ya);path.curveTo(x+side*15,ya,x+side*15,yb,x,yb);c.drawPath(path)
   c.setFont('Body',8);c.drawCentredString(x+side*20,(ya+yb)/2+3,label)
  c.setFont('Body',8)
  for a in [-30,0,30,120]:c.drawCentredString(ox+scale*(a+30),10,str(a)+'°')
class Route(Flowable):
 def __init__(self,seq):self.seq=seq;self.width=W;self.height=40
 def draw(self):
  c=self.canv
  for i,a in enumerate(self.seq):
   x=22+i*67;c.setLineWidth(.8);c.circle(x,20,13);c.setFont('Bold',11);c.drawCentredString(x,16,a)
   if i<7:c.line(x+14,20,x+51,20);c.line(x+51,20,x+46,23);c.line(x+51,20,x+46,17)

def footer(c,doc):
 c.setFont('Body',8);c.drawString(47,28,'Bellingham Math Circle / Week 28 / Facilitator guide / Draft unpiloted')
 c.drawRightString(565,28,str(doc.page))

p('Week 28 flat folding facilitator guide','title')
p('Single vertex crease patterns','h')
p('<b>Draft and unpiloted. Unscheduled library slot.</b> This guide accompanies the finalized F28-K-v2, F28-23-v2 and F28-45-v2 student packets, each with six numbered problems. It does not change those pages. The goal is to build examples, find exact obstructions, and distinguish evidence from proof.')
p('<b>Physical preparation is still required.</b> No paper models were physically folded or classroom-tested in this work. Mathematical checks and diagrams below do not certify a reliable live demonstration. An adult must try the intended constructions on the actual paper before teaching; record difficulty and omit an unready demonstration.')
h('Choose an entry point by prerequisites')
table([['Entry','Useful prerequisites','Primary work'],['K-1','An adult reads aloud. Match four ray positions; distinguish two labels; count to eight. No degree arithmetic.','Refold prepared models; classify labels; share a fixed stock of tabs; find routes.'],['Grades 2-3','Match angle wedges without overlap; recognize a half-turn. Read letters and clockwise orders; degree arithmetic optional.','Exact mismatch, add a ray, enumerate and arrange sectors.'],['Grades 4-5','Reason about orientation, alternating sums, exhaustive cases and order. Addition to 360° helps.','Prove necessity; construct witnesses; complete the right-angle classification.']],[74,222,222])
h('A flexible hour')
p('<b>0-5 min:</b> handle prepared disks and loose wedges. <b>5-9:</b> shared launch. <b>9-27:</b> one substantial opening problem at each table. <b>27-30:</b> stand and mime mountains and valleys with hands, keeping the same front side. <b>30-52:</b> continue or switch to a contrasting task. <b>52-60:</b> share one construction and one reason something cannot work.')
p('Suggested menus: K-1 Problems 1-2, then 4 or 6; grades 2-3 Problems 1-3, then 4 or 6; grades 4-5 Problems 1-3, then 4-5 or 6. A child can stop after a good example or a convincing obstruction. Finishing six pages is not the session goal.')
h('Short shared launch')
p('Show the marked front. Let children feel one ridge and one trough from that side; name them M and V. Demonstrate one legal refold of the prepared right-angle disk, without listing all eight answers. Say: “Use every marked ray and keep the disk whole. Which labels let it close? A stubborn piece of paper may mean we need another attempt.” Show that a loose wedge measures an angle but is never part of the folding specimen.')

page('Preparation and safety')
p('For ten children and three adults, start with thirty thin disks about 18 cm across, ten plain replacements, six demonstration disks, three sheets of tracing paper, three rulers and three adult protractors. Add pencils, removable M/V tabs, envelopes for separate wedge sets, and adult scissors. Use thin paper rather than card for folding. Print student packets single-sided at 100%.')
h('Make three different measurement sets')
table([['Set','Exact contents','Use'],['Seven lettered wedges','A=30°, B=30°, C=60°, D=60°, E=90°, F=120°, G=150°. Common radius 2.25 cm if matching the printed silhouettes.','Grades 2-3 Problem 1. Letters distinguish equal-size pieces.'],['Sixteen matching wedges','A1-A4: 90,90,90,90; B1-B4: 45,90,90,135; C1-C4: 60,120,120,60; D1-D4: 30,60,150,120, in degrees. Radius 2.5 cm matches Problem 2.','One piece per printed sector, including all repeated sizes. Keep case letters and sector numbers visible.'],['Six repeated-letter wedges','A,A=30°, B,B=60°, C,C=90°. Use one common radius, about 2.4 cm to match the page.','Grades 2-3 Problem 6. Equal-letter copies are indistinguishable.']],[100,295,123])
p('Trace each sector onto a separate sheet before cutting. The printed disks are recording diagrams; use separate intact 18 cm folding models. Wedges should share a center and meet edge-to-edge without gaps or overlap. A larger matching set is fine if all its pieces and half-turn template are enlarged together. Never mix the seven-piece and sixteen-piece sets.')
h('Mark the folding models accurately')
p('Put a small “front” mark on every intact disk. Draw a center and ray 1 straight up; number rays clockwise. Use a ruler and adult protractor, without scoring or cutting. Copy the four recurring sector lists from the table on page 10. Prepare several four-right-angle models in advance, then gently unfold them for children to refold. Precrease only the listed rays. Replace a specimen that acquires an unintended permanent crease.')
p('K-1 Problem 4 needs six movable tabs per row: A has 2 M and 4 V, B has 3 M and 3 V, C has 4 M and 2 V. The printed labels are fixed. For Problem 6, make eight small state cards A-H so children can move the route before writing it.')
h('Safety and access')
p('Adults cut the disks and loose wedges before the meeting. If children cut measurement pieces, use child-safe scissors, stay seated, keep fingers clear and pass scissors handle first. Do not cut the folding disk, clip a folded tip or make a slit to force closure. Cross-section drawings in this guide are mathematical diagrams, not a child cutting instruction. Use flat fingertips; avoid sharp tools for crease pressing. An adult may do the folding while a child chooses labels, checks sectors and explains. Dexterity is not a prerequisite for the mathematics.')

page('Constructive models to pretest')
h('Two book folds give a verified right-angle example')
p('Start with front up, rays 1,2,3,4 at top,right,bottom,left. Bring the left semicircle up and over the vertical diameter onto the right semicircle, making rays 1 and 3 valleys. Then bring the upper quarter of this two-layer semicircle up and over its horizontal radius onto the lower quarter. From the original front, ray 2 is V and ray 4 is M. The resulting word is VVVM. Gently unfold enough to identify each ray; keep the front convention fixed.')
p('Rotating this construction relative to the numbered rays puts the exceptional M in any of four positions. Reversing every folding direction exchanges M and V, giving the other four words. These operations give eight mathematical witnesses. Do not merely rotate the recording page while pretending a fixed labeling changed.')
story.append(Disks([{'labels':'VVVM','title':'base witness VVVM'},{'labels':'VVMV','title':'exception on ray 3'},{'labels':'VMVV','title':'exception on ray 2'},{'labels':'MVVV','title':'exception on ray 1'}],r=31))
h('The symmetric unequal model C')
p('For sectors 60°,120°,120°,60°, the rays are 0°,60°,180°,300° clockwise from the top. Fold the left half onto the right along rays 1 and 3. Ray 4 lands on ray 2. Fold the two-layer portion between the top ray and the 60° ray over ray 2. It gives the same label word VVVM. This is an exact two-book-fold construction with no new crease.')
h('The unequal model D needs a tuck')
p('For sectors 30°,60°,150°,120°, use rays 0°,30°,90°,240°. A valid word is <b>MVVV</b>. Mark the four sectors S1,S2,S3,S4 clockwise after ray 1. Precrease only the marked rays with ray 1 mountain and the others valley. Guide the small S1 flap into the stack between S4 and S2; do not add a diameter crease. The target layer order in the four-layer region, bottom to top, is S3,S4,S1,S2. Page 4 gives a geometric certificate and a diagram to diagnose the target.')
p('<b>Before children arrive:</b> actually collapse C and D with the chosen paper, check the original-side labels after unfolding, and make a spare successful specimen. If D is not reliable, retain its exact mathematical status but let children record “not yet made” for their physical attempt. Do not count a cut-and-reassembled picture or a buckled model with extra creases as their successful fold.')

page('A geometric witness for the unequal model D')
p('This is a certificate of a noncrossing ideal flat state, plus a target for adult preparation. It is not a claim that a physical specimen was tested, and it is not a rigid-folding motion or a promise that the tuck is easy.')
p('Choose the flattened direction of ray 1 as 0°. Reflect successive sectors at every crease. The ray directions become 0°,30°,−30°,120°, then 0° again. Thus the flattened sectors occupy angular intervals S1=[0,30], S2=[−30,30], S3=[−30,120], S4=[0,120]. All are radius-preserving copies of the original sectors.')
story.append(LayerDiagram())
p('Angular cross-section of the flat state. Vertical spacing shows layer order only; paper thickness is idealized away. The curved connectors show which layers meet at a crease. They are drawn outside the relevant sector ends and do not cross. “Bottom” is the S3 line.','small')
h('Why the certificate works')
p('For angles between −30° and 0°, only S3 and S2 overlap; place S3 below S2. Between 0° and 30°, use bottom-to-top S3,S4,S1,S2. Between 30° and 120°, only S3 and S4 overlap, in that order. The restricted orders agree wherever the regions meet, so no two overlapping pieces reverse order.')
p('At 0°, ray 1 joins adjacent layers S4 and S1, with neither passing through the continuing S2 or S3 layers. At 30°, ray 2 joins adjacent S1 and S2 above the continuing S3 and S4. At −30°, ray 3 joins the two layers present there. At 120°, ray 4 joins the two layers present there. These joins supply all and only the original creases. The diagram is therefore a continuous piecewise-reflected disk with a compatible noncrossing layer order.')
p('With S1 and S3 front-up and S2 and S4 front-down, the joins read M,V,V,V from the original front. The smallest sector, S1, lies between opposite crease types. The 3-to-1 word VVVM is impossible here: its front-side joins force S1 below S4 below S3 below S2. At 30°, the ray-2 join from S1 to S2 would enclose S4 and S3, which continue across that direction, forcing a crossing. Thus this specific counterexample also shows why the count alone is insufficient for unequal sectors.')
h('What the drawing establishes')
p('It verifies mathematical realizability of this specific assignment, including layer compatibility. It does not prove that every alternating-angle pattern has a flat state, does not certify a multi-vertex sheet, and does not replace the required hands-on adult pretest.')

page('Two complete necessary-condition proofs')
h('An odd number of active rays is impossible')
p('Take a small closed walk around the interior center, crossing every ray exactly once and no other crease. In a fully flat fold, crossing an active crease reflects the next sector, reversing which original face is up. After an odd number of reversals the final sector would present the opposite face from the starting sector. But the walk returns to the same uncreased starting sector, whose orientation must agree with itself. This contradiction rules out every odd number of active rays. A ray left unfolded would invalidate the hypothesis.')
h('Every other sector must total a half-turn')
p('Suppose there are 2m positive sector angles a1,…,a2m, totaling 360°. Choose the first flattened ray direction as 0°. Along the paper, each crossing reverses the direction in which the next angle is swept. After one circuit the direction change is S=a1−a2+a3−a4+…−a2m. The final ray is the starting ray, so S is an integer multiple of 360°.')
p('Let O be the sum of odd-position sectors and E the sum of even-position sectors. Both are positive, and O+E=360°. Hence −360°&lt;O−E&lt;360°. The only multiple of 360° in this open interval is zero. Therefore O=E=180°. This proves the stated obstruction, rather than relying only on a suggestive picture.')
table([['For the child','Exact adult interpretation'],['“The face flips every time we cross a crease.”','Orientation parity rules out 3, 5 and 7 active rays.'],['“The gray pieces and white pieces each need a half-turn.”','For even degree, the alternating sum must be zero.'],['“It passes our test.”','This necessary condition did not rule it out. It has not validated arbitrary M/V labels.'],['“I cannot flatten it yet.”','A report about this trial. It is not a mathematical impossibility proof.']],[241,277])
h('Scope of the converse')
p('Kawasaki-Justin’s theorem additionally says that this alternating-angle condition is sufficient for a single interior vertex when M/V directions are free. That converse is source-backed adult context, not proved by the walk above. The student tasks that ask for physical witnesses are supported here by explicit constructions for their four-ray examples. Upper Problem 3 asks only which patterns the obstruction rules out.')
p('All statements here concern a small initially flat disk with positive sectors, zero-thickness ideal paper, every listed ray active and no extra crease. Layers may touch but may not pass through each other. Boundary vertices, cones, prescribed labels and multiple vertices require their own hypotheses.')

page('A complete proof for the four right angles')
p('This finite proof supports the “every” in the catalog tasks and upper Problem 5. It uses only four equal sectors and noncrossing layers; a general mountain/valley theorem is unnecessary.')
h('Reduce a fold to a stack')
p('Call the sectors S1,S2,S3,S4 clockwise between successive rays. Every crease is a reflection. Fix S1 in its original quarter-disk; the other three sectors all reflect onto that same quarter-disk. Since the sectors cannot pass through one another, they have one bottom-to-top order throughout their common interior. Separating touching layers by tiny gaps makes that order visible without changing the combinatorial argument.')
p('At one boundary of the quarter-disk the crease connections pair S1 with S2 and S3 with S4. At the other boundary they pair S2 with S3 and S4 with S1. Two connections at the same boundary cannot have alternating endpoints in the stack: an order such as a,c,b,d forces the a-b connector and c-d connector to cross. Disjoint or nested pairs do not cross.')
h('Check the entire finite list')
p('If S1 is bottom, the six possible orders are 1234,1243,1324,1342,1423,1432. Checking the two boundary pairings leaves only 1234 and 1432. A cyclic renaming of S1,S2,S3,S4 preserves both pairings, so the same six-case check covers each possible bottom sector. The complete survivor table is:')
table([['Bottom sector','Possible orders bottom to top','M/V words on rays 1,2,3,4'],['S1','1234; 1432','VVMV; VVVM'],['S2','2143; 2341','VMMM; MMMV'],['S3','3214; 3412','VMVV; MVVV'],['S4','4123; 4321','MVMM; MMVM']],[104,195,219])
p('To read the last column, let hi be sector Si’s height. S1 and S3 face up; S2 and S4 face down. The labels on rays 1,2,3,4 are V respectively when h4&gt;h1, h2&gt;h1, h2&gt;h3, h4&gt;h3; otherwise they are M. These are precisely the joins with original front faces toward each other.')
h('Both directions are now justified')
p('Necessity: all 24 possible stack orders have been covered, and each allowed word has three of one letter and one of the other. Sufficiency: the two-book-fold construction on page 3, its four rotations and its complete reversals realize every one of those eight words. Therefore there are exactly eight valid right-angle assignments. This reasoning does not assert that every unequal-angle 3-to-1 assignment works.')

page('K-1 Problems 1 to 3 and the eight-fold catalog')
p('Words always list ray 1, then 2,3,4 clockwise with ray 1 at the top. A and H are different labeled states even though both are valid folds. Use removable tabs and an adult scribe when needed.')
labels=['MMMV','MMVM','MVMM','VMMM','MVVV','VMVV','VVMV','VVVM']
story.append(Disks([{'labels':s,'title':f'{chr(65+i)}  {s}'} for i,s in enumerate(labels)],r=25,height=180))
h('Problem 1')
p('<b>Task:</b> make four distinct folds and mark all rays. <b>Answer:</b> any four different words in the catalog. For example A,B,C,D are all valid. Four drawings of the same labels in different physical orientations are not four numbered-ray solutions. Every word has a construction by page 3; page 6 proves that there are no others.')
p('<b>Hold these hints:</b> first offer a gently opened working model; then ask which ray has the different label; only after exploration suggest moving that exceptional label. Check the marked front before treating two children’s opposite labels as disagreement.')
h('Problem 2')
table([['Printed case and word','Result','Printed case and word','Result'],['A  MMMV','Works','B  MMMM','Impossible'],['C  MVVV','Works','D  MMVV','Impossible'],['E  MMVM','Works','F  MVMV','Impossible']],[154,105,154,105])
p('The exact mathematical choices are A,C,E. The worksheet asks children to circle each they make; a mathematically valid case that they have not made should remain a physical attempt in progress. Rule out B,D,F by the complete four-angle classification, not by repeated frustration.')
p('<b>Hold:</b> offer a second specimen, then ask whether one ray differs from all three others. Show a successful model only if needed.')
h('Problem 3')
p('<b>All four answers:</b> MMMV, MMVM, MVMM, MVVV. If M is the majority, its single V can occupy ray 2,3 or 4. If M is the minority, ray 1 is the only M. Those cases exhaust the catalog while keeping ray 1 fixed. <b>Hold:</b> ask whether ray 1 is the special ray or belongs to the group of three. Let children cover duplicate recordings instead of starting over.')

page('K-1 Problem 4 shared tabs')
p('<b>Answer:</b> all three disks can close in rows A and C; row B is impossible. Six tabs must fill all six blanks, with none borrowed between rows. Printed letters stay fixed. This revised task was checked afresh; its answer is not the draft’s independent two-letter completion exercise.')
table([['Disk in each row','Fixed labels','All possible completed words','M tabs needed'],['Left','M ? V ?','MMVM or MVVV','2 or 0'],['Middle','M M ? ?','MMMV or MMVM','1'],['Right','V ? V ?','VMVV or VVVM','1']],[98,100,215,105])
h('Every solution for the row stocks')
p('In row A there are two M tabs. The left disk must be MVVV; the middle and right disks each use one M. In row C there are four M tabs. The left disk must be MMVM; the middle and right again use one M each. The table below gives every completed triple, left to right. Equal-letter tabs have no individual identities.')
table([['Row A with 2 M and 4 V','Row C with 4 M and 2 V'],['MVVV / MMMV / VMVV','MMVM / MMMV / VMVV'],['MVVV / MMMV / VVVM','MMVM / MMMV / VVVM'],['MVVV / MMVM / VMVV','MMVM / MMVM / VMVV'],['MVVV / MMVM / VVVM','MMVM / MMVM / VVVM']],[259,259])
h('Why row B cannot work')
p('Every legal right-angle disk has an odd number of M labels, either one or three. Across three legal disks the total number of M labels is odd. The printed letters contribute three M labels; row B adds three more, giving an even total of six. This contradiction rules out every placement of its tabs. Equivalently, the completion table says the blanks can use only 0+1+1=2 or 2+1+1=4 M tabs, never three.')
h('Held hints and a useful stopping point')
p('First ask children to finish one disk while keeping its printed labels. If they get stuck on the shared stock, ask which disk can use either zero or two M tabs. Save the odd/even observation for a child seeking a reason that covers every placement. A child who makes rows A and C and explains the shortage or surplus in B has completed substantive work without listing all eight triples.')
p('For a concrete proof, put the two possible left-disk choices beside the two forced one-M requirements. Children can point to two or four M tabs and show that three never occurs. This is a complete finite argument without the vocabulary of parity.')

page('K-1 Problems 5 and 6')
h('Problem 5')
p('<b>Answer:</b> exactly the eight catalog words on page 7. Organize them by the exceptional ray and by whether its label is M or V: four positions times two types. The necessity proof is on page 6 and the construction is on page 3. <b>Hold:</b> let children arrange their recordings into “one M” and “one V” groups before asking which ray positions are missing.')
h('Problem 6')
p('<b>Two valid routes:</b> each visits all eight printed states exactly once, uses the required endpoints and changes exactly two ray labels at every step.')
story.append(Route(D['k1_p6_route_witnesses']['H']))
story.append(Route(D['k1_p6_route_witnesses']['D']))
table([['Route ending H','Changed ray numbers','Route ending D','Changed ray numbers'],['A→B','3,4','A→B','3,4'],['B→C','2,3','B→C','2,3'],['C→D','1,2','C→E','3,4'],['D→F','3,4','E→F','1,2'],['F→E','1,2','F→G','2,3'],['E→G','1,3','G→H','3,4'],['G→H','3,4','H→D','2,3']],[128,131,128,131])
p('<b>Complete move rule:</b> any two distinct catalog states are two changes apart except the complementary pairs A-H, B-G, C-F and D-E, which are four changes apart. To see why, each word has an odd number of M labels, so the number of changed positions between two words is even. Distinct words have distance two or four; four changes means every letter is reversed. This accounts for every legal and illegal move.')
p('The printed task asks for two routes, not all routes. The independent script nevertheless exhausts all permutations to check feasibility: there are 240 A-to-H routes and 248 A-to-D routes with the endpoint order fixed. These extra counts are adult checks, not expected child answers.')
h('Held hints')
p('Give movable A-H cards. Ask children to compare two cards ray by ray before drawing an arrow. If a route gets stuck, keep its first few cards and rearrange the rest; do not reveal an entire route immediately. A later hint is to identify the four forbidden complementary pairs. Children need not refold a disk seven times to verify a route: changing and checking tabs is the mathematical move.')

page('Grades 2-3 Problems 1 and 2')
h('Problem 1 seven wedges')
p('<b>All ten groups:</b> AG, BG, CF, DF, ABF, ACE, ADE, BCE, BDE, ABCD. Order within a half-turn does not create a new group; A and B remain distinct letters even though their angles agree. Every listed group sums to 180°. Children can certify this by fitting the pieces against a straight half-turn template.')
p('<b>Completeness:</b> with G=150° the remaining 30° is A or B. With F=120° and no G, the remaining 60° is C, D or AB. With E=90° and neither F nor G, the remaining 90° is one of A,B plus one of C,D, giving four groups. With none of E,F,G, all of A,B,C,D are needed. This gives 2+3+4+1=10 and covers every largest-piece case.')
p('<b>Hold:</b> offer the half-turn outline and ask for exact contact along both straight sides. Later ask what can accompany the largest unused piece. Do not equate equal area with equal angle or allow wedges to overlap.')
h('Problem 2 sixteen separately labeled wedges')
table([['Disk','Clockwise sectors 1,2,3,4','Shaded 1+3','White 2+4','Both half-turns?'],['A','90°,90°,90°,90°','180°','180°','Yes'],['B','45°,90°,90°,135°','135°','225°','No'],['C','60°,120°,120°,60°','180°','180°','Yes'],['D','30°,60°,150°,120°','180°','180°','Yes']],[45,227,81,81,84])
p('For B, the shaded pair falls short by 45° and the white pair exceeds a half-turn by 45°. These are exact mismatches in the ideal pattern; imprecise cutting may blur the observation but cannot change the angle sums. The successful cases pass the angle test; the question here is about measuring the two pairs, not about prescribed labels.')
p('<b>Hold:</b> have a child place A1 and A3 side by side with the tips together. For B, compare against a separate 45° reference if exact mismatch is hard to see. Do not use the earlier seven-piece set: it lacks the required 45° and 135° pieces and the needed repeated 90° pieces.')
h('What to hear before moving on')
p('A child should be able to distinguish “looks close,” “these pieces make exactly a straight angle,” and “these pieces cannot make a straight angle without a gap or overlap.” Degree notation is optional. Let pieces carry the arithmetic before naming the alternating-angle rule.')

page('Grades 2-3 Problems 3 and 4')
h('Problem 3 witnesses and the exact obstruction')
p('<b>A, C and D can close; B cannot.</b> One valid word for A is VVVM by two book folds; the same word works for C by the adjusted book-fold construction. For D use MVVV with the layer certificate on page 4. Other successful assignments can be accepted if an intact disk uses every listed ray and no extra crease. The task requests one witness per possible pattern, not all assignments.')
story.append(Disks([{'sectors':[90]*4,'labels':'VVVM','title':'A  VVVM'},{'sectors':[45,90,90,135],'title':'B  impossible'},{'sectors':[60,120,120,60],'labels':'VVVM','title':'C  VVVM'},{'sectors':[30,60,150,120],'labels':'MVVV','title':'D  MVVV'}],r=34))
p('B is impossible by 135° versus 225°, using the necessity proof on page 5. A child may explain with its assembled wedge pairs rather than written degrees. The construction of A,C,D establishes existence; a failure to make one with real paper should be recorded separately. <b>Hold:</b> revisit the measuring result, then offer the prepared witness to inspect and refold.')
h('Problem 4 the unique new ray in each case')
table([['Case','Given rays clockwise from top','Add ray at','Final sectors clockwise'],['A','0°,90°,180°','270°','90°,90°,90°,90°'],['B','0°,60°,180°','300°','60°,120°,120°,60°'],['C','0°,30°,180°','330°','30°,150°,150°,30°'],['D','0°,120°,180°','240°','120°,60°,60°,120°']],[45,188,77,208])
story.append(Disks([{'rays':[0,a,180],'added':360-a,'title':f'{chr(65+i)}  add {360-a}°'} for i,a in enumerate([90,60,30,120])],r=30))
p('<b>Uniqueness proof:</b> write the middle given ray as a, where 0&lt;a&lt;180°. If a new ray x is inserted between 0 and a, the alternating sum x+(180−a) can equal 180 only if x=a, an existing ray. If inserted between a and 180, the odd sum a+(180−x)=180 again forces x=a. Thus x must lie between 180 and 360. Its sectors are a,180−a,x−180,360−x; the odd sum gives x=360−a. This is valid and unique. Each completion is a two-book-fold model of page 3 with the second fold at a; VVVM is a witness. <b>Hold:</b> try the marked ticks, then compare alternating pairs before refolding.')

page('Grades 2-3 Problems 5 and 6')
h('Problem 5 every right-angle labeling')
p('<b>Answer:</b> the same eight words and diagrams on page 7. Keep ray 1 at the top; rotations count as new only when the numbered-ray labels change. A full justification has two parts: all listed words work by construction, and all others are ruled out by page 6. For children, sorting by “which ray is different?” gives a concrete completeness explanation once that classification has been established.')
p('<b>Hold:</b> ask the child to group drawings by whether they have one M or one V. Offer an adult-assisted refold for a missing state. A long struggle with the same disk is a reason to replace it or let the adult handle it, not to reduce the child’s reasoning task.')
h('Problem 6 four orders of the six wedges')
p('Here A=30°, B=60°, C=90°, and each letter appears twice. Four sample answers are <b>AABBCC, AABCCB, AACBBC, AACCBB</b>. Each word is read clockwise from the top ray; swapping the two physical copies of a letter makes no new order.')
table([['Exact word','Odd slots 1,3,5','Even slots 2,4,6'],['AABBCC','A,B,C = 180°','A,B,C = 180°'],['AABCCB','A,B,C = 180°','A,C,B = 180°'],['AACBBC','A,C,B = 180°','A,B,C = 180°'],['AACCBB','A,C,B = 180°','A,C,B = 180°']],[174,172,172])
p('To draw a sample, place the first wedge immediately clockwise after the top ray, then accumulate its angles. For AABBCC, the boundary rays are 0°,30°,60°,120°,180°,270°. For AABCCB they are 0°,30°,60°,120°,210°,300°. For AACBBC they are 0°,30°,60°,150°,210°,270°. For AACCBB they are 0°,30°,60°,150°,240°,300°.')
story.append(Disks([{'sectors':a,'title':t} for a,t in zip([[30,30,60,60,90,90],[30,30,60,90,90,60],[30,30,90,60,60,90],[30,30,90,90,60,60]],['AABBCC','AABCCB','AACBBC','AACCBB'])],r=31))
p('There are 36 rooted letter orders in all, although only four are requested. Each alternating triple must contain A,B,C once: in units of 30°, three entries from {1,2,3} summing to 6 are either 1,2,3 or 2,2,2; the latter is unavailable because only two B pieces exist. Arrange A,B,C in odd slots in 6 ways and even slots in 6 ways, giving 36. This counts angle orders, not M/V assignments or different layer orders.')
p('<b>Hold:</b> first let children rearrange wedges freely. If needed ask what the alternating three pieces total. Only later suggest reserving one A, one B and one C for each alternating group. No physical six-crease fold is demanded by this problem.')

page('Grades 4-5 Problems 1 to 3')
h('Problem 1 distinguish a fold from an undecided attempt')
p('<b>Mathematical outcomes:</b> A,C,D are possible; B is impossible. The angles and exact totals are on page 10, and witness assignments are on page 11. The printed task deliberately permits a question mark when a child has not found a witness. Honor that recording: do not replace the child’s evidence with an asserted success. Return to the exact obstruction after Problems 2-3.')
p('<b>Hold:</b> ask what “every listed ray” rules out; offer a new specimen; then compare the folded model’s marked front to the recording. If needed, give the verified target layers for D rather than a general sufficiency claim.')
h('Problem 2 three odd-degree patterns')
table([['Case','Consecutive angles','Number of active rays','Answer'],['A','120°,120°,120°','3','Impossible'],['B','60°,60°,60°,90°,90°','5','Impossible'],['C','30°,30°,60°,60°,60°,60°,60°','7','Impossible']],[48,273,104,93])
p('The orientation-parity proof on page 5 covers all three. The sectors sum to 360° in each case, so a missing wedge is not the obstruction. <b>Hold:</b> label alternating sectors “front up” and “front down” as an imaginary walk crosses each ray. Ask what happens on the last crossing back to the first sector. This argument must use full active folds; adding a new crease changes the problem.')
h('Problem 3 alternating angles')
table([['Case','Odd sectors','Even sectors','What the proof establishes'],['A','45+90=135°','90+135=225°','Ruled out'],['B','30+60+90=180°','30+60+90=180°','Not ruled out'],['C','30+30+90=150°','30+60+120=210°','Ruled out'],['D','4×45=180°','4×45=180°','Not ruled out']],[48,147,147,176])
p('<b>Answer:</b> rule out A and C. Page 5 gives the complete requested proof, including why an apparent full-turn ambiguity cannot produce ±360°. In B and D, passing this test does not validate a particular M/V choice; none is prescribed here. The full unassigned theorem says they have flat states, but that converse is not needed to answer “which patterns does your explanation rule out?”')
p('<b>Held ladder:</b> let children assemble alternating wedges; then track a ray direction by successive reflections; finally name the two totals O and E. Do not immediately print the desired alternating equation on a child’s work. Stop with an exact impossibility explanation if the signed-angle proof is beyond current readiness.')

page('Grades 4-5 Problems 4 and 5')
h('Problem 4 constructions')
p('<b>Full possible list:</b> MMMV, MMVM, MVMM, VMMM, MVVV, VMVV, VVMV, VVVM. The page asks for as many as children can find and an explanation that each works. It does not yet require them to know the list is complete. For each state, use the two-book-fold construction, rotate the exceptional ray, and if needed reverse all folds. Page 7 supplies exact labeled diagrams.')
p('<b>Hold:</b> ask whether the same two operations can move the exceptional crease. To explain validity, children may perform or direct a construction, rather than cite the count condition. A drawing with three M labels and one V label is a proposed assignment until construction or a sufficient argument supports it.')
h('Problem 5 eliminate all remaining labelings')
table([['Printed case','Word','All cases represented by rotation'],['A','MMMM','MMMM'],['B','VVVV','VVVV'],['C','MMVV','MMVV, MVVM, VVMM, VMMV'],['D','MVMV','MVMV, VMVM']],[89,111,318])
p('<b>None of A-D can close flat.</b> Page 6 proves that every legal four-right-angle stack produces exactly one exceptional ray. Consequently four equal labels and every 2-and-2 arrangement are impossible. The table shows that rotations of the printed cases cover all eight invalid words.')
h('Why the classification is complete')
p('Four binary ray labels make 2×2×2×2=16 assignments. Count by number of M labels: there is one with zero M, four with one M, six with two M, four with three M, and one with four M. Problem 4 constructs the eight with one or three M. Problem 5 rules out the zero-M and four-M words and all six two-M words: in the latter, the two M positions are either adjacent (four choices) or opposite (two choices). No assignment belongs to both lists and no case is omitted.')
p('This is the revised finite four-angle task. It does not ask children to prove Maekawa’s theorem for arbitrary degree. If an adult mentions the general result |M−V|=2, identify it as a broader theorem rather than treating eight observed examples as its proof. Conversely, the complete local proof here is enough to justify the exact four-angle classification.')
h('Held hints and a concrete proof route')
p('First let children try the displayed labels. When someone says “none works,” ask for a reason other than failed trials. Lay four labeled sector cards in a stack and draw their two boundary pairings; show one interleaving pair and ask why its connectors would cross. Let an interested child check the six orders with S1 bottom. For a less abstract group, inspect the working folds and retain the proof as adult explanation, rather than claim the children independently established necessity.')

page('Grades 4-5 Problem 6')
p('<b>Answer:</b> exactly twelve clockwise orders start with 30° and give two alternating sums of 180°. The first sector lies immediately clockwise after the marked top ray. Equal copies are indistinguishable; reflections and rotations are not identified after this starting convention is fixed.')
rows=[['#','Clockwise sector order in degrees','Odd / even totals']]
for i,o in enumerate(D['grades45_p6_orders'],1):rows.append([i,', '.join(map(str,o)),'180° / 180°'])
table(rows,[36,335,147])
h('Complete count')
p('Divide all angles by 30°. Each alternating triple has three entries from {1,2,3} and must sum to 6. Sorted triples with that property are (1,2,3) and (2,2,2): if the smallest is 1, the other two must sum to 5 and hence be 2,3; if the smallest is 2, all three must be 2; if it is 3 the sum is at least 9. Only two 2s are available, so both alternating triples must contain one each of 1,2,3.')
p('The first 30° fills one odd slot. The other odd slots 3 and 5 hold 60°,90° in two possible orders. The even slots 2,4,6 hold 30°,60°,90° in 3×2×1=6 orders. The choices are independent, giving 2×6=12. They determine every position, so no two choices yield the same order. The displayed list contains each one exactly once.')
h('Held hints and limits')
p('Start with actual six wedges or six angle cards. Ask what three pieces could make 180°; later ask which positions alternate with the first sector. Save the product count until the child has a way to organize examples. The task counts angle sequences, not valid M/V assignments, layerings or physical folding motions. No six-ray folding pretest is needed to check these arrangements because the printed task does not request folding them.')

page('Extensions sources and readiness record')
h('Optional extensions with checked outcomes')
p('<b>Change one tab stock.</b> For K-1 Problem 4, ask which M-tab counts from 0 through 6 allow all three disks to close. Exactly 2 and 4 work, by the completion table on page 8; every other count fails. <b>Build a closed route.</b> A-B-C-D-F-E-H-G-A is a cycle through every state with two changes per move. Check each edge against the complementary-pair rule on page 9.')
p('<b>Generalize the new-ray problem.</b> Given rays 0°,a°,180° for any 0&lt;a&lt;180°, the unique fourth ray is 360°−a. The proof and book-fold construction on page 11 apply without restricting a to a 30° tick. <b>Why does 3-to-1 fail for unequal angles?</b> Inspect model D on page 4: local layer constraints at its smallest sector carry information beyond a count. Do not turn this question into an unsupported universal rule.')
h('Source trail and fidelity limits')
p('<b>Thomas C. Hull, The Combinatorics of Flat Folds: a Survey</b>, Origami3 (2002), author version arXiv:1307.1065. Section 2, Theorems 2.1-2.2, printed pp. 2-3: single-vertex angle and M/V conditions. Section 3: local versus global distinctions. Section 5 and Figure 4(a), printed pp. 7-8: eight right-angle assignments. The theorem’s full converse is cited as adult context; this guide supplies separate finite constructions and a four-sector layer proof. Verified 2026-10-03. <link href="https://arxiv.org/pdf/1307.1065" color="#174d77">Read Hull’s author PDF</link>.','small')
p('<b>Erik D. Demaine and Martin L. Demaine, Recent Results in Computational Origami</b>, OSME 2001, Section 3.1, printed p. 6: unassigned single-vertex versus assigned/global questions. Section 3.3 distinguishes existence of folded states from continuous folding processes. These scope distinctions guide our physical-readiness cautions. Verified 2026-10-03. <link href="https://erikdemaine.org/papers/OSME2001/paper.pdf" color="#174d77">Read the authors’ PDF</link>.','small')
p('<b>Natasha Rozhkovskaya, Math Circles for Elementary School Students</b>, local reference collection: Introduction “Berkeley 2009” describes adult assistance; Lesson 6, Problems 6.6-6.8 and “At the lesson” report that angle-assembly experiments did not automatically excite or clarify geometry for children. Our short launch, generous handling time and optional proof ladder are planning judgments informed by that account, not outcomes observed for Week 28. This guide’s exact tasks come from the finalized Week 28 packets, not from that book.','small')
h('Verification and what remains')
p('Fresh checks independently enumerate 24 right-angle layer orders, the revised tab stocks, all proposed routes, ten wedge subsets, all integer-degree candidate added rays, 36 unrestricted rooted six-angle orders and twelve starting with 30°. The continuous uniqueness proof covers rays between tick marks. The source folder includes the standard-library check script and its machine-readable result; it does not use the student builder as its oracle. All guide pages are rendered and visually inspected before delivery. Student pages remain unchanged.','small')
table([['Before teaching','Record after the adult pretest'],['Right-angle example and reversals','Date / paper / adult / difficulties: __________________'],['Unequal C and D; added-ray examples','Date / paper / adult / difficulties: __________________'],['Wedge sets and original-front labels','Checked / replacements / missing pieces: ______________'],['After the first session','What children tried / confusion / next revision: __________']],[254,264])
p('<b>Current readiness:</b> mathematically checked draft; unscheduled and unpiloted. Adult physical pretesting, session choice and classroom feedback remain outstanding.','small')

out=ROOT.parent/'build'/'facilitator-guide.pdf'
doc=SimpleDocTemplate(str(out),pagesize=(612,792),rightMargin=47,leftMargin=47,topMargin=42,bottomMargin=48,title='Week 28 flat folding facilitator guide',author='Bellingham Math Circle')
doc.build(story,onFirstPage=footer,onLaterPages=footer,canvasmaker=partial(Canvas,initialFontName="Body"))
print(out)
