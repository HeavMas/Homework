import sys
user_input = sys.stdin.readline()
if user_input[:7] == 'sys.in.':
    print('Command apply')
else:
    print('Enable command')
