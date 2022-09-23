games = []
a = input()
games.append(a)
while a != '0':
    a = input()
    if a not in games:
        games.append(a)
    else:
        print('Игра уже существует')
games.pop()
games.sort()
print(games)