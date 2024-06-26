input = open("2023/Day 5 - If You Give A Seed A Fertilizer/input.txt", "r").read().split(':')
endValue = 0

seeds = input[1].split('\n')[0].split(' ')[1:]

seedRanges = []
for i in range(0, len(seeds), 2):
    seedRanges.append(range(int(seeds[i]),int(seeds[i])+int(seeds[i + 1])))

categories = [
    #seedToSoil
    input[2].split('\n')[1:-2], 
    #soilToFertilizer
    input[3].split('\n')[1:-2],
    #fertilizerToWater
    input[4].split('\n')[1:-2],
    #waterToLight
    input[5].split('\n')[1:-2],
    #lightToTemperature
    input[6].split('\n')[1:-2],
    #temperatureToHumidity
    input[7].split('\n')[1:-2],
    #humidityToLocation
    input[8].split('\n')[1:]
]

listCounter = 0

def getDestinationValues(startValues):
    global listCounter
    list = categories[listCounter]
    destinationValues = []
    for value in startValues:
        notInRange = 0
        for line in list:
            line = line.split(' ')
            sourceRangeStart = int(line[1])
            rangeLength = int(line[2])
            sourceRange = range(sourceRangeStart, sourceRangeStart + rangeLength)
            if int(value) in sourceRange:
                index = sourceRange.index(int(value))
                if index >= 0:
                    destination = int(line[0])+index
                    destinationValues.append(destination)
                    break
            else: notInRange += 1
        if notInRange == len(list):
            destinationValues.append(int(value))
    if listCounter < len(categories) - 1:
        listCounter += 1
        return getDestinationValues(destinationValues)
    else:
        return sorted(destinationValues)[0]

locations = []
for seedRange in seedRanges:
    locations.append(getDestinationValues([*seedRange]))
print(sorted(locations)[0])