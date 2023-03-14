import multiprocessing

def first(width, length, height):
    s = 2 * (width * height) + 2 * (length * height)
    with open('answer.txt', "w") as f:
        f.write(str(s))
    return s

def second():
    with open('answer.txt', "r") as f:
        s = f.read()
    with open('answer.txt', "a") as f:
        f.write(' ' + str(5 * int(s)))

if __name__ == '__main__':
    width = int(input('Введите ширину: '))
    length = int(input('Введите длину: '))
    height = int(input('Введите высоту: '))
    p1 = multiprocessing.Process(target=first, args=(width, length, height, ))
    p2 = multiprocessing.Process(target=second)
    p1.start()
    p1.join()
    p2.start()