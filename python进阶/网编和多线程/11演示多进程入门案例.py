"""
@File : 11演示多进程入门案例.py
@Author : 王子墨
@Description : 
@Date :2026/8/27

实现方式：
    1.导包
    2.创建进程对象，关联目标函数
    3.启动进程
"""

#导包
import multiprocessing
import time

def coding():
    for i in range(1,11):
        time.sleep(0.1)
        print(f"正在敲第{i}遍代码")

def music():
    for i in range(1,11):
        time.sleep(0.1)
        print(f"正在听第{i}遍音乐")

#创建两个进程对象，分别关联上述的两个目标函数
#通过main进程(主进程)来创建子进程
if __name__ == '__main__':
    #进程p1关联，coding函数，p1进程抢到了(CPU资源)，就会执行这个函数
    p1 = multiprocessing.Process(target=coding)
    p2 = multiprocessing.Process(target=music)

    #启动进程，表示进程启动了，就可以开始枪CPU资源了
    p1.start()
    p2.start()
