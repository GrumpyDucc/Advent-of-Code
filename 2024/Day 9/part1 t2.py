from utils.input_handling import loadDay
#input = loadDay(9, 2024, True, "2")
input = loadDay(9, 2024, False)
endValue = 0

def calculateChecksum(diskMap:list[tuple[int, int]]) -> int:
    checksum = 0
    j = 0
    for block in diskMap:
        for _ in range(block[0]):
            checksum += block[1] * j
            j += 1
    return checksum

diskMap = []
j = 0
for i, num in enumerate(list(map(int, list(input)))):
    if i % 2: diskMap.append((num, None))
    else: 
        diskMap.append((num, j))
        j += 1

for i, block in enumerate(diskMap):
    print(i)
    if block[1] == None:
        if i == len(diskMap)-2: 
            diskMap[-2] = diskMap[-1]
            del diskMap[-1]
            break
        space = block[0]
        del diskMap[i]
        if diskMap[-1][1] == None: del diskMap[-1]
        
        difference = diskMap[-1][0] - space
        if difference > 0:
            diskMap.insert(i, (space, diskMap[-1][1]))
            diskMap[-1] = (difference, diskMap[-1][1])
        else:
            diskMap.insert(i, diskMap[-1])
            space -= diskMap[i][0]
            del diskMap[-1] # the moved block
            del diskMap[-1] # the space that was infront of the block
            while space > 0:
                difference = diskMap[-1][0] - space
                print(difference)
                if difference > 0:
                    diskMap.insert(i+1, (space, diskMap[-1][1]))
                    diskMap[-1] = (difference, diskMap[-1][1])
                    space -= diskMap[i+1][0]
                # ¯\_(ツ)_/¯ else needed idk why

endValue = calculateChecksum(diskMap)
print(endValue)