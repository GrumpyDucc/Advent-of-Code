input = open("2023/Day 18 - Lavaduct Lagoon/testinput.txt", "r").read().split("\n")
endValue = 0

widthList = [0]
heightList = [0]
for instruction in input:
    instruction = instruction.split(" ")
    if instruction[0] == "R":
        widthList.append(widthList[-1] + int(instruction[1]))
    elif instruction[0] == "L":
        widthList.append(widthList[-1] - int(instruction[1]))
    elif instruction[0] == "U":
        heightList.append(heightList[-1] + int(instruction[1]))
    elif instruction[0] == "D":
        heightList.append(heightList[-1] - int(instruction[1]))

maxWidth = max(widthList)
maxHeight = min(heightList)*-1
digSite = [['.' for _ in range(maxWidth)] for _ in range(maxHeight)]
digSite[0][0] = "#"

x, y = 0, 0
for instruction in input:
    instruction = instruction.split(" ")
    span = int(instruction[1])

    if instruction[0] == "R":
        for i in range(1, span):
            digSite[y][x+i] = "#"
        x += span - 1
    elif instruction[0] == "D":
        for i in range(1, span):
            digSite[y+i][x] = "#"
        y += span
    elif instruction[0] == "L":
        for i in range(1, span):
            digSite[y][x-i] = "#"
        x -= span

print(digSite)
