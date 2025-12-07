database = open("2025/Day 5/input.txt", 'r').read().split('\n\n')
ingredientIDs = database[0].split('\n')

ranges: list[tuple[int, int]] = []
for range in ingredientIDs:
    start, end = map(int, range.split('-'))
    ranges.append((start, end))

ranges.sort()

merged = [ranges[0]]
for start, end in ranges[1:]:
    if start <= merged[-1][1] + 1:
        merged[-1] = (merged[-1][0], max(merged[-1][1], end))
    else:
        merged.append((start, end))

total = sum(end - start + 1 for start, end in merged)

print(total)