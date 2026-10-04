"""Build the Week 2 shared exploration and drawing pages (ReportLab, US Letter).
Mathematical instance data lives in plans/week-02-shared-data.json.
Run with the bundled Python; no LaTeX or new activity accessories required.
"""
from pathlib import Path
import json
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import Paragraph

ROOT = Path(__file__).resolve().parents[3]
DATA = json.loads((ROOT/'plans/week-02-shared-data.json').read_text())
OUT = ROOT/'tmp/pdfs/week-02-shared/shared-explore-draw.pdf'
W,H=612,792
M=44

def fonts():
    for base,a,b in [('/System/Library/Fonts/Supplemental','Arial.ttf','Arial Bold.ttf'),('/usr/share/fonts/truetype/dejavu','DejaVuSans.ttf','DejaVuSans-Bold.ttf')]:
        if (Path(base)/a).exists():
            pdfmetrics.registerFont(TTFont('Aux',str(Path(base)/a)))
            pdfmetrics.registerFont(TTFont('AuxB',str(Path(base)/b)))
            pdfmetrics.registerFontFamily('Aux',normal='Aux',bold='AuxB')
            return
    raise RuntimeError('Arial or DejaVu Sans required')

class Book:
    def __init__(self):
        OUT.parent.mkdir(parents=True,exist_ok=True)
        self.c=canvas.Canvas(str(OUT),pagesize=(W,H))
        self.c.setTitle('Week 2 / Shared exploration and drawing pages')
        self.c.setAuthor('Bellingham Math Circle')
        self.page=0
    def start(self,topic='Lamp lab'):
        if self.page:self.c.showPage()
        self.page+=1
        c=self.c;c.setFillGray(.1);c.setStrokeGray(.1)
        c.setFont('AuxB',10.3)
        c.drawString(M,H-39,f'Week 2 / {topic} / Shared collection')
        c.setLineWidth(.6);c.setStrokeGray(.55);c.line(M,44,W-M,44)
        c.setFont('Aux',8.5);c.setFillGray(.2)
        c.drawString(M,29,'Bellingham Math Circle / Week 2 / F02-S-v1')
        c.drawRightString(W-M,29,str(self.page if self.page <= 8 else self.page + 20))
    def problem(self,num,text,top=65,size=17):
        sty=ParagraphStyle('p',fontName='Aux',fontSize=size,leading=23,textColor='#171717')
        display_num = num if num <= 14 else num + 18
        p=Paragraph(f'<b>Problem {display_num}:</b> {text}',sty)
        _,ht=p.wrap(W-2*M,680)
        assert top+ht<741,(self.page,num,ht)
        p.drawOn(self.c,M,H-top-ht)
        return top+ht
    def graph(self,name,box,on=(),labels=True,r=None):
        # box is x,top,width,height. Fit isotropically, including generous node margin.
        c=self.c;x,t,w,h=box;g=DATA['graphs'][name]
        xy=g['xy'];xs=[p[0] for p in xy];ys=[p[1] for p in xy]
        r = r if r is not None else (20 if w>250 else 8)
        margin=r+18 if labels else r+4
        sc=min((w-2*margin)/(max(xs)-min(xs)),(h-2*margin)/(max(ys)-min(ys)))
        pts=[(x+w/2+(a-(min(xs)+max(xs))/2)*sc,H-t-h/2+(b-(min(ys)+max(ys))/2)*sc) for a,b in xy]
        c.setStrokeGray(.18);c.setLineWidth(2 if labels else 1.25)
        for a,b in g['edges']:c.line(*pts[a-1],*pts[b-1])
        for i,(px,py) in enumerate(pts,1):
            c.setFillGray(1);c.circle(px,py,r,fill=1,stroke=1)
            if i in on:
                c.setFillGray(.1);c.circle(px,py,4.3 if labels else 3.3,fill=1,stroke=0)
            # Student lamps are unnumbered; numbered matching keys are in the shared adult guide.
    def targets(self,name,sets,top,height=108):
        slot=(W-2*M)/len(sets)
        for i,ons in enumerate(sets):self.graph(name,(M+i*slot+8,top,slot-16,height),ons,False)
    def box(self,x,top,w,h,gray=.65):
        c=self.c;c.setStrokeGray(gray);c.setLineWidth(.8);c.rect(x,H-top-h,w,h)
    def dots(self,x,top,w,h,n=4):
        c=self.c;c.setFillGray(.58)
        size=min(w,h)-32;left=x+(w-size)/2;bottom=H-top-(h+size)/2
        for row in range(n):
            for col in range(n):c.circle(left+col*size/(n-1),bottom+row*size/(n-1),2,fill=1,stroke=0)
    def room(self,x,top,size,walls=()):
        c=self.c;c.setLineWidth(1.7);c.setStrokeGray(.15);c.rect(x,H-top-size,size,size)
        for a,b in walls:c.line(x+a[0]*size,H-top-size+a[1]*size,x+b[0]*size,H-top-size+b[1]*size)
    def save(self):
        assert self.page==14
        self.c.save()

def main():
    fonts();b=Book()
    b.start()
    b.problem(1,'Empty is OFF. A dot is ON. Choose a line. Change BOTH lamps at its ends: add a dot or erase a dot. Try a move. Try that same move again.')
    b.graph('square',(130,184,352,290))
    b.problem(2,'Start all OFF each time. Make each small picture on the big board.',490)
    b.targets('square',[[1,2],[1,3],[1,2,3,4]],589,116)

    b.start()
    b.problem(3,'Play with a partner. Start all OFF. Make one move: change both ends of a line. Can your partner turn all the lamps OFF? Swap jobs.')
    b.graph('square',(125,182,362,300))
    b.problem(4,'Start all OFF. Make TWO moves for your partner to undo. Swap jobs. Then try THREE moves. Show your moves if your partner wants a hint.',507)

    b.start()
    b.problem(5,'Start with only the top lamp ON each time. Change both ends of a line to make each small picture. Keep exactly ONE lamp ON after every move.')
    b.graph('ring6',(124,177,364,338))
    b.targets('ring6',[[3],[4]],525,99)
    b.problem(6,'Start at the top again. Visit every lamp and bring the light home.',653)

    b.start()
    b.problem(7,'Start with only the far-left lamp ON each time. Change both ends of a line. Move the light to match each small picture. Keep ONE lamp ON.')
    b.graph('tree8',(52,174,508,268))
    b.targets('tree8',[[5],[7],[8]],453,94)
    b.problem(8,'Now start all OFF. Make this two-light picture. You may have more than one light ON.',569)
    b.graph('tree8',(193,642,226,80),[1,8],False)

    b.start()
    b.problem(9,'Start all OFF for each small picture. Change BOTH ends of one line each move. Make the picture on the big board. Point to one you want to do again.')
    b.graph('ring6',(102,178,408,374))
    b.targets('ring6',[[1,2],[1,4],[1,2,4,5],[1,2,3,4,5,6]],599,118)

    b.start()
    b.problem(10,'Start all OFF for each small picture. Change BOTH ends of one line each move. Make the picture on the big board. Try a different way to make one picture.')
    b.graph('grid9',(105,181,402,360))
    b.targets('grid9',[[1,5],[2,8],[1,3,7,9],[1,3,4,6,7,9]],594,120)

    b.start()
    b.problem(11,'Put a dot in the top-left lamp of the LEFT island. Change BOTH ends of one line each move. Can you make the small picture?')
    b.graph('islands8',(46,205,520,230))
    b.graph('islands8',(156,445,300,124),[5],False)
    b.problem(12,'Draw ONE new line between lamps on different islands. Start again with only the top-left lamp of the left island ON. Try the trip with your bridge.',609)

    b.start()
    b.problem(13,'Draw 4 to 8 lamps. Join them with lines so every lamp has a path to every other lamp. Keep lines from crossing. Start all OFF. Make TWO moves, changing both ends of a line each time. Let a partner turn them all OFF.')
    b.box(M,215,W-2*M,346)
    b.problem(14,'Add one new lamp. Join it to an old lamp with a line. Make a new puzzle for your partner.',596)

    b.start('Shape drawing')
    b.problem(15,'Join dots with straight lines to make a closed shape with THREE corners. Keep your lines from crossing. Make two different shapes.')
    b.dots(46,176,244,218);b.dots(322,176,244,218)
    b.problem(16,'Now make two different closed shapes with FOUR corners. Touch each corner where your line turns.',435)
    b.dots(46,519,244,208);b.dots(322,519,244,208)

    b.start('Room making')
    b.problem(17,'Each square is a house. Draw ONE straight wall all the way across each house, from its outside edge to its outside edge. Make two rooms. Try different walls.')
    for x,t in [(70,184),(352,184),(70,409),(352,409)]:b.room(x,t,188)
    b.problem(18,'Make or find a house with two triangle rooms. Make or find one with two four-corner rooms. Draw on another sheet if you want to try more houses.',630)

    b.start('Room making')
    b.problem(19,'Draw TWO different straight walls all the way across each house. Walls may cross. Put one dot in each room. Try to make different numbers of rooms.')
    for x,t in [(70,185),(352,185),(70,449),(352,449)]:b.room(x,t,188)

    b.start('Room making')
    b.problem(20,'These houses each have THREE straight walls. Put one dot in every room. Which has the most rooms? In the empty house, try three different walls of your own.')
    for (x,t),name in zip([(70,185),(352,185),(70,449),(352,449)],['parallel3','concurrent3','general3',None]):
        b.room(x,t,188,DATA['room_maps'][name] if name else [])

    b.start('Room making')
    b.problem(21,'Put a dot or an X in every room in the first three houses. Rooms sharing a wall must have DIFFERENT marks. Rooms touching only at a corner may match.',size=16.5)
    for x,name in zip([44,233,422],['stripes','cross','general3']):
        b.room(x,201,146,DATA['room_maps'][name])
    b.problem(22,'Try this house. If two marks do not work, you may also use an O.',402,size=16.5)
    b.room(196,491,220,DATA['room_maps']['tee'])

    b.start('Room making')
    b.problem(23,'Make a house with one, two, or three different straight walls. Draw each wall all the way across. Let a partner put one dot in every room. Swap jobs.')
    b.room(144,187,324)
    b.problem(24,'Make a giant house together on a whiteboard or another sheet. Take turns adding one new straight wall all the way across. Do not trace an old wall. Stop after three walls. Find every room together.',557)
    b.save()
    print(f'Built {OUT}: 14 component pages (shared pages 1-8 and 29-34)')

if __name__=='__main__':main()
