data = open("2022\\Day 6\\data.txt","r").read()

dataList = []
for letter in data:
    dataList.append(letter)

done = False
n = hit = count = 0

while done == False:
    groupList = [dataList[n],dataList[n+1],dataList[n+2],dataList[n+3]]
    group = "".join(groupList)
    for letter in group:
        count += 1
        if group.count(letter) == 1:
            hit += 1
            if hit == 4:
                done = True
                print(data.index(group)+4)
    hit = 0
    n += 1