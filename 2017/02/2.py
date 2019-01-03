rows = []

with open('input.txt') as f:
    for line in f.readlines():
        rows.append([int(x) for x in line.split('\t')])


def part1():
    return sum([max(row) - min(row) for row in rows])


print(part1())


def find_evenly_divisble(seq):
    for num1 in seq:
        for num2 in seq:
            if num1 != num2 and num1 % num2 == 0:
                return num1, num2


def part2():
    checksum = 0
    for row in rows:
        num1, num2 = find_evenly_divisble(row)
        checksum += num1 // num2
    return checksum


print(part2())
