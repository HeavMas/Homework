with open('list2.txt', 'w') as f:
    f.write('но у меня ничего не получается')
with open('list.txt', 'r') as f:
    with open('list2.txt', 'a') as file:
        file.write(str(f.read()))
with open('list2.txt', 'r') as f:
    for line in f:
        print(line)

