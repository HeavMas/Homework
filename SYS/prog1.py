import sys
St = ''
k = 0
for i in sys.argv:
    St += i
if '--name' not in St:
    print('Hello world')
else:
    St.split(' ')
    for i in St:
        if i == '--name':
            break
        else:
            k += 1
    print(St[k + 1])