#Программа 5 без цикла
Num = int(input())
if ((Num % 10) % 2 == 0) and sum(map(int, list(str(Num)))) % 3 == 0:
    print('Да делится')
else:
    print('Не делится')
