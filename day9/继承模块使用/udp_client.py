from socket import *
import sys
#从命令行获取ip和port
HOST = sys.argv[1]
PORT = int(sys.argv[2])
ADDR = (HOST,PORT)

#创建udp套接字
sockfd = socket(AF_INET,SOCK_DGRAM)

#收发消息
while True:
    data = input("Msg:")
    if not data:
        break
    sockfd.sendto(data.encode(),ADDR)

    msg,addr=sockfd.recvfrom(1024)
    print("Server msg:",msg.decode())
sockfd.close()

# from socket import *
# import sys
# HOST = sys.argv[1]
# PORT = int(sys.argv[2])
# ADDR = (HOST,PORT)
# s = socket(AF_INET,SOCK_DGRAM)
# while True:
#     data = input("MSG:")
#     if not data:
#         break
#     s.sendto(data.encode(),ADDR)
#     msg,addr = s.recvfrom(1024)
#     print("SERVER mSG:",msg.decode())
# s.close()

