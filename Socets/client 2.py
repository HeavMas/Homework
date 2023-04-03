import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('localhost', 55000))
while True:
    file_name = input()
    with open(file_name, 'r',encoding="UTF-8") as f:
        massange = f.read()
    sock.send(massange.encode())
    data = sock.recv(1024)
sock.close()