"""
Создайте функцию которая из файла Names.txt берет имена, превращает его в путь до файла и помещает в очередь.
Создайте функцию которая создает txt файл  по пути из очереди.
Запустите все в разных потоках.
"""
from threading import Thread
from queue import Queue
import os
w = input()
def way(queue):
    with open('Names.txt', 'r', encoding='UTF-8') as f:
        a = f.read().split('\n')
    queue.put(a)

def repl(queue):
    lst = queue.get()
    for i in range(6):
        with open(f'{w + lst[i] +  ".txt"}', 'w') as f:
            f.write('файл' + str(i))
    queue.task_done()



def main():
    queue = Queue()
    Impname_thread = Thread(target=way, args=(queue, ))
    Impname_thread.start()
    Done_thread = Thread(target=repl, args=(queue, ), daemon=True)
    Done_thread.start()
    Impname_thread.join()
    queue.join()

if __name__ == '__main__':
    main()

