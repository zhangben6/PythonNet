#此示例示意进程对象的属性
from multiprocessing import Process
from time import sleep,ctime

def tm():
    for i in range(4):
        sleep(2)
        print(ctime())
# 此时上面只是个普通函数,只能通过下面的p并且传递参数才能变成进程函数
p = Process(target=tm,name='Tedu')
p.start()
#此时打印进程的属性
print('name:',p.name) #系统默认分配名字,也可以自定义修改
print('pid:',p.pid)
print("alive:",p.is_alive())
p.join()


#此示例演示daemon属性 默认为False,主进程退出,子进程不会结束
# 如果设置True,主进程退出,子进程也会结束
from multiprocessing import Process
from time import sleep,ctime

def tm():
    for i in range(4):
        sleep(2)
        print(ctime())
# 此时上面只是个普通函数,只能通过下面的p并且传递参数才能变成进程函数
p = Process(target=tm,name='Tedu')
p.daemon = True  #使子进程随主进程结束,前提是没有join()回收进程函数对象
p.start()
#此时打印进程的属性
print('name:',p.name) #系统默认分配名字,也可以自定义修改
print('pid:',p.pid)
print("alive:",p.is_alive())
# p.join()