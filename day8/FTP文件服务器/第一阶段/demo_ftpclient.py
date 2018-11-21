from socket import *
import sys

#具体功能实现的类
class FtpClient():
    def __init__(self,s):
        self.sockfd = s
    
    def do_list(self):
        self.sockfd.send(b'L')
        data = self.sockfd.recv(128).decode()
        if data == 'OK':
            while True:
                file = self.sockfd.recv(1024).decode()
                if file == '##':
                    break
                print(file)
        else:
            #无法操作
            print(data)

    def do_quit(self):
        self.sockfd.send(b'Q')
        self.sockfd.close()
        sys.exit("谢谢使用")


def main():
    if len(sys.argv) < 3:
        sys.exit("输入格式不对")
    HOST = sys.argv[1]
    PORT = int(sys.argv[2])
    ADDR = (HOST,PORT)

    #创建流式套接字
    s = socket()
    try:
        s.connect(ADDR)
    except Exception as e:
        print("服务器异常",e)
        return 
    ftp = FtpClient(s)

    while True:
        print("========张奔版GUI下载工具 V8.92========")
        print("****    list        ****")
        print("****    get file    ****")
        print("****    put file    ****")
        print("****    quit        ****")
        print("=====================================")
        try:
            cmd = input("请输入命令:")
        except KeyboardInterrupt:
            sys.exit("客户端退出")
        if cmd == 'list':
           ftp.do_list()
        elif cmd == 'quit':
            ftp.do_quit()
            
main()