def F():
    a = input()
    if a != '':
        return int(a) + F()
    else:
        return 0




print(F())