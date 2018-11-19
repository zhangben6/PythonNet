# from multiprocessing import Process, Pool
# import os
# import time


# def run_proc(s):
#   n = 0
#   while n < 3:
#     print("subProcess %s run," % os.getpid(), "{0}".format(time.ctime()) ) #获取当前进程号和正在运行是的时间
#     time.sleep(s)  #等待（休眠）
#     n += 1

# if __name__ == "__main__":
#   p = Process(target=run_proc, args=(2,)) #申请子进程
#   p.start()   #运行进程
#   print("Parent process run. subProcess is ", p.pid)
# #   print("Parent process end,{0}".format(time.ctime()))
#   print("Parent process end",time.ctime())

from multiprocessing import Process,Pool
from time import sleep,ctime
def fun(s):
    sleep(s)
    msg = ctime()
    print(msg)
# def creatpro():
#     result = []
#     for _ in range(5):
#         p = Process(target=fun,args=(2,))    
#         result.append(p)
#         return result
def main():
    pool = Pool()
    for _ in range(8):
        pool.apply_async(func=fun,args=(2,))
        print(1)
    pool.close()
    pool.join()
main()
