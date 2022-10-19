def main(input):
    if 'расп' in input.lower():
        timetable()
    if 'трен' in input.lower():
        coach()
    if 'оплат' in input.lower():
        cost()
    if 'назв' in input.lower():
        nameK()
    if 'сайт' in input.lower():
        site()
    if 'зап' in input.lower():
        record()


slov = dict()


def timetable():
    if str(slov) != '{}':
        print(slov)
    else:
        print('Все дни свободны')


def coach():
    print('Контакт Магомэда - +79288735502')
    print('Одноклассники - Магомэд Магомэдов')


def cost():
    print('С вас таки 123841 шекелей')


def nameK():
    print('Наша компания - Гачикач 3000')


def site():
    print('Наш сайт - gachikach3000.com')


def record():
    date = input('Введите день: ')
    time = input('Введите время с 8 - 22: ')
    if time in str(slov.get(date)):
        print('На такое время уже есть записать')
        return record()
    else:
        if 22 > int(time) > 8:
             slov[date] = time
        else:
            print('Неправильное время')
            return record()