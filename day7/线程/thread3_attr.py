# from threading import Thread,currentThread
# from time import sleep
# def fun():
#     print('线程属性测试')
#     sleep(3)
#     print("%s线程执行完毕"%currentThread().getName())
# t = Thread(target=fun,name='Tarena')
# t.start()
# t.setName('Tedu')
# print('Thread name:',t.name)
# print('Get Thread name:',t.getName())
# print('is_alive:',t.is_alive())
# t.join()


#daemon属性实例
from threading import Thread,currentThread
from time import sleep
def fun():
    print('线程属性测试')
    sleep(3)
    print("%s线程执行完毕"%currentThread().getName())
t = Thread(target=fun,name='Tarena')
t.start()
t.setName('Tedu')
print('Thread name:',t.name)
print('Get Thread name:',t.getName())
print('is_alive:',t.is_alive())
# t.join()
print('============main thread==============')

