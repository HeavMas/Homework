#newspaper = range(1, 76)
#magazine = range(77, 104)
#both = range(21, 34)
newspaper = set()
magazin = set()
both = set()
for i in range(1, 76):
    newspaper.add(i)
for i in range(77, 104):
    magazin.add(i)
for i in range(21, 34):
    both.add(i)
all = set()
all.update(newspaper | magazin | both)
print(len(all))