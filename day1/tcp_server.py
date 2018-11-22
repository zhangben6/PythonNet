# from socket import *

# # 创建套接字
# sockfd = socket(AF_INET,SOCK_STREAM)
# sockfd.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
# #绑定地址
# sockfd.bind(("0.0.0.0",8633))

# #设置监听
# sockfd.listen(5)
# while True:
#     print("Watting for connect...")
#     #处理客户端连接
#     try:
#         connfd,addr = sockfd.accept()
#         print("Connect for:",addr)
#     except KeyboardInterrupt:
#         break
#     while True:
#         #收发消息
#         data = connfd.recv(1024)
#         if not data:
#             break
#         print("Receive:",data.decode())

        
#         n = connfd.send("helo Kitty".encode())
#         print("Send %d bytes" % n)
       
#     #关闭套接字
#     connfd.close()
# sockfd.close()


from socket import *

#创建套接字
sockfd = socket(AF_INET,SOCK_STREAM)
sockfd.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
sockfd.bind(("localhost",8000))
sockfd.listen(5)
print("waiting for....")

c,addr = sockfd.accept()

#循环打印消息:
while True:
    data = c.recv(1024)
    if not data:
        c.close()
        break
    print(data.decode())
    n = c.send("Receive msg".encode())
    print("发送了%d个字节" % n)
c.close()
sockfd.close()



