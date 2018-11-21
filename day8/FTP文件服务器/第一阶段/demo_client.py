from socket import * 
import os,sys

class FTPClient():
    def __init__(self,sockfd):
        self.sockfd = sockfd
    def do_list(self):
        self.sockfd.send(b'L')
        #等待回复:
        data = self.sockfd.recv(128).decode()
        if data == 'OK':
            while True:
                file = self.sockfd.recv(1024).decode()
                if file == '##':
                    break
                file = file.strip().split(' ')
                for line in file:
                    print(line)
        else:
            #无法操作
            print(data)

    def do_quit(self):
        self.sockfd.send(b'Q')
        self.sockfd.close()
        sys.exit("退出客户端")
def main():
    if len(sys.argv) < 3:
        sys.exit("格式有误")
    HOST = sys.argv[1]
    PORT = int(sys.argv[2])
    ADDR = (HOST,PORT)
    
    s = socket()
    try:
        s.connect(ADDR)
    except Exception as e:
        print("服务器异常",e)
        return 

    #创建封装套接字类的对象
    ftp = FTPClient(s)
    while True:
        #展示页面
        print("========张奔版GUI下载工具 V8.92========")
        print("****    list        ****")
        print("****    get file    ****")
        print("****    put file    ****")
        print("****    quit        ****")
        print("=====================================")

        cmd = input("请输入命令:")
        if cmd.strip() =='list':
            ftp.do_list()
        elif cmd.strip() == 'quit':
            ftp.do_quit()

main()