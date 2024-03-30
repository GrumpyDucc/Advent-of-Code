input = open("2023/Day 16 - The Floor Will Be Lava/input.txt", "r").read().split("\n")
endValue = 0

# --- INFO ---
# . -> beam coninues
# / or \ -> beam turns 90 degrees
# | or - (pointy end) -> beam continues
# | or - (flat end) -> beam splits into two beams
# Beams do not interact with other beams

beams = []

class Beam:
    def __init__(self, x, y, d) -> None:
        self.x = x
        self.y = y
        self.d = d
    
    def checkBlock(self):
        match input[self.y][self.x]:
            case "|": 

    def moveUp(self):
        self.y -= 1
    
    def moveDown(self):
        self.y += 1

    def moveLeft(self):
        self.x -= 1

    def moveRight(self):
        self.x += 1

    def move(self):
        match self.d:
            case "u":
                self.moveUp()
            case "d":
                self.moveDown()
            case "l":
                self.moveLeft()
            case "r":
                self.moveRight()