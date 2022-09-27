numbers = "0139412831055230677798"
a = {}
for i in range(0, 10):
    a[i] = numbers.count(str(i))
print(a)