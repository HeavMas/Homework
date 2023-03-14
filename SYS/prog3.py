import sys
first_arg = sys.stdin.readline()
second_arg = sys.stdin.readline()
f = open(second_arg, 'w')
f.write(first_arg)
f.close()