import gevent 
from gevent import monkey 
monkey.patch_socket() #执行脚本修改阻塞行为
from socket import * 

#创建套接字
def server():
    s = socket()
    s.bind(("0.0.0.0",8000))
    s.listen(10)
    while True:
        c,addr = s.accept()
        print("Connect from",addr)
        # handle(c)
        gevent.spawn(handle,c)


def handle(c):
    while True:
        data = c.recv(1024)
        if not data:
            break
        print(data.decode())
        c.send(b'Receive')
    c.close()



server()

