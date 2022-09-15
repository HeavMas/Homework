def F(n):
    Summ = 0
    for i in range(len(n)):
        Summ += int(n[i])
    return Summ


Num = int(input())
if ((Num % 10) % 2 == 0) and F(str(Num)) % 3 == 0:
    print('Да делится')
else:
    print('Не делится')
