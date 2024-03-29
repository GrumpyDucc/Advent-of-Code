input = open("2023/Day 13 - Point of Incidence/input.txt", "r").read().split("\n\n")
endValue = 0

def findMirror(field):
    for row in range(1, len(field)):
        above = field[:row][::-1]
        below = field[row:]
        
        if sum(sum(0 if a == b else 1 for a, b in zip(x, y)) for x, y in zip(above, below)) == 1: # Check if there is only one difference (https://www.youtube.com/watch?v=GYbjIvTQ_HA)
            return row
    return 0

for field in input:
    rowsOfField = field.split("\n")
    colsOfField = list(zip(*rowsOfField))
    
    row = findMirror(rowsOfField)
    col = findMirror(colsOfField)

    endValue += row * 100 + col

print(endValue)