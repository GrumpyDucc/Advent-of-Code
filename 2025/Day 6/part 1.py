from dataclasses import dataclass
from math import prod

homework = open("2025/Day 6/input.txt", 'r').read().split('\n')
homeworkLength = len(homework)

totalSum = 0

@dataclass
class Problem:
    numbers: list[int]
    operator: str = ""

problems: list[Problem] = []

for i in range(len(homework[0].split())): problems.append(Problem([], '?'))

for lineId, line in enumerate(homework):
    for itemId, item in enumerate(line.split()):
        if lineId != homeworkLength - 1:
            problems[itemId].numbers.append(int(item))
        else:
            problems[itemId].operator = item

for problem in problems:
    if problem.operator == '+':
        totalSum += sum(problem.numbers)
    else:
        totalSum += prod(problem.numbers)

print(totalSum)
