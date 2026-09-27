#!/usr/bin/env python3
"""Generate the final eighty-family page finder from data and build reports."""
import json
from pathlib import Path

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[2]
REPORT=ROOT/'tmp/pdfs/atlas-remaining/build-report.json'
LABELS={'algebra-discrete':'Algebra and discrete mathematics',
        'geometry-analysis':'Geometry and analysis','applied-probability':'Probability and applications'}


def span(record,fid):
    pages=[p['page'] for p in record['page_map'] if p['family_id']==fid]
    assert pages and pages==list(range(min(pages),max(pages)+1)),fid
    return str(pages[0]) if len(pages)==1 else f'{pages[0]}–{pages[-1]}'


def cell(text):
    return str(text).replace('|','/').replace('\n',' ')


def relative_pdf(record):
    path=Path(record['path'])
    if not path.is_absolute():path=ROOT/path
    return str(path.resolve().relative_to(ROOT))


def main():
    scope=json.loads((HERE/'scope.json').read_text())
    reports=json.loads(REPORT.read_text())
    rows=['# Page finder: the remaining eighty','',
          'Choose by the tools needed for a satisfying investigation, rather than age. '
          'Page numbers below are printed/PDF page numbers. Hand out one student page at a time; '
          'later pages may be a separate meeting. All activities remain unpiloted.','',
          'The [original ten](../worksheet-trial/README.md) remain in their own two books. '
          'Those ten plus the eighty below cover all ninety atlas family IDs.','']
    ids=[];records=[]
    for group,meta in scope['groups'].items():
        rep=reports[group]
        link=lambda kind:'../../../'+relative_pdf(rep[kind])
        rows += ['## '+LABELS[group],'',f"[Student book]({link('student')}) · [Facilitator guide]({link('facilitator')})",'',
                 '| Family and investigation | Core tools | Student pages | Guide pages |',
                 '|---|---|---|---|']
        families=[]
        for batch in meta['batches']:
            data=json.loads((HERE/f"{batch['batch']}-data.json").read_text())
            by_id={f['id']:f for f in data['families']}
            assert len(data['families'])==len(by_id)==len(batch['ids']) and set(by_id)==set(batch['ids'])
            families.extend(by_id[fid] for fid in batch['ids'])
        for f in families:
            fid=f['id'];ids.append(fid)
            student,guide=span(rep['student'],fid),span(rep['facilitator'],fid)
            gate=f.get('index_gate',f['core_gate'])
            rows.append(f"| {fid} — {cell(f['title'])} | {cell(gate)} | {student} | {guide} |")
            records.append({'id':fid,'title':f['title'],'group':group,'core_gate':f['core_gate'],
                'index_gate':gate,'extension_gate':f['extension_gate'],'assessment':f['assessment'],
                'satisfying_stop':f['satisfying_stop'],'student_pages':student,'guide_pages':guide,
                'student_pdf':relative_pdf(rep['student']),
                'facilitator_pdf':relative_pdf(rep['facilitator'])})
        rows+=['','### Teaching judgments','']
        for f in families:rows.append(f"- **{f['id']}:** {f['assessment']}")
        rows+=['']
    assert len(ids)==len(set(ids))==80
    assert not set(ids)&set(scope['excluded_completed'])
    (HERE/'INDEX.md').write_text('\n'.join(rows)+'\n')
    (HERE/'family-index.json').write_text(json.dumps(records,ensure_ascii=False,indent=2)+'\n')
    print('Indexed80unique families with verified page spans.')


if __name__=='__main__':main()
