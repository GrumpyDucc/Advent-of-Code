import time
from aocd import get_data

USE_TEST_INPUT = False
if USE_TEST_INPUT: input = open("2024/Day 6/tinput.txt", 'r').read().strip()
else: input = get_data(day=6, year=2024)
endValue = 0

start = time.time()

map = [list(x)for x in input.splitlines()]

def findGuard() -> list[int]:
    for r in range(len(map)):
        if '^' in map[r]: return [r, map[r].index('^')]
    return []

def isBlocked(coords: list[int]):
    if map[coords[0]][coords[1]] == "#": return True
    return False

guardCoords = findGuard()
guardLeft = False
guardDirection = 0
visitedCoords = [guardCoords]

while not guardLeft:
    match guardDirection % 4:
        case 0: # Up = 0
            newCoords = [guardCoords[0]-1, guardCoords[1]]
        case 1: # Right = 1
            newCoords = [guardCoords[0], guardCoords[1]+1]
        case 2: # Down = 2
            newCoords = [guardCoords[0]+1, guardCoords[1]]
        case 3: # Left = 3
            newCoords = [guardCoords[0], guardCoords[1]-1]
    
    if isBlocked(newCoords): guardDirection += 1
    else: guardCoords = newCoords
    if guardCoords[0] not in range(len(map)-1) or guardCoords[1] not in range(len(map)-1): guardLeft = True
    if guardCoords not in visitedCoords: visitedCoords.append(guardCoords)

end = time.time()
print(end-start)

endValue = len(visitedCoords)

print(endValue)