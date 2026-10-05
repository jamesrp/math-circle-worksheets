"""My own transcription of every Week 13 board, typed from the rendered pages.

Edges are written tail->head.  Positions are only used to match unlabeled K-1
dots to letters; extract_graphs.py checks every edge set against the PDFs.
s = Start, t = Finish.
"""


def E(spec):
    return [tuple(e.split('>')) for e in spec.split()]


BOARDS = {
    'diamond': (E('s>A s>B A>t B>t'),
                {'s': (0, 0), 'A': (1, 1), 'B': (1, -1), 't': (2, 0)}),
    'greedy': (E('s>A s>B A>B A>t B>t'),
               {'s': (0, 0), 'A': (1, 1), 'B': (1, -1), 't': (2, 0)}),
    'bowtie': (E('s>A s>B A>C B>C C>D C>E D>t E>t'),
               {'s': (0, 0), 'A': (1, 1), 'B': (1, -1), 'C': (2, 0), 'D': (3, 1), 'E': (3, -1), 't': (4, 0)}),
    'doubletrap': (E('s>A s>B A>B A>C B>C C>D C>E D>E D>t E>t'),
                   {'s': (0, 0), 'A': (1, 1), 'B': (1, -1), 'C': (2, 0), 'D': (3, 1), 'E': (3, -1), 't': (4, 0)}),
    'funnel': (E('s>A s>B A>C B>C C>D D>t'),
               {'s': (0, 0), 'A': (3, 1), 'B': (3, -1), 'C': (6, 0), 'D': (9, 0), 't': (14, 0)}),
    'threetwo': (E('s>A s>B s>C A>D B>D C>D D>E D>F E>t F>t'),
                 {'s': (0, 0), 'A': (1, 1), 'B': (1, 0), 'C': (1, -1), 'D': (2, 0), 'E': (3, 1), 'F': (3, -1), 't': (4, 0)}),
    'three': (E('s>A s>B s>C A>t B>t C>t'),
              {'s': (0, 0), 'A': (1, 1), 'B': (1, 0), 'C': (1, -1), 't': (2, 0)}),
    'bottleneck': (E('s>A s>B s>C A>D B>D C>D D>E D>F E>G F>G G>H G>I G>J H>t I>t J>t'),
                   {'s': (0, 0), 'A': (1, 1), 'B': (1, 0), 'C': (1, -1), 'D': (2, 0), 'E': (3, .8), 'F': (3, -.8),
                    'G': (4, 0), 'H': (5, 1), 'I': (5, 0), 'J': (5, -1), 't': (6, 0)}),
    'endpoint_two': (E('s>A s>C A>D C>D D>E D>F E>G F>G G>H G>I G>J H>t I>t J>t'),
                     {'s': (0, 0), 'A': (1, 1), 'C': (1, -1), 'D': (2, 0), 'E': (3, .8), 'F': (3, -.8),
                      'G': (4, 0), 'H': (5, 1), 'I': (5, 0), 'J': (5, -1), 't': (6, 0)}),
    'backward': (E('s>A s>B A>C B>D C>t D>t B>A C>D C>B'),
                 {'s': (0, 0), 'A': (4, 1), 'B': (4, -1), 'C': (10, 1), 'D': (10, -1), 't': (14, 0)}),
    'staircase': (E('s>A s>B s>C A>D B>D B>E C>E C>F D>t E>t F>t'),
                  {'s': (0, 0), 'A': (1, 1), 'B': (1, 0), 'C': (1, -1), 'D': (2.5, 1), 'E': (2.5, 0), 'F': (2.5, -1), 't': (3.5, 0)}),
    # Return visit (S, T are the endpoints there; written s, t here)
    'hub': (E('s>A s>B A>H B>H H>C H>D C>t D>t'),
            {'s': (0, 0), 'A': (1, 1), 'B': (1, -1), 'H': (2, 0), 'C': (3, 1), 'D': (3, -1), 't': (4, 0)}),
    'hub_bypass': (E('s>A s>B A>H B>H H>C H>D C>t D>t A>C'),
                   {'s': (0, 0), 'A': (1, 1), 'B': (1, -1), 'H': (2, 0), 'C': (3, 1), 'D': (3, -1), 't': (4, 0)}),
    'pairs': (E('P>A Q>B A>X B>Y A>C B>C C>D D>X D>Y'), {}),
    'capacity3': (E('s>A s>B A>C B>C C>t A>t'), {}),
    'capacity4': (E('s>A s>B A>C B>C C>t A>t'), {}),
}

CAPACITY = {
    'capacity3': {('s', 'A'): 3, ('s', 'B'): 2, ('A', 'C'): 2, ('B', 'C'): 2, ('C', 't'): 3, ('A', 't'): 1},
    'capacity4': {('s', 'A'): 3, ('s', 'B'): 2, ('A', 'C'): 2, ('B', 'C'): 2, ('C', 't'): 4, ('A', 't'): 1},
}

# What I read on each printed page: (band file, page) -> list of (board, set of thick arrows)
R1 = {('s', 'A'), ('A', 'B'), ('B', 't')}
RD = {('s', 'A'), ('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'E'), ('E', 't')}
RS = {('s', 'B'), ('B', 'D'), ('D', 't'), ('s', 'C'), ('C', 'E'), ('E', 't')}
RB = {('s', 'A'), ('A', 'D'), ('D', 'E'), ('E', 'G'), ('G', 'H'), ('H', 't'),
      ('s', 'C'), ('C', 'D'), ('D', 'F'), ('F', 'G'), ('G', 'J'), ('J', 't')}
N = set()
EXPECTED = {
    ('k-1', 1): [('greedy', N), ('bowtie', N)],
    ('k-1', 2): [('diamond', N), ('funnel', N)],
    ('k-1', 3): [('threetwo', N), ('three', N)],
    ('k-1', 4): [('threetwo', N), ('greedy', N)],
    ('k-1', 5): [('bowtie', N)] * 9,
    ('k-1', 6): [('diamond', N), ('greedy', N)],
    ('grades-2-3', 1): [('bowtie', N), ('greedy', N)],
    ('grades-2-3', 2): [('bottleneck', N)],
    ('grades-2-3', 3): [('bowtie', N)],
    ('grades-2-3', 4): [('bottleneck', N), ('endpoint_two', N)],
    ('grades-2-3', 5): [('greedy', R1), ('doubletrap', RD)],
    ('grades-2-3', 6): [('greedy', N), ('doubletrap', N)],
    ('grades-2-3', 7): [('diamond', N), ('greedy', N)],
    ('grades-4-5', 1): [('greedy', R1), ('doubletrap', RD)],
    ('grades-4-5', 2): [('greedy', N), ('doubletrap', N)],
    ('grades-4-5', 3): [('bottleneck', N)],
    ('grades-4-5', 4): [('backward', N), ('backward', N)],
    ('grades-4-5', 5): [('backward', N)],
    ('grades-4-5', 6): [('staircase', RS), ('staircase', N)],
    ('grades-4-5', 7): [('bottleneck', RB)],
    # facilitator guide figures (ReportLab)
    ('facilitator', 3): [('diamond', N), ('greedy', N)],
    ('facilitator', 4): [('bowtie', N), ('funnel', N)],
    ('facilitator', 5): [('threetwo', N), ('three', N)],
    ('facilitator', 7): [('bottleneck', N), ('doubletrap', RD)],
    ('facilitator', 8): [('backward', N)],
    ('facilitator', 9): [('staircase', RS)],
}
LETTERED = {'grades-2-3', 'grades-4-5', 'facilitator'}
