datasheet = open("2023/Day 9/inputtest.txt", "r").read().split('\n')
endValue = 0

def getDifferenceSequence(history):    
    sequence = []
    currValue = None
    for value in history:
        prevValue = currValue
        currValue = value
        if prevValue != None:
            sequence.append(int(currValue) - int(prevValue))
    historySequences.append(sequence)
    if len(sequence) > 0 and any(sequence):
        getDifferenceSequence(sequence)

for history in datasheet:
    historySequences = []
    history = history.split(' ')
    historySequences.append(history)
    getDifferenceSequence(history)
    historySequences[len(historySequences)-1].append(0)
    cnt = 0
    while cnt < len(historySequences)-1:
        cnt += 1

        # a - b = c -> b = (c - a) * -1
        c = int(historySequences[len(historySequences)-cnt-1][-1])
        a = int(historySequences[len(historySequences)-cnt][-1])
        b = c + a
        
        historySequences[len(historySequences)-cnt-1].append(b)
    endValue += historySequences[0][-1]
print(endValue)