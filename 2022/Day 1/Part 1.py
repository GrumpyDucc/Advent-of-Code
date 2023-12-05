fileList = open("2022\\Day 1\\data.txt","r").read().split("\n\n")

caloriesList = []

for elves in fileList:
    calories = elves.split("\n")
    combinedCalories = 0
    for items in calories:        
        combinedCalories += int(items)
    caloriesList.append(combinedCalories)   

caloriesList.sort(reverse=True)
print(caloriesList[0] + caloriesList[1] + caloriesList[2])
