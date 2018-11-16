# from socket import *

# #创建套接字
# sockfd = socket(AF_INET,SOCK_DGRAM)

# #绑定地址
# sockfd.bind(("0.0.0.0",8888))
# print("Waiting......")
# #收发消息
# while True:
#     data,addr = sockfd.recvfrom(5)
#     print("Receive from",addr,data.decode())

#     sockfd.sendto(b"Thanks for your message",addr)

# sockfd.close()


from socket import *
s = socket(AF_INET,SOCK_DGRAM)
s.bind(("0.0.0.0",8888))
print("wating for....")
while True:
    data,addr = s.recvfrom(1024)
    if not data:
        break
    print(data.decode())
    n = s.sendto(b"Thanks",addr)
    print("发送的字节数是%d" % n)

s.close()




