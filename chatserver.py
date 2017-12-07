import sys
import time
import socket
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
host = socket.gethostname()
port = 1024
try:
    s.bind((host,port))
    s.setblocking(0)
except socket.error as e:
    print("Connection Error: "+e)
    sys.exit()
print("Connected... \n type 'logout' to exit")
cli=[]
while True:
    inp,addr=s.recv(1024)
    if 'logout'in str(inp):
        break
    if addr not in cli:
        cli.append(addr)
    print(str(addr)+": "+str(inp))
    for clients in cli:
        s.send(inp,clients)
s.close()
