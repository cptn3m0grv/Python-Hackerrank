from collections import OrderedDict

orDict = OrderedDict()

for i in range(int(input())):
    userInput = input()
    defKey = 0
    if userInput in orDict:
        orDict[userInput] = orDict[userInput] + 1
    else:
        orDict[userInput] = 1

print(len(orDict.items()))
for key, value in orDict.items():
    print(value, end=" ")