#!/usr/bin/env python3
"""Independently enumerate the student tasks; no third-party code required."""
from functools import lru_cache
import json


def partitions(total, largest=None):
    if total == 0:
        yield ()
        return
    if largest is None:
        largest = total
    for first in range(min(total, largest), 0, -1):
        for rest in partitions(total - first, first):
            yield (first,) + rest


def canonical(parts):
    return tuple(sorted(parts, reverse=True))


def split_to_odd(parts):
    out = []
    for part in parts:
        multiplicity = 1
        while part % 2 == 0:
            part //= 2
            multiplicity *= 2
        out.extend([part] * multiplicity)
    return canonical(out)


@lru_cache(None)
def join_endings(parts):
    endings = set()
    for size in set(parts):
        if parts.count(size) > 1:
            remaining = list(parts)
            remaining.remove(size)
            remaining.remove(size)
            remaining.append(2 * size)
            endings.update(join_endings(canonical(remaining)))
    return frozenset(endings or {parts})


def join(parts):
    endings = join_endings(canonical(parts))
    assert len(endings) == 1, (parts, endings)
    return next(iter(endings))


def exchange(parts):
    return tuple(sum(part >= column for part in parts)
                 for column in range(1, max(parts, default=0) + 1))


def is_odd(parts):
    return all(part % 2 for part in parts)


def is_distinct(parts):
    return len(parts) == len(set(parts))


# Worked visuals and printed starting collections, transcribed from students.tex.
join_cases = [
    (3, 3, 1, 1, 1, 1),  # worked input 10 -> 6+4
    (1,) * 9,
    (5, 5, 3, 3, 3, 1, 1),
    (5, 3, 1),
    (3,) * 4 + (1,) * 6,  # order investigation 18 -> 12+4+2
]
split_cases = [(4, 3, 2), (10, 7, 4, 2, 1), (12, 6, 3), (7, 3, 1)]
exchange_cases = [(5, 3, 3, 1), (5, 2, 1), (4, 4), (3, 3, 1, 1)]
def one_join(parts, size):
    remainder = list(parts)
    remainder.remove(size)
    remainder.remove(size)
    return canonical(remainder + [2 * size])


def one_split(parts, size):
    assert size % 2 == 0
    remainder = list(parts)
    remainder.remove(size)
    return canonical(remainder + [size // 2, size // 2])


assert one_join((3, 3, 1, 1, 1, 1), 3) == (6, 1, 1, 1, 1)
assert join((3, 3, 1, 1, 1, 1)) == (6, 4)
assert one_split((4, 3, 2), 4) == (3, 2, 2, 2)
assert split_to_odd((4, 3, 2)) == (3, 1, 1, 1, 1, 1, 1)
assert exchange((5, 3, 3, 1)) == (4, 3, 3, 1, 1)
for parts in join_cases:
    assert is_odd(parts) and sum(parts) <= 24
    result = join(parts)
    assert is_distinct(result) and sum(result) == sum(parts)
    assert split_to_odd(result) == canonical(parts)
for parts in split_cases:
    assert is_distinct(parts) and sum(parts) <= 24
    result = split_to_odd(parts)
    assert is_odd(result) and sum(result) == sum(parts)
    assert join(result) == canonical(parts)
for parts in exchange_cases:
    assert exchange(exchange(parts)) == canonical(parts)
    assert sum(exchange(parts)) == sum(parts)

catalogs = {}
for total in (4, 5, 6, 7, 8):
    all_parts = list(partitions(total))
    odd = [p for p in all_parts if is_odd(p)]
    distinct = [p for p in all_parts if is_distinct(p)]
    assert {join(p) for p in odd} == set(distinct)
    assert {split_to_odd(p) for p in distinct} == set(odd)
    catalogs[total] = {
        'all': all_parts,
        'only_odd': odd,
        'all_different': distinct,
        'matched_pairs': [(p, join(p)) for p in odd],
    }
assert len(catalogs[4]['all']) == 5
assert len(catalogs[5]['all']) == 7
assert len(catalogs[6]['only_odd']) == len(catalogs[6]['all_different']) == 4
assert len(catalogs[7]['only_odd']) == len(catalogs[7]['all_different']) == 5
assert len(catalogs[8]['only_odd']) == len(catalogs[8]['all_different']) == 6
restricted = [p for p in partitions(8) if len(p) <= 3]
assert len(restricted) == 10
assert {exchange(p) for p in restricted} == {
    p for p in partitions(8) if max(p) <= 3
}
# Finite general checks support printed experiments. They do not prove the theorem.
checked = 0
for total in range(25):
    for p in partitions(total):
        checked += 1
        assert exchange(exchange(p)) == p
        if is_odd(p):
            assert split_to_odd(join(p)) == p
        if is_distinct(p):
            assert join(split_to_odd(p)) == p
report = {
    'status': 'pass',
    'partition_range_checked': [0, 24],
    'partitions_checked': checked,
    'catalogs': catalogs,
    'join_examples': [(p, join(p)) for p in join_cases],
    'split_examples': [(p, split_to_odd(p), join(split_to_odd(p))) for p in split_cases],
    'row_column_examples': [(p, exchange(p), exchange(exchange(p))) for p in exchange_cases],
    'at_most_three_strips_total_eight': [(p, exchange(p)) for p in restricted],
    'scope': 'Finite enumerations and actual diagram inputs, not a proof or a physical/classroom test.',
}
print(json.dumps(report, indent=2))
