"""
Запустите фоновый процесс который следит за сроком подписки пользователя( для примера 10 секунд) если время подписки вышло выведите надпись "Ваша подписка закончилась."
и завершите работу программы. В основной программе сыграйте с пользователем в игру "угадай число".
"""
import multiprocessing
from threading import Thread
from threading import Event
import time
import sys

def fon(n):
    time.sleep(n)
    print('Время вышло')
if __name__=="__main__":
    a = int(input('Введите время вашей подписки: '))
    p1 = multiprocessing.Process(target=fon, args=(a, ))
    p1.start()
    if p1.is_alive() is True:
        n = int(input('Угадай цифру: '))
        if n == 6:
            print('Верно')
        else:
            print('Не верно')