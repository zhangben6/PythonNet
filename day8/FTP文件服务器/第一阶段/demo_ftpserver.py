from socket import * 
import os,sys
from threading import Thread
import time
#全局变量
HOST = '0.0.0.0'
PORT = 8000
ADDR = (HOST,PORT)
FILE_DIR = "/home/tarena/selfpbase/"

def zombie():
    os.wait()


#具体功能封装的类
class FtpServer():
    def __init__(self,c):
        self.c = c
    def do_list(self):
        #获取文件列表
        file_list = os.listdir(FILE_DIR)        
        if not file_list:
            self.c.send("文件库为空".encode())
        else:
            self.c.send(b'OK')
            #避免粘包
            time.sleep(0.1)
        for file in file_list:
            if file[0] != '.' and os.path.isfile(FILE_DIR+file):
                self.c.send(file.encode())
                time.sleep(0.1)
        self.c.send(b'##')


def main():
    s = socket()
    s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    s.bind(ADDR)
    s.listen(5)
    print("Listen to the port 8000...")

    #循环接受客户端消息
    while True:
        try:
            c,addr = s.accept()
        except KeyboardInterrupt:
            s.close()
            sys.exit('服务器退出')
        except Exception as e:
            print("服务器异常",e)
            continue
        print("连接用户:",addr)

        #创建进程
        pid = os.fork()
        if pid == 0:
            s.close()
            ftp = FtpServer(c)
            while True:
                data = c.recv(1024).decode()
                if not data or data[0] == 'Q':
                    print(addr,"客户端退出")
                    c.close()
                    os._exit(0)
                elif data[0] == 'L':
                    ftp.do_list()

            #子进程退出
            os._exit(0)
        else:
            c.close()
            t = Thread(target=zombie)
            t.setDaemon(True)
            t.start()
            continue

main()