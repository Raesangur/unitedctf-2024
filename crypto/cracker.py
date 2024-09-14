#Spencer Smith
 
import time
import hashlib
import socket
import sys

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("c.unitedctf.ca", 10002))
s.sendall("fr".encode())
s.shutdown(socket.SHUT_WR)

while 1:
    data = s.recv(1024)
    if len(data) == 0:
        break
    print("Received: ", repr(data))
s.close()
exit()
 
#set md5 encrypted password from command line we are looking for
solution = str(sys.argv[1])
guess=" "
sol = "no solution found"
 
#open dictionary file
filename = open(str(sys.argv[2]),'r')
 
#for each entry, generate md5 encryption and check ...
# ... against desired solution
 
for line in filename:
  m = hashlib.md5()
  #cut off '\n' character
  m.update(line[:-1])
  guess = m.hexdigest()
  if guess == solution:
    sol = line
    break
 
#close dictionary file
filename.close()
