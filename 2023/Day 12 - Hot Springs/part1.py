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
    notes = tuple(notes.split(","))

    for note in notes:
        
