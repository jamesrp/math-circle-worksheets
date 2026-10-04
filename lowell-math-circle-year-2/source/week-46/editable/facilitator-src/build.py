#!/usr/bin/env python3
"""Rebuild this adult guide from editable guide.json. Requires reportlab and DejaVu."""
from pathlib import Path
import json
from reportlab.pdfgen import canvas
from reportlab.platypus import Paragraph,Table,TableStyle
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib import colors
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
HERE=Path(__file__).resolve().parent
for label,file in [('D','DejaVuSans.ttf'),('DB','DejaVuSans-Bold.ttf'),('DI','DejaVuSans-Oblique.ttf')]:
 pdfmetrics.registerFont(TTFont(label,str(HERE.parent/'fonts'/file)))
pdfmetrics.registerFontFamily('D',normal='D',bold='DB',italic='DI',boldItalic='DB')
styles={
 'title':ParagraphStyle('title',fontName='DB',fontSize=20,leading=25,textColor=colors.black,spaceAfter=12),
 'h':ParagraphStyle('h',fontName='DB',fontSize=12.5,leading=16,textColor=colors.black,spaceBefore=6,spaceAfter=4),
 'p':ParagraphStyle('p',fontName='D',fontSize=10.2,leading=14.2,textColor=colors.black,spaceAfter=6),
 'small':ParagraphStyle('small',fontName='D',fontSize=9,leading=12.5,textColor=colors.black,spaceAfter=6),
 'cell':ParagraphStyle('cell',fontName='D',fontSize=9.8,leading=13,textColor=colors.black),
}
data=json.loads((HERE/'guide.json').read_text())
out=HERE.parent/'facilitator-guide.pdf'
c=canvas.Canvas(str(out),pagesize=(612,792));c.setTitle(f"Week {data['week']} {data['title']} Facilitator guide");c.setAuthor('Bellingham Math Circle')
ys=[]
for pi,page in enumerate(data['pages'],1):
 c.setFont('D',8);c.setFillColor(colors.black);c.drawString(44,763,f"Week {data['week']} / {data['title']} / Adult guide")
 y=741
 for block in page:
  typ=block[0]
  if typ=='table':
   rows=[[Paragraph(str(v),styles['cell']) for v in row] for row in block[1]]
   widths=[524*x/sum(block[2]) for x in block[2]]
   t=Table(rows,colWidths=widths,hAlign='LEFT')
   t.setStyle(TableStyle([('VALIGN',(0,0),(-1,-1),'MIDDLE'),('LEFTPADDING',(0,0),(-1,-1),7),('RIGHTPADDING',(0,0),(-1,-1),7),('TOPPADDING',(0,0),(-1,-1),4),('BOTTOMPADDING',(0,0),(-1,-1),4),('BACKGROUND',(0,0),(-1,0),colors.HexColor('#EAEAEA')),('GRID',(0,0),(-1,-1),.4,colors.HexColor('#D9D9D9'))]))
   w,h=t.wrap(524,700);y-=h;t.drawOn(c,44,y);y-=10
  else:
   sty=styles[typ];y-=sty.spaceBefore;p=Paragraph(block[1],sty);w,h=p.wrap(524,720);y-=h;p.drawOn(c,44,y);y-=sty.spaceAfter
  if y<48:raise RuntimeError(f"Page {pi} overflows to y={y:.1f}")
 ys.append(round(y,1))
 c.setFont('D',8);c.setFillColor(colors.black);c.drawString(44,27,'Bellingham Math Circle / Prepared October 2026 / Unpiloted');c.drawRightString(568,27,str(pi));c.showPage()
c.save();print(out);print('Lowest content baselines',ys)
