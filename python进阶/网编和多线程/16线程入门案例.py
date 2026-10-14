"""
@File : 16线程入门案例.py
@Author : 王子墨
@Description : 
@Date :2026/8/28
进程和线程的关系:
    1.进程是CPU分配资源的基本单位，线程是CPU调度资源的最小单位
    2.线程是依附于进程的，每个进程至少有一个线程(主线程)
    3.进程间数据相互隔离，(同一个进程的)线程间数据可以共享
"""

import threading
import time

def coding():
    for i in range(1,11):
        time.sleep(0.1)
        print(f"正在敲第{i}遍代码")

def music():
    for i in range(1,11):
        time.sleep(0.1)
        print(f"正在听第{i}遍音乐")

if __name__ == '__main__':

    t1 = threading.Thread(target=coding)
    t2 = threading.Thread(target=music)

    t1.start()
    t2.start()