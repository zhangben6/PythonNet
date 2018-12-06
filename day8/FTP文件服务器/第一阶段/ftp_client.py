from socket import * 
import sys

#具体功能实现
class FtpClient(object):
    pass


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
    
    while True:
        print("========张奔版GUI下载工具 V8.92========")
        print("****    list        ****")
        print("****    get file    ****")
        print("****    put file    ****")
        print("****    quit        ****")
        print("=====================================")

        cmd = input("请输入命令")
       
main()



    