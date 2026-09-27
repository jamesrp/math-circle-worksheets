"""Validate atlas links/records and rebuild human and machine-readable indexes.

Only field-level survey status is overlaid. No descendant coverage is inferred.
"""
from pathlib import Path
import csv
import json
import re
from collections import Counter

HERE = Path(__file__).resolve().parent
VOLUMES = ['algebra-discrete', 'geometry-analysis', 'applied-probability']
REQUIRED = set(json.loads((HERE/'family-format.json').read_text())['example_record'])
TYPES = {'exact-special-case','faithful-representation','shared-mechanism','motivation-only'}

def clean(text):
    return str(text).replace('|','/').replace('\n',' ')

def main():
    taxonomy = json.loads((HERE/'taxonomy.json').read_text())
    fields = {n['code'][:2]:n for n in taxonomy['nodes'] if n['level']=='field'}
    surveys = {}
    families = []
    for volume in VOLUMES:
        survey = HERE/'surveys'/f'{volume}.md'
        if survey.exists():
            for code in re.findall(r'^##\s+(\d\d)\s*[-—–:]', survey.read_text(), re.M):
                assert code in fields, ('unknown survey field',code)
                assert code not in surveys, ('duplicate survey field',code)
                surveys[code] = volume
        src = HERE/'families'/f'{volume}.json'
        if not src.exists():
            continue
        records = json.loads(src.read_text())
        assert isinstance(records,list), src
        for f in records:
            assert REQUIRED <= set(f), (f.get('id'), sorted(REQUIRED-set(f)))
            assert f['msc_primary'] in fields, f['id']
            assert all(c in fields for c in f['msc_secondary']), f['id']
            assert f['bridge']['type'] in TYPES, f['id']
            assert isinstance(f['prep_minutes'],(int,float)) and f['prep_minutes']>=0
            assert len(f['hints'])>=2 and len(f['questions'])>=2, f['id']
            assert set(['entry','explore','explain','prove','reading','arithmetic','reasoning','hard_stop']) <= set(f['gates']),f['id']
            assert set(['problem','solution','boundary']) <= set(f['example']),f['id']
            assert all(s.get('title') and s.get('url') and s.get('locator') and s.get('checked') for s in f['source']),f['id']
            assert f['source'], f['id']
            assert all(isinstance(f[k],str) and f[k].strip() for k in ['id','title','adult_question','anchor','materials','launch','choices','session','satisfying_stop','prior_use','status']),f['id']
            f = dict(f, volume=volume)
            families.append(f)
    assert len({f['id'] for f in families})==len(families), 'duplicate family ID'
    primary = Counter(f['msc_primary'] for f in families)
    rows = []
    for code,field in fields.items():
        support = code in ('00','01','97')
        rows.append(dict(code=code,title=field['title'],survey_status='screened' if code in surveys else 'unvisited',
                         disposition='cross-cutting support; separate dossier' if support else 'candidate families; no field-completion claim' if primary[code] else 'survey only; design frontier',
                         survey=surveys.get(code,''),primary_families=primary[code],
                         family_ids='; '.join(f['id'] for f in families if f['msc_primary']==code),
                         descendant_status='unvisited; no inherited coverage',classroom_evidence='none for new atlas designs'))
    with (HERE/'field-coverage.csv').open('w',newline='') as out:
        writer=csv.DictWriter(out,fieldnames=list(rows[0])); writer.writeheader(); writer.writerows(rows)
    with (HERE/'family-index.csv').open('w',newline='') as out:
        writer=csv.DictWriter(out,fieldnames=['id','title','msc_primary','volume','bridge_type','entry','hard_stop','prep_minutes','status'])
        writer.writeheader()
        for f in families:
            writer.writerow({**{k:f[k] for k in ['id','title','msc_primary','volume','prep_minutes','status']},
                             'bridge_type':f['bridge']['type'],'entry':f['gates']['entry'],'hard_stop':f['gates']['hard_stop']})
    lines=['# Mathematics atlas - family index','',
           'Generated from the editable JSON records. Search by mathematical question or prerequisite. Codes classify the primary anchor only; no family covers a whole MSC field. All new designs remain unpiloted.','',
           '| ID | Investigation | Field | Entry capabilities | Bridge |','|---|---|---|---|---|']
    for f in families:
        lines.append(f"| {f['id']} | [{clean(f['title'])}](families/{f['volume']}.md#{f['id'].lower()}) | {f['msc_primary']} | {clean(f['gates']['entry'])} | {f['bridge']['type']} |")
    (HERE/'INDEX.md').write_text('\n'.join(lines)+'\n')
    for volume in VOLUMES:
        selected=[f for f in families if f['volume']==volume]
        if not selected: continue
        lines=[f'# {volume.replace("-"," ").title()} - investigation families','',
               'Facilitator planning cards. These are proposed investigations, not classroom-piloted student packets. The JSON alongside this file is the editable source; this Markdown is generated.','']
        for f in selected:
            lines.extend([f'<a id="{f["id"].lower()}"></a>',f'## {f["id"]} - {f["title"]}','',f'Primary field: {f["msc_primary"]}. Related: {", ".join(f["msc_secondary"]) or "none listed"}. Status: {f["status"]}.','',
                          f'**Adult question.** {f["adult_question"]}','',f'**Anchor.** {f["anchor"]}','',
                          f'**Bridge ({f["bridge"]["type"]}).** {f["bridge"]["preserves"]} Limits: {f["bridge"]["limits"]}','',
                          '**Prerequisite gates.**',''])
            for k,v in f['gates'].items(): lines.append(f'- **{k.replace("_"," ").title()}:** {v}')
            lines.extend(['',f'**Materials and preparation ({f["prep_minutes"]} minutes).** {f["materials"]}','',f'**Launch.** {f["launch"]}','',f'**Learner choices.** {f["choices"]}','',f'**Hour menu.** {f["session"]}','', '**Explore.**',''])
            lines.extend(f'- {q}' for q in f['questions'])
            lines.extend(['','**Hint ladder.**',''])
            lines.extend(f'{i}. {h}' for i,h in enumerate(f['hints'],1))
            lines.extend(['',f'**Checked instance.** {f["example"]["problem"]}','',f'**Reasoning.** {f["example"]["solution"]}','',f'**Boundary.** {f["example"]["boundary"]}','', '**Extensions.**',''])
            lines.extend(f'- {q}' for q in f['extensions'])
            lines.extend(['',f'**Satisfying stop.** {f["satisfying_stop"]}','',f'**Prior use.** {f["prior_use"]}','', '**Sources.**',''])
            for s in f['source']: lines.append(f'- [{s["title"]}]({s["url"]}), {s["locator"]}. Inspection: {s["checked"]}.')
            lines.append('')
        (HERE/'families'/f'{volume}.md').write_text('\n'.join(lines)+'\n')
    report=dict(taxonomy_counts=taxonomy['manifest']['counts'],surveyed_fields=len(surveys),missing_surveys=sorted(set(fields)-set(surveys)),
                family_count=len(families),families_by_volume=dict(Counter(f['volume'] for f in families)),
                primary_fields_with_families=len(primary),substantive_fields_without_families=sorted(set(fields)-{'00','01','97'}-set(primary)),
                bridge_types=dict(Counter(f['bridge']['type'] for f in families)),lower_level_codes_reviewed=0,classroom_pilots=0)
    (HERE/'inventory.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(report,indent=2))

if __name__ == '__main__': main()
