nums = []
a = input()
nums.append(a)
while a != '0':
    a = input()
    nums.append(a)
nums.pop()
print(nums)
print('count 5:', nums.count('5'), 'count 4:', nums.count('4'), 'count 3:', nums.count('3'), 'count 2:', nums.count('2'))
print((nums.count('5') + nums.count('4') + nums.count('3')) / len(nums) * 100)