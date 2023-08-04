operations = open("2022\\Day 7\\data.txt", "r").read().split("\n")

path = ""

for operation in operations:
    if str(operation).startswith("$ cd "):
        path = path + "/" + str(operation).split(" ")[2]
    if str(operation).startswith("$ cd .."):
        index = str(path).rindex("/")
        path = path[:index]

print(path)