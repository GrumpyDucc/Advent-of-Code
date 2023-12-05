input = open("2023/Day 4/input.txt", "r").read().split("\n")
endValue = 0

for card in input:
    points = 0
    card = card.split(':')[1:][0].split('|')
    winningNums = card[0].split(' ')
    numToCheck = card[1].split(' ')
    for num in winningNums:
        if num != '':
            if numToCheck.count(num) > 0:
                if points == 0:
                    points += 1
                else:
                    points = points * 2
    endValue += points

print(endValue)