Summ = 0
while True:
    tov = int(input())
    if tov == 0:
        break
    Summ += tov
if Summ % 2 == 0:
    while Summ % 2 == 0:
        Summ /= 2
else:
    Summ *= 0.75
print(Summ)
