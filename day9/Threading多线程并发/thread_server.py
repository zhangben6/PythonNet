from socket import * 
from threading import Thread
import sys,os

#定义全局变量
HOST = '0.0.0.0'
PORT = 8000
ADDR = (HOST,PORT)

def handler(c):
    print("Connect from",c.getpeername())
    while True:
        data = c.recv(1024)
        if not data:
            break
        print(data.decode())
        c.send(b'Receive')
    c.close()

#创建套接字
s = socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(ADDR)
s.listen(5)
print("Listen to the port 8888....")

#接受客户端请求
while True:
    try:
        c,addr = s.accept()
    except KeyboardInterrupt:
        s.close()
        sys.exit("服务器退出")
    except Exception as e:
        print("服务器异常:",e)
    
    #创建线程:
    t = Thread(target = handler,args=(c,))
    t.setDaemon(True)
    t.start()
    

