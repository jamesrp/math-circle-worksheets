# Independent check of Week 94 K-1 Problems 4-6, read from the problem-file TikZ.
import re, sys, itertools
src = sys.argv[1]
p12 = open(src + '/12-every-hidden-pair.md').read()
p14 = open(src + '/14-known-strip-rows.md').read()
tmpl = open(src + '/../template.tex').read()

# Drawn heights
out = [int(h) for h in re.findall(r'\\tcubes\{[^}]*\}\{0\}\{(\d)\}', p12.split('## text [K-1]')[1].split('## text')[0])]
print('P5 drawn outputs (P, Q):', out)
slots = len(re.findall(r'\\foreach\\s in\{0,\.\.\.,(\d)\}', p12))
nslots = int(re.search(r'\\foreach\\s in\{0,\.\.\.,(\d)\}', p12).group(1)) + 1
cells5 = int(re.search(r'\\tcells\{6\+4\*\\s\}\{0\}\{(\d)\}', p12).group(1))
print('P5 answer slots:', nslots, 'cells per column:', cells5)
rows = [tuple(map(int, t)) for t in re.findall(r'(\d)/(\d)/(\d)', p14)]
known = [(a, b) for i, a, b in rows]
cells6 = int(re.search(r'\\tcells\{1\.4\}\{-9\.8\}\{(\d)\}', p14).group(1))
print('P6 known towers (in, out):', known, 'cells per column:', cells6)
ex = re.search(r'in: (\d) cubes.*?add (\d) extra.*?out: (\d) cubes', tmpl, re.S).groups()
print('worked example:', ex)

P, Q = out
EXTRAS = (1, 2, 3)
# P5: brute force over inputs >= 1 and shared extra
worlds = sorted({(p, q, c) for p in range(0, 13) for q in range(0, 13) for c in EXTRAS
                 if p >= 1 and q >= 1 and p + c == P and q + c == Q})
print('P5 shared-extra worlds:', worlds, '| Q-P always', {q - p for p, q, c in worlds})
assert len(worlds) <= nslots and max(q for _, q, _ in worlds) <= cells5
# Misreading: each tower gets its own extra
indep = sorted({(p, q) for c1 in EXTRAS for c2 in EXTRAS for p in [P - c1] for q in [Q - c2] if p >= 1 and q >= 1})
print('P5 if extras were independent:', len(indep), 'pairs', indep, '| P==Q possible:', any(p == q for p, q in indep))
# Guide extension: extras up to 5
for allow0 in (False, True):
    w5 = sorted({(P - c, Q - c, c) for c in range(1, 6) if P - c >= (0 if allow0 else 1) and Q - c >= (0 if allow0 else 1)})
    print('extras 1-5, empty tower allowed=%s:' % allow0, w5)
# P6
picked = []
for i, o in known:
    cs = [c for c in EXTRAS if i + c == o]
    assert len(cs) == 1, (i, o, cs)
    c = cs[0]
    picked.append((P - c, Q - c, c))
print('P6 answers (P, Q, extra):', picked)
assert sorted(picked) == worlds and max(q for _, q, _ in picked) <= cells6
# worked example is not a task instance
ex = tuple(map(int, ex))
assert ex[0] + ex[1] == ex[2]
assert (ex[0], ex[2]) not in known, 'example duplicates a P6 machine'
print('example (in, out) =', (ex[0], ex[2]), 'is not a P6 machine; its extra', ex[1], 'equals P6 machine 1 extra:', ex[1] == picked[0][2])
# P4: one known tower always identifies the extra; how big can towers get with 30 cubes
for c, n in itertools.product(EXTRAS, range(1, 14)):
    assert [d for d in EXTRAS if n + d == n + c] == [c]
print('P4: one known tower identifies the extra; input n needs 2n+c cubes with a twin kept, so 30 cubes allow n <= 13')
print('cube totals: P5 all answers', sum(p + q for p, q, _ in worlds), '+ outputs', P + Q,
      '; P6 all three machines built with answers', sum(i + o for i, o in known) + sum(p + q for p, q, _ in picked) + P + Q)
print('PASS')
