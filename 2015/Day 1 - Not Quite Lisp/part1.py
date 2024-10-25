input = open("input.txt", "r").read()
endValue = 0

endValue += input.count("(") - input.count(")")

print(endValue)