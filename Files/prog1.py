with open('list.txt', 'w') as f:
    f.write('Один Один Два Два Три Один, Три, Четыре, Два, Два, Два, Два., Два')
    f.write('Один Один Два Два Три Один, Три, Четыре, Два, Два, Два, Два., Два')
with open('list.txt', 'r') as f:
    print(f.read(7))