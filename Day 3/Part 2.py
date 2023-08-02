allItems = open("Day 3\data.txt","r").read().split("\n")

priority = 0
count = 0
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

while count < len(allItems):
    common=list(set(allItems[count])&set(allItems[count + 1])&set(allItems[count + 2]))
    for letter in common:
        if letter.islower() != True:
            priority += 26
        priority += alphabet.index(letter.casefold()) + 1
    count += 3
        
print(priority)