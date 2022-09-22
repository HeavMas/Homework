Short = float(input())
hg = float(input())
Cost = float(input())
VB = float(input())
SaveC = float(input())
NeedC = Short * hg
CountB = NeedC / Cost
Banki = round((CountB / VB) + 1)
print(round(NeedC, 2))
print(round(CountB * (1 + SaveC / 100), 2))
print(Banki)#переделать
print(Banki * VB) #переделать