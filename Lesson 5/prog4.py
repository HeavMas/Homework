info = []
TnameL = []
rangL = []
countSl = []
while True:
    Tname = input('Name:')
    if Tname == '':
        break
    rang = input('rang:')
    countS = input('Count:')
    TnameL.append(Tname)
    rangL.append(rang)
    countSl.append(countS)
info.insert(0, TnameL)
info.insert(1, rangL)
info.insert(2, countSl)
print(info)
