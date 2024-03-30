input = open("2023/Day 3 - Gear Ratios/input.txt", "r").read().split("\n")
endValue = 0

# OUTCOME test2input = 4694

def checkSurroundings(r, c):
    if       r - 1 > 0:
        if   c - 1 >= 0 and                 input[r-1][c-1] in symbols: return True # top left
        elif                                input[r-1][c] in symbols: return True   # top
        elif c + 1 < len(input[0]) and      input[r-1][c+1] in symbols: return True # top right
    
    if       c - 1 >= 0 and                 input[r][c-1] in symbols: return True   # left
    elif     c + 1 < len(input[0]) and      input[r][c+1] in symbols: return True   # right
    
    if       r + 1 < len(input) - 1:
        if   c - 1 >= 0 and                 input[r+1][c-1] in symbols: return True # bel left
        elif                                input[r+1][c] in symbols: return True   # bel
        elif c + 1 < len(input[0]) and      input[r+1][c+1] in symbols: return True #bel right
    
    else: return False

symbols = ['*', '#', '+', '$', '-', '=', '@', '/', '&', '%']
currentNum = ''
found = False
foundNums = []

for r in range(len(input)):
    for c in range(len(input[r])):
        char = input[r][c]
        if char.isdigit():
            currentNum += char
            if not found and checkSurroundings(r, c):
                found = True
        elif found:
            foundNums.append(int(currentNum))
            endValue += int(currentNum)
            found = False
            currentNum = ''
        elif char == '.':                               # !!! 
            currentNum = ''
    if char.isdigit() and found and currentNum:         # !!! auch wenn zahl am rand ist mitzählen
        foundNums.append(int(currentNum))
        endValue += int(currentNum)
    currentNum = ''
    found = False
print(endValue)