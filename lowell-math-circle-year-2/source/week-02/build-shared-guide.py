#!/usr/bin/env python3
"""Build the Week 2 shared facilitator guide. Run from any directory."""
from pathlib import Path
import json
from collections import deque
from math import sin, cos, pi
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor, Color, white
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import Paragraph
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

ROOT = Path(__file__).resolve().parents[3]
DATA = json.loads((ROOT / "plans/week-02-shared-data.json").read_text())
OUT = ROOT / "lowell-math-circle-year-2/week-02/week-02-shared-facilitator.pdf"
FONTDIR = Path("/System/Library/Fonts/Supplemental")
for name, file in [("Guide", "Arial.ttf"), ("GuideBold", "Arial Bold.ttf"), ("GuideItalic", "Arial Italic.ttf")]:
    pdfmetrics.registerFont(TTFont(name, str(FONTDIR / file)))
pdfmetrics.registerFontFamily("Guide",normal="Guide",bold="GuideBold",italic="GuideItalic",boldItalic="GuideBold")
W,H=612,792
INK=HexColor("#1f2933"); TEAL=HexColor("#126269"); PALE=HexColor("#edf5f4"); MUTED=HexColor("#5a6570"); RULE=HexColor("#bac7c8")
STYLE=ParagraphStyle("body",fontName="Guide",fontSize=10.5,leading=14,textColor=INK,spaceAfter=0)
SMALL=ParagraphStyle("small",parent=STYLE,fontSize=9.2,leading=12)
TITLE=ParagraphStyle("title",parent=STYLE,fontName="GuideBold",fontSize=23,leading=27,textColor=TEAL)
SUB=ParagraphStyle("sub",parent=STYLE,fontName="GuideBold",fontSize=13,leading=16,textColor=TEAL)

OUT.parent.mkdir(parents=True,exist_ok=True)
c=canvas.Canvas(str(OUT),pagesize=(W,H))
c.setTitle("Week 2 / Lamp lab / Shared facilitator")
c.setAuthor("Bellingham Math Circle")
page=0

def para(text,x,y,width=516,style=STYLE):
    p=Paragraph(text,style); _,h=p.wrap(width,1000)
    assert y-h >= 53, (page, text[:80], y-h)
    p.drawOn(c,x,y-h); return y-h

def text(text,x,y,size=10.5,bold=False,color=INK):
    c.setFillColor(color); c.setFont("GuideBold" if bold else "Guide",size); c.drawString(x,y,text)

def section(title,body,y,x=48,width=516):
    y=para(title,x,y,width,SUB)-5
    return para(body,x,y,width)-14

def start(kicker,title,deck):
    global page
    if page:c.showPage()
    page+=1
    c.setFillColor(TEAL); c.rect(0,H-9,W,9,fill=1,stroke=0)
    text("WEEK 2  /  SHARED COLLECTION  /  ADULT GUIDE",48,757,9.2,True,TEAL)
    text(kicker,48,732,10,True,MUTED)
    y=para(title,48,711,516,TITLE)-11
    y=para(deck,48,y)-15
    c.setStrokeColor(RULE); c.setLineWidth(.6); c.line(48,43,564,43)
    text("Bellingham Math Circle / Week 2 / F02-S-FAC-v1",48,28,8,color=MUTED)
    c.setFillColor(MUTED); c.setFont("Guide",8); c.drawRightString(564,28,str(page))
    return y

def band(body,y,height=58):
    c.setFillColor(PALE); c.roundRect(48,y-height,516,height,8,stroke=0,fill=1)
    para(body,60,y-10,492)
    return y-height-16

def graph(name,x,y,w,h,on=()):
    """Numbered adult key; x,y are bottom left."""
    g=DATA['graphs'][name]; xs=[p[0] for p in g['xy']];ys=[p[1] for p in g['xy']]
    dx=max(xs)-min(xs) or 1;dy=max(ys)-min(ys) or 1
    scale=min((w-30)/dx,(h-30)/dy)
    pos=[(x+w/2+(a-(max(xs)+min(xs))/2)*scale,y+h/2+(b-(max(ys)+min(ys))/2)*scale) for a,b in g['xy']]
    c.setStrokeColor(INK);c.setLineWidth(1.4)
    for a,b in g['edges']:c.line(*pos[a-1],*pos[b-1])
    for i,(a,b) in enumerate(pos,1):
        c.setFillColor(TEAL if i in on else white);c.circle(a,b,10,stroke=1,fill=1)
        c.setFillColor(white if i in on else INK);c.setFont("GuideBold",9);c.drawCentredString(a,b-3.2,str(i))

def path_string(edges):return "; ".join(f"{a}-{b}" for a,b in edges)

def solve(problem,target):
    q=next(q for q in DATA['checks'] if q['problem']==problem)
    g=DATA['graphs'][q['graph']]; edges=g['edges']+q.get('extra_edges',[])
    s=sum(1<<(i-1) for i in q['start']);goal=sum(1<<(i-1) for i in target)
    paths={s:[]};todo=deque([s])
    while todo:
        state=todo.popleft()
        if state==goal:return paths[state]
        for a,b in edges:
            nxt=state^(1<<(a-1))^(1<<(b-1))
            if q.get('one_light') and nxt.bit_count()!=1:continue
            if nxt not in paths:paths[nxt]=paths[state]+[(a,b)];todo.append(nxt)
    return None

def solutions(problem):
    q=next(q for q in DATA['checks'] if q['problem']==problem)
    return "<br/>".join("ON "+", ".join(map(str,t))+": <b>"+path_string(solve(problem,t))+"</b>." for t in q['targets'])

def draw_poly(points,x,y,w,h,closed=True):
    c.setLineWidth(1.8);c.setStrokeColor(INK)
    p=c.beginPath();p.moveTo(x+w*points[0][0],y+h*points[0][1])
    for a,b in points[1:]:p.lineTo(x+w*a,y+h*b)
    if closed:p.close()
    c.drawPath(p,stroke=1,fill=0)

def clipped_polys(walls):
    polys=[[(0.,0.),(1.,0.),(1.,1.),(0.,1.)]]
    for (a,b) in walls:
        def sign(p):return (b[0]-a[0])*(p[1]-a[1])-(b[1]-a[1])*(p[0]-a[0])
        new=[]
        for poly in polys:
            for side in (1,-1):
                out=[]
                for p,q in zip(poly,poly[1:]+poly[:1]):
                    sp,sq=side*sign(p),side*sign(q)
                    if sp>=-1e-9:out.append(p)
                    if (sp>1e-9 and sq < -1e-9) or (sp < -1e-9 and sq>1e-9):
                        t=sp/(sp-sq);out.append((p[0]+t*(q[0]-p[0]),p[1]+t*(q[1]-p[1])))
                if len(out)>=3:
                    area=abs(sum(p[0]*q[1]-q[0]*p[1] for p,q in zip(out,out[1:]+out[:1])))/2
                    if area>1e-8:new.append(out)
        polys=new
    return polys

def mark(x,y,symbol):
    c.setStrokeColor(TEAL);c.setFillColor(TEAL);c.setLineWidth(1.5)
    if symbol==0:c.circle(x,y,3,stroke=0,fill=1)
    elif symbol==1:c.line(x-3,y-3,x+3,y+3);c.line(x-3,y+3,x+3,y-3)
    else:c.circle(x,y,4,stroke=1,fill=0)

def room(name,x,y,size=125,coloring=False,label=None):
    walls=DATA['room_maps'][name] if isinstance(name,str) else name
    c.setStrokeColor(INK);c.setLineWidth(1.6);c.rect(x,y,size,size,stroke=1,fill=0)
    for a,b in walls:c.line(x+a[0]*size,y+a[1]*size,x+b[0]*size,y+b[1]*size)
    if name=='tee':
        centers=[(.25,.75),(.75,.75),(.5,.25)]
        for i,(a,b) in enumerate(centers):mark(x+a*size,y+b*size,i if coloring else 0)
        count=3
    else:
        polygons=clipped_polys(walls);count=len(polygons)
        for poly in polygons:
            a=sum(p[0] for p in poly)/len(poly);b=sum(p[1] for p in poly)/len(poly)
            symbol=sum((q[0]-p[0])*(b-p[1])-(q[1]-p[1])*(a-p[0])>0 for p,q in walls)%2
            mark(x+a*size,y+b*size,symbol if coloring else 0)
    if label:text(label,x,y-18,10,True)
    return count


def rule_table(rows, y, widths=(120,396), head=True, padding=15):
    x0=48
    for n,row in enumerate(rows):
        heights=[]
        for val,w in zip(row,widths):
            p=Paragraph(str(val), SMALL); _,h=p.wrap(w-16,1000); heights.append(h)
        height=max(heights)+padding
        assert y-height>=53, (page,row,y-height)
        if n==0 and head:
            c.setFillColor(PALE); c.rect(x0,y-height,sum(widths),height,stroke=0,fill=1)
        c.setStrokeColor(RULE);c.setLineWidth(.5);c.line(x0,y-height,x0+sum(widths),y-height)
        x=x0
        for val,w in zip(row,widths):
            para(str(val),x+8,y-padding/2,w-16,SMALL);x+=w
        y-=height
    return y-15

def numbered_graph(labels, edges, pos, x,y,w,h,on=(), cut=None):
    xs=[p[0] for p in pos];ys=[p[1] for p in pos]
    scale=min((w-32)/(max(xs)-min(xs) or 1),(h-32)/(max(ys)-min(ys) or 1))
    locations={n:(x+w/2+(a-(min(xs)+max(xs))/2)*scale,y+h/2+(b-(min(ys)+max(ys))/2)*scale) for n,(a,b) in zip(labels,pos)}
    c.setStrokeColor(INK);c.setLineWidth(1.4)
    for a,b in edges:
        if cut and set((a,b))==set(cut):continue
        c.line(*locations[a],*locations[b])
    for n,(a,b) in locations.items():
        c.setFillColor(TEAL if n in on else white);c.circle(a,b,11,stroke=1,fill=1)
        c.setFillColor(white if n in on else INK);c.setFont('GuideBold',10);c.drawCentredString(a,b-3.4,str(n))

def ring(n,x,y,w,h,on=()):
    numbered_graph(list(range(1,n+1)),[(i,i%n+1) for i in range(1,n+1)],[(sin(2*pi*i/n),cos(2*pi*i/n)) for i in range(n)],x,y,w,h,on)

NET_LABELS=list('ABCDE')
NET_POS=[(0,.7),(-.65,-.4),(.65,-.4),(2.1,.3),(3.1,.3)]
NET_EDGES=[('A','B'),('B','C'),('A','C'),('D','E')]
TREE_LABELS=list('ABCDEF')
TREE_POS=[(-1.4,.6),(0,.6),(0,1.35),(0,-.3),(-1.4,-.3),(1.4,-.3)]
TREE_EDGES=[('A','B'),('B','C'),('B','D'),('D','E'),('D','F')]

# 1. A practical first page, shared by all three adults.
y=start('QUICKSTART / GIVE THIS PAGE TO EACH ADULT', 'One collection, many good routes', '42 student pages / 50 problems. Prepared September 28, 2026; unpiloted. Choose a few pages. Nobody is expected to work through the book in order.')
y=band('<b>Start together on student page 1.</b> After a child can make and undo a legal move, choose exploration (pp. 2-8), collecting pictures (pp. 9-16), or improving solutions (pp. 17-28). Drawing (pp. 29-34) is always available. Networks (pp. 35-42) are reserve investigations.',y,73)
y=section('Three stable tables; pages can travel', 'Ten children: KK1 / 3333 / 445. The non-mathematician parent initially anchors the three youngest children; the other mathematician anchors the four third graders; the organizer anchors the remaining three. This is a staffing arrangement, not a restriction on tasks. Keep seats and adults stable while offering suitable pages across the whole collection. There are no required station rotations.',y)
y=section('Materials and manageable printing', 'Pencils and erasers, or whiteboard tablets with markers and erasers; ordinary pens work for fresh drawings. Existing two-sided counters are optional. Print ten copies of student p. 1. Suggested reserve stacks: <b>parent:</b> three each of pp. 2, 3, 30, 31; <b>mathematician A:</b> four each of pp. 9-12 and 15; <b>mathematician B:</b> three each of pp. 17-21. These are available choices, not assigned piles. Copy reserve pages before the meeting. Keep one complete master collection to display or sketch from.',y)
y=section('What each adult needs', 'All three adults: this page and the page finder (guide p. 2). Parent: guide pp. <b>3-5 and 11-13</b> give scripts and answers for all exploration/drawing choices. Mathematicians: guide pp. 6-10 and 14-16 supply the remaining keys and proofs. All answer references use the shared student problem numbers.',y)
y=section('A flexible hour', '<b>0-5:</b> handle materials; draw and erase. <b>5-10:</b> demonstrate, then replay one legal move together. <b>10-30:</b> selected tasks, solo or shared. <b>30-35:</b> stand and stretch. <b>35-50:</b> continue, change difficulty, or draw rooms. <b>50-55:</b> show one discovery. <b>55-60:</b> tidy. End a route after a satisfying attempt; explanation and proof can be a conversation.',y)
y=section('When someone needs more help', 'Keep the child on a familiar board or drawing task while the adult helps a neighbor. If the parent needs mathematical support, the organizer first asks the other mathematician to cover the two older tables, then visits briefly. Never leave a group without agreed adult coverage. An older child may choose an easier drawing task; a younger child may tackle a deeper question orally.',y)

# 2. The complete page finder doubles as the readiness menu.
y=start('PAGE FINDER / STUDENT PAGE NUMBERS', 'Choose by the next useful action', 'Offer one or two choices within a table. A child can point or dictate while an adult records. Reading speed, handwriting, and number of finished pages do not decide access.')
rows=[['<b>Student pages / problems</b>','<b>What children do; useful entry knowledge</b>'],
 ['1-2 / P1-4','Make, undo, and share puzzles. Match a picture; change both endpoints. No independent reading or arithmetic needed.'],
 ['3-4 / P5-8','Walk one light around a ring or tree; compare starting with one ON versus all OFF. Follow connected roads.'],
 ['5-6 / P9-10','Match many targets on larger rings and a grid. Use a legal pair move reliably; count only if helpful.'],
 ['7-8 / P11-14','Try separated islands, draw a bridge, invent a board. A brief impossible attempt followed by a successful change.'],
 ['9-12 / P15-18','Record a move list; try pictured targets; inspect what one move does. Recognize labels 1-4; count to four or pair lamps.'],
 ['13-16 / P19-22','Compare attempts, follow paths, save different pictures, explain the collection. Sort pictures; notice repeated states.'],
 ['17-19 / P23-25','Try a five-ring, find different lists, cancel duplicate presses. Track a short list; count to five.'],
 ['20-22 / P26-27','Compare chosen roads with the roads left out. Tell a picture of selected roads from a picture of lit lamps.'],
 ['23-25 / P28-29','Make forced yes/no decisions; replay and compare results. Finish one lamp before attending to the next.'],
 ['26-28 / P30-32','Rule out a target; invent short solutions; compare a six-ring. Follow the two decision branches and discuss why.'],
 ['29-30 / P33-36','Draw closed shapes, then split a square with one wall. Trace boundaries; adult can draw or count corners.'],
 ['31-32 / P37-38','Try two walls; compare three-wall maps. Find each room and mark it once.'],
 ['33-34 / P39-42','Mark neighboring rooms, invent a town, make a shared town. Identify rooms sharing a piece of wall.'],
 ['35-38 / P43-46','Separate components, add a bridge, cancel shared path edges. Follow lettered routes; count targets within each piece.'],
 ['39-42 / P47-50','Invent components; solve a tree by cuts. Judge even/odd groups by pairing; track the two sides of a cut.']]
y=rule_table(rows,y,(137,379),padding=8)
y=para('<b>Useful jumps:</b> p. 1 → p. 3 for a child who wants movement; p. 1 → p. 9 for a collector; p. 1 → p. 17 for someone already making reliable lists. Keep pp. 15-16 together: P22 uses the saved collection from P21. Start drawing at p. 29 or 30 at any time. A mathematician can introduce p. 35 after component questions arise. P26 and P28 each occupy two pages.',48,y,516,SMALL)

# 3. Explicit launch and all common-entry answers.
y=start('STUDENT PP. 1-2 / P1-4', 'Make, change, undo', 'Idea: a legal move changes both ends of one road. Repeating the move undoes it. Before any explanation, let children change the lamps themselves.')
y=band('<b>Say:</b> “An empty lamp is OFF. A dot is ON. Choose a road. Change BOTH ends: add a dot where it was empty; erase a dot where it was ON. Leave the other lamps alone.” With counters: white is OFF and dark is ON. Use one method consistently at each board.',y,76)
graph('square',53,y-140,143,133)
y2=section('P1: demonstrate and undo', 'Begin all OFF. Use road 1-2, then use it again: both lamps return OFF. Next use 1-2 and then 2-3: one endpoint turns OFF and another turns ON. Ask a child to replay. Point to both ends before changing either. Finish the whole move before choosing another road.',y,x=223,width=341)
y=min(y-155,y2)
y=section('P2: three pictured targets', solutions(2)+'<br/>Reset all OFF between targets. These numbers belong to the adult key: 1 top, 2 right, 3 bottom, 4 left. “1-2; 2-3” means two roads in succession, not a list of lit lamps.',y)
y=section('P3: a one-move partner puzzle', 'The maker starts all OFF and makes one move while the partner watches. The partner undoes it; swap. A hint can simply point to the original road. Showing and replaying the move counts as a solution.',y)
y=section('P4: two moves, then three if wanted', 'The maker starts all OFF and makes two moves. The partner tries to return all OFF. Reversing the original moves always works; a shorter solution may also work. Two uses of the same road leave the already-solved picture: welcome that discovery. Try three moves only when the pair wants more.',y)
y=section('Trio roles and a clear stopping point', 'One child chooses the road; one changes one end; one changes the other. Rotate roles after each move. For partner tasks, the adult can partner with the third child. After two successful independent moves, offer a new page without requiring every target or a written list. If erasing is dominating, use the one-light walk (p. 3) or room drawing (p. 30).',y)

# 4. One-light comparisons.
y=start('STUDENT PP. 3-4 / P5-8', 'A light travels; a path leaves ends', 'Set up the starting picture by hand. This is different from reaching that picture through legal moves. The printed working boards are blank so children can erase every dot.')
graph('ring6',52,y-137,172,132);graph('tree8',275,y-137,280,132)
text('Six-ring: lamp 1 at the top',52,y-157,9.5,True);text('Tree: lamp 1 at the far left',277,y-157,9.5,True)
y-=180
y=section('P5: reach a destination with exactly one light', 'Start with only 1 ON. To reach 3: <b>1-2; 2-3</b>. To reach 4: <b>1-2; 2-3; 3-4</b>. Reset for each target. Going the other way also works. Choose a road touching the lit lamp; erase that dot and add one at the other end. A finger can trace the route before the child starts.',y)
y=section('P6: tour the ring', 'Use <b>1-2; 2-3; 3-4; 4-5; 5-6; 6-1</b>. The light visits every lamp and returns home. Detours are allowed; no move list is required. Ask a partner to choose a different destination or a direction.',y)
y=section('P7: choose a branch', 'Reset with only 1 ON before each trip.<br/>To 5: <b>1-2; 2-3; 3-4; 4-5</b>.<br/>To 7: <b>1-2; 2-3; 3-6; 6-7</b>.<br/>To 8: <b>1-2; 2-3; 3-6; 6-8</b>.<br/>Backtracking is legal. Stop after one destination if that was enough.',y)
y=section('P8: use the same route from a different start', '<b>Reset all OFF.</b> To leave 1 and 8 ON, use <b>1-2; 2-3; 3-6; 6-8</b>. The starting lamp stays ON while the other light travels. Middle lamps change twice and end OFF. Compare this with the last trip in P7. “Watch the lamps behind you” is a useful hint.',y)
y=band('<b>Optional depth:</b> Act out the same route with one light at its beginning, then with all lamps OFF. The difference is visible. Let the child explain by pointing; general parity language can wait.',y,59)

# 5. Larger graphs and creation.
y=start('STUDENT PP. 5-8 / P9-14', 'Bigger boards and invented puzzles', 'Use these pages when children want more lamps or room to invent. None is a gate to the collection, optimization, or drawing pages.')
graph('ring6',50,y-113,136,109);graph('grid9',230,y-113,134,109);graph('islands8',392,y-113,170,109)
y-=133
left=section('P9: ring targets',solutions(9),y,x=48,width=245)
right=section('P10: grid targets',solutions(10),y,x=319,width=245)
y=min(left,right)
y=section('Help without taking over', 'Reset all OFF for each picture. Suggest a route between two desired lamps. A path leaves only its endpoints ON; try another path for another pair. On the grid, the top row is 1, 2, 3; the middle is 4, 5, 6; the bottom is 7, 8, 9. Longer working lists are welcome. The lists above are examples, not answers children must copy.',y)
y=section('P11: a short island mystery', 'Start with only lamp 1 ON on the left; try to leave only lamp 5 ON on the right. It is impossible on the printed map. The light has no road between islands. Even allowing extra lights cannot fix this: each move changes two lamps on one island, so the left island cannot change its odd count to zero. Keep the unsuccessful search brief; move to P12 after a few useful attempts.',y)
y=section('P12: change the map', 'Draw bridge <b>2-5</b>. Reset with only 1 ON. Use <b>1-2; 2-5</b> to carry the light to 5. Other bridges also work with suitable routes. Ask what changed; completing the new route is enough.',y)
y=section('P13-14: make a board and share it', '<b>P13:</b> Draw 4-8 lamps connected by roads, with no crossings except at lamps. From all OFF make two moves, then let a partner undo the result. Reversing the moves always succeeds. <b>P14:</b> Add a lamp and a road connecting it to the old map; reset and make another puzzle. If a crossing is ambiguous, add a lamp there or redraw. An adult can draw while the child chooses.',y)

# 6. Accessible entry to collecting states.
y=start('STUDENT PP. 9-12 / P15-18', 'Pictures first; a record that helps', 'Idea: compare reachable and apparently troublesome pictures, then examine what one move can change. Readiness: follow labels 1-4 and count or pair up to four lamps.')
y=section('P15: introduce the move list through a replay', 'Start all OFF, use <b>1-2</b>, then <b>2-3</b>. The pictures are first {1,2} and then {1,3}. Show that “12, 23” records roads used, not the target lamps. Replay the two presses in reverse to return all OFF. For the child’s own list, accept any correctly recorded sequence that a partner can replay. The adult can write the numbers.',y)
graph('square',58,y-118,120,112,(1,2));graph('square',258,y-118,120,112,(1,3))
text('After road 1-2',59,y-137,10,True);text('Then road 2-3',260,y-137,10,True)
y-=160
y=section('P16: four successful targets', '<b>{1,2}:</b> 1-2. <b>{1,3}:</b> 1-2; 2-3.<br/><b>{2,4}:</b> 1-2; 1-4. <b>{1,2,3,4}:</b> 1-2; 3-4.<br/>Reset all OFF each time. Any working list counts. A longer list can expose undoing or a different route; do not demand a shortest solution yet.',y)
y=section('P17: two successes and two obstructions', 'Targets <b>{1}</b> and <b>{1,2,3}</b> cannot be reached from all OFF. Targets <b>{2,3}</b> and <b>{1,4}</b> use 2-3 and 1-4. “Not yet” accurately records that the child has not found a list; it is not a proof of impossibility. Mix these attempts with successful ones and stop a fruitless search before it becomes frustrating.',y)
y=section('P18: three local changes', 'Set up each printed start <b>by hand</b>, including the one-ON picture; setup need not be reachable from all OFF. Flip road 1-2 once. At its endpoints: <b>0 ON → 2 ON</b>, <b>2 ON → 0 ON</b>, or <b>1 ON → 1 ON</b>. Other lamps stay as they were. Children can point to the two affected lamps or pair the ON lamps instead of naming odd and even.',y)
y=band('<b>Decision to continue:</b> If children are curious why some targets resist every attempt, use pp. 13-16. If recording is tiring, return to a bigger board or partner puzzle; the mathematical exploration still counts.',y,57)

# 7. Complete state collection and proof.
y=start('STUDENT PP. 13-16 / P19-22', 'Eight pictures, and why these eight', 'The recording grid gives twelve spaces so the page does not reveal the answer. Save the all-OFF picture deliberately; a blank unused space is different.')
y=section('P19: revisit the eight target attempts', 'The pictured targets from P16-17 have ON counts <b>2, 2, 2, 4; 1, 2, 3, 2</b>. The six even targets can be made; the two odd targets cannot. Children mark their own progress and retry, rather than copying a finished classification. Ask them to compare the counts of pictures they made.',y)
y=section('P20: two routes leave two ends', '<b>1-2; 2-3; 3-4</b> leaves {1,4}. <b>1-4; 4-3</b> leaves {1,3}; 4-3 is the same road as 3-4. The middle lamps change twice; the two ends change once. Replay slowly and point to those lamps. This is a construction tool for the next page.',y)
y=section('P21: collect different pictures', 'Exactly eight pictures are reachable: none ON; any of the six pairs; all four ON. Check “saved” for each recorded picture, including all OFF. A different move list that gives the same picture is not a new state. Help compare drawings without making counting or handwriting a gate.',y)
for i,on in enumerate([(),(1,2),(1,3),(1,4),(2,3),(2,4),(3,4),(1,2,3,4)]):
    xx=48+(i%4)*133;yy=y-88-(i//4)*113
    graph('square',xx,yy,102,86,on)
    lab='all OFF' if not on else ', '.join(map(str,on))
    text(lab,xx+29,yy-12,9.5,True)
y-=236
y=section('P22: organize, then replay a construction', 'Counts are <b>0, 2, or 4</b>; the complete collection has eight pictures. A child can select any saved target and find a list for a partner to replay. For all OFF, no moves works; pressing one road twice also works. Invite the completeness question only after the collection has a purpose.',y)
y=para('<b>Why complete?</b> Every move changes the ON count by +2, -2, or 0, so an odd count cannot arise from zero. All six pairs are made by paths; all four by roads 1-2 and 3-4. This both rules out every missing state and constructs every listed state. Pairing lamps or acting out the cases is a valid child-level explanation.',48,y)

# 8. Five-ring constructions and complementary sets.
y=start('STUDENT PP. 17-21 / P23-26', 'Find two ways, then compare them', 'Children may start here after demonstrating the rule. Readiness: track short move lists, distinguish roads from lamps, and count presses. Writing can be shared with an adult.')
y=section('P23: a five-ring and undoing', 'Start all OFF. Press 1-2, then 1-2 again: return all OFF. Choose any two moves and undo them by reversing the order. Here and below road 5-1 is also written 51. Ring labels begin at the top and run clockwise.',y)
y=rule_table([['<b>P24 target</b>','<b>Two lists, with number of presses</b>'],['{1,2}','1-2 (1); or 2-3, 3-4, 4-5, 5-1 (4). Minimum 1.'],['{1,3}','1-2, 2-3 (2); or 5-1, 4-5, 3-4 (3). Minimum 2.'],['{1,2,3,4}','1-2, 3-4 (2); or 2-3, 4-5, 5-1 (3). Minimum 2.']],y)
y=section('P24: let the experiment precede the lower bound', 'Reset before each list. Two different lists can tie (for example, 12,23 and 23,12); accept “same,” then invite a shorter or longer alternative. The singleton-edge target needs at least one press because the start is different. One press lights adjacent lamps, so cannot make {1,3}; it lights only two lamps, so cannot make the four-lamp target. These facts prove the shown two-press solutions shortest.',y)
y=section('P25: order and repeated presses', 'Lists <b>12,23</b>, <b>23,12</b>, and <b>12,23,12,12</b> all leave {1,3}. Removing two copies of the same road preserves the result. Each lamp only cares whether it was changed an odd or even number of times. Let children test before offering this explanation.',y)
y=rule_table([['<b>P26 selected roads</b>','<b>Complement / common target / counts</b>'],['12','23,34,45,51 / {1,2} / 1 and 4'],['12,23','34,45,51 / {1,3} / 2 and 3'],['12,34','23,45,51 / {1,2,3,4} / 2 and 3'],['12,23,34','45,51 / {1,4} / 3 and 2']],y)
y=para('<b>P26 spans student pp. 20-21.</b> Thick roads mean “press once”; dashed roads mean “do not press.” These are not pictures of lit lamps. Reset before each half. Both complementary sets give the same target because pressing every ring road changes each lamp twice.',48,y)

# 9. Forced choices with fully checked decision rows.
y=start('STUDENT PP. 22-26 / P27-30', 'Finish one lamp at a time', 'The decision method investigates all reduced solutions: each road used zero or one times. Lists with repeated roads are infinite in number; pairs of repeats can be cancelled.')
y=section('P27: invent a complementary pair', 'Choose one to three roads on the left; mark exactly the omitted roads on the right. Use every chosen road once, starting all OFF for each trial. Both give the same target, and the counts add to five. A working example is left <b>12,34</b>, right <b>23,45,51</b>, target {1,2,3,4}.',y)
y=band('<b>Demonstrate the decision:</b> First fix whether 51 is used. Then decide 12 to leave lamp 1 matching its target. Decide 23 to finish lamp 2; then 34; then 45. Never revisit a finished lamp. Check lamp 5 last. Replay the completed list on the working board.',y,72)
y=rule_table([['<b>Problem / target</b>','<b>51</b>','<b>12</b>','<b>23</b>','<b>34</b>','<b>45</b>','<b>Check / count</b>'],['P28 / {1,3}','no','yes','yes','no','no','works / 2'],['P28 / {1,3}','yes','no','no','yes','yes','works / 3'],['P29 / {1,2,3,4}','no','yes','no','yes','no','works / 2'],['P29 / {1,2,3,4}','yes','no','yes','no','yes','works / 3'],['P30 / {1}','no','yes','yes','yes','yes','fails / 4'],['P30 / {1}','yes','no','no','no','no','fails / 1']],y,(150,43,43,43,43,43,151))
y=section('P28: carry both branches through', 'On student p. 23, do not use 51; the first forced decision is to use 12. On p. 24, first use 51; the next forced decision is not to use 12. Both branches reach the target. Count the initial 51 when it is used. The order of the final chosen roads does not affect the final picture.',y)
y=section('P29: make four lights', 'On student p. 25, the two lists are <b>12,34</b> and <b>51,23,45</b>, with lengths two and three. The shorter list is shortest: one press cannot light four lamps. Ask the child to circle the shorter trial after replaying both.',y)
y=section('P30: check the last lamp honestly', 'On student p. 26, both decision branches leave <b>{1,5}</b>, so lamp 5 is wrong. The two branches exhaust all reduced possibilities; cancelling repeats shows no longer list can evade that failure. Pair parity gives a second explanation: one ON cannot arise from all OFF. End with the reason for failure, rather than more random trials.',y)

# 10. Generalization and minimum arguments.
y=start('STUDENT PP. 27-28 / P31-32', 'How short can every solution be?', 'Reserve deeper questions for children who want to explain the patterns. A child may instead construct and compare examples without completing a general proof.')
y=section('P31: invent targets and compare complementary lists', 'Any new target with two or four ON lamps on the five-ring works. One sample set of three targets is:<br/><b>{1,4}:</b> 51,45 (2) or 12,23,34 (3).<br/><b>{2,5}:</b> 12,51 (2) or 23,34,45 (3).<br/><b>{2,3,4,5}:</b> 23,45 (2) or 12,34,51 (3).<br/>The second list must use every road omitted by the first; merely reordering the same roads does not test the complementary pattern.',y)
y=section('The five-ring has a two-press bound', 'Every reachable target has exactly two reduced solutions. Once 51 is fixed, successive lamps force the other four decisions, so there are at most two. Complementing any solution gives another one, because using every edge changes each lamp twice. Their sizes add to five: one is at most two. Cancelling pairs of repeated roads never makes a list longer, so the smaller reduced solution is globally shortest. No reachable target needs more than two presses.',y)
ring(6,50,y-132,157,125,(1,4));ring(6,267,y-132,157,125,(1,3))
text('P32: opposite lamps 1 and 4',51,y-151,9.5,True);text('P32: lamps 1 and 3',269,y-151,9.5,True)
y-=172
y=section('P32: six lamps change the comparison', '<b>{1,4}:</b> 12,23,34 or 61,56,45; both have three presses.<br/><b>{1,3}:</b> 12,23 or 61,56,45,34; lengths two and four.<br/>The same forced-choice argument gives exactly these two reduced solutions, so no shorter list exists. The two complementary reduced solutions can tie on a six-ring; they cannot tie on the five-ring. More generally a ring with n edges gives complementary lengths k and n-k.',y)
y=section('Prompts that preserve the discovery', '“What does using all the roads do?” “After deciding this road, is there any choice at the next lamp?” “Could a repeated road help make a shortest list?” Invite the child to demonstrate with a drawing or list. Keep the general argument as a discussion after enough examples, not a written requirement.',y)

# 11. Fresh drawing entry at any readiness.
y=start('STUDENT PP. 29-30 / P33-36', 'Closed shapes and one-wall houses', 'A change of theme with the same paper or tablets. No lamp prerequisite. Trace, compare, and invent; adults may draw or record for children.')
y=section('P33-34: corners on a dot grid', '<b>P33:</b> Join three non-collinear dots with three straight sides to make a triangle; make another. <b>P34:</b> Join four dots in a closed four-sided shape without crossed sides; make another. Squares and rectangles count. A four-corner shape may have a dent. Count direction changes while tracing, not every grid dot along a straight side.',y)
for points,label,x in [([(0,0),(1,0),(.33,1)],'3 corners',71),([(0,0),(1,0),(1,1),(0,1)],'4 corners',247),([(0,0),(1,0),(.33,.33),(0,1)],'4 corners, a dent',423)]:
    draw_poly(points,x,y-80,102,72);text(label,x-3,y-101,9.7,True)
y-=124
y=band('<b>Launch a house:</b> “Here is one room. Draw one straight wall from the outside edge to the outside edge. Put one dot inside every room.” Trace a room boundary together. The wall goes through the inside, has no gap, and does not follow the outside edge.',y,72)
y=section('P35: make four different one-wall houses', 'Every full wall makes <b>two rooms</b>. Vary its direction or endpoints. Different-looking examples are useful even when their underlying structure is the same. Dot each room before counting aloud. Neatness is not the mathematical problem; an adult can straighten a child’s chosen wall.',y)
y=section('P36: change the shapes of the rooms', 'A diagonal between opposite corners makes <b>two triangles</b>. A wall joining opposite sides away from corners makes <b>two four-corner rooms</b>. Children may make or find these examples. Optional follow-up: a wall cutting off one corner makes <b>a triangle and a five-corner room</b>. Trace each boundary and tap each corner.',y)
for walls,label,x in [([[[0,0],[1,1]]],'3 + 3 corners',65),([[[0,.45],[1,.45]]],'4 + 4 corners',244),([[[0,.6],[.6,1]]],'3 + 5 corners',423)]:
    room(walls,x,y-95,95,label=label)

# 12. Two/three-wall counts including non-maximal examples.
y=start('STUDENT PP. 31-32 / P37-38', 'Room counts worth comparing', 'Each picture needs its own concrete counting action: one dot in each room, then touch each dot. The adult can supply a number after the child finds the rooms.')
y=section('P37: two distinct full walls', 'Try four drawings. Two walls make <b>three rooms</b> if they do not cross inside the square, or <b>four rooms</b> if they do. Meeting only on the boundary is not an interior crossing. Tracing an old wall does not add a new wall. Ask for a different room count only after the child has counted a picture successfully.',y)
room([[[0,.33],[1,.33]],[[0,.67],[1,.67]]],95,y-94,93,label='3 rooms: no crossing')
room('cross',370,y-94,93,label='4 rooms: one crossing')
y-=132
y=section('P38: count three printed towns, then invent', 'The printed maps have <b>4, 6, and 7 rooms</b>, in that order. In the middle, all three walls meet at the same point. The last has three distinct crossings and a central triangular room; mark that room too. For the blank town, any three distinct full walls are valid. No maximum or complete list is required.',y)
for name,label,x in [('parallel3','4 rooms',61),('concurrent3','6 rooms',241),('general3','7 rooms',421)]:
    assert room(name,x,y-103,103,label=label)==int(label[0])
y-=144
room('five3',54,y-110,110,label='Optional: 5 rooms')
y2=section('If someone asks for a missing number', 'Three full walls can also make <b>five rooms</b>: the example crosses the slanted wall with only the upper horizontal wall. Three distinct full walls can therefore make 4, 5, 6, or 7 rooms.',y,x=206,width=358)
y2=para('Follow a new wall from edge to edge. Each piece between distinct interior crossing points cuts an old room in two. With three walls there can be at most 1 + 1 + 2 + 3 = 7 rooms. A repeated crossing point counts once along the new wall.',206,y2,358)

# 13. Room marking and shared construction.
y=start('STUDENT PP. 33-34 / P39-42', 'Neighbors and a town to share', 'Offer room marking once children can find the rooms. These are choices for any table; a shared whiteboard town is also a good regrouping activity.')
y=section('P39: a dot or an X in every room', 'Rooms sharing a piece of wall must have different marks. Touching only at a corner is allowed. These are valid two-mark solutions for the three printed maps. Swapping every dot and X gives another. Demonstrate one neighboring pair first.',y)
for name,x in [('stripes',66),('cross',246),('general3',426)]:room(name,x,y-108,108,coloring=True)
y-=139
room('tee',55,y-117,117,coloring=True,label='Three mutual neighbors')
y2=section('P40: a T-shaped surprise', 'This map has a wall that stops at another wall. Every room touches both of the others along a wall. If the top rooms are dot and X, neither mark works below. <b>Two marks cannot work; adding a circle works.</b> Keep the attempt short, then let the child finish with a third symbol.',y,x=204,width=360)
y=min(y-154,y2)
y=section('P41: invent a partner’s town', 'Draw one, two, or three distinct full straight walls. A partner dots and counts the rooms, then the children swap. Counts can range from two through seven. Trace questionable boundaries together. Dot/X marking can be an extra oral invitation after counting; it is not needed to finish this task.',y)
y=section('P42: a giant shared town', 'Draw one large square on paper or a whiteboard. Take <b>three turns</b>, adding one new full wall per turn, then stop. Do not trace an old wall or steer toward a maximum. With more than three children, share drawing and marking roles. Each child can dot an undotted room; count together. Optional next round: try dot/X marks.',y)
y=para('<b>Why two marks work for full walls:</b> Choose one side of each wall. Give each room a dot or X according to whether it lies on an even or odd number of chosen sides. Crossing a wall changes exactly one side choice, so adjacent rooms differ. The T has an interior endpoint and three mutually adjacent rooms, so this argument does not apply.',48,y,516,SMALL)

# 14. Components and shared paths.
y=start('STUDENT PP. 35-38 / P43-46', 'When the map falls into pieces', 'Reserve route: compare connected pieces before introducing tree cuts. Children should track lettered roads and count or pair targets within a component.')
numbered_graph(NET_LABELS,NET_EDGES,NET_POS,59,y-106,485,99)
y-=122
y=rule_table([['<b>P43 ON target</b>','<b>Sample moves / outcome</b>'],['{A,C}','AC'],['{D,E}','DE'],['{A,D}','Impossible: one target in each component.'],['{A,C,D,E}','AC; DE'],['{A,B,C,D}','Impossible: three in the triangle, one in the edge.'],['{A,B,D,E}','AB; DE']],y,padding=8)
y=section('P44: count inside each piece', 'For the first six targets in order, counts in triangle ABC / edge DE are <b>2/0, 0/2, 1/1, 2/2, 3/1, 2/2</b>. The added all-OFF target has <b>0/0</b> (no presses); {B,C} has <b>2/0</b> (press BC). Exactly the rows with an even count in each component work. Two targets in total are not enough: {A,D} separates them into different components. Let the child point to the unmatched target in each piece.',y)
y=section('P45: add the bridge CD', 'Now {A,D} uses <b>AC; CD</b>. Target {A,B,C,D} uses <b>AB; CD</b>. Both previously failed. Adding the bridge makes one component, so every even target is reachable. Reset all OFF for each target.',y)
y=section('P46: overlapping paths cancel', 'The paths A-C-D and B-C-D give <b>AC; CD; BC; CD</b>. The repeated CD can be removed twice, leaving <b>AC; BC</b>. Both lists light exactly A and B. Count a shared road twice before cancelling; taking the ordinary union of path edges would leave the wrong endpoints.',y)
y=para('<b>Complete component rule:</b> Starting all OFF, each move changes two lamps in a single component, preserving evenness there. Conversely, pair target lamps within each component and use a path for each pair. Interior lamps cancel and the paired endpoints remain. Shared path edges can be pressed twice or cancelled. Isolated lamps are components too and cannot be turned ON.',48,y)

# 15. Invention and exact tree key.
y=start('STUDENT PP. 39-42 / P47-50', 'Road choices on a tree', 'P47 offers invention before the tree investigation. Cut reasoning is an optional deeper conversation; give it enough time after successful component examples.')
y=section('P47: invent two components', 'Draw two separate connected pieces, each with at least three lamps. A possible target has an even number in each piece; one example selects two lamps in each. An impossible target can select one lamp in each: even overall, but odd in both pieces. Pair and connect desired lamps by paths to verify the possible example. Preserve the child’s invented map for later use.',y)
numbered_graph(TREE_LABELS,TREE_EDGES,TREE_POS,78,y-136,432,130,on=('A','C','E','F'))
y-=146
y=section('P48: two targets on this tree', '<b>{A,C}:</b> AB; BC. <b>{A,C,E,F}:</b> AB; BC; DE; DF.<br/>The picture above shows the second target. Both lists leave B and D OFF. Repeated moves may yield longer lists, but after cancelling pairs there is exactly one solution on a tree.',y)
y=rule_table([['<b>P49 road removed</b>','<b>Named side</b>','<b>Targets there</b>','<b>Use this road?</b>'],['AB','A','1','yes'],['BC','C','1','yes'],['BD','A,B,C','2','no'],['DE','E','1','yes'],['DF','F','1','yes']],y,(126,133,128,129),padding=8)
y=section('P50: predict a new even target', 'For any new even target, remove each road mentally and count target lamps on one side. Use the road exactly when that count is odd. For example, target <b>{A,E}</b> needs <b>AB; BD; DE</b>. Target <b>{B,D}</b> needs only <b>BD</b>. Replay to check the prediction. Either side of a cut gives the same odd/even answer when the whole target is even.',y)
y=para('<b>Why unique and shortest:</b> In a tree, the removed road is the only road across that cut. Moves within one side change two lamps there; only the cut road changes its parity. Its use is therefore forced by the target count. This determines every road. Path pairing guarantees a solution exists. Each required road must appear an odd number of times in any list, so using each required road once is shortest.',48,y,516,SMALL)

# 16. Grounding and follow-through.
y=start('SOURCES / MATHEMATICAL DEPTH / AFTER THE MEETING', 'Keep the evidence and the next questions', 'This shared edition is a response to the organizer’s printed-page feedback and approval of a shared collection. Its success in this classroom has not yet been observed.')
y=section('Source findings that informed the design', '<b><i>Math Circle by the Bay</i>, preface, pp. viii-x; especially p. x:</b> the authors describe using the same material across ages at different pace and depth, with younger groups sometimes proceeding equally quickly. The shared collection is our adaptation; the book does not establish this staffing plan.<br/><b>Natasha Rozhkovskaya, <i>Math Circles for Elementary School Students</i>, Lesson 3, “At the lesson,” item 1:</b> children tried and explained before a table was introduced; reserve problems served a mixed-experience group. <b>Lesson 7, items 1-2:</b> missed legal moves affected a game investigation; open polygon construction was engaging. Drawing polygons instead of using K’nex is our adaptation. <b>Lesson 8, item 2:</b> writing and coloring pace split the class. Our adult scribing and readiness-based page choices respond to that report.',y)
y=section('Local continuity, with a limit on the claim', 'The project README and Week 1 classroom review record the need for concrete attempts, time with materials, and explicit next actions. Lowell year-1 <b>Handout 11, Problem 11.3</b>, has invented shapes split and recombined for a partner; <b>Handout 9, Problem 9.1</b>, toggles doors. The pair-road rule, component test, and optimization here ask different questions. A handout’s presence in the collection does not show which children encountered it.',y)
y=section('Further mathematical connections', 'Toggling adds by symmetric difference: using something twice cancels. Edge subsets with prescribed odd-degree vertices are T-joins. The cycle and tree arguments in this guide prove our instances directly; they do not claim to prove the general matching algorithm. Adult references: Edmonds and Johnson, <i>Matching, Euler tours and the Chinese postman</i> (1973), <link href="https://doi.org/10.1007/BF01580113" color="#126269">doi:10.1007/BF01580113</link>; Cornuéjols, <i>Combinatorial Optimization: Packing and Covering</i>, Chapter 2, pp. 27-29. For matrix context, MIT 18.06SC, “Graphs, Networks, Incidence Matrices”; the binary adaptation used here is ours.',y)
y=section('Record actual use, not the whole available collection', 'Log the date, shared edition ID, exact problem numbers and targets tried, and invented maps worth keeping. Note whether children made a legal move unaided, replayed a record, found every room, explained a failure, or asked to repeat something. Separate observations (“erasing took most of the turn”) from interpretations (“the recording method may be too slow”). Mark conclusions as tried, conjectured, checked in cases, proved, or supplied.',y)
y=section('Returning children and the next revision', 'Keep unused pages for later. Revisit the theme with a different graph, question, representation, or proof depth; do not simply reissue every target. Preserve drawings and memorable explanations. Expand a useful idea that needed more attempts; simplify a record that needed repeated adult rescue. Finishing fewer pages while making and explaining a discovery is a successful outcome.',y)

assert page==16,page
c.save()
print(f'Built {OUT} ({page} pages)')
