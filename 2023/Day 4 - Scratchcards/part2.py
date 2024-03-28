input = open("2023/Day 4/input.txt", "r").read().split("\n")
endValue = 0
cardCount = 0
values = []
for i in range(len(input)):
    values.append(0)

def checkCards(cardList):
    global cardCount, input
    for card in cardList:
        cardCount += 1
        cardID = int(card.split(':')[0].split(' ')[-1])
        card = card.split(':')[1:][0].split('|')
        winningNums = card[0].split(' ')
        numToCheck = card[1].split(' ')

        matching = 0
        for num in winningNums:
            if num != '':
                if numToCheck.count(num) > 0:
                    matching += 1
        newCards = input[cardID:min(matching+cardID, len(input))]
        if len(newCards) != 0:
            checkCards(newCards)

checkCards(input)
print(cardCount)
