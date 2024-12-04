input = open("2024/Day 2/input.txt", "r").readlines()

reports = [list(map(int, x.split())) for x in input]
answer = 0

for report in reports:
    acending = report[0] - report[1] > 0
    for i, level in enumerate(report[:-1]):
        difference = level - report[i+1]
        
        if (difference > 0) == acending and abs(difference) in range(1,4): #if safe
            answer += 1
            break

print(answer)
