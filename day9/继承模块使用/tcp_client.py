from socket import * 

#创建套接字
sockfd = socket()
#发起连接
ADDR = ("127.0.0.1",8000)
sockfd.connect(ADDR)
while True:
    data = input("请输入:")
    if not data:
        break
    sockfd.send(data.encode())
    data = sockfd.recv(1024)
    print("from server:",data.decode())
sockfd.close()

