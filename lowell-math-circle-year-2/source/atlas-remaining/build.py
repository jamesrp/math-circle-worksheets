#!/usr/bin/env python3
"""Build the remaining eighty investigations, or a single author's preview."""
import sys
sys.dont_write_bytecode=True
import argparse
import importlib
import json
import hashlib
import subprocess
from pathlib import Path
from collections import Counter
import pdfplumber
from pypdf import PdfReader
from PIL import Image,ImageDraw,ImageFont
from sheet import Book,ROOT,DATA,TMP,BOLD,TEAL,GRAY,LIGHT
from common import render_facilitator

NAMES={
    'algebra-discrete':'Algebra and discrete mathematics',
    'geometry-analysis':'Geometry and analysis',
    'applied-probability':'Probability and applications',
}
FILES={
    'algebra-discrete':'algebra-discrete',
    'geometry-analysis':'geometry-analysis',
    'applied-probability':'probability-applications',
}
REQUIRED=['id','title','core_gate','extension_gate','reading','materials','prep_minutes',
          'timing','launch','satisfying_stop','prior_use','assessment','mathematical_connection',
          'sources','pages','extensions']


def load_families(ids,assignments):
    families={};modules={}
    for batch in sorted({assignments[fid] for fid in ids}):
        data=json.loads((DATA/f'{batch}-data.json').read_text())
        assert data['batch']==batch
        rows=data['families']
        expected={fid for fid,b in assignments.items() if b==batch}
        assert len(rows)==len(expected) and {f['id'] for f in rows}==expected,(batch,'Wrong family set')
        modules[batch]=importlib.import_module(batch)
        for f in rows:
            assert all(k in f for k in REQUIRED),(f['id'],'Missing data fields')
            prompts=[p for page in f['pages'] for p in page['prompts']]
            assert prompts and f['sources'] and len(f['pages'])>=2
            assert len({str(p['id']) for p in prompts})==len(prompts),(f['id'],'Duplicate task ID')
            for p in prompts:
                assert all(k in p for k in ['id','text','solution','hints']),(f['id'],p)
                assert p['text'].strip() and p['solution'].strip()
            for source in f['sources']:
                assert all(source.get(k) for k in ['title','url','locator','adaptation','checked']),(f['id'],source)
            families[f['id']]=f
    return families,modules


def contents(book,title,ids,families,starts=None):
    per_page=8
    for offset in range(0,len(ids),per_page):
        first=offset==0
        book.new_page('ATLAS / CONTENTS',title if first else 'Contents continued',
                      ('Student investigations' if book.kind=='student' else 'Facilitator guide and complete solutions')+
                      ' / Remaining atlas entries / September 2026')
        intro=('Choose an investigation whose tools you know. Make things, try ideas and explain what you notice. '
               'Use scrap paper or work with a partner. Later pages can be another meeting.' if book.kind=='student' else
               'Give one student page at a time; allow exploration before hints. The accompanying check programs verify finite instances and identities. '
               'General statements need the arguments or supplied facts in the keys. Preparation, timing and classroom engagement remain untested.')
        book.p(intro if first else 'The listed tools are prerequisite gates, not age labels. More detailed gates appear in the facilitator guide.',y=120,size=11.3)
        y=190
        for fid in ids[offset:offset+per_page]:
            f=families[fid]
            book.label(fid,44,y,size=10,font=BOLD,color=TEAL)
            book.p(f['title'],x=96,y=y-1,width=421,size=11.6,font=BOLD,leading=14)
            gate=f.get('index_gate',f['core_gate'])
            if len(gate)>115:gate=gate[:112].rsplit(' ',1)[0]+'...'
            book.p(gate,x=96,y=y+28,width=421,size=9.7,leading=12,color=GRAY)
            if starts:
                pn=starts[fid];book.label(str(pn),568,y,size=11,align='right',color=TEAL)
                book.c.linkRect('',f'page-{pn}',(42,792-y-55,570,792-y+3),relative=0,thickness=0)
            book.line(44,y+57,568,y+57,color=LIGHT,width=.5)
            y+=60
        book.p('Print selected pages, single-sided, on US Letter at actual size. Keep student pages and solutions separate. '
               'The original random-ten book remains a separate volume.',y=max(690,y+10),size=10.2,leading=14)


def make(kind,title,ids,path,families,modules,assignments):
    starts=None
    for _ in range(2):
        book=Book(path,title+' / '+kind,kind=kind)
        contents(book,title,ids,families,starts)
        current={}
        for fid in ids:
            current[fid]=book.page_no+1
            module=modules[assignments[fid]]
            if kind=='student':module.render_students(book,fid)
            else:render_facilitator(book,families[fid],module)
        rec=book.save()
        if starts is not None:assert starts==current,'Unstable contents pagination'
        starts=current
    rec['starts']=starts
    rec['sha256']=hashlib.sha256(path.read_bytes()).hexdigest()
    if kind=='student':
        expected=Counter((fid,str(p['id'])) for fid in ids for page in families[fid]['pages'] for p in page['prompts'])
        actual=Counter((p['family_id'],p['prompt_id']) for p in rec['printed_tasks'])
        assert actual==expected,dict(missing=list((expected-actual).elements()),extra=list((actual-expected).elements()))
        for fid in ids:
            n=sum(p['family_id']==fid for p in rec['page_map'])
            assert n==len(families[fid]['pages']),(fid,n,len(families[fid]['pages']))
    return rec


def inspect(path):
    bad=[];suspect=[];texts=[]
    with pdfplumber.open(path) as pdf:
        for i,page in enumerate(pdf.pages,1):
            texts.append(page.extract_text() or '')
            for ch in page.chars:
                if ch['x0']<25 or ch['x1']>587 or ch['top']<12 or ch['bottom']>783:
                    bad.append(dict(page=i,text=ch['text'],box=[ch['x0'],ch['top'],ch['x1'],ch['bottom']]))
                if any(c in ch['text'] for c in ['\x00','\ufffd','\u25a0']):suspect.append(dict(page=i,text=ch['text']))
    return dict(pages=len(texts),blank_pages=[i+1 for i,t in enumerate(texts) if not t.strip()],
                out_of_page_chars=bad,suspect_glyphs=suspect,text_characters_by_page=[len(t) for t in texts]),'\n\n'.join(texts)


def render(path,directory,dpi):
    pages=directory/'pages';pages.mkdir(parents=True,exist_ok=True)
    for p in pages.glob('page-*.png'):p.unlink()
    subprocess.run(['pdftoppm','-r',str(dpi),'-png',str(path),str(pages/'page')],check=True)
    images=sorted(pages.glob('page-*.png'));contact=directory/'contacts';contact.mkdir(exist_ok=True)
    for p in contact.glob('contact-*.jpg'):p.unlink()
    font=ImageFont.truetype('/System/Library/Fonts/Supplemental/Arial.ttf',18)
    for start in range(0,len(images),9):
        canvas=Image.new('RGB',(1110,1485),'#E2E9EB');draw=ImageDraw.Draw(canvas)
        for j,path in enumerate(images[start:start+9]):
            im=Image.open(path).convert('RGB');im.thumbnail((344,446));x=12+(j%3)*368;y=10+(j//3)*492
            canvas.paste(im,(x,y));draw.text((x,y+452),f'Page {start+j+1}',font=font,fill='#173747')
        canvas.save(contact/f'contact-{start//9+1:02}.jpg',quality=92)
    return dict(pages=len(images),dpi=dpi,pages_dir=str(pages),contacts_dir=str(contact))


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--batch',nargs='+')
    parser.add_argument('--only',nargs='+')
    parser.add_argument('--group',choices=list(NAMES))
    parser.add_argument('--output-dir',type=Path)
    parser.add_argument('--qa-dir',type=Path)
    parser.add_argument('--dpi',type=int,default=100)
    parser.add_argument('--no-render',action='store_true')
    args=parser.parse_args()
    scope=json.loads((DATA/'scope.json').read_text())
    assignments={fid:b['batch'] for g in scope['groups'].values() for b in g['batches'] for fid in b['ids']}
    batch_ids={b['batch']:b['ids'] for g in scope['groups'].values() for b in g['batches']}
    preview=bool(args.batch or args.only)
    if preview:
        ids=args.only or [fid for b in args.batch for fid in batch_ids[b]]
        assert ids and len(set(ids))==len(ids) and all(fid in assignments for fid in ids)
        slug='-'.join(args.batch) if args.batch else '-'.join(ids).lower()
        volumes={slug:('Atlas investigation preview',ids)}
    else:
        volumes={g:(NAMES[g],[fid for b in v['batches'] for fid in b['ids']]) for g,v in scope['groups'].items() if not args.group or args.group==g}
    out=args.output_dir or (TMP/'preview' if preview else ROOT/'lowell-math-circle-year-2/combined')
    out.mkdir(parents=True,exist_ok=True)
    qa=args.qa_dir or (out/'qa' if preview or args.output_dir else TMP)
    qa.mkdir(parents=True,exist_ok=True)
    all_reports={}
    for slug,(title,ids) in volumes.items():
        families,modules=load_families(ids,assignments);reports={}
        for kind in ['student','facilitator']:
            suffix='student-worksheets' if kind=='student' else 'facilitator-guide'
            path=out/f'atlas-{FILES.get(slug,slug)}-{suffix}.pdf'
            record=make(kind,title,ids,path,families,modules,assignments)
            checks,text=inspect(path);record['checks']=checks
            directory=qa/kind if preview else qa/slug/kind
            directory.mkdir(parents=True,exist_ok=True)
            (directory/'extracted.txt').write_text(text)
            if not args.no_render:record['render']=render(path,directory,args.dpi)
            (directory/'build-report.json').write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n')
            print(slug,kind,'pages',record['pages'],'bounds',len(checks['out_of_page_chars']),'glyphs',len(checks['suspect_glyphs']),flush=True)
            assert not checks['blank_pages'] and not checks['out_of_page_chars'] and not checks['suspect_glyphs'],checks
            reports[kind]=record
        all_reports[slug]=reports
    (qa/'build-report.json').write_text(json.dumps(all_reports,ensure_ascii=False,indent=2)+'\n')


if __name__=='__main__':main()
