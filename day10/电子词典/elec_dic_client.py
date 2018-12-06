from socket import *
import sys,os

#客户端的功能类
class DictionaryClient():
    def __init__(self,sockfd):
        self.sockfd = sockfd
    def do_register(self):
        name = input("请输入注册用户名字:") #########
        password1 = input("请输入密码:")
        password2 = input("请再次胡输入密码:") ###判断密码是否一致
        self.sockfd.send(('R '+ name + ' ' + password1 + ' ' + password2).encode())
        #等待回复
        data = self.sockfd.recv(1024).decode()
        if data == 'OK':
            print("恭喜你注册成功")
        else:
            print(data)

    def do_ligin(self):
        
def main():
    if len(sys.argv) < 3:
        sys.exit("输入格式不对")
    HOST = sys.argv[1]
    PORT = int(sys.argv[2])
    ADDR = (HOST,PORT)
    
    sockfd = socket()  
    sockfd.connect(ADDR)    ######

    client = DictionaryClient(sockfd)
    
    print("\n========张奔版GUI工具 V8.92========")
    print("****      注册(register)        ****")
    print("****      登录(login)        ****")
    print("****      退出(quit)        ****")
    print("=====================================")
    while True:
        demand = input("\n请输入格式:")
        if demand == 'register':
            client.do_register() 
        elif demand == 'login':
            client.do_login()
    

    


if __name__ == '__main__':
    main()