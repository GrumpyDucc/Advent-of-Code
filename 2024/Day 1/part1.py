from aocd import get_data
input = get_data(day=1, year=2024).split('\n')
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
