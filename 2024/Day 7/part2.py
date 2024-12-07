from aocd import get_data

USE_TEST_INPUT = True
if USE_TEST_INPUT: input = open("2024/Day 7/tinput.txt", 'r').read().strip()
else: input = get_data(day=7, year=2024)
endValue = 0

equations = [x.split(':') for x in input.split('\n')]
equations = [[int(eq[0]), eq[1].split()] for eq in equations]

for eqation in equations:
    result = eqation[0]
    nums = list(map(int, eqation[1]))
    
    isResult = False
    maxOptions = pow(2, len(nums)-1)
    for i in range(0, maxOptions):
        if isResult: break
        binary = bin(i).replace("0b", '').zfill(len(nums)-1).replace('0', '+').replace('1', '*')
        
        eqationResult = 0
        isFirst = True
        for i, operator in enumerate(binary):
            if operator == "+": 
                if isFirst: eqationResult += nums[i] + nums[i+1]
                else: eqationResult += nums[i+1]
                isFirst = False
            else:
                if isFirst: eqationResult += nums[i] * nums[i+1]
                else: eqationResult *= nums[i+1]
                isFirst = False
        if eqationResult == result:
            endValue += result
            print(result,  "->", endValue)
            isResult = True
            break
        else:
            newEqations = []
            for i in range(len(nums)-1):
                concatedNumbers = int(str(nums[i])+str(nums[i+1]))
                numbersAfter = nums[i+2:]
                numbersBefore = nums[:i]
                newEqations.append([*numbersBefore, concatedNumbers, *numbersAfter])
            
            if len(newEqations) == 1:
                if newEqations[0][0] == result:
                    endValue += result
                    print(result, "concating ->", endValue)
                    isResult = True
                    break
                else: break
            
            for newNum in newEqations:
                if isResult: break
                maxOptions = pow(2, len(newNum)-1)
                for i in range(0, maxOptions):
                    binary = bin(i).replace("0b", '').zfill(len(newNum)-1).replace('0', '+').replace('1', '*')
                    
                    eqationResult = 0
                    isFirst = True
                    for i, operator in enumerate(binary):
                        if operator == "+": 
                            if isFirst: eqationResult += newNum[i] + newNum[i+1]
                            else: eqationResult += newNum[i+1]
                            isFirst = False
                        else:
                            if isFirst: eqationResult += newNum[i] * newNum[i+1]
                            else: eqationResult *= newNum[i+1]
                            isFirst = False
                    if eqationResult == result:
                        endValue += result
                        print(result, "concating ->", endValue)
                        isResult = True
                        break

print(endValue)