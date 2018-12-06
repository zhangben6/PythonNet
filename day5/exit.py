import os,sys


#进程退出,必须得传一个整数参数
# os._exit(2)

 


try:
    sys.exit("进程退出")
except SystemExit:
    pass
print("Process end")
