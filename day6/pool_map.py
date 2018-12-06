from multiprocessing import Pool
from time import sleep

def fun(n):
    sleep(1)
    return n * n
pool = Pool()

r = pool.map(fun,range(6))

pool.close()
pool.join()
print(r) 
