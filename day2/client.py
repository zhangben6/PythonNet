# from socket import * 

# s = socket()

# sever_addr = ("127.0.0.1",9800)
# s.connect(sever_addr)
# filename="send.jpg"
# with open(filename,"rb") as f:
#     while True:
#         s1 = f.read(1024)
#         if not s1:
#             break
#         s.send(s1)

# # recv = s.recv(1024)
# # print("from server:",recv.decode())
# s.close()

from socket import *
s = socket()
s.connect(("127.0.0.1",8000))
f = open('send.jpg','rb')
while True:
    s1 = f.read(1024)
    if not s1:
        break
    s.send(s1)
    # recv = s.recv(1024)
    # print("from server msg:",recv.decode())

f.close()
s.close()