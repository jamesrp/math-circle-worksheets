"""The flow layout: problem sections are LaTeX that flows inside the week's template.

week.toml names the template and may set how a numbered prompt and a forced
page break are written:

    layout = "flow"
    template = "template.tex"        # the whole document, with <<body>> where problems go
    prompt = '\\textbf{Problem <<n>>:} <<body>>'   # default shown; a band table may override it
    page_break = '\\newpage'          # default shown

The template's other placeholders are filled from week.toml: <<week>>, <<topic>>,
<<header>> and <<tag>> of the band, <<footer>> (packet-tag-version, plus -first or
-return in route packets), <<band>>, and any other string or number set in the
band's table. A band table may also name its own `template`.

The body is built in reading order. Each atom's sections are joined by a blank
line, so every section starts a new paragraph; atoms are joined the same way;
a forced page break (page = "new") goes on its own line between them. Section
bodies are LaTeX kept exactly as written, apart from leading and trailing blank
lines.
"""
from __future__ import annotations

from pathlib import Path

import atoms
from atoms import PLACEHOLDER, ProblemFileError, _rel

DEFAULT_PROMPT = r'\textbf{Problem <<n>>:} <<body>>'
DEFAULT_BREAK = r'\newpage'
FIXED = ('week', 'topic', 'header', 'tag', 'footer', 'band', 'body')


def template_path(week, band) -> Path:
    name = week.bands[band].get('template', week.meta.get('template'))
    if not name:
        raise ProblemFileError(f'{_rel(week.folder / "week.toml")}: layout = "flow" needs template = "template.tex", '
                               'a LaTeX file holding the whole document with <<body>> where the problems go')
    path = week.folder / name
    if not path.exists():
        raise ProblemFileError(f'{_rel(week.folder / "week.toml")}: template {name!r} does not exist in {_rel(week.folder)}')
    return path


def values(week, band, footer='') -> dict:
    style = week.bands[band]
    out = {k: str(v) for k, v in style.items() if isinstance(v, (str, int, float)) and k not in ('template', 'prompt')}
    out.update(week=str(week.meta['week']), topic=week.meta['topic'], header=style['header'],
               tag=style['tag'], footer=footer or week.footer(band), band=band)
    return out


def fill(text: str, vals: dict, where: str) -> str:
    def sub(m):
        if m.group(1) not in vals:
            line = text[:m.start()].count('\n') + 1
            known = ', '.join(f'<<{k}>>' for k in sorted(vals))
            raise ProblemFileError(f'{where}, line {line}: <<{m.group(1)}>> is not defined. Defined here: {known}. '
                                   f'Set other values in the band\'s table in week.toml')
        return vals[m.group(1)]
    return PLACEHOLDER.sub(sub, text)


def check_template(week) -> None:
    """Fail early, with the file and line, on a template that cannot be filled."""
    for key in ('prompt', 'page_break'):
        if key in week.meta and not isinstance(week.meta[key], str):
            raise ProblemFileError(f'{_rel(week.folder / "week.toml")}: {key} must be a string of LaTeX')
    for band in week.bands:
        path = template_path(week, band)
        text = path.read_text()
        if text.count('<<body>>') != 1:
            raise ProblemFileError(f'{_rel(path)}: the template needs <<body>> exactly once, where the problems go '
                                   f'(found {text.count("<<body>>")})')
        fill(text, values(week, band) | {'body': ''}, _rel(path))
        prompt = week.bands[band].get('prompt', week.meta.get('prompt', DEFAULT_PROMPT))
        if '<<body>>' not in prompt:
            raise ProblemFileError(f'{_rel(week.folder / "week.toml")}: prompt = {prompt!r} needs <<body>> '
                                   '(and usually <<n>>)')
        fill(prompt, {'n': '1', 'body': ''}, f'{_rel(week.folder / "week.toml")} prompt')


def render_atom(week, band, p) -> str:
    fmt = week.bands[band].get('prompt', week.meta.get('prompt', DEFAULT_PROMPT))
    parts = []
    for s in p.atom.resolve(band):
        if s.kind == 'prompt':
            parts.append(fill(fmt, {'n': str(p.number), 'body': s.raw}, 'prompt'))
        elif s.kind == 'text':
            parts.append(s.raw)
        elif s.kind == 'figure':
            parts.append(atoms.figure(week, p.atom, s))
    return '\n\n'.join(parts)


def student_tex(week, band, placed, footer) -> str:
    page_break = week.meta.get('page_break', DEFAULT_BREAK)
    chunks, page = [], None
    for p in placed:
        if page is not None and p.page != page:
            chunks.append(page_break)
        page = p.page
        chunks.append(render_atom(week, band, p))
    path = template_path(week, band)
    return fill(path.read_text(), values(week, band, footer) | {'body': '\n\n'.join(chunks)}, _rel(path))
