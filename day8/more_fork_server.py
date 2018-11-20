from socket import *
import os,sys


def client_handle(c):
    print('客户端地址',c.getpeername())
    while True:
        try:
            data = c.recv(1024)
            if not data:
                break
        except KeyboardInterrupt:
            break
        print(data.decode())
        c.send(b'Receive')
    c.close()

ADDR = ("0.0.0.0",8000)
s = socket(AF_INET,SOCK_STREAM)
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,True)
s.bind(ADDR)
s.listen(128)
#循环等待客户端连接
print("Listen to the port 8000....")
while True:
    try:
        c,addr = s.accept()
    except KeyboardInterrupt:
        sys.exit('退出服务器')
    except Exception as e:
        print(e)
        continue
    #创建新的进程处理客户端请求
    pid = os.fork()
    if pid == 0:
        p = os.fork()
        if p == 0:
            s.close()
            #处理具体的客户端请求
            client_handle(c)
            os._exit(0) #客户端处理完毕二级子进程退出
        else:
            os._exit(0) #一级子进程退出
    else:
        c.close()
        os.wait()
        continue
