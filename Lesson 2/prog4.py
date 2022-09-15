St = input()
aF = ''
for i in St:
    if i != ' ':
        aF += i
    else:
        break
print(St[len(aF) + 1:] + ' ' + aF)