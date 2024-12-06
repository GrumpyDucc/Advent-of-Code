from aocd import get_data

USE_TEST_INPUT = True
if USE_TEST_INPUT: input = open("2024/Day 6/tinput.txt", 'r').read()
else: input = get_data(day=6, year=2024)
endValue = 0

map = [list(x)for x in input.splitlines()]

def findGuard() -> list[int]:
    for r in range(len(map)):
        if map[r].count('^') > 0: return [r, map[r].index('^')]

def isBlocked(coords: list[int]):
    if coords[0] not in range(len(input)) or coords[1] not in range(len(input)): return None
    if map[coords[0]][coords[1]] == "#": return True
    return False

guardCoords = findGuard()
guardLeft = False

# Up = 0
# Right = 1
# Down = 2
# Left = 3
guardDirection = 0

while not guardLeft:
    match guardDirection:
        case 0:
            newCoords = [guardCoords[0]+1, guardCoords[1]]
            if not isBlocked(newCoords) == int:
                guardDirection = 1
            else: guardLeft = True
        case 1:
            newCoords = [guardCoords[0], guardCoords[1]+1]
            if not isBlocked(newCoords) == int:
                guardDirection = 2
            else: guardLeft = True
        case 2:
            newCoords = [guardCoords[0]-1, guardCoords[1]]
            if not isBlocked(newCoords) == int:
                guardDirection = 3
            else: guardLeft = True
        case 3:
            newCoords = [guardCoords[0], guardCoords[1]-1]
            if not isBlocked(newCoords) == int:
                guardDirection = 0
            else: guardLeft = True
    map[guardCoords[0]][guardCoords[1]] = 'X'
    print(map[guardCoords[0]][guardCoords[1]])
    guardCoords = newCoords

print(endValue)