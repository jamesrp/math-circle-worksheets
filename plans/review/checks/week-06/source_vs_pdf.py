"""Do the delivered PDFs carry the sources I read?

* Student packets: every problem statement and the 4-5 opening rules in
  src/*.tex must appear in the PDF text, and the puzzle records written in the
  source (\\kpuzzle, \\puzzlebox) must equal the ones read from the PDF drawing.
* Adult guide: every sentence of 30+ characters in guide-src/facilitator.tex
  that survives a plain-text conversion must appear in the guide PDF.
* Return visit: the same for student/return-visit.tex and facilitator.tex.
pdfLaTeX/XeLaTeX are not installed here, so no rebuild is attempted.
"""
import os, re, sys, json, subprocess
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from codegame import HERE, PKT, SRC, RV_SRC

D = json.load(open(os.path.join(HERE, 'pdf_data.json')))


def pdf_text(fn):
    t = subprocess.run(['pdftotext', os.path.join(PKT, fn), '-'], capture_output=True, text=True).stdout
    t = re.sub(r'Week 6 / Code breaking / [^\n]*\n', ' ', t)
    t = re.sub(r'Bellingham Math Circle / Week 6 / \S+\s+\d+', ' ', t)
    return norm(t)


def norm(t):
    t = (t.replace('\u2019', "'").replace('\u2018', "'").replace('\u201c', '"').replace('\u201d', '"')
         .replace('\u2013', '-').replace('\u2014', '-').replace('\u2212', '-').replace('\ufb01', 'fi').replace('\ufb02', 'fl')
         .replace('\u00b7', '*').replace('\u2264', '<=').replace('\u2265', '>=').replace('\u2192', '->'))
    return re.sub(r'\s+', ' ', t).strip()


def unwrap(s, cmd, sep=' '):
    # \cmd{a}{b} -> a b, with nested braces
    out, i = '', 0
    key = '\\' + cmd + '{'
    while True:
        j = s.find(key, i)
        if j < 0:
            return out + s[i:]
        out += s[i:j]
        k = j + len(key) - 1
        args = []
        while k < len(s) and s[k] == '{':
            depth, m = 0, k
            while True:
                if s[m] == '{' and s[m - 1] != '\\':
                    depth += 1
                elif s[m] == '}' and s[m - 1] != '\\':
                    depth -= 1
                    if depth == 0:
                        break
                m += 1
            args.append(s[k + 1:m])
            k = m + 1
        out += sep.join(args) + sep
        i = k


def detex(s):
    s = re.sub(r'(?<!\\)%.*', '', s)
    for c in ('labelled', 'parttitle', 'lab'):
        s = unwrap(s, c)
    s = re.sub(r'\\begin\{(minipage|tcolorbox)\}(\[[^\]]*\])?(\{[^{}]*\})?', ' ', s)
    s = s.replace('\\{', '{').replace('\\}', '}')
    s = s.replace('``', '"').replace("''", '"').replace('--', '-').replace('~', ' ').replace('\\,', ' ')
    s = s.replace('\\%', '%').replace('\\&', '&').replace('\\ ', ' ').replace('\\\\', ' ')
    for _ in range(3):
        s = re.sub(r'\\(cd|textbf|emph|textsf|mbox|textit|texttt|lab|hints|small|normalsize)\{([^{}]*)\}', r'\2', s)
    s = re.sub(r'\\(core|further)\b', lambda m: m.group(1), s)
    s = re.sub(r'\\textperiodcentered', '*', s)
    s = re.sub(r'\\[a-zA-Z]+\*?(\[[^\]]*\])?(\{[^{}]*\})*', ' ', s)
    s = s.replace('{', '').replace('}', '').replace('\\_', '_')
    return norm(s)


def problem_statements(tex):
    body = tex.split('\\begin{document}', 1)[1]
    out = []
    for chunk in re.split(r'\\problem\b', body)[1:]:
        stmt = []
        for line in chunk.split('\n'):
            if line.strip().startswith('\\') and not line.strip().startswith('\\problem'):
                if stmt:
                    break
                continue
            if not line.strip():
                if stmt:
                    break
                continue
            stmt.append(line)
        out.append(detex(' '.join(stmt)))
    return out


bad = 0
for band, fn in (('k-1', 'k-1.tex'), ('grades-2-3', 'grades-2-3.tex'), ('grades-4-5', 'grades-4-5.tex')):
    tex = open(os.path.join(SRC, 'src', fn)).read()
    text = pdf_text(f'week-06-{band}.pdf')
    stm = problem_statements(tex)
    miss = [s for s in stm if s not in text]
    print(f'{band}: {len(stm)} problem statements in source; {len(stm) - len(miss)} found verbatim in the PDF')
    for s in miss:
        print('   MISSING:', s); bad += 1
    if band == 'grades-4-5':
        intro = detex(tex.split('\\begin{document}', 1)[1].split('\\medskip')[0].replace('\\fontsize{12.5}{16.5}\\selectfont', ''))
        ok = intro in text
        print(f'   opening rules found verbatim: {ok}'); bad += not ok
    # puzzle records
    src_k = [[tuple(x.split('/')) for x in m.split(',')] for m in re.findall(r'\\kpuzzle\{([^}]*)\}', tex)]
    src_p = [[tuple(x.split('/')) for x in m.split(',')] for m in re.findall(r'\\puzzlebox\{\d\}\{([^}]*)\}', tex)]
    pdf_k = [pz for pg in D[band] for pz in pg.get('k1_puzzles', [])]
    pdf_p = [g for pg in D[band] for g in pg.get('records', [])]
    if src_k:
        ok = [[(c, int(s)) for c, s in pz] for pz in src_k] == [[tuple(t) for t in pz] for pz in pdf_k]
        print(f'   K-1 drawn tests in source == drawn in PDF: {ok}'); bad += not ok
    if src_p:
        ok = [[(c, int(s)) for c, s in pz] for pz in src_p] == [[tuple(t) for t in pz] for pz in pdf_p]
        print(f'   puzzle records in source == drawn in PDF: {ok}'); bad += not ok

# adult guide: sentence containment
def guide_check(texfile, pdf):
    tex = open(texfile).read().split('\\begin{document}', 1)[1]
    tex = re.sub(r'\\begin\{tikzpicture\}.*?\\end\{tikzpicture\}', ' ', tex, flags=re.S)
    tex = re.sub(r'\\begin\{tabularx\}.*?\\end\{tabularx\}', ' ', tex, flags=re.S)
    tex = re.sub(r'\$[^$]*\$', ' MATH ', tex)
    text = pdf_text(pdf)
    sents = []
    for para in re.split(r'\n\s*\n|\\item|\\\\|\\par\b', tex):
        p = detex(para)
        for s in re.split(r'(?<=[.?!])\s+', p):
            if len(s) >= 30 and 'MATH' not in s:
                sents.append(s.strip())
    miss = [s for s in sents if s not in text]
    print(f'{os.path.basename(pdf)}: {len(sents)} plain sentences from the source; {len(sents) - len(miss)} found in the PDF')
    for s in miss[:15]:
        print('   not matched:', s[:140])
    return len(miss)

guide_check(os.path.join(SRC, 'guide-src', 'facilitator.tex'), 'week-06-facilitator.pdf')

# return visit
rv = open(os.path.join(RV_SRC, 'student', 'return-visit.tex')).read()
text = pdf_text('week-06-return-visit.pdf')
paras = [detex(p) for p in re.findall(r'\n\n([A-Z\\][^\n]*(?:\n[^\n\\][^\n]*)*)', rv.split('\\begin{document}', 1)[1])]
paras = [p for p in paras if len(p) > 40]
miss = [p for p in paras if p not in text]
print(f'return-visit student: {len(paras)} text paragraphs; {len(paras) - len(miss)} found verbatim')
for p in miss:
    print('   MISSING:', p[:140]); bad += 1
guide_check(os.path.join(RV_SRC, 'facilitator.tex'), 'week-06-return-visit-facilitator.pdf')
print(f'student-text mismatches: {bad}')
