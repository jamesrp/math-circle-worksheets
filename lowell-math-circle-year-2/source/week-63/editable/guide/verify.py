#!/usr/bin/env python3
"""Independent finite math audit, plus actual-guide/page checks.

No student/research verifier, builder data or precomputed generated answer table
is imported. General proofs remain human arguments in the guide.
"""
import argparse
import hashlib
from itertools import combinations, permutations
import json
from math import comb, factorial
from pathlib import Path
import re

CAT3 = 'BCA CAB'.split()
CAT4 = 'BADC BCDA BDAC CADB CDAB CDBA DABC DCAB DCBA'.split()
PARTIAL4 = 'BACD BADC BCAD BCDA BDAC BDCA CABD CADB CDAB CDBA DABC DACB DCAB DCBA'.split()
BRANCHES5 = {
    'A': 'EABCD EADBC EADCB ECABD ECBAD ECDAB ECDBA EDABC EDACB EDBAC EDBCA'.split(),
    'B': 'BEACD BEDAC BEDCA CEABD CEBAD CEDAB CEDBA DEABC DEACB DEBAC DEBCA'.split(),
    'C': 'BAECD BCEAD BDEAC BDECA CAEBD CDEAB CDEBA DAEBC DAECB DCEAB DCEBA'.split(),
    'D': 'BADEC BCAED BCDEA BDAEC CABED CADEB CDAEB CDBEA DABEC DCAEB DCBEA'.split(),
}
RECIP5 = {'A': 'ECDBA EDBCA'.split(), 'B': 'CEDAB DEACB'.split(),
          'C': 'BDEAC DAEBC'.split(), 'D': 'BCAED CABED'.split()}
INTERSECTIONS4 = {
    'A': 'ABCD ABDC ACBD ACDB ADBC ADCB'.split(),
    'B': 'ABCD ABDC CBAD CBDA DBAC DBCA'.split(),
    'C': 'ABCD ADCB BACD BDCA DACB DBCA'.split(),
    'D': 'ABCD ACBD BACD BCAD CABD CBAD'.split(),
    'AB': 'ABCD ABDC'.split(), 'AC': 'ABCD ADCB'.split(),
    'AD': 'ABCD ACBD'.split(), 'BC': 'ABCD DBCA'.split(),
    'BD': 'ABCD CBAD'.split(), 'CD': 'ABCD BACD'.split(),
    'ABC': ['ABCD'], 'ABD': ['ABCD'], 'ACD': ['ABCD'],
    'BCD': ['ABCD'], 'ABCD': ['ABCD'],
}
REDUCTIONS5_A = {
    'ECDBA': ('reciprocal', 'BCD', 'CDB'),
    'EDBCA': ('reciprocal', 'BCD', 'DBC'),
    'EABCD': ('longer', 'ABCD', 'DABC'),
    'EADBC': ('longer', 'ABCD', 'CADB'),
    'EADCB': ('longer', 'ABCD', 'BADC'),
    'ECABD': ('longer', 'ABCD', 'DCAB'),
    'ECBAD': ('longer', 'ABCD', 'DCBA'),
    'ECDAB': ('longer', 'ABCD', 'BCDA'),
    'EDABC': ('longer', 'ABCD', 'CDAB'),
    'EDACB': ('longer', 'ABCD', 'BDAC'),
    'EDBAC': ('longer', 'ABCD', 'CDBA'),
}

def universe(labels):
    return [''.join(p) for p in permutations(labels)]

def matches(labels, row):
    return frozenset(h for h, c in zip(labels, row) if h == c)

def derangements(labels):
    return [r for r in universe(labels) if not matches(labels, r)]

def arrows(labels, row):
    return {card: home for home, card in zip(labels, row)}

def reduce_row(labels, row, z, h):
    assert row[labels.index(h)] == z and z != h
    loc = dict(zip(labels, row))
    if loc[z] == h:
        family = 'reciprocal'
        keep = ''.join(c for c in labels if c not in (z, h))
    else:
        family = 'longer'
        loc[h] = loc[z]
        keep = labels.replace(z, '')
    smaller = ''.join(loc[c] for c in keep)
    assert not matches(keep, smaller)
    return family, keep, smaller

def restore(labels, z, h, family, keep, smaller):
    loc = dict(zip(keep, smaller))
    if family == 'reciprocal':
        loc[h], loc[z] = z, h
    else:
        loc[z], loc[h] = loc[h], z
    return ''.join(loc[c] for c in labels)

def math_audit():
    result = {'counts': {}, 'intersections': {}, 'bijections': {},
              'general_proof_limit': 'Finite checks supplement, not prove, the general arguments.'}
    expected_counts = [1, 0, 1, 2, 9, 44, 265]
    for n in range(7):
        labels = 'ABCDEF'[:n]
        rows, ders = universe(labels), derangements(labels)
        assert len(rows) == factorial(n) and len(ders) == expected_counts[n]
        terms = [(-1)**k * comb(n, k) * factorial(n-k) for k in range(n+1)]
        assert sum(terms) == len(ders)
        subsets = [s for k in range(n+1) for s in combinations(labels, k)]
        inter = {}
        for s in subsets:
            found = [r for r in rows if set(s) <= matches(labels, r)]
            assert len(found) == factorial(n-len(s))
            inter[''.join(s)] = found
        for r in rows:
            m = matches(labels, r)
            contributions = [(s, (-1)**len(s)) for s in subsets if set(s) <= m]
            assert sum(weight for _, weight in contributions) == (0 if m else 1)
            if m:
                pivot = min(m)
                terms_by_set = {frozenset(s): sign for s, sign in contributions}
                for s, sign in terms_by_set.items():
                    if pivot not in s:
                        assert terms_by_set[s | {pivot}] == -sign
        hist = [sum(len(matches(labels, r)) == m for r in rows) for m in range(n+1)]
        result['counts'][n] = {'universe': len(rows), 'derangements': len(ders),
                               'terms': terms, 'exact_match_histogram': hist}
        result['intersections'][n] = inter
        if n >= 2:
            assert len(ders) == (n-1)*(expected_counts[n-1]+expected_counts[n-2])
            z = labels[-1]
            branches = {}
            for h in labels[:-1]:
                branch = [r for r in ders if r[labels.index(h)] == z]
                fam = {'reciprocal': [], 'longer': []}
                for r in branch:
                    family, keep, smaller = reduce_row(labels, r, z, h)
                    assert restore(labels, z, h, family, keep, smaller) == r
                    fam[family].append((r, keep, smaller))
                for family in fam:
                    keep = (''.join(c for c in labels if c not in (z,h))
                            if family == 'reciprocal' else labels.replace(z,''))
                    target = derangements(keep)
                    assert sorted(item[2] for item in fam[family]) == target
                    for r in target:
                        full = restore(labels,z,h,family,keep,r)
                        assert full in branch and reduce_row(labels,full,z,h) == (family,keep,r)
                branches[h] = fam
            assert len({r for h in branches for family in branches[h]
                        for r, _, _ in branches[h][family]}) == len(ders)
            result['bijections'][n] = branches
    assert derangements('ABC') == CAT3
    assert derangements('ABCD') == CAT4
    assert [r for r in universe('ABCD') if r[0]!='A' and r[1]!='B'] == PARTIAL4
    assert [r for r in universe('ABC') if r[0]!='A' and r[1]!='B'] == 'BAC BCA CAB'.split()
    for s, expected in INTERSECTIONS4.items():
        assert result['intersections'][4][s] == expected
    all5 = []
    for h, rows in BRANCHES5.items():
        actual = [r for r in derangements('ABCDE') if r['ABCDE'.index(h)]=='E']
        assert actual == rows and len(rows)==11
        reciprocal = [r for r in rows if r[-1]==h]
        assert reciprocal == RECIP5[h]
        all5 += rows
    assert sorted(all5) == derangements('ABCDE') and len(set(all5))==44
    for r, triple in REDUCTIONS5_A.items():
        assert reduce_row('ABCDE',r,'E','A') == triple
    expected7 = {'DCBA':('reciprocal','BC','CB'),
                 'DABC':('longer','ABC','CAB'),'DCAB':('longer','ABC','BCA')}
    for r, triple in expected7.items():
        assert reduce_row('ABCD',r,'D','A') == triple
    assert matches('UVWX','VUWX') == {'W','X'}
    assert arrows('PQRST','QRSTP') == dict(P='T',T='S',S='R',R='Q',Q='P')
    assert reduce_row('PQRSTU','UTQRSP','U','P') == ('reciprocal','QRST','TQRS')
    assert reduce_row('PQRSTU','UPQRST','U','P') == ('longer','PQRST','TPQRS')
    assert matches('ABCDE','AECDB') == {'A','C','D'}
    assert 5*(10+2) + 5*(6+5+12) + 2*24 == 223
    assert 24*56*27 == 36288 > 173*97
    result['guide_catalogs'] = {'three':CAT3,'four':CAT4,'partial_four':PARTIAL4,
                               'five_by_E_home':BRANCHES5,'E_at_A_reductions':REDUCTIONS5_A}
    return result

def pdf_audit(path):
    import pymupdf as fitz
    doc = fitz.open(path)
    assert len(doc)==10, f'Expected 10 guide pages, got {len(doc)}'
    result = {'sha256':hashlib.sha256(path.read_bytes()).hexdigest(), 'pages':[]}
    for i,p in enumerate(doc):
        assert tuple(p.rect)==(0,0,612,792)
        text = p.get_text()
        assert 'Week 63 / Cards away from home / Facilitator' in text
        assert 'W63-G-v1' in text
        words=p.get_text('words')
        assert all(w[0]>=0 and w[1]>=0 and w[2]<=612 and w[3]<=792 for w in words)
        result['pages'].append({'page':i+1,'size':[612,792],
                               'text_sha256':hashlib.sha256(text.encode()).hexdigest(),
                               'pixel_sha256_144dpi':hashlib.sha256(p.get_pixmap(matrix=fitz.Matrix(2,2)).samples).hexdigest()})
    expected_page_words = {
        4: CAT3+CAT4+'ABC ACB BAC CBA'.split(), 5: PARTIAL4,
        7: 'DCBA DABC DCAB CB CAB BCA QRSTP UTQRSP TQRS UPQRST TPQRS'.split(),
        8: list(REDUCTIONS5_A)+[t[2] for t in REDUCTIONS5_A.values()],
        9: [r for rs in BRANCHES5.values() for r in rs],
    }
    for page, rows in expected_page_words.items():
        found=re.findall(r'\b[A-Z]{2,6}\b',doc[page-1].get_text())
        for row in rows: assert row in found, (page,row)
    # Bind each printed reduction to its own table row, rather than merely
    # asserting that the labels occur somewhere on the page.
    words8=doc[7].get_text('words')
    for full, (family, keep, smaller) in REDUCTIONS5_A.items():
        anchors=[w for w in words8 if w[4]==full and w[0]<180]
        assert len(anchors)==1,(full,anchors)
        line=sorted((w for w in words8 if abs(w[1]-anchors[0][1])<3),key=lambda w:w[0])
        line_text=' '.join(w[4] for w in line)
        assert family in line_text and smaller in line_text, (full,line_text)
        assert '/'.join(keep) in line_text, (full,keep,line_text)
    assert 'UNPERFORMED' in doc[2].get_text()
    assert 'AECDB' in doc[5].get_text()
    assert 'Mathematical overview' in doc[0].get_text()
    return result

def main():
    p=argparse.ArgumentParser()
    p.add_argument('--pdf',type=Path)
    p.add_argument('--out',type=Path,required=True)
    a=p.parse_args()
    result={'math':math_audit()}
    if a.pdf: result['pdf']=pdf_audit(a.pdf)
    a.out.parent.mkdir(parents=True,exist_ok=True)
    a.out.write_text(json.dumps(result,indent=2)+'\n')
    print('PASS: all n=0..6 permutations, inclusive intersections, cancellation, label-preserving inverse maps, guide catalogs and requested PDF checks.')

if __name__=='__main__':main()
