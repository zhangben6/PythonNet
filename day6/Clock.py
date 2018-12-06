from multiprocessing import Process
from time import ctime,sleep

#进程类
class ClockProcess(Process):
    def __init__(self,value):#以字典的方式传参
        self.value = value
        super(ClockProcess,self).__init__() #加载父类init方法

    def time1(self):
        print("开始倒计时")
        for i in range(self.value):
            sleep(1)
            print(ctime())

    def time2(self):
        print("倒计时结束")

    #重写run方法,起到逻辑调控的作用
    def run(self):
        self.time1()
        self.time2()
    
#创建进程对象
p = ClockProcess(5)
p.start()
p.join()

