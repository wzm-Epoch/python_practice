"""
@File : 5网编案例_一句话_模拟多任务版服务器端.py
@Author : 王子墨
@Description : 
@Date :2026/8/25
"""
# 导包````````````````````````````````````````````````````+++++++++++++++++++
import socket
# 1. 创建服务器端Socket对象.
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 2. 绑定IP地址和端口号.
server_socket.bind(('127.0.0.1', 10086))
# 3. 设置最大监听数.
server_socket.listen(5)
while True:
    try:
        # 4. 等待客户端申请建立连接.
        accept_socket,client_info = server_socket.accept()
        # 5. 给客户端发送消息.
        accept_socket.send(b'Welcome to the server!')
        # 6. 接收客户端的信息并打印.
        data = accept_socket.recv(1024).decode('utf-8')
        print(f"服务器端收到:{data}")
        # 7. 释放资源.
        accept_socket.close()
    except:
        pass