input = open("2023/Day 15 - Lens Library/input.txt", "r").read().split(",")
endValue = 0

# --- HASH FUNCTION ---
# Determine the ASCII code for the current character of the string.
# Increase the current value by the ASCII code you just determined.
# Set the current value to itself multiplied by 17.
# Set the current value to the remainder of dividing itself by 256.

for step in input:
    currentValue = 0
    for char in step:
        currentValue += ord(char)
        currentValue *= 17
        currentValue %= 256
    endValue += currentValue
print(endValue)