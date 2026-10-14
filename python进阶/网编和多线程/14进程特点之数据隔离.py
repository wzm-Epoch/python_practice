"""
@File : 14进程特点之数据隔离.py
@Author : 王子墨
@Description : 
@Date :2026/8/27

进程的特点：
    1.进程之间数据是相互隔离的
        因为子进程相当于是父进程的“副本”，会将父进程的“main外资源”拷贝一份，即：各是各的
    2.主进程会等待子进程执行结束再结束
"""

import multiprocessing

my_list = []

def write_data():
    for i in range(1,10):
        my_list.append(i)
        print(f"添加数据:{i}")
    print(f"write_data:{my_list}")

def read_data():
    print(f"read_data:{my_list}")

if __name__ == '__main__':

    p1 = multiprocessing.Process(target=write_data)
    p2 = multiprocessing.Process(target=read_data)

    p1.start()
    p2.start()