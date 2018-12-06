from socket import *
from select import *

#创建套接字作为关注IO
s = socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(("localhost",8000))
s.listen(5)

# 创建poll对象
p = poll()

#建立查找字典(因为返回值必须创建这样的字段)
fdmap = {s.fileno():s}

#注册和关注io
p.register(s,POLLERR|POLLIN)

#监控主循环
while True:
    events = p.poll()  #等待io发生
    for fd,event in events:
        if fd == s.fileno():                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               
            c,addr = fdmap[fd].accept()
            print("Connect from",addr)
            # 添加新的关注io事件(让字典与关注的io事件同步)
            p.register(c,POLLIN|POLLERR)
            fdmap[c.fileno()] = c
        elif event & POLLIN:
            data = fdmap[fd].recv(1024)
            if not data:
                p.unregister(fd)
                fdmap[fd].close()
                del fdmap[fd]
            else:
                print("Receive:",data.decode())
                fdmap[fd].send(b"Receive")


    

