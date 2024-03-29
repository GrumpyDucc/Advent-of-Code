input = open("2023/Day 14 - Parabolic Reflector Dish/input.txt", "r").read().split("\n")
endValue = 0

field = list(map(list, zip(*input)))

def getWeightOfRow(rowIndex:int, row:list)->int:
    return row.count("O") * (rowIndex + 1)

def findRoundStones(col):
    roundStones = []
    for index, stone in enumerate(col):
        if stone == "O":
            roundStones.append(index)
    if roundStones == []:
        return []
    return roundStones

def printField():
    for col in field:
        col = list(col)
        print(col)
    print("\r")

for col in range(len(field)):
    roundStones = findRoundStones(field[col])
    for roundStone in roundStones:
        newIndex = roundStone
        while newIndex - 1 >= 0 and field[col][newIndex-1] == ".":
            newIndex -= 1
        field[col][roundStone] = "."
        field[col][newIndex] = "O"

field = list(map(list, zip(*field)))

field.reverse()
for rowIndex, row in enumerate(field):
    endValue += getWeightOfRow(rowIndex, row)
print(endValue)