# from multiprocessing import Process,Pipe
# import os,time

# fd1,fd2 = Pipe() #管道参数默认为True,表示双向管道
# def fun(name):
#     time.sleep(3)
#     fd1.send("hello! "+ name.title())

# jobs = []
# for i in ['tom','zack','abby','sam']:
#     p = Process(target=fun,args=(i,))
#     jobs.append(p)
#     p.start()

# #从管道读取内容
# for i in range(4):
#     data = fd2.recv()
#     print(data)

# for i in jobs:
#     i.join()


from multiprocessing import Process,Pipe
import os,time

# fd1,fd2 = Pipe() #管道参数默认为True,表示双向管道
def fun(name):
    time.sleep(1)
    print("hello:"+name)
jobs = []
for i in ['tom','zack','abby','sam']:
    p = Process(target=fun,args=(i,))
    jobs.append(p)
    # time.sleep(2)
    p.start()

#从管道读取内容
# for i in range(4):
#     data = fd2.recv()
#     print(data)

for i in jobs:
    i.join()






