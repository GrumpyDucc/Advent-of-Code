import time
from utils.input_handling import loadDay

USE_TEST_INPUT = False
input = loadDay(8, 2024, USE_TEST_INPUT)
endValue = 0

start = time.time()

map = [list(x) for x in input.splitlines()]
mapSize = len(map)

antennas = {}
for lineIndex, line in enumerate(map):
    for markerIndex, marker in enumerate(line):
        if marker != '.':
            if marker not in antennas:
                antennas[marker] = []
            antennas[marker].append((lineIndex, markerIndex))

def getDistance(positionAntenna1: tuple[int, int], positionAntenna2: tuple[int, int]):
    deltaX = positionAntenna1[1]-positionAntenna2[1]
    deltaY = positionAntenna1[0]-positionAntenna2[0]
    return (deltaY, deltaX)

def onMap(positionAnidote: tuple[int, int]):
    if all(x in range(mapSize) for x in positionAnidote):
        return True
    return False

def getAntinotes(positionAntenna1: tuple[int, int], positionAntenna2: tuple[int, int]) -> list[tuple[int, int]|None]:
    antennaOffset = getDistance(positionAntenna1, positionAntenna2)
    antiNodes1 = [positionAntenna1]
    antiNodes2 = [positionAntenna2]
    
    while True:
        antinode = (antiNodes1[-1][0]+antennaOffset[0], antiNodes1[-1][1]+antennaOffset[1])
        if not onMap(antinode): break
        else: antiNodes1.append(antinode)
    
    while True:
        antinode = (antiNodes2[-1][0]-antennaOffset[0], antiNodes2[-1][1]-antennaOffset[1])
        if not onMap(antinode): break
        else: antiNodes2.append(antinode)
    
    return [*antiNodes1, *antiNodes2]

antinodes = []
for antennaType in antennas:
    typedAntennas = antennas.get(antennaType)
    if typedAntennas is None: continue
    n = len(typedAntennas)
    # 0.5*n*(n+1) gausche summenformel (anzahl der möglichen kombinationen) ༼ つ ◕_◕ ༽つ
    combinations = [(i, j) for i in range(n) for j in range(i + 1, n)]
    for combination in combinations:
        i = combination[0]
        j = combination[1]
        print(i, j)
        currentAntenna = typedAntennas[i]
        nextAntenna = typedAntennas[j]
        antinodes.extend(getAntinotes(currentAntenna, nextAntenna))

endValue = len(list(dict.fromkeys(antinodes)))

end = time.time()
print(end-start)

print(endValue)