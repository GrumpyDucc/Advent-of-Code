datasheet = open("2023/Day 11/inputtest.txt", "r").read().split('\n')
endValue = 0

def getDistance(firstLocation, secondLocation): 
    x1 = firstLocation[0]
    y1 = firstLocation[1]-1
    
    x2 = secondLocation[0]
    y2 = secondLocation[1]-1

    EXPANTION = 10

    for i in range(len(millionRows)):
        if x1 > millionRows[i]: 
            x1 += EXPANTION
        if x2 > millionRows[i]: 
            x2 += EXPANTION

    for i in range(len(millionColumns)):
        if y1 > millionColumns[i]: 
            y1 += EXPANTION
        if y2 > millionColumns[i]: 
            y2 += EXPANTION

    if x1 < x2:
        deltaX = x2 - x1
    else:
        deltaX = x1 - x2
    
    if y1 < y2:
        deltaY = y2 - y1
    else:
        deltaY = y1 - y2

    return deltaX + deltaY

millionColumns = []
partiallyRealDatasheet = []
for index, column in enumerate(zip(*datasheet)):
    if column.count('#') == 0:
        partiallyRealDatasheet.append(column)
        millionColumns.append(index)
    partiallyRealDatasheet.append(column)

partiallyRealDatasheet = zip(*partiallyRealDatasheet)

millionRows = []
realDatasheet = []
for index, row in enumerate(partiallyRealDatasheet):
    if row.count('#') == 0:
        realDatasheet.append(row)
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