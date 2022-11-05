#3. write a function which will be able to print an ip address of your system

import socket

def test2():
    ip = socket.gethostbyname(socket.gethostname())
    return ip

print(test2())