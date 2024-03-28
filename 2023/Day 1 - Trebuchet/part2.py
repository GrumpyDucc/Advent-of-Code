input = open("2023/Day 1/input.txt", "r").read().split("\n")
endValue = 0

for line in input:
    line = line.replace("oneight", "18").replace("twone", "21").replace("threeight", "38").replace("fiveight", "58").replace("sevenine", "79").replace("eighthree", "83").replace("eightwo", "82").replace("nineight", "98").replace("one", "1").replace("two", "2").replace("three", "3").replace("four", "4").replace("five", "5").replace("six", "6").replace("seven", "7").replace("eight", "8").replace("nine", "9")
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