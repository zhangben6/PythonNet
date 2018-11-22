# from socket import * 
# # 创建套接字
# s = socket()
# s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
# s.bind(("0.0.0.0",7000))
# s.listen(5)
# print("waiting for ....")
# while True:
#     c,addr = s.accept()
#     print("connect from :",addr)
#     # 浏览器
#     data = c.recv(4096)
#     print(data)
#     # 返回http响应
#     f = open("zhangben.html")
#     s = f.read()
#     c.send(s.encode())
#     f.close()
#     c.close()
# s.close()

from socket import *
# 接收request 发送response
def handleClient(connfd):
    request = connfd.recv(4096)
    #将requset按行分割
    # print(request)
    request_lines= request.splitlines()
    for line in request_lines:
        print(line)
    try:
        f = open("/home/tarena/python/Pythonnet/day2/zhangben.html")
    except Exception:
        response = "HTTP/1.1 404 Not Found\r\n"
        response += "Content-Type:text/html\r\n"  
        response += "\r\n"
        response += "<h1> Sorry the page not found111</h1>"
    else:
        response = "HTTP/1.1 200 OK\r\n"
        response += "Content-Encoding:utf8\r\n"
        response += "Content-Type:text/html\r\n"  
        response += "\r\n"
        response += f.read()
    finally:
        #将结果给客户端
        connfd.send(response.encode())  



def main():
    sockfd = socket()
    sockfd.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    sockfd.bind(("127.0.0.1",8000))
    sockfd.listen(5)
    print("Listen the port 8000....")
    while True:
        connfd,addr = sockfd.accept()
        #处理请求
        handleClient(connfd)
        connfd.close()
main()

