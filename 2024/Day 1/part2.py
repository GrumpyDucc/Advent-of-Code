input = open("2024/Day 1/input.txt", "r").readlines()
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
