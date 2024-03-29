input = open("2023/Day 13 - Point of Incidence/input.txt", "r").read().split("\n\n")
endValue = 0

def findMirror(field):
    for row in range(1, len(field)):
        above = field[:row][::-1]
        below = field[row:]

        above = above[:len(below)]
        below = below[:len(above)]
        
        if above == below:
            return row
    return 0

for field in input:
    rowsOfField = field.split("\n")
    colsOfField = list(zip(*rowsOfField))
    
    row = findMirror(rowsOfField)
    col = findMirror(colsOfField)

    endValue += row * 100 + col

print(endValue)