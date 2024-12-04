data = open("2024/Day 4/input.txt", "r").readlines()
endValue = 0

grid = [list(x.removesuffix("\n")) for x in data] # [line][char in line]
rotatedGrid = [list(x) for x in zip(*grid)]

XMAS = [['X','M','A','S'], ['S','A','M','X']]

def checkForXMAS(gridToCheck):
    count = 0
    for line in range(len(gridToCheck)):
        for char in range(len(gridToCheck[line])-3):
            selection = gridToCheck[line][char:char+4]
            if selection in XMAS:
                count += 1
                # print(selection, line, char)
    return count

endValue = checkForXMAS(grid) + checkForXMAS(rotatedGrid)
print(endValue)

n = len(grid)
diagonalGrid = []
for d in range(2 * n - 1):
    diagonal = []
    for i in range(n):
        j = d - i
        if 0 <= j < n:
            diagonal.append(grid[i][j])
    diagonalGrid.append(diagonal)

for diagonal in diagonalGrid:
    if len(diagonal) < 4: continue
    if diagonal in XMAS: continue
    for char in range(len(diagonal)-3):
        selection = diagonal[char:char+4]
        if selection in XMAS:
            endValue += 1
     
n = len(grid)
diagonalGrid = []
for d in range(2 * n - 1):
    diagonal = []
    for i in range(n):
        j = i - (d - (n - 1))
        if 0 <= j < n:
            diagonal.append(grid[i][j])
    diagonalGrid.append(diagonal)

for diagonal in diagonalGrid:
    if len(diagonal) < 4: continue
    if diagonal in XMAS: 
        endValue += 1
        continue
    for char in range(len(diagonal)-3):
        selection = diagonal[char:char+4]
        if selection in XMAS:
            endValue += 1

print(endValue)
