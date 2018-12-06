# from socket import * 

# #创建套接字
# sockfd = socket()
# #发起连接
# sever_addr = ("127.0.0.1",8633)
# sockfd.connect(sever_addr)
# while True:
#     #发送消息
#     data = input("请输入:")
#     if not data:
#         break
#     sockfd.send(data.encode())
#     data = sockfd.recv(1024)
#     print("from server:",data.decode())
# sockfd.close()

from socket import *
ADDR = ("127.0.0.1",8000)
s = socket()
s.connect(ADDR)
while True:
    msg = input(">>>")
    if not msg:
        s.close()
        break
    s.send(msg.encode())
    data = s.recv(1024)
    print(data.decode())

