data = open("2024/Day 4/tinput.txt", "r").readlines()
endValue = 0

grid = [list(x.removesuffix("\n")) for x in data] # [line][char in line]
rotatedGrid = [list(x) for x in zip(*grid)]

XMAS = ['X','M','A','S']
SAMX = ['S','A','M','X']

def checkForXMAS(gridToCheck):
    count = 0
    for line in range(len(gridToCheck)):
        for char in range(len(gridToCheck[line])-3):
            selection = gridToCheck[line][char:char+4]
            if selection == XMAS or selection == SAMX:
                count += 1
                # print(selection, line, char)
    return count

endValue = checkForXMAS(grid) + checkForXMAS(rotatedGrid)

# x.append([grid[0][-1]])
# x.append([grid[0][-2], grid[1][-1]])
# x.append([grid[0][-3], grid[1][-2], grid[2][-1]])

print(endValue)
