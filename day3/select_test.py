from select import select

from socket import *

import sys

s = socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(('0.0.0.0',8000))
s.listen(3)

#监控IO
print("等待我监控的IO")
rs,ws,xs = select([s,sys.stdin],[],[s],3)
print("终于发生了")
print(rs)

