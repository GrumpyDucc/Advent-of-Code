input = open("2023/Day 7/inputtest2.txt", "r").read().split('\n')
endValue = 0

sortedHands = []
alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
cnt = 0

def getLetterValue(letter):
    return alphabet.index(letter) + 1

def getValue(hand):
    checked = []
    fullList = []
    value = 0
    hand = hand.split(' ')[0]
    splitHand = list(hand)
    for label in splitHand:
        if label not in checked:
            count = hand.count(label)
            checked.append(label)
            fullList.append((count, label))
    fullList.sort(reverse=True)
    # Wertigkeitssetzung
    if fullList[0][0] == 5: # Five of a kind, where all five cards have the same label: AAAAA
        value = 6
    elif fullList[0][0] == 4: # Four of a kind, where four cards have the same label and one card has a different label: AA8AA
        value = 5
    elif fullList[0][0] == 3 and fullList[1][0] == 2: # Full house, where three cards have the same label, and the remaining two cards share a different label: 23332
        value = 4
    elif fullList[0][0] == 3 and fullList[1][0] == 1: # Three of a kind, where three cards have the same label, and the remaining two cards are each different from any other card in the hand: TTT98
        value = 3
    elif fullList[0][0] == 2 and fullList[1][0] == 2: # Two pair, where two cards share one label, two other cards share a second label, and the remaining card has a third label: 23432
        value = 2
    elif fullList[0][0] == 2 and fullList[1][0] == 1: # One pair, where two cards share one label, and the other three cards have a different label from the pair and each other: A23A4
        value = 1
    elif fullList[0][0] == 1: # High card, where all cards' labels are distinct: 23456
        value = 0
    return value

def compare(currHand, prevHand):
    currVal = 0
    prevVal = 0
    for i in range(5):
        if not currHand[i].isdigit(): currVal = getLetterValue(currHand[i])
        else: currVal = currHand[i]
        if not  prevHand[i].isdigit(): prevVal = getLetterValue(prevHand[i])
        else: prevVal = prevHand[i]

        if int(currVal) > int(prevVal):
            return 0
        elif int(currVal) < int(prevVal):
            return 1
    return -1

for hand in input:
    if len(sortedHands) > 0:
        cnt = len(sortedHands)
        hVal = getValue(hand)
        while hVal > getValue(sortedHands[cnt-1]):
            cnt -= 1
            if cnt == 0:
                sortedHands.insert(cnt, hand)
                break
        else:
            # sort if same value
            if hVal == getValue(sortedHands[cnt-1]):
                index = cnt
                index = compare(list(hand.split(' ')[0]), list(sortedHands[index-1].split(' ')[0]))
                sortedHands.insert(cnt - index, hand)
            else: sortedHands.insert(cnt, hand)
    else:
        sortedHands.append(hand)
sortedHands.reverse()
cnt = 0
for hand in sortedHands:
    cnt += 1
    endValue += cnt * int(hand.split(' ')[1])
print(endValue)