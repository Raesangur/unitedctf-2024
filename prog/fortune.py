import socket

def netcat(hostname, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((hostname, port))

    return s

def read(s):
    print("--------")
    data = s.recv(2048)
    data = repr(data)
    print("recieved : " + data)
    lines = data.split("\\n")

    for line in lines:
        print(line)

    return lines

s = netcat('c.unitedctf.ca', 10010)
read(s)

s.sendall("0".encode())
read(s)

s.shutdown(socket.SHUT_WR)
s.close()
