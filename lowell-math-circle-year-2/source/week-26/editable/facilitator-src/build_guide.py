#!/usr/bin/env python3
"""Editable, self-contained Week 26 facilitator PDF. Run from any directory.
Requires Python 3 and reportlab. Optional output argument defaults to ../facilitator-guide.pdf.
"""
from pathlib import Path
import sys
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor, Color, white
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import Paragraph
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from check_math import DATA, per, shared, rows, strip
HERE=Path(__file__).resolve().parent
from portable_fonts import font_directory
FONTS=font_directory('DejaVu Sans',['DejaVuSans.ttf','DejaVuSans-Bold.ttf'],'DEJAVU_FONT_DIR')
for family,file in [('Guide','DejaVuSans.ttf'),('GuideBold','DejaVuSans-Bold.ttf')]:
    pdfmetrics.registerFont(TTFont(family,str(FONTS/file)))
pdfmetrics.registerFontFamily('Guide',normal='Guide',bold='GuideBold',italic='Guide',boldItalic='GuideBold')
OUT=Path(sys.argv[1]).resolve() if len(sys.argv)>1 else HERE.parent/'build'/'facilitator-guide.pdf'
OUT.parent.mkdir(parents=True,exist_ok=True)
c=canvas.Canvas(str(OUT),pagesize=(612,792),invariant=1,pageCompression=1)
c.setTitle('Week 26 - Same area, different boundaries - Facilitator guide')
c.setAuthor('Bellingham Math Circle')
INK=HexColor('#243746');TEAL=HexColor('#19636c');PALE=HexColor('#dde9ec');GRAY=HexColor('#52626d')
style=ParagraphStyle('body',fontName='Guide',fontSize=10.1,leading=14.3,textColor=INK,spaceAfter=0)
small=ParagraphStyle('small',parent=style,fontSize=8.8,leading=12)
y=0;page_num=0;records=[]
def page(title,strap=''):
    global y,page_num
    if page_num:c.showPage()
    page_num+=1;y=714
    c.setFillColor(TEAL);c.setFont('GuideBold',9);c.drawString(48,754,'WEEK 26 / FACILITATOR GUIDE')
    c.setFillColor(GRAY);c.setFont('Guide',8);c.drawRightString(564,754,'DRAFT / UNPILOTED')
    c.setFillColor(INK);c.setFont('GuideBold',20);c.drawString(48,723,title)
    if strap:
        y=698;para(strap,small);y-=3
    c.setFillColor(GRAY);c.setFont('Guide',8);c.drawString(48,30,'Bellingham Math Circle / Unscheduled library slot / 2026-10-03')
    c.drawRightString(564,30,str(page_num))
    records.append({'page':page_num,'title':title})
def para(text,st=style,gap=8):
    global y
    p=Paragraph(text,st);w,h=p.wrap(516,700)
    if y-h<53:raise RuntimeError(f'Overflow page {page_num}: y={y}, h={h}, {text[:55]}')
    p.drawOn(c,48,y-h);y-=h+gap

def sub(text):
    global y
    y-=3;c.setFillColor(TEAL);c.setFont('GuideBold',11);c.drawString(48,y,text);y-=18

def figs(shapes,labels,columns=3,cell=15,added=None,removed=None,notes=None):
    global y
    for off in range(0,len(shapes),columns):
        batch=shapes[off:off+columns];W=516/columns;top=y-5;maxh=0
        for j,s in enumerate(batch):
            i=off+j;ss=set(s);ad=set(added[i]) if added and added[i] else set();rm=set(removed[i]) if removed and removed[i] else set()
            allpts=ss|ad|rm
            x0=min(x for x,z in allpts);x1=max(x for x,z in allpts);z0=min(z for x,z in allpts);z1=max(z for x,z in allpts)
            sz=min(cell,(W-22)/(x1-x0+1));height=(z1-z0+1)*sz
            left=48+j*W+(W-(x1-x0+1)*sz)/2
            c.setLineWidth(.65)
            for x,z in allpts:
                px=left+(x-x0)*sz;py=top-(z-z0+1)*sz
                c.setStrokeColor(INK);c.setFillColor(PALE if (x,z) not in ad else HexColor('#90c9b1'))
                if (x,z) in rm:
                    c.setFillColor(white);c.setDash(2,2)
                c.rect(px,py,sz,sz,stroke=1,fill=1);c.setDash()
                if (x,z) in ad:
                    c.setFont('GuideBold',min(10,sz*.7));c.setFillColor(INK);c.drawCentredString(px+sz/2,py+sz*.22,'+')
                if (x,z) in rm:
                    c.line(px+3,py+3,px+sz-3,py+sz-3);c.line(px+3,py+sz-3,px+sz-3,py+3)
            label=Paragraph(labels[i],small);_,lh=label.wrap(W-12,80);label.drawOn(c,48+j*W+6,top-height-10-lh)
            maxh=max(maxh,height+10+lh)
        y=top-maxh-17
        if y<53:raise RuntimeError(f'Figure overflow page {page_num}: {y}')

def hint(a,b):
    para('<b>Hold these hints.</b> First: '+a+' Then, only if needed: '+b)
def gate(text):para('<b>Prerequisites.</b> '+text)

page('Same area, different boundaries','Adult teaching key for the final six-page K-1, Grades 2-3 and Grades 4-5 packets (W26-*-v2). This is an unscheduled library activity, not a meeting date or a record of classroom use.')
sub('The mathematical invitation')
para('Keep the same number of square tiles. Rearrange them to make a shorter or longer boundary. Children can enter by building and counting; later they can explain why their record cannot be beaten. The task is to choose the region, unlike a tiling problem that supplies a fixed region to cover.')
sub('Prepare three tables')
para('For each table: 24 identical unit-square tiles, a reusable matching grid or clear table space, 40 short edge markers/counters, a ruler, pencils and blank square-grid paper. These are proposed supplies; check what is actually available. With the current group, plan for 3 younger children, 4 middle children and 3 older children, each table with one adult.')
para('Use roughly 20 mm tiles. A 12-by-12 working mat is 24 by 24 cm, wider than a US Letter sheet. Use a separate mat, align two sheets, or build on the table. A 12-tile straight row is 24 cm long. The small grids in the packets are drawing grids, not tile-sized placement boards. Do not let paper size rule out a long shape.')
para('Twenty-four tiles are a shared table set: let the middle table work in two pairs or build and compare in turns; use one shared model for large upper tasks. Reuse the 40 boundary markers between models. If each child needs an independent 24-tile set, prepare 240 tiles instead. Upper Problem 6 uses drawings of 37, 50 and 73 squares; extra physical tiles are optional.')
para('Print student pages single-sided on US Letter at 100%. Start with selected pages; keep the rest in reserve. Test a print, especially the student footer, which is near the paper edge. Never scale a tile mat without measuring it against the actual tiles. The guide figures are schematic.')
sub('Legal shape and boundary')
para('Put exactly the requested number of whole tiles in play. No overlaps, stacking or cutting. Every tile must be reachable from every other through full shared sides. Corner-only contact does not connect separate parts. Extra corner contact within an already side-connected shape is allowed. Count every exposed unit edge, including inner hole edges. Turns, flips and translation do not make a new shape. A tight string would miss indentations and holes, so use edge markers instead.')

page('A flexible hour','Choose a route by readiness. No child needs to finish a packet, and a good investigation can fill the entire group-work period.')
sub('A short shared launch: about 0-8 minutes')
para('Allow 3 minutes of free handling. Gather everyone around three tiles. Make an L, slide one tile to make a straight row, and show how a finger or marker counts one exposed unit side at a time. Ask, "What stayed the same? What changed?" Both boundaries happen to be 8. Show a corner-only join and repair it to a full-side join. Copy a small shape onto a recording grid. State the hole-edge rule without giving away the later hole problem. Stop the demonstration before explaining an optimizing method.')
sub('A menu for about 8-48 minutes')
para('<b>Concrete route:</b> K-1 Problem 1, then one of Problems 2-3. Children who enjoy exact possibilities can try Problems 4-5; one-tile relocation in Problem 6 is a separate substantial puzzle. Stop after a convincing all-four-tile collection or a pair of well-counted records.')
para('<b>Shared-edge route:</b> Grades 2-3 Problems 1-2, then 3 or 4. Offer Problem 5 for new maximum shapes, or Problem 6 for a harder minimization. Stop when children can account for an added tile or explain one maximum; symbolic algebra is optional.')
para('<b>Certification route:</b> Grades 4-5 Problem 1, then 3-4 to develop row/column bounds, and 5 to use them. Problem 2 is a separate maximum/tree/hole branch. Problem 6 is for children ready to generalize. Stop after one optimum with a construction and an argument ruling out less.')
para('Around minute 30, offer a brief stand-and-stretch or gallery look if attention needs a reset. Do not interrupt an absorbed group just to keep the menu. At 48-56 minutes, share two equal-area shapes or one surprising result; let a child point to the reason. Use the last few minutes to collect tiles and record what was actually attempted.')
sub('Readiness and adult moves')
para('<b>K-1:</b> adult reads aloud; count to about 18, pair a marker with an edge, compare lengths and recognize turns/flips. No multiplication or written proof required. <b>Grades 2-3:</b> count to about 26, add/subtract small numbers and follow a reason applying to all shapes; a formula can be expressed in words. <b>Grades 4-5:</b> count rows/columns, multiply dimensions, compare integer possibilities and distinguish evidence from a proof. Square roots are optional adult notation.')
para('Give quiet building time before using the held hints. Ask for a recount when two counts disagree; do not announce which child is right. If drawing consumes the thinking time, the adult can record a child-built model. Save formal arguments for children who want to know why no better shape exists.')

page('The three reusable arguments','Use these arguments after concrete examples. A proof can be a careful explanation with tiles, edge markers or a drawing.')
sub('1. Shared edges and the longest boundary')
para('Let n be the number of tiles and e the number of full shared sides (count each meeting once). Separate tiles offer 4n edge contributions. Each shared side hides two contributions, so <b>P = 4n - 2e</b>. Thus P is even. Adding one tile beside exactly k old tiles gives <b>change in P = 4 - 2k</b>; k = 1, 2, 3, 4 gives +2, 0, -2, -4.')
para('A side-connected set of n tiles has at least n - 1 shared sides. To see this without graph terminology, start at any tile and discover every other tile along shared-side connections. Each newly discovered tile needs a connection to what is already reached; these n - 1 connections are distinct. Therefore <b>P is at most 2n + 2</b>. A straight row attains it.')
para('Equality means there are exactly n - 1 connections: the tile-adjacency graph is a tree. A 2-by-2 block supplies a cycle, so it cannot occur at the maximum. A hole need not force an adjacency cycle: a point contact can seal one without adding a shared side. See page 14 for an explicit counterexample to a false "no holes" rule.')
sub('2. Rows and columns certify a short boundary')
para('Suppose a shape occupies r rows and c columns. In each row, the leftmost and rightmost occupied intervals contribute at least two vertical exposed edges; extra gaps only add more. This gives at least 2r vertical edges. Columns similarly give at least 2c horizontal edges. Hence <b>P is at least 2(r + c)</b>, while <b>n is at most rc</b>. Equality in the boundary bound holds when every occupied row and column is a single interval. It does not require a full rectangle.')
sub('3. Balanced dimensions and attaining the bound')
para('For a fixed dimension sum s, the largest product comes from dimensions as close as possible: if c is at least r + 2, replacing (r,c) by (r + 1,c - 1) increases the product by c - r - 1. Repeating gives dimensions floor(s/2) and ceil(s/2). For even boundary P = 2s, the greatest area is therefore <b>floor(s/2) times ceil(s/2)</b>. The corresponding rectangle attains exactly P.')
para('For a given n, find the smallest s whose balanced rectangle can hold n. The minimum is 2s. Attainment for every n: start at a k-by-k square; append 1 through k adjacent tiles along a new side, starting at a corner (boundary 4k + 2). Then start at k by (k + 1); append 1 through k + 1 along the other new side (boundary 4k + 4). No gaps are left in rows or columns. At n = k squared, boundary is 4k. The compact adult formula is 2 ceil(2 sqrt(n)); the integer-dimension argument is enough throughout the packets.')

page('K-1 / Problem 1','Final student page 1: make every different four-tile shape and count its boundary.')
gate('Count exposed sides and compare a built shape after turning or flipping it. An adult can draw each discovery.')
figs(DATA['tetrominoes'],['Straight: P = 10','Square: P = 8','L: P = 10','T: P = 10','Zigzag: P = 10'],columns=3,cell=24)
para('<b>Exact answer:</b> five shapes up to turns and flips. The square has 8 exposed sides; the other four have 10. The sixth blank recording grid is not a request for a sixth shape.')
hint('Can you turn one of these models onto a model you already have?','Try shapes with a row of four, then a row of three, then no row of three in either direction.')
sub('Why this list is complete')
para('If four tiles lie in a straight row, there is only the straight shape. If the longest straight run is three, the fourth tile must join that run. Placing it beyond an end returns the straight shape; placing it beside an end gives L; placing it beside the middle gives T. Turns and flips account for either side or end.')
para('If there is no run of three horizontally or vertically, first find a connected three-tile part. It cannot be straight, so it is an L. Add the fourth tile along a side. Positions that make a three-tile run have already been handled; the remaining positions either fill its missing square or extend a two-step zigzag. These are the square and zigzag shown above. Thus no sixth type remains.')
para('For the counts, the square has four shared sides, giving 16 - 8 = 8. Each other shape has three shared sides, giving 16 - 6 = 10. Let children check with markers before introducing the subtraction shorthand.')
sub('A useful stopping point')
para('Accept five models with a careful explanation of duplicate turns/flips. The longest-run classification is a held adult argument, not a demand that every young child give a formal exhaustive proof. For an extension, ask which shape can gain a fifth tile without increasing its boundary; the square cannot, while L can fill its missing corner.')

page('K-1 / Problems 2 and 3','Final student pages 2-3: find shortest and longest shapes for 5, 6, 7 and 8 tiles.')
gate('Keep the tile count fixed while rearranging; count to 18. The lower-bound explanation may be demonstrated by an adult.')
figs(DATA['k2']+DATA['k3'],['5 tiles: shortest 10','5 tiles: longest 12','6 tiles: shortest 10','6 tiles: longest 14','7 tiles: shortest 12','7 tiles: longest 16','8 tiles: shortest 12','8 tiles: longest 18'],columns=4,cell=17)
para('<b>Exact extrema:</b> 5 tiles give 10 and 12; 6 give 10 and 14; 7 give 12 and 16; 8 give 12 and 18. These are witnesses, not lists of every optimizer. In particular, the seven-tile minimum is a 2-by-4 rectangle with one corner missing.')
hint('Where are two sides hidden when tiles meet?','For a short boundary, try making the shape compact. For a long one, try tiles that meet the old shape on just one side.')
sub('Why the records are unbeatable')
para('<b>Longest:</b> the connection argument on page 3 gives 2n + 2. The rows shown meet that bound. Children can start with 4 sides on one tile and add 2 exposed sides for each new tile in a row.')
para('<b>Shortest for 5 or 6:</b> boundary 8 or less would allow r + c at most 4. The largest rectangle with that sum is 2 by 2, holding only 4 tiles. Thus at least 10 sides are needed, and the diagrams attain 10.')
para('<b>Shortest for 7 or 8:</b> boundary 10 or less would allow r + c at most 5. The best such box is 2 by 3, holding only 6 tiles. At least 12 sides are needed, and the diagrams attain 12. Odd boundary lengths are excluded by paired shared-edge cancellations.')
sub('What to notice without rushing to a rule')
para('Adding area does not necessarily increase the least possible boundary: 5 and 6 share a minimum, as do 7 and 8. A shortest shape need not be a rectangle. An explanation can consist of counting exposed edges on the model and fitting candidate small boxes around it; square-root arithmetic is unnecessary.')

page('K-1 / Problems 4 and 5','Final student pages 4-5: six-tile repeated boundary lengths; possible five-tile boundary lengths.')
gate('Recognize when two shapes are genuinely different, and distinguish a failed attempt from an impossibility.')
sub('Problem 4: exactly 12 and 14 have two different answers')
figs(DATA['k4'],['P = 10: only type','P = 12: one type','P = 12: another type','P = 14: one type','P = 14: another type'],columns=3,cell=18)
para('With six tiles, P = 10 occurs only for a 2-by-3 rectangle up to turns/flips. Indeed P = 10 implies r + c at most 5. To hold 6 cells, dimensions must be 2 and 3 and every cell of that box must be filled. Therefore the second 10-side answer space cannot contain a different shape. The 12-side examples above have different bounding boxes (4 by 2 and 3 by 3); the two 14-side examples are a row and a bent row.')
hint('Do your two models match after a turn or flip?','If six tiles had only 10 sides, how small a box would have to contain them?')
sub('Problem 5: among 8, 9, 10, 11, 12, 13, only 10 and 12 work')
figs(DATA['k5'],['5 tiles, P = 10','5 tiles, P = 12'],columns=2,cell=19)
para('Boundary 8 would force a box holding at most 4 tiles (page 5), so it is too short. Odd lengths 9, 11 and 13 are impossible because starting from 4 sides per tile, every shared side removes two. Thus every boundary is even. The two drawings attain the remaining candidates. Equivalently, every occupied row contributes an even number of vertical boundary edges and every occupied column an even number of horizontal edges.')
hint('Try marking the edges you stop counting when two tiles meet.','Do those exposed edges disappear one at a time or in pairs?')

page('K-1 / Problem 6','Final student page 6 uses the revised task: move one tile, draw one best result, and say which starts can become shorter. It does not ask for every move.')
gate('Keep five tiles fixed while relocating the sixth. The final shape must be side-connected; do not count replacing a tile in its original position as a move.')
figs(DATA['k6_start'],['Top start: P = 14','Middle start: P = 14','Bottom start: P = 14'],columns=3,cell=18)
figs(DATA['k6_result'],['Best after one move: 14','Best after one move: 10','Best after one move: 12'],columns=3,cell=18)
para('<b>Moves shown:</b> in the top row, move the right endpoint just below the left endpoint. In the middle start, move the rightmost tile of its four-tile row into the gap between the two tiles in the next row. In the bottom L, move the far end of its four-tile arm into the inside corner. Turn/flip the diagrams freely to match the student page.')
para('<b>Exact answer:</b> only the middle and bottom starts can be made shorter. Their best boundaries are 10 and 12; the straight row stays at 14.')
hint('Choose a tile to lift and look at the five that remain.','Can the moved tile touch two or three old tiles without leaving another part disconnected?')
sub('Complete optimality arguments')
para('<b>Top:</b> moving an interior row tile splits the five remaining tiles into two straight pieces. The only grid cell side-adjacent to both pieces is the cell just vacated, so no different destination reconnects them. Moving an endpoint leaves a five-tile row. Any new cell can share only one side with that row, giving 12 + 2 = 14. This proves no shortening is possible.')
para('<b>Middle:</b> the move fills a 2-by-3 rectangle, boundary 10. No six-tile shape can have boundary less than 10 (page 5), so it is best.')
para('<b>Bottom:</b> the drawing attains 12. A boundary below 12 would have to be 10; page 6 shows that this requires a 2-by-3 rectangle. Any 2-by-3 rectangle in either orientation contains at most four of the original L tiles: a 3-by-2 box catches at most 3 + 1, and a 2-by-3 box at most 2 + 1 + 1. A one-tile move preserves five originals, so reaching that rectangle is impossible. Hence 12 is optimal.')
para('The independent exhaustive move check finds 22, 1 and 2 optimal source/destination moves respectively. Those counts are adult verification only; no exhaustive move list is required by the final worksheet.',small)

page('Grades 2-3 / Problem 1','Final student page 1: two different shortest and two different longest eight-tile shapes.')
gate('Count to 18, preserve eight tiles, and compare turns/flips. No formula is needed to enter.')
figs(DATA['m1'],['Shortest: 2 by 4, P = 12','Shortest: corner missing, P = 12','Longest: row, P = 18','Longest: bent row, P = 18'],columns=2,cell=22)
para('<b>Exact answer:</b> minimum 12, maximum 18. The 2-by-4 rectangle and 3-by-3 square missing a corner are different shapes, because their bounding boxes are different even after turning. The two long-boundary examples are also different.')
hint('Can you put more tile sides together without changing the tile count?','Could a shape of boundary 10 have enough rows and columns to hold eight tiles?')
sub('Why the extrema are exact')
para('For a short boundary, P at most 10 forces r + c at most 5, whose largest possible box is 2 by 3, holding 6 tiles. Eight tiles therefore need P at least 12, and both compact figures attain it. For the maximum, connectivity requires at least 7 shared sides; 32 - 2 times 7 = 18. Both long examples have exactly 7 shared sides.')
sub('Why exactly two shortest types exist (optional)')
para('A boundary-12 eight-tile shape has r + c at most 6 and rc at least 8. Up to interchange, only (2,4) and (3,3) qualify. The first must be the full rectangle. The second misses one cell: deleting a corner leaves perimeter 12, deleting a noncorner edge cell raises it to 14, and deleting the center raises it to 16. Thus the two pictured types are the complete minimum list. The task asks only for two, not this classification.')
para('If children reach their examples quickly, have them exchange models and independently count. Keep the connection lower bound for a group that is ready to argue about every possible shape rather than merely more trials.')

page('Grades 2-3 / Problem 2','Final student page 2: add one tile to each pictured start; find every different boundary change.')
gate('Compare before and after counts; understand that only the final position of the added tile matters.')
figs(DATA['m2'],['Row: before 12; only +2','Stair: before 12; 0 or +2','U: before 12; -2 or +2','Frame: before 16; -4 or +2'],columns=2,cell=19)
figs([DATA['m2'][1],DATA['m2'][2],DATA['m2'][3]],['Stair: + at (0,1), after 12','U: fill gap, after 10','Frame: fill center, after 12'],columns=3,cell=20,added=[{(0,1)},{(1,1)},{(1,1)}])
para('The green + cells are additions; coordinates in the first caption count columns from 0 at left and rows from 0 at top. For +2 in every start, attach a tile beyond the left end of the top row. The resulting boundaries are 14, 14, 14 and 18 in reading order. A row has only one possible change; its spare recording box may remain blank.')
hint('At the new position, how many old sides will be covered?','The new tile starts with four sides. For every old neighbor, one old side and one new side stop being exposed.')
sub('Why there are no other changes')
para('An addition touching k old neighbors changes P by 4 - 2k. The row has no empty position touching two of its cells. The stair has empty positions touching one or two cells, but none touching three. In the U, its central gap touches three; all other available positions touch only one (there is no two-neighbor position). In the frame, the center touches four and every exterior position touches one. This accounts for every empty side-neighbor position, so the complete change sets are {+2}, {0,+2}, {-2,+2}, {-4,+2}.')
para('The frame has outer boundary 12 and inner boundary 4, totaling 16. Filling the hole removes its 4 inner edges, giving 12. Counting only the outside would give a wrong starting value and obscure the intended phenomenon.')

page('Grades 2-3 / Problems 3 and 4','Final student pages 3-4: ten-tile shared-side examples; longest boundaries for four tile counts.')
gate('Count a shared side once, although it belongs to two tiles; use multiplication by 4 or repeated addition.')
sub('Problem 3: all five requested shared-side counts are possible')
figs(DATA['m3'],['e = 9: P = 22','e = 10: P = 20','e = 11: P = 18','e = 12: P = 16','e = 13: P = 14'],columns=3,cell=14)
para('Each figure has ten tiles. The two-row examples have row lengths (8,2), (7,3), (6,4) and (5,5), all left-aligned. Their shared sides are, respectively, 7 + 1 + 2 = 10; 6 + 2 + 3 = 11; 5 + 3 + 4 = 12; and 4 + 4 + 5 = 13. These sums count within each row, then between rows. The row of ten has 9 meetings.')
para('<b>Rule:</b> four times the tile count, minus twice the shared-side count. In symbols, P = 4n - 2e. The proof is the two hidden contributions at each meeting (page 3). This identity includes inner hole edges and allows shapes with holes.')
hint('Mark each meeting between tiles with one small dot.','How many of the original four-sides-per-tile count disappear at each dot?')
sub('Problem 4: maxima 10, 16, 22, 26')
figs(DATA['m4'],['4 tiles: P = 10','7 tiles: P = 16','10 tiles: P = 22','12 tiles: P = 26'],columns=2,cell=13)
para('A connected shape needs at least n - 1 meetings, so P = 4n - 2e is at most 2n + 2. The rows attain it. Explain the connection bound by discovering tiles one at a time through the already connected part, assigning each new tile a distinct joining edge. Extra meetings can only make the boundary shorter. This proves the maximum for every n, not just these four trials.')
hint('How few meetings can keep all your tiles in one piece?','Begin with one tile; every additional tile needs at least one connection to the group already reached.')

page('Grades 2-3 / Problem 5','Final student page 5: identify the given eight-tile maximum shapes, then make two more with no straight run of four.')
gate('Use the maximum 18 from Problem 4; count straight runs in both directions.')
figs(DATA['m5_given'],['Given top left: P = 18, yes','Given top right: P = 18, yes','Given bottom left: P = 12, no','Given bottom right: P = 16, no'],columns=2,cell=19)
para('In worksheet reading order the boundaries are <b>18, 18, 12, 16</b>. The straight and branching examples each have 7 shared sides. The rectangle has 10; the frame has 8. Since 8 tiles allow at most 18 exposed sides, exactly the first two reach the maximum.')
figs(DATA['m5_new'],['New staircase: 8 tiles, e = 7, P = 18','New bent path: 8 tiles, e = 7, P = 18'],columns=2,cell=20)
para('The two new examples each have eight tiles, exactly seven shared sides, and no horizontal or vertical straight run of four. Their bounding boxes are 5 by 4 and 3 by 4, so they cannot coincide under turns or flips. This gives the requested two different examples. Other answers are welcome if they satisfy all three checks.')
hint('Does a maximum shape have to be a straight row?','Try bending a chain. Watch for a new tile touching a second old tile, which would hide two extra boundary edges.')
sub('The complete argument children can use')
para('Every eight-tile connected shape has at least seven meetings. A chosen example with exactly seven is automatically maximal, because 32 - 14 = 18. Therefore a child does not have to compare it with every conceivable eight-tile shape. A branch is allowed: the key is the number of meetings, not whether the shape looks like a single path.')


page('Grades 2-3 / Problem 6','Final student page 6: produce changes +2, 0, -2, -4 with the fewest possible starting tiles.')
gate('Use change = 4 - 2k and reason about connecting the k neighbors of an empty target cell.')
figs(DATA['m6'],['+2: 1 starting tile','0: 3 starting tiles','-2: 5 starting tiles','-4: 7 starting tiles'],columns=4,cell=22,added=[{(1,0)},{(1,1)},{(1,1)},{(1,1)}])
para('<b>Exact minima:</b> 1, 3, 5 and 7 starting tiles. Green + marks the added tile. The starting perimeters are 4, 8, 12 and 16; after addition they are 6, 8, 10 and 12. The last start is a 3-by-3 frame missing its center and one corner. It is side-connected and valid; eight starting tiles are not necessary.')
hint('For your desired change, how many neighbors must the new square touch?','Build those neighbors around a still-empty target. How many extra tiles connect them without filling the target?')
sub('Why fewer cannot work')
para('<b>+2 needs one neighbor.</b> A starting shape is nonempty, so one is the lower bound and the singleton works.')
para('<b>0 needs two neighbors.</b> Any two side-neighbor cells of the same empty target are not side-adjacent to one another. Two starting tiles therefore cannot form a connected shape. Three arranged as an L do work.')
para('<b>-2 needs three neighbors.</b> These three neighbor cells are pairwise nonadjacent. One additional cell other than the target can touch at most two of them: only a diagonal corner can touch two, and no allowed cell touches three. Thus four starting tiles cannot connect all three target neighbors. Five tiles in the U shown do work.')
para('<b>-4 needs four neighbors.</b> Color the grid like a chessboard, with the empty target black. All four required neighbors are white. With at most six starting tiles there are at most two other tiles. A black connector other than the target touches at most two of the four required neighbors. If both extra tiles are black, they are not adjacent to one another and give at most four total shared sides. Six connected tiles need at least five. If at most one extra tile is black, at most two required neighbors can meet it; no other white required neighbor has a connection. Five or fewer starting tiles fail for the same reason. Seven in the pictured almost-frame work.')
para('This is a connector-count argument, not an assumption that every hole needs a complete eight-tile ring. The point-sealed gap is precisely the useful counterexample.',small)

page('Grades 4-5 / Problem 1','Final student page 1: find two different shortest shapes for 7, 10 and 13 tiles, if possible.')
gate('Experiment with compact shapes; count rows and columns. The optimum proof can wait until Problems 3-4.')
figs(DATA['h1'],['7 tiles: rows 4,3; P = 12','7 tiles: rows 3,3,1; P = 12','10 tiles: rows 4,4,2; P = 14','10 tiles: rows 4,3,3; P = 14','13 tiles: rows 4,4,4,1; P = 16','13 tiles: rows 4,4,3,2; P = 16'],columns=2,cell=19)
para('<b>Exact minima:</b> 7 gives 12, 10 gives 14, 13 gives 16. Each listed row-length description is left-aligned from top to bottom. Each figure has every row and every column in one interval, so P = 2(r + c).')
hint('Can you spread fewer rows or columns without losing tiles?','How many tiles could fit in a rectangle if its two side lengths add to one less than yours?')
sub('Certificates and distinctness')
para('At boundary 10, the biggest possible area is 2 times 3 = 6, so 7 needs at least 12. At boundary 12, the biggest area is 3 times 3 = 9, so 10 needs at least 14. At boundary 14, the biggest area is 3 times 4 = 12, so 13 needs at least 16. The diagrams attain these next even lengths.')
para('The two seven-tile boxes have dimensions 4 by 2 and 3 by 3. For ten tiles, both boxes are 4 by 3 but the two missing corner cells run along different-length sides of that box, so they cannot be matched by an isometry. For thirteen tiles, the first has a tile with only one neighbor; the second does not. Thus each pair is genuinely different.')

page('Grades 4-5 / Problem 2','Final student page 2: maximum twelve-tile boundary; three nonstraight examples; 2-by-2 blocks and holes.')
gate('Understand the shared-side formula and why a connected set needs at least n - 1 meetings. Allow enough time for the hole surprise.')
figs(DATA['h2'],['Bent row: e = 11, P = 26','Branch: e = 11, P = 26','Point-sealed hole: e = 11, P = 26'],columns=1,cell=17)
para('<b>Exact answer:</b> maximum 26. All three examples attain it, with twelve tiles and eleven shared sides. None is a straight row. The connection bound gives P at most 48 - 22 = 26, so no longer boundary is possible.')
hint('What condition on shared sides gives equality in the maximum bound?','Try leaving a corner out of a ring, and see whether all tiles still connect through full sides.')
sub('A 2-by-2 block: no. A hole: yes.')
para('A 2-by-2 block creates a four-edge cycle in the tile-adjacency graph. Removing one edge from a cycle leaves its vertices connected, so any connected graph with such a cycle has at least n edges rather than n - 1. Its perimeter is at most 2n, below the maximum. This rules out the block.')
para('In the third drawing, the empty center cell has a tile along each of its four sides. The missing upper-left corner is outside. At the point where those two empty cells meet diagonally, two occupied tiles meet at a corner and close the passage. For the usual union of closed grid squares, the center is a bounded component of the complement: a hole. Four of the 26 exposed edges surround it; the outer boundary contributes 22.')
para('This extra corner contact adds no shared side. The twelve tile-centers and their eleven side-connections still form a tree. Hence "tree adjacency implies no holes" is false under these worksheet rules. The rule forbidding corner-only connections merely requires the whole tile collection to be side-connected; it does not forbid additional corner contact inside a connected shape. Do not silently impose a different hole convention.')

page('Grades 4-5 / Problem 3','Final student page 3: row, column and boundary counts; two twelve-tile shapes spanning four rows and five columns.')
gate('Count occupied rows/columns rather than tiles in each; identify vertical versus horizontal exposed edges.')
figs(DATA['h3_given'],['2 rows, 6 columns, P = 16','3 rows, 4 columns, P = 14','4 rows, 5 columns, P = 18'],columns=3,cell=16)
para('All three supplied shapes have twelve tiles. Their exact (rows, columns, boundary) triples, left to right, are <b>(2,6,16), (3,4,14), (4,5,18)</b>. The third has left-aligned row lengths 5, 3, 2, 2.')
figs(DATA['h3_more'],['12 tiles, 4 by 5 span, P = 18','12 tiles, 4 by 5 span, P = 20'],columns=2,cell=24)
para('For the second construction, move the right tile from the bottom row of the first construction to the far right of the second row. Its rows become 5; 3 plus a separated tile; 2; 1. It remains connected through the full top row. Both examples use twelve tiles and exactly four rows and five columns.')
hint('In one occupied row, where must its left and right boundary edges occur?','Can extra gaps make those row or column contributions smaller?')
sub('The least possible boundary is 18')
para('Each of four occupied rows contributes at least two vertical boundary edges, for at least 8. Each of five occupied columns contributes at least two horizontal boundary edges, for at least 10. These count disjoint edge directions, so P is at least 18. The first construction attains it. Its rows and columns are all contiguous, so it has exactly those mandatory boundary edges.')
para('The second construction has an extra gap in its second row, producing two extra vertical boundary edges; its columns remain contiguous. Thus P = 20. This also explains why occupied dimensions alone give a lower bound rather than an exact perimeter in all cases.')
para('The final student sentence asks for the minimum for a shape occupying four rows and five columns. Whether children retain the twelve-tile restriction or read that sentence for any tile count, the answer remains 18, because the lower bound is the same and the first twelve-tile witness is admissible.')

page('Grades 4-5 / Problems 4 and 5','Final student pages 4-5: greatest area for a boundary, then least boundary for an area.')
gate('Multiply rectangular dimensions and compare products at a fixed dimension sum.')
sub('Problem 4: greatest numbers of tiles')
figs(DATA['h4'],['P = 12: 3 x 3 = 9','P = 14: 4 x 3 = 12','P = 16: 4 x 4 = 16','P = 18: 5 x 4 = 20'],columns=4,cell=15)
para('The exact answers are <b>9, 12, 16, 20</b>. For boundary 12, 14, 16 or 18, the sum r + c cannot exceed 6, 7, 8 or 9. For each sum, the balanced dimension pair gives the largest product (page 3). A smaller sum cannot give more area: increasing one positive dimension increases its product. The displayed rectangles reach the bounds with exactly the requested boundary.')
hint('What dimension pairs have the permitted sum?','Compare a long thin rectangle with a more balanced one that has the same dimension sum.')
sub('Problem 5: shortest boundaries')
figs(DATA['h5'],['12 tiles: P = 14','13 tiles: P = 16','17 tiles: P = 18','20 tiles: P = 18','21 tiles: P = 20'],columns=5,cell=14)
para('The exact answers are <b>14, 16, 18, 18, 20</b>. Construction row lengths are (4,4,4), (4,4,4,1), (4,4,4,4,1), (5,5,5,5), and (5,5,5,5,1). Every row/column is contiguous, so its perimeter is twice its row-plus-column span.')
para('<b>Lower-bound certificates:</b> boundary 12 holds at most 9 tiles, excluding it for n = 12. Boundary 14 holds at most 12, excluding it for n = 13. Boundary 16 holds at most 16, excluding it for n = 17 and n = 20. Boundary 18 holds at most 20, excluding it for n = 21. Because boundaries are even, each construction at the next even value is optimal. Bounds for smaller perimeters are no larger, so excluding the preceding even value excludes all smaller ones.')
hint('What is the biggest shape that could fit under the preceding even boundary?','Use your answers to Problem 4 as impossibility certificates.')

page('Grades 4-5 / Problem 6','Final student page 6: a rule for any even boundary at least 4; shortest boundaries for 37, 50 and 73 squares.')
gate('Generalize a fixed-sum product argument. Large diagrams can be shaded by rows; physical 73-tile stock is not required.')
para('<b>Rule:</b> halve the even boundary P to get s. Split s into two positive whole numbers as equal as possible, a = floor(s/2), b = ceil(s/2). The greatest area is ab. In terms of P alone this is floor(P squared / 16), but the balanced-dimensions rule is easier to use and explain.')
hint('What does half the boundary bound about rows plus columns?','When two dimensions differ by at least two, move one unit from the larger dimension to the smaller. What happens to the product?')
sub('Why the rule works for every allowed P')
para('Every shape has area n at most rc and r + c at most s. If r + c is smaller, increase a dimension until the sum is s; the product increases. With sum s fixed, replacing (r,c) by (r + 1,c - 1) when c is at least r + 2 increases the product by c - r - 1. Repeat until the dimensions differ by at most one. This proves n at most ab. The full a-by-b rectangle has area ab and boundary 2(a + b) = P, so the bound is attained. P at least 4 makes both dimensions positive.')
figs(DATA['h6'],['37 squares: 6 x 6 plus 1; P = 26','50 squares: 7 x 7 plus 1; P = 30','73 squares: 9 x 8 plus 1; P = 36'],columns=3,cell=13)
para('<b>37:</b> boundary 24 permits at most 6 times 6 = 36. The pictured 6-by-6 square plus one tile has 37 and boundary 24 + 2 = 26.')
para('<b>50:</b> boundary 28 permits at most 7 times 7 = 49. The pictured 7-by-7 square plus one tile has 50 and boundary 28 + 2 = 30.')
para('<b>73:</b> boundary 34 permits at most 8 times 9 = 72. The pictured 8-by-9 rectangle plus one tile has 73 and boundary 34 + 2 = 36.')
para('All three added tiles meet the rectangle on exactly one side. Each next even boundary is attained; the preceding one and all smaller values are impossible. Thus the exact minimum boundaries are <b>26, 30, 36</b>. The drawings fit the student recording grids after a turn if desired.')

page('Extensions, sources and limits','Keep extension questions in reserve. They are options for future or continuing work, not additional requirements on the final student pages.')
sub('Three extensions with adult resolutions')
para('<b>When does the least boundary jump?</b> Build from k-by-k to k-by-(k + 1), then to (k + 1)-by-(k + 1), using corner-started partial strips. The minimum is 4k at k squared; 4k + 2 for k squared &lt; n &lt;= k(k + 1); and 4k + 4 for k(k + 1) &lt; n &lt;= (k + 1) squared. The balancing bound and these constructions prove every interval (page 3).')
para('<b>Which shapes attain a row/column bound?</b> Exactly those with one occupied interval in every occupied row and every occupied column. A gap creates at least two extra edges in the relevant direction. Conversely, without gaps every row/column contributes exactly its mandatory pair. This permits many nonrectangular minimum examples.')
para('<b>Is no 2-by-2 block sufficient for maximum?</b> No: the eight-tile frame has no such block but has e = 8 and P = 16 rather than 18. Ask children to replace the false test with "exactly n - 1 shared sides." The point-sealed-hole example shows why "no hole" is also not the right tree test.')
sub('Sources actually consulted')
para('<b>Mathematics:</b> Greg Malen, Erika Roldan and Rosemberg Toala-Enriquez, <i>Extremal {p,q}-Animals</i>, arXiv:2109.05331v1, Corollary 1.8 and section 2. <link href="https://arxiv.org/html/2109.05331v1" color="#19636c">https://arxiv.org/html/2109.05331v1</link>. Read 2026-10-03. Corollary 1.8 gives the square-grid minimum 2 ceil(2 sqrt(n)); section 2 distinguishes perimeter edges and holes. The elementary counting, connection, balancing and relocation proofs in this guide were independently derived. The paper is an adult context reference, not a claim that these student tasks are reproduced from it.',small)
para('<b>Teaching:</b> Laura Givental, Maria Nemirovskaya and Ilya Zakharevich, <i>Math Circle by the Bay: Topics for Grades 1-5</i> (AMS, 2018), preface printed pp. viii-x (PDF pp. 9-11 in the local reference). These pages discuss mathematically rich themes, manipulatives, dialogue, independent attempts, explanations and flexible pace/depth. The launch, timing menu and exact page choices here are our adaptation, not the book\'s prescribed lesson. Local source: external-resources/msri-math-circle-books/Math Circle by the Bay.pdf.',small)
para('<b>Local design evidence:</b> project AGENTS.md and README.md; plans/week-01-classroom-review.md (feedback recorded 2026-09-27); this run\'s PROMPT.md, review.md, review-math.md, review-math-work/verification.md, and final student PDFs/sources. The September report supports a common concrete launch and more time with examples. It does not establish that this perimeter activity has been taught.',small)
sub('Verification and after-use notes')
para('The supplied portable check script counts exposed edges directly, checks every illustrated construction, enumerates connected shapes through 8 cells, and exhausts the three revised one-tile relocation tasks. It checks row/column optimum values and attaining constructions through n = 200. These finite checks support the examples; the general claims rest on the proofs above. All 18 final guide pages were rendered for visual review. Student files were not changed.',small)
para('This guide and its timing proposals remain draft/unpiloted. After use, record the actual date, participants, pages attempted, models or explanations children produced, where adults had to restate a task, and questions worth continuing. Keep observations separate from guesses about causes; do not mark an unused page as taught.',small)
c.save()
import json
(HERE/'page-map.json').write_text(json.dumps(records,indent=2)+'\n')
print(f'Built {OUT} ({page_num} pages)')
