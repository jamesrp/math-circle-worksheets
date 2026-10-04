#!/usr/bin/env python3
"""Check actual local releases against page coverage, builds and source ZIPs."""
from pathlib import Path
import argparse,hashlib,json,re,zipfile
from urllib.parse import unquote
from inspect_pdfs import fingerprint

ROOT=Path(__file__).resolve().parents[2]
BASE=Path(__file__).resolve().parent
YEAR=ROOT/'lowell-math-circle-year-2'
ap=argparse.ArgumentParser();ap.add_argument('--require-all',action='store_true');args=ap.parse_args()
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
stages=json.loads((BASE/'stage-status.json').read_text())
visual=json.loads((BASE/'final-visual-review.json').read_text())
rows=[]
for stage in stages:
    n=stage['week']
    if stage['release']!='completed':
        assert not args.require_all,stage
        continue
    assert all(stage[k]=='completed' for k in ['research','writer','critic','math_review','revision','guide','guide_review','release']),stage
    proof=json.loads((BASE/f'week-{n}/release-checks.json').read_text())
    archive=ROOT/proof['source_zip'];assert sha(archive)==proof['zip_sha256']
    source=YEAR/f'source/week-{n}'
    with zipfile.ZipFile(archive) as z:
        zipped={p:z.read(p) for p in z.namelist() if not p.endswith('/')}
    on_disk={f'week-{n}/'+str(p.relative_to(source)):p.read_bytes() for p in source.rglob('*') if p.is_file()}
    assert zipped==on_disk,(n,'source ZIP mismatch')
    assert all(Path(p).suffix not in ['.pdf','.png','.jpg','.pyc','.aux','.log'] for p in zipped),(n,'unexpected source intermediate/reference')
    docrows=[]
    for doc in proof['documents']:
        p=YEAR/f'week-{n}'/doc['output_file'];actual=fingerprint(p)
        assert actual['sha256']==doc['original']['sha256']
        assert actual['page_evidence']==doc['original']['page_evidence']==doc['extracted_rebuild']['page_evidence']
        assert actual['pages']==doc['original']['pages']==doc['extracted_rebuild']['pages']
        assert doc['exact_text_dimensions_pixels'] is True
        kind='guide' if 'facilitator' in p.name else 'student' if 'students' in p.name else 'materials'
        inspected=[v for v in visual if (v['week'],v['kind'])==(n,kind)]
        assert len(inspected)==1
        v=inspected[0]
        assert v['sha256']==actual['sha256'] and v['pages']==actual['pages']
        assert v['root_inspected_pages']==list(range(1,actual['pages']+1))
        assert v['released_bytes_match_inspected_final'] is True
        docrows.append({'file':str(p.relative_to(ROOT)),'kind':kind,'pages':actual['pages'],'sha256':actual['sha256'],
                        'all_pages_inspected':True,'extracted_zip_exact_text_dimensions_pixels':True})
    reviews=BASE/f'week-{n}/reviews'
    assert all((reviews/p).exists() for p in ['student-adversarial.md','student-math.md','student-revision.md','facilitator-independent.md'])
    rows.append({'week':n,'source_files':len(zipped),'source_zip_matches_directory':True,'documents':docrows})

# Check every local link in the new user-facing index, including pending rows.
index=YEAR/'WEEKS-52-63.md';links=[]
for raw in re.findall(r'\[[^\]]+\]\(([^)]+)\)',index.read_text()):
    url=raw.strip('<>')
    if re.match(r'^[a-zA-Z][a-zA-Z0-9+.-]*:',url) or url.startswith('#'):continue
    p=(index.parent/unquote(url.split('#')[0])).resolve();assert p.exists(),p
    links.append(str(p.relative_to(ROOT)))

old=json.loads((BASE/'corpus-inventory.json').read_text())
workflow=json.loads((BASE/'workflow-input-hashes.json').read_text())
bad=[x['pdf'] for x in old if sha(ROOT/x['pdf'])!=x['sha256']]
bad += [p for p,h in workflow.items() if sha(ROOT/p)!=h]
assert not bad,bad
preserved={'current_existing_pdf_count':len(old),'existing_current_pdf_bytes_unchanged':True,
           'workflow_input_count':len(workflow),'workflow_inputs_unchanged':True,
           'scope':'Only the 309 inventoried current PDFs and ten workflow inputs; not every historical source or pre-existing user edit. No Git mutation performed.',
           'mismatches':bad}
(BASE/'preservation-check.json').write_text(json.dumps(preserved,indent=2)+'\n')
data={'released_themes':len(rows),'selected_themes':len(stages),'all_selected_complete':len(rows)==len(stages),
      'delivered_pdfs':sum(len(r['documents']) for r in rows),'delivered_pages':sum(d['pages'] for r in rows for d in r['documents']),
      'source_zip_count':len(rows),'index_local_links_checked':len(links),'weeks':rows,
      'preservation':preserved,'physical_pretests':'unperformed','classroom_piloting':'unperformed',
      'remote_upload_or_publication':'none','git_mutations':'none'}
(BASE/'final-release-audit.json').write_text(json.dumps(data,indent=2)+'\n')
print(json.dumps({k:v for k,v in data.items() if k not in ['weeks','preservation']}))
