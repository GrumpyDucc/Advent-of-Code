from aocd import get_data
input = get_data(day=4, year=2024).split('\n')
endValue = 0

grid = [list(x.removesuffix("\n")) for x in input]

for row in range(1, len(grid)-1):
    for column in range(1, len(grid[row])-1):
        middle = grid[row][column]
        
        topLeft = grid[row-1][column-1]
        topRight = grid[row-1][column+1]
        bottomLeft = grid[row+1][column-1]
        bottomRight = grid[row+1][column+1]
        
        diagonal1 = [topLeft, middle, bottomRight]
        diagonal2 = [topRight, middle, bottomLeft]
        
        MAS = [['M','A','S'], ['S','A','M']]
        
        if middle == 'A' and diagonal1 in MAS and diagonal2 in MAS: endValue += 1

print(endValue)