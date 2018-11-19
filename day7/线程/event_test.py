from threading import Event

#创建事件对象
e = Event()

e.set() #设置e
e.clear()
print(e.is_set())
e.wait(3)

print("*********")