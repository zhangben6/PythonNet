from multiprocessing import Pool
from time import sleep,ctime

#将事件放入进程池
def worker(msg):
    sleep(2)
    print(msg)
    return msg
#创建进程池对象
pool = Pool()

result = []
#向进程池添加事件
for i in range(10):
    msg = "hello %d" % i
    r = pool.apply_async(func=worker,args=(msg,)) #返回值是一个对象
    result.append(r)

    #将事件同步方式放入进程池
    # pool.apply(func=worker,args=(msg,))

#关闭进程池
pool.close()

#回收进程池
pool.join()
print("===================================")
print(result)
for i in result:
    print(i.get())
    #函数对象本身有一个方法get()方法,可以获取进程函数的返回值


