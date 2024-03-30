input = open("2023/Day 15 - Lens Library/input.txt", "r").read().split(",")
endValue = 0

# --- HASH FUNCTION ---
# Determine the ASCII code for the current character of the string.
# Increase the current value by the ASCII code you just determined.
# Set the current value to itself multiplied by 17.
# Set the current value to the remainder of dividing itself by 256.

# --- INFOS ---
# focal length ranging from 1 through 9
# OPERATORS:
# "-" -> Goto Box, Remove lens with correct label, move up remaining lenses filling up empty slot
# "=" -> num after = is focal lengh, 2 possibilities:
#                                       1. Lens with same label present: replace lens
#                                       2. no Lens with same label: append lens
# FOCUSING POWER:
# One plus the box number of the lens in question.
# The slot number of the lens within the box: 1 for the first lens, 2 for the second lens, and so on.
# The focal length of the lens.

def getHash(step):
    currentValue = 0
    for char in step:
        currentValue += ord(char)
        currentValue *= 17
        currentValue %= 256
    return currentValue

shelf = [[]]

for package in input:
    index = package.find("=")
    if index != -1:
        dest, flengh = package[:index], package[index+1:]
        box = getHash(dest)
        while box > len(shelf)-1: shelf.append([])
        found = False
        for item in shelf[box]:
            if item[0] == dest: 
                i = shelf[box].index(item)
                shelf[box].remove(item)
                shelf[box].insert(i, (dest, flengh))
                found = True
                break
        if not found: shelf[box].append((dest, flengh))
    else:
        dest = package[:index]
        box = getHash(dest)
        while box > len(shelf)-1: shelf.append([])
        for item in shelf[box]:
            if item[0] == dest: 
                shelf[box].remove(item)
                break

for boxIndex, box in enumerate(shelf):
    for lensIndex, lens in enumerate(box):
        endValue += (boxIndex + 1) * (lensIndex + 1) * int(lens[1])
        #print((boxIndex + 1) * (lensIndex + 1) * int(lens[1]))
print(endValue)