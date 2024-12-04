from aocd import get_data
input = get_data(day=1, year=2024).split('\n')
answer = 0

leftList = []
rightList = []

for x in input:
    n1, n2 = x.split()
    leftList.append(int(n1))
    rightList.append(int(n2))

for num in leftList:
    answer += num * rightList.count(num)

print(answer)
