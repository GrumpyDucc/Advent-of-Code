database = open("2025/Day 5/input.txt", 'r').read().split('\n\n')
ingredientIDs = database[0].split('\n')
avaliableIngredientIDs = list(map(lambda x: int(x), database[1].split('\n')))

freshIngredients = 0

for avaliableIngredientID in avaliableIngredientIDs:
    for idRange in ingredientIDs:
        idRange = list(map(lambda x: int(x), idRange.split('-')))
        print(idRange)
        if avaliableIngredientID in range(idRange[0], idRange[1]+1):
            freshIngredients += 1
            break

print(freshIngredients)
