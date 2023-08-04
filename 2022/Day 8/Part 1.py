rows = open("2022\\Day 8\\data.txt", "r").read().split("\n")
colums = [list(column) for column in zip(*rows)]

def visibleLeft(currRow, height, currentTreePos):
    count = 0
    for letter in [*rows[currRow]][:currentTreePos]:
        if int(letter) < int(height):
            count += 1
    if count == len([*rows[currRow]][:currentTreePos]):
        return True
    else:
        return False

def visibleRight(currRow, height, currentTreePos):
    count = 0
    for letter in [*rows[currRow]][currentTreePos+1:]:
        if int(letter) < int(height):
            count += 1
    if count == len([*rows[currRow]][currentTreePos+1:]):
        return True
    else:
        return False

def visibleUp(currRow, height, currentTreePos):
    count = 0
    treesToCheck = [*colums[currentTreePos]][:currRow]
    for letter in treesToCheck:
        if int(letter) < int(height):
            count += 1
    if count == len(treesToCheck):
        return True
    else:
        return False

def visibleDown(currRow, height, currentTreePos):
    count = 0
    for letter in [*colums[currentTreePos]][currRow+1:]:
        if int(letter) < int(height):
            count += 1
    if count == len([*colums[currentTreePos]][currRow+1:]):
        return True
    else:
        return False

def checkTree(currentTreeRow, currentTree):
    currRowTrees = [*rows[currentTreeRow]]
    tree = currRowTrees[currentTree]
    if visibleUp(currentTreeRow, tree, currentTree) or visibleDown(currentTreeRow, tree, currentTree) or visibleLeft(currentTreeRow, tree, currentTree) or visibleRight(currentTreeRow, tree, currentTree):
        return 1    # Tree is visible
    else:
        return 0    # Tree is not visible

visibleTrees = 0

currentRow = 1
currentTree = 1

while currentRow < len(rows)-1:
    row = [*rows[currentRow]][:-1]
    currentTree = 0
    while currentTree < len(row)-1:
        currentTree += 1
        visibleTrees += checkTree(currentRow, currentTree)
    currentRow += 1

outerRing = (len(rows)-2)*2+len(rows[0])*2
print(visibleTrees + outerRing)