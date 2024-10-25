input = open("2015/Day 2 - I Was Told There Would Be No Math/input.txt", "r").read().split("\n")
endValue = 0

for line in input:
    l, w, h = map(int, line.split("x"))
    wrap = 2*l + 2*w + 2*h - 2*max(l, w, h)
    bow = l*w*h
    endValue += wrap + bow
    
print(endValue)