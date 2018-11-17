# 此示例示意进程池的操作步骤
#并且收集进程函数的返回值,进行打印
from multiprocessing import Pool
from time import sleep

def tm(msg):
    sleep(2)
    print(msg)
    return msg

#创建进程池对象
pool = Pool()

#存放进程函数对象
result = []
#想进程池添加对象
for i in range(10):
    msg = "hello %d" % i
    r = pool.apply_async(func=tm,args=(msg,))
    result.append(r)

# 关闭进程池
pool.close()

#回收进程池
pool.join()
print('======================')
for i in result:
    print(i.get())




#此示例示意pool_map的用法,相当于用高阶函数map的方法直接创建了多个进程扔进进程池
from multiprocessing import Pool
from time import sleep

def fun(n):
    time.sleep(1)
    return n * n

pool = Pool

r = pool.map(fun,range(6))
pool.close()
pool.join()
print(r)
