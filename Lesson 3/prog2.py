Num = int(input())
Time = int(input())
if Time > 22 or Time < 8:
    print('Мы не работаем')
else:
    if (Time > 10) and (Time < 12):
        print(Num / 2)
    elif (Time > 20) and (Time < 22):
        print(Num / 4)
