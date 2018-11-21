from socket import * 
from multiprocessing import Process
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
            print(c.getpeername(),"已退出")
            break
        print(data.decode())
        c.send(b"Receive")
    c.close()
    os._exit(0)
 

#创建套接字
s = socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(ADDR)
s.listen(5)
print("Listen to the port 8000....")

#接受客户端请求
while True:
    try:
        c,addr = s.accept()
    except KeyboardInterrupt:
        s.close()
        sys.exit("服务器退出")
    except Exception as e:
        print("服务器异常:",e)
    
    #创建多进程函数处理对象
    p = Process(target=handler,args=(c,))
    p.daemon = True # 主进程退出必须保证处理客户端函数对象的子进程退出
    p.start()
