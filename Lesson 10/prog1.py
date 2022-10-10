from time import *
def chess():
    Atime = 30
    while True:
         start = time()
         a = input()
         if a == 'off':
            break
         end = time()
         total = round((end - start) / 60, 2)
         Atime -= total
         print(Atime)
chess()
