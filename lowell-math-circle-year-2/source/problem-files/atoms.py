"""Problem files and the views composed from them.

A week folder holds `week.toml`, `problems/*.md` and, when its figures are drawn
in Python, `figures.py`. Each problem file is one atom: TOML front matter between
`+++` lines, then `## kind` sections.

    ## prompt [K-1]          band-qualified wording
    ## prompt                default wording for the atom's other bands
    ## text @10,184 w=174    canvas position, text width, optional size=
    ## figure                a Python expression evaluated in figures.py
    ## key / ## key-figure / ## hints    adult-only material for the guide

Consecutive sections of one kind form a slot. For a band, a slot uses the section
whose [bands] include it, else its unqualified section, else nothing.

Two page layouts compose the student packets (README.md, "Layouts"):
  canvas  each page is one fixed TikZ picture and sections carry positions;
  flow    the sections are LaTeX that flows inside the week's template.tex.
"""
from __future__ import annotations

import importlib.util
import re
import sys
import tomllib
from dataclasses import dataclass, field
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))
import canvas  # noqa: E402

STUDENT_KINDS = {'prompt', 'text', 'figure'}
ADULT_KINDS = {'key', 'key-figure', 'hints'}
KINDS = STUDENT_KINDS | ADULT_KINDS
LAYOUTS = ('canvas', 'flow')
ROUTES = ('first', 'return', 'bonus')
PAGES = ('new', 'same')
FRONT_KEYS = {
    'id': 'permanent id, e.g. "w43.chooser-rows"',
    'title': 'short title used in menus and the adult key',
    'grades': 'list of bands, e.g. ["K-1", "2-3"]',
    'route': '"first", "return" or "bonus"; a list; or a table by band',
    'kind': '"problem" (numbered, the default) or "setup" (unnumbered shared rule)',
    'page': '"new" or "same"; or a table by band',
    'scale': '"actual" when the page must print at 100%',
    'kernel': 'one-sentence mathematical idea for the adult key',
    'app': 'the app family or group that ports it',
}
HEAD = re.compile(r'^(?P<kind>[a-z-]+)'
                  r'(?:\s+@(?P<pos>-?[\d.]+(?:,-?[\d.]+)?))?'
                  r'(?:\s+w=(?P<w>[\d.]+))?'
                  r'(?:\s+size=(?P<size>[\d.]+))?'
                  r'(?:\s+\[(?P<bands>[^\]]+)\])?\s*$')
PLACEHOLDER = re.compile(r'<<([A-Za-z_][A-Za-z0-9_-]*)>>')


class ProblemFileError(Exception):
    """A problem file, week.toml or template says something the tools cannot use."""


def _num(text):
    """Keep integers as integers so generated coordinates read as the old builders wrote them."""
    return float(text) if '.' in text else int(text)


def _rel(path: Path) -> str:
    try:
        return str(path.relative_to(Path.cwd()))
    except ValueError:
        return str(path)


@dataclass
class Section:
    kind: str
    raw: str                      # the body as written, without leading or trailing blank lines
    bands: frozenset | None = None
    x: float | None = None
    y: float | None = None
    w: float | None = None
    size: float | None = None
    line: int = 0                 # line of the heading in the problem file
    heading: str = ''

    @property
    def body(self):
        """The body on one line, as canvas text nodes take it."""
        return ' '.join(self.raw.split())

    @property
    def placed(self):
        return self.x is not None or self.y is not None or self.w is not None


@dataclass
class Atom:
    path: Path
    meta: dict
    sections: list[Section]

    def __getattr__(self, name):
        try:
            return self.meta[name]
        except KeyError:
            raise AttributeError(name)

    @property
    def numbered(self):
        return self.meta.get('kind', 'problem') != 'setup'

    def where_in_file(self, s: Section | None = None) -> str:
        return f'{_rel(self.path)}' + (f', line {s.line} "## {s.heading}"' if s else '')

    def page_for(self, band, default):
        value = self.meta.get('page', default)
        if isinstance(value, dict):
            value = value.get(band, default)
        return value

    def routes(self, band) -> set:
        value = self.meta['route']
        if isinstance(value, dict):
            value = value.get(band, [])
        return {value} if isinstance(value, str) else set(value)

    def route_label(self, bands) -> str:
        """`first`, or `K-1 first; 2-3 return` when bands differ."""
        per = {b: '/'.join(sorted(self.routes(b))) for b in bands if b in self.grades}
        if len(set(per.values())) == 1:
            return next(iter(per.values()))
        return '; '.join(f'{b} {r}' for b, r in per.items())

    def slots(self, kinds):
        out = []
        for s in self.sections:
            if s.kind not in kinds:
                continue
            if out and out[-1][0].kind == s.kind:
                out[-1].append(s)
            else:
                out.append([s])
        return out

    def resolve(self, band, kinds=STUDENT_KINDS):
        """The sections a child in `band` sees, in page order."""
        chosen = []
        for slot in self.slots(kinds):
            hit = next((s for s in slot if s.bands and band in s.bands), None)
            hit = hit or next((s for s in slot if not s.bands), None)
            if hit:
                chosen.append(hit)
        return chosen

    def varies(self):
        """True when some band sees different student wording or figures."""
        seen = {tuple((s.kind, s.raw) for s in self.resolve(b)) for b in self.grades}
        return len(seen) > 1


def _check_choice(where, key, value, allowed, bands):
    """Validate a front-matter value that is a string, a list, or a table by band."""
    def one(v, ctx):
        items = [v] if isinstance(v, str) else v
        if not isinstance(items, list) or not items or any(i not in allowed for i in items):
            raise ProblemFileError(f'{where}: {key} {ctx}= {v!r}; use one of {", ".join(map(repr, allowed))}'
                                   + (' or a list of them' if key == 'route' else ''))
        if key == 'page' and len(items) != 1:
            raise ProblemFileError(f'{where}: page takes one value, "new" or "same", not a list')
    if isinstance(value, dict):
        for band, v in value.items():
            if band not in bands:
                raise ProblemFileError(f'{where}: {key} names band "{band}", which is not in grades {bands}')
            one(v, f'for "{band}" ')
    else:
        one(value, '')


def parse_atom(path: Path) -> Atom:
    text = path.read_text()
    m = re.match(r'\+\+\+\n(.*?)\n\+\+\+\n(.*)', text, re.S)
    if not m:
        raise ProblemFileError(f'{_rel(path)}: a problem file starts with TOML front matter between two "+++" lines')
    try:
        meta = tomllib.loads(m.group(1))
    except tomllib.TOMLDecodeError as e:
        raise ProblemFileError(f'{_rel(path)}: front matter is not valid TOML ({e})')
    where = _rel(path)
    unknown = sorted(set(meta) - set(FRONT_KEYS))
    if unknown:
        raise ProblemFileError(f'{where}: unknown front-matter key {", ".join(unknown)}. Known keys: '
                               + '; '.join(f'{k} ({v})' for k, v in FRONT_KEYS.items()))
    for key in ('id', 'title', 'grades', 'route'):
        if key not in meta:
            raise ProblemFileError(f'{where}: front matter needs {key}, the {FRONT_KEYS[key]}')
    if not isinstance(meta['grades'], list) or not meta['grades']:
        raise ProblemFileError(f'{where}: grades must be a list of bands, e.g. ["K-1", "2-3", "4-5"]')
    if meta.get('kind', 'problem') not in ('problem', 'setup'):
        raise ProblemFileError(f'{where}: kind = {meta["kind"]!r}; use "problem" or "setup"')
    _check_choice(where, 'route', meta['route'], ROUTES, meta['grades'])
    if 'page' in meta:
        _check_choice(where, 'page', meta['page'], PAGES, meta['grades'])

    sections = []
    body_start = text[:m.start(2)].count('\n') + 1
    chunks = re.split(r'^## ', m.group(2), flags=re.M)
    if chunks[0].strip():
        raise ProblemFileError(f'{where}: text after the front matter must begin with a "## kind" heading; '
                               f'found "{chunks[0].strip()[:40]}"')
    line = body_start + chunks[0].count('\n')
    for chunk in chunks[1:]:
        head, _, body = chunk.partition('\n')
        h = HEAD.match(head.strip())
        if not h:
            raise ProblemFileError(f'{where}, line {line}: cannot read the heading "## {head}". '
                                   'Write "## kind", then optionally @x,y (or @y), w=, size= and [bands]')
        if h['kind'] not in KINDS:
            raise ProblemFileError(f'{where}, line {line}: "## {h["kind"]}" is not a section kind. '
                                   f'Children see {", ".join(sorted(STUDENT_KINDS))}; '
                                   f'adults see {", ".join(sorted(ADULT_KINDS))}')
        x = y = None
        if h['pos']:
            nums = [_num(v) for v in h['pos'].split(',')]
            x, y = (None, nums[0]) if len(nums) == 1 else nums
        bands = frozenset(b.strip() for b in h['bands'].split(',')) if h['bands'] else None
        if bands and not bands <= set(meta['grades']):
            raise ProblemFileError(f'{where}, line {line}: [{h["bands"]}] names a band outside grades {meta["grades"]}')
        raw = re.sub(r'\A(?:[ \t]*\n)+', '', body).rstrip()
        sections.append(Section(h['kind'], raw, bands, x, y,
                                _num(h['w']) if h['w'] else None,
                                _num(h['size']) if h['size'] else None, line, head.strip()))
        line += chunk.count('\n')
    atom = Atom(path, meta, sections)
    if not atom.numbered and any(s.kind == 'prompt' for s in sections):
        raise ProblemFileError(f'{where}: a setup file is not numbered, so it has no "## prompt"; '
                               'put its rules in "## text"')
    return atom


@dataclass
class Week:
    folder: Path
    meta: dict
    atoms: list[Atom]
    figures: dict = field(repr=False)

    @property
    def bands(self):
        return self.meta['bands']

    @property
    def layout(self):
        return self.meta.get('layout', 'canvas')

    @property
    def default_page(self):
        return 'new' if self.layout == 'canvas' else 'same'

    def atom(self, ident):
        return next(a for a in self.atoms if a.id == ident)

    @property
    def inputs(self):
        """Folders searched for files the LaTeX inputs: the week folder, then week.toml's inputs."""
        return [self.folder] + [(self.folder / d).resolve() for d in self.meta.get('inputs', [])]

    def footer(self, band, suffix=''):
        return f"{self.meta['packet']}-{self.bands[band]['tag']}-{self.meta['version']}{suffix}"


WEEK_KEYS = ('week', 'topic', 'packet', 'version', 'bands')


def load_week(folder: Path) -> Week:
    folder = Path(folder).resolve()
    toml = folder / 'week.toml'
    if not toml.exists():
        raise ProblemFileError(f'{_rel(folder)}: no week.toml; a week folder holds week.toml and problems/')
    try:
        meta = tomllib.loads(toml.read_text())
    except tomllib.TOMLDecodeError as e:
        raise ProblemFileError(f'{_rel(toml)}: not valid TOML ({e})')
    for key in WEEK_KEYS:
        if key not in meta:
            raise ProblemFileError(f'{_rel(toml)}: needs {key} (week, topic, packet, version and [bands."K-1"] ... tables)')
    for band, style in meta['bands'].items():
        for key in ('header', 'tag'):
            if key not in style:
                raise ProblemFileError(f'{_rel(toml)}: [bands."{band}"] needs {key}')
    layout = meta.get('layout', 'canvas')
    if layout not in LAYOUTS:
        raise ProblemFileError(f'{_rel(toml)}: layout = {layout!r}; use "canvas" or "flow"')

    for d in meta.get('inputs', []):
        if not (folder / d).is_dir():
            raise ProblemFileError(f'{_rel(toml)}: inputs names {d!r}, which is not a folder beside week.toml')
    paths = sorted((folder / 'problems').glob('*.md'))
    if not paths:
        raise ProblemFileError(f'{_rel(folder)}/problems/ has no .md problem files')
    atoms = [parse_atom(p) for p in paths]
    seen = {}
    for a in atoms:
        if a.id in seen:
            raise ProblemFileError(f'{_rel(a.path)}: id "{a.id}" is already used by {_rel(seen[a.id].path)}')
        seen[a.id] = a
        extra = [g for g in a.grades if g not in meta['bands']]
        if extra:
            raise ProblemFileError(f'{_rel(a.path)}: grades name {extra}, but week.toml defines only bands '
                                   f'{list(meta["bands"])}')
        for band in a.grades:
            if a.numbered and not any(s.kind == 'prompt' for s in a.resolve(band)):
                raise ProblemFileError(f'{_rel(a.path)}: no "## prompt" reaches band {band}; give the band a '
                                       f'prompt, an untagged prompt, or drop {band} from grades')
        for s in a.sections:
            if layout == 'flow' and s.placed:
                raise ProblemFileError(f'{a.where_in_file(s)}: positions (@x,y, w=, size=) belong to the canvas '
                                       'layout; in flow, sections are LaTeX in reading order')

    figures = {}
    fig_file = folder / 'figures.py'
    if fig_file.exists():
        spec = importlib.util.spec_from_file_location(f'figures_{folder.name.replace("-", "_")}', fig_file)
        mod = importlib.util.module_from_spec(spec)
        sys.dont_write_bytecode, keep = True, sys.dont_write_bytecode   # no __pycache__ in source folders
        try:
            spec.loader.exec_module(mod)
        finally:
            sys.dont_write_bytecode = keep
        figures = {k: getattr(mod, k) for k in dir(mod) if not k.startswith('_')}
    else:
        for a in atoms:
            for s in a.sections:
                if s.kind in ('figure', 'key-figure'):
                    raise ProblemFileError(f'{a.where_in_file(s)}: a figure section calls figures.py, '
                                           f'but {_rel(folder)} has no figures.py (in flow, put LaTeX in "## text")')
    week = Week(folder, meta, atoms, figures)
    if layout == 'flow':
        import flow
        flow.check_template(week)
    return week


def figure(week: Week, atom: Atom, s: Section) -> str:
    """Evaluate a figure section's Python expression in the week's figures.py."""
    try:
        out = eval('(\n' + s.raw + '\n)', dict(week.figures))
    except Exception as e:  # report the problem file, not a traceback into eval
        raise ProblemFileError(f'{atom.where_in_file(s)}: the figure expression failed: '
                               f'{type(e).__name__}: {e}')
    if not isinstance(out, str):
        raise ProblemFileError(f'{atom.where_in_file(s)}: the figure expression returned '
                               f'{type(out).__name__}, not LaTeX text')
    return out


# ---------------------------------------------------------------- composing

@dataclass
class Placed:
    atom: Atom
    number: int | None
    page: int


def compose(week: Week, band: str, route: str | None = None) -> list[Placed]:
    """Pick and number the atoms for one band. Numbers follow the full packet,
    so a route subset keeps the numbers the guide uses.

    `page` counts forced page starts. In canvas, an atom that shares a page
    starts a new one when the atom before it was left out of the view."""
    placed, number, page, prev_kept = [], 0, 0, False
    for atom in week.atoms:
        if band not in atom.grades:
            continue
        if atom.numbered:
            number += 1
        if route and route not in atom.routes(band):
            prev_kept = False
            continue
        new = atom.page_for(band, week.default_page) == 'new'
        if not placed or new or (week.layout == 'canvas' and not prev_kept):
            page += 1
        placed.append(Placed(atom, number if atom.numbered else None, page))
        prev_kept = True
    return placed


@dataclass
class Page:
    """What a canvas week's page_open(page) and page_close(page) are told."""
    number: int     # 1, 2, ... within the view being built
    count: int      # pages in that view
    band: str
    header: str     # the band's header from week.toml
    footer: str     # packet-tag-version, plus -first or -return in a route packet
    week: int
    topic: str


def canvas_hooks(week: Week) -> dict:
    """The canvas page template: the week's figures.py may replace any default.

    Each page is page_open(page) + the page's sections + page_close(page). A week
    whose pages draw their own header, footer or page number defines those two
    functions; otherwise the PAGE_OPEN and PAGE_CLOSE strings are used."""
    names = ('page_preamble', 'page_prompt', 'page_text')
    hooks = {n: week.figures.get(n, getattr(canvas, n)) for n in names}
    for fn, const in (('page_open', 'PAGE_OPEN'), ('page_close', 'PAGE_CLOSE')):
        if fn in week.figures:
            hooks[fn] = _page_hook(week, fn, week.figures[fn])
        else:
            text = week.figures.get(const, getattr(canvas, const))
            hooks[fn] = lambda page, text=text: text
    return hooks


def _page_hook(week: Week, name: str, fn):
    where = _rel(week.folder / 'figures.py')
    if not callable(fn):
        raise ProblemFileError(f'{where}: {name} must be a function of one Page (number, count, band, header, '
                               f'footer, week, topic); for a fixed string use {name.upper()} instead')

    def call(page):
        try:
            out = fn(page)
        except Exception as e:
            raise ProblemFileError(f'{where}: {name}(page) failed on page {page.number} of {page.band}: '
                                   f'{type(e).__name__}: {e}')
        if not isinstance(out, str):
            raise ProblemFileError(f'{where}: {name}(page) returned {type(out).__name__}, not LaTeX text')
        return out
    return call


def render_canvas_atom(week: Week, band: str, p: Placed, hooks: dict) -> str:
    style = week.bands[band]
    out = ''
    for s in p.atom.resolve(band):
        if s.kind == 'prompt':
            out += hooks['page_prompt'](p.number, s.body, s.x, s.y, s.size or style.get('prompt_size'))
        elif s.kind == 'text':
            out += hooks['page_text'](s.x, s.y, s.body, s.w, s.size or style.get('text_size'))
        elif s.kind == 'figure':
            out += figure(week, p.atom, s)
    return out


def student_tex(week: Week, band: str, route: str | None = None, footer_suffix: str = '') -> str:
    placed = compose(week, band, route)
    footer = week.footer(band, footer_suffix)
    if week.layout == 'flow':
        import flow
        return flow.student_tex(week, band, placed, footer)
    hooks = canvas_hooks(week)
    tex = hooks['page_preamble'](week.meta['week'], week.meta['topic'], week.bands[band]['header'], footer)
    pages = {}
    for p in placed:
        pages.setdefault(p.page, []).append(render_canvas_atom(week, band, p, hooks))
    ordered = sorted(pages.items())
    for i, (n, parts) in enumerate(ordered):
        if i:
            tex += '\\newpage\n'
        page = Page(i + 1, len(ordered), band, week.bands[band]['header'], footer, week.meta['week'], week.meta['topic'])
        tex += hooks['page_open'](page) + ''.join(parts) + hooks['page_close'](page)
    return tex + '\\end{document}\n'


def where(week: Week, atom: Atom) -> dict:
    """Problem number of an atom in each band's full packet."""
    out = {}
    for band in week.bands:
        for p in compose(week, band):
            if p.atom is atom:
                out[band] = p.number
    return out
