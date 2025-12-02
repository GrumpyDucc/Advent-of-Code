data = open("2025/Day 2/input.txt", 'r').read().split(',')
ranges = list(map(lambda full_range: list(map(lambda x: int(x), full_range.split('-'))), data))

def isInvalid(number: str):
    # chars with repeaters are invalid
    chars = len(number)

    if chars % 2 == 0: # Number is even -> can contain repeaters
        halfLength = int(chars/2)
        firstHalf = number[:halfLength]
        secondHalf = number[halfLength:]
        if (firstHalf == secondHalf): return True
    return False

invalidSum = 0

for dataRange in ranges:
    for number in range(dataRange[0], dataRange[1]+1):
        if isInvalid(str(number)): invalidSum += number

print(invalidSum)
