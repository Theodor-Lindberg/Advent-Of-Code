import re
from collections import defaultdict

claims = {}
with open('input.txt') as f:
    for line in f.readlines():
        id, x, y, w, h = [int(digit) for digit in re.findall(r'\d+', line)]
        claims[id] = [x, y, w, h]


def part1():
    overlapped = defaultdict(int)
    for claim in claims:
        x, y, w, h = claims[claim]
        for dx in range(x, x + w):
            for dy in range(y, y + h):
                overlapped[(dx, dy)] += 1
    return sum(1 for i in overlapped.values() if i > 1)

print(part1())


def overlaps(x1, y1, w1, h1, x2, y2, w2, h2):
    return x1 + w1 >= x2 and x1 <= x2 + w2 and \
            y1 + h1 >= y2 and y1 <= y2 + h2


def part2():
    for claim in claims:
        overlapped = False
        for claim_cmp in claims:
            if claim == claim_cmp:
                continue
            if overlaps(*claims[claim], *claims[claim_cmp]):
                overlapped = True
                break
        if not overlapped:
            return claim

print(part2())
