"""
Из файла Task1.csv выведите данные в формате:
Имя - Звание
"""
import csv

keys = []
with open('file.csv', encoding="UTF-8") as f:
    reader = csv.reader(f, delimiter=';')
    for row in reader:
        keys.append(row[0])
        keys.append(row[3])
keys.pop(0)
keys.pop(0)
print(keys)