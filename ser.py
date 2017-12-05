import socket
import sys
sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host=socket.gethostname()
port=65535
try:
    sock.bind((host,port))
    print("Connected to",host)
except socket.error as e:
    print("error",e)
    sys.exit()
sock.listen(2)
print("listening")
com, addr = sock.accept()
print(addr)
a = com.recv(1024)
print(''.join(a) )
com.send(a)
com.close()
