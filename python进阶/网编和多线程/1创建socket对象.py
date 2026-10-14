"""
@File : 1.py
@Author : 王子墨
@Description : 
@Date :2026/7/2

网洛编程介绍:
    概述:
        网络编程也叫网络通信,socket通信,即:通信双方都独有自己的socket对象;
        数据在socket之间通过 数据报包(UDP协议) 或者 字节流(TCP协议) 的形式进行传输
"""
#导包
import socket
#创建socket对象
#参1:Address Family , 地址族 , 即: Ipv4 还是 Ipv6 , 默认值：AF_INET(ipv4) , AF_INT6(ipv6)
#参2:Socket Type , Socket类型 , 即 : TCP 还是 UDP , 默认值:SOCK_STREAM(TCP) , SOCK_DGRAM(UDP)
socket_obj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print(socket_obj)