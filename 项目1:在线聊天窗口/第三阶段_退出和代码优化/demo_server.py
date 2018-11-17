# coding=utf-8
from socket import *
import os

def do_quit(s,user,name):
    msg = '\n%s退出了聊天室' % name
    for i in user:
        if i != name:
            s.sendto(msg.encode(),user[i])
        else:
            s.sendto(b'EXIT',user[name])
    del user[name]
def do_chat(s,user,name,text):
    #此格式是显示到别人的终端上
    msg = "\n%s 说:%s" % (name,text)
    for i in user:
        if i != name:
            s.sendto(msg.encode(),user[i])

def do_login(s,user,name,addr):
    #起名字不能用管理员名字
    if (name in user) or name == "管理员":
        s.sendto("该用户已经存在".encode(),addr)
        return
    s.sendto(b'OK',addr)

    #通知其他人
    msg = "\n欢迎%s进入聊天室" % name
    for i in user:
        s.sendto(msg.encode(),user[i])
    #加入登录用户
    user[name] = addr

def do_request(s):
    #　测试
    # data,addr = s.recvfrom(1024)
    # print("收到:",data.decode())
    user = {}
    while True:
        msg,addr = s.recvfrom(1024)
        msglist = msg.decode().split(" ")
        # 区分请求类型
        if msglist[0] == "L":
            #登录函数两个功能:1.给客户端反馈 2.把客户端登录信息收集到字典中
            do_login(s,user,msglist[1],addr)
        elif msglist[0] == 'C':
            #重新组织消息,避免用户输入消息出现空格或者多空格导致消息转发不完全
            text = ' '.join(msglist[2:])
            do_chat(s,user,msglist[1],text) 
        elif msglist[0] == 'Q':
            do_quit(s,user,msglist[1])

def main():
    ADDR = ("0.0.0.0",8888)
    #创建udp套接字
    s = socket(AF_INET,SOCK_DGRAM)
    #设置端口重用
    s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    #绑定地址
    s.bind(ADDR)

    #创建多线程
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
    
main()