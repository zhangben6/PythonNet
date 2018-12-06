from socket import * 
import struct
ADDR = ("127.0.0.1",8888)
s = socket(AF_INET,SOCK_DGRAM)

# st = struct.Struct("i4sf")

while True:
    stu_id = input("id:")
    name = input("name:")
    n = len(name)
    height = input("height:")
    fmt = "i%dsf" % n
    #先发送格式,然后在发送数据
    s.sendto(fmt.encode(),ADDR)
    data = struct.pack(fmt,int(stu_id),name.encode(),float(height))
    s.sendto(data,ADDR)


