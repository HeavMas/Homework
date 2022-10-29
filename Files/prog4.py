inp_filename = input() + '.txt'
new_f = ''
with open(inp_filename, 'r') as f:
    for i in f:
        new_f += i
new_f = new_f.replace(',', '')
new_f = new_f.replace('.', '')
new_f = new_f.lower()
lst = list(new_f.split(' '))
maxW = 0
wordW = ''
for i in lst:
    if lst.count(i) > maxW:
        maxW = lst.count(i)
        wordW = i


print(wordW)