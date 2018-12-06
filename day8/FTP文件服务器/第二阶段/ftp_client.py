from socket import * 
import sys

#具体功能实现
class FtpClient(object):
    def __init__(self,sockfd):
        self.sockfd = sockfd

    def do_list(self):
        self.sockfd.send(b'L') #发送请求
        #等待回复:
        data = self.sockfd.recv(128).decode()
        if data == 'OK':
            while True:
                file = self.sockfd.recv(1024).decode()
                if file =='##':
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
    if len(sys.argv) > 3:
        sys.exit("输入格式不对")
    HOST = sys.argv[1]
    PORT = int(sys.argv[2])
    ADDR = (HOST,PORT)
    #创建流式套接字
    sockfd = socket()
    try:
        sockfd.connect(ADDR)
    except Exception as e:
        print("连接服务器失败",e)
        return 
    
    #创建类对象
    ftp = FtpClient(sockfd)

    while True:
        print("\n========张奔版GUI下载工具 V8.92========")
        print("****    list        ****")
        print("****    get file    ****")
        print("****    put file    ****")
        print("****    quit        ****")
        print("=====================================")

        cmd = input("请输入命令:")
        if cmd.strip() == "list":
            ftp.do_list()
        elif cmd.strip() == 'quit':
            ftp.do_quit()

        else:
            print("请输入正确命令")
main()



    