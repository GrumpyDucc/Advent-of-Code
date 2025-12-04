diagram = list(map(lambda x: list(x), open("2025/Day 4/input.txt", 'r').read().split('\n')))

directions = [
    (-1, -1), (-1, 0), (-1, 1), # top-left, top, top-right
    (0, -1),           (0, 1),  # left, right
    (1, -1),  (1, 0),  (1, 1)   # bottom-left, bottom, bottom-right
]

rows = len(diagram)
cols = len(diagram[0])
movableRolls = 0

def getSurroundings(row: int, col: int) -> list[str]:
    neighbors: list[str] = []
    
    for dr, dc in directions:
        new_row = row + dr
        new_col = col + dc
        
        # Check if the neighbor is within bounds
        if 0 <= new_row < rows and 0 <= new_col < cols:
            neighbors.append(diagram[new_row][new_col])
    
    return neighbors

for row in range(rows):
    for col in range(cols):
        if (diagram[row][col] != '@'): continue

        adjacentRolls = getSurroundings(row, col).count('@')
        if adjacentRolls < 4: 
            movableRolls += 1

print(movableRolls)
