"""
@File : 3网络编程_一句话_客户端.py
@Author : 王子墨
@Description : 
@Date :2026/8/18
"""
"""
案例: 网编入门案例, 服务器端给客户端发送消息, 客户端给出回执信息.

客户端开发流程:
    1. 创建客户端Socket对象.
    2. 连接服务器端,指定:服务器端IP,端口号.
    3. 接收服务器端的信息并打印.
    4. 给服务器端发送消息.
    5. 释放资源.

细节:
    客户端和服务器端是通过 字节液(bytes) 的形式实现的.
"""
# 导包
import socket
# 1. 创建客户端Socket对象.
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 2. 连接服务器端,指定:服务器端IP,端口号.
client_socket.connect(('127.0.0.1', 10086))
# 3. 接收服务器端的信息并打印.
data = client_socket.recv(1024).decode('utf-8')
print(f"客户端收到:{data}")
# 4. 给服务器端发送消息.
client_socket.send('你好'.encode('utf-8'))
# 5. 释放资源.
client_socket.close()