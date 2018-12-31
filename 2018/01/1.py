def part1():
    return sum(map(int,open('input.txt').readlines()))

print(part1())

def part2():
    sum = 0
    seen = {sum}
    with open('input.txt') as f:
        numbers = [int(line) for line in f.readlines()]
    while True:
        for num in numbers:
            sum += int(num)
            if sum in seen:
                return sum
            seen.add(sum)

print(part2())
