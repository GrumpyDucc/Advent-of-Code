engSche = open("2023/Day 3/inputtest.txt", "r").read().split("\n")

endValue = 0
line = index = 1

def checkList(lst):
 
    ele = lst[0]
    chk = True
 
    # Comparing each element with first item
    for item in lst:
        if ele != item:
            chk = False
            break
    return chk

def getNum(line, index):
    num = ""
    cnt = 0
    while engSche[line][index-cnt].isdigit():
        cnt += 1
    else:
        index -= cnt - 1
        cnt = 0
        while engSche[line][index+cnt].isdigit():
            num += engSche[line][index+cnt]
            cnt += 1
    return int(num)

def getNumbers(line, index):
    values = []
    above = below = topLeft = topRight = bottomLeft = bottomRight = 0
    # Bottom, Above, Left, Right, TopLeft, TopRight, BottomLeft, BottomRight
    # check below
    if engSche[line+1][index].isdigit():
        below = getNum(line+1, index)
    # check above
    if engSche[line-1][index].isdigit():
       above = getNum(line-1, index)
    # check left
    if engSche[line][index-1].isdigit():
        values.append(getNum(line, index-1))
    # check right
    if engSche[line][index+1].isdigit():
        values.append(getNum(line, index+1))
    # check top left
    if engSche[line-1][index-1].isdigit():
        topLeft = getNum(line-1, index-1)
    # check top right
    if engSche[line-1][index+1].isdigit():
        topRight = getNum(line-1, index+1)
    # check bottom left
    if engSche[line+1][index-1].isdigit():
        bottomLeft = getNum(line+1, index-1)
    # check bottom right
    if engSche[line+1][index+1].isdigit():
        bottomRight = getNum(line+1, index+1)

    if len(values) < 2: values.append(0)

    return values[0], values[1]

while line < len(engSche):
    if engSche[line].count('*') != 0:
        indexes = [i for i, e in enumerate(engSche[line]) if e == '*']
        for index in indexes:
            num1, num2 = getNumbers(line, index)
            print(f"line: {line+1} index: {index} {num1}*{num2}={int(num1)*int(num2)}")
            endValue += int(num1) * int(num2)
    line += 1

print(endValue)