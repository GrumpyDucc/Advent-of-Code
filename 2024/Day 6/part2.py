import time
from aocd import get_data

USE_TEST_INPUT = False
if USE_TEST_INPUT: input = open("2024/Day 6/tinput.txt", 'r').read().strip()
else: input = get_data(day=6, year=2024)
endValue = 0

start = time.time()

map = [list(x)for x in input.splitlines()]

def getGuardPosition() -> list[int]:
    for r in range(len(map)):
        if '^' in map[r]: return [r, map[r].index('^')]
    return []


startingPosition = getGuardPosition()
position = startingPosition
guardReachedBoundary = False
facing = 0
visitedCoords = [position]

while not guardReachedBoundary:
    match facing % 4:
        case 0: # up = 0
            nextPosition = [position[0]-1, position[1]]
        case 1: # right = 1
            nextPosition = [position[0], position[1]+1]
        case 2: # down = 2
            nextPosition = [position[0]+1, position[1]]
        case 3: # left = 3
            nextPosition = [position[0], position[1]-1]
    
    if map[nextPosition[0]][nextPosition[1]] == "#": facing += 1
    else: position = nextPosition
    if position[0] not in range(len(map)-1) or position[1] not in range(len(map)-1): guardReachedBoundary = True
    if position not in visitedCoords: visitedCoords.append(position)

for positionToBlock in visitedCoords[1:]:
    position = startingPosition
    visitedCoordsWithFacing = [[position, 0]]
    facing = 0
    while True:
        match facing:
            case 0: # up = 0
                nextPosition = [position[0]-1, position[1]]
            case 1: # right = 1
                nextPosition = [position[0], position[1]+1]
            case 2: # down = 2
                nextPosition = [position[0]+1, position[1]]
            case 3: # left = 3
                nextPosition = [position[0], position[1]-1]
        
        if map[nextPosition[0]][nextPosition[1]] == "#" or positionToBlock == nextPosition: 
            if facing == 3: facing = 0
            else: facing += 1
            if [position, facing] not in visitedCoordsWithFacing: 
                visitedCoordsWithFacing.append([position, facing])
            else: 
                endValue += 1
                print(endValue)
                break
        else: 
            position = nextPosition
        
        if position[0] not in range(len(map)-1) or position[1] not in range(len(map)-1):            
            break

end = time.time()
print(end-start)

print(endValue)