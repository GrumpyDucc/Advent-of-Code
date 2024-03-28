import timeit

t = timeit.default_timer()

input = open("2023/Day 8/input.txt", "r").read().split('\n')
endValue = 0

instructions = list(input[0])
nodes = input[2:]

def indexNode(element):
    startIndex  = 0
    for node in nodes:
        node = node.split('=')[0]
        if element in node:
            return startIndex
        else:
            startIndex += 1
    return 0

startIndex = indexNode('AAA')
currentNode = nodes[startIndex]

steps = 0
cnt = 0
instruction = 0
while currentNode.split(' = ')[0] != 'ZZZ':
    if cnt > len(instructions)-1: cnt = 0
    if instructions[cnt] == 'L': instruction = 0
    elif instructions[cnt] == 'R': instruction = 1
    currentNode = nodes[indexNode(currentNode.split(' = ')[1].split(', ')[instruction].replace('(', '').replace(')', ''))]
    cnt += 1
    steps += 1
print(steps)

print(timeit.default_timer()-t)