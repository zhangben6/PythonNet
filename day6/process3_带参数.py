from multiprocessing import Process
from time import sleep

#带参数的进程函数
def worker(sec,name):
    for i in range(3):
        sleep(sec)
        print("I'm %s"%name)
        print("I'm working...")

#两种进程函数传参形式
# p = Process(target=worker,args=(2,"Zack"))
# p = Process(target=worker,kwargs={"sec":2,"name":'zack'})
p = Process(target=worker,args=(2,),kwargs={'name':'zack'})

p.start()
print("我是父进程.......")
p.join()
