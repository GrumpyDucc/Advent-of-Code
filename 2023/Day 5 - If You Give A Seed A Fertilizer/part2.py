inputs, *blocks = open("2023/Day 5 - If You Give A Seed A Fertilizer/input.txt", "r").read().split('\n\n')
endValue = 0

inputs = list(map(int, inputs.split(":")[1].split()))

seeds = []
for i in range(0, len(inputs), 2):
    seeds.append((inputs[i], inputs[i] + inputs[i+1]))

for block in blocks:
    ranges = []
    for line in block.splitlines()[1:]:
        ranges.append(list(map(int, line.split())))
    new = []
    while seeds:
        start, end = seeds.pop()
        for a, b, c in ranges:
            overlapStart = max(start, b)
            overlapEnd = min(end, b + c)
            if overlapStart < overlapEnd:
                new.append((overlapStart - b + a, overlapEnd - b + a))
                if overlapStart > start:
                    seeds.append((start, overlapStart))
                if end > overlapEnd:
                    seeds.append((overlapEnd, end))
                break
        else:
            new.append((start, end))
    seeds = new
endValue = min(seeds)[0]

print(endValue)