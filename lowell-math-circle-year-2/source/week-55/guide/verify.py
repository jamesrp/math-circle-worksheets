#!/usr/bin/env python3
"""Fresh guide checks, with no imports from any student, research or reviewer code."""
import argparse
from collections import Counter
import hashlib
from itertools import combinations
import json
from pathlib import Path
import shutil
import subprocess
import sys
import zipfile
import pymupdf as fitz

ROOT = Path(__file__).resolve().parent
FILES = ['README.md', 'build.py', 'facilitator.tex', 'verify.py']

def totals(a, b):
    return sorted({x+y for x in a for y in b})

def spacing(a):
    if len(a)<2:
        return None
    gaps = {y-x for x,y in zip(a,a[1:])}
    return next(iter(gaps)) if len(gaps)==1 else None

def math_check():
    # Values are independently transcribed from the ten actual final pages.
    cases = [
        ('launch', [1,4], [0,3], [1,4,7]),
        ('P1a', [0,2], [1,3], [1,3,5]),
        ('P1b', [0,2], [1,4], [1,3,4,6]),
        ('P2a', [0,1,2], [0,1,2], [0,1,2,3,4]),
        ('P2b', [0,1,3], [0,1,3], [0,1,2,3,4,6]),
        ('P2c', [0,1,2], [0,3,6], list(range(9))),
        ('P4-2+3', [0,1], [0,1,2], list(range(4))),
        ('P4-2+4', [0,1], [0,1,2,3], list(range(5))),
        ('P4-3+4', [0,1,2], [0,1,2,3], list(range(6))),
        ('P6a', [1,3,5], [2,4], [3,5,7,9]),
        ('P6b', [0,2,4], [0,3], [0,2,3,4,5,7]),
        ('P6c', [0,2,4], [1,3], [1,3,5,7]),
        ('P6d', [0,3,6], [1,4], [1,4,7,10]),
        ('P7a', [4], [0,1,3], [4,5,7]),
        ('P7b', [2], [0,2,4], [2,4,6]),
        ('P7c', [0], [1,4,6,9], [1,4,6,9]),
        ('P9-count-example', [1,4], [0,2,5,8], [1,3,4,6,9,12]),
        ('P9-maximum-3+4', [0,1,2], [0,3,6,9], list(range(12))),
        ('signed-continuation', [-2,0,2], [-3,-1,1], [-5,-3,-1,1,3]),
    ]
    fixed = {}
    for label,a,b,expected in cases:
        actual = totals(a,b)
        assert actual==expected, (label,actual,expected)
        fixed[label] = {'A':a,'B':b,'totals':actual,'count':len(actual)}
    assert fixed['P9-count-example']['count']==6
    # Full catalog by direct set addition, not the general theorem.
    catalogs = {}
    for name,a,gap in [('P5',[0,3,6],3),('alternate-gap-2',[0,2,4],2),
                       ('irregular',[0,1,3],None)]:
        catalog = [{'B':list(b),'totals':totals(a,b)}
                   for b in combinations(range(10),2) if len(totals(a,b))==4]
        expected = [[i,i+gap] for i in range(10-gap)] if gap else []
        assert [x['B'] for x in catalog]==expected
        catalogs[name] = {'tested_choices':45,'solutions':catalog}
    assert len(catalogs['P5']['solutions'])==7

    # Bitset convolution of every nonempty 0--9 input pair checks equality and
    # independently enumerates all legal designs for each printed size.
    items=[]
    for mask in range(1,1<<10):
        a=[i for i in range(10) if mask>>i&1]
        items.append((mask,a,len(a),spacing(a)))
    sizes={(3,3):(5,9,14400),(2,3):(4,6,5400),
           (2,4):(5,8,9450),(3,4):(6,12,25200)}
    extrema={k:{'min':99,'max':0,'designs':0,'histogram':Counter()} for k in sizes}
    singleton_equal=0
    nonsingleton_equal=0
    for _,a,m,da in items:
        for bmask,b,n,db in items:
            sum_mask=0
            for x in a:
                sum_mask|=bmask<<x
            count=sum_mask.bit_count()
            assert m+n-1<=count<=m*n
            equality=count==m+n-1
            predicted=(m==1 or n==1 or (da is not None and da==db))
            assert equality==predicted,(a,b,count)
            if equality:
                if m==1 or n==1:
                    singleton_equal+=1
                else:
                    nonsingleton_equal+=1
            if (m,n) in extrema:
                row=extrema[(m,n)]
                row['designs']+=1
                row['histogram'][count]+=1
                if count<row['min']:
                    row['min']=count
                    row['min_witness']={'A':a,'B':b,'totals':totals(a,b)}
                if count>row['max']:
                    row['max']=count
                    row['max_witness']={'A':a,'B':b,'totals':totals(a,b)}
    for size,(lo,hi,ncases) in sizes.items():
        assert (extrema[size]['min'],extrema[size]['max'],extrema[size]['designs'])==(lo,hi,ncases)
    assert singleton_equal==20360
    assert nonsingleton_equal==2688

    # All monotone paths and a local swap at every adjacent square.
    def routes(a,b):
        def go(i,j,word,values):
            if i==len(a)-1 and j==len(b)-1:
                yield {'word':word,'totals':values}
            if j+1<len(b):
                yield from go(i,j+1,word+'R',values+[a[i]+b[j+1]])
            if i+1<len(a):
                yield from go(i+1,j,word+'U',values+[a[i+1]+b[j]])
        return list(go(0,0,'',[a[0]+b[0]]))
    grids={}
    for label,a,b,expected_grid,nroutes in [
        ('demo',[1,5],[0,2,6],[[1,3,7],[5,7,11]],3),
        ('left',[0,2,5],[1,3,4],[[1,3,4],[3,5,6],[6,8,9]],6),
        ('right',[1,3,5],[0,2,4,6],[[1,3,5,7],[3,5,7,9],[5,7,9,11]],10),
    ]:
        rows=[[x+y for y in b] for x in a]
        assert rows==expected_grid
        paths=routes(a,b)
        assert len(paths)==nroutes
        for route in paths:
            assert len(route['totals'])==len(a)+len(b)-1
            assert all(y>x for x,y in zip(route['totals'],route['totals'][1:]))
        grids[label]={'A':a,'B':b,'rows_bottom_to_top':rows,
                      'sumset':totals(a,b),'paths':paths}
    assert next(x for x in grids['demo']['paths'] if x['word']=='RUR')['totals']==[1,3,7,11]
    # Check actual shared-value removal in common-gap arrays for many dimensions.
    swaps=0
    for m in range(2,7):
        for n in range(2,7):
            for gap in range(1,5):
                a=[2+i*gap for i in range(m)]
                b=[7+j*gap for j in range(n)]
                all_totals=set(totals(a,b))
                for i in range(m-1):
                    for j in range(n-1):
                        prefix=[(k,0) for k in range(i+1)]+[(i,k) for k in range(1,j+1)]
                        suffix=[(k,j+1) for k in range(i+2,m)]+[(m-1,k) for k in range(j+2,n)]
                        common=prefix+[(i+1,j+1)]+suffix
                        shared={a[x]+b[y] for x,y in common}
                        assert len(shared)==m+n-2
                        assert all_totals-shared=={a[i+1]+b[j]}=={a[i]+b[j+1]}
                        swaps+=1
    # General sharpness witnesses for arbitrary sizes beyond the physical kit.
    for m in range(1,15):
        for n in range(1,15):
            assert len(totals(list(range(m)),list(range(n))))==m+n-1
            assert len(totals(list(range(m)),[m*j for j in range(n)]))==m*n
    return {'status':'pass','fixed_inputs':fixed,'catalogs':catalogs,
            'all_nonempty_0_to_9_pairs':1023**2,
            'singleton_equality_pairs':singleton_equal,
            'nonsingleton_equality_pairs':nonsingleton_equal,
            'extrema':{f'{a}+{b}':v for (a,b),v in extrema.items()},
            'grids':grids,'local_swaps_checked':swaps,
            'general_sharpness_sizes_tested':'m,n = 1..14',
            'proof_scope':'Finite experiments; universal proof written in guide.'}

def fingerprint(pdf, render=None):
    d=fitz.open(pdf)
    assert len(d)==9, ('Expected nine guide pages',len(d))
    markers=['Mathematical overview: sharp bounds','Prepare for the fixed',
             'Launch, then let the concrete','Problems 1','Problems 5',
             'Problem 8: a grid','Problem 9: sharp bounds',
             'Problem 10: the complete inverse','Return visits, evidence']
    pages=[]
    if render:
        render.mkdir(parents=True,exist_ok=True)
    for i,page in enumerate(d):
        assert tuple(page.rect)==(0.0,0.0,612.0,792.0)
        text=page.get_text()
        assert markers[i] in text,(i+1,markers[i],text[:500])
        assert 'W55-F-v1' in text
        for block in page.get_text('dict')['blocks']:
            if 'lines' not in block:
                continue
            for line in block['lines']:
                for span in line['spans']:
                    x0,y0,x1,y1=span['bbox']
                    assert x0>=0 and y0>=0 and x1<=612 and y1<=792,(i+1,span)
        pix=page.get_pixmap(matrix=fitz.Matrix(120/72,120/72),alpha=False)
        if render:
            pix.save(render/f'page-{i+1:02d}.png')
        pages.append({'dimensions':list(page.rect),'text':text,
                      'pixel_sha256_120dpi':hashlib.sha256(pix.samples).hexdigest()})
    return pages

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--pdf',type=Path,required=True)
    parser.add_argument('--work',type=Path,required=True)
    args=parser.parse_args()
    work=args.work.resolve()
    work.mkdir(parents=True,exist_ok=True)
    mathematics=math_check()
    (work/'math-checks.json').write_text(json.dumps(mathematics,indent=2)+'\n')
    reference=fingerprint(args.pdf,work/'render')
    copy_src=work/'copied'/'guide-src'
    copy_src.mkdir(parents=True,exist_ok=True)
    assert sorted(p.name for p in ROOT.iterdir() if p.is_file())==sorted(FILES)
    for filename in FILES:
        shutil.copyfile(ROOT/filename,copy_src/filename)
    archive=work/'week55-guide-source-test.zip'
    with zipfile.ZipFile(archive,'w',zipfile.ZIP_DEFLATED) as z:
        for filename in FILES:
            z.write(ROOT/filename,Path('guide-src')/filename)
    extracted=work/'extracted'
    with zipfile.ZipFile(archive) as z:
        assert len(z.namelist())==4
        z.extractall(extracted)
    rebuild=[]
    for mode,source in [('clean_copy',copy_src),('zip_extracted',extracted/'guide-src')]:
        output=source.parent/'output'
        subprocess.run([sys.executable,str(source/'build.py'),'--out',str(output)],check=True)
        current=fingerprint(output/'facilitator.pdf')
        assert current==reference,(mode,'text, dimensions or pixels differed')
        rebuild.append({'mode':mode,'pages':9,'text_equal':True,
                        'dimensions_equal':True,'pixels_equal_120dpi':True})
    summary={'status':'pass','pdf_sha256':hashlib.sha256(args.pdf.read_bytes()).hexdigest(),
             'pages':9,'source_files':FILES,'rebuilds':rebuild,
             'rendered_pages':[f'page-{i:02d}.png' for i in range(1,10)],
             'mathematics':'math-checks.json',
             'boundaries':'No physical rehearsal, kit-fit test or classroom piloting performed.'}
    (work/'verification.json').write_text(json.dumps(summary,indent=2)+'\n')
    (work/'page-fingerprints.json').write_text(json.dumps(reference,indent=2)+'\n')
    print('PASS: math, all nine page dimensions, and clean-copy/ZIP text/pixels at 120 dpi')

if __name__=='__main__':
    main()
