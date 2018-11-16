from socket import *

s = socket()
s.bind(("0.0.0.0",9800))
s.listen(5)
print("Waiting for ....")
c,addr = s.accept()
print("Connect for:",addr)
f  = open("recv4.jpg","wb")
while True:
    data = c.recv(1024)
    if not data:
        break
    f.write(data)
    # c.send("我成功接受并打印THANKS".encode())
c.close()
f.close()
s.close()
