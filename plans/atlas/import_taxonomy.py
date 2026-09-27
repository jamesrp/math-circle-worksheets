"""Import the pinned official MSC file without granting coverage to descendants."""
from pathlib import Path
import csv
import hashlib
import json

ROOT = Path(__file__).resolve().parents[2]
SOURCE = ROOT / 'external-resources/math-atlas/MSC_2020.csv'
OUT = Path(__file__).resolve().parent

def main():
    raw = SOURCE.read_bytes()
    rows = list(csv.DictReader(raw.decode('cp1252').splitlines(), delimiter='\t'))
    assert len({r['code'] for r in rows}) == len(rows)
    nodes = []
    codes = {r['code'] for r in rows}
    for row in rows:
        code = row['code']
        level = 'field' if code.endswith('-XX') else 'subarea' if code.endswith('xx') else 'facet' if '-' in code else 'subject'
        parent = None if level == 'field' else code[:2] + '-XX' if level in ('subarea','facet') else code[:3] + 'xx'
        assert parent is None or parent in codes, (code,parent)
        nodes.append(dict(code=code, title=row['text'], description=row['description'], level=level, parent=parent,
                          research_status='unvisited', bridge_status='unassessed', classroom_status='not-piloted'))
    counts = {k:sum(n['level']==k for n in nodes) for k in ['field','subarea','subject','facet']}
    manifest = dict(source_url='https://msc2020.org/MSC_2020.csv', downloaded='2026-09-25',
                    sha256=hashlib.sha256(raw).hexdigest(), bytes=len(raw), encoding='cp1252', delimiter='tab',
                    publisher='Mathematical Reviews / zbMATH', license='CC-BY-NC-SA-4.0',
                    license_url='https://creativecommons.org/licenses/by-nc-sa/4.0/',
                    node_count=len(nodes), counts=counts,
                    note='Counts are from this downloaded file, not the historical counts on the landing page. Facets are separated from ordinary five-character subjects; nothing is silently discarded.')
    (OUT/'taxonomy.json').write_text(json.dumps(dict(manifest=manifest,nodes=nodes),indent=2,ensure_ascii=False)+'\n')
    (ROOT/'external-resources/math-atlas/manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
    print(json.dumps(manifest,indent=2))

if __name__ == '__main__':
    main()
