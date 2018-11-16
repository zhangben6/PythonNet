import os
from time import sleep
print("========================================")
a = 1
pid = os.fork()

if pid < 0:
    print("create process failed")
elif pid == 0:
    print("Child process")
    print("child a:",a)
    a = 10000
else:
    sleep(2)
    print("Parent process")
    print("Parent a = ",a)
    