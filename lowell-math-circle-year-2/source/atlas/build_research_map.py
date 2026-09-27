#!/usr/bin/env python3
"""Build the complete research-map book from the editable atlas surveys.

Run using the Codex bundled Python, or Python with reportlab/pypdf/pdfplumber/PIL.
No network access is required. The artifact-start marker is managed by the parent
publication workflow and is intentionally not invoked by this repeatable builder.
"""
from __future__ import annotations

import argparse
import csv
from collections import Counter
import hashlib
import html
import json
from pathlib import Path
import re
import shutil
import subprocess
import unicodedata

from PIL import Image, ImageDraw, ImageFont
from pypdf import PdfReader
import pdfplumber
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import inch
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (
    BaseDocTemplate, Frame, PageTemplate, Paragraph, Spacer, PageBreak,
    Table, TableStyle, KeepTogether, CondPageBreak,
)
from reportlab.platypus.tableofcontents import TableOfContents

ROOT = Path(__file__).resolve().parents[3]
ATLAS = ROOT / 'plans' / 'atlas'
DEFAULT_PDF = ROOT / 'lowell-math-circle-year-2' / 'combined' / 'math-atlas-research-map.pdf'
DEFAULT_QA = ROOT / 'tmp' / 'pdfs' / 'atlas' / 'map'
FONTDIR = Path('/System/Library/Fonts/Supplemental')
NAVY = colors.HexColor('#183342')
TEAL = colors.HexColor('#176B70')
GRAY = colors.HexColor('#52616B')
PALE = colors.HexColor('#EEF5F4')
PAGE = (612, 792)
LEFT, RIGHT, TOP, BOTTOM = 48, 48, 48, 48
WIDTH = PAGE[0]-LEFT-RIGHT

SURVEYS = [
    ('algebra-discrete', 'Algebra, discrete mathematics, and foundations', 'Part I'),
    ('geometry-analysis', 'Geometry, topology, and analysis', 'Part II'),
    ('applied-probability', 'Probability, computation, and applications', 'Part III'),
]

FONTS = {}
MISSING = Counter()
VISIBLE_TEXT = []


def register_fonts():
    for name, filename in [('Atlas', 'Arial Unicode.ttf'), ('AtlasBold', 'Arial Bold.ttf'), ('AtlasItalic', 'Arial Italic.ttf')]:
        f = TTFont(name, str(FONTDIR / filename))
        pdfmetrics.registerFont(f)
        FONTS[name] = f
    pdfmetrics.registerFontFamily('Atlas', normal='Atlas', bold='AtlasBold', italic='AtlasItalic', boldItalic='AtlasBold')


def normalize(text):
    # These four glyphs are absent from Arial Unicode. Keep the mathematical
    # meaning while using readable supported forms, not empty-glyph boxes.
    text = text.replace('𝔽', 'F').replace('⟨', '〈').replace('⟩', '〉').replace('ᵈ', '^d')
    text = text.replace('—', ' - ').replace('–', '-').replace('‑', '-').replace('\u00ad', '')
    text = text.replace('\\\\', '∖').replace('\\K', '∖K')
    text = ''.join(unicodedata.normalize('NFKC', c) if 0x1D400 <= ord(c) <= 0x1D7FF else c for c in text)
    return text


def glyph_text(text, font='Atlas'):
    text = normalize(text)
    VISIBLE_TEXT.append(text)
    result=[]
    for c in text:
        if ord(c) not in FONTS['Atlas'].face.charWidths and not c.isspace():
            MISSING[c] += 1
        escaped = html.escape(c)
        if ord(c) not in FONTS[font].face.charWidths and ord(c) in FONTS['Atlas'].face.charWidths:
            result.append(f'<font name="Atlas">{escaped}</font>')
        else:
            result.append(escaped)
    return ''.join(result)


def math_text(text, font='Atlas'):
    # Typeset simple plain-math powers and subscripts; leave paths as filenames.
    text = normalize(text)
    if re.search(r'\.(?:md|json|csv|py|pdf)\b', text):
        return glyph_text(text, font)
    # A plain index can contain several letters (u_tt), while a plain power
    # stays one letter so adjacent factors such as x^iy^j remain x^i y^j.
    pattern = r'([_^])(?:\{([^{}]+)\}|\(([^()]+)\)|((?<=_)[A-Za-z]+|[A-Za-z]|\d+))'
    out=[]; cursor=0
    for m in re.finditer(pattern,text):
        out.append(glyph_text(text[cursor:m.start()],font))
        value=next(v for v in m.groups()[1:] if v is not None)
        tag='super' if m.group(1)=='^' else 'sub'
        out.append(f'<{tag}>{glyph_text(value,font)}</{tag}>')
        cursor=m.end()
    out.append(glyph_text(text[cursor:],font))
    return ''.join(out)


TOKEN = re.compile(r'\[([^\]]+)\]\(([^)]+)\)|\*\*([^*]+)\*\*|(?<!\*)\*([^*]+)\*(?!\*)|`([^`]+)`|\[S(\d+)([^\]]*)\]')


def inline(text, font='Atlas', source_links=False):
    out=[]; cursor=0
    for m in TOKEN.finditer(text):
        out.append(math_text(text[cursor:m.start()],font))
        if m.group(1) is not None:
            label, url=m.group(1),m.group(2)
            content=inline(label,font,source_links)
            if url.startswith(('https://','http://')):
                out.append(f'<link href="{html.escape(url,quote=True)}" color="#176B70">{content}</link>')
            else:
                out.append(content)
        elif m.group(3) is not None:
            out.append('<font name="AtlasBold">'+inline(m.group(3),'AtlasBold',source_links)+'</font>')
        elif m.group(4) is not None:
            out.append('<font name="AtlasItalic">'+inline(m.group(4),'AtlasItalic',source_links)+'</font>')
        elif m.group(5) is not None:
            out.append(math_text(m.group(5),font))
        else:
            label='S'+m.group(6)+(m.group(7) or '')
            s=glyph_text(label,font)
            out.append(f'<link href="#AD-S{m.group(6)}" color="#176B70">[{s}]</link>' if source_links else '['+s+']')
        cursor=m.end()
    out.append(math_text(text[cursor:],font))
    return ''.join(out)


def make_styles():
    common=dict(fontName='Atlas',fontSize=10.4,leading=14.5,textColor=NAVY,spaceAfter=7,allowWidows=0,allowOrphans=0)
    body=ParagraphStyle('Body',**common)
    return {
        'body':body,
        'small':ParagraphStyle('Small',parent=body,fontSize=9.5,leading=13,textColor=GRAY),
        'label':ParagraphStyle('Label',parent=body,fontName='AtlasBold',fontSize=9.5,leading=13,textColor=TEAL,spaceAfter=8),
        'field':ParagraphStyle('Field',parent=body,fontName='AtlasBold',fontSize=20,leading=24,spaceAfter=12,keepWithNext=1),
        'chapter':ParagraphStyle('Chapter',parent=body,fontName='AtlasBold',fontSize=25,leading=30,spaceAfter=18,keepWithNext=1),
        'h2':ParagraphStyle('H2',parent=body,fontName='AtlasBold',fontSize=14,leading=18,spaceBefore=10,spaceAfter=9,keepWithNext=1),
        'bullet':ParagraphStyle('Bullet',parent=body,leftIndent=12,firstLineIndent=-12),
        'seed':ParagraphStyle('Seed',parent=body,leftIndent=0,spaceBefore=2,spaceAfter=10),
        'table':ParagraphStyle('Table',parent=body,fontSize=10,leading=13,spaceAfter=0),
        'cover':ParagraphStyle('Cover',parent=body,fontName='AtlasBold',fontSize=36,leading=42,spaceAfter=22),
        'cover_sub':ParagraphStyle('CoverSub',parent=body,fontSize=18,leading=25,spaceAfter=24),
    }


class AtlasDoc(BaseDocTemplate):
    def __init__(self, filename, **kw):
        super().__init__(filename,pagesize=PAGE,leftMargin=LEFT,rightMargin=RIGHT,topMargin=TOP,bottomMargin=BOTTOM,**kw)
        frame=Frame(LEFT,BOTTOM,WIDTH,PAGE[1]-TOP-BOTTOM,leftPadding=0,rightPadding=0,topPadding=0,bottomPadding=0)
        self.addPageTemplates(PageTemplate(id='Atlas',frames=frame,onPage=self.decorate))
        self.page_map={}

    def beforeDocument(self):
        self.page_map={}

    def decorate(self, canvas, doc):
        canvas.saveState()
        if doc.page>1:
            canvas.setStrokeColor(colors.HexColor('#CBDCDE'));canvas.setLineWidth(.45)
            canvas.line(LEFT,764,PAGE[0]-RIGHT,764)
            canvas.setFont('Atlas',8.2);canvas.setFillColor(GRAY)
            canvas.drawString(LEFT,773,'MATHEMATICS ATLAS  /  RESEARCH MAP')
        canvas.setFont('Atlas',8.4);canvas.setFillColor(GRAY)
        canvas.drawString(LEFT,25,'Atlas map v1  |  25 September 2026')
        canvas.drawRightString(PAGE[0]-RIGHT,25,str(doc.page))
        canvas.restoreState()

    def afterFlowable(self,flowable):
        if hasattr(flowable,'atlas_key'):
            key=flowable.atlas_key;title=flowable.atlas_title;level=flowable.atlas_level
            self.canv.bookmarkPage(key)
            self.canv.addOutlineEntry(title,key,level=level,closed=False)
            self.notify('TOCEntry',(level,html.escape(title),self.page,key))
            self.page_map[key]={'title':title,'page':self.page,'level':level}


def heading(title,key,level,styles,style='chapter'):
    p=Paragraph(inline(title,'AtlasBold'),styles[style])
    p.atlas_key=key;p.atlas_title=normalize(title);p.atlas_level=level
    return p


def table_from_rows(rows,styles,widths=None):
    data=[[Paragraph(inline(c,'AtlasBold' if i==0 else 'Atlas'),styles['table'])for c in row]for i,row in enumerate(rows)]
    t=Table(data,colWidths=widths or [WIDTH/len(rows[0])]*len(rows[0]),repeatRows=1,hAlign='LEFT')
    t.setStyle(TableStyle([
        ('BACKGROUND',(0,0),(-1,0),PALE),('VALIGN',(0,0),(-1,-1),'TOP'),
        ('LEFTPADDING',(0,0),(-1,-1),7),('RIGHTPADDING',(0,0),(-1,-1),7),
        ('TOPPADDING',(0,0),(-1,-1),7),('BOTTOMPADDING',(0,0),(-1,-1),7),
        ('LINEBELOW',(0,0),(-1,0),.6,TEAL),('LINEBELOW',(0,1),(-1,-1),.3,colors.HexColor('#DFE6E8')),
    ]))
    return t


def render_blocks(text,styles,field=None,source_links=False,seed_seen=None):
    story=[];lines=text.strip().splitlines();i=0
    while i<len(lines):
        line=lines[i].strip()
        if not line:i+=1;continue
        if line.startswith('|'):
            rows=[]
            while i<len(lines) and lines[i].strip().startswith('|'):
                cells=[c.strip() for c in lines[i].strip().strip('|').split('|')]
                if not all(re.fullmatch(r'[-: ]+',c)for c in cells):rows.append(cells)
                i+=1
            widths=[115,205,196] if len(rows[0])==3 else None
            story.append(table_from_rows(rows,styles,widths));story.append(Spacer(1,10));continue
        if line.startswith('#'):
            title=re.sub(r'^#+\s*','',line)
            story.append(Paragraph(inline(title,'AtlasBold',source_links),styles['h2']));i+=1;continue
        para=[line];i+=1
        is_list=bool(re.match(r'^(\d+\.|-)\s+',line))
        while i<len(lines) and lines[i].strip() and not lines[i].startswith('#'):
            if lines[i].startswith('|') or re.match(r'^(\d+\.|-)\s+',lines[i]):break
            para.append(lines[i].strip());i+=1
        block=' '.join(para)
        if field and block.startswith('**Anchors.**'):
            parts=re.split(r'\((\d+)\) ',block)
            intro=parts[0].replace('**Anchors.**','').strip()
            story.append(Paragraph('<font name="AtlasBold">Question seeds.</font> '+inline(intro,source_links=source_links),styles['body']))
            for j in range(1,len(parts),2):
                sid=f'{field}-S{int(parts[j]):02}'
                seed_seen.add(sid)
                story.append(Paragraph(f'<font name="AtlasBold" color="#176B70">{sid}</font>  '+inline(parts[j+1].strip(),source_links=source_links),styles['seed']))
            continue
        m=re.match(r'^(\d+)\.\s+(.+)',block)
        if m and field:
            sid=f'{field}-S{int(m.group(1)):02}';seed_seen.add(sid)
            story.append(Paragraph(f'<font name="AtlasBold" color="#176B70">{sid}</font>  '+inline(m.group(2),source_links=source_links),styles['seed']))
        elif block.startswith('- '):
            anchor=''
            sm=re.match(r'- \*\*S(\d+)\.\*\*',block)
            if sm:anchor=f'<a name="AD-S{sm.group(1)}"/>'
            story.append(Paragraph(anchor+'- '+inline(block[2:],source_links=source_links),styles['bullet']))
        else:
            story.append(Paragraph(inline(block,source_links=source_links),styles['body']))
    return story


def build(output,qa):
    register_fonts();styles=make_styles();story=[]
    inventory=json.loads((ATLAS/'inventory.json').read_text())
    seeds=json.loads((ATLAS/'problem-seeds.json').read_text())
    coverage={r['code']:r for r in csv.DictReader((ATLAS/'field-coverage.csv').open())}
    seed_counts=Counter(s['field']for s in seeds);seed_seen=set()
    # Cover / scope: three different kinds of counts, explicitly not a funnel.
    story += [Spacer(1,58),Paragraph('MATHEMATICS ATLAS',styles['label']),
        Paragraph('Research map',styles['cover']),
        Paragraph('Interesting mathematics, faithful entrances,<br/>and the questions still ahead.',styles['cover_sub']),
        Spacer(1,20)]
    story.append(table_from_rows([
        ['63','231','90'],['field dossiers','surveyed question seeds','facilitator planning cards']],styles,[172]*3))
    story += [Spacer(1,25),Paragraph('First breadth edition  /  map v1<br/>25 September 2026',styles['body']),
        Paragraph('This volume preserves all three research surveys and their source locators. The companion volume contains the 90 reviewed planning records. These counts describe different layers of the library; they are not counts of elementary sessions or completed research subjects.',styles['body']),
        Paragraph('<link href="math-atlas-investigation-plans.pdf" color="#176B70">Companion volume: Mathematics atlas - investigation plans</link>',styles['body']),
        Paragraph('Prepared for the Lowell Math Circle library in Bellingham. Capability prerequisites replace fixed grade placement. No new atlas activity is represented as classroom-piloted.',styles['small']),PageBreak()]
    story.append(heading('Contents','contents',0,styles))
    story.append(Paragraph('Field headings are linked. Use PDF bookmarks to move directly between the map, the 63 dossiers, source notes, and the frontier. Each seed has a stable field-based ID; planning-card IDs are shown beside their primary field.',styles['body']))
    toc=TableOfContents()
    toc.levelStyles=[
        ParagraphStyle('TOC0',fontName='AtlasBold',fontSize=10.5,leading=15,spaceBefore=9,textColor=NAVY,leftIndent=0,firstLineIndent=0),
        ParagraphStyle('TOC1',fontName='Atlas',fontSize=10,leading=14,spaceBefore=4,leftIndent=12,firstLineIndent=0,textColor=NAVY),
    ]
    story.append(toc);story.append(PageBreak())
    story.append(heading('Reading this map','reading',0,styles))
    scope='''The atlas begins with an adult mathematical question and searches for a faithful investigation at an explicit prerequisite level. A finite special case can be real mathematics without exhausting its field. Some worthwhile entrances require complex numbers, matrices, calculus, or university-level definitions; those gates remain visible.

The 63 dossiers are a complete top-level breadth pass through the pinned MSC snapshot. Their 231 numbered seeds are provisional research proposals, not a de-duplicated count of mechanisms. The companion 90 cards are a selected and expanded planning library: 24 algebra/discrete, 36 geometry/analysis, and 30 probability/application records. They represent all 60 substantive top-level fields as primary topics. Fields 00, 01, and 97 have supporting dossiers.

The surveys are retained as screening records. References in them to future family design or to work not yet completed describe that research stage. Family-level mathematical/editorial review and repairs have since been recorded separately. Agent review does not establish classroom suitability, and none of the new atlas families has classroom evidence.

All 534 subareas, 5,503 ordinary subject entries, and 503 cross-cutting entries remain individually unvisited. Top-level representation gives them no inherited coverage. A source contents page supports scope; inspected relevant text or a self-contained proof is needed to support a particular theorem. Failed retrievals, excerpt-only access, and older editions remain visible in the dossiers.

The low entrances are proposals, not promises about age. Reading may be supplied orally; arithmetic, spatial tracking, abstraction, and proof may develop independently. A satisfying early stop need not reach the most advanced theorem. For an actual meeting, use the companion planning card rather than treating a research seed as a finished session.

MSC2020 is jointly published by Mathematical Reviews and zbMATH. The pinned classification and classification-derived coverage are licensed [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/). The atlas is an independent selection and educational design, without endorsement by those publishers. Cited mathematical works retain their own rights. The snapshot is the official [MSC2020 download](https://msc2020.org/MSC_2020.csv), retrieved 25 September 2026; its actual finer-level counts differ from the original landing-page totals.'''
    story += render_blocks(scope,styles)
    story.append(table_from_rows([
        ['Layer','Extent','Meaning'],
        ['Top-level fields','63 dossiers','Screened; 60 primary content fields plus 3 support fields'],
        ['Research seeds','231','Full seed text printed in its field dossier'],
        ['Investigation plans','90','Reviewed planning records in the companion book'],
        ['Taxonomy descendants','6,540 rows','All individually unvisited; no inherited coverage'],
        ['Classroom pilots','0','No claimed evidence of use for new atlas designs'],
    ],styles,[125,98,293]))
    story.append(PageBreak())
    story.append(heading('Map lock and coverage contract','map-lock',0,styles))
    locked=(ATLAS/'MAP-LOCK.md').read_text()
    story+=render_blocks(re.sub(r'^# [^\n]+\n','',locked),styles)
    for slug,title,part in SURVEYS:
        source=(ATLAS/'surveys'/f'{slug}.md').read_text()
        chunks=re.split(r'^## ([^\n]+)\n',source,flags=re.M)
        story.append(PageBreak());story.append(Paragraph(part.upper(),styles['label']))
        story.append(heading(title,slug,0,styles))
        story+=render_blocks(re.sub(r'^# [^\n]+\n','',chunks[0]),styles,source_links=slug=='algebra-discrete')
        for i in range(1,len(chunks),2):
            title2,body=chunks[i:i+2]
            field_match=re.match(r'^(\d\d)\s*[-—–:]\s*(.*)',title2)
            story.append(PageBreak())
            if field_match:
                code,field_title=field_match.groups();row=coverage[code]
                families=row['family_ids'] or 'support dossier'
                story.append(Paragraph(f'FIELD {code}  |  {seed_counts[code]} SURVEYED SEEDS  |  {families}',styles['label']))
                story.append(heading(f'{code}  {field_title}',f'field-{code}',1,styles,'field'))
                story+=render_blocks(body,styles,field=code,source_links=slug=='algebra-discrete',seed_seen=seed_seen)
            else:
                key=slug+'-'+re.sub(r'[^a-z0-9]+','-',title2.lower()).strip('-')
                story.append(heading(title2,key,1,styles,'field'))
                story+=render_blocks(body,styles,source_links=slug=='algebra-discrete')
    story.append(PageBreak());story.append(heading('The next research frontier','frontier',0,styles))
    story+=render_blocks(re.sub(r'^# [^\n]+\n','',(ATLAS/'FRONTIER.md').read_text()),styles)
    expected={s['id']for s in seeds}
    assert seed_seen==expected,(sorted(expected-seed_seen),sorted(seed_seen-expected))
    if MISSING:raise RuntimeError(f'Unsupported glyphs: {dict(MISSING)}')
    output.parent.mkdir(parents=True,exist_ok=True);qa.mkdir(parents=True,exist_ok=True)
    doc=AtlasDoc(str(output),title='Mathematics atlas - research map',author='Lowell Math Circle atlas project',subject='63 field dossiers and 231 mathematical investigation seeds')
    doc.multiBuild(story)
    reader=PdfReader(output)
    mapping=doc.page_map
    ordered=sorted(mapping.items(),key=lambda kv:kv[1]['page'])
    for j,(key,value)in enumerate(ordered):
        following=next((v for _,v in ordered[j+1:] if v['level']<=value['level']),None)
        value['end_page']=following['page']-1 if following else len(reader.pages)
    meta={'pdf':str(output),'page_count':len(reader.pages),'fields':63,'seeds':len(seed_seen),'companion_families':inventory['family_count'],'bookmarks':mapping,'source_hashes':{str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest()for p in [ATLAS/'MAP-LOCK.md',ATLAS/'FRONTIER.md',ATLAS/'inventory.json',ATLAS/'problem-seeds.json',ATLAS/'field-coverage.csv']+[ATLAS/'surveys'/f'{s[0]}.md'for s in SURVEYS]},'pdf_sha256':hashlib.sha256(output.read_bytes()).hexdigest()}
    (qa/'page-map.json').write_text(json.dumps(meta,ensure_ascii=False,indent=2)+'\n')
    return meta


def qa_and_render(output,qa,meta,dpi=90):
    reader=PdfReader(output)
    pages=[p.extract_text()or''for p in reader.pages]
    combined='\n'.join(pages)
    seed_ids=set(re.findall(r'\b\d\d-S\d\d\b',combined))
    def compact(text):
        text=re.sub(r'\[([^\]]+)\]\([^)]*\)',r'\1',text)
        return ''.join(c.lower()for c in unicodedata.normalize('NFKC',text)if c.isalnum())
    compact_pdf=compact(combined)
    seeds=json.loads((ATLAS/'problem-seeds.json').read_text())
    unmatched=[s['id']for s in seeds if compact(s['anchor'])not in compact_pdf]
    external=[]
    for page in reader.pages:
        for ref in page.get('/Annots',[]):
            annot=ref.get_object();action=annot.get('/A',{})
            if action.get('/URI'):external.append(str(action['/URI']))
    geometry=[]
    with pdfplumber.open(output)as pdf:
        for n,page in enumerate(pdf.pages,1):
            for c in page.chars:
                if c['x0']<LEFT-1 or c['x1']>PAGE[0]-RIGHT+1 or c['top']<10 or c['bottom']>774:
                    geometry.append({'page':n,'text':c['text'],'bbox':[c['x0'],c['top'],c['x1'],c['bottom']]})
    flags={
        'replacement_char':combined.count('\ufffd'),
        'raw_markdown_links':len(re.findall(r'\]\(https?://',combined)),
        'raw_latex_commands':re.findall(r'\\[A-Za-z]+',combined),
        'raw_bold_markers':combined.count('**'),
    }
    assert len(seed_ids)==231,len(seed_ids)
    assert not unmatched,unmatched
    assert len([k for k in meta['bookmarks']if k.startswith('field-')])==63
    assert not any(flags.values()),flags
    assert not geometry,geometry[:12]
    check={'page_count':len(pages),'seed_ids_extracted':len(seed_ids),'full_seed_text_matches':len(seeds)-len(unmatched),'unmatched_seed_texts':unmatched,'field_bookmarks':63,'uri_links':len(external),'unique_uri_links':len(set(external)),'glyph_missing':dict(MISSING),'text_flags':flags,'out_of_bounds_chars':geometry,'min_extracted_page_chars':min(map(len,pages))}
    (qa/'structural-checks.json').write_text(json.dumps(check,indent=2)+'\n')
    (qa/'extracted.txt').write_text(combined)
    rendered=qa/'pages';rendered.mkdir(exist_ok=True)
    contacts=qa/'contact-sheets';contacts.mkdir(exist_ok=True)
    for old in rendered.glob('page-*.png'):old.unlink()
    for old in contacts.glob('contact-*.jpg'):old.unlink()
    subprocess.run(['pdftoppm','-r',str(dpi),'-png',str(output),str(rendered/'page')],check=True)
    images=sorted(rendered.glob('page-*.png'))
    assert len(images)==len(pages)
    font=ImageFont.truetype(str(FONTDIR/'Arial.ttf'),16)
    for start in range(0,len(images),12):
        batch=images[start:start+12];sheet=Image.new('RGB',(1008,4*355),'#dde4e7');draw=ImageDraw.Draw(sheet)
        for j,path in enumerate(batch):
            im=Image.open(path).convert('RGB');im.thumbnail((316,321))
            x=12+(j%3)*332;y=10+(j//3)*355
            sheet.paste(im,(x+(316-im.width)//2,y))
            draw.text((x,y+326),f'Page {start+j+1}',font=font,fill='#183342')
        sheet.save(contacts/f'contact-{start//12+1:02}.jpg',quality=90)
    print(json.dumps({'pdf':str(output),'pages':len(pages),'rendered_pages':str(rendered),'contact_sheets':str(contacts),'checks':check},indent=2))


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path,default=DEFAULT_PDF)
    parser.add_argument('--qa-dir',type=Path,default=DEFAULT_QA)
    parser.add_argument('--no-render',action='store_true',help='Build and map pages without raster QA (development only).')
    parser.add_argument('--dpi',type=int,default=90)
    args=parser.parse_args()
    meta=build(args.output,args.qa_dir)
    if not args.no_render:qa_and_render(args.output,args.qa_dir,meta,args.dpi)
    else:print(json.dumps({'pdf':str(args.output),'pages':meta['page_count']},indent=2))


if __name__=='__main__':
    main()
