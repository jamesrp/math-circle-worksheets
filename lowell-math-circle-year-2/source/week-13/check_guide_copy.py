#!/usr/bin/env python3
"""Check that the problem files' answer keys still say what the print guide says.

The print guide (week-13-facilitator.pdf) is built from editable/facilitator-src/build_guide.py (ReportLab).
The problem files' key sections repeat its answers by problem for the key view. Every
sentence and table row of a key must appear in the guide's text, after markup is removed.
Run from anywhere:

    python3 lowell-math-circle-year-2/source/week-13/check_guide_copy.py
"""
import ast
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
# The repository keeps the package in editable/; the portable ZIP puts these files in problem-files/ beside it.
GUIDE = next(p for p in (HERE / 'editable/facilitator-src/build_guide.py', HERE.parent / 'facilitator-src/build_guide.py')
             if p.exists())


def words(s):
    """Lower-case words and numbers only: markup and symbols removed."""
    s = re.sub(r'<[^>]+>', ' ', s).replace('&lt;', '<').replace('&gt;', '>')
    s = re.sub(r'\\begin\{tabular\}\{[^}]*\}|\\end\{tabular\}|\\(begin|end)\{center\}|\\(top|mid|bottom)rule|\\(textbf|emph|mbox)\b', ' ', s)
    for a, b in (('^\\circ', ''), ('°', ''), ('→', ' to '), ('\\to', ' to '), ('×', ' times '), ('\\times', ' times '),
                 ('±', ' pm '), ('\\pm', ' pm ')):
        s = s.replace(a, b)
    return ' '.join(re.findall(r'[a-z0-9]+', s.lower()))


def units(text):
    """Sentences, and table rows (split at \\\\)."""
    out = []
    for part in re.split(r'\\\\|\n\s*\n', text):
        out += [u for u in (words(x) for x in re.split(r'(?<=[.:;?])[}’\']*\s+(?=[A-Z(\\])', part)) if u]
    return out


def guide_text():
    """Every string constant of the guide builder, in source order."""
    tree = ast.parse(GUIDE.read_text())
    consts = [n for n in ast.walk(tree) if isinstance(n, ast.Constant) and isinstance(n.value, str)]
    consts.sort(key=lambda n: (n.lineno, n.col_offset))
    return ' ' + ' '.join(words(n.value) for n in consts) + ' '


def main():
    guide = guide_text()
    missing = []
    for f in sorted((HERE / 'problems').glob('*.md')):
        for chunk in re.split(r'^## ', f.read_text(), flags=re.M)[1:]:
            head, _, body = chunk.partition('\n')
            if head.split()[0] not in ('key', 'hints'):
                continue
            missing += [f'{f.name} "## {head.strip()}": {u}' for u in units(body) if f' {u} ' not in guide]
    if missing:
        print('Not in the print guide source:\n  ' + '\n  '.join(missing))
        sys.exit(1)
    print(f'Every key sentence and table row in problems/ appears in {GUIDE.name}.')


if __name__ == '__main__':
    main()
