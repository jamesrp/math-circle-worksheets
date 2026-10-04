#!/usr/bin/env python3
"""Optional PDF structural QA; requires pdfplumber. Visual review still required."""
from pathlib import Path
import sys,json
import pdfplumber
p=Path(sys.argv[1]) if len(sys.argv)>1 else Path(__file__).resolve().parent.parent/'build'/'facilitator-guide.pdf'
with pdfplumber.open(p) as doc:
    assert len(doc.pages)==18
    alltext=[];results=[]
    for n,page in enumerate(doc.pages,1):
        text=page.extract_text() or '';alltext.append(text)
        assert 'DRAFT / UNPILOTED' in text,(n,'status')
        assert 'Unscheduled library slot' in text,(n,'slot')
        assert '\ufffd' not in text,(n,'replacement glyph')
        bad=[w for w in page.extract_words() if w['x0']<35 or w['x1']>577 or w['top']<20 or w['bottom']>775]
        assert not bad,(n,bad)
        results.append({'page':n,'words':len(page.extract_words()),'text_geometry':'pass'})
    expected={4:'K-1 / Problem 1',5:'K-1 / Problems 2 and 3',6:'K-1 / Problems 4 and 5',7:'K-1 / Problem 6',8:'Grades 2-3 / Problem 1',9:'Grades 2-3 / Problem 2',10:'Grades 2-3 / Problems 3 and 4',11:'Grades 2-3 / Problem 5',12:'Grades 2-3 / Problem 6',13:'Grades 4-5 / Problem 1',14:'Grades 4-5 / Problem 2',15:'Grades 4-5 / Problem 3',16:'Grades 4-5 / Problems 4 and 5',17:'Grades 4-5 / Problem 6'}
    for n,heading in expected.items():assert heading in alltext[n-1],(n,heading)
    assert 'tree adjacency implies no holes' in alltext[13]
    assert '14, 10 and 12' in '\n'.join(alltext) or ('best boundaries are 10' in alltext[6] and 'row stays at 14' in alltext[6])
print(json.dumps({'status':'PASS','pages':results},indent=2))
