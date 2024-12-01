data = open("2023/Day 12 - Hot Springs/testinput.txt", "r").read().strip().splitlines()
endValue = 0

"""
???.### 1,1,3
.??..??...?##. 1,1,3
?#?#?#?#?#?#?#? 1,3,1,6
????.#...#... 4,1,1
????.######..#####. 1,6,5
?###???????? 3,2,1
"""

for row in data:
    record, notes = row.split()
    record = tuple(record)
    notes = tuple(notes.split(","))

    """
    splitRecord = []
    save = ''
    for char in record:
        save += char
        if len(save) != 1 and char != save[-2]:
            splitRecord.append(save[:-1])
            save = save[-1]
    splitRecord.append(save)
    record = splitRecord
    """
    
    currentRecordIndex = 0
    currentNoteIndex = 0
    while currentRecordIndex < len(record):
        currentChar = record[currentRecordIndex]
        if currentChar == '?':
            print(record[currentRecordIndex:int(notes[currentNoteIndex])])
        
        currentRecordIndex += 1
    break