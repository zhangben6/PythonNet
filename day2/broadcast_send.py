from socket import *
from time import sleep

#设置广播地址
dest=(("192.168.43.255",6446))
s = socket(AF_INET,SOCK_DGRAM)

#设置可以发送广播
s.setsockopt(SOL_SOCKET,SO_BROADCAST,1)
while True:

    sleep(2)
    s.sendto("想带你去看晴空万里".encode(),dest)
s.close()