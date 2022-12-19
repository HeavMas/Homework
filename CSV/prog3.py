"""
Создайте список предметов формата Название, препод, ваша любовь к предмету(от 0 до 10).
Сохраните в CSV файл(название файла - ваша фамилия).
P.S не менее 4 столбцов.
"""
import csv

data = [['Name', 'Prepod', 'Love'],
        ['Python', 'Bobchenok', '∞'],
        ['Math', 'Boris Igorevich', '10'],
        ['histore', 'Somename', '8'],
        ['Somelesson', 'SomePrepod', '7']]

with open('new.csv', 'w',  encoding="UTF-8") as f:
    writer = csv.writer(f, delimiter=';')
    for row in data:
        writer.writerow(row)