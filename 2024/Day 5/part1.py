from aocd import get_data

USE_TEST_INPUT = True
if USE_TEST_INPUT: input = open("2024/Day 5/tinput.txt", 'r').read()
else: input = get_data(day=5, year=2024)
endValue = 0

ruleSet, updates = input.split("\n\n")
ruleSet = ruleSet.split('\n')
ruleSet = [x.split('|') for x in ruleSet]
updates = updates.strip().split('\n')
updates = [x.split(',') for x in updates]

def allRulesApply(update:list[str]) -> bool:
    for rule in ruleSet:
        if update.count(rule[0]) > 0 and update.count(rule[1]) > 0:
            first = update.index(rule[0])
            second = update.index(rule[1])
            
            if first > second:
                return False
    return True

for update in updates:
    if allRulesApply(update):
        middleValue = int(update[int(len(update)/2)])
        endValue += middleValue

print(endValue)