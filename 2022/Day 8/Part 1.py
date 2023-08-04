rows = open("2022\\Day 8\\data.txt", "r").read().split("\n")

def checkTree(currentTreeRow, currentTree):
    prevRowTrees = [*rows[currentTreeRow-1]][:-1]
    currRowTrees = [*rows[currentTreeRow]][:-1]
    nextRowTrees = [*rows[currentTreeRow+1]][:-1]
    tree = currRowTrees[currentTree]
    if prevRowTrees[currentTree] <= tree:
        if currRowTrees[currentTree-1] <= tree:
            if currRowTrees[currentTree+1] <= tree:
                if nextRowTrees[currentTree] <= tree: return 1 # Tree is visible
                else: return 0
            else: return 0
        else: return 0
    else: return 0


visibleTrees = len(rows)*len(rows[0])

currentRow = 1
currentTree = 1

while currentRow < len(rows)-1:
    row = [*rows[currentRow]][:-1]
    currentTree = 0
    while currentTree < len(row)-2:
        visibleTrees += checkTree(currentRow, currentTree)
        currentTree += 1
    currentRow += 1

print(visibleTrees)