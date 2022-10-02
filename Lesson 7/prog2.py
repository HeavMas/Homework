testList = [1, 2, 2, [3, 4], (1, 2, 3), "1", {1, 2, 3}]
printSet = set()
Flag = True
for i in testList:
    try:
        printSet.add(i)
        testList.remove(i)
    except:
        Flag = False
print(Flag, testList)

