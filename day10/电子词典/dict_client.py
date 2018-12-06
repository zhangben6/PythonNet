from socket import *
import sys
import getpass


#创建网络连接
def main():
    if len(sys.argv) < 3:
        print('argv is error')
        return
    HOST = sys.argv[1]
    PORT = int(sys.argv[2])
    ADDR = (HOST,PORT)
    s = socket()

    #连接服务器
    try:
        s.connect(ADDR)
    except Exception as e:
        print("服务器异常",e)
        return 
    
    while True:
        print("\n========张奔版GUI工具 V8.92========")
        print("****      1.注册(register)        ****")
        print("****      2.登录(login)        ****")
        print("****      3.退出(quit)        ****")
        print("=====================================")
        try:
            cmd = int(input("请输入:"))
        except Exception as e:
            print("命令错误")
            continue
        except KeyboardInterrupt:
            s.send(b'Q')
            s.close()
            sys.exit("感谢使用")
        if cmd not in [1,2,3]:
            print("不存在该选项")
            continue
        elif cmd == 1:
            do_register(s)
        elif cmd == 2:
            do_login(s)
        elif cmd == 3:
            s.send(b'Q')
            s.close()
            sys.exit("谢谢使用")
            
def do_register(s):
    while True:
        name = input("User:")
        passwd = getpass.getpass("Enter your password:")
        passwd1 = getpass.getpass("Aagin enter your password:")

        if (' 'in name) or (' ' in passwd):
            print("用户名或者密码不允许有空格")
            continue
        if passwd != passwd1:
            print("两次输入密码不一致")
            continue
        msg = "R %s %s" %(name,passwd)

        #发送给服务端
        s.send(msg.encode())

        #等待回复
        data = s.recv(128).decode()

        if data == 'OK':
            print("注册成功")
            return
        elif data == 'EXIST':
            print("该用户已存在")
        else:
            print('注册失败')
        return

def do_login(s):
    name = input("User:")
    passwd = getpass.getpass()

    msg = "L %s %s" % (name,passwd)
    s.send(msg.encode())
    data = s.recv(128).decode()
    if data == 'OK':
        print("登录成功")
        login(s,name)
    else:
        print("登录失败")

def login(s,name):
    '''这个函数是二级页面客户端操作'''
    while True:
        print('''
        ============查询界面============
        --1.查词  2.历史记录  3.注销--
        ===============================
        ''')
        
        try:
            cmd = int(input("请输入:"))
        except Exception as e:
            print("命令错误")
            continue
        except KeyboardInterrupt:
            s.send(b'Q')
            s.close()
            sys.exit("二级界面退出")
        if cmd not in [1,2,3]:
            print("不存在该选项")
            continue
        elif cmd == 1:
            do_query(s,name)
        elif cmd == 2:
            do_history(s,name)
        elif cmd == 3:
            break

#以下为二级页面操作函数
def do_query(s,name):
    while True:
        word = input("单词:")
        if word == '##':
            break
        msg = 'E %s %s'%(name,word)
        s.send(msg.encode())
        #接受服务端反馈结果
        data = s.recv(2048).decode()
        if data == 'FALL':
            print("没有该单词")
        else:
            print(data)

def do_history(s,name):
    msg = 'H %s' % (name)    
    s.send(msg.encode())
    data = s.recv(128).decode()
    if data == 'OK':
        while True:
            data = s.recv(1024).decode()
            if data == '##':
                break
            print(data)
    else:
        print("没有历史记录")
if __name__ == '__main__':
    main()