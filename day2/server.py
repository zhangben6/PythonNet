# from socket import *

# s = socket()
# s.bind(("0.0.0.0",9800))
# s.listen(5)
# print("Waiting for ....")
# c,addr = s.accept()
# print("Connect for:",addr)
# f  = open("recv4.jpg","wb")
# while True:
#     data = c.recv(1024)
#     if not data:
#         break
#     f.write(data)
#     # c.send("我成功接受并打印THANKS".encode())
# c.close()
# f.close()
# s.close()

#需求:接受客户端发来的文件:
from socket import *
s = socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(("0.0.0.0",8000))
s.listen(5)
print("waiting...")
c,addr = s.accept()
try:
    f = open('recv.jpg','wb')
except:
    print("打开文件失败")
while True:
    data = c.recv(1024)
    if not data:
        break
    f.write(data)
    # c.send(b'OK')
f.close()
c.close()
s.close()
