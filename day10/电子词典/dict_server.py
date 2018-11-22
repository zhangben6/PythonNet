from socket import * 
import pymysql
import os,sys
from threading import Thread

# if import multiprocessing and the chirld procss can't input

#定义全局变量
HOST = '0.0.0.0'
PORT = 8000
ADDR = (HOST,PORT)
DICT_TEXT = './dict.txt'

#处理僵尸进程函数
def zombie():
    os.wait()


def do_child(c,db):
    print(c.recv(1024))




#搭建网络
def main():

    #创建数据库连接对象
    db = pymysql.connect('localhost','root','123456','dict')

    #创建套接字
    s = socket()
    s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    s.bind(ADDR)
    s.listen(5)
    print("Listen to the port 8000...")

    while True:
        try:
            c,addr = s.accept()
            print("Connect from",addr)
        except KeyboardInterrupt:
            sys.exit("服务器退出")
        except Exception as e:
            print("服务器异常",e)
            continue

        #创建子进程
        pid = os.fork()
        if pid == 0:
            s.close()
            do_child(c,db) #子进程函数
            os._exit(0)

        else:
            c.close()
            t = Thread(target=zombie)
            t.setDaemon(True)
            t.start()
            continue
main()