import socket
host =''
port = 5000

clients = []

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((host,port))
s.setblocking(0)

quitting = False
print "Server Started."

while not quitting:
    try:
        data, addr = s.recvfrom(1024)

        if "Quit" in str(data):
            quitting = True
            for client in clients:
                s.sendto(data, client)

        if addr not in clients:
            clients.append(addr)

        print(str(addr) + ": :" + str(data))
        for client in clients:
            s.sendto(data, client)
    except:
        pass
s.close()
