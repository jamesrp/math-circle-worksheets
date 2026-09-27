#!/usr/bin/env python3
"""Assemble the ten random student investigations and separate teaching key."""
import argparse
import sys
sys.dont_write_bytecode = True
import importlib
import json
import hashlib
import subprocess
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont
from pypdf import PdfReader
import pdfplumber

from sheet import Book, ROOT, DATA, TMP, NAVY, TEAL, GRAY, PALE, LIGHT

MODULES={
    'GA-26':'geometry','GA-29':'geometry','GA-25':'geometry',
    'GA-11':'systems','AP-26':'systems','AP-07':'systems',
    'AP-23':'decisions','AP-21':'decisions','AP-01':'decisions','AP-29':'decisions',
}
CONTENTS={
    'GA-26':('Can colors detect a knot?','Three colors; careful tracing'),
    'GA-29':('The disappearing strip','Fractions and powers; optional infinite arguments'),
    'GA-11':('What must an addition machine reveal?','Signed fractions and algebra; later, irrational inputs'),
    'AP-26':('The controller remembers yesterday','Signed numbers; fraction/algebra extension'),
    'AP-23':('Everyone chooses a faster road','Small counts, addition and comparisons'),
    'AP-21':('Spend the battery now, or save it?','Small sums; comparing and explaining plans'),
    'GA-25':('Roads, loops and courtyards','Tracing networks; systematic choices'),
    'AP-07':('Can a cooling simulator be trusted?','Derivatives and exponential decay; calculator'),
    'AP-01':('Which shore? How long?','Fractions and fair-coin reasoning'),
    'AP-29':('Give common messages shorter names','Counting, left/right trees and careful decoding'),
}


def front(book,ids,starts=None):
    guide=book.kind=='facilitator'
    book.new_page('TEN INVESTIGATIONS','Facilitator guide' if guide else 'Ten mathematical investigations',
                  'A random sample from the mathematics atlas - September 2026')
    if guide:
        book.p('Give one student page at a time. Let learners try their own examples before offering a hint or a new representation. These are reviewed worksheet trials; classroom pacing is still untested.',y=119,size=11.5)
    else:
        book.p('Choose an investigation whose tools you know. Make things, try ideas, and explain what you notice. You can work with a partner and use scrap paper. A good question can last longer than one meeting.',y=119,size=11.5)
    y=190
    book.label('INVESTIGATION',44,y,size=9,font='CircleBold',color=GRAY)
    book.label('PAGE',568,y,size=9,font='CircleBold',color=GRAY,align='right')
    y+=22
    for fid in ids:
        title,tools=CONTENTS[fid]
        book.label(fid,44,y,size=10,font='CircleBold',color=TEAL)
        book.p(title,x=96,y=y-1,width=430,size=12,font='CircleBold')
        book.p(tools,x=96,y=y+17,width=430,size=10.3,color=GRAY)
        if starts:
            page=starts[fid]
            book.label(str(page),568,y,size=11,color=TEAL,align='right')
            book.c.linkRect('',f'page-{page}',(42,792-y-36,570,792-y+3),relative=0,thickness=0)
        book.line(44,y+38,568,y+38,color=LIGHT,width=.5)
        y+=47
    footer=('Preparation, staged hints, all solutions and source notes follow in the same order. Calculus is a real prerequisite for AP-07, rather than an optional label.' if guide else 'Print selected pages, single-sided. The separate facilitator guide contains answers and hints. Some investigations need algebra or calculus; the tools above are prerequisites, not age labels.')
    book.p(footer,y=max(y+4,692),size=10.2,leading=14)


def make(kind,ids,path,modules):
    starts=None
    for _ in range(2):
        book=Book(path,'Ten random atlas investigations - '+kind,kind=kind)
        front(book,ids,starts)
        now={}
        for fid in ids:
            now[fid]=book.page_no+1
            function=getattr(modules[MODULES[fid]],'render_facilitator' if kind=='facilitator' else 'render_students')
            function(book,fid)
        report=book.save()
        if starts is not None:assert starts==now,'Contents pagination changed'
        starts=now
    report['starts']=starts
    report['sha256']=hashlib.sha256(path.read_bytes()).hexdigest()
    return report


def inspect(path,record):
    reader=PdfReader(path);texts=[];bad=[];suspect=[]
    with pdfplumber.open(path) as pdf:
        for i,page in enumerate(pdf.pages,1):
            texts.append(page.extract_text() or '')
            for ch in page.chars:
                if ch['x0']<25 or ch['x1']>587 or ch['top']<12 or ch['bottom']>783:
                    bad.append(dict(page=i,text=ch['text'],box=[ch['x0'],ch['top'],ch['x1'],ch['bottom']]))
                if any(x in ch['text'] for x in ('\x00','\ufffd','\u25a0')):suspect.append(dict(page=i,text=ch['text']))
    blank=[i+1 for i,t in enumerate(texts) if not t.strip()]
    result=dict(pages=len(reader.pages),blank_pages=blank,out_of_page_chars=bad,suspect_glyphs=suspect,
                text_characters_by_page=[len(t) for t in texts],source_pages=record['page_map'])
    return result,'\n\n'.join(texts)


def render(path,folder,dpi):
    folder.mkdir(parents=True,exist_ok=True)
    for p in folder.glob('page-*.png'):p.unlink()
    subprocess.run(['pdftoppm','-r',str(dpi),'-png',str(path),str(folder/'page')],check=True)
    images=sorted(folder.glob('page-*.png'))
    contact=folder.parent/'contacts';contact.mkdir(exist_ok=True)
    for p in contact.glob('contact-*.jpg'):p.unlink()
    font=ImageFont.truetype('/System/Library/Fonts/Supplemental/Arial.ttf',18)
    for start in range(0,len(images),9):
        sheet=Image.new('RGB',(1110,1485),'#E2E9EB');draw=ImageDraw.Draw(sheet)
        for j,p in enumerate(images[start:start+9]):
            im=Image.open(p).convert('RGB');im.thumbnail((344,446))
            x=12+(j%3)*368;y=10+(j//3)*492
            sheet.paste(im,(x,y));draw.text((x,y+452),f'Page {start+j+1}',font=font,fill='#173747')
        sheet.save(contact/f'contact-{start//9+1:02}.jpg',quality=92)
    return dict(pages=len(images),dpi=dpi,pages_dir=str(folder),contacts_dir=str(contact))


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--only',nargs='+',help='Selected family IDs; development outputs go to tmp')
    parser.add_argument('--no-render',action='store_true')
    parser.add_argument('--dpi',type=int,default=100)
    parser.add_argument('--output-dir',type=Path)
    parser.add_argument('--qa-dir',type=Path,help='Separate render and QA folder for parallel previews')
    args=parser.parse_args()
    sample=json.loads((DATA/'sample.json').read_text())
    ids=args.only or sample['draw_order']
    assert len(set(ids))==len(ids) and all(i in MODULES for i in ids)
    modules={name:importlib.import_module(name) for name in sorted({MODULES[i] for i in ids})}
    out=args.output_dir or (TMP/'preview' if args.only else ROOT/'lowell-math-circle-year-2/combined')
    out.mkdir(parents=True,exist_ok=True)
    qa=args.qa_dir or (out/'qa' if args.only or args.output_dir else TMP)
    qa.mkdir(parents=True,exist_ok=True)
    reports={}
    for kind,filename in [('student','atlas-random-ten-student-worksheets.pdf'),('facilitator','atlas-random-ten-facilitator-guide.pdf')]:
        path=out/filename
        record=make(kind,ids,path,modules)
        checks,text=inspect(path,record)
        directory=qa/kind
        directory.mkdir(parents=True,exist_ok=True)
        (directory/'extracted.txt').write_text(text)
        if not args.no_render:record['render']=render(path,directory/'pages',args.dpi)
        record['checks']=checks
        (directory/'build-report.json').write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n')
        print(kind,'pages',record['pages'],'bounds',len(checks['out_of_page_chars']),'suspect',len(checks['suspect_glyphs']))
        assert not checks['blank_pages'] and not checks['out_of_page_chars'] and not checks['suspect_glyphs'],checks
        reports[kind]=record
    (qa/'build-report.json').write_text(json.dumps(reports,ensure_ascii=False,indent=2)+'\n')


if __name__=='__main__':main()
