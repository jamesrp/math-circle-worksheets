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

def build():
 cfg=json.loads((HERE/'config.json').read_text()); week=cfg['week']; out=HERE.parent/'facilitator-guide.pdf'
 text=(HERE/'guide.md').read_text();story=[]
 for block in text.split('\n\n'):
  b=block.strip()
  if not b:continue
  if b=='---page---':story.append(PageBreak());continue
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
  c.drawString(45,30,'Unpiloted / Current base packets / Revised October 4 2026')
  c.drawRightString(567,30,str(doc.page));c.restoreState()
 doc=SimpleDocTemplate(str(out),pagesize=(612,792),rightMargin=45,leftMargin=45,topMargin=50,bottomMargin=48,title=f"Week {week} {cfg['title']} facilitator guide",author='Bellingham Math Circle',pageCompression=1)
 doc.build(story,onFirstPage=footer,onLaterPages=footer)
 print(out)
if __name__=='__main__':build()
