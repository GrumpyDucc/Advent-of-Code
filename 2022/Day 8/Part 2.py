forest = open("2022\\Day 8\\data.txt", "r").read().split("\n")

def up(currentRow, currentTree):
    count = 0
    while count < currentRow:
        if [*forest[currentRow - 1 - count]][currentTree] < [*forest[currentRow]][currentTree]:
            count += 1
        else:
            return count + 1
    return count

def down(currentRow, currentTree):
    count = 0
    while count < len(forest) - 1 - currentRow:
        if [*forest[currentRow + 1 + count]][currentTree] < [*forest[currentRow]][currentTree]:
            count += 1
        else:
            return count + 1
    return count

def left(currentRow, currentTree):
    count = 0
    if currentTree - 1 - count < len([*forest[currentRow]]):
        while count < currentTree:
            if [*forest[currentRow]][currentTree - 1 - count] < [*forest[currentRow]][currentTree]:
                count += 1
            else:
                return count + 1
        return count
    else:
        return count

def right(currentRow, currentTree):
    count = 0
    while count < currentTree:
        if currentTree + 1 + count >= len(forest[0]):
            return count
        else:
            if [*forest[currentRow]][currentTree + 1 + count] < [*forest[currentRow]][currentTree]:
                count += 1
            else:
                return count + 1
    return count

maxSenicScore = 0
currentRow = 1
currentTree = 1

while currentRow < len(forest):
    row, pos = currentRow, currentTree
    senicScore = up(row, pos) * left(row, pos) * right(row, pos) * down(row, pos)
    if senicScore > maxSenicScore:
        maxSenicScore = senicScore
    currentTree += 1
    if currentTree > len(forest[0]) - 2:
        currentTree = 0
        currentRow += 1

print(maxSenicScore)