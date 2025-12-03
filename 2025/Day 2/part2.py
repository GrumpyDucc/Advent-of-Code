data = open("2025/Day 2/input.txt", 'r').read().split(',')
ranges = list(map(lambda full_range: list(map(lambda x: int(x), full_range.split('-'))), data))

def allSameDigit(number: int):
    stringNumber = str(number)

    digit = stringNumber[0]

    for i in range(1, len(stringNumber)):
        if stringNumber[i] != digit:
            return False

    return True


def isInvalid(number: str):
    viewedDigits = 1
    length = len(number)

    if (length == 2): return False
  
    while(viewedDigits <= length / 2):
        if (length % viewedDigits != 0): 
            viewedDigits += 1
            continue

        possibleRepetitions = int(length / viewedDigits) - 1
        actualRepetitions = 0
        
        repStart = 0 # repeater Start
        for repetition in range(1, possibleRepetitions + 1):
            repEnd = viewedDigits * repetition # repeater End

            if number[repStart:repEnd] == number[repEnd:repEnd + viewedDigits]:
                actualRepetitions += 1
                repStart = repEnd
            else: break
        
        if (actualRepetitions == possibleRepetitions): return True

        viewedDigits += 1
    return False

invalidSum = 0

for dataRange in ranges:
    for number in range(dataRange[0], dataRange[1]+1):
        if -9 <= number <= 9: continue
        
        if allSameDigit(number): invalidSum += number
        elif  isInvalid(str(number)): invalidSum += number

print(invalidSum)
