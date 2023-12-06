input = open("2023/Day 6/input.txt", "r").read().split('\n')
endValue = 1

totalWins = []
times = input[0].split(':')[1].split(' ')
times = [j for i,j in enumerate(times) if j!='']
tempTime = ''
for time in times:
    tempTime += time
times = [tempTime]

distances = input[1].split(':')[1].split(' ')
distances = [j for i,j in enumerate(distances) if j!='']
tempDistance = ''
for distance in distances:
    tempDistance += distance
distances = [tempDistance]

for i in range(len(times)):
    duration = int(times[i])
    recordDistance = int(distances[i])
    totalWinningHoldTimes = []
    for j in range(duration):        

        holdTime = j
        remainTime = duration - holdTime
        distance = remainTime * holdTime

        if distance > recordDistance:
            totalWinningHoldTimes.append(holdTime)
    totalWins.append(len(totalWinningHoldTimes))          

for win in totalWins:
    endValue *= win

print(endValue)