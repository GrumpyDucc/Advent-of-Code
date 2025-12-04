banks = open("2025/Day 3/input.txt", 'r').read().split('\n')
joltageSum = 0

for bank in banks:        
    result:list[str] = []
    remaining = list(bank)
    
    for position in range(12):
        digitsNeededAfterPos = 12 - position - 1
        searchRange = len(remaining) - digitsNeededAfterPos
        
        maxDigit = max(remaining[:searchRange])
        maxIndex = remaining.index(maxDigit)
        
        result.append(maxDigit)
        remaining = remaining[maxIndex + 1:]
    
    maxJoltage = int(''.join(result))
    joltageSum += maxJoltage

print(joltageSum)