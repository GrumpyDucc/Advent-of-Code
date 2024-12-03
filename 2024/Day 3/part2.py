data = open("2024/Day 3/input.txt", "r").read().strip()
endValue = 0

import re
multiplications = re.finditer("mul\\(\\d{0,3},\\d{0,3}\\)",data)
switches = [x.span() for x in re.finditer("do\\(\\)|don't\\(\\)", data)]

currentSwitch = 0
endLast = 0
do = True

for multiplication in multiplications:
    span = multiplication.span() 
    num1, num2 = data[span[0]:span[1]].replace("mul(", "").replace(")", "").split(',')
    
    startNew = span[0]
    
    if currentSwitch < len(switches) and switches[currentSwitch][0] in range(endLast, startNew):
        switchSpan = switches[currentSwitch]
        if data[switchSpan[0]:switchSpan[1]] == "do()" and do == False: 
            do = True
        elif data[switchSpan[0]:switchSpan[1]] == "don't()" and do == True: 
            do = False
        currentSwitch += 1
    
    if do: endValue += int(num1) * int(num2)

print(endValue)