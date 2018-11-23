from select import select
from socket import *

#创建套接字作为关注IO
s = socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(("localhost",8000))
s.listen(5)
print("waiting ...")

#添加到关注列表里面
rlist = [s]
wlist = []
xlist = []

while True:
    #循环监控IO事件的发生
    rs,ws,xs = select(rlist,wlist,xlist)

    #处理发生的IO事件
    for r in rs: 
        #遍历到s,说明s就绪,有客户端连接
        if r is s:
            c,addr = r.accept()
            print("Connect from",addr)
            rlist.append(c)
        else:
            data = r.recv(1024)
            if not data:
                rlist.remove(r) #客户端退出,移除关注
                r.close()
                continue
            print("收到:",data.decode())
            print("from",addr)
            # r.send(b"Receive msg")
            wlist.append(r)  #添加这个r下一次循环优先循环这个r,相当于多添加一次循环

    for w in ws:
        w.send(b"Receive")
        
        wlist.remove(w)
    for x in xs:
        pass



