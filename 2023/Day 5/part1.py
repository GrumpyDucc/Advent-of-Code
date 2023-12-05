input = open("2023/Day 5/inputtest.txt", "r").read().split(':')
endValue = 0

seeds = input[1].split('\n')[1].split(' ')
seedToSoil = input[2].split('\n')[1:-2]
soilToFertilizer = input[3].split('\n')[1:-2]
fertilizerToWater = input[4].split('\n')[1:-2]
waterToLight = input[5].split('\n')[1:-2]
lightToTemperature = input[6].split('\n')[1:-2]
temperatureToHumidity = input[7].split('\n')[1:-2]
humidityToLocation = input[8].split('\n')[1:]

for line in seedToSoil:
    line = line.split(' ')
    sourceRangeStart = int(line[0])
    destinationRangeStart = int(line[1])
    rangeLength = int(line[2])

    sourceRange = range(sourceRangeStart, sourceRangeStart+rangeLength-1)
    destinationRange = range(destinationRangeStart, destinationRangeStart+rangeLength-1)
    print(None)
