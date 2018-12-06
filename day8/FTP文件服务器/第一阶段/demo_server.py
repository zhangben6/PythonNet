from socket import *
import sys,os
from threading import Thread
import time
HOST = '0.0.0.0'
PORT = 8000
ADDR = (HOST,PORT)
FILE_DIR = '/home/tarena/selfpbase/'

class FtpServer():
    def __init__(self,c):
        self.c = c 
    def do_list(self):
        #首先获取文件列表
        file_list = os.listdir(FILE_DIR)
        if not list:
            self.c.send("文件夹为空").encode()
        self.c.send(b'OK')
        time.sleep(0.1)
        for file in file_list:
            if file[0] != '.' and os.path.isfile(FILE_DIR+file):
                self.c.send((file+" ").encode())
        time.sleep(0.1)
        self.c.send(b'##')


def zombie():
    os.wait()


def main():
    s = socket()
    s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    s.bind(ADDR)
    s.listen(5)
    print('Listen to the port 8000...')

    while True:
        try:
            c,addr = s.accept()
        except KeyboardInterrupt:
            sys.exit("退出服务器")
        except Exception as e:
            print("服务器异常",e)
            continue 
        print("连接用户:",addr)

        #多进程并发操作,子进程负责与客户端进行通信
        pid = os.fork()
        if pid == 0:
            s.close()
            ftp = FtpServer(c)
            # print("这里是我接收到的信息")
            while True:
                data = c.recv(1024).decode()
                if not data  and data[0] == 'Q':
                    #记着要关闭c
                    c.close()
                    sys.exit("服务端退出") 

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