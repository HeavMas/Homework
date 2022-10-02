colvo = int(input())
all_l = set()
for i in range(colvo):
    all_l.add(input())
colvo1 = int(input())
notall = set()
for i in range(colvo1):
    notall.add(input())
colvo_2 = int(input())
notall1 = set()
for i in range(colvo_2):
    notall1.add(input())
print((all_l | notall | notall), (all_l & notall & notall))



