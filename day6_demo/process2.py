#带参数的进程函数
from multiprocessing import Process
from time import sleep

def worker(sec,name):
    for i in range(3):
        sleep(2)
        print("我是%s"%name)
        print("i an working")

# p = Process(target=worker,args=(2,"zhangben"))
# p = Process(target=worker,args=(2,),kwargs={"name":"zhangben"})
p = Process(target=worker,kwargs={"sec":2,"name":"zhangben"})


p.start()

p.join()