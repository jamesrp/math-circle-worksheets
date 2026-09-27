#!/usr/bin/env python3
"""Audit final assembly against the independently reviewed batch previews."""
import hashlib,json,re,subprocess,sys
from datetime import date
from pathlib import Path
from collections import Counter
import pdfplumber
from pypdf import PdfReader
HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[2]
TMP=ROOT/'tmp/pdfs/atlas-remaining'

def digest(path):return hashlib.sha256(path.read_bytes()).hexdigest()
def norm(value):
    if isinstance(value,(int,float)):return round(float(value),5)
    if isinstance(value,(list,tuple)):return [norm(v) for v in value]
    if isinstance(value,dict):return {k:norm(v) for k,v in sorted(value.items())}
    return str(value) if value is not None and not isinstance(value,(str,bool)) else value

def body_signature(page):
    # All text and vector geometry in the reviewed body, excluding running
    # folios and top running labels. Family titles remain inside the comparison.
    def intersects_body(obj):return obj.get('bottom',792)>=44 and obj.get('top',0)<=746
    chars=[]
    for c in page.chars:
        if not intersects_body(c):continue
        item={k:c.get(k) for k in ['text','x0','x1','top','bottom','size','fontname','non_stroking_color']}
        # PDF subset tags identify embedding batches, not typefaces. The same
        # glyph can move between subsets when several preview books are joined.
        item['fontname']=re.sub(r'^[A-Z]{6}\+','',item['fontname'])
        chars.append(item)
    shapes={}
    for kind in ['lines','rects','curves','images']:
        shapes[kind]=[{k:s.get(k) for k in ['x0','x1','top','bottom','pts','path','linewidth','stroke','fill','stroking_color','non_stroking_color','dash','srcsize'] if k in s}
                      for s in getattr(page,kind) if intersects_body(s)]
    shapes['image_content']=[digest_bytes(s['stream'].get_data()) for s in page.images if intersects_body(s)]
    return digest_bytes(json.dumps(norm({'chars':chars,'shapes':shapes}),sort_keys=True,ensure_ascii=False).encode())

def digest_bytes(data):return hashlib.sha256(data).hexdigest()

def report_at(path):
    data=json.loads(path.read_text())
    assert len(data)==1,('Batch report should contain one volume',path)
    return next(iter(data.values()))

def verify_links(record):
    pdf=PdfReader(record['path'])
    assert len(pdf.pages)==record['pages'],('Actual PDF page count',record['path'])
    starts=record['starts'];expected=set(starts.values());links=[]
    assert starts,('Empty family contents',record['path'])
    for fid,pn in starts.items():
        body_pages=[p['page'] for p in record['page_map'] if p['family_id']==fid]
        assert body_pages and pn==min(body_pages),('Family start differs from body',fid,pn,body_pages)
    id_to_page={p.indirect_reference.idnum:i+1 for i,p in enumerate(pdf.pages)}
    for i in range(min(expected)-1):
        for a in pdf.pages[i].get('/Annots',[]):
            ann=a.get_object()
            if ann.get('/Subtype')!='/Link':continue
            dest=ann.get('/Dest')
            if dest:
                obj=dest.get_object()
                assert isinstance(obj,list),('Unexpected contents destination',obj)
                links.append(id_to_page[obj[0].idnum])
    assert Counter(links)==Counter(expected),('Contents links',links,expected)
    outlines=[]
    def walk(items):
        for item in items:
            if isinstance(item,list):walk(item)
            else:outlines.append((item.title,pdf.get_destination_page_number(item)+1))
    walk(pdf.outline)
    for fid,pn in starts.items():
        hits=[p for title,p in outlines if title.startswith(fid+' - ')]
        assert hits==[pn],('Family bookmark',fid,hits,pn)
    return {'contents_links':len(links),'family_bookmarks':len(starts)}

def main():
    scope=json.loads((HERE/'scope.json').read_text())
    registry=json.loads((HERE/'reviewed-previews.json').read_text())
    finals=json.loads((TMP/'build-report.json').read_text())
    assert set(finals)==set(scope['groups']),('Final subject set',set(finals))
    for group,records in finals.items():
        assert set(records)=={'student','facilitator'},('Missing or extra book kind',group,set(records))
    preservation={}
    for path,sha in {**scope['source_hashes'],**scope['preserved_trial_outputs'],**scope.get('preserved_trial_sources',{})}.items():
        actual=digest(ROOT/path);assert actual==sha,('Preserved file changed',path)
        preservation[path]=actual
    batches={b['batch']:b for g in scope['groups'].values() for b in g['batches']}
    assert set(registry)==set(batches),('Missing reviewed previews',set(batches)-set(registry))
    all_ids=[];all_prompts=[];family_data={};batch_data={}
    for batch,b in batches.items():
        d=json.loads((HERE/f'{batch}-data.json').read_text());batch_data[batch]=d
        ids=[f['id'] for f in d['families']]
        assert len(ids)==len(set(ids))==8 and set(ids)==set(b['ids'])
        all_ids+=ids
        for f in d['families']:
            family_data[f['id']]=f
            for pg in f['pages']:
                assert pg['gate'] and pg['intro']
                for q in pg['prompts']:
                    assert q['text'].strip() and q['solution'].strip()
                    all_prompts.append((f['id'],str(q['id'])))
            for ex in f['extensions']:assert ex['solution'].strip() and ex['gate'].strip()
        r=registry[batch]
        assert r['design_review_closed'] and r['pdf_review_closed'],batch
        for path,sha in r['reviewed_input_hashes'].items():assert digest(ROOT/path)==sha,('Reviewed input changed',path)
        for key in ['design_review','pdf_review','maker_qa']:assert (ROOT/r[key]).exists(),r[key]
    assert len(all_ids)==len(set(all_ids))==80 and not set(all_ids)&set(scope['excluded_completed'])
    original_ids=set()
    for path in scope['source_hashes']:
        d=json.loads((ROOT/path).read_text());rows=d if isinstance(d,list) else d['families']
        original_ids.update(f['id'] for f in rows)
    assert set(all_ids)|set(scope['excluded_completed'])==original_ids
    assert len(all_prompts)==len(set(all_prompts))
    assert 'calculus' in family_data['GA-08']['core_gate'].lower() or 'derivative' in family_data['GA-08']['core_gate'].lower()
    outputs={};body_matches={}
    for group,meta in scope['groups'].items():
        outputs[group]={}
        for kind,rec in finals[group].items():
            expected_ids={fid for b in meta['batches'] for fid in b['ids']}
            assert set(rec['starts'])==expected_ids,('Final book family set',group,kind)
            path=Path(rec['path']);assert digest(path)==rec['sha256']
            c=rec['checks'];assert not c['blank_pages'] and not c['out_of_page_chars'] and not c['suspect_glyphs']
            assert rec['render']['pages']==rec['pages']
            if kind=='student':
                expected=[p for p in all_prompts if p[0] in rec['starts']]
                actual=[(p['family_id'],p['prompt_id']) for p in rec['printed_tasks']]
                assert Counter(actual)==Counter(expected)
            links=verify_links(rec)
            count=0
            with pdfplumber.open(path) as final_pdf:
                for b in meta['batches']:
                    batch=b['batch'];r=registry[batch];preview=report_at(ROOT/r['build_report'])[kind]
                    assert digest(Path(preview['path']))==r['preview_sha256'][kind],('Preview changed',batch,kind)
                    with pdfplumber.open(preview['path']) as pre_pdf:
                        for fid in b['ids']:
                            fp=[p['page'] for p in rec['page_map'] if p['family_id']==fid]
                            pp=[p['page'] for p in preview['page_map'] if p['family_id']==fid]
                            assert len(fp)==len(pp),('Body page count changed',fid,kind)
                            for a,z in zip(fp,pp):
                                assert body_signature(final_pdf.pages[a-1])==body_signature(pre_pdf.pages[z-1]),('Body differs from reviewed preview',fid,kind,a,z)
                                count+=1
            outputs[group][kind]={'path':str(path.relative_to(ROOT)),'pages':rec['pages'],'sha256':rec['sha256'],
                'rendered_pages':rec['render']['pages'],'body_pages_matching_reviewed_previews':count,**links,
                'family_pages':{fid:[p['page'] for p in rec['page_map'] if p['family_id']==fid] for fid in rec['starts']},
                'blank_pages':0,'out_of_page_characters':0,'suspect_glyphs':0}
    checks={}
    for path in sorted(HERE.glob('*-checks.py')):
        result=subprocess.run([sys.executable,str(path)],cwd=ROOT,capture_output=True,text=True)
        assert result.returncode==0,(path,result.stdout,result.stderr)
        checks[path.name]={'sha256':digest(path),'status':'pass','output':result.stdout.strip()[-3000:]}
    manifest={'review_date':date.today().isoformat(),'status':'all eighty produced and independently reviewed; not classroom-piloted',
        'families':80,'student_prompts':len(all_prompts),'guide_extensions':sum(len(f['extensions']) for f in family_data.values()),
        'preserved_files':preservation,'outputs':outputs,'mathematical_checks':checks,
        'reviewed_preview_registry_sha256':digest(HERE/'reviewed-previews.json'),
        'review_scope':'Every student body was inspected full-size by maker and independent reviewer. Every guide page was inspected at least on contacts, with dense/diagram pages full-size. Final contents were newly inspected; final body text and vector geometry match the reviewed batch previews exactly.',
        'input_hashes':{str(p.relative_to(ROOT)):digest(p) for p in sorted(list(HERE.glob('*-data.json'))+list((ROOT/'lowell-math-circle-year-2/source/atlas-remaining').glob('*.py')))}}
    (HERE/'release-manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
    print('Release audit passed:',len(all_ids),'families;',len(all_prompts),'student prompts; six PDFs.')
if __name__=='__main__':main()
