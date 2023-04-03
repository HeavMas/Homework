"""
Реализовать чат,
который позволит обмениваться сообщениями только между клиентом и сервером.
Клиент должен получать сообщения сервера в том числе. Сигналом окончания связи служит слово "Пока".
"""
import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('', 55000))
sock.listen(10)
conn, addr = sock.accept()
while True:
    print('connected:', addr)
    data = conn.recv(1024)
    print(str(data))
    conn.send(data.upper())
    if data.decode() == 'Пока':
        break
conn.close()
