datasheet = open("2023/Day 12/inputtest.txt", "r").read().split('\n')
endValue = 0

for line in datasheet:
    line = line.split(' ')
    springs = list(line[0])
    conditionRecord = line[1].split(',')
    pass