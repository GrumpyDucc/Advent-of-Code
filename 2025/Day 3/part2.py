from itertools import combinations

banks = open("2025/Day 3/tinput.txt", 'r').read().split('\n')

joltageSum = 0
cnt = 0

for bank in banks:
    length = len(bank) - 2
    maxJoltage = 0

    for batteriesToRemove in combinations(range(len(bank)), 3):
        testBank = list(bank)
        for index in sorted(batteriesToRemove, reverse=True):
            testBank.pop(index)
        
        testJoltage = int(''.join(testBank))
        if(testJoltage > maxJoltage): maxJoltage = testJoltage

    cnt += 1
    print(cnt)

    joltageSum += maxJoltage

print(joltageSum)