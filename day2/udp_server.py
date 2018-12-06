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
s.bind(("0.0.0.0",8000))
print("waiting...")

while True:
    data,addr = s.recvfrom(5)
    print("Receive from",addr,data.decode())

    s.sendto(b'Thanks',addr)

s.close()



