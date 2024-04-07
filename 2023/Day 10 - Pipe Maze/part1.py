data = open("2023/Day 10 - Pipe Maze/input.txt", "r").read().split('\n')
endValue = 0

""" INFO - Pipes:
| is a vertical pipe connecting north and south.
- is a horizontal pipe connecting east and west.
L is a 90-degree bend connecting north and east.
J is a 90-degree bend connecting north and west.
7 is a 90-degree bend connecting south and west.
F is a 90-degree bend connecting south and east.
. is ground; there is no pipe in this tile. """

width  = len(data[0])
height = len(data)

def findOption(y:int, x:int):
    global prev
    if y + 1 < height and (y + 1, x) not in prev and data[y+1][x] in '|LJS' and data[y][x] not in 'LJ-': 
        prev[0] = prev[1]
        prev[1] = (y, x)
        return y + 1, x
    if y - 1 >= 0     and (y - 1, x) not in prev and data[y-1][x] in '|F7S' and data[y][x] not in 'F7-': 
        prev[0] = prev[1]
        prev[1] = (y, x)
        return y - 1, x
    if x + 1 < width  and (y, x + 1) not in prev and data[y][x+1] in '-J7S' and data[y][x] not in 'J7':  
        prev[0] = prev[1]
        prev[1] = (y, x)
        return y, x + 1
    if x - 1 >= 0     and (y, x - 1) not in prev and data[y][x-1] in '-LFS':
        prev[0] = prev[1]
        prev[1] = (y, x)
        return y, x - 1
    raise Exception("BAD CODE")

y, x = 0, 0
moves = 1
global prev
prev = [(0, 0),()]
for lineIndex, line in enumerate(data):
    if line.count('S'):
        y, x = findOption(lineIndex, line.index('S'))

while data[y][x] != 'S':
    y, x = findOption(y, x)
    moves += 1
endValue = round(moves / 2)

print(endValue)