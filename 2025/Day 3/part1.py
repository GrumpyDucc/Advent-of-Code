banks = open("2025/Day 3/input.txt", 'r').read().split('\n')

joltageSum = 0

for bank in banks:
    joltages = list(bank)
    maxJoltage = 0
    for index, joltage in enumerate(joltages):
        partialJoltage = joltage
        for remainingJoltage in joltages[:index]:
            fullJoltage = int(f"{remainingJoltage}{partialJoltage}")
            if (fullJoltage > maxJoltage): maxJoltage = fullJoltage
    joltageSum += maxJoltage

print(joltageSum)