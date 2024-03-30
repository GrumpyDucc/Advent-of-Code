from os import listdir, getcwd, remove, rename

def getText(year, day):
    return f'input = open("{year}/{day}/input.txt", "r").read().split("\\n")\nendValue = 0'

for year in listdir(getcwd()):
    if year.count(".") == 0:
        for day in listdir(year):
            for file in listdir(f"{year}/{day}"):
                if file == "part2.py" and open(f"{year}/{day}/part2.py", "r").read() == getText(year, day):
                    remove(f"{year}/{day}/part2.py")
                elif file == "Part 1.py":
                    rename(f"{year}/{day}/Part 1.py", f"{year}/{day}/part1.py")
                elif file == "Part 2.py":
                    rename(f"{year}/{day}/Part 2.py", f"{year}/{day}/part2.py")