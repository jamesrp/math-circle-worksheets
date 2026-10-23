from pathlib import Path
from reportlab.pdfgen import canvas
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, KeepTogether
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib import colors
import re,sys,hashlib,json
from reportlab import rl_config
rl_config.invariant = 1
HERE=Path(__file__).resolve().parent
FONT=str(HERE.parent/'fonts'/'DejaVuSans.ttf')
BOLD=str(HERE.parent/'fonts'/'DejaVuSans-Bold.ttf')
pdfmetrics.registerFont(TTFont('Guide',FONT));pdfmetrics.registerFont(TTFont('GuideBold',BOLD));pdfmetrics.registerFontFamily('Guide',normal='Guide',bold='GuideBold',italic='Guide',boldItalic='GuideBold')
styles={
 'title':ParagraphStyle('title',fontName='GuideBold',fontSize=20,leading=25,spaceAfter=14),
 'h2':ParagraphStyle('h2',fontName='GuideBold',fontSize=13,leading=17,spaceBefore=12,spaceAfter=7,keepWithNext=True),
 'h3':ParagraphStyle('h3',fontName='GuideBold',fontSize=11,leading=14.5,spaceBefore=8,spaceAfter=4,keepWithNext=True),
 'p':ParagraphStyle('p',fontName='Guide',fontSize=10.3,leading=14.1,spaceAfter=7),
 'bullet':ParagraphStyle('bullet',fontName='Guide',fontSize=10.3,leading=14.1,spaceAfter=5,leftIndent=12,firstLineIndent=-10),
 'small':ParagraphStyle('small',fontName='Guide',fontSize=9.2,leading=12.5,spaceAfter=6),
}
def inline(s):
 s=s.replace('&','&amp;').replace('<','&lt;').replace('>','&gt;')
 s=re.sub(r'\*\*(.*?)\*\*',r'<b>\1</b>',s)
 s=re.sub(r'\[([^\]]+)\]\(([^)]+)\)',r'<link href="\2" color="#163c61">\1</link>',s)
 return s

from reportlab.platypus import Flowable
# The guide's five witness borders (page 4), drawn from the same motif as the student pages
# (problem-files figures.py; editable/src/mathematical-checks.json), October 23, 2026.
MOTIF=[(-1.3,-1.1),(1.3,-1.1),(1.3,-.4),(.8,-.4),(.8,-.65),(-.5,-.65),(-.5,0),(.6,0),(.6,.45),(-.5,.45),(-.5,1.1),(-1.3,1.1)]
ARROW=[(-.25,-.86),(.55,-.86)]
# Form -> sign changes of (x, y) in the motif's own coordinates (y down, as on the student pages).
FORMS={'A':(1,1),'H A':(1,-1),'V A':(-1,1),'R A':(-1,-1)}
H=1.5
WITNESSES=[('T: slides only',6,[(0,H,'A')]),('G: a glide, no flip',6,[(0,H,'A'),(3,-H,'H A')]),
 ('H: the flip, no half-turn',6,[(0,H,'A'),(0,-H,'H A')]),('R: half-turns, no flip',6,[(0,H,'A'),(3,-H,'R A')]),
 ('E: two crossing flips',6,[(1.5,H,'A'),(-1.5,H,'V A'),(1.5,-H,'H A'),(-1.5,-H,'R A')])]
class Witnesses(Flowable):
 """Three repeats of each witness at 30%, centred in an 18 by 6 cm box."""
 S=.3*28.3465;LAB=13;ROW=1.8*28.3465+24
 def wrap(self,aw,ah):self.aw=aw;return aw,2*self.ROW
 def draw(self):
  c=self.canv;S=self.S;col=self.aw/3
  for i,(name,period,motifs) in enumerate(WITNESSES):
   ox=(i%3)*col+(col-18*S)/2+3*S;oy=self.ROW*(2-i//3)-self.LAB-3*S  # border (0,0) on the page
   c.setFont('GuideBold',8.5);c.setFillColor(colors.black);c.drawString(ox-3*S,oy+3*S+4,name)
   c.setStrokeColor(colors.HexColor('#999999'));c.setLineWidth(.5);c.rect(ox-3*S,oy-3*S,18*S,6*S)
   c.setStrokeColor(colors.black);c.setDash(2,1.5);c.line(ox-3*S,oy,ox+15*S,oy);c.setDash()
   cs=[(x+period*k,y,form) for k in range(3) for x,y,form in motifs]
   lo=min(c[0] for c in cs)-1.3;hi=max(c[0] for c in cs)+1.3;shift=-3+(18-(hi-lo))/2-lo  # centre the three repeats
   for x,y,form in cs:
     cx=x+shift
     sx,sy=FORMS[form]
     pt=lambda u,v:(ox+(cx+sx*u)*S,oy+(y-sy*v)*S)
     p=c.beginPath();p.moveTo(*pt(*MOTIF[0]))
     for u,v in MOTIF[1:]:p.lineTo(*pt(u,v))
     p.close();c.setFillColor(colors.HexColor('#e6e6e6'));c.setLineWidth(.45);c.drawPath(p,fill=1,stroke=1)
     (a,b),(e,f)=pt(*ARROW[0]),pt(*ARROW[1]);c.setLineWidth(.45);c.line(a,b,e,f)
     dx=(e-a)/abs(e-a)*1.6;h=c.beginPath();h.moveTo(e+dx*.4,f);h.lineTo(e-dx,f+1.1);h.lineTo(e-dx,f-1.1);h.close()
     c.setFillColor(colors.black);c.drawPath(h,fill=1,stroke=0)

def build():
 cfg=json.loads((HERE/'config.json').read_text()); week=cfg['week']; out=HERE.parent/'facilitator-guide.pdf'
 text=(HERE/'guide.md').read_text();story=[]
 for block in text.split('\n\n'):
  b=block.strip()
  if not b:continue
  if b=='---page---':story.append(PageBreak());continue
  if b=='!witnesses':story.append(Witnesses());continue
  kind='p'
  if b.startswith('# '):kind='title';b=b[2:]
  elif b.startswith('## '):kind='h2';b=b[3:]
  elif b.startswith('### '):kind='h3';b=b[4:]
  elif b.startswith('- '):kind='bullet';b='• '+b[2:]
  elif b.startswith('!small '):kind='small';b=b[7:]
  story.append(Paragraph(inline(b.replace('\n',' ')),styles[kind]))
 def footer(c,doc):
  c.saveState();c.setFont('Guide',8);c.setFillColor(colors.HexColor('#555555'))
  c.drawString(45,759,f"Bellingham Math Circle / Week {week} / Adult facilitator guide")
  c.drawString(45,30,'Unpiloted / Current base packets / Revised October 23 2026 (K-1 and 4-5 v5)')
  c.drawRightString(567,30,str(doc.page));c.restoreState()
 doc=SimpleDocTemplate(str(out),pagesize=(612,792),rightMargin=45,leftMargin=45,topMargin=50,bottomMargin=48,title=f"Week {week} {cfg['title']} facilitator guide",author='Bellingham Math Circle',pageCompression=1)
 doc.build(story,onFirstPage=footer,onLaterPages=footer)
 print(out)
if __name__=='__main__':build()
