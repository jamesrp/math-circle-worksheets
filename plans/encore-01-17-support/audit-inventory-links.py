#!/usr/bin/env python3
"""Check local Markdown links in the four producer inventories."""
from pathlib import Path
import re,json
ROOT=Path(__file__).resolve().parents[2]
records=[]
for name in ['bonus-weeks-01-05.md','bonus-weeks-06-10.md','bonus-weeks-11-17.md','bonus-weeks-01-17.md']:
    document=ROOT/'plans'/name
    if not document.exists():continue
    for target in re.findall(r'\]\(([^)]+)\)',document.read_text()):
        target=target.strip('<>')
        if re.match(r'^[a-zA-Z][a-zA-Z0-9+.-]*:',target) or target.startswith('#'):continue
        path=target.split('#',1)[0]
        resolved=(document.parent/path).resolve()
        records.append({'document':str(document.relative_to(ROOT)),'target':target,'exists':resolved.exists()})
Path(__file__).with_name('inventory-link-audit.json').write_text(json.dumps(records,indent=2)+'\n')
missing=[x for x in records if not x['exists']]
print(f'{len(records)} local links checked; {len(missing)} absent targets (pending outputs count until release).')
for x in missing:print(x['document'],x['target'])
released=json.loads(Path(__file__).with_name('release-status.json').read_text())
if len(released)==17 and missing:raise SystemExit(1)
