#!/usr/bin/env python3
"""Portable adult guide renderer. Usage: python build_guide.py guide.json output.pdf"""
from pathlib import Path
import json,sys,html
from reportlab.pdfgen import canvas
from reportlab.platypus import SimpleDocTemplate,Paragraph,Spacer,PageBreak,KeepTogether
from reportlab.lib.styles import getSampleStyleSheet,ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT
src=Path(sys.argv[1]);dest=Path(sys.argv[2]);dest.parent.mkdir(parents=True,exist_ok=True)
g=json.loads(src.read_text());week=g['week'];styles=getSampleStyleSheet()
styles.add(ParagraphStyle(name='BodyEncore',fontName='Helvetica',fontSize=10.5,leading=14,spaceAfter=7))
styles.add(ParagraphStyle(name='HeadEncore',fontName='Helvetica-Bold',fontSize=14,leading=17,spaceBefore=8,spaceAfter=9))
styles.add(ParagraphStyle(name='SubEncore',fontName='Helvetica-Bold',fontSize=11,leading=14,spaceBefore=7,spaceAfter=5))
def p(text,sty='BodyEncore'):
 text=html.escape(str(text)).replace('\n','<br/>')
 return Paragraph(text,styles[sty])
def section(title,text):
 out=[p(title,'SubEncore')]
 for item in text if isinstance(text,list) else [text]:out.append(p(item))
 return out
story=[p('Mathematical overview','HeadEncore')]
story.extend(p(t) for t in g['overview'])
story+=section('Entry routes and readiness',g['readiness'])
story+=section('Materials and preparation',g['materials'])
story+=section('Launch together',g['launch'])
story+=section('First visit and return visits',g['route'])
for inv in g['investigations']:
 story.append(PageBreak());story.append(p(f"Problem {inv['problem']}: {inv['title']}",'HeadEncore'))
 for label,key in [('Entry, prerequisites and timing','entry'),('Mathematical facts and solutions','solution'),('Hold-back hints','hints'),('Depth and further questions','extensions')]:
  story+=section(label,inv[key])
 if inv.get('notes'):story+=section('Facilitator notes',inv['notes'])
story.append(PageBreak());story.append(p('Sources, checks and classroom record','HeadEncore'))
story+=section('Sources and adaptation',g['sources'])
story+=section('Verification',g['verification'])
story+=section('What to record after a visit',g.get('observations',['Record investigations used, where each pair stopped, observations in the children\'s own words, and an interesting next question. Separate observation from your explanation of it.']))
story+=section('Status','Draft bonus companion. Unpiloted. Digital and mathematical checks do not establish physical fit, procedural rehearsal, staffing success or classroom pacing. Physical pretests have not been performed. Base student pages and base facilitator guide are separate.')
def page(c,doc):
 c.saveState();c.setFillColor(colors.black);c.setFont('Helvetica',9)
 c.drawString(36,755,f"Week {week} / {g['topic']} encore / Adult bonus guide")
 c.drawString(36,29,f"Bellingham Math Circle / Week {week} / W{week:02}-BON-FAC-v1")
 c.drawRightString(576,29,str(doc.page));c.restoreState()
doc=SimpleDocTemplate(str(dest),pagesize=(612,792),leftMargin=36,rightMargin=36,topMargin=60,bottomMargin=52,title=f"Week {week} bonus facilitator guide",author='Bellingham Math Circle',pageCompression=1)
doc.build(story,onFirstPage=page,onLaterPages=page)
print(dest)
