#!/usr/bin/env python3
"""Check delivered vectors; copy-source and ZIP-extracted builds must agree."""
import argparse
import hashlib
import json
import re
from pathlib import Path
import shutil
import subprocess
import sys
import zipfile
import pymupdf as fitz

UNIT=20*72/25.4
TOL=.015  # points; covers TeX's unit conversion rounding, under .006 mm.


def close(p,q):
    return abs(p[0]-q[0])<TOL and abs(p[1]-q[1])<TOL


def dot_centers(page):
    result=[]
    for d in page.get_drawings():
        r=d['rect']
        if d['type']=='f' and d.get('fill')==(0,0,0) and abs(r.width-1.1*72/25.4)<TOL and abs(r.height-1.1*72/25.4)<TOL:
            result.append(((r.x0+r.x1)/2,(r.y0+r.y1)/2))
    return result


def edges(d):
    result=[]
    for item in d['items']:
        if item[0]=='l': result.append((tuple(item[1]),tuple(item[2])))
        elif item[0]=='re':
            r=item[1];v=[(r.x0,r.y0),(r.x1,r.y0),(r.x1,r.y1),(r.x0,r.y1)]
            result.extend(zip(v,v[1:]+v[:1]))
        else: raise AssertionError(('unexpected polygon primitive',item))
    return result


def check_loop(poly,d,all_dots):
    actual_edges=edges(d)
    assert len(actual_edges)==len(poly),(len(actual_edges),len(poly))
    actual_points=[a for a,b in actual_edges]
    minpx=min(x for x,y in actual_points);maxpy=max(y for x,y in actual_points)
    minx=min(x for x,y in poly);miny=min(y for x,y in poly)
    origin=(minpx-minx*UNIT,maxpy+miny*UNIT)
    projected=[(origin[0]+x*UNIT,origin[1]-y*UNIT) for x,y in poly]
    assert all(any(close(a,b) for b in actual_points) for a in projected)
    wanted=list(zip(projected,projected[1:]+projected[:1]))
    assert all(any((close(a,c) and close(b,e)) or (close(a,e) and close(b,c)) for c,e in actual_edges) for a,b in wanted)
    assert all(any(close(v,p) for p in all_dots) for v in projected)
    return origin


def figures_check(pdf,cases):
    doc=fitz.open(pdf);assert len(doc)==10
    result=[]
    for page_number,page in enumerate(doc,1):
        assert tuple(page.rect)==(0,0,612,792)
        text=page.get_text()
        band='Grades 3–5' if page_number<=6 else 'Grades 4–5'
        assert f'Week 57 / Area from dots / {band}' in text
        assert f'Problem {page_number}:' in text
        assert re.findall(r'Problem \d+:',text)==[f'Problem {page_number}:']
        assert 'Bellingham Math Circle / Week 57 / N57-S-final-v2' in text
        assert 'Name' not in text and 'Date' not in text
        for block in page.get_text('blocks'):
            assert block[0]>=40 and block[2]<=572 and block[1]>=20 and block[3]<=778,block
        outlines=[d for d in page.get_drawings() if d.get('color') and all(abs(a-b)<.001 for a,b in zip(d['color'],(.12,.16,.20)))]
        page_cases=[(k,c) for k,c in cases.items() if c.get('draw',True) and c.get('page')==page_number]
        assert len(outlines)==sum(1+len(c.get('holes',[])) for k,c in page_cases)
        dots=dot_centers(page);used=[];cursor=0;figures=[]
        for name,case in page_cases:
            origin=check_loop(case['vertices'],outlines[cursor],dots);cursor+=1
            for hole in case.get('holes',[]):
                hole_origin=check_loop(hole,outlines[cursor],dots);cursor+=1
                assert close(origin,hole_origin),(name,'hole relative position')
            for a,b in case.get('seams',[]):
                a=(origin[0]+a[0]*UNIT,origin[1]-a[1]*UNIT)
                b=(origin[0]+b[0]*UNIT,origin[1]-b[1]*UNIT)
                dashed=[d for d in page.get_drawings() if d.get('dashes') and d['dashes']!='[] 0' and len(d['items'])==1 and d['items'][0][0]=='l']
                assert any((close(a,tuple(d['items'][0][1])) and close(b,tuple(d['items'][0][2]))) or (close(a,tuple(d['items'][0][2])) and close(b,tuple(d['items'][0][1]))) for d in dashed),(name,'seam geometry')
            w,h=case['board']
            target=[(origin[0]+x*UNIT,origin[1]-y*UNIT) for x in range(w+1) for y in range(h+1)]
            assert all(any(close(v,p) for p in dots) for v in target),(name,'missing lattice dot')
            used.extend(target)
            figures.append(dict(name=name,outer_sides=case['sides'],hole_sides=case.get('hole_sides',[]),board_dots=(w+1)*(h+1),x_spacing_mm=20,y_spacing_mm=20))
        rest=[p for p in dots if not any(close(p,v) for v in used)]
        expected={3:(2,5,5),4:(1,7,7),5:(1,7,7),7:(1,7,7),9:(1,7,4),10:(1,7,7)}.get(page_number,(0,0,0))
        count,columns,rows=expected
        assert len(rest)==count*columns*rows,(page_number,len(rest),expected)
        if count:
            # Every blank board is an exact rectangular lattice at the same unit.
            remaining=list(rest)
            for _ in range(count):
                x0=min(x for x,y in remaining);y0=min(y for x,y in remaining if abs(x-x0)<TOL)
                target=[(x0+x*UNIT,y0+y*UNIT) for x in range(columns) for y in range(rows)]
                assert all(any(close(v,p) for p in remaining) for v in target),(page_number,'blank board geometry')
                remaining=[p for p in remaining if not any(close(p,v) for v in target)]
            assert not remaining
        result.append(dict(page=page_number,band=band,figures=figures,blank_boards=count,all_dots_checked=len(dots)))
    return result


def signature(pdf):
    doc=fitz.open(pdf)
    return [dict(text=p.get_text(),dimensions=list(p.rect),pixels=hashlib.sha256(p.get_pixmap(matrix=fitz.Matrix(2,2),alpha=False).samples).hexdigest()) for p in doc]


def main():
    p=argparse.ArgumentParser();p.add_argument('--pdf',required=True);p.add_argument('--qa-dir',required=True);args=p.parse_args()
    source=Path(__file__).resolve().parent
    qa=Path(args.qa_dir).resolve();qa.mkdir(parents=True,exist_ok=True)
    original=Path(args.pdf).resolve()
    cases=json.loads((source/'assets'/'polygons.json').read_text())
    geometry=figures_check(original,cases)
    author_files=[path for path in source.rglob('*') if path.is_file() and '__pycache__' not in path.parts and path.suffix in ('.py','.tex','.json','.md')]
    assert all(path.name not in ('PROMPT.md','CRITIC.md','CRITIC-MATH.md','REVISE.md','exemplars.md') for path in author_files)
    copied=qa/'copied-source';extracted=qa/'zip-extracted-source'
    for dest in (copied,extracted):
        if dest.exists(): shutil.rmtree(dest)
        dest.mkdir()
    for path in author_files:
        dest=copied/path.relative_to(source);dest.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(path,dest)
    archive=qa/'week-57-final-source-qa.zip'
    with zipfile.ZipFile(archive,'w',compression=zipfile.ZIP_DEFLATED) as z:
        for path in author_files: z.write(path,Path('week-57-final-source')/path.relative_to(source))
    with zipfile.ZipFile(archive) as z: z.extractall(extracted)
    baseline=signature(original);compared=[]
    for name,src in [('copied',copied),('zip-extracted',extracted/'week-57-final-source')]:
        dest=qa/f'{name}-build'
        subprocess.run([sys.executable,str(src/'build.py'),'--output-dir',str(dest)],check=True,capture_output=True,text=True)
        rebuilt=signature(dest/'students.pdf')
        assert rebuilt==baseline,(name,'text, page dimensions, or 144-dpi pixels differ')
        compared.append(dict(kind=name,page_count=len(rebuilt),text_equal=True,dimensions_equal=True,all_page_pixels_equal=True))
    render=qa/'rendered';render.mkdir(exist_ok=True)
    doc=fitz.open(original)
    for n,page in enumerate(doc,1):page.get_pixmap(matrix=fitz.Matrix(1.25,1.25),alpha=False).save(render/f'page-{n:02d}.png')
    report=dict(pages=10,page_checks=geometry,portable_source_files=[str(p.relative_to(source)) for p in sorted(author_files)],portable_build_checks=compared,pixel_check_dpi=144,physical_fit='unperformed',classroom_piloting='unperformed')
    (qa/'pdf-checks.json').write_text(json.dumps(report,indent=2)+'\n')
    print('Verified every outline edge/side count and every 20 mm lattice dot; copied-source and ZIP-extracted builds match all 10 pages in text, dimensions, and rendered pixels.')


if __name__=='__main__':main()
