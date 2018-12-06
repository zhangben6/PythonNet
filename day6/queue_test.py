from multiprocessing import Queue
from time import sleep

#创建消息序列
q = Queue(3)

q.put(1)
sleep(0.01)
print(q.empty())
q.put(2)
q.put(3)
print(q.full())
# q.put(4,False)   非阻塞状态
# q.put(4,timeout=3)
print(q.get())
print(q.qsize())
q.close()



# queque1.py  消息间通信

