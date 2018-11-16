from socket import *
import struct
s = socket(AF_INET,SOCK_DGRAM)
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(("127.0.0.1",8888))

#接收数据格式
# st = struct.Struct("i20sf")
while True:

    data,addr = s.recvfrom(128)  #接受格式
    fmt = data.decode()

    data,addr = s.recvfrom(1024)  #接受数据
    data = struct.unpack(fmt,data) #按照格式转换 
    print(data)
s.close()


# from soketet import * 
# import struct
# s = socket(AF_INET,SOCK_DGRAM)
# s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
# s.bind(("127.0.0.1",8888))
# while True:
#     data,addr =s.recvfrom(128)
#     fmt = data.encode()
#     data,addr = s.recvfrom(1024)
#     data = struct.unpack(fmt,data)
#     print(data)
# s.close()
