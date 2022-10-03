def F(n):
    if 0 < n < 49:
        return ('Скидка 10%')
    if 50 < n < 99:
        return ('Скидка 15%')
    if n >= 100:
        return ('Скидка 20%')
a = int(input())
print(F(a))
