"""
@File : 13获取进程的编号.py
@Author : 王子墨
@Description : 
@Date :2026/8/27
"""
"""
案例：演示获取进程的编号。

进程的编号解释：
概述：
    在设备中，每个程序(进程)都有自己的唯一进程id，当程序释放的时候，该进程id也会释放，即：进程id是可以重复使用的。
目的：
    1. 查看子进程和父进程的关系，方便管理。
    2. 例如：杀死指定进程，创建子进程...
格式：
    查看当前进程的pid:
        os模块(operating，系统模块) 的 getpid()    · get Process id
        multiprocess#current_process()的pid属性

    查看当前进程的ppid:     parent process id(父进程id)
        os#getppid()

细节:
    main中创建的进程，如果没有特殊指定，它的父进程都是main进程，
    而main进程的父进程是 PyCharm程序的pid
"""

import multiprocessing
import time
import os

def coding(name,num):
    for i in range(1,num+1):
        time.sleep(0.1)
        print(f"{name}正在敲第{i}遍代码")
    print(f'p1进程的pid:{os.getpid()},父进程的pid{os.getppid()}')
def music(name,count):
    for i in range(1,count+1):
        time.sleep(0.1)
        print(f"{name}正在听第{i}首音乐")
    print(f'p2进程的pid{multiprocessing.current_process().pid},父进程的pid{os.getppid()}')
if __name__ == '__main__':

    p1 = multiprocessing.Process(target=coding,args=('王子墨',10))
    p2 = multiprocessing.Process(target=music,kwargs={'name':'王子墨','count':20})

    p1.start()
    p2.start()

    print(f'main进程的pid:{os.getpid()},父进程的pid{os.getppid()}')