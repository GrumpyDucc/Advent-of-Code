turnList = open("Day 2\data.txt","r").read().split("\n")

score = 0
draw = 3
win = 6
loss = 0

for turn in turnList:
    moves = turn.split(" ")

    m1 = moves[0]
    m2 = moves[1]

    if m1 == "A" and m2 == "X":
        score += 3 + loss
    elif m1 == "A" and m2 == "Y":
        score += 1 + draw
    elif m1 == "A" and m2 == "Z":
        score += 2 + win
    elif m1 == "B" and m2 == "X":
        score += 1 + loss
    elif m1 == "B" and m2 == "Y":
        score += 2 + draw
    elif m1 == "B" and m2 == "Z":
        score += 3 + win
    elif m1 == "C" and m2 == "X":
        score += 2 + loss
    elif m1 == "C" and m2 == "Y":
        score += 3 + draw
    elif m1 == "C" and m2 == "Z":
        score += 1 + win

print(score)