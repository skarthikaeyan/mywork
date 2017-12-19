import socket
import threading
import time
import sys
global re

t = threading.Lock()
def receving(name, sock):

    re = False
    while not re:
        try:


            t.acquire()
            while True:

                data, addr = sock.recvfrom(1024)
                print str(data)

        except:
            pass
        finally:
            t.release()

host =''
port = 0
po=5000

server = ((host,po))

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((host, port))
s.setblocking(0)

rT = threading.Thread(target=receving, args=("RecvThread",s))
rT.start()

usrname = raw_input("Name: ")
message = raw_input(usrname + "-> ")
while message != 'q':
    if message != '':
        s.sendto(usrname + ": " + message, server)
    t.acquire()
    message = raw_input(usrname + "-> ")
    time.sleep(0.2)
    t.release()

rT.join()
s.close()
