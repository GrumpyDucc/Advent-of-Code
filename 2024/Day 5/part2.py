from aocd import get_data
from random import shuffle

USE_TEST_INPUT = False
if USE_TEST_INPUT: input = open("2024/Day 5/tinput.txt", 'r').read()
else: input = get_data(day=5, year=2024)
endValue = 0

ruleSet, updates = input.split("\n\n")
ruleSet = ruleSet.split('\n')
ruleSet = [x.split('|') for x in ruleSet]
updates = updates.strip().split('\n')
updates = [x.split(',') for x in updates]

def ruleApplys(rule:str | list[str], update:list[str]):
    if update.count(rule[0]) > 0 and update.count(rule[1]) > 0:
            first = update.index(rule[0])
            second = update.index(rule[1])
            
            if first > second:
                return False
    return True

def allRulesApply(update:list[str]) -> bool:
    for rule in ruleSet:
        if not ruleApplys(rule, update): return False
    return True

def bringToCorrectOrder(update:list[str]) -> list[str]:
    while not allRulesApply(update):
        for rule in ruleSet:
            if not ruleApplys(rule, update):
                first = update.index(rule[0])
                second = update.index(rule[1])
                
                update.pop(second)
                update.insert(first, rule[1]) #place 2nd behind 1st
    return update

for update in updates:
    if not allRulesApply(update):
        corrrectlyOrderedUpdate = bringToCorrectOrder(update)
        middleValue = int(corrrectlyOrderedUpdate[int(len(corrrectlyOrderedUpdate)/2)])
        endValue += middleValue

print(endValue)