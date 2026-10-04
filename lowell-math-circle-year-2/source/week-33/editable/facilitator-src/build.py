#!/usr/bin/env python3
"""Rebuild the adult guide from guide.json. Requires reportlab and DejaVu fonts."""
from pathlib import Path
import json
from reportlab.pdfgen import canvas
from reportlab.platypus import Paragraph, Table, TableStyle
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib import colors
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
HERE=Path(__file__).resolve().parent
for label,file in [('D','DejaVuSans.ttf'),('DB','DejaVuSans-Bold.ttf'),('DI','DejaVuSans-Oblique.ttf')]:
 pdfmetrics.registerFont(TTFont(label,str(HERE.parent/'fonts'/file)))
pdfmetrics.registerFontFamily('D',normal='D',bold='DB',italic='DI',boldItalic='DB')
INK=colors.HexColor('#192A36');BLUE=colors.HexColor('#214E69');MUTED=colors.HexColor('#586875')
styles={
 'title':ParagraphStyle('title',fontName='DB',fontSize=20,leading=24,textColor=BLUE,spaceAfter=10),
 'h':ParagraphStyle('h',fontName='DB',fontSize=12.2,leading=16,textColor=BLUE,spaceBefore=9,spaceAfter=5),
 'p':ParagraphStyle('p',fontName='D',fontSize=10.1,leading=14,textColor=INK,spaceAfter=6),
 'small':ParagraphStyle('small',fontName='D',fontSize=8.6,leading=12,textColor=MUTED,spaceAfter=5),
 'cell':ParagraphStyle('cell',fontName='D',fontSize=9.3,leading=12.5,textColor=INK),
}
data=json.loads((HERE/'guide.json').read_text())
out=HERE.parent/'facilitator-guide.pdf'
c=canvas.Canvas(str(out),pagesize=(612,792));c.setTitle(f"Week {data['week']} / {data['title']} / Facilitator guide");c.setAuthor('Bellingham Math Circle')
for pi,page in enumerate(data['pages'],1):
 c.setFont('D',8.5);c.setFillColor(MUTED);c.drawString(42,763,f"Week {data['week']} / {data['title']} / Adult guide")
 y=742
 for block in page:
  typ=block[0]
  if typ=='table':
   rows=[[Paragraph(str(v),styles['cell']) for v in row] for row in block[1]]
   widths=[528*x/sum(block[2]) for x in block[2]]
   t=Table(rows,colWidths=widths,hAlign='LEFT')
   t.setStyle(TableStyle([('VALIGN',(0,0),(-1,-1),'TOP'),('LEFTPADDING',(0,0),(-1,-1),6),('RIGHTPADDING',(0,0),(-1,-1),6),('TOPPADDING',(0,0),(-1,-1),5),('BOTTOMPADDING',(0,0),(-1,-1),5),('BACKGROUND',(0,0),(-1,0),colors.HexColor('#EAF0F3')),('ROWBACKGROUNDS',(0,1),(-1,-1),[colors.white,colors.HexColor('#F5F7F8')])]))
   w,h=t.wrap(528,700);y-=h;t.drawOn(c,42,y);y-=9
  else:
   sty=styles[typ];y-=sty.spaceBefore;p=Paragraph(block[1],sty);w,h=p.wrap(528,720);y-=h;p.drawOn(c,42,y);y-=sty.spaceAfter
  if y<44:raise RuntimeError(f"Page {pi} overflows to y={y}")
 c.setFont('D',8);c.setFillColor(MUTED);c.drawString(42,27,'Bellingham Math Circle | Prepared October 2026 | Unpiloted');c.drawRightString(570,27,str(pi));c.showPage()
c.save();print(out)
