"""
@File : 15进程特点之主进程等待子进程结束再结束.py
@Author : 王子墨
@Description : 
@Date :2026/8/28
"""
import time
import multiprocessing

def work():
    for i in range(1,10):
        print('正在努力工作中省略号…')
        time.sleep(0.2)

if __name__ == '__main__':

    p1 = multiprocessing.Process(target=work,name='wzm')
    #进程的默认命名规则是:Process-编号，编号是从1开始的
    print(f'p1进程的名字:{p1.name}')
    p1.daemon = True
    p1.start()
    time.sleep(1)
    print('main进程结束了')