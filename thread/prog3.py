"""
Создайте функцию в демоне потока которая каждые 3 секунды будет писать "Вводите быстрее".
В основной части программы запросите ввод кода от бомбы и если код неверный выведите: "Вы взорвались", если верный - "Бомба разминирована"
"""
import sys
import time
from threading import Thread
def faster():
    while True:
        time.sleep(3)
        print('\n')
        print('МУЖИК БЫСТРЕЙ')
Th_1 = Thread(target=faster, daemon=True, args=())
Th_1.start()
a = int(input('Обезвредь бомбу(только цифры): '))
if a == 1111:
    print('Красава бомба обезврежена')
    sys.exit()
else:
    print('Бомба взорвалась')
    sys.exit()
