#!/usr/bin/env python3
"""Check every current portable source ZIP: contents, clean rebuild, links.

    python3 lowell-math-circle-year-2/source/zip-sweep/zip_sweep.py contents [ZIP ...]
    python3 lowell-math-circle-year-2/source/zip-sweep/zip_sweep.py build [ZIP ...] [--jobs 2]
    python3 lowell-math-circle-year-2/source/zip-sweep/zip_sweep.py links
    python3 lowell-math-circle-year-2/source/zip-sweep/zip_sweep.py coverage
    python3 lowell-math-circle-year-2/source/zip-sweep/zip_sweep.py report

A current ZIP is any *.zip under lowell-math-circle-year-2/source/ outside archive*/ folders.
ZIP arguments are paths relative to that folder, or unique substrings of them.

contents  Compares each member with the file it packages now. ZIPs written by
          problem-files/package.py are checked against package.py's own inclusion rules
          (so "new in source" is exactly what repackaging would add); the problem-file
          tools copy is reported separately, since a ZIP keeps the tools of the day it was
          packaged. Other ZIPs map <top>/<path> to the week folder, skipping archive*/,
          ZIPs and build folders. Reference PDFs inside a ZIP are matched to print copies.
build     Extracts each ZIP into a fresh folder, runs the package's own build (build.py
          with --out/--work when it takes them, else build.sh as its README says) with no
          network and the checkout hidden, then compares every PDF it wrote with the
          committed print PDF of the same name: page count, pdftotext text, and 50-dpi
          renders (pixels whose grey differs by more than 40). PDFs that are not
          byte-identical are also compared at 100 dpi, by word positions and vector drawings
          (PyMuPDF), and against git history (source commits after the PDF's last commit).
links     Markdown links to ZIPs in the print indexes and source READMEs: broken links and
          ZIPs nothing links to.
coverage  Print PDFs that no ZIP build reproduced.
report    One Markdown row per ZIP and the counts, from the JSON results.

Results go to tmp/zip-sweep/ (contents.json, builds/<id>/result.json and build.log,
links.json, coverage.json, report.md). Run at most two builds at a time on a shared machine.

Rebuild classes: exact (byte-identical), same render (same pages and text, no differing
pixel at 50 dpi), toolchain (same pages, the same text apart from spacing and the minus
sign's glyph, the same number of drawings on every page, and a different PDF producer, so
the difference comes from the TeX or library version), DIFFERS, FAILED.

Requirements: Python 3.11+, numpy, Pillow, PyMuPDF, Poppler (pdfinfo, pdftotext, pdftoppm),
git, and whatever each package needs (pdfLaTeX, XeLaTeX, ReportLab, pypdf). Isolation uses
Linux `unshare` (user, mount and network namespaces); without it builds run unisolated and
the result says so.
"""
import argparse
import concurrent.futures as cf
import difflib
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import time
import zipfile
from collections import Counter
from pathlib import Path

REPO = Path(__file__).resolve().parents[3]
Y2 = REPO / 'lowell-math-circle-year-2'
SRC = Y2 / 'source'
TOOLS = SRC / 'problem-files'
OUT = REPO / 'tmp' / 'zip-sweep'
sys.path.insert(0, str(TOOLS))
import package as pkgtool  # noqa: E402  (package.py's inclusion rules)

PIX_THRESHOLD = 40
ORDER = ['exact', 'same render', 'pixels differ', 'text differs', 'pages differ']
GENERIC_SKIP_DIRS = {'__pycache__', 'build', 'build-state', 'render', 'qa', '.venv', 'output', 'out',
                     'rebuilt', '.build'}


def md5(p: Path) -> str:
    return hashlib.md5(p.read_bytes()).hexdigest()


def run(argv, **kw):
    return subprocess.run(argv, capture_output=True, text=True, **kw)


# ------------------------------------------------------------------ which ZIP is which

def all_zips():
    return [p for p in sorted(SRC.rglob('*.zip'))
            if not any(part.startswith('archive') for part in p.relative_to(SRC).parts)]


def select(patterns):
    zs = all_zips()
    if not patterns:
        return zs
    out = []
    for pat in patterns:
        hit = [z for z in zs if z.relative_to(SRC).as_posix() == pat] or \
              [z for z in zs if pat in z.relative_to(SRC).as_posix()]
        if not hit:
            sys.exit(f'no current ZIP matches {pat}')
        out += [h for h in hit if h not in out]
    return out


def zip_id(z: Path) -> str:
    return z.name[:-4]


def week_folder(z: Path) -> Path:
    """The repository folder a ZIP packages: source/week-NN for a ZIP inside it, else the
    folder named like the ZIP (week-NN-source.zip -> week-NN, week-NN-bonus-source.zip -> week-NN-bonus)."""
    if z.parent != SRC:
        return z.parent
    return SRC / z.name[:-len('-source.zip')]


def week_label(z: Path) -> str:
    m = re.match(r'week-(\d+)(.*)', week_folder(z).name)
    n, rest = int(m.group(1)), m.group(2)
    if rest == '-encore':
        return f'{n}e'
    return f'{n} {rest[1:].replace("-", " ")}' if rest else str(n)


def print_folder(z: Path) -> Path:
    f = week_folder(z).name
    if f == 'week-01-encore':
        return Y2 / f
    return Y2 / f'week-{int(re.match(r"week-(\d+)", f).group(1)):02d}'


def zip_mode(names):
    top = names[0].split('/')[0]
    if f'{top}/problem-files/tools/atoms.py' in names:
        return top, 'editable'      # package.py: editable/ + problem-files/ + problem-files/tools/
    if f'{top}/tools/atoms.py' in names:
        return top, 'flat'          # package.py --flat: the week folder + tools/
    return top, 'plain'             # another packager: <top>/ is the folder


# ------------------------------------------------------------------ contents

def plain_files(root: Path):
    for f in sorted(root.rglob('*')):
        rel = f.relative_to(root)
        if f.is_dir() or rel.parts[0].startswith('archive') or f.suffix in ('.zip', '.pyc'):
            continue
        if GENERIC_SKIP_DIRS & set(rel.parts[:-1]):
            continue
        yield rel, f


def expected_entries(z: Path, top: str, mode: str):
    week = week_folder(z)
    entries, tools = {}, set()
    if mode == 'editable':
        for rel, f in pkgtool.editable_files(week / 'editable'):
            entries[f'{top}/{rel.as_posix()}'] = f
        for rel, f in pkgtool.week_files(week):
            entries[f'{top}/problem-files/{rel.as_posix()}'] = f
        tool_dir = f'{top}/problem-files/tools'
    elif mode == 'flat':
        for rel, f in pkgtool.week_files(week, flat=True):
            entries[f'{top}/{rel.as_posix()}'] = f
        tool_dir = f'{top}/tools'
    else:
        root = week / 'editable' if (z.parent != SRC and (week / 'editable').is_dir()) else week
        for rel, f in plain_files(root):
            entries[f'{top}/{rel.as_posix()}'] = f
        return entries, tools
    for n in pkgtool.TOOL_FILES:
        entries[f'{tool_dir}/{n}'] = TOOLS / n
        tools.add(f'{tool_dir}/{n}')
    return entries, tools


def contents_one(z: Path):
    zf = zipfile.ZipFile(z)
    names = [n for n in zf.namelist() if not n.endswith('/')]
    top, mode = zip_mode(names)
    expected, tools = expected_entries(z, top, mode)
    zip_only, new_in_source, differ, tools_differ = [], [], [], []
    for n in names:
        if n not in expected:
            zip_only.append(n)
        elif zf.read(n) != expected[n].read_bytes():
            (tools_differ if n in tools else differ).append(n)
    for a in expected:
        if a not in names:
            (tools_differ if a in tools else new_in_source).append(a)
    pf = print_folder(z)
    prints = {md5(p): p.name for p in pf.glob('*.pdf')} if pf.is_dir() else {}
    refs = {n: prints.get(hashlib.md5(zf.read(n)).hexdigest())
            for n in names if '/reference-pdfs/' in n and n.endswith('.pdf')}
    suspicious = {n for n in names if re.search(
        r'(__pycache__|\.pyc$|\.log$|\.aux$|/build/|/build-state/|/render/|/\.venv/|\.DS_Store|(^|/)\.env$|/tmp/)', n)}
    suspicious |= {n for n in names if n.endswith('.pdf') and '/reference-pdfs/' not in n and '/approved-examples/' not in n}
    return {'zip': z.relative_to(SRC).as_posix(), 'week': week_label(z), 'folder': week_folder(z).relative_to(REPO).as_posix(),
            'mode': mode, 'top': top, 'members': len(names), 'zip_only': zip_only, 'new_in_source': new_in_source,
            'differ': differ, 'tools_differ': tools_differ, 'refs': refs, 'suspicious': sorted(suspicious)}


def cmd_contents(args):
    OUT.mkdir(parents=True, exist_ok=True)
    path = OUT / 'contents.json'
    old = {r['zip']: r for r in json.loads(path.read_text())} if path.exists() and args.zips else {}
    for z in select(args.zips):
        r = contents_one(z)
        old[r['zip']] = r
        stale = len(r['zip_only']) + len(r['new_in_source']) + len(r['differ'])
        refs_off = sum(v is None for v in r['refs'].values())
        print(f"{'STALE' if stale else 'ok':<6} {r['zip']:<66} {r['mode']:<8} only-in-zip {len(r['zip_only'])} "
              f"new-in-source {len(r['new_in_source'])} differ {len(r['differ'])} tools-differ {len(r['tools_differ'])} "
              f"refs-not-print {refs_off} suspicious {len(r['suspicious'])}")
    path.write_text(json.dumps(list(old.values()), indent=1))


# ------------------------------------------------------------------ builds

def hide_root() -> Path:
    """The top-level folder holding the checkout (e.g. /home); hidden during builds."""
    return Path('/' + REPO.parts[1])


ISOLATE = ('set -e; mount --make-rprivate /; T=$(mktemp -d); mount --bind "$1" "$T"; '
           'mount -t tmpfs tmpfs "$3"; mkdir -p "$1"; mount --bind "$T" "$1"; cd "$2"; shift 3; exec "$@"')


def can_isolate():
    if not shutil.which('unshare'):
        return False
    return run(['unshare', '-rmn', 'true']).returncode == 0


def command_in(base: Path, cwd: Path, argv, isolate: bool):
    """argv to run in cwd: no network, and only base visible inside the folder holding the checkout."""
    if not isolate:
        return argv, cwd
    return ['unshare', '-rmn', 'sh', '-c', ISOLATE, 'sh', str(base), str(cwd), str(hide_root())] + list(argv), None


def help_text(base: Path, pkg: Path, isolate: bool):
    argv, cwd = command_in(base, pkg, [sys.executable, 'build.py', '--help'], isolate)
    try:
        r = run(argv, cwd=cwd, timeout=120)
        return r.stdout + r.stderr
    except subprocess.TimeoutExpired:
        return ''


def build_command(base: Path, x: Path, top: str, isolate: bool):
    """The package's own build: build.py (with --out and --work when it takes them), else build.sh."""
    pkg = x / top
    readme = (pkg / 'README.md').read_text(errors='replace') if (pkg / 'README.md').exists() else ''
    if (pkg / 'build.py').exists():
        h = help_text(base, pkg, isolate)
        argv = [sys.executable, f'{top}/build.py']
        note = 'python3 build.py'
        if '--out' in h:
            argv += ['--out', str(x / 'out')]
            note += ' --out OUT'
        if '--work' in h:
            argv += ['--work', str(x / 'work')]
            note += ' --work WORK'
        return x, argv, note
    if (pkg / 'build.sh').exists():
        if re.search(r'build\.sh\s+(/|<|\S*out)', readme):
            return pkg, ['sh', 'build.sh', str(x / 'out')], 'sh build.sh OUT'
        return pkg, ['bash', 'build.sh'], 'bash build.sh'
    return pkg, None, 'no build entry point'


def snapshot(x: Path):
    return {p.relative_to(x).as_posix(): md5(p) for p in x.rglob('*') if p.is_file()}


def producer(p: Path):
    m = re.search(r'^Producer:\s+(.*)$', run(['pdfinfo', str(p)]).stdout, re.M)
    return m.group(1).strip() if m else ''


def pdf_pages(p: Path):
    m = re.search(r'^Pages:\s+(\d+)', run(['pdfinfo', str(p)]).stdout, re.M)
    return int(m.group(1)) if m else None


DATE_RE = re.compile(r'\b(20\d\d-\d\d-\d\d([ T]\d\d:\d\d(:\d\d)?)?|D:\d{14}\S*)\b')


def pdf_text_pages(p: Path):
    t = subprocess.run(['pdftotext', '-q', str(p), '-'], capture_output=True).stdout.decode('utf-8', 'replace')
    pages = t.split('\f')
    if pages and not pages[-1].strip():
        pages = pages[:-1]
    return ['\n'.join(l.rstrip() for l in DATE_RE.sub('<date>', pg).splitlines() if l.strip()) for pg in pages]


def loose(text):
    return re.sub(r'\s+', '', text.replace('\u2212', '\u2013'))


def renders(p: Path, d: Path, dpi: int):
    d.mkdir(parents=True, exist_ok=True)
    subprocess.run(['pdftoppm', '-r', str(dpi), '-gray', str(p), str(d / 'p')], check=True, capture_output=True)
    return sorted(d.glob('p-*.pgm'))


def pixel_diffs(a: Path, b: Path, dpi: int):
    """Per page: differing pixels, or None (page missing) / -1 (page size differs)."""
    import numpy as np
    from PIL import Image
    with tempfile.TemporaryDirectory() as t:
        ra, rb = renders(a, Path(t) / 'a', dpi), renders(b, Path(t) / 'b', dpi)
        out = []
        for i in range(max(len(ra), len(rb))):
            if i >= len(ra) or i >= len(rb):
                out.append(None)
                continue
            ia = np.asarray(Image.open(ra[i]), dtype=np.int16)
            ib = np.asarray(Image.open(rb[i]), dtype=np.int16)
            out.append(int((np.abs(ia - ib) > PIX_THRESHOLD).sum()) if ia.shape == ib.shape else -1)
    return out


def page_structure(page):
    words = [(w[4].replace('\u2212', '\u2013'), w[0], w[1]) for w in page.get_text('words')]
    draws = sorted((round(d['rect'].x0, 1), round(d['rect'].y0, 1), round(d['rect'].x1, 1), round(d['rect'].y1, 1))
                   for d in page.get_drawings())
    return words, draws


def struct_compare(a: Path, b: Path):
    """Per page: words equal, largest word shift, drawing counts, largest drawing shift (points)."""
    import pymupdf
    A, B = pymupdf.open(a), pymupdf.open(b)
    pages = []
    for i in range(min(len(A), len(B))):
        wa, da = page_structure(A[i])
        wb, db = page_structure(B[i])
        same = [w[0] for w in wa] == [w[0] for w in wb]
        wshift = max((max(abs(x[1] - y[1]), abs(x[2] - y[2])) for x, y in zip(wa, wb)), default=0) if same else None
        dshift = None
        if len(da) == len(db):
            rest, dshift = list(db), 0.0
            for r in da:
                j = min(range(len(rest)), key=lambda k: sum(abs(r[t] - rest[k][t]) for t in range(4)))
                dshift = max(dshift, max(abs(r[t] - rest[j][t]) for t in range(4)))
                rest.pop(j)
        pages.append({'page': i + 1, 'words_equal': same, 'word_shift': None if wshift is None else round(wshift, 2),
                      'drawings': [len(da), len(db)], 'drawing_shift': None if dshift is None else round(dshift, 2)})
    return pages


def git(*a):
    return run(['git', '-C', str(REPO)] + list(a)).stdout


def history(folder: str, pdf: str):
    """The PDF's last commit and the commits after it that touched the package's folder."""
    last = git('log', '-1', '--format=%H %cI', '--', pdf).split()
    if not last:
        return None
    later = git('log', '--format=%h %cI %s', f'{last[0]}..HEAD', '--', folder,
                f':(exclude){folder}/archive*', f':(exclude){folder}/*/archive*').strip().splitlines()
    return {'pdf_commit': last[0][:7], 'pdf_date': last[1], 'source_commits_after': later}


def compare_pdf(built: Path, ref: Path):
    r = {'committed': ref.relative_to(REPO).as_posix(), 'producers': [producer(built), producer(ref)]}
    if md5(built) == md5(ref):
        r.update(verdict='exact')
        return r
    pa, pb = pdf_pages(built), pdf_pages(ref)
    ta, tb = pdf_text_pages(built), pdf_text_pages(ref)
    tdiff = [i + 1 for i in range(max(len(ta), len(tb))) if i >= len(ta) or i >= len(tb) or ta[i] != tb[i]]
    px = pixel_diffs(built, ref, 50)
    r.update(pages=[pa, pb], text_diff_pages=tdiff, px50=px)
    if pa != pb or any(not isinstance(v, int) or v < 0 for v in px):
        r['verdict'] = 'pages differ'
    elif tdiff:
        r['verdict'] = 'text differs'
    elif all(v == 0 for v in px):
        r['verdict'] = 'same render'
    else:
        r['verdict'] = 'pixels differ'
    if tdiff:
        snippets = []
        for i in tdiff[:4]:
            a = ta[i - 1].splitlines() if i <= len(ta) else []
            b = tb[i - 1].splitlines() if i <= len(tb) else []
            d = [l for l in difflib.unified_diff(b, a, 'committed', 'built', n=0, lineterm='')
                 if not l.startswith(('---', '+++', '@@'))]
            snippets.append({'page': i, 'diff': d[:12]})
        r['text_snippets'] = snippets
    r['loose_text_equal'] = pa == pb and loose(''.join(ta)) == loose(''.join(tb))
    r['px100'] = pixel_diffs(built, ref, 100)
    try:
        r['structure'] = struct_compare(built, ref)
    except Exception as e:  # noqa: BLE001
        r['structure'] = f'error: {e}'
    r['class'] = classify(r)
    return r


def classify(c):
    if c['verdict'] in ('exact', 'same render'):
        return c['verdict']
    st = c.get('structure')
    if (c['verdict'] in ('pixels differ', 'text differs') and c.get('loose_text_equal')
            and isinstance(st, list) and all(p['drawings'][0] == p['drawings'][1] for p in st)
            and c['producers'][0] != c['producers'][1]):
        return 'toolchain'
    return 'DIFFERS'


ALIASES = {
    'facilitator-guide.pdf': ['{w}-facilitator.pdf'],
    'facilitator.pdf': ['{w}-facilitator.pdf'],
    'guide.pdf': ['{w}-facilitator.pdf'],
    'students.pdf': ['{w}-students.pdf'],
    'student.pdf': ['{w}-students.pdf'],
    'materials.pdf': ['{w}-materials.pdf'],
}


def committed_for(z: Path, built: Path, refs_by_name):
    """The print PDF a built PDF should equal: same name; for return-visit and bonus packages
    the companion's student or facilitator copy; week-NN-<name>; the print copy equal to the
    package's reference copy of that name; or a known alias."""
    pf = print_folder(z)
    w, name = pf.name, built.name
    if (pf / name).exists():
        return pf / name
    folder = week_folder(z).name
    if folder.endswith(('-return-visit', '-bonus')):
        suffix = folder[len(w):]
        cand = pf / (f'{w}{suffix}-facilitator.pdf' if ('facilitator' in name or 'guide' in name) else f'{w}{suffix}.pdf')
        return cand if cand.exists() else None
    if (pf / f'{w}-{name}').exists():
        return pf / f'{w}-{name}'
    if name in refs_by_name:
        for p in pf.glob('*.pdf'):
            if md5(p) == refs_by_name[name]:
                return p
    for pat in ALIASES.get(name, []):
        if (pf / pat.format(w=w)).exists():
            return pf / pat.format(w=w)
    return None


def build_one(z: Path, isolate: bool):
    base = OUT / 'builds' / zip_id(z)
    if base.exists():
        shutil.rmtree(base)
    x = base / 'x'
    x.mkdir(parents=True)
    with zipfile.ZipFile(z) as zf:
        names = [n for n in zf.namelist() if not n.endswith('/')]
        top, mode = zip_mode(names)
        zf.extractall(x)
        for info in zf.infolist():
            bits = (info.external_attr >> 16) & 0o777
            if bits and not info.filename.endswith('/'):
                os.chmod(x / info.filename, bits | 0o600)
        refs_by_name = {n.rsplit('/', 1)[1]: hashlib.md5(zf.read(n)).hexdigest()
                        for n in names if '/reference-pdfs/' in n and n.endswith('.pdf')}
    before = snapshot(x)
    cwd, argv, note = build_command(base, x, top, isolate)
    res = {'zip': z.relative_to(SRC).as_posix(), 'week': week_label(z), 'top': top, 'mode': mode,
           'command': note, 'isolated': isolate}
    t0 = time.time()
    if argv is None:
        res.update(status='no build', seconds=0)
    else:
        env = {k: v for k, v in os.environ.items() if k != 'PYTHONPATH'}
        full, run_cwd = command_in(base, cwd, argv, isolate)
        with (base / 'build.log').open('w') as f:
            try:
                p = subprocess.run(full, cwd=run_cwd, env=env, stdout=f, stderr=subprocess.STDOUT, timeout=3600)
                res['returncode'] = p.returncode
            except subprocess.TimeoutExpired:
                res['returncode'] = 'timeout'
        res['seconds'] = round(time.time() - t0)
        res['status'] = 'built' if res['returncode'] == 0 else 'failed'
        res['log_tail'] = (base / 'build.log').read_text(errors='replace').splitlines()[-15:]
    after = snapshot(x)
    produced = sorted(k for k, v in after.items() if k.endswith('.pdf') and before.get(k) != v
                      and '/reference-pdfs/' not in k and '/approved-examples/' not in k)
    comps, unmatched = [], []
    for rel in produced:
        ref = committed_for(z, x / rel, refs_by_name)
        if ref is None:
            unmatched.append(rel)
            continue
        c = compare_pdf(x / rel, ref)
        c['built'] = rel
        c.setdefault('class', c['verdict'])
        comps.append(c)
    best, extra = {}, []

    def rank(c):
        return ORDER.index(c['verdict']), Path(c['built']).name != Path(c['committed']).name, len(c['built'])
    for c in comps:  # an intermediate copy of the same PDF: keep the best match, list the others
        k = c['committed']
        if k not in best or rank(c) < rank(best[k]):
            if k in best:
                extra.append(best[k])
            best[k] = c
        else:
            extra.append(c)
    folder = week_folder(z).relative_to(REPO).as_posix()
    for c in best.values():
        if c['verdict'] != 'exact':
            c['history'] = history(folder, c['committed'])
    res['comparisons'] = list(best.values())
    res['intermediates'] = [{'built': c['built'], 'committed': c['committed'], 'verdict': c['verdict']} for c in extra]
    res['unmatched'] = unmatched
    pf = print_folder(z)
    expected = {p.name for h in refs_by_name.values() for p in pf.glob('*.pdf') if md5(p) == h}
    res['refs_not_rebuilt'] = sorted(expected - {Path(c['committed']).name for c in res['comparisons']})
    (base / 'result.json').write_text(json.dumps(res, indent=1))
    return res


def rebuild_class(res):
    if res.get('status') != 'built':
        return 'FAILED'
    if res.get('unmatched') or res.get('refs_not_rebuilt') or not res.get('comparisons'):
        return 'DIFFERS'
    classes = [c['class'] for c in res['comparisons']]
    for k in ('DIFFERS', 'toolchain', 'same render'):
        if k in classes:
            return k
    return 'exact'


def cmd_build(args):
    zs = select(args.zips)
    isolate = can_isolate() and not args.no_isolate
    print(f'{len(zs)} builds, {args.jobs} at a time, {"isolated" if isolate else "NOT isolated"}', flush=True)
    with cf.ThreadPoolExecutor(max_workers=args.jobs) as ex:
        futs = {ex.submit(build_one, z, isolate): z for z in zs}
        for f in cf.as_completed(futs):
            try:
                r = f.result()
                cls = Counter(c['class'] for c in r['comparisons'])
                print(f"{rebuild_class(r):<12} {r['zip']:<66} {r.get('seconds', 0):>4}s {dict(cls)} "
                      f"unmatched {len(r['unmatched'])} refs-not-rebuilt {len(r['refs_not_rebuilt'])}", flush=True)
            except Exception as e:  # noqa: BLE001
                print(f'ERROR        {futs[f].relative_to(SRC)}: {e!r}', flush=True)


# ------------------------------------------------------------------ links, coverage, report

def cmd_links(args):
    zs = {z.resolve(): z for z in all_zips()}
    linked = {z: [] for z in zs}
    broken = []
    mds = [Y2 / 'README.md', SRC / 'README.md'] + sorted(Y2.glob('*.md'))
    mds += sorted(p for p in SRC.rglob('README.md')
                  if not any(s.startswith('archive') for s in p.relative_to(SRC).parts) and 'editable' not in p.parts)
    seen = []
    for md in mds:
        if md in seen or not md.exists():
            continue
        seen.append(md)
        for m in re.finditer(r'\]\(([^)\s]+?\.zip)(#[^)]*)?\)', md.read_text(errors='replace')):
            target = (md.parent / m.group(1)).resolve()
            if target in linked:
                linked[target].append(md.relative_to(REPO).as_posix())
            elif not target.exists():
                broken.append({'from': md.relative_to(REPO).as_posix(), 'link': m.group(1)})
    res = {'files_scanned': len(seen), 'broken': broken,
           'unlinked': [zs[z].relative_to(SRC).as_posix() for z, v in linked.items() if not v],
           'linked_from': {zs[z].relative_to(SRC).as_posix(): sorted(set(v)) for z, v in linked.items()}}
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / 'links.json').write_text(json.dumps(res, indent=1))
    print(f"scanned {len(seen)} index and README files; broken ZIP links {len(broken)}; unlinked ZIPs {len(res['unlinked'])}")
    for b in broken:
        print('BROKEN  ', b['from'], b['link'])
    for u in res['unlinked']:
        print('UNLINKED', u)


def results():
    return {json.loads(p.read_text())['zip']: json.loads(p.read_text()) for p in (OUT / 'builds').glob('*/result.json')}


def cmd_coverage(args):
    covered = {c['committed'] for r in results().values() for c in r['comparisons']}
    missing = {}
    for pf in sorted(p for p in Y2.glob('week-*') if p.is_dir()):
        for pdf in sorted(pf.glob('*.pdf')):
            if pdf.relative_to(REPO).as_posix() not in covered:
                missing.setdefault(pf.name, []).append(pdf.name)
    (OUT / 'coverage.json').write_text(json.dumps(missing, indent=1))
    print(f'{len(covered)} print PDFs reproduced by a ZIP build; '
          f'{sum(len(v) for v in missing.values())} current print PDFs not built from any ZIP')
    for k, v in missing.items():
        print(f'  {k}: {", ".join(v)}')


def sort_key(label):
    m = re.match(r'(\d+)(e)?(.*)', label)
    return int(m.group(1)), (0.5 if m.group(2) else 0 if not m.group(3) else 1 if 'return' in m.group(3) else 2)


def fmt_shift(v):
    return '<0.1' if v < 0.1 else f'{v:.1f}'


def cmd_report(args):
    contents = {r['zip']: r for r in json.loads((OUT / 'contents.json').read_text())}
    builds = results()
    links = json.loads((OUT / 'links.json').read_text()) if (OUT / 'links.json').exists() else {'unlinked': []}
    regenerated = set(args.regenerated or [])
    organizer = set(args.organizer or [])
    rows, counts = [], Counter()
    for z in sorted(contents, key=lambda k: sort_key(contents[k]['week'])):
        c, b = contents[z], builds.get(z)
        stale = c['zip_only'] or c['new_in_source'] or c['differ']
        cont = 'STALE' if stale else ('regenerated' if z in regenerated else 'ok')
        rb = rebuild_class(b) if b else 'not built'
        counts[f'contents {cont}'] += 1
        counts[f'rebuild {rb}'] += 1
        notes = []
        if b:
            cls = Counter(x['class'] for x in b['comparisons'])
            n = len(b['comparisons'])
            if cls.get('exact') == n:
                notes.append(f'{n} PDFs byte-identical')
            else:
                bits = [f"{cls[k]} {'byte-identical' if k == 'exact' else k}" for k in ('exact', 'same render') if cls.get(k)]
                for x in b['comparisons']:
                    counts[f"pdf {x['class']}"] += 1
                    if x['class'] in ('exact', 'same render'):
                        continue
                    st = x.get('structure') if isinstance(x.get('structure'), list) else []
                    shift = max([max(p['word_shift'] or 0, p['drawing_shift'] or 0) for p in st] or [0])
                    extra = ', minus signs extract as en dashes' if x['verdict'] == 'text differs' else ''
                    bits.append(f"{Path(x['committed']).name} {x['class']}: {max(x.get('px100') or [0])} px at 100 dpi, "
                                f"shifts up to {fmt_shift(shift)} pt{extra}")
                notes.append('; '.join(bits))
            if cls.get('exact') == n:
                counts['pdf exact'] += n
            for k in ('unmatched', 'refs_not_rebuilt'):
                if b.get(k):
                    notes.append(f"{k.replace('_', ' ')}: {', '.join(b[k])}")
        for k, label in (('zip_only', 'only in ZIP'), ('new_in_source', 'new in source'), ('differ', 'differ')):
            if c[k]:
                notes.append(f"{label}: {', '.join(m.split('/', 1)[1] for m in c[k])}")
        if c['tools_differ']:
            notes.append('tools copy older than source/problem-files')
        if z in links['unlinked']:
            notes.append('not linked from an index or README')
        if c['week'] in organizer:
            notes.append('organizer week: checked, not modified')
        rows.append(f"| {c['week']} | `{z}` | {cont} | {rb} | {'; '.join(notes)} |")
    text = '\n'.join(rows) + '\n\n' + '\n'.join(f'- {k}: {v}' for k, v in sorted(counts.items())) + '\n'
    (OUT / 'report.md').write_text(text)
    print(text)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest='cmd', required=True)
    c = sub.add_parser('contents'); c.add_argument('zips', nargs='*'); c.set_defaults(fn=cmd_contents)
    b = sub.add_parser('build'); b.add_argument('zips', nargs='*'); b.add_argument('--jobs', type=int, default=2)
    b.add_argument('--no-isolate', action='store_true'); b.set_defaults(fn=cmd_build)
    sub.add_parser('links').set_defaults(fn=cmd_links)
    sub.add_parser('coverage').set_defaults(fn=cmd_coverage)
    r = sub.add_parser('report'); r.add_argument('--regenerated', nargs='*', help='ZIPs this sweep regenerated')
    r.add_argument('--organizer', nargs='*', help='week labels left for the organizer'); r.set_defaults(fn=cmd_report)
    args = ap.parse_args()
    args.fn(args)


if __name__ == '__main__':
    main()
