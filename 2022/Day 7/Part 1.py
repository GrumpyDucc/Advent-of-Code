data = open("2022\\Day 7\\data.txt","r").read().split("\n")

count = 0
dirList = []
for message in data:
    count += 1
    n = 0
    if message == "$ ls":
        singleDir = []
        singleDir.append(data[count - 2].split(" ")[2])
        while count + n < len(data) - count and data[count + n].startswith("$") == False:
            singleDir.append(data[count + n])
            n += 1
        dirList.append(singleDir)
print(dirList)