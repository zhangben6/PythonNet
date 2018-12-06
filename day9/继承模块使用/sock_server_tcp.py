
'''运用类创建多进程的tcp传输方式'''
from socketserver import * 

#创建服务器类
class Server(ForkingMixIn,TCPServer):
    pass

#处理请求类
class Handler(StreamRequestHandler):
    #重写handler父类方法:
    def handle(self):
        print("Connect from:",self.client_address)
        while True:
            #self.request ==> accept 返回的连接套接字
            data = self.request.recv(1024)
            if not data:
                break
            print(data.decode())
            self.request.send(b"Receive")


server = Server(('0.0.0.0',8000),Handler) #传入地址和处理客户端请求类

server.serve_forever() #通过服务器对象调用该函数启动服务

