from socket import * 
s = socket()


#设置端口重用
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)

s.bind(("127.0.0.1",8533))

# print("family:",s.family) #地址类型
# print("type",s.type) #套接字类型
# print(s.getsockname()) # 绑定地址

# #文件描述符
# print("fileno:",s.fileno())


#获取选项值
print("get opt:",s.getsockopt(SOL_SOCKET,SO_REUSEADDR))
s.listen(3)
c,addr=s.accept()
print(c.getpeername())
c.recv(1024)  

