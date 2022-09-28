slov = {1: '1', 2: '2', 3: '3', 4: '4', 5: '5'}
slov[1], slov[5] = slov[5], slov[1]
slov['new_key'] = 'new_value'
del slov[2]
print(slov)
