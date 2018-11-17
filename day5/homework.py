import os
filename = './test.jpg'
# 获取文件大小
size = os.path.getsize(filename)

def copy1():
    f = open(filename,'rb')
    fw = open('1.jpg','wb')
    n = size // 2
    while True:
        if n < 1024:
            data = f.read(n)
            fw.write(data)
            break
        data = f.read(1024)
        fw.write(data)
        n -= 1024
    f.close()
    fw.close()

def copy2():
    f = open("./test.jpg",'rb')
    fw = open("2.jpg",'wb')
    #设置光标
    f.seek(size//2,0)
    while True:
        data = f.read(1024)
        if not data:
            break
        fw.write(data)
    f.close()
    fw.close()
pid = os.fork()
if pid < 0:
    print("Create process faild")
elif pid == 0:
    copy1()
else:
    copy2()

