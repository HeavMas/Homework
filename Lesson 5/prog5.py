#НЕДОДЕЛАЛ
nums = []
while True:
    a = input()
    if a == '':
        break
    nums.append(int(a))
if len(nums) != 1:
    flag = True
    for i in range(len(nums)):
        try:
            if nums[i] > nums[i + 1]:
                flag = False
        except:
            pass
    if flag == True:
        print('Да')
    else:
        print('Нет')
else:
    print('Нет')

