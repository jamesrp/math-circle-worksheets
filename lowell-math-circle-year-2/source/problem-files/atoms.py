"""Problem files and the views composed from them.

A week folder holds `week.toml`, `figures.py` and `problems/*.md`. Each problem
file is one atom: TOML front matter between `+++` lines, then `## kind` sections.

    ## prompt [K-1]          band-qualified wording
    ## prompt                default wording for the atom's other bands
    ## text @10,184 w=174    canvas position (mm), text width, optional size=
    ## figure                a Python expression evaluated in figures.py
    ## key / ## key-figure / ## hints    adult-only material for the guide

Consecutive sections of one kind form a slot. For a band, a slot uses the section
whose [bands] include it, else its unqualified section, else nothing.
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
HEAD = re.compile(r'^(?P<kind>[a-z-]+)'
                  r'(?:\s+@(?P<pos>[\d.]+(?:,[\d.]+)?))?'
                  r'(?:\s+w=(?P<w>[\d.]+))?'
                  r'(?:\s+size=(?P<size>\d+))?'
                  r'(?:\s+\[(?P<bands>[^\]]+)\])?\s*$')


@dataclass
class Section:
    kind: str
    body: str
    bands: frozenset | None = None
    x: float | None = None
    y: float | None = None
    w: float | None = None
    size: int | None = None


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

    @property
    def page(self):
        return self.meta.get('page', 'new')

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
        seen = {tuple((s.kind, s.body) for s in self.resolve(b)) for b in self.grades}
        return len(seen) > 1


def parse_atom(path: Path) -> Atom:
    m = re.match(r'\+\+\+\n(.*?)\n\+\+\+\n(.*)', path.read_text(), re.S)
    if not m:
        raise ValueError(f'{path}: missing +++ front matter')
    meta = tomllib.loads(m.group(1))
    sections = []
    for chunk in re.split(r'^## ', m.group(2), flags=re.M)[1:]:
        head, _, body = chunk.partition('\n')
        h = HEAD.match(head.strip())
        if not h:
            raise ValueError(f'{path}: cannot read section heading "## {head}"')
        x = y = None
        if h['pos']:
            nums = [float(v) for v in h['pos'].split(',')]
            x, y = (None, nums[0]) if len(nums) == 1 else nums
        bands = frozenset(b.strip() for b in h['bands'].split(',')) if h['bands'] else None
        if bands and not bands <= set(meta['grades']):
            raise ValueError(f'{path}: section [{h["bands"]}] names a band outside grades')
        sections.append(Section(h['kind'], ' '.join(body.split()), bands, x, y,
                                float(h['w']) if h['w'] else None,
                                int(h['size']) if h['size'] else None))
    return Atom(path, meta, sections)


@dataclass
class Week:
    folder: Path
    meta: dict
    atoms: list[Atom]
    figures: dict = field(repr=False)

    @property
    def bands(self):
        return self.meta['bands']

    def atom(self, ident):
        return next(a for a in self.atoms if a.id == ident)


def load_week(folder: Path) -> Week:
    folder = Path(folder).resolve()
    meta = tomllib.loads((folder / 'week.toml').read_text())
    if meta.get('layout', 'canvas') != 'canvas':
        raise NotImplementedError(f"{folder}: only layout = \"canvas\" is built so far")
    atoms = [parse_atom(p) for p in sorted((folder / 'problems').glob('*.md'))]
    ids = [a.id for a in atoms]
    if len(set(ids)) != len(ids):
        raise ValueError('duplicate problem ids')
    spec = importlib.util.spec_from_file_location(f'figures_{folder.name}', folder / 'figures.py')
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return Week(folder, meta, atoms, {k: getattr(mod, k) for k in dir(mod) if not k.startswith('_')})


# ---------------------------------------------------------------- composing

@dataclass
class Placed:
    atom: Atom
    number: int | None
    page: int


def compose(week: Week, band: str, route: str | None = None) -> list[Placed]:
    """Pick and number the atoms for one band. Numbers follow the full packet,
    so a route subset keeps the numbers the guide uses."""
    placed, number, page = [], 0, 0
    for atom in week.atoms:
        if band not in atom.grades:
            continue
        if atom.numbered:
            number += 1
        if route and atom.route != route:
            continue
        if not placed or atom.page != 'same':
            page += 1
        placed.append(Placed(atom, number if atom.numbered else None, page))
    return placed


def render_atom(week: Week, band: str, p: Placed) -> str:
    style = week.bands[band]
    out = ''
    for s in p.atom.resolve(band):
        if s.kind == 'prompt':
            out += canvas.prob(p.number, s.body, s.y or 0, size=style.get('prompt_size', 13))
        elif s.kind == 'text':
            out += canvas.text(s.x or 0, s.y or 0, s.body, w=s.w or 180, size=s.size or style.get('text_size', 12))
        elif s.kind == 'figure':
            out += eval(s.body, dict(week.figures))
    return out


def student_tex(week: Week, band: str, route: str | None = None, footer_suffix: str = '') -> str:
    style = week.bands[band]
    footer = f"{week.meta['packet']}-{style['tag']}-{week.meta['version']}{footer_suffix}"
    tex = canvas.student_preamble(week.meta['week'], week.meta['topic'], style['header'], footer)
    pages = {}
    for p in compose(week, band, route):
        pages.setdefault(p.page, []).append(render_atom(week, band, p))
    for i, (n, parts) in enumerate(sorted(pages.items())):
        if i:
            tex += '\\newpage\n'
        tex += canvas.PAGE_OPEN + ''.join(parts) + canvas.PAGE_CLOSE
    return tex + '\\end{document}\n'


def where(week: Week, atom: Atom) -> dict:
    """Problem number of an atom in each band's full packet."""
    out = {}
    for band in week.bands:
        for p in compose(week, band):
            if p.atom is atom:
                out[band] = p.number
    return out
