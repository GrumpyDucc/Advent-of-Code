import math

import timeit

t = timeit.default_timer()

input = open("2023/Day 8/input.txt", "r").read().split('\n')
endValue = 0

instructions = list(input[0])
nodes = input[2:]
hitList = []
nodesForIndexing = []
for node in nodes:
    nodesForIndexing.append(node.split(' = ')[0])

def indexNode(element):
    return nodesForIndexing.index(element)

currentNodes = []
for node in nodes:
    if node.split(' = ')[0].endswith('A'):
        currentNodes.append(node)

hitList = []

steps = 0
cnt = 0
instruction = 0
setLength = len(currentNodes)
while len(hitList) != setLength:
    if cnt > len(instructions)-1: cnt = 0
    if instructions[cnt] == 'L': instruction = 0
    elif instructions[cnt] == 'R': instruction = 1
    newNodes = []
    for currentNode in currentNodes:
        currentNode = nodes[indexNode(currentNode.split(' = ')[1].split(', ')[instruction].replace('(', '').replace(')', ''))]
        if currentNode.split(' = ')[0].endswith('Z'):
            hitList.append(steps+1)
        else:
            newNodes.append(currentNode)
    currentNodes = newNodes
    cnt += 1
    steps += 1

print(timeit.default_timer()-t)
print(math.lcm(*hitList))