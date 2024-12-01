input = open("Day 1/input.txt", "r").readlines()
answer = 0

leftList = []
rightList = []

for x in input:
    n1, n2 = x.split()
    leftList.append(int(n1))
    rightList.append(int(n2))

leftList.sort()
rightList.sort()

for i in range(len(leftList)):
    answer += abs(leftList[i] - rightList[i])

print(answer)
