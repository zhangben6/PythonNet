from socket import *
import sys

#创建网络连接
def main():
    if len(sys.argv) < 3:
        print('argv is error')
        return
    HOST = sys.argv[1]
    PORT = int(sys.argv[2])
    ADDR = (HOST,PORT)
    s = socket()
    try:
        s.connect(ADDR)
    except Exception as e:
        print("服务器异常",e)
        return 
    
    print("\n========张奔版GUI工具 V8.92========")
    print("****      注册(register)        ****")
    print("****      登录(login)        ****")
    print("****      退出(quit)        ****")
    print("=====================================")
    
    cmd = input("请输入:")
    s.send(cmd.encode())

main()