"""
Разработайте приложение, которое будет запрашивать у пользователя название файла,
а затем отправлять содержимое этого файла серверу. Сервер будет выводить сообщение, подсчитывать количество слов и возвращать ответ.
Протестируйте на test.txt
"""
import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('', 55000))
sock.listen(10)
conn, addr = sock.accept()
while True:
    print('connected:', addr)
    data = conn.recv(1024).decode()
    print(data, 'Кол-во слов - ' + str(len(data.split(' '))))
    if data == 'Пока':
        break
conn.close()