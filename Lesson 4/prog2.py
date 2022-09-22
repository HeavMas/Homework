while True:
    a = input()
    if a == 'game':
        print('УГАДАЙ ЧИСЛО')
        for i in range(3):
            b = input('Введите число: ')
            if b != '5':
                print('Неверно')
            if b == '5':
                print('Вы выиграли билет на концерт')
                break
    else:
        print('Неправильная команда. (ДОСТУПНЫЕ КОМАНДЫ(game, off))')
    if a == 'off':
        break