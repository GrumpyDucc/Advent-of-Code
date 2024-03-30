input = open("2023/Day 3 - Gear Ratios/input.txt", "r").read().split("\n")
endValue = 0

# OUTCOME test2input = 4694

def checkSurroundings(r, c):
    if       r - 1 > 0:
        if   c - 1 >= 0 and                 input[r-1][c-1] in symbols: return True, (r-1,c-1) # top left
        elif                                input[r-1][c] in symbols: return True, (r-1,c)    # top
        elif c + 1 < len(input[0]) and      input[r-1][c+1] in symbols: return True, (r-1,c+1) # top right
    
    if       c - 1 >= 0 and                 input[r][c-1] in symbols: return True, (r,c-1)    # left
    elif     c + 1 < len(input[0]) and      input[r][c+1] in symbols: return True, (r,c+1)    # right
    
    if       r + 1 < len(input) - 1:
        if   c - 1 >= 0 and                 input[r+1][c-1] in symbols: return True, (r+1,c-1) # bel left
        elif                                input[r+1][c] in symbols: return True, (r+1,c)    # bel
        elif c + 1 < len(input[0]) and      input[r+1][c+1] in symbols: return True, (r+1,c+1) #bel right
    
    else: return False, (0, 0)
    return False, (0, 0)

def findPair(cogPos, currentNum):
    for f in range(len(foundNums)):
        if foundNums[f][0] == cogPos:
            foundNums[f][1].append(int(currentNum))
            return
    foundNums.append([cogPos, [int(currentNum)]])

symbols = ['*']
currentNum = ''
found = False
foundNums = []

for r in range(len(input)):
    for c in range(len(input[r])):
        char = input[r][c]
        if char.isdigit():
            currentNum += char
            out = checkSurroundings(r, c)
            if not found and out[0]:
                found = True
                cogPos = out[1]
        elif found:
            findPair(cogPos, currentNum)
            found = False
            currentNum = ''
        elif char == '.':                               # !!! trennung nach ungewerteter zahl
            currentNum = ''
    if char.isdigit() and found and currentNum:         # !!! auch wenn zahl am rand ist mitzählen
        findPair(cogPos, currentNum)
    currentNum = ''
    found = False

for foundNum in foundNums:
    if len(foundNum[1]) == 2:
        endValue += foundNum[1][0] * foundNum[1][1]
print(endValue)