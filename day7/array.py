'''the biggest difference with 
Value is incoming parameters must be
integer or array
'''
from multiprocessing import Process,Array
import time
shm = Array('i',[1,2,3,4,5,6])
def run():
    for i in shm:
        print(i)
    shm[0]=1000
p = Process(target=run)
p.start()
p.join()
for i in shm:
    print(i,end=' ')
print()


# from multiprocessing import Process,Array
# import time
# shm = Array('c',b'hello')
# def run():
#     for i in shm:
#         print(i)
#     shm[0]=b'H'
# p = Process(target=run)
# p.start()
# p.join()
# for i in shm:
#     print(i,end=' ')
# print()
# print(shm.value)