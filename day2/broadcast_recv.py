from socket import * 

s = socket(AF_INET,SOCK_DGRAM)

#可以接受广播

s.setsockopt(SOL_SOCKET,SO_REUSEADDR,True)

s.bind(("0.0.0.0",6446))

while True:
    try:
        msg,addr = s.recvfrom(1024)
        print("广播为:",msg.decode())
    except KeyboardInterrupt:
        break
s.close()