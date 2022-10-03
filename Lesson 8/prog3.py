def F(n):
    if n <= 50:
        print('False', 'Ти болше не студент')
    if n > 50:
        print('True')
Count = int(input())
for i in range(Count):
    a = int(input())
    print(F(a))
