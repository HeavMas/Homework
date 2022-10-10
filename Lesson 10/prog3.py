from random import *
k1 = 0
k2 = 0
while True:
    a = input('Введите off чтобы выключить, введите enter чтобы протолжить:')
    if a == 'off':
        break
    b = randint(0, 1)
    print('ваш номер:', b)
    if b == 0:
        k1 += 1
    else:
        k2 += 1
    print('В первом забеге:', k1, 'Во втором забеге:', k2)
