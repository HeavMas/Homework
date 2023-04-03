import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('localhost', 55000))
while True:
    massange = input()
    sock.send(bytes(massange, encoding='UTF-8'))
    data = sock.recv(1024)
    print(str(data))
sock.close()