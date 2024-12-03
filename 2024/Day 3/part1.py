data = open("2024/Day 3/tinput.txt", "r").read().strip()
endValue = 0

import re
multiplications = re.finditer("mul\\(\\d{0,3},\\d{0,3}\\)",data)
dos = reversed([x.start() for x in re.finditer("do\\(\\)", data)])
donts = reversed([x.start() for x in re.finditer("don't\\(\\)", data)])

def isDo(start, dos, donts):
    smallestDo = None
    smallestDont = None
    
    for do in dos:
        if start < do:
            smallestDo = do
            break
        
    for dont in donts:
        if start < dont:
            smallestDont = dont
            break
    
    if smallestDo == None: return True
    if smallestDont == None: return True
    if smallestDo > smallestDont: return True
    return False

for multiplication in multiplications:
    span = multiplication.span() 
    num1, num2 = data[span[0]:span[1]].replace("mul(", "").replace(")", "").split(',')
    print(isDo(span[0], dos, donts))
    endValue += int(num1) * int(num2)

print(endValue)