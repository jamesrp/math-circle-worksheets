"""Finite checks; uniqueness explanations and limits are in README.md."""
from itertools import permutations, product

weights = (4, 2, 1, 1)
trees = ((2, 2, 2, 2), (1, 2, 3, 3))
costs = [(sum(w * d for w, d in zip(weights, depths)), depths)
         for tree in trees for depths in set(permutations(tree))]
assert min(cost for cost, _ in costs) == 14
assert sum(w * d for w, d in zip(weights, (1, 2, 3, 3))) == 14
print('Eight-message batch optimum: 14; A/B/C/D depths: 1/2/3/3.')

# The proposed two-weighing strategy has distinct observations for all secrets.
groups = ((1, 2, 3), (4, 5, 6), (7, 8, 9))
observations = {}
for heavy in range(1, 10):
    first = next(i for i, group in enumerate(groups) if heavy in group)
    remaining = groups[first]
    second = remaining.index(heavy)
    observations[heavy] = (first, second)
assert len(set(observations.values())) == 9
print('Nine secrets: all nine observation pairs distinct in two weighings.')

books = ({'A': 'R', 'B': 'RY', 'C': 'Y'},
         {'A': 'R', 'B': 'YR', 'C': 'YY'},
         {'A': 'R', 'B': 'RY'})
for i, book in enumerate(books, 1):
    seen = {}
    collisions = []
    for length in range(1, 7):
        for letters in product(book, repeat=length):
            word = ''.join(letters)
            encoded = ''.join(book[letter] for letter in letters)
            previous = seen.get(encoded)
            if previous is not None and previous != word:
                collisions.append((encoded, previous, word))
            else:
                seen[encoded] = word
    if i == 1:
        assert book['B'] == book['A'] + book['C']
        assert collisions
        print('Book 1 collision: B and AC both make RY.')
    else:
        assert not collisions
        print(f'Book {i}: no collision through six letters (finite check only).')

assert ''.join({'M':'YR','N':'R'}[letter] for letter in 'MN') == 'YRR'
print('Worked code example: MN -> YR|R -> YRR.')
