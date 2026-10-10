"""My own transcription of every board on the Week 9 student pages, typed from
the pages rendered with pdftoppm at 90 dpi, not from the packet's sources.

Each entry: (w, h, kind, extra) with
  kind  'table'  thick walls all round;  'blank' grid without walls;
        'sheet'  thick walls with inner thick copy lines;  'fold' walls with dashed fold lines;
  extra dict: dot ('BL' / 'BR' / None), label (text under it), box (answer box under it),
        lines (inner thick or dashed x and y positions, in squares), side (inches).
Listed per page in reading order (top row first, left to right).
"""

K1 = {
    1: [(5, 3, 'table', dict(dot='BL', side=0.5, rules=True)),      # rules picture with arrow
        (3, 5, 'table', dict(dot='BL', side=0.75)),
        (3, 5, 'table', dict(dot='BR', side=0.75))],
    2: [(2, 2, 'table', dict(dot='BL', side=0.75)), (1, 3, 'table', dict(dot='BL', side=0.75)),
        (2, 1, 'table', dict(dot='BL', side=0.75)),
        (2, 3, 'table', dict(dot='BL', side=0.75)), (3, 3, 'table', dict(dot='BL', side=0.75)),
        (3, 2, 'table', dict(dot='BL', side=0.75))],
    3: [(1, 4, 'table', dict(dot='BL', box=True, side=0.75)), (1, 5, 'table', dict(dot='BL', box=True, side=0.75)),
        (2, 5, 'table', dict(dot='BL', box=True, side=0.75)), (3, 4, 'table', dict(dot='BL', box=True, side=0.75))],
    4: [(1, 2, 'table', dict(dot='BL', box=True, side=0.75)), (2, 4, 'table', dict(dot='BL', box=True, side=0.75)),
        (3, 6, 'table', dict(dot='BL', box=True, side=0.75))],
    5: [(2, 3, 'table', dict(dot='BL', box=True, side=0.75)), (4, 6, 'table', dict(dot='BL', box=True, side=0.75))],
    6: [(3, 3, 'blank', dict(dot='BL', side=0.75))] * 6,
    7: [(4, 4, 'blank', dict(dot='BL', side=0.75))] * 4,
    8: [(2, 2, 'fold', dict(dot='BL', lines=([1], []), side=0.75)), (1, 2, 'table', dict(dot='BL', side=0.75)),
        (3, 3, 'fold', dict(dot='BL', lines=([1, 2], []), side=0.75)), (1, 3, 'table', dict(dot='BL', side=0.75)),
        (4, 4, 'fold', dict(dot='BL', lines=([2], []), side=0.75)), (2, 4, 'table', dict(dot='BL', side=0.75))],
}
K1_ICONS = {6: ['TL', 'BR', 'TR'], 7: ['BL']}   # ring corner of each small picture, top to bottom


def lab(w, h):
    return f'{w} by {h}'


def T(w, h, **kw):
    d = dict(dot='BL', label=lab(w, h), side=0.5)
    d.update(kw)
    return (w, h, 'table', d)


M23 = {
    1: [T(7, 3, side=0.4, rules=True),
        T(2, 3), T(3, 2), T(1, 4), T(3, 4), T(4, 3), T(3, 5)],
    2: [T(1, 2), T(2, 4), T(3, 6), T(1, 3), T(2, 6), T(4, 6)],
    3: [T(5, 10), T(8, 12)],
    4: [(6, 6, 'blank', dict(dot='BL', label='stops at the bottom right after 1 bounce', side=0.5)),
        (6, 6, 'blank', dict(dot='BL', label='stops at the top right after 4 bounces', side=0.5)),
        (6, 6, 'blank', dict(dot='BL', label='stops at the top left after 7 bounces', side=0.5)),
        (6, 6, 'blank', dict(dot='BL', label='stops at the top right after 3 bounces', side=0.5))],
    5: [(14, 15, 'blank', dict(dot=None, side=0.5))],
    6: [(14, 10, 'blank', dict(dot=None, side=0.5))],
    7: [(6, 6, 'sheet', dict(dot='BL', lines=([2, 4], [3]), side=0.5)), T(2, 3),
        (3, 3, 'sheet', dict(dot='BL', lines=([1, 2], []), side=0.5)), T(1, 3)],
    8: [(14, 10, 'blank', dict(dot=None, side=0.5))],
}

U45 = {
    1: [T(7, 3, side=0.4, rules=True),
        T(2, 3), T(3, 2), T(1, 4), T(3, 4), T(6, 4), T(3, 5)],
    3: [(14, 16, 'blank', dict(dot=None, side=0.5))],
    4: [(8, 9, 'sheet', dict(dot='BL', lines=([2, 4, 6], [3, 6]), side=0.5)), T(2, 3)],
    5: [(13, 13, 'blank', dict(dot='BL', side=0.5))],
    6: [T(6, 10)],
    7: [(14, 12, 'blank', dict(dot=None, side=0.5))],
}
U45_CHART = {2: dict(cols=6, rows=6, xlabels=['1', '2', '3', '4', '5', '6'],
                     ylabels=['1', '2', '3', '4', '5', '6'])}   # bottom-to-top heights, left-to-right widths

# Guide thumbnails (pages 4-5): (w, h, start, caption first line, caption second line)
GUIDE_THUMBS = {
    4: [(3, 5, 'BL', 'left dot', None), (3, 5, 'BR', 'right dot', None),
        (2, 2, 'BL', '2 by 2', 'top right, 0'), (1, 3, 'BL', '1 by 3', 'top right, 2'),
        (2, 1, 'BL', '2 by 1', 'bottom right, 1'), (2, 3, 'BL', '2 by 3', 'bottom right, 3'),
        (3, 3, 'BL', '3 by 3', 'top right, 0'), (3, 2, 'BL', '3 by 2', 'top left, 3')],
    5: [(1, 4, 'BL', '1 by 4', '3 (top left)'), (1, 5, 'BL', '1 by 5', '4 (top right)'),
        (2, 5, 'BL', '2 by 5', '5 (bottom right)'), (3, 4, 'BL', '3 by 4', '5 (top left)'),
        (1, 2, 'BL', '1 by 2', 'top left, 1'), (2, 4, 'BL', '2 by 4', 'top left, 1'),
        (3, 6, 'BL', '3 by 6', 'top left, 1'), (2, 3, 'BL', '2 by 3', 'bottom right, 3'),
        (4, 6, 'BL', '4 by 6', 'bottom right, 3')],
}
