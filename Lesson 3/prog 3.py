Tov1 = int(input())
Tov2 = int(input())
Tov3 = int(input())
if Tov3 > Tov2 > Tov1:
    print('АКЦИЯ!', (Tov1 + Tov2 + Tov3) / 2)
elif Tov1 > Tov2 > Tov3:
    print('АКЦИЯ!', (Tov3 + Tov2 + Tov1) / 3)
else:
    print('К оплате:' + str(Tov1 + Tov2 + Tov3))
