from socket import *
import sys,os

def send_msg(s,name,ADDR):
    while True:
        text = input("请输入消息:")
        msg = "C %s %s" % (name,text)
        s.sendto(msg.encode(),ADDR)

def recv_msg(s):
    while True:
        data,addr = s.recvfrom(2048)
        print(data.decode())

def main():
    if len(sys.argv) < 3:
        print("argv is error!")
        return
    HOST = sys.argv[1]
    PORT = int(sys.argv[2])
    ADDR = (HOST,PORT)
    s = socket(AF_INET,SOCK_DGRAM)

    # msg = input(">>>")
    # s.sendto(msg.encode(),ADDR)
    while True:
        name = input("请输入用户名:")
        msg = "L "+name
        
        #发送给服务器做比对
        s.sendto(msg.encode(),ADDR)
        #得到反馈
        data,addr = s.recvfrom(1024)
        if data.decode() == "OK":
            print("您已进入聊天室....")
            break
        else:
            print(data.decode())
    #创建父子进程,用于发送接受消息
    pid = os.fork()
    if pid < 0:
        sys.exit("创建进程失败")
    # 子进程负责发送消息
    elif pid == 0:
        send_msg(s,name,ADDR)
    #父进程负责接受消息
    else:
        recv_msg(s)
main()
