input = open("2023/Day 8/input.txt", "r").read().split('\n')
endValue = 0

instructions = list(input[0])
nodes = input[2:]
nodesForIndexing = []
for node in nodes:
    nodesForIndexing.append(node.split(' = ')[0])

def indexNode(element):
    return nodesForIndexing.index(element)

def similar(array):
    if array:
        count = 0
        for item in array:
            if item.endswith('Z'):
                count += 1
        if count == len(array): return True
        else: return False

currentNodes = []

for node in nodes:
    if node.split(' = ')[0].endswith('A'):
        currentNodes.append(node)

lastLetterArray = []
steps = 0
cnt = 0
instruction = 0

while not similar(lastLetterArray):
    newNodes = []
    lastLetterArray = []
    if cnt > len(instructions)-1: cnt = 0
    if instructions[cnt] == 'L': instruction = 0
    elif instructions[cnt] == 'R': instruction = 1
    for currentNode in currentNodes:
        node = nodes[indexNode(currentNode.split(' = ')[1].split(', ')[instruction].replace('(', '').replace(')', ''))]
        newNodes.append(node)
        lastLetterArray.append(list(node.split(' = ')[0])[-1])
    cnt += 1    
    steps += 1
    currentNodes = newNodes
print(steps)