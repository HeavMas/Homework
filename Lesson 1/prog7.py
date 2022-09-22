cash = 1572
cost = int(input())
if cash < cost:
    print(0)
if cash > cost:
    print(cash // cost)