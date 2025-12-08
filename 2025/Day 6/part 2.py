from dataclasses import dataclass
from math import prod

homework = open("2025/Day 6/tinput.txt", 'r').read().split('\n')
homeworkLength = len(homework)

totalSum = 0

@dataclass
class Problem:
    numbers: list[list[str]]
    operator: str = ""

problems: list[Problem] = []

for i in range(len(homework[0].split())): problems.append(Problem([], '?'))

for lineId, line in enumerate(homework):
    for itemId, item in enumerate(line.split()):
        if lineId != homeworkLength - 1:
            number = list(item)
            while len(number)<4: number.insert(0, '')
            problems[itemId].numbers.append(number)
        else:
            problems[itemId].operator = item

for problem in problems:
    numbers = problem.numbers
    fishNumbers: list[list[str]] = []
    for i in range(len(numbers)): fishNumbers.append([])

    for i, number in enumerate(numbers):
        print(number)
        for j, digit in enumerate(number):
            fishNumbers[j].append(digit)
            print(fishNumbers)
            
    
    print(fishNumbers)

# for problem in problems:
#     if problem.operator == '+':
#         totalSum += sum(problem.numbers)
#     else:
#         totalSum += prod(problem.numbers)

print(totalSum)
