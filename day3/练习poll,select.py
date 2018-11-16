# from socket import * 
# from time import sleep,ctime

# #创建套接字
# sockfd = socket()
# sockfd.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
# sockfd.bind(("localhost",9000))
# sockfd.listen(5)

# #设置为非阻塞状态
# sockfd.setblocking(False)

# #循环接受消息
# while True:
#     print("waiting for connect....")
#     try:
#         connfd,addr = sockfd.accept()
#     except BlockingIOError:
#         sleep(1)
#         print(ctime())
#     else:
#         data = connfd.recv(1024).decode()
#         print(data)
#         connfd.send(b"Receive message")
#         if not data:
#             connfd.close()
#             break
# sockfd.close()


# 利用select模块中的select 方法进行io多路复用  
# from select import select 
# from socket import *
# # 创建套接字
# s = socket()
# s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
# s.bind(("localhost",8000))
# s.listen(5)
# print("waiting for ....")

# #添加关注列表
# rlist = [s]
# wlist = []
# xlist= []

# while True:
#     rs,ws,xs = select(rlist,wlist,xlist)

#     for r in rs:
#         if r is s:
#            c,addr = r.accept() 
#            print("Conncet from",addr)
#            rlist.append(c)
#         else:
#             data = r.recv(2048) 
#             if not data:
#                 rlist.remove(r)
#                 r.close()
#                 continue
#             print("收到:",data.decode())
#             print("from",addr)
#             wlist.append(r)

#     for w in ws:
#         w.send("receive msg".encode())
#         wlist.remove(w)
#     for x in xs:
#         pass

from select import *
from socket import *

#创建套接字
s = socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(("localhost",8000))
s.listen(5)
print("waiting for ...")

#创建poll对象
p = poll()

#建立查找词典(因为返回值必须创建这样的字段)
fdmap = {s.fileno():s}

#注册io
p.register(s,POLLIN|POLLERR)

while True:
    events = p.poll()
    for fd,event in events:
        if fd == s.fileno():
            c,addr = fdmap[fd].accept()
            print("Connect from",addr)

            # 添加新的关注io事件
            p.register(c,POLLIN|POLLHUP)
            #让字典与关注的io事件同步
            fdmap[c.fileno()] = c
        elif event & POLLIN:
            data = fdmap[fd].recv(1024)
            if not data:
                p.unregister(fd) #fd是文件描述符
                fdmap[fd].close()
                del fdmap[fd]
            else:
                print("Receive :",data.decode())
                fdmap[fd].send("THAKS!Receive this msg".encode())







