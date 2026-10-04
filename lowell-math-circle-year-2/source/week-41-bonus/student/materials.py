#!/usr/bin/env python3
"""Optional portal-copy preparation sheet. Requires ReportLab; no repo imports."""
from pathlib import Path
import argparse
from reportlab.pdfgen import canvas
p=argparse.ArgumentParser();p.add_argument('--out',type=Path,default=Path(__file__).resolve().parent.parent);a=p.parse_args();a.out.mkdir(parents=True,exist_ok=True)
c=canvas.Canvas(str(a.out/'portal-copies.pdf'),pagesize=(612,792),invariant=1)
c.setTitle('Week 41 portal copies - preparation template')
c.setFont('Helvetica',12);c.drawString(44,751,'Week 41 / Portals / Extra workspace')
letters=[['F','G','I'],['D','H','E'],['A','B','C']]
for x,y in [(54,433),(324,433),(54,151),(324,151)]:
 for r in range(3):
  for col in range(3):
   c.setLineWidth(.7);c.rect(x+78*col,y+78*r,78,78,stroke=1,fill=0)
   c.setFont('Helvetica',14);c.drawCentredString(x+(col+.5)*78,y+(r+.5)*78-4,letters[r][col])
c.setFont('Helvetica',9);c.drawString(44,34,'Bellingham Math Circle / Week 41 / W41-BONUS-materials-v1');c.save()
