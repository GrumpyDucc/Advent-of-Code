from aocd import get_data
input = get_data(day=4, year=2024).split('\n')
endValue = 0

grid = [list(x.removesuffix("\n")) for x in input] # [line][char in line]
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

def makeDiagonal(type: bool):
    n = len(grid)
    diagonalGrid = []
    for d in range(2 * n - 1):
        diagonal = []
        for i in range(n):
            if type: j = d - i
            else: j = i - (d - (n - 1))
            if 0 <= j < n:
                diagonal.append(grid[i][j])
        diagonalGrid.append(diagonal)
    return diagonalGrid

endValue = checkForXMAS(grid) + checkForXMAS(rotatedGrid) + checkForXMAS(makeDiagonal(True)) + checkForXMAS(makeDiagonal(False))

print(endValue)
