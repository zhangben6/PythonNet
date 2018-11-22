#coding=utf-8
'''
HTTP SERVER 2.0
解析具体request
使用多线程并发处理
能返回简单数据
使用类封装
'''

from socket import *
from threading import Thread
import sys


#封装 httpserver2.0 类功能
class HTTPServer():
    def __init__(self,server_addr,static_dir):
        self.server_address = server_addr
        self.static_dir = static_dir
        self.ip = server_addr[0]
        self.port = server_addr[1]
        #创建套接字
        self.create_socket()

    def serv_forever(self):
        self.sockfd.listen(5)
        print("Listen to the port %d" % self.port)
        while True:
            try:
                connfd,addr = self.sockfd.accept()
            except KeyboardInterrupt:
                self.sockfd.close()
                sys.exit("退出服务器")
            except Exception as e:
                print("服务器异常:",e)
                continue
        #创建线程处理客户端请求
        clientThread = Thread(target=self.handle,args=(connfd,))
        clientThread.setDaemon(True)
        clientThread.start()
    
    #处理客户端请求
    def handle(self,connfd):
        #接收request
        request = connfd.recv(4096)
        print(request)


    def create_socket(self):
        self.sockfd = socket()
        self.sockfd.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
        self.sockfd.bind(self.server_address)

#提供服务器地址和静态文件路径
server_addr = ("0.0.0.0",8000)
static_dir = "../static"

#创建服务器对象
httpd = HTTPServer(server_addr,static_dir)
#调用函数启动服务
httpd.serv_forever()
