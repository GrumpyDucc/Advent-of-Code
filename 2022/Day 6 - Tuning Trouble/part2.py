data = open("2022\\Day 6\\data.txt","r").read()

dataList = []
for letter in data:
    dataList.append(letter)

done = False
n = hit = count = 0
groupList = []
characters = 14

while done == False:
    i = 0
    groupList.clear()
    while i < characters:
        groupList.append(dataList[n+i])
        i += 1
    group = "".join(groupList)
    for letter in group:
        count += 1
        if group.count(letter) == 1:
            hit += 1
            if hit == characters:
                done = True
                print(data.index(group)+characters)
    hit = 0
    n += 1