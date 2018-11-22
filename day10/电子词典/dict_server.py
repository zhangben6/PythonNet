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
    # print(c.recv(1024))
    while True:
        data = c.recv(1024).decode()
        print(c.getpeername(),':',data)

        if not data[0] or data[0] == 'Q':
            c.close() 
            break

        elif data[0] == 'R':
            do_register(c,db,data)

        elif data[0] == 'L':
            do_login(c,db,data)


def do_login(c,db,data):
    l = data.split(" ")
    # 取出数据
    name = l[1]
    passwd = l[2]

    #创建油表对象
    cursor = db.cursor()
    sql = "select * from user where name='%s' and passwd='%s'" % (name,passwd)

    #查找用户
    cursor.execute(sql)
    r = cursor.fetchone()
    if r == None:
        c.send(b'FALL')
    else:
        c.send(b'OK')


def do_register(c,db,data):
    l = data.split(' ')
    name = l[1]
    passwd = l[2]
    cursor = db.cursor()
    sql = "select * from user where name='%s'" % name
    cursor.execute(sql)
    r = cursor.fetchone()
    #r部位NONE表示该用户已存在
    if r != None:
        c.send(b'EXIST')
        return
    #插入用户
    sql = "insert into user (name,passwd) values('%s','%s')" % (name,passwd)
    
    try:
        cursor.execute(sql)
        db.commit()
        c.send(b'OK')
    except:
        db.rollback()
        c.send(b'FALL')
    

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



if __name__ == '__main__':
    main()