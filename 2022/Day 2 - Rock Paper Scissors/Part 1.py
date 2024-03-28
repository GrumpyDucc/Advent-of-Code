turnList = open("2022\\Day 2\\data.txt","r").read().split("\n")

score = 0

for turn in turnList:
    moves = turn.split(" ")

    if moves[0] == "A":
        m1 = 1
    elif moves[0] == "B":
        m1 = 2
    else:
        m1 = 3
    
    if moves[1] == "X":
        m2 = 1
    elif moves[1] == "Y":
        m2 = 2
    else:
        m2 = 3
    
    if m1 == m2:
        score += m2 + 3         # Unentschieden
    if m1 == 1 and m2 == 2:     # Stein, Papier  > win
        score += m2 + 6         
    if m1 == 1 and m2 == 3:     # Stein, Schere  > loss
        score += m2
    if m1 == 2 and m2 == 1:     # Papier, Stein  > loss
        score += m2
    if m1 == 2 and m2 == 3:     # Papier, Schere > win
        score += m2 + 6
    if m1 == 3 and m2 == 1:     # Schere, Stein  > win
        score += m2 + 6
    if m1 == 3 and m2 == 2:     # Schere, Papier > loss
        score += m2

print(score)