input = open("Day 1/input.txt", "r").read().split("\n")
endValue = 0

for line in input:
    for char in line:
        if char.isdigit():
            firstNum = char
            break
    for char in reversed(line):
        if char.isdigit():
            lastNum = char
            break
    fullNum = int(f"{firstNum}{lastNum}")
    endValue += fullNum
print(endValue) 