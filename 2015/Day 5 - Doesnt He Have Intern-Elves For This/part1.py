input = open("2015/Day 5 - Doesnt He Have Intern-Elves For This/input.txt", "r").read().split("\n")
endValue = 0

vowels = ["a", "e", "i", "o", "u"]
banned = {"ab", "cd", "pq", "xy"}

for line in input:
    vowelCount = 0
    hasDouble = False
            
    for index, letter in enumerate(line):
        for vowel in vowels:
            vowelCount += line.count(vowel)
        if index + 1 <= len(line) - 1 and line[index + 1] == letter: hasDouble = True
    
    if vowelCount < 3: break
    if not hasDouble: break
    
    for ban in banned:
        if line.count(ban) >= 1: break
        
    endValue += 1

print(endValue)