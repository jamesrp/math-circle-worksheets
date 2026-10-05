"""My own transcription of every Week 14 drawing, typed from the rendered pages.

Key: (pdf file, page) -> list of (corner count, diagonals) for every polygon on
the page, in any order.  Diagonals are written by their two corner labels
(numbers on K-1 pages and K-1 guide figures).  For guide pages the diagonals
are those named in the caption or table next to each picture, so a match also
checks that each guide picture agrees with its caption.
"""

K, M, U, RV, GD = ('week-14-k-1.pdf', 'week-14-grades-2-3.pdf', 'week-14-grades-4-5.pdf',
                   'week-14-return-visit.pdf', 'week-14-facilitator.pdf')


def blank(n, k):
    return [(n, '')] * k


FA5 = 'AC AD'; FB5 = 'BD BE'; FC5 = 'AC CE'; FD5 = 'AD BD'; FE5 = 'BE CE'
FAN_A6 = 'AC AD AE'; CENTRAL6 = 'AC CE AE'; FAN_B6 = 'BD BE BF'; FAN_D6 = 'AD BD DF'
OCT_S = 'AC AD DF DG DH'; OCT_T = 'AE BD BE EG EH'

EXPECTED = {
    # K-1
    (K, 1): blank(5, 3) + blank(6, 3),
    (K, 2): blank(5, 9),
    (K, 3): blank(6, 9),
    (K, 4): [(5, '13')] * 5 + [(6, '14')] * 5,
    (K, 5): [(6, '13 14 15'), (6, '13 15 35')] + blank(6, 8),
    (K, 6): [(5, '13 14')] + blank(5, 8),
    # Grades 2-3
    (M, 1): blank(6, 3) + blank(7, 3),
    (M, 2): blank(5, 9),
    (M, 3): [(6, FAN_A6), (6, CENTRAL6)] + blank(6, 8),
    (M, 4): [(4, 'AC'), (4, 'BD'), (5, FA5), (5, FC5), (5, FE5), (5, FB5), (5, FD5)],
    (M, 5): [(5, FA5)] + blank(5, 8),
    (M, 6): [(6, FAN_B6), (6, FAN_A6)] + blank(6, 9),
    (M, 7): blank(6, 9),
    (M, 8): blank(6, 9),
    # Grades 4-5
    (U, 1): blank(5, 9),
    (U, 2): [(6, FAN_A6), (6, CENTRAL6)] + blank(6, 8),
    (U, 3): [(4, 'AC'), (4, 'BD'), (5, FA5), (5, FC5), (5, FE5), (5, FB5), (5, FD5)],
    (U, 4): [(6, FAN_B6), (6, CENTRAL6), (6, FAN_D6), (6, FAN_A6)] + blank(6, 9),
    (U, 5): [(8, OCT_S)] + blank(8, 8),
    (U, 6): blank(8, 1),
    (U, 7): [(8, OCT_S), (8, OCT_T), (8, '')],
    # Return visit (the "After" example is the quadrilateral A,C,D,E with AD)
    (RV, 1): [(5, 'AC AD'), (5, 'AC AD'), (4, 'AD'), (6, FAN_A6)],
    (RV, 2): [(6, CENTRAL6)],
    (RV, 3): [(6, FAN_A6)] * 3,
    (RV, 4): [(6, CENTRAL6)] * 3,
    (RV, 5): [(6, 'AC'), (6, 'AC DF'), (6, 'DF'), (6, '')],
    (RV, 6): blank(6, 9),
    # Adult guide figures, as captioned
    (GD, 3): [(5, FA5), (5, FB5), (5, FC5), (5, FD5), (5, FE5)],
    (GD, 4): [(5, '13 35'), (5, '13 14'), (6, '14 24 46'), (6, '13 14 46'), (6, '14 15 24'), (6, '13 14 15')],
    (GD, 5): [(6, '13 14 46'), (6, '13 15 35'), (6, '14 15 24'), (6, '13 35 36'), (6, '15 25 35'), (6, '13 14 15')],
    (GD, 7): [(6, 'BD BE BF'), (6, 'AE BD BE'), (6, 'AD AE BD'), (6, 'AC AD AE'),
              (6, 'BD BE BF'), (6, 'BE BF CE'), (6, 'AE BE CE'), (6, 'AC AE CE'), (6, 'AC AD AE')],
    (GD, 8): [(6, d) for d in ['BF CF DF', 'BF CE CF', 'BD BF DF', 'BE BF CE', 'BD BE BF', 'AC CF DF', 'AC CE CF',
                               'AD BD DF', 'AC AD DF', 'AE BE CE', 'AE BD BE', 'AC AE CE', 'AD AE BD', 'AC AD AE']],
    (GD, 9): [(6, 'AC AE CE'), (6, 'AC AD AE'), (6, 'AD BD DF'), (6, 'AC AD DF'), (6, 'AC AD AE')],
    (GD, 10): [(8, OCT_S), (8, 'AC AD AE AF AG'), (8, 'AE BE CE EG EH')],
    (GD, 11): [(4, 'uw'), (4, 'Ax')],
    (GD, 12): [(8, d) for d in [OCT_S, 'AD BD DF DG DH', 'AD BD DG DH EG', 'AD BD DH EG EH', 'AD AE BD EG EH', OCT_T]],
}
