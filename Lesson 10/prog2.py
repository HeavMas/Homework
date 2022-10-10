from random import *
a1 = int(input('Введите кол-во участников Из сборной 1:'))
b1 = int(input('Введите кол-во участников Из сборной 2:'))
a = randint(0, a1)
b = randint(0, b1)
if a == b:
    a = randint(0, a1)
    b = randint(0, b1)
print('Спортсмен из сборной 1:', a, 'Спортсмен из сборной 2:', b)

