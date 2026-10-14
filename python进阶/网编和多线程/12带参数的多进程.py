"""
@File : 12带参数的多进程.py
@Author : 王子墨
@Description : 
@Date :2026/8/27

进程传参有两种方式：
    方式1：args方式，接受所有的 位置参数
    方式2：kwargs方式，接受所有的 关键字参数
"""

import multiprocessing
import time

def coding(name,num):
    for i in range(1,num+1):
        time.sleep(0.1)
        print(f"{name}正在敲第{i}遍代码")

def music(name,count):
    for i in range(1,count+1):
        time.sleep(0.1)
        print(f"{name}正在听第{i}首音乐")

if __name__ == '__main__':

    p1 = multiprocessing.Process(target=coding,args=('王子墨',10))
    p2 = multiprocessing.Process(target=music,kwargs={'name':'王子墨','count':20})

    p1.start()
    p2.start()