
banks = open("2025/Day 3/input.txt", 'r').read().split('\n')

joltageSum = 0

for bank in banks:
    length = len(bank) - 2
    maxJoltage = 0
    allPossibleBanks: list[int] = []

    for i in range(length):
        for j in range(length):
            for k in range(length):
                testBank = list(bank)
                testBank.pop(i)
                testBank.pop(j)
                testBank.pop(k)
                testJoltage = int(''.join(testBank))
                if(testJoltage > maxJoltage): maxJoltage = testJoltage

    joltageSum += maxJoltage

print(joltageSum)