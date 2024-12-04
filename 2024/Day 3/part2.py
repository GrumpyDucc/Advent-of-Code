from aocd import get_data
input = get_data(day=3, year=2024)
endValue = 0

import re
multiplications = re.finditer("mul\\(\\d{0,3},\\d{0,3}\\)", input)
switches = [x.span() for x in re.finditer("do\\(\\)|don't\\(\\)", input)]

currentSwitch = 0
do = True

for multiplication in multiplications:
    span = multiplication.span()
    num1, num2 = multiplication.group().replace("mul(", "").replace(")", "").split(',')
    
    startNew = span[0]
    
    if currentSwitch < len(switches) and switches[currentSwitch][0] < startNew:
        switchSpan = switches[currentSwitch]
        switchLength = switchSpan[1]-switchSpan[0]
        if switchLength == 4 and do == False: 
            do = True
        elif switchLength == 7 and do == True: 
            do = False
        currentSwitch += 1
    
    if do: endValue += int(num1) * int(num2)

print(endValue)