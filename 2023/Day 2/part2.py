games = open("Day 2/input.txt", "r").read().split("\n")
endValue = 0

for game in games:
    game = game.split(":")
    index = int(game[0].split(" ")[1])
    draws = game[1:][0].split(";")
    red = green = blue = 0
    for draw in draws:
        draw = draw.split(",")        
        for cubes in draw:
            cubes = cubes.split(" ")[1:]
            cubeCount = int(cubes[0])
            if cubes[1] == 'red' and cubeCount > red:
                red = cubeCount
            elif cubes[1] == 'green' and cubeCount > green:
                green = cubeCount
            elif cubes[1] == 'blue' and cubeCount > blue:
                blue = cubeCount
    endValue += red * blue * green
print(endValue)