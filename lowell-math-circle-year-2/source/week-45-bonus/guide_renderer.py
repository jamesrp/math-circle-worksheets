#!/usr/bin/env python3
"""Render a standalone Markdown adult guide with ReportLab; no network required."""
import argparse, re
from pathlib import Path
from xml.sax.saxutils import escape
from reportlab.pdfgen import canvas
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, KeepTogether
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

def render(source, output, week, topic):
    here=Path(__file__).resolve().parent
    font_dir=here/'fonts'
    font='Helvetica';bold='Helvetica-Bold'
    if (font_dir/'DejaVuSans.ttf').exists():
        pdfmetrics.registerFont(TTFont('GuideSans',str(font_dir/'DejaVuSans.ttf')))
        pdfmetrics.registerFont(TTFont('GuideSans-Bold',str(font_dir/'DejaVuSans-Bold.ttf')))
        pdfmetrics.registerFontFamily('GuideSans', normal='GuideSans',bold='GuideSans-Bold',italic='GuideSans',boldItalic='GuideSans-Bold')
        font='GuideSans';bold='GuideSans-Bold'
    styles=getSampleStyleSheet()
    body=ParagraphStyle('GuideBody',fontName=font,fontSize=9.8,leading=12.4,spaceAfter=4)
    h1=ParagraphStyle('GuideSection',fontName=bold,fontSize=12.5,leading=16,spaceBefore=8,spaceAfter=4,keepWithNext=True)
    h2=ParagraphStyle('GuideSub',fontName=bold,fontSize=11,leading=15,spaceBefore=8,spaceAfter=4,keepWithNext=True)
    bullet=ParagraphStyle('GuideBullet',parent=body,leftIndent=10,firstLineIndent=-7)
    code=ParagraphStyle('GuideCode',parent=body,fontSize=9,leading=12,leftIndent=10)
    def inline(s):
        s=escape(s)
        s=re.sub(r'\*\*(.+?)\*\*',r'<b>\1</b>',s)
        s=re.sub(r'(?<!\*)\*([^*]+)\*(?!\*)',r'<i>\1</i>',s)
        s=re.sub(r'`([^`]+)`',r'<font face="'+font+r'">\1</font>',s)
        s=re.sub(r'\[([^]]+)\]\(([^)]+)\)',r'\1 (\2)',s)
        return s
    lines=Path(source).read_text().splitlines()
    story=[];pending=[];in_code=False;table=[]
    def flush():
        if pending:story.append(Paragraph(inline(' '.join(pending)),body));pending.clear()
    def flush_table():
        if not table:return
        rows=[]
        for row in table:
            cells=[x.strip() for x in row.strip().strip('|').split('|')]
            if all(re.fullmatch(r':?-+:?',x) for x in cells):continue
            rows.append([Paragraph(inline(x),code) for x in cells])
        cols=max(map(len,rows));width=516/cols
        for row in rows:row.extend(['']*(cols-len(row)))
        obj=Table(rows,colWidths=[width]*cols,hAlign='LEFT',repeatRows=1)
        obj.setStyle(TableStyle([('VALIGN',(0,0),(-1,-1),'TOP'),('LINEBELOW',(0,0),(-1,0),.5,colors.grey),('LEFTPADDING',(0,0),(-1,-1),4),('RIGHTPADDING',(0,0),(-1,-1),4),('BOTTOMPADDING',(0,0),(-1,-1),6)]))
        story.extend([obj,Spacer(1,8)]);table.clear()
    for line in lines:
        if line.startswith('```'):
            flush();flush_table();in_code=not in_code;continue
        if in_code:
            story.append(Paragraph(inline(line).replace(' ','&#160;'),code));continue
        if line.startswith('|'):
            flush();table.append(line);continue
        flush_table()
        if not line.strip():flush();continue
        if line.startswith('#'):
            flush();depth=len(line)-len(line.lstrip('#'));title=line.lstrip('#').strip()
            # The adult page header supplies week/topic; redundant file title is omitted.
            if depth==1 and ('week' in title.lower() or 'bonus' in title.lower()) and 'mathemat' not in title.lower():continue
            story.append(Paragraph(inline(title),h1 if depth<=2 else h2));continue
        if re.match(r'^[-*] ',line):
            flush();story.append(Paragraph('&#8226; '+inline(line[2:]),bullet));continue
        pending.append(line.strip())
    flush();flush_table()
    Path(output).parent.mkdir(parents=True,exist_ok=True)
    def furniture(c,doc):
        c.saveState();c.setFont(font,9)
        c.drawString(48,762,f'Week {week} / {topic} / Bonus facilitator')
        c.setStrokeColor(colors.HexColor('#aaaaaa'));c.line(48,751,564,751)
        c.setFont(font,8)
        c.drawString(48,27,f'Bellingham Math Circle / Week {week} / W{week:02}-BONUS-FAC-v1 / Unpiloted')
        c.drawRightString(564,27,str(doc.page));c.restoreState()
    class DeterministicCanvas(canvas.Canvas):
        def __init__(self,*a,**kw):kw['invariant']=1;super().__init__(*a,**kw)
    doc=SimpleDocTemplate(str(output),pagesize=(612,792),leftMargin=48,rightMargin=48,topMargin=52,bottomMargin=44,title=f'Week {week} bonus facilitator: {topic}',author='Bellingham Math Circle')
    doc.build(story,onFirstPage=furniture,onLaterPages=furniture,canvasmaker=DeterministicCanvas)

if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('source');ap.add_argument('output');ap.add_argument('--week',type=int,required=True);ap.add_argument('--topic',required=True);args=ap.parse_args()
    render(args.source,args.output,args.week,args.topic)
