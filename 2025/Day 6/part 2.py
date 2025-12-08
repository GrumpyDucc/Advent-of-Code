from dataclasses import dataclass
from math import prod

homework = open("2025/Day 6/input.txt", 'r').read().split('\n')
homeworkLength = len(homework)

totalSum = 0

@dataclass
class Problem:
    numbers: list[list[str]]
    startIndex: int
    digits: int
    operator: str = ""

problems: list[Problem] = []

def setProperties(problemId:int, digits:int|None = None, operator:str|None = None, startIndex:int|None = None):
    problem = problems[problemId]

    if (digits): 
        problem.digits = digits
        problem.numbers = [[] for _ in range(digits)]
    if (operator): problem.operator = operator
    if (startIndex): problem.startIndex = startIndex

digits = 1
problem = 0
operatorLine = homework[-1]

for i in range(len(homework[0].split())): 
    problems.append(Problem([], 0, 0, operatorLine[0]))

# Set operator line informations
for index, character in enumerate(operatorLine.split(' ')):
    if character == '': 
        digits += 1
    else:
        setProperties(problemId = problem, operator = character, startIndex=index)
        if (problem != 0): setProperties(problemId = problem - 1, digits=digits)
        problem += 1
        digits = 1
setProperties(-1, digits=digits)

# Set numbers
for problemId, problem in enumerate(problems):
    for line in range(homeworkLength - 1):
        for digit in range(problem.digits):
            problem.numbers[digit].append(homework[line][problem.startIndex + problemId + digit])

for problem in problems:
    integers: list[int] = []
    print(problem.numbers)
    for number in problem.numbers:
        integers.append(int(''.join(number)))

    if problem.operator == '+':
        totalSum += sum(integers)
    else:
        totalSum += prod(integers)

print(totalSum)
