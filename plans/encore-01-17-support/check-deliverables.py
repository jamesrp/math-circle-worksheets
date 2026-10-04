#!/usr/bin/env python3
"""Inventory final companions and render every page for a root QA pass.

Run from repo root using a Python environment with PyMuPDF and Pillow.
This records digital observations only; it does not assert classroom or material fit tests.
"""
from pathlib import Path
import json,re,hashlib
import pymupdf
from PIL import Image,ImageDraw
ROOT=Path(__file__).resolve().parents[2]
OUT=ROOT/'tmp/encore-01-17-final-qa';OUT.mkdir(parents=True,exist_ok=True)
records=[]
for n in range(1,18):
    for suffix in ('','-facilitator'):
        p=ROOT/f'lowell-math-circle-year-2/week-{n:02}/week-{n:02}-return-visit{suffix}.pdf'
        if not p.exists():continue
        pages=[];images=[];problem_numbers=[]
        for i,page in enumerate(pymupdf.open(p)):
            text=page.get_text();numbers=[int(k) for k in re.findall(r'Problem\s+(\d+)(?:\s*\(continued\))?\s*:',text)]
            problem_numbers.extend(numbers)
            bad=[]
            for b in page.get_text('blocks'):
                x0,y0,x1,y1=b[:4]
                if x0<0 or y0<0 or x1>page.rect.width+.1 or y1>page.rect.height+.1:bad.append(b[:4])
            png=OUT/f'{p.stem}-p{i+1:02}.png'
            page.get_pixmap(matrix=pymupdf.Matrix(1.2,1.2),alpha=False).save(png)
            images.append(png)
            pages.append({'page':i+1,'problems':numbers,'bounds':list(page.rect),'out_of_page_text_blocks':bad,'replacement_character':'\ufffd' in text,'footer_present':f'Bellingham Math Circle' in text,'header_present':bool(re.search(r'Week\s+\d+\s*/',text)),'text_characters':len(text)})
        sheet=Image.new('RGB',(612*min(3,len(images)),820*((len(images)+2)//3)),(236,238,239));draw=ImageDraw.Draw(sheet)
        for i,png in enumerate(images):
            img=Image.open(png);img.thumbnail((596,772));x=612*(i%3)+8;y=820*(i//3)+26
            sheet.paste(img,(x,y));draw.text((x,y-18),f'{p.stem} p{i+1}',fill=(0,0,0))
        contact=OUT/f'{p.stem}-contact.jpg';sheet.save(contact,quality=91)
        records.append({'week':n,'kind':'facilitator' if suffix else 'student','path':str(p.relative_to(ROOT)),'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'pages':pages,'problem_numbers':problem_numbers,'contact':str(contact.relative_to(ROOT))})
summary={'status':'digital_check_results_require_visual_review','companions_found':len(records),'expected_companions':34,'student_numbered_problem_counts':{str(r['week']):len(set(r['problem_numbers'])) for r in records if r['kind']=='student'},'files':records}
(ROOT/'plans/encore-01-17-support/deliverable-qa.json').write_text(json.dumps(summary,indent=2)+'\n')
print(json.dumps({k:v for k,v in summary.items() if k!='files'},indent=2))
print('Text outside page:',[(r['week'],r['kind'],p['page']) for r in records for p in r['pages'] if p['out_of_page_text_blocks']])
print('Bad glyphs:',[(r['week'],r['kind'],p['page']) for r in records for p in r['pages'] if p['replacement_character']])
print('Suspiciously empty pages:',[(r['week'],r['kind'],p['page']) for r in records for p in r['pages'] if p['text_characters']<100])
