"""
Сохраните данные из списка в json файл(Имя файла - ваша фамилия и номер задания) с отступом 4, формата:
name: ***
age: ***
countries: ***
"""
import json

task = ["oleg", 24, ["Belarus","Russia"]]
data = {'name': task[0],
        'age': task[1],
        'countries': task[2]
}
with open('Philippov2.json', 'w')as write_file:
    json.dump(data, write_file, indent=4)