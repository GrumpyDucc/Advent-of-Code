input = open("2024/Day 2/tinput.txt", "r").readlines()

reports = [list(map(int, x.split())) for x in input]
answer = 0

wrongReports = 0

def isSafe(difference, increasing):
    return (difference > 0) == increasing and abs(difference) in range(1,4)

for report in reports:
    removed = False
    increasing = report[0] - report[1] > 0
    
    for i, level in enumerate(report[:-1]):
        if isSafe(level - report[i+1], increasing):
            continue
        elif i+2 < len(report) and isSafe(level - report[i+2], increasing) and not removed:
            removed = True
        elif i == 0 and isSafe(report[1] - report[2], increasing):
            increasing = report[1] - report[2] > 0
            removed = True
        else:
            wrongReports += 1
            break
                

print(len(reports)-wrongReports)
