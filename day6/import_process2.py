from multiprocessing import Process
from time import sleep
import os

def th1():
    sleep(3)
    print("吃饭")
    print(os.getppid(),'--',os.getpid())

def th2():
    sleep(2)
    print("睡觉")
    print(os.getppid(),'--',os.getpid())

def th3():
    sleep(4)
    print("打豆豆")
    print(os.getppid(),'--',os.getpid())

things = [th1,th2,th3]
process = []
for th in things:
    p = Process(target=th)
    process.append(p) # 保留每次的进程对象
    p.start()
    
#这是父进程做的事情
while True:
    pass

回收过程
for i in process:
    i.join()

#如果非得让父进程搞点事情,代码就写在p.start()和p.join()之间

