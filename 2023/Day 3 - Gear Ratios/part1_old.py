engSche = open("2023/Day 3 - Gear Ratios/inputEdit.txt", "r").read().split("\n")

endValue = 0
line = index = 1
number = ""

def touch(line, index, lenOfNum):
    # check touch above
    for num in range(lenOfNum):
        if engSche[line-1][index + num] != '.':
            return True
    
    # check touch below
    for num in range(lenOfNum):
        if engSche[line+1][index + num] != '.':
            return True
    
    # check touch left
    if engSche[line][index - 1] != '.':
        return True
    
    # check touch right
    if engSche[line][index + lenOfNum] != '.':
        return True

    # check touch top left
    if engSche[line-1][index - 1] != '.':
        return True
    
    #check touch top right
    if engSche[line-1][index + lenOfNum] != '.':
        return True
    
    #check touch bottom left
    if engSche[line+1][index - 1] != '.':
        return True
    
    #check touch bottom right
    if engSche[line+1][index + lenOfNum] != '.':
        return True

    return False

while line < len(engSche):
    index = 0
    while index < len(engSche[line]):
        if engSche[line][index].isdigit():
            number = engSche[line][index]
            while engSche[line][index+1].isdigit():
                number += engSche[line][index+1]
                index += 1
            if touch(line, index-len(number)+1, len(number)):
                endValue += int(number)
                index += 1
            else:
                index += 1
        else: index += 1
    else: line += 1

print(endValue)