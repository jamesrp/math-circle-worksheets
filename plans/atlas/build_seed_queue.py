"""Extract surveyed anchor paragraphs as stable, explicitly provisional seeds."""
from pathlib import Path
import csv
import json
import re

HERE=Path(__file__).resolve().parent

def main():
    seeds=[]
    for src in sorted((HERE/'surveys').glob('*.md')):
        sections=re.split(r'^## (\d\d)\s*[-—–:]\s*([^\n]+)\n',src.read_text(),flags=re.M)
        for i in range(1,len(sections),3):
            code,title,body=sections[i:i+3]
            body=re.split(r'^## ',body,flags=re.M)[0]
            if src.stem=='geometry-analysis':
                anchors=re.search(r'\*\*Anchors\.\*\*(.*?)(?:\n\n|$)',body,re.S)
                assert anchors,code
                parts=re.split(r'\((\d+)\) ',anchors.group(1))
                items=[(parts[j],parts[j+1].strip()) for j in range(1,len(parts),2)]
            else:
                items=re.findall(r'^(\d+)\.\s+(.+?)(?=\n\d+\.\s|\n\n|\Z)',body,re.M|re.S)
            assert 3<=len(items)<=5,(code,len(items))
            for number,text in items:
                seeds.append(dict(id=f'{code}-S{int(number):02}',field=code,field_title=title,anchor=text.strip(),
                                  survey=f'surveys/{src.name}',status='surveyed seed; family-level review required',
                                  classroom_evidence='none',coverage_scope='this anchor only; no descendant MSC credit'))
    assert len({s['id'] for s in seeds})==len(seeds)
    (HERE/'problem-seeds.json').write_text(json.dumps(seeds,indent=2,ensure_ascii=False)+'\n')
    with (HERE/'problem-seeds.csv').open('w',newline='') as out:
        writer=csv.DictWriter(out,fieldnames=list(seeds[0]));writer.writeheader();writer.writerows(seeds)
    print(f'{len(seeds)} surveyed seeds in {len(set(s["field"] for s in seeds))} fields. Not a de-duplicated mechanism count.')

if __name__=='__main__': main()
