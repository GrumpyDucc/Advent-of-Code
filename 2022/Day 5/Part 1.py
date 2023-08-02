data = open("2022\\Day 5\\data.txt","r").read().split("\n\n")

crateList = data[0].replace("\n", "  ").replace("[", "").replace("]", "").replace("    ", " ").split(" ")
lastNum = int(crateList[-2])
del crateList[-lastNum*3-1:]
moveList = data[1].split("\n")

#verticalCrateList = [crateList[:9], crateList[10:19], crateList[20:29], crateList[30:39],crateList[40:49], crateList[50:59], crateList[60:69], crateList[70:79]]
verticalCreateList = []
i = 0
while i < 80:
    verticalCreateList.append(crateList[i:i+lastNum])
    i += lastNum+1

horizontalCrateList = []
i = 0
while i < lastNum:
    l = []
    for lists in verticalCreateList:
        l.append(lists[i])
    l.reverse()
    horizontalCrateList.append(l)
    i += 1

for lists in horizontalCrateList:
        d = 0
        while d != 1:
            try:
                lists.remove("")
                d = 0
            except:
                d = 1

def move(amount, src, dst):
    items = horizontalCrateList[src][-amount:]
    items.reverse()
    inIndex = ''.join(horizontalCrateList[dst]).rindex('')

    j = 0
    while j < len(items):    
        horizontalCrateList[dst].insert(inIndex + j, items[j])
        j += 1    
    del horizontalCrateList[src][-amount:]

for moves in moveList:
    numbers = [int(s) for s in moves.split() if s.isdigit()]
    move(numbers[0], numbers[1] - 1, numbers[2] - 1)

msg = ""
for lists in horizontalCrateList:
    msg = msg + lists[-1]
print(msg)