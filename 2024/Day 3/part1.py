data = open("2024/Day 3/input.txt", "r").read().strip()
endValue = 0

import re
multiplications = re.finditer("mul\\(\\d{0,3},\\d{0,3}\\)",data)
for multiplication in multiplications:
    span = multiplication.span() 
    num1, num2 = multiplication.group().replace("mul(", "").replace(")", "").split(',')
    endValue += int(num1) * int(num2)

print(endValue)