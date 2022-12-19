"""
Из данных в файле Task1.csv сделайте словарь вида:
(Имя,фамилия):{оценка: звание}
"""

import csv

kyes = []
val = []
dik = {}
with open('file.csv', encoding="UTF-8") as f:
    reader = csv.reader(f, delimiter=';')
    for row in reader:
        kyes.append(row[0])
        kyes.append(row[1])
        val.append(row[2])
        val.append(row[3])
for i in range(2):
    kyes.pop(0)
    val.pop(0)
for i in range(len(kyes) - 1):
    dik[kyes[i], kyes[i + 1]] = val[i], val[i + 1]
print(dik)
