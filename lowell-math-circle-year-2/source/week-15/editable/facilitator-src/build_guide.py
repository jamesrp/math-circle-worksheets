from pathlib import Path
from fractions import Fraction as F
from itertools import combinations
ROOT=Path(__file__).resolve().parent

# Independent, closed-half-plane cell construction. Student sources are never imported.
def ff(x): return F(str(x))
def cell(sites,name,box=3):
    out=[(-F(box),-F(box)),(F(box),-F(box)),(F(box),F(box)),(-F(box),F(box))]
    ax,ay=map(ff,sites[name])
    for n,(bx,by) in sites.items():
        if n==name:continue
        bx,by=map(ff,(bx,by));u,v=2*(bx-ax),2*(by-ay);c=bx*bx+by*by-ax*ax-ay*ay
        f=lambda p:u*p[0]+v*p[1]-c
        new=[]
        for p,q in zip(out,out[1:]+out[:1]):
            fp,fq=f(p),f(q)
            if fp<=0:new.append(p)
            if (fp<0<fq) or (fq<0<fp):
                t=fp/(fp-fq);new.append((p[0]+t*(q[0]-p[0]),p[1]+t*(q[1]-p[1])))
        out=new
    return out

def nearest(p,sites):
    p=tuple(map(ff,p));d={n:sum((ff(a)-b)**2 for a,b in zip(q,p)) for n,q in sites.items()}
    return ''.join(n for n in sites if d[n]==min(d.values()))
def xy(p):return '('+','.join(f'{float(v):.8f}' for v in p)+')'
AB={'A':(-2,0),'B':(2,0)}
OB={'A':(-1.5,-1),'B':(1.5,1)}
TRI={**AB,'C':(0,2)}
SQ={'A':(-2,2),'B':(2,2),'C':(2,-2),'D':(-2,-2)}
FIVE={**SQ,'E':(0,0)}
KP=[(-2.5,2.3),(-1.4,1.2),(-.55,2.4),(0,2.6),(.7,1.3),(2.4,2.3),(-2.55,-1.2),(-1.3,-2.25),(-.5,-.9),(0,0),(0,-2.5),(.6,-2.05),(1.5,-.8),(2.5,-2.3),(2.65,.75),(-2.55,.75)]
TP=[(-2.5,2.5),(-1.8,1.2),(0,1),(1.8,1.2),(2.5,2.5),(-2.3,-1.5),(-.7,-1.5),(0,-1),(1.3,-1.7),(2.4,-.9),(0,0),(0,-2.4)]
GP=[(-2.4,2.4),(-2,1),(-1,2),(0,0),(1,-1),(2.4,-2.4),(-2.2,-.4),(-.4,-2.2),(-2.1,-2.5),(.2,1.9),(1.7,.2),(2.4,2.5),(2.5,-.6),(-.6,2.5)]
DIAG={'A':(-1.5,-1.5),'B':(1.5,1.5)}

def diagram(sites,probes=(),annotate=False,only=None,added=(),removed=False,extra='',segments=()):
    out=[r'\begin{tikzpicture}[x=.445in,y=.445in]',r'\path[use as bounding box] (-3.16,-3.2) rectangle (3.2,3.2);']
    if only:
        out += [r'\fill[black!9] '+'--'.join(xy(p) for p in cell(sites,only))+r'--cycle;']
    out += [r'\begin{scope}',r'\clip (-3,-3) rectangle (3,3);']
    if removed:
        out += [r'\draw[black!50,densely dashed,line width=.9pt] (-2,0)--(2,0) (0,-2)--(0,2);']
    for n in sites:
        if only and n!=only:continue
        p=cell(sites,n)
        out += [r'\draw[line width=.7pt] '+'--'.join(xy(t) for t in p)+r'--cycle;']
    for p,q in segments:out += [r'\draw[black!50,dashed] '+xy(p)+'--'+xy(q)+';']
    out += [extra,r'\end{scope}',r'\draw[black!50,line width=.5pt] (-3,-3) rectangle (3,3);']
    for p in probes:
        x,y=p[:2];label=p[2] if len(p)>2 else ''
        label=label+(':'+nearest((x,y),sites) if label and annotate else nearest((x,y),sites) if annotate else '')
        out += [f'\\draw[line width=.6pt] ({x-.055},{y})--({x+.055},{y}) ({x},{y-.055})--({x},{y+.055});']
        if label:
            anchor='north west' if y>2.3 else 'south west'
            dx=.10 if x<2 else -.10
            if x>=2:anchor=anchor.replace('west','east')
            yy=y-.09 if y>2.3 else y+.09
            out += [f'\\node[anchor={anchor},fill=white,inner sep=.8pt,font=\\sffamily\\fontsize{{7.6}}{{8.4}}\\selectfont] at ({x+dx},{yy}) {{{label}}};']
    for n,(x,y) in sites.items():
        out += [f'\\draw[fill=white,line width=.7pt] {xy((x,y))} circle[radius=.065];',f'\\fill {xy((x,y))} circle[radius=.021];']
        anchor='south west'; dx=.1;dy=.10
        if n=='E' and removed:dy=.15
        if len(sites)==4 and sites.get('D')==(0,-2.5) and n=='D':anchor='north west';dy=-.13
        out += [f'\\node[anchor={anchor},fill=white,inner sep=.8pt,font=\\bfseries\\fontsize{{9}}{{10}}\\selectfont] at ({float(x)+dx},{float(y)+dy}) {{{n}'+('*' if n in added else '')+'};']
    out += [r'\end{tikzpicture}']
    return '\n'.join(out)

P=[]
def add(band,num,title,answer,why,hint,extend,sites,caption,**kw):
    P.append(dict(band=band,num=num,title=title,answer=answer,why=why,hint=hint,extend=extend,diagram=diagram(sites,**kw),caption=caption))

add('K--1',1,'Compare lengths',r'All crosses left of the vertical middle line get A; all right get B. The three crosses on the line get AB. The diagram labels all 16 answers (7 A, 6 B, 3 AB).',r'The two sites are mirror images in the middle line. Equal height does not determine the winner; distance to each center does.',r'Hold one end of a string on a cross, pinch its length to A, then swing the same length toward B.',r'Invite a child to choose a new cross whose answer is AB.',AB,'Small letters beside crosses give every nearest site.',probes=KP,annotate=True)
add('K--1',2,'An oblique dividing line',r'The whole boundary is the sloping line through the center shown at right. A owns its lower-left side, B its upper-right side; both own the line.',r'Fold A exactly onto B. Every crease point stays in place while A and B swap, so its two lengths agree. The nearer side is the side containing that site. Adult check: $3x+2y=0$.',r'If folding is awkward, trace the dots on translucent paper first.',r'Choose two far-apart places on the crease and check them with string.',OB,'The boundary reaches the top and bottom at $(-2,3)$ and $(2,-3)$.')
add('K--1',3,'A middle strip',r'A owns $x\leq-1$; B owns $-1\leq x\leq1$; C owns $x\geq1$. The left line is shared by AB, the right by BC. There is no AC nearest tie.',r'The two adjacent midlines bound the middle strip. On the line halfway between A and C, B is closer than either outside site.',r'After one pair agrees on a length, check that length against the third dot.',r'Ask whether a place very high above the middle dot still belongs to B.',{'A':(-2,0),'B':(0,0),'C':(2,0)},'The strip continues beyond both ends of the printed frame.')
add('K--1',4,'Three competitors',r'The top region belongs to C; the lower-left to A and lower-right to B. All 12 cross answers are marked. Counts: 3 A, 3 B, 1 C, 2 AB, 1 AC, 1 BC and 1 ABC.',r'The upper central cross belongs only to C even though its A and B lengths agree. The center belongs to ABC. The lower vertical ray is AB; the upper sloping rays are AC and BC.',r'For a proposed tie, ask whether another dot is even nearer.',r'Make one new cross for each kind of answer that occurs.',TRI,r'Closed cells: A: $x\leq0,\ y\leq-x$; B: $x\geq0,\ y\leq x$; C: $y\geq|x|$.',probes=TP,annotate=True)
add('K--1',5,'Four regions can meet',r'The middle vertical and horizontal lines divide the map into four quarters: A upper-left, B upper-right, C lower-right, D lower-left. Their crossing belongs to all four.',r'Symmetry makes the center equally far from all four sites. On each half-axis, only the two adjacent quarters share a nearest tie; at the center all four do.',r'Fold the left pair onto the right pair, then the top pair onto the bottom pair.',r'Have children find a place shared by exactly two dots.',SQ,'Adjacent regions share rays; opposite regions meet only at the center.')
add('K--1',6,'A new center takes a diamond',r'E gets the central diamond, including its edges. Each corner keeps the part of its old quarter outside the diamond. Its four vertices are three-way ties.',r'Compare E to each old site separately: four sloping midlines enclose E. Adult check: $|x|+|y|\leq2$. At $(0,2)$ the tie is ABE; at $(2,0)$ BCE; at $(0,-2)$ CDE; at $(-2,0)$ ADE.',r'Find just the boundary between E and A before comparing E with the others.',r'Overlay Problems 5 and 6. Which old shared places no longer belong to either old neighbor?',FIVE,'Dashed segments were old boundaries; their four outer endpoints remain ties.',removed=True)
add('K--1',7,'Take places from both dots',r'One valid choice puts the new dot C at the midpoint of A and B. C then gets a sloping strip; A and B get the two outside sides. Other successful placements are welcome.',r'Near C on either side of the old A/B boundary, C is strictly closer. The new boundaries are the perpendicular bisectors of AC and BC. Adult check: C gets $|3x-2y|\leq39/10$.',r'Where can you put a dot close to places from both old regions?',r'Let a partner propose a different placement and test a place taken from each old owner.',{'A':(-1.8,1.2),'B':(1.8,-1.2),'C':(0,0)},'C* is the added midpoint. Both strip edges are shared ties.',added=('C',))
add('K--1',8,'Make the target strip',r'Place B at $(-2,0)$ and C at $(2,0)$, or exchange their names. A gets exactly the shaded strip in the frame, including both dashed target edges.',r'Each new site is the mirror image of A across one strip edge. Those edges become the two bisectors. Outside them, the respective new dot wins.',r'Fold along one target edge. Where does the dot A land?',r'Choose a narrower strip around A and repeat on blank paper.',{'A':(0,0),'B':(-2,0),'C':(2,0)},r'A owns $-1\leq x\leq1$. Its whole region is an infinite strip.',added=('B','C'),only='A')
add('Grades 2--3',1,'From samples to a whole boundary',r'A wins at the 4 crosses with $x+y<0$; B at the 6 with $x+y>0$; the 4 with $x+y=0$ get AB. All 14 answers are shown. The full boundary is the descending diagonal.',r'The sites reflect across $x+y=0$. Testing crosses suggests the line; a fold or reflection explains the entire line and its two sides.',r'Find two tied places far apart, then ask what might connect them.',r'Choose a point not printed and predict its answer before measuring.',DIAG,'AB crosses are $(-2.4,2.4)$, $(0,0)$, $(1,-1)$ and $(2.4,-2.4)$.',probes=GP,annotate=True)
add('Grades 2--3',2,'An equality may lose',r'Three rays, rather than three complete lines, form the nearest-site boundaries. The center belongs to ABC.',r'A and B are equally far from every place on the vertical middle line. Below the center they are nearest; above it C is nearer. Keep only ties for nearest dots, including the three-way tie at the center.',r'Check all three lengths before keeping any pairwise tie.',r'Find a point on the erased part of the A/B bisector.',TRI,r'AB: $x=0,y\leq0$; AC: $y=-x,x\leq0$; BC: $y=x,x\geq0$.')
add('Grades 2--3',3,'Unequal gaps on a line',r'A: $x\leq-5/4$; B: $-5/4\leq x\leq3/4$; C: $x\geq3/4$. The boundary lines are AB and BC, respectively. No place belongs to all three.',r'An AB tie would need $x=-5/4$, whereas a BC tie needs $x=3/4$. No point can have both horizontal coordinates. Equivalently, the two midlines are parallel and different.',r'Compare the midpoints of the two neighboring gaps.',r'Move B along the line on a fresh map. Does a three-way tie ever appear while the sites stay distinct?',{'A':(-2,0),'B':(-.5,0),'C':(2,0)},'On the AC equality line $x=0$, the middle site B is closer.')
add('Grades 2--3',4,'All shared places in the square',r'The cells are the four closed quarters shown. Every point of either central axis is shared: AB above, BC right, CD below, AD left. The center belongs to ABCD.',r'Horizontal and vertical symmetry supplies the boundaries. AC and BD share the center only, so shared points need not form a positive-length edge.',r'At a proposed shared place, ask which of the four distances are shortest.',r'Compare with Problem 5: what changes when one corner moves?',SQ,'This is also the counterexample to a blanket claim that only three cells can meet.')
add('Grades 2--3',5,'A perturbed square',r'The sharing pairs are AB, AD, BC, BD and CD. AC has no shared point. The short BD edge joins $U=(0,-1/2)$ and $V=(3/8,0)$. U belongs to ABD; V to BCD.',r'The surviving outer rays are AB: $x=0,y\leq-1/2$; AD: $y=-1/2,x\leq0$; BC: $y=0,x\geq3/8$; CD: $4x+y=3/2,x\leq3/8$. BD is $y=4x/3-1/2$ between U and V.',r'Inspect a small neighborhood near the middle, rather than extending every crease forever.',r'Compare the two three-way vertices with the single four-way vertex in Problem 4.',{'A':(-2,-2),'B':(2,-2),'C':(2,2),'D':(-2,1)},'The BD segment has length $5/8$ map unit; it is not a four-way tie.',extra=r'\fill (0,-.5) circle[radius=.032] (.375,0) circle[radius=.032];\node[anchor=north east,font=\scriptsize,fill=white,inner sep=1pt] at (0,-.53) {U};\node[anchor=south west,font=\scriptsize,fill=white,inner sep=1pt] at (.4,.03) {V};')
add('Grades 2--3',6,'Which old boundaries disappear',r'E gets $|x|+|y|\leq2$. Each old dot keeps its old quarter intersected with $|x|+|y|\geq2$. On either old axis, the portions strictly between the diamond vertices cease to be old-site boundaries.',r'At the four vertices, E ties the two old neighbors, so retain the endpoints. On the open central segments E is strictly closer; beyond the diamond the old two-way ties survive.',r'Overlay the old map, and test a point near the center and one far along the same line.',r'Can an old site gain a place when a new site is added? Why?',FIVE,'Dashed cross: erased old boundaries. Solid diamond edges: new shared ties.',removed=True)
add('Grades 2--3',7,'Share with two regions and avoid the third',r'One successful choice is D at $(0,-5/2)$. It gets $y\leq-4|x|/5-9/20$. It shares the two lower sloping rays with A and B, and no point with C.',r'The new ABD vertex is $(0,-9/20)$, below the old ABC vertex $(0,0)$. The AB edge connects them. C still has $y\geq|x|$, leaving a gap between C and D. Putting D at $(0,-2)$ fails: D then shares the center with C.',r'If D touches C at the center, move D a little farther down and rebuild the comparisons.',r'For a centered D at $(0,-t)$, the construction works whenever $2<t\leq3$.',{'A':(-2,0),'B':(2,0),'C':(0,2),'D':(0,-2.5)},r'A: $x\leq0,\ 4x/5-9/20\leq y\leq-x$; B is its mirror.',added=('D',))
add('Grades 2--3',8,'Make a corner region',r'Put B at $(2,0)$ and C at $(0,2)$, or exchange their names. A gets $x\leq1$ and $y\leq1$, exactly the target inside the frame. B gets $x\geq1,y\leq x$; C gets $y\geq1,y\geq x$.',r'Reflect A across each of the two interior target edges. The remaining B/C boundary is the ray $y=x,x\geq1$. All three cells meet at $(1,1)$.',r'Which printed edges really separate owners, and which are merely the frame?',r'Extend the paper mentally: explain why A does not have a bounded square cell.',{'A':(0,0),'B':(2,0),'C':(0,2)},r'The left and bottom frame edges do not bound A\textquotesingle s whole region.',added=('B','C'))
add('Grades 4--5',1,'Certify the whole two-site map',r'The boundary is $3x+2y=0$. A owns $3x+2y\leq0$; B owns $3x+2y\geq0$. Every crease point is shared.',r'Folding A onto B proves equality on the crease. On A\textquotesingle s side, the segment to B crosses the crease at T. Since $TA=TB$, the triangle inequality gives $XA\leq XT+TA=XB$, with strict inequality off the crease. The opposite side is symmetric.',r'Use reflection to explain points not tested with a string.',r'Explain why measuring fifty points would still leave other points untested.',OB,'A perpendicular bisector certifies infinitely many comparisons at once.')
add('Grades 4--5',2,'Keep only nearest ties',r'A gets $x\leq0,y\leq-x$; B gets $x\geq0,y\leq x$; C gets $y\geq|x|$. The three surviving rays meet at the origin.',r'A pairwise bisector is only a candidate boundary: retain the parts where no other site is closer than the tied pair. The positive $y$-axis fails this test because C is nearer; the three surviving rays include their three-way meeting point.',r'On each proposed boundary, try a point on either side of the three-way meeting.',r'Draw a circle centered at the triple tie through all three sites. What would a site inside it do?',TRI,'The positive $y$-axis is an A/B equality, but is not a nearest-site boundary.')
add('Grades 4--5',3,'A whole bounded cell',r'D gets the triangle with vertices $(-7/4,1)$, $(7/4,1)$ and $(0,-5/2)$. Its inequalities are $y\leq1$ and $y\geq2|x|-5/2$. No joining segment can leave it.',r'D must stay on its winning side against each of A, B and C. Each allowed half-plane contains the entire segment between any two of its points. A segment between two points allowed by all three comparisons therefore stays allowed by all three.',r'Trace each allowed side on a separate sheet, then overlap the sheets.',r'The same argument works for any finite set of distinct point sites. Invite a child to explain that generalization.',{'A':(-2,-1),'B':(2,-1),'C':(0,2),'D':(0,0)},r'The shaded triangle is D\textquotesingle s entire cell, not merely its part inside the frame.',only='D',segments=[((-1.1,.7),(.8,-.3))])
add('Grades 4--5',4,'A four-way meeting',r'The cells are the four closed quarters. The origin is the only place shared by three or more sites; it is shared by all four. Elsewhere on an axis there are exactly two nearest sites.',r'The four sites lie on one circle centered at the origin. An AB equality requires $x=0$, and a tie with D also requires $y=0$, fixing the point. The same point also ties C.',r'Look for the center of a circle through the sites.',r'Explain why saying ``three regions always meet at a vertex\textquotesingle\textquotesingle\ is false. Compare the perturbed square in grades 2--3 Problem 5.',SQ,'A four-way tie is intentional; no general-position assumption is in force.')
add('Grades 4--5',5,'Insertion can only shrink',r'E gets the diamond $|x|+|y|\leq2$. Each old region is its old quarter cut by $|x|+|y|\geq2$. Erase the old axis pieces with distance from the origin strictly less than 2; keep the four endpoint ties.',r'For an old site A, its new region is its old region intersected with the additional condition $d(X,A)\leq d(X,E)$. An intersection cannot add points. Some regions may stay unchanged; none can grow.',r'Ask whether an old loser can become a winner merely because one more competitor appears.',r'Could removing a site shrink an old region? Reverse the comparison argument.',FIVE,'The diamond vertices are ABE, BCE, CDE and ADE, in clockwise order from the top.',removed=True)
add('Grades 4--5',6,'The fewest sites to close a strip',r'Two new dots suffice: D at $(0,2)$ and E at $(0,-2)$. B then gets exactly $[-1,1]\times[-1,1]$, entirely inside the frame. One new dot cannot work.',r'Originally B owns the unbounded vertical strip $|x|\leq1$. One new site contributes only one half-plane. If its height is positive, a downward vertical tail remains; if negative, an upward tail remains; if zero, a full vertical line remains. Thus at least two are necessary.',r'After trying one new dot, follow B\textquotesingle s region beyond the top and bottom of the picture.',r'Find another pair that makes B a bounded quadrilateral.',{'A':(-2,0),'B':(0,0),'C':(2,0),'D':(0,2),'E':(0,-2)},'D* and E* are added. The frame is $[-3,3]^2$; it does not itself stop a region.',added=('D','E'),only='B')
add('Grades 4--5',7,'Build the prescribed triangle',r'Reflect A across each target side. One labeling is B$=(0,-2)$, C$=(24/13,16/13)$ and D$=(-24/13,16/13)$. All three new dots fit in the frame.',r'The three winning comparisons are $y\geq-1$, $3x+2y\leq4$, and $-3x+2y\leq4$. Their intersection has exactly the target vertices $(-2,-1)$, $(2,-1)$ and $(0,2)$. No additional constraint appears.',r'Fold on one target edge and mark where A lands; repeat independently for the other two.',r'Can the same reflection construction make a different convex polygon around A?',{'A':(0,0),'B':(0,-2),'C':(F(24,13),F(16,13)),'D':(-F(24,13),F(16,13))},'Each side is shared with its reflected site. The whole closed triangle belongs to A.',added=('B','C','D'),only='A')
add('Grades 4--5',8,'A point that cannot be taken',r'R cannot be taken while P and Q still belong to A: R lies on segment PQ, and A\textquotesingle s cell is convex. S can be taken. Add B at $(0,-5/2)$; its bisector with A is $y=-1/4$.',r'A keeps $y\geq-1/4$, so P, Q and R remain strictly in A\textquotesingle s cell; S is strictly in B\textquotesingle s. At P and Q, squared distances are $8<41/4$; at S, $1/4<16$. Merely tying A at R would not remove R from A.',r'For R, draw the segment PQ. For S, try a new dot below it.',r'Every point in triangle APQ must also remain with A. Why must A itself always remain?',{'A':(0,2),'B':(0,-2.5)},'One successful construction for S; no construction works for R.',added=('B',),probes=[(-2,0,'P'),(2,0,'Q'),(0,0,'R'),(0,-2,'S')],segments=[((-2,0),(2,0))])

pre=r'''\documentclass[letterpaper,11pt]{article}
\usepackage[margin=.65in,headheight=14pt,headsep=.16in,footskip=.3in]{geometry}
\usepackage[T1]{fontenc}
\usepackage{lmodern}
\pdfmapfile{+lm.map}
\usepackage{amsmath,amssymb,tikz,fancyhdr,enumitem,hyperref,textcomp}
\hypersetup{hidelinks,pdftitle={Week 15 Nearest site regions Facilitator guide},pdfauthor={Bellingham Math Circle}}
\pagestyle{fancy}\fancyhf{}
\fancyhead[L]{\small Bellingham Math Circle}\fancyhead[R]{\small Week 15 / Adult guide / Piloted}
\fancyfoot[L]{\small Nearest-site regions}\fancyfoot[R]{\small\thepage}
\renewcommand{\headrulewidth}{0pt}\renewcommand{\footrulewidth}{0pt}
\setlength{\parindent}{0pt}\setlength{\parskip}{5pt}
\setlist[itemize]{leftmargin=1.3em,itemsep=3pt,topsep=3pt}
\setlist[enumerate]{leftmargin=1.5em,itemsep=3pt,topsep=3pt}
\newcommand{\heading}[1]{\par\vspace{5pt}{\large\bfseries #1}\par}
\begin{document}
{\LARGE\bfseries Nearest site regions}\par
{\large Facilitator guide for Week 15}\par
\textbf{Piloted.} The organizer tested this week with children and judged it good (reported October 4, 2026). This adult guide accompanies the three eight-page student packets, with Problems 1--8 in each. The hour below is the original proposal.

\heading{What the children are exploring}
A place belongs to every site that is nearest to it. Two sites give a straight dividing line; other sites can erase parts of that line. Whole regions come from satisfying all comparisons at once. Children can discover these ideas through string comparisons, folds and drawings; the coordinates in this guide are adult checks, not prerequisites.

\heading{Prerequisites and flexible entry points}
\begin{itemize}
\item \textbf{K--1:} compare two lengths and follow a spoken rule. Adult reads aloud and can scribe letters. No number reading, ruler arithmetic or coordinates needed.
\item \textbf{Grades 2--3:} compare several lengths, draw straight lines and keep all tied winners. Explain with a drawing or a spoken example; numerical measurement is optional.
\item \textbf{Grades 4--5:} reason about all points, overlapping allowed sides, possibility and a minimum. Algebra and formal proof notation are optional adult tools.
\end{itemize}
Grade labels are flexible. Offer a page based on readiness and interest. A child may spend the working time on two rich maps; finishing the packet is not the goal.

\heading{Practical preparation for ten children and three adults}
Print selected student pages single-sided, US Letter, at 100\% scale. Each working map is 5.8 inches across. Start with just one or two pages per child; hold the remaining pages in reserve. Make one adult copy of this guide and the relevant key pages for each table.

Prepare 10 pencils and erasers, 10 straightedges, 10 pieces of non-stretch string about 12 inches long, 40 sheets of translucent foldable paper, and 20 blank Letter sheets. Three colored pencils per child are optional; letters or hatching work equally well. These are preparation quantities, not checked inventory. Pre-cut string and try one fold before the meeting. Compare to the printed dot centers, not their circles or labels. Keep string on the table.

\heading{A flexible hour}
\begin{itemize}
\item \textbf{0--4 minutes:} freely try string comparisons and folds on spare paper.
\item \textbf{4--8:} launch together. Put two dots on a blank sheet; let a child choose a place and compare its straight lengths. Record A, B or AB. Say, ``We are finding every place that belongs to each dot. Tied nearest dots share the place.'' Demonstrate the recording, not the whole map.
\item \textbf{8--28:} work at three adult-led tables. Start with Problem 1; then K--1: 2 or 3; grades 2--3: 2 then 3; grades 4--5: 2 then 3. Offer a fold only if useful.
\item \textbf{28--31:} pause, stand and stretch. Two children act as fixed sites while another points to where a tie might be. Treat this as an estimate, not an exact measurement.
\item \textbf{31--52:} choose a branch: squares and insertion (K 5--6, middle 4--6, upper 4--5), or making a target (K 7--8, middle 7--8, upper 6--8). Save unfinished maps.
\item \textbf{52--60:} share a surprising tie or changed boundary. Ask for one drawing or physical reason; leave time to pack up.
\end{itemize}
\newpage
\begingroup\fontsize{10.5}{12.4}\selectfont
{\Large\bfseries Adult mathematical reference}\par
\heading{Shared conventions and fidelity limits}
All sites are distinct points and stay fixed within one map; placement problems add new sites without moving printed ones. Distance is straight-line distance in a flat plane, not grid travel. A cell is \emph{closed}: a point belongs to every nearest site. A two-way equality is not enough if a third site is nearer. The rectangular frame is only a window, except where a task explicitly compares a target inside it.

String and folding give evidence. Exact symmetry and the arguments below settle ties; do not turn printing or folding error into a new mathematical rule. Guide maps are reduced answer diagrams, not measurement masters. Use the original full-size student maps for children. Throughout the answer key, adult coordinates put the frame at $[-3,3]\times[-3,3]$, with $x$ right and $y$ up. A star marks a site added in one valid construction; inverse tasks can have other answers.

\heading{Why the methods work}
\textbf{Two sites.} Folding A onto B gives their perpendicular bisector. Reflection swaps A and B and fixes the crease, proving equality there. Each side is nearer its own site (see upper Problem 1). Only the crease ties.

\textbf{Several sites.} Keep the winning closed half-plane for one site against each competitor, then overlap those allowed sides. A surviving shared edge must also pass every other comparison. This explains why a third competitor can erase a pairwise bisector.

\textbf{Convexity.} A half-plane contains the entire segment between any two of its points. If both endpoints pass every comparison, so does their segment. Thus a cell cannot have a hole or an inward notch. This does not require children to know the word ``convex.''

\textbf{Insertion.} Adding a site adds a restriction for each old site. Old cells can shrink or stay the same; they cannot grow. Boundaries may disappear, but endpoints that remain nearest ties must be kept.

\textbf{Inverse construction.} To make an edge for A, reflect A across that edge and use its image as a competitor. The edge is then the bisector. Intersect all the chosen A-sides. This works for a convex polygon with A strictly inside it; it cannot make a nonconvex cell.

\textbf{Optional algebra.} For sites $a,b$ and test point $z$, squaring the nonnegative lengths and cancelling $z\cdot z$ gives
\[|z-a|^2\leq|z-b|^2\quad\Longleftrightarrow\quad 2(b-a)\cdot z\leq |b|^2-|a|^2.\]
This supplies the exact half-plane checks used for the answer diagrams.

\heading{Use hints sparingly and observe}
Let children make and test a proposal before offering the hint printed with each answer. Accept a fold, a drawing or a spoken argument. Ask ``Is some other dot closer?'' when an extra bisector remains; ``Does the region really stop there?'' when the frame is mistaken for a boundary. Record which pages were used, what children tried, and where adult rescue was needed.

\heading{Sources and scope of adaptation}
\textbf{Mathematical reference:} David M. Mount, \emph{CMSC 754 Lecture 10: Voronoi Diagrams and Fortune's Algorithm}, Fall 2021, pp. 1--3. The definition, half-plane description, convexity and nearest-tie circle interpretation inform this lesson. The source uses open cells and assumes no four cocircular sites for its three-edge vertex claim. Here cells include their boundaries, and the square intentionally has a four-way meeting. The concrete arrangements, inverse examples, proofs and answer checks are independently worked for these packets.\par
{\small\url{https://www.cs.umd.edu/class/fall2021/cmsc754/Lects/lect10-vor.pdf}}\par
\textbf{Pedagogical consultation:} Natasha Rozhkovskaya, \emph{Math Circles for Elementary School Students}, ``Introduction: Berkeley 2009'' (local EPUB, section beginning with that heading). It describes individual adult attention, two additional instructors, and parents helping children and distributing handouts. The pacing, launch and hint choices here are this project's own suggestions, shaped by its concrete-first guidance, not a lesson copied from that book.
\endgroup
'''

pre=pre.replace(r'\begin{document}',r'\begin{document}'+(ROOT/'mathematical-overview.tex').read_text()+r'\newpage',1)
out=[pre]
for idx,p in enumerate(P):
    if idx%2==0:
        out += [r'\newpage',f'{{\\Large\\bfseries {p["band"]} solutions}}\\par',r'\vspace{.08in}']
    else:out += [r'\vfill']
    out += [f'{{\\large\\bfseries Problem {p["num"]} {p["title"]}}}\\par',r'\vspace{3pt}',r'\noindent\begin{minipage}[t]{.58\textwidth}\vspace{0pt}',r'\fontsize{10.8}{13.2}\selectfont',r'\textbf{Solution.} '+p['answer']+'\n\n'+r'\textbf{Reasoning.} '+p['why']+'\n\n'+r'\textbf{Hint to hold.} '+p['hint']+'\n\n'+r'\textbf{Optional extension.} '+p['extend'],r'\end{minipage}\hfill\begin{minipage}[t]{.40\textwidth}\vspace{0pt}\centering',p['diagram'],r'\par\raggedright\fontsize{9}{11}\selectfont '+p['caption'],r'\end{minipage}']
    if idx%2==1:out += [r'\vspace{.15in}']
out += [r'\end{document}']
if __name__ == '__main__':
    (ROOT/'facilitator-guide.tex').write_text('\n'.join(out))
    print('Wrote 24 complete solutions and 24 answer diagrams.')
