from utils.input_handling import loadDay
input = loadDay(9, 2024, True, "2")
#input = loadDay(9, 2024, True)
endValue = 0

def calculateChecksum(files:list[tuple[int, int]]) -> int:
    checksum = 0
    i = 0
    for block in files:
        for j in range(block[0]):
            checksum += block[1] * (j + i)
        i += j
    return checksum

diskMap = list(map(int, list(input)))

files = diskMap[::2]
spaces = diskMap[1::2]

newFiles = []
for i, file in enumerate(files):
    newFiles.append((file, i))
files = newFiles
del newFiles

for i, space in enumerate(spaces):
    filler = []
    fillerLength = 0
    while fillerLength != space:
        if files[-1][0] >= space:
            filler = [(space, files[-1][1])]
            if files[-1][0] > space:
                lastFile = files[-1]
                del files[-1]
                files.append((lastFile[0]-space, lastFile[1]))
            else: del files[-1]
        else:
            filler.append(files[-1])
            fillerLength += filler[-1][0]
            del files[-1]
    for j, fill in enumerate(filler):
        files.insert(i+j+1, fill)

print(files)
endValue = calculateChecksum(files)
print(endValue)