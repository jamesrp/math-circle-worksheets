"""Structural release checks; not a substitute for mathematical or visual review."""
from pathlib import Path
import csv
import hashlib
import json
import re
from urllib.parse import unquote

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[1]

def main():
    inventory=json.loads((HERE/'inventory.json').read_text())
    seeds=json.loads((HERE/'problem-seeds.json').read_text())
    assert inventory['surveyed_fields']==63 and not inventory['missing_surveys']
    assert inventory['family_count']==90,inventory['family_count']
    assert inventory['primary_fields_with_families']==60
    assert not inventory['substantive_fields_without_families']
    assert len(seeds)==231 and len({s['id'] for s in seeds})==231
    assert inventory['lower_level_codes_reviewed']==0 and inventory['classroom_pilots']==0
    sources=[]; hashes={}; empty=[]; reviewed=0
    for p in sorted((HERE/'families').glob('*.json')):
        hashes[str(p.relative_to(ROOT))]=hashlib.sha256(p.read_bytes()).hexdigest()
        for family in json.loads(p.read_text()):
            assert family['status']=='reviewed plan v1; exact instance checked; not classroom-piloted',family['id']
            reviewed+=1
            for source in family['source']:
                sources.append(dict(family=family['id'],**source))
            for key in ['materials','launch','choices','session','satisfying_stop','prior_use']:
                if not family[key].strip():empty.append((family['id'],key))
    assert not empty,empty
    with (HERE/'source-map.csv').open('w',newline='') as out:
        w=csv.DictWriter(out,fieldnames=['family','title','url','locator','checked']);w.writeheader();w.writerows(sources)
    broken=[]
    for p in sorted(HERE.rglob('*.md')):
        # Anchors and external URLs are not filesystem targets. Source links may
        # contain literal parentheses; check only unambiguous local file links.
        for target in re.findall(r'\]\(([^\n]+?)\)',p.read_text()):
            target=target.strip('<>').split('#')[0]
            if not target or '://' in target or target.startswith('mailto:'):continue
            if '(' in target or ')' in target:continue
            path=Path(unquote(target))
            if not path.is_absolute(): path=p.parent/path
            if not path.exists():broken.append((str(p.relative_to(HERE)),target))
    assert not broken,broken
    reviews=['algebra-discrete-review.md','geometry-analysis-review.md','applied-probability-review.md']
    assert all((HERE/'reviews'/name).is_file() for name in reviews)
    pdfs={}
    for name in ['math-atlas-investigation-plans.pdf','math-atlas-research-map.pdf']:
        p=ROOT/'lowell-math-circle-year-2/combined'/name
        assert p.is_file(),p
        pdfs[str(p.relative_to(ROOT))]=dict(bytes=p.stat().st_size,sha256=hashlib.sha256(p.read_bytes()).hexdigest())
    report=dict(status='structural checks passed',fields=63,problem_seeds=231,families=90,
                substantive_fields_with_primary_family=60,source_entries=len(sources),
                unique_source_urls=len({s['url'] for s in sources}),source_hashes=hashes,
                reviewed_plan_families=reviewed,independent_plan_review_reports=reviews,pdf_outputs=pdfs,
                note='Source entries are provenance records, not a source-quality score. Mathematical and visual checks are separate.')
    (HERE/'release-check.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(report,indent=2))

if __name__=='__main__': main()
