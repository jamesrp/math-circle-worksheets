#!/usr/bin/env python3
"""Editable, portable ReportLab builder for the Week 25 facilitator guide.
Run: python build_guide.py [--output ../facilitator-guide.pdf]
Only the standard library and ReportLab are required. Student files are read-only.
"""
from pathlib import Path
import argparse, json
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import Paragraph
from reportlab.lib.enums import TA_LEFT

ROOT=Path(__file__).resolve().parent
from portable_fonts import font_directory
FONTS=font_directory('Liberation Sans',[f'LiberationSans-{v}.ttf' for v in ['Regular','Bold','Italic','BoldItalic']],'LIBERATION_FONT_DIR')
for name, filename in [('GuideSans','Regular'),('GuideSans-Bold','Bold'),('GuideSans-Italic','Italic'),('GuideSans-BoldItalic','BoldItalic')]:
    pdfmetrics.registerFont(TTFont(name, str(FONTS/('LiberationSans-'+filename+'.ttf'))))
pdfmetrics.registerFontFamily('GuideSans',normal='GuideSans',bold='GuideSans-Bold',italic='GuideSans-Italic',boldItalic='GuideSans-BoldItalic')
W,H=612,792; M=46; WIDTH=W-2*M
BODY=ParagraphStyle('body',fontName='GuideSans',fontSize=10.5,leading=14.3,textColor=colors.black,spaceAfter=0)
SMALL=ParagraphStyle('small',parent=BODY,fontSize=9.2,leading=12.3)
CAP=ParagraphStyle('caption',parent=BODY,fontSize=9.3,leading=11.7,alignment=TA_LEFT)

class Guide:
    def __init__(self,path):
        self.c=canvas.Canvas(str(path),pagesize=(W,H),invariant=1);self.page=0;self.log=[]
        self.c.setTitle('Week 25 Discrete Tomography Facilitator Guide')
        self.c.setAuthor('Bellingham Math Circle')
        self.c.setSubject('Draft and unpiloted facilitator guide for unscheduled library slot')
    def new(self,title,where=''):
        if self.page:self.finish()
        self.page+=1;self.c.setFillColor(colors.black)
        self.c.setFont('GuideSans',9);self.c.drawString(M,H-32,'BELLINGHAM MATH CIRCLE  /  WEEK 25')
        self.c.setFont('GuideSans-Bold',18);self.c.drawString(M,H-64,title)
        self.y=H-88
        if where:self.p(where,small=True)
    def finish(self):
        assert self.y>=40,(self.page,self.y)
        self.log.append({'page':self.page,'bottom_content_y':round(self.y,2)})
        self.c.setFillColor(colors.HexColor('#555555'));self.c.setFont('GuideSans',8)
        self.c.drawString(M,29,'Facilitator draft / Unpiloted / Unscheduled library slot')
        self.c.drawRightString(W-M,29,str(self.page));self.c.showPage()
    def p(self,text,small=False,space=8):
        st=SMALL if small else BODY;p=Paragraph(text,st);_,h=p.wrap(WIDTH,700)
        assert self.y-h>=49,('overflow',self.page,text[:80],self.y,h)
        p.drawOn(self.c,M,self.y-h);self.y-=h+space
    def h(self,text):
        self.y-=5;self.c.setFont('GuideSans-Bold',12);self.c.setFillColor(colors.black)
        self.c.drawString(M,self.y-12,text);self.y-=23
    def boards(self,entries,cell=23):
        # Entries are (caption, binary picture). Every diagram shows fixed labels and counts.
        n=len(entries);slot=WIDTH/n;maxr=max(len(s.split('/')) for _,s in entries)
        height=maxr*cell+62;top=self.y
        for index,(caption,s) in enumerate(entries):
            rows=s.split('/');r=len(rows);c=len(rows[0]); assert all(len(t)==c for t in rows)
            assert c*cell+37 <=slot,(caption,'too wide')
            left=M+index*slot;cap=Paragraph(caption,CAP);_,ch=cap.wrap(slot-10,32)
            assert ch<=27,(caption,ch)
            cap.drawOn(self.c,left,top-ch)
            x=left+(slot-(c*cell+30))/2+10;y=top-37
            self.c.setStrokeColor(colors.HexColor('#555555'));self.c.setLineWidth(.55)
            for j in range(c+1):self.c.line(x+j*cell,y,x+j*cell,y-r*cell)
            for i in range(r+1):self.c.line(x,y-i*cell,x+c*cell,y-i*cell)
            self.c.setFont('GuideSans',9);self.c.setFillColor(colors.black)
            for j in range(c):self.c.drawCentredString(x+(j+.5)*cell,y+6,str(j+1))
            for i,row in enumerate(rows):
                yy=y-(i+.5)*cell
                self.c.drawRightString(x-5,yy-3,chr(65+i))
                self.c.circle(x+c*cell+12,yy,7,stroke=1,fill=0)
                self.c.drawCentredString(x+c*cell+12,yy-3,str(row.count('1')))
                for j,a in enumerate(row):
                    if a=='1':self.c.circle(x+(j+.5)*cell,yy,cell*.16,stroke=0,fill=1)
            for j in range(c):
                xx=x+(j+.5)*cell;yy=y-r*cell-12
                self.c.circle(xx,yy,7,stroke=1,fill=0)
                self.c.drawCentredString(xx,yy-3,str(sum(row[j]=='1' for row in rows)))
        self.y-=height+6;assert self.y>=49,('boards overflow',self.page,self.y)
    def done(self):
        self.finish();self.c.save();(ROOT/'layout-checks.json').write_text(json.dumps(self.log,indent=2)+'\n')


def build(path):
    g=Guide(path)
    g.new('Discrete tomography facilitator guide','Row and column shadows / Final student packets W25-K-v3, W25-23-v2, W25-45-v2')
    g.p('<b>Use this as a table-side answer and teaching guide.</b> Children build binary pictures, discover that identical line counts can hide different pictures, and investigate moves that preserve every count. The upper packet proves an exact shortest-route rule for two-row boards.')
    g.p('<b>Status:</b> facilitator draft, unpiloted; an unscheduled library slot. Week 25 is a library identifier, not a promised calendar date. K-1 page 1 models counts with A1 and A2 occupied; older packets retain their switch examples. Timing and hints below are proposals, not classroom observations.')
    g.h('Supplies and realistic preparation')
    g.p('For each of three tables: two reusable labeled grids, up to 4 rows by 6 columns; twelve identical counters at most 18 mm wide; count cards 0-6; two pencils; an eraser; and loose paper. Use reusable-mat cells at least 22 mm square. At 100% Letter size, student task cells are 22 mm, except upper p3 (20 mm); small switch examples are diagrams, not working mats. Print single-sided.')
    g.p('Print the three student packets: K-1 has 8 pages, grades 2-3 has 6, and grades 4-5 has 7. Print one guide for each adult, or just the relevant solution pages plus pages 1-2 and 16-18. Check scale with a ruler; clip each band separately. Draw a labeled 2-by-3 demonstration board on a whiteboard. Preparation should take about 10-15 minutes once materials are assembled.')
    g.p('Twelve counters per table support the largest comparison: two six-counter pictures. They do not preserve a whole catalog. Children draw each solution before reusing its counters. Keep both endpoints visible when comparing. Do not leave counters available to stack; every cell is empty or occupied once.')
    g.h('Place children by prerequisites')
    g.p('Plan one adult at each table: the current ten-child group has three K-1 children, four third graders, and three upper-band children. The parent volunteer can lead K-1; move children between entry points by readiness.',small=True)
    g.p('<b>K-1:</b> count up to 4, match a spoken count to a row or column, and distinguish labeled positions. No independent reading is needed; an adult reads the question and may record dictated counts. The six-picture catalog asks for organized search and persistence.')
    g.p('<b>Grades 2-3:</b> count up to 6, coordinate row and column conditions, and compare pictures. Reading can be shared. The main reasoning is completeness, a preserved quantity, and why fewer moves cannot work.')
    g.p('<b>Grades 4-5:</b> the same small counting plus reasoning about all possible pairs and a general construction. Multiplication, binomial notation, set notation, and formal proof language are optional adult tools. Use the concrete two-row tasks before the general statement.')
    g.p('<b>Diagram key:</b> black dots are counters, letters and top numbers are permanent labels, and circled side/bottom numbers are whole-line counts. Guide diagrams are answer sketches, not counter-sized working boards.',small=True)

    g.new('Launch and a flexible hour')
    g.h('Shared launch in about four minutes')
    g.p('First allow 2-3 minutes of handling the counters. Then place counters at A1, A3, and B2 on a labeled 2-by-3 board. Ask, "How many in row A? In row B? In each column?" Write row counts 2, 1 and column counts 1, 1, 1. Sweep along each entire line with a finger. Here "shadow" means a whole-line count, not a silhouette or a list of separate runs. Ask a child to make a picture matching these counts on the second board.')
    g.boards([('One launch picture','101/010'),('A different matching picture','110/001')],cell=25)
    g.p('Say, "Can the counts fit a different picture? The row letters and column numbers stay where they are." Demonstrate drawing a dot record before lifting counters. K-1 page 1 separates labels from circled counts with row/column sweeps. Stop here; hold back search orders, switches and uniqueness rules. Let children encounter ambiguity first.')
    g.h('An hour is a menu, not a page race')
    g.p('<b>0-3 minutes:</b> free handling. <b>3-7:</b> shared launch. <b>7-47:</b> table investigations, with a one-minute stand-and-stretch when needed. <b>47-55:</b> choose one result to show. <b>55-60:</b> whole-group sharing and reset. Let a productive problem take the whole working period.')
    g.p('<b>K-1 route:</b> P1 to establish the task, P2 or P3 for a catalog, then P4 for a forced picture. P5 and the new P6 are construction reserves. A child who is still comparing two pictures need not complete a six-picture catalog.')
    g.p('<b>Middle route:</b> P1, P2, then P3. Offer P4 for a shortest-route question or P5 for puzzle-making. <b>Upper route:</b> P1-P2, P3, then P4 or P5. P4 earns its place by introducing fixed full and empty columns before the general rule.')
    g.h('Hold hints until they are needed')
    g.p('Read the goal once, ask the child to show a legal attempt, and let the attempt develop. If stuck, give only the first held hint for that problem. Wait for a new attempt before offering the next. Adults may count aloud, trace a row, or scribe without taking over the choices. A drawing or an explanation with counters is a complete mathematical argument when it covers every case.')
    g.p('Sharing prompt: "Show two pictures with the same counts, or show why your picture is forced." Ask the upper table to show a shortest route and explain its lower bound. Do not require each group to report a theorem.',small=True)

    g.new('K-1 Problem 1','Student page 2 / Make two different pictures for each pair of grids')
    g.p('<b>Answer:</b> every pair can be filled differently. The three cases have 2, 2, and 3 solutions respectively. Any two of the displayed solutions solve each pair. Pictures are different when any fixed labeled cell changes, even if one is a reflection of another.')
    g.h('Top pair has exactly two pictures')
    g.boards([('A1 and B2','10/01'),('A2 and B1','01/10')],cell=26)
    g.p('<b>Why complete:</b> row A has one counter, in column 1 or 2. The other column must be occupied in row B, since both column counts are 1.',small=True)
    g.h('Middle pair has exactly two pictures')
    g.boards([('A1 and B3','100/001'),('A3 and B1','001/100')],cell=24)
    g.p('<b>Why complete:</b> column 2 is empty in both rows. Row A chooses column 1 or 3; row B must use the other. Keep column 2 in place. Removing it physically can obscure the labeled-board rule.',small=True)
    g.h('Bottom pair has exactly three pictures')
    g.boards([('B counter in column 3','110/001'),('B counter in column 2','101/010'),('B counter in column 1','011/100')],cell=22)
    g.p('<b>Why complete:</b> the lone B counter has three possible columns. Each choice forces A to fill the other two. <b>Held hints:</b> (1) "What does the zero tell us?" for the middle pair. (2) For the bottom pair, ask where B could put its one counter. <b>Look for:</b> changed pictures whose counts really stay unchanged, rather than moving only one counter and losing a column count.',small=True)

    g.new('K-1 Problem 2','Student page 3 / Find and draw every different picture for each set of counts')
    g.p('<b>Answer:</b> three pictures for the left column of grids and three for the right. They are two separate catalogs with different row counts. Draw one result before taking its counters away.')
    g.h('Left grids have row counts 1 and 2')
    g.boards([('A counter in column 1','100/011'),('A counter in column 2','010/101'),('A counter in column 3','001/110')],cell=25)
    g.h('Right grids have row counts 2 and 1')
    g.boards([('B counter in column 1','011/100'),('B counter in column 2','101/010'),('B counter in column 3','110/001')],cell=25)
    g.h('A complete argument a young child can give')
    g.p('For the left grids, the single top counter must be in one of three cells. Once it is placed, the bottom counters must occupy the other two columns, because each column needs exactly one. These are all three choices. The same argument with the bottom counter gives the right catalog. Top/bottom reversal connects the two catalogs, but does not merge them into one.')
    g.h('Held hints and facilitation')
    g.p('<b>First:</b> "Which row has just one counter?" <b>Second:</b> point to each cell in that row and ask whether the single counter could go there. If the child repeats a picture, compare the fixed labeled cells with an earlier drawing rather than crossing out a reflection as equivalent.')
    g.p('Accept counters plus an adult-scribed record. Three separate drawings establish the examples; pointing to all three possible locations establishes completeness. If a child finds a valid picture but gets lost in recording, let the adult copy that picture while the child checks its counts.')
    g.p('<b>Ready for more:</b> ask which pair of counters changes between two answers. Save the name "switch" for later unless the child wants it. <b>Stopping point:</b> one complete three-picture catalog with a reason it is complete is substantial work; the second is optional practice with reversed row counts.')

    g.new('K-1 Problem 3','Student pages 4-5 / All three-counter pictures with one in each row and column')
    g.p('<b>Answer:</b> exactly six. The first four recording grids are on page 4; the remaining two are at the top of page 5. The row letters stay fixed. These are the six permutation pictures, though children do not need that term.')
    g.boards([('A1, B2, C3','100/010/001'),('A1, B3, C2','100/001/010'),('A2, B1, C3','010/100/001')],cell=27)
    g.boards([('A2, B3, C1','010/001/100'),('A3, B1, C2','001/100/010'),('A3, B2, C1','001/010/100')],cell=27)
    g.h('Why six is the whole list')
    g.p('The A counter can occupy column 1, 2, or 3. For each choice, B can use either of the two remaining columns. C must use the last column. Thus there are two pictures for each of three choices: 2 + 2 + 2 = 6. The catalog groups these pairs by A position, so no picture is missed or counted twice.')
    g.h('Held hints')
    g.p('<b>First:</b> "Can you find another picture while this top counter stays put?" <b>Second:</b> after finding both, ask what happens if the top counter uses a different column. Do not print or dictate the whole case tree before children try organizing their own search.')
    g.p('<b>Common snag:</b> a child may call rotated or mirrored pictures "the same." Point to a named cell such as A1. If it is occupied in one and empty in the other, the pictures are different here. Conversely, moving physically indistinguishable counters without changing occupied cells does not create a new picture.')
    g.p('<b>Further question:</b> can two pictures be connected by changing only two counters at a time while every count stays 1? Yes. Exchanging the columns occupied by two rows is a legal switch. This is an optional bridge, not a prerequisite for a six-picture argument.')

    g.new('K-1 Problem 4','Student pages 5-6 / Decide when two different pictures are possible')
    g.p('<b>Answers in printed order:</b> no, no, yes. The solution counts are 1, 1, and 5. A failure to find another picture is not yet a reason that none exists; use the forcing arguments below.')
    g.boards([('Page 5 bottom: forced','111/100'),('Page 6 top: forced','110/100/000')],cell=25)
    g.p('<b>Page 5:</b> row A needs all three cells. Column 1 needs two counters, so B1 is occupied; B2 and B3 must be empty. <b>Page 6 top:</b> row C and column 3 are empty. Column 1 needs two counters, forcing A1 and B1. B is now full, so the remaining counter in column 2 is A2. Each case forces every cell.',small=True)
    g.h('Page 6 bottom has five matching pictures')
    g.boards([('1','011/100/100'),('2','101/010/100'),('3','101/100/010')],cell=22)
    g.boards([('4','110/001/100'),('5','110/100/001')],cell=22)
    g.p('Any two different boards from this five-picture list answer the question. For a completeness argument, split by the two occupied columns of A: if A uses 2 and 3, B and C both use 1; if A uses 1 and 3, B and C split columns 1 and 2 in two orders; if A uses 1 and 2, they split 1 and 3 in two orders. Total: 1 + 2 + 2 = 5.',small=True)
    g.p('<b>Held hints:</b> (1) "Which row or column is completely full or empty?" (2) Ask what cells that forces next. For the final pair, invite moving two counters together. K-1 only needs two valid examples there; the full list supports an adult or a child who asks for all possibilities.',small=True)

    g.new('K-1 Problems 5 and 6','Student pages 7-8 / Partner puzzles and the revised unique-versus-ambiguous construction')
    g.p('<b>P5:</b> there is no single required picture. Make any four-counter picture on each left grid, enter all counts, and let the partner test whether a different picture exists. Either answer can be correct. <b>P6:</b> the left grids must have unique reconstructions; the right grids must have more than one. The counts of the left and right grids need not match.')
    g.h('A complete valid answer to Problem 6')
    g.boards([('Left 2-by-3: unique','111/100'),('Right 2-by-3: ambiguous','110/101'),('Alternative for right','101/110')],cell=22)
    g.boards([('Left 3-by-3: unique','111/100/000'),('Right 3-by-3: ambiguous','110/001/100'),('Alternative for right','101/010/100')],cell=22)
    g.p('<b>Why the left pictures are unique:</b> A is full. On the 2-by-3 board, column 1 then forces B1, and B has no other counter. On the 3-by-3 board, C is empty and the same reasoning forces B1. These are complete forcing arguments, not just a search that found no alternative.')
    g.p('<b>Why the right pictures are ambiguous:</b> the adjacent alternative has exactly the same circled counts and is different in labeled cells. The 2-by-3 example has exactly two solutions. The 3-by-3 example has five, all displayed on guide page 6. Two witnesses suffice to establish "more than one." Every displayed picture uses four counters.')
    g.h('Checking a child-created answer')
    g.p('Count four occupied cells; verify every written margin; and compare labeled positions. For ambiguity, ask for a second matching board. For uniqueness, ask which cells are forced, or privately use the no-switch test on guide page 16. A picture with any legal switch cannot be unique. Never accept "my partner could not find one" as the only uniqueness argument.')
    g.p('<b>Held hints:</b> for a unique example, "What happens if a row is full?" For an ambiguous example, "Can two counters trade opposite corners without changing the counts?" Give these only after construction attempts. P6 is a new unpiloted reserve; do not claim its added page guarantees forty minutes for every child.',small=True)

    g.new('Grades 2-3 Problem 1','Student page 1 / Two matching pictures if possible')
    g.p('<b>Answers from top to bottom:</b> yes, no, yes. The three margin sets have 3, 1, and 2 solutions. All of them are shown here.')
    g.h('Top pair')
    g.boards([('B1','011/100'),('B2','101/010'),('B3','110/001')],cell=25)
    g.p('The single B counter has three choices. Once its column is selected, A must occupy the other two. Any two boards answer the printed task.',small=True)
    g.h('Middle pair')
    g.boards([('The only picture','111/100')],cell=25)
    g.p('Row A is full. The column count 2 forces B1; B has no counter left for another column. Therefore a different matching picture is impossible.',small=True)
    g.h('Bottom pair')
    g.boards([('First picture','110/101'),('Second picture','101/110')],cell=25)
    g.p('Column 1 is full. Each row still needs one counter, and columns 2 and 3 each need one, so those two counters split between the rows in exactly two ways.',small=True)
    g.p('<b>Held hints:</b> first ask about any full row or full column. Then ask where the single remaining counter can go. <b>Observe:</b> are children testing both rows and columns, or only matching the total number of counters? Equal total alone does not certify a solution.',small=True)

    g.new('Grades 2-3 Problem 2','Student pages 2-3 / Every picture with row and column counts 2, 1, 1')
    g.p('<b>Answer:</b> exactly five. Six recording grids are available; the unused grid is intentional space, not evidence of a sixth solution. Identical pieces and fixed row/column labels define the objects being counted.')
    g.boards([('A uses columns 2 and 3','011/100/100'),('A1, A3; B2','101/010/100'),('A1, A3; B1','101/100/010')],cell=26)
    g.boards([('A uses 1 and 2; B3','110/001/100'),('A uses 1 and 2; B1','110/100/001')],cell=26)
    g.h('Complete argument')
    g.p('Row A occupies exactly two of three columns, so it has exactly three possible patterns. If A uses columns 2 and 3, the remaining column counts are 2, 0, 0; both B and C must use column 1. This gives one picture.')
    g.p('If A uses 1 and 3, the remaining counts are 1, 1, 0. B and C each need one counter, so they use columns 1 and 2 in either order. This gives two pictures. If A uses 1 and 2, the remaining counts are 1, 0, 1, giving two more in the same way. These cases are disjoint and exhaust row A, so there are 1 + 2 + 2 = 5.')
    g.h('Held hints and useful questions')
    g.p('<b>First:</b> "Which of your pictures have the same top row?" <b>Second:</b> "If that top row is fixed, what column counts still have to be supplied below?" Offer the three possible top-row patterns only if the child cannot organize cases after trying.')
    g.p('If a child offers six, compare them cell by cell for a duplicate or recount the margins. If a child offers four, ask whether every top-row pattern has been considered. Accept a completeness explanation by pointing to drawings and covering row A with a strip of paper. Naming combinations is unnecessary.')
    g.p('<b>Optional bridge:</b> choose two catalog pictures and try to move between them while preserving counts. One pair may require more than one switch; finding a single switch is evidence of ambiguity, not a claim that every alternative is one move away.',small=True)

    g.new('Grades 2-3 Problem 3','Student pages 3-4 / A two-counter move and every legal switch')
    g.p('<b>Page 3:</b> the only alternative moves A1 and C3 to A3 and C1. The selected rows and columns are nonadjacent. All of row B, column 2, and the other cells remain unchanged.')
    g.boards([('Printed start','100/000/001'),('Only alternative','001/000/100')],cell=21)
    g.p('<b>Why a switch preserves counts:</b> each selected row loses one counter and gains one, and so does each selected column. Every other line is unchanged. The destination corners must both be empty. Counters need not move through the intervening cells.',small=True)
    g.h('Page 4 pictures in reading order')
    g.boards([('Top left: 0 switches','110/100/000'),('Top right: 1 switch','100/000/001')],cell=21)
    g.boards([('Bottom left: 3 switches','110/001/100'),('Bottom right: 0 switches','111/110/100')],cell=21)
    g.p('<b>Complete switch list:</b> top right has rows A,C and columns 1,3. Bottom left has rows A,B with columns 1,3; rows A,B with columns 2,3; and rows B,C with columns 1,3. Their results are respectively 011/100/100, 101/010/100, and 110/100/001, with slashes separating A/B/C. There are no others.',small=True)
    g.p('<b>Why the list is complete:</b> for each pair of rows, a switch needs a column occupied only in the first row and a column occupied only in the second. In the bottom-left picture, A versus B gives 2 choices; A versus C gives none because C is contained in A; B versus C gives 1. The top-left and bottom-right pictures have nested occupied-column sets for every row pair, so no switch exists.',small=True)
    g.p('<b>Held hints:</b> (1) "Must the two rows be next to each other?" (2) Choose a pair of rows and look for one counter unique to each. Do not slide all counters inside a rectangle; only its four selected corner cells change.',small=True)

    g.new('Grades 2-3 Problems 4 and 5','Student pages 5-6 / Exact move counts and partner constructions')
    g.h('Problem 4')
    g.p('<b>One complete answer:</b> use the middle picture below on the middle grid and the last picture on the bottom grid. The route switches columns 1,3 and then 2,4.')
    g.boards([('Start','1100/0011'),('Exactly 1 switch','0110/1001'),('Exactly 2 switches','0011/1100')],cell=23)
    g.p('<b>Why two cannot be one:</b> initially A occupies columns 1 and 2; in the last picture it occupies 3 and 4. One switch removes only one top-row counter from its old column and puts it in one new column. Two unwanted top positions must be removed, so at least two switches are necessary. The displayed route achieves two.')
    g.p('<b>All valid one-switch middle answers:</b> A occupies {1,3}, {1,4}, {2,3}, or {2,4}; B occupies the complementary pair. The only picture exactly two switches from the printed start has A={3,4}, B={1,2}. There are no other two-switch targets with these margins. The original picture has distance zero.',small=True)
    g.p('<b>Held hints:</b> first compare only row A of start and target. Then ask how many of its occupied columns one switch can replace. Counting four moved counters is not by itself a lower bound, because a route could move counters more than once.',small=True)
    g.h('Problem 5')
    g.p('<b>Yes, a different matching picture can be made impossible on both shapes.</b> These four-counter choices are valid. Their margins appear in the diagrams.')
    g.boards([('Unique 2-by-3 choice','111/100'),('Unique 3-by-3 choice','111/100/000')],cell=23)
    g.p('In each board A must be full. Column 1 requires B1. The 3-by-3 board has empty row C; all remaining cells are then forced empty. This establishes uniqueness. Other answers are welcome; check them using forcing or the criterion on guide page 16. A failed partner search alone proves nothing.',small=True)
    g.p('<b>Held hints:</b> ask whether a completely full row might help; then ask what the column counts force below it. For an ambiguous contrast, use 110/101 or 110/001/100 from guide page 7. A partner may solve by building the same picture; the question asks whether a <i>different</i> one exists.',small=True)

    g.new('Grades 4-5 Problems 1 and 2','Student pages 1-3 / The six two-row pictures and their greatest shortest distance')
    g.h('Problem 1 has exactly six pictures')
    g.boards([('Top columns 1,2','1100/0011'),('Top columns 1,3','1010/0101'),('Top columns 1,4','1001/0110')],cell=23)
    g.boards([('Top columns 2,3','0110/1001'),('Top columns 2,4','0101/1010'),('Top columns 3,4','0011/1100')],cell=23)
    g.p('Every column contains exactly one counter, so choosing the two occupied top columns determines the bottom row. The six possible pairs are 12, 13, 14, 23, 24, and 34. One way to prove completeness is to list pairs by their smaller element: three beginning with 1, two beginning with 2, and one beginning with 3. Total: 3 + 2 + 1 = 6.')
    g.h('Problem 2 has answer yes and greatest distance two')
    g.p('A legal switch exchanges one selected top column with one unselected top column. If two pictures are identical, distance is 0. If their top pairs share one column, switch the unwanted top column with the missing one; distance is 1. If the pairs are disjoint, replace one unwanted column, then the other; distance is 2.')
    g.p('The only distance-two pairs are {1,2} versus {3,4}, {1,3} versus {2,4}, and {1,4} versus {2,3}. Each needs at least two moves because one switch replaces just one top position. Every distinct pair fits one of these two cases, so all pictures communicate and the largest shortest distance is exactly 2.')
    g.p('<b>Example:</b> 12 to 23 to 34 is a shortest route from 12 to 34; the three corresponding boards appear on guide page 11. Each picture has four one-switch neighbors and one distance-two opposite.',small=True)
    g.h('Held hints')
    g.p('<b>P1 first:</b> "If I know the top row, is the bottom row still a choice?" <b>P1 second:</b> group pictures by the leftmost top counter. <b>P2 first:</b> choose a target and compare its top row with the current picture. <b>P2 second:</b> ask what one switch replaces. Keep a complete move graph as an optional child-made record, not an advance scaffold.')

    g.new('Grades 4-5 Problem 3','Student pages 4-5 / A shortest route on six columns')
    g.p('<b>Answer:</b> exactly 3 switches. The two blank grids on student page 5 record the two intermediate pictures. The route below switches column pairs 1,4; then 2,5; then 3,6. These are all legal two-row rectangles.')
    g.boards([('Start: top 1,2,3','111000/000111'),('After switching 1 and 4','011100/100011')],cell=27)
    g.boards([('After switching 2 and 5','001110/110001'),('After switching 3 and 6','000111/111000')],cell=27)
    g.h('Why no shorter route exists')
    g.p('The target has no top counter in columns 1, 2, or 3. The start has one in each of those columns. One switch can remove a top counter from at most one of these three unwanted columns, so every route uses at least three switches. The displayed three-switch route meets this lower bound exactly.')
    g.p('Equivalently, track the number of top counters already in target columns 4, 5, 6. It starts at 0 and ends at 3; one switch can raise it by at most 1. This is a lower bound for <i>all</i> legal routes, including routes that temporarily move a correct counter away.')
    g.h('Held hints')
    g.p('<b>First:</b> "Which top counters are in columns where the target has no top counter?" <b>Second:</b> ask how many such columns one move can fix. If the child has a three-move route but no minimality argument, do not ask them merely to try many two-move routes; focus on what every single move can do.')
    g.p('<b>Accept other routes:</b> pair the three unwanted top columns with the three missing top columns in any order, making each replacement once. Drawings or a list of switched column pairs both record a route, provided its moves are unambiguous. A legal move needs two occupied opposite corners and two empty opposite corners; check each actual intermediate board.')
    g.p('<b>Optional count:</b> these margins allow twenty pictures, because the top row chooses three of six columns. This fact is not required by P3. The proof of the shortest route does not depend on enumerating those twenty pictures.',small=True)

    g.new('Grades 4-5 Problem 4','Student page 6 / Fixed columns and four free columns')
    g.p('<b>Answers:</b> the printed endpoints are 2 switches apart; there are 6 pictures with these counts; the greatest shortest distance is 2. Column 1 is full and column 3 is empty in every solution. The only choices are columns 2, 4, 5, 6; exactly two must have their counter in row A.')
    g.boards([('Free top pair 2,4: start','110100/100011'),('Free top pair 2,5','110010/100101'),('Free top pair 2,6','110001/100110')],cell=20)
    g.boards([('Free top pair 4,5','100110/110001'),('Free top pair 4,6','100101/110010'),('Free top pair 5,6: target','100011/110100')],cell=20)
    g.h('A shortest route and its lower bound')
    g.p('Start with free top pair {2,4}. Switch columns 2,5 to obtain {4,5}, then columns 4,6 to obtain {5,6}. The intermediate board is the first board in the second row above. The two unwanted top columns, 2 and 4, each have to be removed; a single switch removes at most one. Therefore two is both necessary and sufficient.')
    g.h('Why there are six and why the diameter is two')
    g.p('Each solution corresponds to a two-element selection from four free columns. List the six selections shown: 24, 25, 26, 45, 46, 56. All full and empty columns are forced; once the free top pair is chosen, each remaining free counter must be below. The six cases are exhaustive and distinct.')
    g.p('Any pair of selections agrees on two, one, or zero columns, so its shortest distance is respectively 0, 1, or 2, by replacing unwanted top columns. The printed start and target are disjoint selections, so distance 2 actually occurs. It is incorrect to report 3 merely because there are three counters in each row: the counter in column 1 never needs to move.')
    g.h('Held hints')
    g.p('<b>First:</b> "Which columns are completely settled before you choose anything?" <b>Second:</b> "After placing the top counter in column 1, how many top counters remain among columns 2, 4, 5, and 6?" Preserve the original labels rather than silently renumbering those four columns.')

    g.new('Grades 4-5 Problem 5','Student page 7 / A complete theorem for any two-row board')
    g.p('<b>Rule:</b> the fewest switches equals the number of columns with a top counter in the start and no top counter in the target. Count unwanted top positions, not all differing cells. If there are none, the pictures already agree and the answer is zero.')
    g.h('A proof by construction and lower bound')
    g.p('<b>1. Separate forced columns.</b> A column total of 0 forces both cells empty; a total of 2 forces both full. Such columns agree in both pictures and never participate in a switch. Every remaining column has total 1 and exactly one counter, either above or below.')
    g.p('<b>2. There are equally many unwanted and missing top positions.</b> Both pictures have the same top-row count, and the same forced full columns. Among the total-1 columns, each therefore chooses the same number of top positions. Every top position present only in the start is balanced by one present only in the target.')
    g.p('<b>3. Match one of each.</b> Choose an unwanted top column u and a missing top column v. Currently the counters are at Au and Bv, while Bu and Av are empty. Switching those corners puts both columns in their target states. It does not disturb any other column. Repeat until there are no unwanted positions. If there were d initially, this supplies a route of d switches.')
    g.p('<b>4. No route can do better.</b> Any two-row switch removes only one top counter and adds only one top counter, so it can reduce the number of unwanted top columns by at most 1. That number must fall from d to 0. At least d switches are required. The constructed route uses exactly d, proving the rule and connectivity for every number of columns.')
    g.boards([('Unwanted top columns 2,4','110100/100011'),('Missing top columns 5,6','100011/110100')],cell=25)
    g.p('<b>Child-level explanation:</b> "Match each top counter in a wrong column with a column that needs one on top. Trade the top and bottom counters in each pair. Each trade fixes one wrong top place, and a move cannot fix more than one." Require both why the trades are legal and why they are enough.',small=True)
    g.p('<b>Held hints:</b> first identify forced columns; next pair a top counter that must leave with a top position that must be filled; only then ask why the two kinds occur equally often. A formula checked on the 6-column example alone is not a proof for any number of columns.',small=True)

    g.new('Why no switch means unique','Adult background and optional extension / Useful for K-1 P6 and grades 2-3 P5')
    g.p('<b>Exact criterion:</b> a binary picture with fixed labeled row and column counts is uniquely determined by those counts if and only if it has no legal rectangle switch. This applies to any finite rectangular board, not only two rows.')
    g.h('One direction is visible')
    g.p('If a legal switch exists, make it. It produces a different picture with the same counts, because each affected row and column loses and gains exactly one counter. Thus the original picture is not unique.')
    g.h('The converse needs an argument')
    g.p('<b>1. No switch forces nested row patterns.</b> Let S and T be the sets of occupied columns in any two rows. If neither set contains the other, choose a column in S but not T and another in T but not S. Their four corners form a switch. Therefore, if there is no switch, every pair of row sets is comparable by containment.')
    g.p('<b>2. The largest row is forced by the margins.</b> List row labels in decreasing row count on a separate note, keeping their identities. The largest row contains every other row set. Consequently it occupies exactly all the columns with positive count. Its required number of counters equals the number of those columns. In any competing picture with the same margins, zero-count columns cannot be used, so this row must fill every positive-count column too.')
    g.p('<b>3. Remove that forced row and repeat.</b> Subtract its counter from each affected column count. The remaining row sets in the original are still nested. The same argument forces the next largest row in every competing picture. Repeating through the finite list forces every row; therefore no different competing picture exists. Equal-size nested row sets are identical, so ties in the ordering cause no problem.')
    g.boards([('Nested: no switch, unique','111/110/100'),('Incomparable A and B: a switch','110/001/100')],cell=26)
    g.p('<b>How to use this with children:</b> invite two-row comparisons after concrete construction. If one row has a counter outside the other in each direction, the child can show a rectangle. For a uniqueness explanation, use forced full/empty lines on the small examples before introducing the whole nested-row argument.',small=True)
    g.p('<b>Scope:</b> reordering row labels is a device in the adult proof, not a permitted way to identify two student pictures. This proof is supplied here as an elementary argument. Ryser supplies the broader interchange theorem cited on page 18; the guide does not attribute this exact teaching proof to his paper.',small=True)

    g.new('Extensions and classroom decisions')
    g.h('Choose one extension that fits the work children did')
    g.p('<b>How many two-row pictures?</b> For a two-row board with column counts only 0, 1, or 2, if s columns have count 1 and t have count 2, a top-row count a requires k = a - t top counters among the s free columns. If 0 &le; k &le; s and the bottom count agrees with the total, every k-element selection gives one picture. The number is "s choose k." For children, enumerate the selections without requiring this notation. If the conditions fail, there are no pictures.')
    g.p('<b>How far apart can two be?</b> For feasible margins, the maximum shortest distance is min(k, s-k). A top selection has only k counters to remove and only s-k outside places to fill, so no distance can exceed either number. If k &le; s/2, choose disjoint k-element top selections to attain k. If k &gt; s/2, choose disjoint missing-position selections of size s-k; their complementary top selections attain s-k. This includes k=0 or k=s, when the picture is unique.')
    g.p('<b>Will equal total counts guarantee a picture?</b> No. On a 2-by-2 board, row counts (2,0) and column counts (2,0) both total 2, but row B is empty while column 1 asks for both rows. That contradiction proves impossibility. This extension concerns existence; the printed uniqueness questions all have at least one solution.')
    g.h('Do not extend the two-row distance formula blindly')
    g.boards([('Three-row start','100/010/001'),('Same top row; distance 1','100/001/010')],cell=23)
    g.p('These pictures have identical row and column counts and identical top rows, but one switch in rows B,C and columns 2,3 is needed. The two-row top-position formula would give zero, so it cannot be used for arbitrary-height pictures. General connectivity is true by Ryser, but our two-row proof alone does not establish it.',small=True)
    g.h('What to notice and what to record after a pilot')
    g.p('Record which exact problems children attempted, time spent, whether counts and fixed labels were clear, how they recorded catalogs, and which held hint changed the work. Note an actual child explanation of completeness or minimality if possible. Separate observations from hypotheses: "P3 needed three readings" is evidence; "the abstraction came too early" is an interpretation.')
    g.p('Keep the current status unpiloted until a real session occurs. In particular, check whether the new K-1 P6 sustains construction work and whether upper P3 uses its two intermediate grids well. Do not infer readiness or successful pacing from page count or from this mathematical verification.',small=True)

    g.new('Sources and verification','Preparation and mathematical checks completed 3 October 2026')
    g.h('Primary mathematical source')
    g.p('H. J. Ryser, <i>Combinatorial Properties of Matrices of Zeros and Ones</i>, <i>Canadian Journal of Mathematics</i> 9 (1957), 371-377. Section 3, Theorem 3.1, pages 375-376, defines interchanges and proves that binary matrices with identical row and column sums are connected by them. The definition and theorem/proof pages were inspected directly on 3 October 2026. <link href="https://doi.org/10.4153/CJM-1957-044-3" color="#000000"><u>DOI 10.4153/CJM-1957-044-3</u></link>.')
    g.p('The elementary nested-row uniqueness proof and exact two-row distance proof are supplied in this guide and the activity outline. They are not quoted from Ryser. Exhaustive finite tests support the printed examples; the general claims rest on the complete arguments on pages 15-17.')
    g.h('Pedagogy actually consulted')
    g.p('Laura Givental, Maria Nemirovskaya, and Ilya Zakharevich, <i>Math Circle by the Bay: Topics for Grades 1-5</i>, Preface, printed pages vii-ix (PDF pages 8-10), especially "How we teach" on page ix. The authors discuss peer interaction, manipulatives, varied pacing, independent problem solving, reserve challenges, and helping children articulate explanations. Local source: the repository copy in the MSRI math-circle collection.')
    g.p('The short common launch, the 60-minute menu, the exact held hints, the readiness routes, and the observation plan are proposed adaptations for this Bellingham group. They are not presented as tested prescriptions from that book. The organizer\'s project guidance and September 28 group context supplied the current planning assumptions: ten children, three adults, and concrete work before abstraction.')
    g.h('Packet alignment and independent checks')
    g.p('Reviewed the final student PDFs and editable source, the Week 25 activity prompt, and both adversarial reviews. Final numbering is K-1 P1-P6 and each older band P1-P5. Revised enumeration tasks explicitly request drawings. K-1 P6 is the added contrast construction; upper P3 continues on the added route page. This revision adds small switch examples to the middle and upper packets.')
    g.p('The separate verifier reconstructs solutions by row-subset enumeration and checks shortest paths by breadth-first search, without importing student answer files or the student builder. It verifies 13 fixed margin cases, every printed switch, all displayed shortest routes, and unique/ambiguous four-counter examples on both shapes. Four-counter margins have 9 unique and 3 ambiguous classes on 2-by-3; 45 unique and 27 ambiguous classes on 3-by-3. Labels remain fixed throughout.')
    g.p('It also checks the no-switch uniqueness criterion for every binary 2-by-4, 2-by-6, and 3-by-3 board, totaling 4,864 boards, and checks every same-margin ordered pair on both two-row sizes against the distance formula. The portable source bundle contains build_guide.py, verify_math.py, verification.json, layout-checks.json, and rebuilding instructions. The checks are finite verification, not classroom testing.',small=True)
    g.p('<b>Honest limits:</b> this guide and the revised tasks have not been piloted. No claim is made that every child will finish the packet or follow every proof in one hour. Use actual work to choose the next question. The arbitrary-height connectivity theorem is cited, not proved here; the exact distance result is proved only for two-row boards.',small=True)
    g.done()

if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--output',type=Path,default=ROOT.parent/'build'/'facilitator-guide.pdf');args=ap.parse_args()
    build(args.output);print(args.output)
