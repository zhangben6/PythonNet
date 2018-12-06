#coding=utf-8
'''
chat room 
env:python3.5
socket and fork
'''
from socket import *
import os,sys
def do_login(s,user,name,addr):
    if (name in user) or name =="管理员":
        s.sendto("\n该用户已存在".encode(),addr)
        
    s.sendto(b'OK',addr)

    #通知其他人
    msg = "\n欢迎 %s 进入聊天室" % name
    for i in user:
        s.sendto(msg.encode(),user[i])
    #加入用此登录用户
    user[name] = addr

def do_chat(s,user,name,text):
    msg = "\n%s 说:%s" % (name,text)
    for i in user:
        if i != name:
            s.sendto(msg.encode(),user[i])
def do_quit(s,user,name):
    msg = "\n%s退出了聊天室" % name 
    for i in user:
        if i != name:
            s.sendto(msg.encode(),user[i])
        else:
            s.sendto(b'EXIT',user[name])
    del user[name]
def do_request(s):
    #测试
    # data,addr = s.recvfrom(1024)
    # print(data)

    #存储用户{'zhangsan':('127.0.0.1',8888)}
    user = {}
    while True:
        msg,addr = s.recvfrom(1024)
        msglist = msg.decode().split(" ")
        #区分请求类型
        if msglist[0] == 'L':
            do_login(s,user,msglist[1],addr)
        elif msglist[0] == 'C':
            #重新组织消息
            text = ' '.join(msglist[2:])
            do_chat(s,user,msglist[1],text)
        elif msglist[0] == 'Q':
            do_quit(s,user,msglist[1])

#创建网络连接
def main():
    ADDR = ("0.0.0.0",8888)
    #创建数据包套接字
    s = socket(AF_INET,SOCK_DGRAM)
    s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    s.bind(ADDR)

    #创建多进程
    pid = os.fork()
    if pid < 0:
        print("Create process faild")
        return 
    #子进程发送管理员消息
    elif pid == 0:
        # print("子进程任务")
        while True:
            msg = input("管理员消息:")
            msg = "C 管理员 %s" % msg
            s.sendto(msg.encode(),ADDR)
    #父进程处理客户端请求
    else:
        do_request(s)
        
if __name__ == "__main__":
    main()
