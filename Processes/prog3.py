"""
Напишите функцию которая через канал обмена возвращает количество валюты которую можно приобрести на n сумму денег при курсе 1 к 75.
Запустите функцию в отдельном процессе и отправьте в нее данные задержкой в 0.5 секунды передайте ей разное количество доступных денег.
Выводите количество валюты на экран по мере обработки данных.
"""
import time
import multiprocessing
def exsj(n):
    print('Вы можете получить: ' + str(n * 75))
def repl(n, a):
    time.sleep(0.5)
    print('Вы получите : ',   (n * a) * 75)
if __name__ == '__main__':
    n = int(input('Введите сумму: '))
    p1 = multiprocessing.Process(target=exsj, args=(n,))
    a = float(input('Введите часть который нужно перевести№1:'))
    b = float(input('Введите часть который нужно перевести№2:'))
    p2 = multiprocessing.Process(target=repl, args=(n, a))
    p3 = multiprocessing.Process(target=repl, args=(n, b))
    p1.start()
    p1.join()
    p2.start()
    p2.join()
    p3.start()
    p3.join()
