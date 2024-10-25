input = open("2015/Day 2 - I Was Told There Would Be No Math/input.txt", "r").read().split("\n")
endValue = 0

for line in input:
    l, w, h = map(int, line.split("x"))
    endValue += 2*l*w + 2*w*h + 2*h*l + min(l*w, w*h, h*l)
    
print(endValue)