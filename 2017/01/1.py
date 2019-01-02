with open('input.txt') as f:
    numbers = [int(x) for x in f.readline()]

def part1():
    sum = 0
    for i in range(len(numbers)):
        i_cmp = (i + 1) % len(numbers)
        if numbers[i] == numbers[i_cmp]:
            sum += numbers[i]
    return sum

print(part1())


def part2():
    sum = 0
    for i in range(len(numbers)):
        i_cmp = (i + len(numbers) // 2) % len(numbers)
        if numbers[i] == numbers[i_cmp]:
            sum += numbers[i]
    return sum

print(part2())
