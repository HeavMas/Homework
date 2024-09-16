numsL = []
num = int(input())
numsL.append(num)
while num != '':
    num = input()
    try:
        numsL.append(int(num))
    except:
        pass
if len(numsL) > 1:
    flag = True
    for i in range(1, len(numsL)):
        if numsL[i - 1] > numsL[i]:
            flag = False
    if flag == True:
        print('ДА')
    else:
        print('НЕТ')
else:
    print('НЕТ')
