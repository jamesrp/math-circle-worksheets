#!/usr/bin/env python3
"""Build and verify the complete facilitator investigation-plan atlas.

Defaults resolve from this file, so the command works from any directory.
Use the Codex bundled Python (ReportLab, pypdf, pdfplumber and Pillow).
Examples:
  python3 build_plans.py
  python3 build_plans.py --render --dpi 90
No student diagrams or content are synthesized by this renderer.
"""
from __future__ import annotations

import argparse
from collections import Counter
import hashlib
import html
import json
import math
from pathlib import Path
import re
import shutil
import subprocess
import sys
import unicodedata

from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (
    BaseDocTemplate, Flowable, Frame, KeepTogether, PageBreak, PageTemplate,
    Paragraph, Spacer, Table, TableStyle,
)
from pypdf import PdfReader

ROOT = Path(__file__).resolve().parents[3]
DEFAULT_PDF = ROOT / 'lowell-math-circle-year-2/combined/math-atlas-investigation-plans.pdf'
DEFAULT_QA = ROOT / 'tmp/pdfs/atlas/plans'
FAMILIES = ROOT / 'plans/atlas/families'
FONT_DIR = Path('/System/Library/Fonts/Supplemental')
NAVY = colors.HexColor('#17384A')
TEAL = colors.HexColor('#216C78')
INK = colors.HexColor('#25343C')
MUTED = colors.HexColor('#586872')
PALE = colors.HexColor('#EAF1F3')
LINE = colors.HexColor('#B6C9CD')
GROUPS = [
    ('algebra-discrete', 'Algebra and discrete mathematics', 'AD', 24),
    ('geometry-analysis', 'Geometry and analysis', 'GA', 36),
    ('applied-probability', 'Probability and applications', 'AP', 30),
]
GATES = [
    ('O', 'Follow a short spoken rule; sort, match, move or compare objects. Reading optional.'),
    ('C', 'Count small sets and track cases; add or subtract whole numbers as required.'),
    ('M', 'Multiply/divide and reason about factors or remainders.'),
    ('F', 'Fractions, ratios and signed numbers; the card specifies which are needed.'),
    ('V', 'Coordinates, vectors or geometric measurement in the stated representation.'),
    ('A', 'Variables, equations and functions; the card specifies the kind of algebra.'),
    ('P', 'Systematic proof: cases, induction, contradiction or quantified claims.'),
    ('L', 'Linear algebra: vectors, matrices, systems or eigenvectors as specified.'),
    ('D', 'Differential calculus: limits and derivatives as specified.'),
    ('I', 'Integral calculus: integrals and their meaning as specified.'),
    ('X', 'A named advanced prerequisite, such as groups, metric spaces or measure theory.'),
]


def typography(s):
    # Prose dashes/hyphens only. The mathematical minus U+2212 is preserved.
    return str(s).translate(str.maketrans({'\u2010':'-', '\u2011':'-', '\u2012':'-', '\u2013':'-', '\u2014':'-', '\u00ad':''}))


def esc(s):
    escaped=html.escape(typography(s), quote=False)
    for ch in '⟨⟩':
        escaped=escaped.replace(ch,'<font name="AtlasSymbols">'+ch+'</font>')
    return escaped


def register_fonts():
    for name, file in [('Atlas','Arial Unicode.ttf'), ('AtlasBold','Arial Bold.ttf'), ('AtlasItalic','Arial Italic.ttf')]:
        pdfmetrics.registerFont(TTFont(name, str(FONT_DIR/file)))
    pdfmetrics.registerFontFamily('Atlas',normal='Atlas',bold='AtlasBold',italic='AtlasItalic',boldItalic='AtlasBold')
    pdfmetrics.registerFont(TTFont('AtlasSymbols','/System/Library/Fonts/Apple Symbols.ttf'))


def styles():
    base = dict(fontName='Atlas', textColor=INK, fontSize=10.4, leading=13.65,
                spaceAfter=5, allowWidows=0, allowOrphans=0)
    result = {'body':ParagraphStyle('body',**base)}
    result['small'] = ParagraphStyle('small',parent=result['body'],fontSize=9.2,leading=12,spaceAfter=4)
    result['meta'] = ParagraphStyle('meta',parent=result['small'],textColor=MUTED,fontSize=9,leading=11.5)
    result['title'] = ParagraphStyle('title',fontName='AtlasBold',fontSize=22,leading=26,textColor=NAVY,spaceAfter=8)
    result['cover'] = ParagraphStyle('cover',parent=result['title'],fontSize=34,leading=39,spaceAfter=18)
    result['subtitle'] = ParagraphStyle('subtitle',parent=result['body'],fontSize=16,leading=21,textColor=TEAL,spaceAfter=12)
    result['section'] = ParagraphStyle('section',fontName='AtlasBold',fontSize=11,leading=14,textColor=TEAL,spaceBefore=9,spaceAfter=4,keepWithNext=True)
    result['index'] = ParagraphStyle('index',parent=result['body'],fontSize=11,leading=14.5,spaceAfter=0)
    result['gate'] = ParagraphStyle('gate',parent=result['body'],fontSize=10.1,leading=13.2,spaceAfter=0)
    return result


class Marker(Flowable):
    def __init__(self,key,title,level=0,card=None,part=None):
        super().__init__(); self.key=key; self.title=title; self.level=level; self.card=card; self.part=part
        self.width=0; self.height=0
    def draw(self): pass


class AtlasDoc(BaseDocTemplate):
    def __init__(self,path,**kw):
        super().__init__(str(path),pagesize=letter,leftMargin=48,rightMargin=48,topMargin=50,bottomMargin=45,
            title='Mathematics atlas - investigation plans',author='Bellingham Math Circle',
            subject='90 reviewed facilitator planning families; not classroom-piloted',**kw)
        self.page_map={}; self.sections={}; self.card_current=None
        frame=Frame(48,45,516,697,id='main',leftPadding=0,rightPadding=0,topPadding=0,bottomPadding=0)
        self.addPageTemplates(PageTemplate(id='main',frames=[frame],onPage=self.decorate))
    def decorate(self,canvas,doc):
        canvas.saveState()
        canvas.setStrokeColor(LINE);canvas.setLineWidth(.5);canvas.line(48,756,564,756)
        canvas.setFont('Atlas',8);canvas.setFillColor(MUTED)
        canvas.drawString(48,765,'BELLINGHAM MATH CIRCLE  /  MATHEMATICS ATLAS')
        canvas.drawRightString(564,765,'FACILITATOR PLANS  •  FIRST EDITION')
        canvas.line(48,34,564,34)
        canvas.drawString(48,22,'Plan-level designs. Prerequisites are capabilities, not ages.')
        canvas.drawRightString(564,22,str(doc.page))
        canvas.restoreState()
    def afterFlowable(self,flowable):
        if isinstance(flowable,Marker):
            self.canv.bookmarkPage(flowable.key)
            self.canv.addOutlineEntry(typography(flowable.title),flowable.key,level=flowable.level,closed=flowable.level==1)
            if flowable.card:
                row=self.page_map.setdefault(flowable.card,{})
                row[flowable.part]=self.page
                self.card_current=flowable.card
            else:self.sections[flowable.key]=self.page


def p(text,sty,tag='body'):
    return Paragraph(esc(text),sty[tag])


def labeled(label,text,sty,tag='body'):
    return Paragraph('<b>'+esc(label)+'</b> '+esc(text),sty[tag])


def section(title,contents,sty):
    return [p(title,sty,'section'),*contents]


def items(strings,sty,numbered=False):
    result=[]
    for i,s in enumerate(strings,1):
        prefix=f'{i}. ' if numbered else '• '
        result.append(p(prefix+s,sty))
    return result


def source_paragraph(src,sty):
    url=html.escape(src['url'],quote=True)
    return Paragraph('<link href="'+url+'" color="#216C78"><u>'+esc(src['title'])+'</u></link><br/>'
        +esc(src['locator'])+'<br/><b>Inspected:</b> '+esc(src['checked']),sty['small'])


def frontmatter(sty,cards,page_map):
    story=[Marker('overview','About this edition'),Spacer(1,42),p('Mathematics atlas',sty,'cover'),
        p('Investigation plans',sty,'subtitle'),
        p('90 ways into substantial mathematics',sty,'title'),
        p('A facilitator library extending from objects, drawings and games to algebra, calculus and named advanced prerequisites.',sty),Spacer(1,22)]
    for _,title,_,count in GROUPS:
        story.append(labeled(f'{count} families',title,sty))
    story += [Spacer(1,20),p('Start with the question. Keep the real prerequisites.',sty,'subtitle'),
        p('Each family preserves its exact opening rules, learner choices, access gates, worked example, boundary case, hints, source evidence and proposed hour. These are planning cards for facilitators; they contain answers and are not student worksheets.',sty),
        p('First edition • 25 September 2026',sty,'meta'),Spacer(1,14),
        p('Scope and review',sty,'section'),
        Paragraph('The companion <link href="math-atlas-research-map.pdf" color="#216C78"><u>research map</u></link> surveys 63 MSC fields and records 231 problem seeds. This book develops 90 selected families. Neither count means every subject or interesting problem has been exhausted. Independent mathematical/editorial review checks the stated instances; no family is classroom-piloted.',sty['body']),
        p('MSC attribution',sty,'section'),
        Paragraph('MSC2020 classification codes are from Mathematical Reviews / zbMATH, downloaded 25 September 2026. Classification-derived content is used under '
            '<link href="https://creativecommons.org/licenses/by-nc-sa/4.0/" color="#216C78"><u>CC BY-NC-SA 4.0</u></link>. '
            'The activity designs and annotations are original atlas work. This is an educational planning edition.',sty['small']),PageBreak()]
    story += [Marker('using','Using the planning cards'),p('Choose one investigation',sty,'title'),
        p('Read the launch and try the smallest instance before reading the solution. Choose a family whose question interests you, then check its entry, explanation and proof gates separately.',sty),
        *section('A workable hour',[
            p('The typical arc is 0-10 minutes to handle the materials, 10-15 to launch and check legal moves, 15-35 to investigate, 35-40 to move/reset, 40-55 for a second attempt or extension, and 55-60 to share. Each card customizes that menu. It is not a requirement to finish every question.',sty),
            p('Say the launch and provide the objects or sketch. Keep the solution beside you. Offer hints one at a time and preserve time for the learner to choose, conjecture and explain. The satisfying stop is useful even when a general proof remains beyond reach.',sty)],sty),
        *section('What a connection means',[
            labeled('exact-special-case:', 'The activity is a specified genuine instance of the mathematical object or theorem.',sty),
            labeled('faithful-representation:', 'Objects and legal moves encode the stated mathematical structure.',sty),
            labeled('shared-mechanism:', 'The reasoning has a common mechanism, but the activity does not establish the full advanced claim.',sty),
            labeled('motivation-only:', 'The comparison invites interest; it is not itself an instance or proof of the advanced theory.',sty)],sty),
        *section('Evidence is local to each claim',[
            p('Source entries state what was inspected: a full passage, an excerpt, a located topic, or a continuation. A citation is not a substitute for matching theorem hypotheses. Checked finite examples are distinct from general research continuations; a simulation is not a proof for all inputs.',sty),
            p('The independent reviews, exact-check scripts and limitations are preserved in plans/atlas/reviews/. Preparation times and proposed hour plans are editorial estimates, not classroom measurements. Advanced cards retain hard prerequisites when removing them would remove the mathematics.',sty)],sty),
        *section('Returning learners',[
            p('Before scheduling a family, consult its prior-use note and the collection use log. Record the exact board, starting numbers, rule set, function and explanation encountered. A familiar object can support a new question; changing only the story or the amount of arithmetic does not make a new investigation.',sty),
            p('The six-year goal is approximately 120 varied sessions along a child\'s path. This book is a broader library, not a fixed age sequence. Select, trial and adapt families; develop detailed student pages after choosing a route.',sty)],sty),PageBreak()]
    story += [Marker('capabilities','Prerequisite key'),p('Capabilities, not age labels',sty,'title'),
        p('A learner may have some of these tools and not others. O does not mean cognitively easy: spatial tracking, working memory, language and abstraction are specified separately in each card.',sty)]
    data=[[p(code,sty,'section'),p(desc,sty,'gate')] for code,desc in GATES]
    table=Table(data,colWidths=[35,481],hAlign='LEFT')
    table.setStyle(TableStyle([('VALIGN',(0,0),(-1,-1),'TOP'),('LEFTPADDING',(0,0),(-1,-1),8),('RIGHTPADDING',(0,0),(-1,-1),8),('TOPPADDING',(0,0),(-1,-1),6),('BOTTOMPADDING',(0,0),(-1,-1),6),('ROWBACKGROUNDS',(0,0),(-1,-1),[PALE,colors.white]),('LINEBELOW',(0,-1),(-1,-1),.5,LINE)]))
    story += [table,Spacer(1,10),*section('Four distinct gates',[
        labeled('Enter:', 'Join the activity and make a meaningful first move.',sty),
        labeled('Explore:', 'Track enough cases or calculations to investigate a pattern.',sty),
        labeled('Explain:', 'Justify the stated concrete result in an appropriate representation.',sty),
        labeled('Prove:', 'Meet the prerequisites for the more general theorem or formal argument.',sty),
        p('The hard stop names the point where a prerequisite becomes essential. Reading, arithmetic and reasoning demands supplement these codes. A proof can be an exhaustive arrangement, a drawing or an oral argument; formal notation is not required unless it carries the actual mathematics.',sty)],sty),PageBreak()]
    # Stable contents pages permit a reproducible two-pass page index.
    for _,title,prefix,_ in GROUPS:
        group=[c for c in cards if c['id'].startswith(prefix+'-')]
        chunk_size=24 if prefix=='AD' else (18 if prefix=='GA' else 15)
        chunks=[group[i:i+chunk_size] for i in range(0,len(group),chunk_size)]
        for i,chunk in enumerate(chunks):
            key=f'contents-{prefix}-{i}'
            story.append(Marker(key,title+' - contents'+(f' {i+1}' if len(chunks)>1 else '')))
            story += [p('Contents',sty,'meta'),p(title,sty,'title'),p('Select by question, then check the gates. Page numbers link to the opening plan.',sty,'small'),Spacer(1,8)]
            rows=[]
            for c in chunk:
                pg=page_map.get(c['id'],{}).get('participation','…')
                rows.append([Paragraph('<link href="#'+c['id']+'" color="#216C78">'+esc(c['id'])+'</link>',sty['index']),
                    Paragraph('<link href="#'+c['id']+'" color="#25343C">'+esc(c['title'])+'</link>',sty['index']),p(pg,sty,'index')])
            tab=Table(rows,colWidths=[57,424,35],hAlign='LEFT')
            tab.setStyle(TableStyle([('VALIGN',(0,0),(-1,-1),'TOP'),('LEFTPADDING',(0,0),(-1,-1),0),('RIGHTPADDING',(0,0),(-1,-1),5),('TOPPADDING',(0,0),(-1,-1),5),('BOTTOMPADDING',(0,0),(-1,-1),5),('LINEBELOW',(0,0),(-1,-1),.3,LINE)]))
            story += [tab,Spacer(1,13),p(f'{len(group)} families in this part'+(f' • Contents {i+1} of {len(chunks)}' if len(chunks)>1 else ''),sty,'meta'),PageBreak()]
    return story


def family_story(c,sty,field_names,group_first=None):
    result=[]
    if group_first:result.append(Marker('part-'+c['id'][:2],group_first,0))
    result += [Marker(c['id'],c['id']+'  '+c['title'],1,c['id'],'participation'),
        p(c['id']+'  /  Participation and launch',sty,'meta'),p(c['title'],sty,'title'),
        p('MSC primary '+c['msc_primary']+' - '+field_names.get(c['msc_primary'],'')+'  |  Secondary '+(', '.join(c['msc_secondary']) or 'none'),sty,'meta')]
    result += section('The opening challenge',[p(c['launch'],sty),labeled('Learner choices:',c['choices'],sty)],sty)
    result += section('Prerequisite gates',[labeled(label+':',c['gates'][key],sty) for key,label in [('entry','Enter'),('explore','Explore'),('explain','Explain'),('prove','Prove')]],sty)
    result += [labeled(label+':',c['gates'][key],sty,'small') for key,label in [('reading','Reading'),('arithmetic','Arithmetic'),('reasoning','Reasoning'),('hard_stop','Hard stop')]]
    result += section('Materials and preparation',[labeled(str(c['prep_minutes'])+' minutes estimated prep.',c['materials'],sty)],sty)
    result += section('A flexible hour',[p(c['session'],sty)],sty)
    result += section('Questions to explore',items(c['questions'],sty),sty)
    result += [labeled('Satisfying stop:',c['satisfying_stop'],sty),PageBreak()]
    result += [Marker(c['id']+'-reasoning',c['id']+'  Reasoning, limits and sources',2,c['id'],'reasoning'),
        p(c['id']+'  /  Facilitator reasoning',sty,'meta'),p(c['title'],sty,'title')]
    result += section('The mathematical question',[p(c['adult_question'],sty),p(c['anchor'],sty)],sty)
    result += section('Worked instance',[labeled('Problem:',c['example']['problem'],sty),labeled('Solution:',c['example']['solution'],sty),labeled('Boundary:',c['example']['boundary'],sty)],sty)
    result += section('Hints to reveal in order',items(c['hints'],sty,True),sty)
    result += section('Extensions',items(c['extensions'],sty),sty)
    result += section('Connection and its limits',[labeled('Bridge type:',c['bridge']['type'],sty,'small'),labeled('Preserves:',c['bridge']['preserves'],sty,'small'),labeled('Limits:',c['bridge']['limits'],sty,'small')],sty)
    result += section('Sources and inspection scope',[source_paragraph(s,sty) for s in c['source']],sty)
    result += [labeled('Prior use / what changes:',c['prior_use'],sty,'small'),labeled('Status:',c['status'],sty,'meta'),PageBreak()]
    return result


def normalized(s):
    return re.sub(r'\s+','',unicodedata.normalize('NFC',typography(s)))


def leaves(obj,path=''):
    if isinstance(obj,dict):
        for k,v in obj.items():yield from leaves(v,path+'.'+k)
    elif isinstance(obj,list):
        for i,v in enumerate(obj):yield from leaves(v,path+f'[{i}]')
    else:yield path,str(obj)


def qa(pdf,cards,page_map,qa_dir,input_hashes):
    import pdfplumber
    reader=PdfReader(str(pdf));texts=[page.extract_text() or '' for page in reader.pages]
    alltext='\n'.join(texts)
    uris=[]
    for page in reader.pages:
        for ref in page.get('/Annots',[]):
            annot=ref.get_object();act=annot.get('/A',{})
            if act.get('/URI'):uris.append(str(act['/URI']))
    missing=[]
    for c in cards:
        row=page_map[c['id']]
        text=normalized('\n'.join(texts[row['participation']-1:row['end']]))
        for path,value in leaves(c):
            if path.endswith('.url'):
                if value not in uris:missing.append({'id':c['id'],'field':path,'kind':'URL annotation'})
            elif normalized(value) not in text:
                missing.append({'id':c['id'],'field':path,'kind':'text','value':value[:100]})
    geometry=[]
    with pdfplumber.open(pdf) as doc:
        for i,page in enumerate(doc.pages,1):
            bad=[ch for ch in page.chars if ch['x0']<45 or ch['x1']>568 or ch['top']<15 or ch['bottom']>775]
            if bad:geometry.append({'page':i,'characters':''.join(ch['text'] for ch in bad)[:150]})
    result={'pdf':str(pdf),'pages':len(texts),'families':len(cards),'all_fields_present':not missing,
        'missing_fields':missing,'geometry_flags':geometry,'source_uri_links':len(uris),
        'replacement_character_count':alltext.count('\ufffd'),'pdf_sha256':hashlib.sha256(pdf.read_bytes()).hexdigest(),
        'input_sha256':input_hashes,'page_span_counts':dict(Counter(v['end']-v['participation']+1 for v in page_map.values())),
        'scope':'All source leaves checked against corresponding family PDF text (URLs against annotations); all page character bounds checked. Visual inspection remains separate.'}
    (qa_dir/'structural-qa.json').write_text(json.dumps(result,indent=2,ensure_ascii=False)+'\n')
    (qa_dir/'extracted-text.txt').write_text(alltext)
    if missing or geometry or result['replacement_character_count']:
        raise RuntimeError('PDF QA flags; see '+str(qa_dir/'structural-qa.json'))
    return result


def render(pdf,qa_dir,dpi,poppler):
    from PIL import Image, ImageDraw, ImageFont
    directory=qa_dir/'pages';directory.mkdir(exist_ok=True)
    for old in directory.glob('page-*.png'):old.unlink()
    subprocess.run([poppler,'-r',str(dpi),'-png',str(pdf),str(directory/'page')],check=True)
    pngs=sorted(directory.glob('page-*.png'))
    contacts=qa_dir/'contacts';contacts.mkdir(exist_ok=True)
    for old in contacts.glob('contact-*.png'):old.unlink()
    font=ImageFont.truetype(str(FONT_DIR/'Arial.ttf'),16)
    thumb_w=230;thumb_h=298;cell_w=250;cell_h=329
    for offset in range(0,len(pngs),16):
        group=pngs[offset:offset+16];sheet=Image.new('RGB',(cell_w*4,cell_h*4),(221,229,232));draw=ImageDraw.Draw(sheet)
        for j,file in enumerate(group):
            im=Image.open(file).convert('RGB');im.thumbnail((thumb_w,thumb_h))
            x=(j%4)*cell_w+10;y=(j//4)*cell_h+8
            sheet.paste(im,(x,y));draw.text((x,y+thumb_h+4),f'Page {offset+j+1}',font=font,fill=(23,56,74))
        sheet.save(contacts/f'contact-{offset//16+1:02}.png')
    return {'rendered_pages':len(pngs),'dpi':dpi,'pages_dir':str(directory),'contact_dir':str(contacts),'contact_sheets':math.ceil(len(pngs)/16)}


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path,default=DEFAULT_PDF)
    parser.add_argument('--qa-dir',type=Path,default=DEFAULT_QA)
    parser.add_argument('--render',action='store_true')
    parser.add_argument('--dpi',type=int,default=90)
    parser.add_argument('--pdftoppm',default=shutil.which('pdftoppm'))
    args=parser.parse_args()
    args.output.parent.mkdir(parents=True,exist_ok=True);args.qa_dir.mkdir(parents=True,exist_ok=True)
    register_fonts();sty=styles();cards=[];hashes={}
    for file,_,prefix,count in GROUPS:
        path=FAMILIES/(file+'.json');raw=path.read_bytes();data=json.loads(raw)
        assert len(data)==count and [c['id'] for c in data]==[f'{prefix}-{i:02}' for i in range(1,count+1)]
        cards.extend(data);hashes[str(path.relative_to(ROOT))]=hashlib.sha256(raw).hexdigest()
    tax=json.loads((ROOT/'plans/atlas/taxonomy.json').read_text())
    field_names={n['code'][:2]:n['title'] for n in tax['nodes'] if n['level']=='field'}
    # Fail rather than silently printing a notdef glyph.
    chars=set(typography(''.join(v for c in cards for _,v in leaves(c))))
    coverage=pdfmetrics.getFont('Atlas').face.charWidths
    fallback=pdfmetrics.getFont('AtlasSymbols').face.charWidths
    missing=sorted(ch for ch in chars if not ch.isspace() and ord(ch) not in coverage and not(ch in '⟨⟩' and ord(ch) in fallback))
    (args.qa_dir/'glyph-coverage.json').write_text(json.dumps({'missing':missing,'source_codepoints':len(chars),'font':'Arial Unicode','fallback_font':{'⟨':'Apple Symbols','⟩':'Apple Symbols'},'prose_dash_mapping':'U+2010/U+2011/U+2012/U+2013/U+2014 -> ASCII hyphen; soft hyphen removed','mathematical_minus_preserved':'−' in chars},ensure_ascii=False,indent=2)+'\n')
    if missing:raise RuntimeError('Unsupported source glyphs: '+repr(missing))
    previous={}
    for passno in range(2):
        story=frontmatter(sty,cards,previous)
        for file,title,prefix,_ in GROUPS:
            selected=[c for c in cards if c['id'].startswith(prefix+'-')]
            for i,c in enumerate(selected):story.extend(family_story(c,sty,field_names,title if i==0 else None))
        if isinstance(story[-1],PageBreak):story.pop()
        doc=AtlasDoc(args.output);doc.build(story)
        page_map=doc.page_map
        for i,c in enumerate(cards):
            page_map[c['id']]['end']=page_map[cards[i+1]['id']]['participation']-1 if i+1<len(cards) else doc.page
            page_map[c['id']]['title']=c['title']
        if passno and previous!=page_map:raise RuntimeError('Contents page references changed between passes')
        previous=page_map
    (args.qa_dir/'page-map.json').write_text(json.dumps(page_map,ensure_ascii=False,indent=2)+'\n')
    result=qa(args.output,cards,page_map,args.qa_dir,hashes)
    if args.render:
        if not args.pdftoppm:raise RuntimeError('pdftoppm not found; use --pdftoppm PATH')
        result['render']=render(args.output,args.qa_dir,args.dpi,args.pdftoppm)
    (args.qa_dir/'build-result.json').write_text(json.dumps(result,indent=2,ensure_ascii=False)+'\n')
    print(json.dumps(result,indent=2,ensure_ascii=False))


if __name__=='__main__':main()
