#!/usr/bin/env python3
"""Append current route notes after a freshly rebuilt guide; preserve key page numbers.

The original builder must run first. This script never treats reference PDFs as
source. Route content is editable in route-note.json beside this file.
"""
from pathlib import Path
from io import BytesIO
import json, hashlib
from pypdf import PdfReader, PdfWriter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import ParagraphStyle
from xml.sax.saxutils import escape
HERE=Path(__file__).resolve().parent
ROOT=HERE.parent
cfg=json.loads((HERE/'route-note.json').read_text())
target=ROOT/cfg['guide_output']
reader=PdfReader(target)
stream=BytesIO()
styles={
 'title':ParagraphStyle('route-title',fontName='Helvetica-Bold',fontSize=17,leading=21,spaceAfter=12),
 'head':ParagraphStyle('route-head',fontName='Helvetica-Bold',fontSize=11.5,leading=15,spaceBefore=10,spaceAfter=5),
 'body':ParagraphStyle('route-body',fontName='Helvetica',fontSize=11,leading=15,spaceAfter=7),
 'small':ParagraphStyle('route-small',fontName='Helvetica',fontSize=9,leading=12,spaceAfter=8),
}
story=[Paragraph('Starting routes and return visits',styles['title']),Paragraph('Planning update of 4 October 2026. The timing menus are examples; a theme can continue over several meetings. Keep the full Grades 4-5 investigations and choose by readiness.',styles['small'])]
for heading,body in cfg['notes']:
 story.extend([Paragraph(escape(heading),styles['head']),Paragraph(escape(body),styles['body'])])
def decorate(c,doc):
 c.saveState();c.setFont('Helvetica',8)
 c.drawString(45,762,f"Week {cfg['week']} / {cfg['title']} / Adult guide")
 c.drawString(45,28,f"Bellingham Math Circle / Week {cfg['week']} / Route update / Unpiloted")
 c.drawRightString(567,28,str(len(reader.pages)+doc.page));c.restoreState()
SimpleDocTemplate(stream,pagesize=(612,792),leftMargin=45,rightMargin=45,topMargin=55,bottomMargin=48,title=f"Week {cfg['week']} route update").build(story,onFirstPage=decorate,onLaterPages=decorate)
stream.seek(0);note=PdfReader(stream)
assert len(note.pages)==1,('Route note must remain concise: one page',cfg['week'])
writer=PdfWriter()
for page in reader.pages:writer.add_page(page)
writer.add_page(note.pages[0])
writer.add_metadata({'/Title':f"Week {cfg['week']} {cfg['title']} facilitator guide",'/Subject':'Current base guide with first-route and return-visit notes; unpiloted','/Author':'Bellingham Math Circle'})
with target.open('wb') as f:writer.write(f)
# Keep any builder-generated QA summary aligned with the appended final guide.
manifest=HERE/'qa-manifest.json'
if manifest.exists():
 data=json.loads(manifest.read_text())
 if 'page_count' in data:data['page_count']=len(reader.pages)+1
 if 'guide_sha256' in data:data['guide_sha256']=hashlib.sha256(target.read_bytes()).hexdigest()
 data['fresh_review_revision']='2026-10-04; first routes and return visits; unpiloted'
 manifest.write_text(json.dumps(data,indent=2)+'\n')
print(f"Appended concise route update to {target}")
