import os
from time import sleep
pid = os.fork()

if pid < 0:
     print("Crate process fiald")
elif pid == 0:
    sleep(2)
    print('child process %d exit' % os.getpid())
    os._exit(2)
else:
    # print("sfds")
    # pid,status = os.wait()  #阻塞状态
    pid,status = os.waitpid(-1,os.WNOHANG)  #非阻塞状态,还是会变成僵尸状态

    print("pid",pid)
    print("status:",status)

    #捕获到子进程的退出状态
    # print("status:",os.WEXITSTATUS(status))

    while True:
        pass 
