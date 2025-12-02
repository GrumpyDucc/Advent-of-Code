data = open("2025/Day 1/input.txt", 'r').read().split('\n')

pointer = 50
timesHitZero = 0

for instrucion in data:
    direction = instrucion[0]
    value = int(instrucion[1:])

    if (direction == "R"): pointer += value
    else: pointer -=  value

    while (pointer < 0): pointer = 100 + pointer
    while (pointer > 99): pointer = pointer - 100

    if (pointer == 0): timesHitZero += 1

print("times hit zero:", timesHitZero)