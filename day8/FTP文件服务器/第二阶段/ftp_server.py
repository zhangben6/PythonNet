'''
ftp文件服务器
for server训练
'''

from socket import *
import os,sys
from threading import Thread
import time


#全局变量
HOST = '0.0.0.0'
PORT = 8700
ADDR = (HOST,PORT)
FILE_DIR = '/home/tarena/selfpbase/'

#处理僵尸进程
def zombie():
    # while True:
    #     try:
    #         # os.waitpid(-1,os.WNOHANG)
    #         os.wait()
    #     except Exception:
    #         print("僵尸来了没?")
    os.wait()
 #单独创建线程处理僵尸进程,线程同属于父进程,处理子进程的僵尸进程
# t = Thread(target=zombie)
# t.setDaemon(True)
# t.start()

#具体功能实现
class FtpServer():
    def __init__(self,c):
        self.c = c
    def do_list(self):
        #首先获取文件列表
        file_list = os.listdir(FILE_DIR)
        if not file_list:
            self.c.send("文件库为空".encode())
        else:
            self.c.send(b'OK')
            time.sleep(0.1)
        for file in file_list:
            if file[0] != '.' and os.path.isfile(FILE_DIR + file): #后者为普通文件
                self.c.send(file.encode())
                time.sleep(0.1)
        self.c.send(b'##')



#创建网络网络连接
def main():
    sockfd = socket(AF_INET,SOCK_STREAM)
    sockfd.setsockopt(SOL_SOCKET,SO_REUSEADDR,True)
    sockfd.bind(ADDR)
    sockfd.listen(5)
    print("Lister to the port 8080...")
   
    while True:
        try:
            c,addr = sockfd.accept()
        except KeyboardInterrupt:
            sockfd.close()
            sys.exit("服务器退出")
        except Exception as e:
            print("服务器异常",e)
            continue 
        print("连接用户:",addr)
    
        #创建子进程
        pid = os.fork()
        if pid == 0:
            sockfd.close()
            ftp = FtpServer(c)
            # print("处理客户端请求",os.getpid())
            # data = c.recv(1024)
            # print(data.decode())
            while True:
                data = c.recv(1024).decode()
                if not data or data[0] == 'Q':
                    c.close()
                    sys.exit("客户端退出")
                elif data[0] == 'L':
                    ftp.do_list()
            os._exit(0)        
        else:
            c.close()
            #单独创建线程处理僵尸进程,线程同属于父进程,处理子进程的僵尸进程
            t = Thread(target=zombie)
            t.setDaemon(True)
            t.start()
            continue
main()