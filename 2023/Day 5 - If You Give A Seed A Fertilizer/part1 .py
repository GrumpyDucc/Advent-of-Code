seeds, *blocks = open("2023/Day 5 - If You Give A Seed A Fertilizer/input.txt", "r").read().split('\n\n')
endValue = 0

seeds = list(map(int, seeds.split(":")[1].split()))
for block in blocks:
    ranges = []
    for line in block.splitlines()[1:]:
        ranges.append(list(map(int, line.split())))
    new = []
    for x in seeds:
        for a, b, c in ranges:
            if b <= x < b + c:
                new.append(x - b + a)
                break
        else:
            new.append(x)
    seeds = new
endValue = min(seeds)

print(endValue)