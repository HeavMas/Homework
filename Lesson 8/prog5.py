def F(n):
    a = 0
    for i in range(n):
        a += int(input())
    return a
def G(q):
    print('Итоговый счет:', q)
    if q > 80:
        print('Наградить дипломом')
    if 50 > q < 80:
        print('Наградить похвальной грамотой')
    if q < 50:
        print('Дать на пиво')
while True:
    Name = input()
    if Name == 'stop':
        break
    Count = int(input())
    if Count == 'stop':
        break
    print(G(F(Count)))



