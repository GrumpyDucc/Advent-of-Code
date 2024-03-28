operations = open("2022\\Day 7\\data.txt", "r").read().split("\n")

path = "/"

for operation in operations:
    if operation.startswith("$ cd"):
        task = operation.split(" ")[2]
        if task == "..":
            index = path.rfind("/")
            path = path[:index-1]
        else:
            path = f"{path}/{task}"
                