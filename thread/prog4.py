"""
Создайте функцию которая принимает путь до файла из папки files и меняет в нем "ids" на "id".
Запустите функцию для каждого файла в отдельном потоке.
Измерьте время выполнения программы.
"""

import time
import os
from threading import Thread
way = input()
def repl(i):
    with open(f'{way + "file" + str(i) + ".txt"}', 'r') as f:
        id = f.read()
    id = id.replace('ids', 'id')
    with open(f'{way + "file" + str(i) + ".txt"}', 'w') as f:
        f.write(id)
for i in range(10):
    th = Thread(target=repl(i), args=(i, ))
    th.start()
