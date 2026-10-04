#!/usr/bin/env python3
"""Write only the new-theme index; links appear once the complete bundle is released."""
import json,re
from pathlib import Path
import pymupdf

BASE=Path(__file__).resolve().parent
ROOT=BASE.parents[1]
YEAR=ROOT/'lowell-math-circle-year-2'
catalog=json.loads((BASE/'theme-catalog.json').read_text())
states={r['week']:r for r in json.loads((BASE/'stage-status.json').read_text())}
released=[r for r in catalog if states[r['week']]['release']=='completed']
complete=len(released)==len(catalog)
lines=['# New themes 52–63','',
       f'{len(released)} of 12 selected themes have complete verified local bundles.' if not complete else 'Twelve new themes with verified local student pages, separate facilitator guides, editable sources and source ZIPs.',
       '', 'Each row counts one theme. The routes can support several investigations and return visits; the approximate bands describe prerequisites rather than additional themes. Page headers and guides give the actual entry and continuation levels.',
       '', '**Status:** all new material is unpiloted. Mathematical checks, every-page rendering/inspection and clean extracted-source rebuilds are complete for released bundles. Physical preparation and handling pretests remain unperformed; each guide identifies the tests needed before use.',
       '', '| Week | Theme | Actual page bands | Current PDFs | Editable sources |',
       '| --- | --- | --- | --- | --- |']
for r in catalog:
    n=str(r['week']);s=states[r['week']]
    if s['release']!='completed':
        lines.append(f'| {n} | {r["title"]} | In production | Pending verification | Pending |')
        continue
    folder=YEAR/f'week-{n}';p=folder/f'week-{n}-students.pdf'
    d=pymupdf.open(p);bands=[]
    for page in d:
        head=page.get_text().split('Problem')[0]
        for band in re.findall(r'Grades\s+([K0-9]+[–−-][0-9]+)',head):
            band=band.replace('−','–').replace('-','–')
            if band not in bands:bands.append(band)
    links=[f'[Students](week-{n}/week-{n}-students.pdf)',f'[Guide](week-{n}/week-{n}-facilitator.pdf)']
    if (folder/f'week-{n}-materials.pdf').exists():links.append(f'[Materials](week-{n}/week-{n}-materials.pdf)')
    lines.append(f'| {n} | {r["title"]} | {", ".join(bands)} | {" · ".join(links)} | [Source](source/week-{n}/README.md) · [ZIP](source/week-{n}-source.zip) |')
lines+=['','## Routes and relationships','']
for r in catalog:
    if states[r['week']]['release']=='completed':lines.append(f'- **Week {r["week"]}:** {r["route"]}')
lines+=['','The [novelty audit](../plans/new-themes-52-63/NOVELTY-AUDIT.md) records nearby base and bonus material and the distinct mathematical destination of each theme. Related prior themes and source page references are retained in the bundles’ provenance notes. The earlier atlas is a source of leads, not evidence of classroom validation.',
        '', 'The [production record](../plans/new-themes-52-63/stage-status.json), [final visual coverage](../plans/new-themes-52-63/final-visual-review.json), [release audit](../plans/new-themes-52-63/final-release-audit.json), per-week `release-checks.json` records, and the [preservation check](../plans/new-themes-52-63/preservation-check.json) provide supporting evidence. Each source ZIP includes original editable sources and a standalone build; downloaded references, generated prompts, borrowed style exemplars and rendering intermediates stay outside the bundles.',
        '', 'These are the current local releases. No publication or remote upload is claimed. Record actual use, observations and unresolved investigations before planning a returning child’s next visit.','']
(YEAR/'WEEKS-52-63.md').write_text('\n'.join(lines))
print(json.dumps({'released_themes':len(released),'selected_themes':len(catalog),'index':str((YEAR/'WEEKS-52-63.md').relative_to(ROOT))}))
