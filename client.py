import sys
import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  #creating socket sock
host = socket.gethostname() #getting local ip
print(host)
port = 65535
try:
    sock.connect((host,port))
    print("connected")
except socket.error as e:
    print("Try again",e)
    sys.exit()
print("Type your Message")
while True:
    a=raw_input("").encode()#encoding to byte
    if not a:
        break
    else:
        sock.send(a) #sending the input as input is not from file b' is not used
        print("Your message: ", sock.recv(1024))
sock.close() #closing the socket
print("disconnected")
sys.exit()
