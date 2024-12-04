from aocd import get_data
input = get_data(day=3, year=2024)
endValue = 0

import re
multiplications = re.finditer("mul\\(\\d{0,3},\\d{0,3}\\)",input)
for multiplication in multiplications:
    span = multiplication.span() 
    num1, num2 = multiplication.group().replace("mul(", "").replace(")", "").split(',')
    endValue += int(num1) * int(num2)

print(endValue)