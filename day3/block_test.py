from socket import * 
from time import sleep,ctime

#tcp套接字
sockfd = socket()
sockfd.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
sockfd.bind(("0.0.0.0",9000))
sockfd.listen(3)

#设置为非阻塞状态
sockfd.setblocking(False)

#设置超时时间
# sockfd.settimeout(5)

while True:
    print("waiting for connect.....")
    try:
        connfd,addr = sockfd.accept()
        #设置监听套套接字为非阻塞状态
        # connfd.setblocking(False)
    except BlockingIOError:
        sleep(1)
        print(ctime()+"\r")
        continue
    except timeout:
        print("超时等待5秒")
        continue
    else:
        data = connfd.recv(1024)
        print(data.decode())
        connfd.send(b"Receive message")
        if not data:
            break
sockfd.close()

