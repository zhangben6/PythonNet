# from socket import *
# import sys
# #从命令行获取ip和port
# HOST = sys.argv[1]
# PORT = int(sys.argv[2])
# ADDR = (HOST,PORT)

# #创建udp套接字
# sockfd = socket(AF_INET,SOCK_DGRAM)

# #收发消息
# while True:
#     data = input("Msg:")
#     if not data:
#         break
#     sockfd.sendto(data.encode(),ADDR)

#     msg,addr=sockfd.recvfrom(1024)
#     print("Server msg:",msg.decode())
# sockfd.close()

from socket import *
sockfd= socket(AF_INET,SOCK_DGRAM)

while True:
    data = input("msg:.....")
    if not data:
        break
    sockfd.sendto(data.encode(),('127.0.0.1',8000))
    msg,addr = sockfd.recvfrom(3)
    print('收到服务端的信息:',msg.decode())
s.close()