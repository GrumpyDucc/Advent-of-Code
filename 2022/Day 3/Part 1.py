allItems = open("Day 3\data.txt","r").read().split("\n")

priority = 0
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

for rucksacks in allItems:
    firstContainer, secondContainer = rucksacks[:len(rucksacks)//2], rucksacks[len(rucksacks)//2:]
    common=list(set(firstContainer)&set(secondContainer))
    for letter in common:
        if letter.islower() != True:
            priority += 26
        priority += alphabet.index(letter.casefold()) + 1
        
print(priority)