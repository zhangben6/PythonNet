from socket import *
import os,sys
from threading import Thread
from mysqlfunction import Mysqlpython
from hashlib import sha1

#配置服务器信息
HOST = '0.0.0.0'
PORT = 7000
ADDR = (HOST,PORT)
#数据库电子词典词汇
pass


#处理服务器请求的类
class DictionaryServer():
    def __init__(self,c):
        self.c = c
    def do_register(name,password1,password2):
        sqlh = Mysqlpython('db6')
        sele = "select username from user where username=%s"
        r = sqlh.All(sele,[name])
        if r:
            self.c.send("用户名已经存在".encode())
        else:
            if password1 == password2:
                #对密码加密,存入数据库
                s = sha1()
                s.updata(password1.encode('utf8')) #加密
                pwd = s.hexdigest()
                ins = 'insert into user values(%s,%s)'
                sqlh.zhixing(ins,[name,pwd])
                self.c.send("OK")
                break
            else:
                self.c.send("输入的密码不一致".encode())
                


#处理子进程的退出(僵尸进程)
def zombie():
    os.wait()

def main():
    #tcp流式套接字
    sockfd = socket()
    sockfd.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    sockfd.bind(ADDR)
    sockfd.listen(5)
    print("Listen the port 7000....")
    
    while True:
        try:
            c,addr = sockfd.accept()
        except KeyboardInterrupt:
            sys.exit("退出服务器")
        except Exception as e:
            print("服务器异常",e)
            break

        print("连接客户端",addr)



        pid = os.fork()
        if pid == 0:
            sockfd.close()
            server = DictionaryServer(c)
            #处理客户端的命令请求:
            while True:
                try:
                    data = c.recv(1024).decode()
                except Exception as e:
                    print("异常",e)
                datalist = data.split(' ')
                if datalist[0] == 'R':
                    server.do_register(name,data[1],data[2],data[3])

            os._exit(0)
        else:
            c.close()        
            t = Thread(target=zombie)
            t.setDaemon(True)
            t.start()
            continue


if __name__ == '__main__':
    main()