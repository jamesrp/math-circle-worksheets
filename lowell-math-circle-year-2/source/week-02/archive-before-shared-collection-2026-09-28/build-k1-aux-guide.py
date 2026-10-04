#!/usr/bin/env python3
"""Build the Week 2 K-1 auxiliary parent guide. Run from any directory."""
from pathlib import Path
import json
from collections import deque
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor, Color, white
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import Paragraph
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

ROOT = Path(__file__).resolve().parents[4]
DATA = json.loads((ROOT / "plans/week-02-k1-aux-data.json").read_text())
OUT = ROOT / "lowell-math-circle-year-2/week-02/archive-before-shared-collection-2026-09-28/week-02-k-1-aux-facilitator.pdf"
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
c.setTitle("Week 2 / Lamps and room towns / K-1 auxiliary facilitator")
c.setAuthor("Bellingham Math Circle")
page=0

def para(text,x,y,width=516,style=STYLE):
    p=Paragraph(text,style); _,h=p.wrap(width,1000); p.drawOn(c,x,y-h); return y-h

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
    text("WEEK 2  /  K-1 AUXILIARY  /  PARENT GUIDE",48,757,9.2,True,TEAL)
    text(kicker,48,732,10,True,MUTED)
    y=para(title,48,711,516,TITLE)-11
    y=para(deck,48,y)-15
    c.setStrokeColor(RULE); c.setLineWidth(.6); c.line(48,43,564,43)
    text("Bellingham Math Circle / Week 2 / F02-K-AUX-FAC-v1",48,28,8,color=MUTED)
    c.setFillColor(MUTED); c.setFont("Guide",8); c.drawRightString(564,28,str(page))
    return y

def band(body,y,height=58):
    c.setFillColor(PALE); c.roundRect(48,y-height,516,height,8,stroke=0,fill=1)
    para(body,60,y-10,492)
    return y-height-16

def graph(name,x,y,w,h):
    """Numbered adult key; x,y are bottom left."""
    g=DATA['graphs'][name]; xs=[p[0] for p in g['xy']];ys=[p[1] for p in g['xy']]
    dx=max(xs)-min(xs) or 1;dy=max(ys)-min(ys) or 1
    scale=min((w-30)/dx,(h-30)/dy)
    pos=[(x+w/2+(a-(max(xs)+min(xs))/2)*scale,y+h/2+(b-(max(ys)+min(ys))/2)*scale) for a,b in g['xy']]
    c.setStrokeColor(INK);c.setLineWidth(1.4)
    for a,b in g['edges']:c.line(*pos[a-1],*pos[b-1])
    for i,(a,b) in enumerate(pos,1):
        c.setFillColor(white);c.circle(a,b,10,stroke=1,fill=1)
        c.setFillColor(INK);c.setFont("GuideBold",9);c.drawCentredString(a,b-3.2,str(i))

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

# 1. One-page operational brief.
y=start("START HERE", "A lively hour, with choices", "Ten children: KK1 / 3333 / 445. Three adults. This packet is a menu of 24 tasks, not an assignment to finish.")
y=band("<b>Default K-1 route:</b> student pages <b>1, 2, 3, then 10 and/or 11</b>. Switch to drawing sooner if repeated lamp moves stop being fun. Page 9 is the gentler drawing entry.",y,62)
y=section("Keep one adult with each group", "The parent stays with the three K-1 children; the other mathematician anchors the four third graders; the organizer anchors grades 4, 4, 5. For help, the parent keeps K-1 on a familiar task. The organizer first asks the other mathematician to cover both older groups, visits K-1 briefly, then returns. No group is left without adult coverage.",y)
y=section("Bring and print", "Pencil and eraser, or whiteboard tablets with dry-erase markers and erasers. Lamp tasks need erasable marks. Pens work for fresh drawings. Print three copies each of pages 1, 2, 3, 10, 11 (15 student sheets); keep one master of the other pages. Use tablets instead where convenient. Optional existing counters are fine; no new accessories are needed.",y)
y=section("Prerequisites and access", "No independent reading or written arithmetic. Children point, match pictures, follow a road, and draw or erase a dot. Count corners and small groups of rooms by touching or marking them; the adult can count aloud. If drawing is tiring, a child dictates and the adult draws. The child still chooses the move or wall.",y)
y=section("A flexible 60-minute route", "<b>0-5:</b> handle tablets or pencils; draw and erase freely. <b>5-10:</b> shared lamp demonstration. <b>10-20:</b> square targets and partner puzzles (pp. 1-2). <b>20-30:</b> move one light (p. 3), or switch earlier. <b>30-35:</b> movement break. <b>35-50:</b> one-wall houses and two-wall rooms (pp. 10-11). <b>50-55:</b> each child shows one discovery. <b>55-60:</b> tidy. Choose extra pages only when they serve a child's interest.",y)
y=section("A clean stop is part of the plan", "A successful move, a puzzle shared with a friend, and two different room pictures are enough. Do not make progress depend on finishing a page, writing numbers, proving an impossibility, or finding the most rooms.",y)

# 2. Parent-facing launch and first tasks.
y=start("STUDENT PAGES 1-2 / PROBLEMS 1-4", "Make, change, undo", "Mathematical idea: a move changes two endpoints; doing the same move twice undoes it. A child can create a solvable puzzle for someone else.")
y=band("<b>Whole-group script:</b> “A dot means ON. An empty lamp is OFF. Choose a road. Change BOTH lamps at its ends: erase a dot, or add one. Leave the other lamps alone.” Demonstrate OFF/OFF, then ON/OFF. Let children predict and help change the ends.",y,76)
graph('square',48,y-138,150,128)
y2=section("Problem 1: repeat a move", "Start with every lamp empty. Choose a road and add its two dots. Use that road again and erase both dots. Try a different road. Say, “We came back!” No formal explanation is required.",y,x=221,width=343)
y2=section("Problem 2: match three pictures", solutions(2)+"<br/>The little numbered diagram is an <b>adult key</b>. “1-2” means use the road from lamp 1 to lamp 2; semicolons mean successive moves. Reset to all OFF for each target.",y2,x=221,width=343)
y=min(y-155,y2)
y=section("Problem 3: one-move partner puzzles", "The maker starts all OFF and makes one legal move while the partner watches. The partner returns to all OFF. Swap. The maker can show the original road as a hint. The puzzle has a solution even if the maker forgets it: using the same road again undoes it.",y)
y=section("Problem 4: two, then three moves", "The maker makes two moves, then the solver tries to undo the picture. Reverse the maker's moves for a guaranteed solution; fewer moves may also work. Two uses of the same road produce the already-solved all-OFF picture: accept it as a discovery. Offer three moves only if the children ask for more.",y)
y=section("Make a trio work", "For shared turns, one child <b>chooses the road</b>, one <b>changes one end</b>, and one <b>changes the other end</b>. Rotate all three roles after every move. For partner puzzles, the parent partners with the third child, or all three use these roles. Nobody has a standing spectator or checker job.",y)
y=section("If the rule is getting lost", "Point to both ends first. Change one end, then the other: “move finished.” If the picture is muddled, reset without blame and make one move together. If erasing takes over, switch to a one-light walk or drawing.",y)

# 3. Routing and pair endpoints.
y=start("STUDENT PAGES 3-4 / PROBLEMS 5-8", "Walk a light around", "These walks begin with ONE lamp ON. Add an erasable dot to the blank board to set it up; setting up a puzzle is different from taking a legal move.")
graph('ring6',54,y-149,170,145)
graph('tree8',279,y-149,275,145)
text("Ring key",102,y-168,10,True);text("Branching key",366,y-168,10,True)
y-=190
y=section("Problems 5-6: travel, then take a tour", "<b>P5:</b> Start at lamp 1. For destination 3: use <b>1-2; 2-3</b>. For destination 4: <b>1-2; 2-3; 3-4</b>. The other way around also works. Keep one lamp ON by choosing a road touching the lit lamp: erase its dot and add one at the other end.<br/><b>P6:</b> A complete tour is <b>1-2; 2-3; 3-4; 4-5; 5-6; 6-1</b>. It visits every lamp and returns to the starting picture. A finger can trace the route; recording a move list is unnecessary.",y)
y=section("Problem 7: a light on a branching map", "Reset with only lamp 1 ON before each trip.<br/>To 5: <b>1-2; 2-3; 3-4; 4-5</b>.<br/>To 7: <b>1-2; 2-3; 3-6; 6-7</b>.<br/>To 8: <b>1-2; 2-3; 3-6; 6-8</b>.<br/>Hint: “Point along the road you want the light to take.” Detours and backtracking are legal. A child may stop after one successful destination.",y)
y=section("Problem 8: leave only the two ends lit", "<b>Now reset to all OFF.</b> Make lamps 1 and 8 ON using <b>1-2; 2-3; 3-6; 6-8</b>. The starting lamp stays ON; the other light travels to lamp 8. Each middle lamp changes twice and ends OFF. Hint: “Try the route you just used. Watch the lamps behind you.”",y)
y=band("<b>Optional conversation:</b> “What changed when we began with every lamp OFF instead?” Acting out the two starts on the same route is sufficient mathematical evidence. Do not ask for a general rule before the child has compared examples.",y,61)

# 4. Breadth, optional disconnectedness, invention.
y=start("STUDENT PAGES 5-8 / PROBLEMS 9-14", "Bigger boards and inventions", "Offer one board at a time to children who want more lamps. These are optional alternatives, not steps every K-1 child must climb.")
graph('ring6',50,y-126,136,122);graph('grid9',230,y-126,134,122);graph('islands8',394,y-126,168,122)
y-=146
left=section("Problem 9: four ring targets", solutions(9)+"<br/>Reset all OFF for every target. Other solutions can work.",y,x=48,width=245)
right=section("Problem 10: four grid targets",solutions(10)+"<br/>Reset all OFF each time. Try routes between desired pairs.",y,x=319,width=245)
y=min(left,right)
y=section("Problem 11: the light cannot jump islands", "Add an erasable dot to lamp 1 on the left island. The target has only lamp 5 ON on the right. It cannot happen using the printed roads. Keep this a <b>brief adult-led mystery</b>, after successful examples. Hint: “Where could the light go next?” Even allowing extra lights cannot work: each move changes two lamps on one island, so the odd number on the left cannot become zero.",y)
y=section("Problem 12: draw the missing connection", "Add road <b>2-5</b>. Reset with only lamp 1 ON, then use <b>1-2; 2-5</b>. This carries the single light to lamp 5. Other bridges work with suitable routes. Changing the map changes the answer. End without requiring a proof of P11.",y)
y=section("Problems 13-14: make a switchboard", "<b>P13:</b> Draw 4-8 lamps in one connected map. Roads do not cross except at lamps. Start all OFF, take two moves, and ask a partner to undo them. Reversing the two moves always works.<br/><b>P14:</b> Add a lamp connected to the old map; reset all OFF and make a new two-move puzzle. If roads cross ambiguously, add a lamp at the crossing or redraw. The adult can draw while the child directs.",y)
y=band("<b>Keep it playful:</b> “Make a puzzle I can solve.” Use a smaller map again whenever remembering to change both ends becomes the hard part.",y,48)

# 5. Closed shapes and one cut.
y=start("STUDENT PAGES 9-10 / PROBLEMS 15-18", "Draw shapes; build room towns", "A fresh theme using the same pencils or tablets. Mathematical idea: a closed outline and a new wall create regions that children can trace, compare, and count.")
y=section("Problems 15-16: corners on a dot grid", "<b>P15:</b> Join three dots with three straight sides to make a closed triangle; make another. Three dots on one straight line do not enclose a shape. <b>P16:</b> Join four dots with four sides, closing the shape without crossed sides; make another. Squares and rectangles count. If ready, show that a four-corner shape can have a dent. Count direction changes while tracing, not every grid dot on an edge.",y)
shapes=[([(0,0),(1,0),(.33,1)],"3 corners"), ([(0,0),(1,0),(1,1),(0,1)],"4 corners"), ([(0,0),(1,0),(.33,.33),(0,1)],"4 corners, a dent")]
for (points,label),x in zip(shapes,[71,247,423]):
    draw_poly(points,x,y-80,102,72);text(label,x-3,y-101,9.7,True)
y-=124
y=section("Launch the room task with one mark", "Point inside an empty square: “This is one room. Draw one straight wall from the outside edge to the outside edge. Put one dot inside each room.” Model tracing a room's boundary with a finger. The wall crosses the inside, does not run along the outside edge, and has no gap. Aim for a straight stroke; fine-motor neatness is not the problem.",y)
y=section("Problem 17: four different one-wall houses", "Every valid full wall makes <b>two rooms</b>. Try different endpoints, directions, and sizes. Two copies need not be mathematically inequivalent to count as useful experiments; ask what looks different. Put one dot in each room before counting aloud.",y)
y=section("Problem 18: change the shapes of the rooms", "Make or find these: a corner-to-opposite-corner diagonal makes <b>two triangles</b>; a wall between opposite sides, away from corners, makes <b>two four-corner rooms</b>. Optional adult invitation: cutting across one corner makes <b>a triangle and a five-corner room</b>. Trace each room and tap every corner, including original square corners.",y)
for walls,label,x in [([[[0,0],[1,1]]],"3 + 3 corners",65),([[[0,.45],[1,.45]]],"4 + 4 corners",244),([[[0,.6],[.6,1]]],"3 + 5 corners",423)]:
    room(walls,x,y-95,95,label=label)

# 6. Two and three cuts.
y=start("STUDENT PAGES 11-12 / PROBLEMS 19-20", "How many rooms appear?", "Give each drawing its own counting action: one dot in each room, then touch each dot. Numbers are optional; the adult can record them.")
y=section("Problem 19: two full walls", "Try four different drawings. Two distinct walls make <b>3 rooms</b> when they do not meet inside the square, or <b>4 rooms</b> when they cross inside. Meeting only on the outside boundary does not make an interior crossing. If two strokes follow the same wall, they count as one wall: invite a genuinely new wall. Ask, “Can you make a picture with a different number of rooms?”",y)
room([[[0,.33],[1,.33]],[[0,.67],[1,.67]]],95,y-94,93,label="3 rooms: no crossing")
room('cross',370,y-94,93,label="4 rooms: one crossing")
y-=132
y=section("Problem 20: three printed towns, then your own", "The three printed examples have <b>4, 6, and 7 rooms</b>, in that order. The middle picture's three walls all meet at one point. The last has three separate crossings and a small central triangle: mark that room too. A child may copy or vary any example for the blank town. No maximum or exhaustive list is required.",y)
for name,label,x in [('parallel3','4 rooms',61),('concurrent3','6 rooms',241),('general3','7 rooms',421)]:
    assert room(name,x,y-103,103,label=label)==int(label[0])
y-=144
room('five3',54,y-110,110,label="Optional: 5 rooms")
y2=section("If someone wants the missing count", "Three full walls can also make <b>5 rooms</b>. Draw two horizontal walls, then a slanted wall crossing only the upper one, as shown. Offer it as a new picture to inspect, not an obligation to find every case.",y,x=206,width=358)
y2=para("Follow the new wall with a finger: each piece between crossings splits one old room into two. A crossing at the same point is counted once.",206,y2,358)

# 7. Coloring and collaboration.
y=start("STUDENT PAGES 13-14 / PROBLEMS 21-24", "Neighbors and a shared town", "These pages are reserve material. Offer room marking after children can reliably find the rooms, not as another rule during the first drawing attempt.")
y=section("Problem 21: two kinds of room", "Use <b>a dot or an X</b> in every room. Rooms sharing a piece of wall must have different marks; touching only at a corner is allowed. The three maps below have valid two-mark solutions. Swapping every dot and X gives another. Show one adjacent pair before inviting the child to continue.",y)
for name,x in [('stripes',66),('cross',246),('general3',426)]:room(name,x,y-108,108,coloring=True)
y-=139
room('tee',55,y-117,117,coloring=True,label="Three neighboring rooms")
y2=section("Problem 22: a T-shaped surprise", "This special map includes a wall that stops at another wall. Its three rooms each share a wall with both others. If the top two are dot and X, the bottom can use neither. <b>Two marks cannot work; adding a circle works</b>, as shown. Keep the attempt short. The satisfying action is introducing a third mark and finishing the picture.",y,x=204,width=360)
y2=section("If the conflict is hard to see", "Point to the two top rooms: “These need different marks.” Then trace the bottom room's wall with each of them: “It touches this one and this one.” Do not keep asking a child to search for a two-mark solution after they have found the conflict.",y2,x=204,width=360)
y=min(y-157,y2)
y=section("Problem 23: invent a town for a partner", "Draw one, two, or three distinct full straight walls. Give the town to a partner to dot and count every room; then swap. The maker checks by tracing the rooms together with the partner. Counts can range from 2 through 7. Counting is enough; dot/X marking is an optional adult invitation after finding every room.",y)
y=section("Problem 24: one giant shared town", "The adult draws a large square. Each child adds one full wall in turn, choosing where; do not trace an old wall or steer the children into an optimal picture. Share the dotting: one child dots a room, the next finds a different undotted room, and so on. Count together. Offer dot/X marking only if there is time and interest.",y)

# 8. Adult depth, provenance, observations.
y=start("BACKGROUND / FOLLOW-UP", "What to notice and carry forward", "Prepared September 28, 2026. These are new, unpiloted activities. The worksheet supply is deliberately larger than the expected one-session use.")
y=section("Mathematics behind the lamp play", "A move toggles both endpoints. Repeating it undoes it; reversing a sequence undoes that sequence. Along a route, internal lamps change twice and endpoints once. In a connected graph, any even-size set of ON lamps can be made from all OFF: pair the desired lamps and use routes between the pairs. On separate islands, each island retains its own odd/even status. Children can encounter these facts through undoing, walking, and comparing pictures without naming an invariant.",y)
y=section("Mathematics behind the room play", "Three distinct full straight walls can create 4, 5, 6, or 7 rooms. Each new wall adds one room for every interior piece between crossings; hence at most 1 + 1 + 2 + 3 = 7 rooms with three walls. Any full-line arrangement admits dot/X marking: choose a side of each wall and mark a room by whether it lies on an odd or even number of chosen sides. Crossing a wall changes that count by one. The T map creates three mutually neighboring rooms and needs three marks.",y)
y=section("Sources: findings and adaptations", "<b>Natasha Rozhkovskaya, <i>Math Circles for Elementary School Students</i>, Lesson 7, “At the lesson,” item 2:</b> the author reports sustained engagement in making many polygons with K'nex, including a very large rectangle. The freedom to invent and compare shapes informs Problems 15-16; drawing in place of construction is our adaptation, not a result established by that account.<br/><b>Lesson 8, “At the lesson,” item 2:</b> number writing and different coloring speeds split the group's pace. Our use of dots, pointing, adult recording, and a small selected route is a design response to that report.<br/><b>Local evidence:</b> the organizer's prior-year experience, summarized in the project README, emphasizes concrete action and time to learn by doing. The September Week 1 classroom review supplies the requirement for more concrete examples and explicit next actions. These observations do not establish that the new Week 2 pages will succeed; record what happens.",y)
y=section("After the meeting: record actual use", "In the use log, record <b>only pages and problem instances actually tried</b>, including starting pictures, invented boards, or room maps. Separate observation (“erasing took most of the turn”) from interpretation (“the recording method may be too slow”). Note which child could make a legal move unaided, what they wanted to repeat, where an adult had to rescue a task, and a drawing or phrase worth revisiting. Keep unused pages available for later sessions.",y)
y=section("Returning children", "Related future work: routes and connectedness, undoing operations, pairing lamps, polygons with unusual shapes, and region coloring. Next time, vary the representation or question instead of simply reissuing the same targets. Revisit successful inventions at greater depth when children are ready.",y)

c.save()
print(f"Built {OUT} ({page} pages)")
