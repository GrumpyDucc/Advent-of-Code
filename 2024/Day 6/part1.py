from aocd import get_data

USE_TEST_INPUT = True
if USE_TEST_INPUT: input = open("2024/Day 6/tinput.txt", 'r').read()
else: input = get_data(day=6, year=2024)
endValue = 0

map = [list(x)for x in input.splitlines()]

def findGuard() -> list[int]:
    for r in range(len(map)):
        if map[r].count('^') > 0: return [r, map[r].index('^')]
    return []

def isBlocked(coords: list[int]):
    if coords[0] not in range(len(map)) or coords[1] not in range(len(map)): return False
    if map[coords[0]][coords[1]] == "#": return True
    return False

guardCoords = findGuard()
guardLeft = False
guardDirection = 0
visitedCoords = [guardCoords]

while not guardLeft:
    match guardDirection:
        case 0: # Up = 0
            newCoords = [guardCoords[0]-1, guardCoords[1]]
            if isBlocked(newCoords):
                guardDirection = 1
            else: guardCoords = newCoords
        case 1: # Right = 1
            newCoords = [guardCoords[0], guardCoords[1]+1]
            if isBlocked(newCoords):
                guardDirection = 2
            else: guardCoords = newCoords
        case 2: # Down = 2
            newCoords = [guardCoords[0]+1, guardCoords[1]]
            if isBlocked(newCoords):
                guardDirection = 3
            else: guardCoords = newCoords
        case 3: # Left = 3
            newCoords = [guardCoords[0], guardCoords[1]-1]
            if isBlocked(newCoords): 
                guardDirection = 0
            else: guardCoords = newCoords
    if guardCoords[0] not in range(len(map)-1) or guardCoords[1] not in range(len(map)-1): guardLeft = True
    if visitedCoords.count(guardCoords) < 1: 
        visitedCoords.append(guardCoords)

endValue = len(visitedCoords)

print(endValue)