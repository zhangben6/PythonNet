import threading 
from time import sleep
import os 
a = 1
def music():
    for i in range(3):
        global a 
        print('a=',a)
        a = 1000
        sleep(2)
        print("播放沙漠骆驼",os.getpid())

#创建线程对象
t= threading.Thread(target=music)
t.start()
# for i in range(3):
#     sleep(3)
#     print("播放Action",os.getpid())
t.join()
print("main a:",a)
#因为线程是在进程内开辟的空间,并且线程之间可以共享资源,所以一个线程把全局变量中的
# 变量修改后,也会影响其他线程使用这个变量的值