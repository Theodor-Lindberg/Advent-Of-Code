with open('input.txt') as f:
    lines = f.readlines()


def find_two_three(s):
    found_two = found_three = False
    for c in set(s):
        if found_two and found_three:
            break
        occurrences = s.count(c)
        if occurrences == 2:
            found_two = True
        elif occurrences == 3:
            found_three = True
    return found_two, found_three


def part1():
    twos = threes = 0
    for line in lines:
        found_two, found_three = find_two_three(line)
        twos += found_two
        threes += found_three
    return twos * threes


print(part1())


def diff_by_one(s1, s2):
    diffed_once = False
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            if diffed_once:
                return False
            else:
                diffed_once = True
    return True


def part2():
    for line in lines:
        for line_cmp in lines:
            if line == line_cmp:
                continue
            if diff_by_one(line, line_cmp):
                return ''.join([line[i] if line[i] == line_cmp[i] else '' for i in range(len(line))])

print(part2())
