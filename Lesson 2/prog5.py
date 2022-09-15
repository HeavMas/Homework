Eml = input()
login = ''
for i in Eml:
    if i != '@':
        login += i
    else:
        break
print(login)
