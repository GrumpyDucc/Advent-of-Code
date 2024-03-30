input = open("2023/Day 16 - The Floor Will Be Lava/input.txt", "r").read().split("\n")
endValue = 0

p = []
for i in input:
    p.append(list(i))

# --- INFO ---
# . -> beam coninues
# / or \ -> beam turns 90 degrees
# | or - (pointy end) -> beam continues
# | or - (flat end) -> beam splits into two beams
# Beams do not interact with other beams

class Beam:
    def __init__(self, x:int, y:int, d:str) -> None:
        self.x = x
        self.y = y
        self.d = d

    def getValues(self): return self.x, self.y, self.d

    def changeDirection(self, d:str): self.d = d

    def move(self):
        match self.d:
            case "u": 
                if self.y > 0: self.y -= 1; return True # Move up
                else: return False
            case "d": 
                if self.y < len(input)-1: self.y += 1; return True # Move down
                else: return False
            case "l": 
                if self.x > 0: self.x -= 1; return True # Move left
                else: return False
            case "r": 
                if self.x < len(input[0])-1: self.x += 1; return True # Move right
                else: return False

def checkBeam(beam:Beam):
    x, y, d = beam.getValues()
    beamIndex = beams.index(beam)
    match input[y][x]:
        case ".": return
        case "|":
            if d == "r" or d == "l":
                beams[beamIndex].changeDirection('u')
                beams.append(Beam(x, y, 'd'))
        case "-":
            if d == "u" or d == "d":
                beams[beamIndex].changeDirection('l')
                beams.append(Beam(x, y, 'r'))
        case "/":
            if   d == "r": beams[beamIndex].changeDirection('u')
            elif d == "d": beams[beamIndex].changeDirection('l')
            elif d == "l": beams[beamIndex].changeDirection('d')
            elif d == "u": beams[beamIndex].changeDirection('r')
        case "\\":
            if   d == "r": beams[beamIndex].changeDirection('d')
            elif d == "d": beams[beamIndex].changeDirection('r')
            elif d == "l": beams[beamIndex].changeDirection('u')
            elif d == "u": beams[beamIndex].changeDirection('l')

beams = [Beam(0, 0, 'r')]
energyMap = [["."] * len(input[0]) for _ in range(len(input))]
roundsWithoutChange = []
r = 0

def energize(beam:Beam):
    global roundsWithoutChange, r, endValue
    x, y, _ = beam.getValues()
    r += 1
    if energyMap[y][x] != "#":
        energyMap[y][x] = "#"
        endValue += 1
        roundsWithoutChange.clear()
    else:
        roundsWithoutChange.append(r)
        pass

while beams and len(roundsWithoutChange) < 10000:
    for beam in beams:
        energize(beam)
        checkBeam(beam)
        if not beam.move(): beams.remove(beam)
print(energyMap)
print(endValue)