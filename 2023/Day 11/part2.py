datasheet = open("2023/Day 11/input.txt", "r").read().split('\n')
endValue = 0

def getDistance(firstLocation, secondLocation): 
    x1 = firstLocation[1]
    y1 = firstLocation[0]
    
    x2 = secondLocation[1]
    y2 = secondLocation[0]

    EXPANTION = 1000000 - 1

    if x1 < x2:
        smallX = x1
        bigX = x2
    else:
        smallX = x2
        bigX = x1
    deltaX = bigX - smallX

    for ex in millionColumns:
        if ex in range(smallX, bigX):
            deltaX += EXPANTION
    
    if y1 < y2:
        smallY = y1
        bigY = y2
    else:
        smallY = y2
        bigY = y1
    deltaY = bigY - smallY

    for ex in millionRows:
        if ex in range(smallY, bigY):
            deltaY += EXPANTION

    return deltaX + deltaY

millionColumns = []
partiallyRealDatasheet = []
for index, column in enumerate(zip(*datasheet)):
    if column.count('#') == 0:
        millionColumns.append(index)
    partiallyRealDatasheet.append(column)

partiallyRealDatasheet = zip(*partiallyRealDatasheet)

millionRows = []
realDatasheet = []
for index, row in enumerate(partiallyRealDatasheet):
    if row.count('#') == 0:
        millionRows.append(index)
    realDatasheet.append(row)


galaxyList = []
for row, itemRow in enumerate(realDatasheet):
    for column, itemColumn in enumerate(itemRow):
        if itemColumn == '#':
            galaxyList.append((row, column))

combo = set()
first = 0
second = 1
while first != len(galaxyList):
    while second < len(galaxyList):
        if (first, second) not in combo:
            path = getDistance(galaxyList[first], galaxyList[second])
            endValue += path
        combo.add((second, first))
        second += 1
    else:
        first += 1
        second = 1

#10077850

print(endValue)