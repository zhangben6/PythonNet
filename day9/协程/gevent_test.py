# import gevent
# from time import sleep
# def foo(a,b):
#     print("Running in foo",a,b)
#     sleep(2)
#     print('foo end')

# def bar(a,b):
#     print("Running in bar",a,b)
#     sleep(2)
#     print('bar end')
# f = gevent.spawn(foo,1,2)
# b = gevent.spawn(bar,1,2)

# gevent.joinall([f,b])


import gevent
from time import sleep
def foo(a,b):
    print("Running in foo",a,b)
    gevent.sleep(2)
    print('foo end')

def bar(a,b):
    print("Running in bar",a,b)
    gevent.sleep(2)
    print('bar end')
f = gevent.spawn(foo,1,2)
b = gevent.spawn(bar,1,2)

gevent.joinall([f,b])
