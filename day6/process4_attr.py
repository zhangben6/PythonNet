# from multiprocessing import Process
# from time import sleep,ctime

# def tm():
#     for i in range(4):
#         sleep(2)
#         print(ctime())

# p = Process(target=tm,name='张奔')
# p.start()
# #打印进程对象属性
# print('name:',p.name)
# print('pid:',p.pid)
# print("alive:",p.is_alive())
# p.join()


from multiprocessing import Process
from time import sleep,ctime

def tm():
    for i in range(4):
        sleep(2)
        print(ctime())

p = Process(target=tm,name='张奔')
p.daemon = True
p.start()
#打印进程对象属性
print('name:',p.name)
print('pid:',p.pid)
print("alive:",p.is_alive())
# p.join()
