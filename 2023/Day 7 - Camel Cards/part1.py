input = open("2023/Day 7 - Camel Cards/input.txt", "r").read().split('\n')
if input[-1] == '': input = input[:-1]
endValue = 0

possibleCards = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']

def getValue(hand):
    values = []
    hand = [*hand]
    values = sorted([hand.count(c) for c in possibleCards])
    values.reverse()

    if values[0] == 5: return 6                             # Five of a kind
    if values[0] == 4: return 5                             # Four of a kind
    if values[0] == 3:
        if values[1] == 2: return 4                         # Full house
        else: return 3                                          # Three of a kind
    if values.count(2) == 2: return 2                       # Two pair
    if values.count(2) == 1: return 1                       # One pair
    return 0                                                # High card

def checkGreater(hand1, hand2):
    x = 0
    while hand1[x] == hand2[x]:
        x += 1
    highestCard1 = possibleCards.index(hand1[x])
    highestCard2 = possibleCards.index(hand2[x])
    if highestCard1 > highestCard2: return True
    else: return False

def getRank(hand1, value):
    for rank, hand2 in enumerate(reversed(ranking[value])):
        if checkGreater(hand1, hand2[0]): 
            return len(ranking[value]) - rank
    return 0

ranking = [[],[],[],[],[],[],[]]

for handBidString in input:
    hand, bid = handBidString.split(' ')
    handValue = getValue(hand)
    if ranking[handValue] == []:
        ranking[handValue].append((hand, bid))
    else:
        ranking[handValue].insert(getRank(hand, handValue), (hand, bid))

rank = 0
for group in ranking:
    for handBidString in group:
        rank += 1
        endValue += int(handBidString[1]) * rank
print(endValue)