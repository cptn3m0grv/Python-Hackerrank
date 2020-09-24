from collections import OrderedDict

orDict = OrderedDict()

for i in range(int(input())):
    userInput = input().split(' ')
    dictKey = ' '.join(userInput[:-1])
    dictValue = int(userInput[-1])
    if dictKey in orDict:
        orDict[dictKey] = orDict[dictKey] + dictValue
    else:
        orDict[dictKey] = dictValue

for key, value in orDict.items():
    print(key, value)