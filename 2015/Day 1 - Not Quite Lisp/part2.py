input = open("input.txt", "r").read()

floor = 0
cnt = 0

for door in input:
    if (door == "("):floor += 1
    else:floor -= 1
    cnt += 1
    if (floor == -1):
        print(cnt)
        break