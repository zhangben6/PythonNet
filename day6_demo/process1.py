#使用multiprocessing创建多个进程
#父进程只负责创建进程和回收进程,子进程用来做事情
#父进程做的事情应该写在start和join之间
from multiprocessing import Process
from time import sleep,ctime
import os

def th1():
    sleep(1)
    print("吃饭")
    print(os.getppid(),'--',os.getpid())

def th2():
    sleep(2)
    print("睡觉")
    print(os.getppid(),'--',os.getpid())

def th3():
    sleep(3)
    print("打豆豆")
    print(os.getppid(),'--',os.getpid())
    
things = [th1,th2,th3]
process = [] #保留每次进程的对象
for th in things:
    p = Process(target=th)
    process.append(p)   #易错点:应该添加进程对象,不能添加函数
    p.start()

#回收过程
for i in process:
    i.join()