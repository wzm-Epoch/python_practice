"""
@File : 21多线程共享全局变量出现问题.py
@Author : 王子墨
@Description : 
@Date :2026/8/28
案例：演示多线程共享全局变量，可能出现的问题。

多线程共享全局变量，出现问题的问题：
    累加次数不够。
产生原因：
    线程1还没有来记得执行完(一个完整的动作)前，被线程2抢走了资源，就可能出问题。
解决方案：
    加锁思想，即：互斥锁。
细节：
    使用互斥锁的时候，要在合适的时机释放所，否则可能出现 死锁 或者 锁不住的情况。

进程和线程的区别：
    1．线程依赖进程，进程是CPU分配资源的基本单位，线程是CPU调度资源的基本单位。
    2．进程更消耗资源，不能共享全局变量，相对更稳定。
    3．线程更轻量级，可以共享全局变量，相对更灵活。
"""

import threading

global_num = 0

mutex = threading.Lock()

def target_func1():
    mutex.acquire() #加锁
    global global_num
    for i in range(1000000):
        global_num += 1
    print(f'target_func1函数结果:{global_num}')
    mutex.release() #释放锁

def target_func2():
    mutex.acquire()
    global global_num
    for i in range(1000000):
        global_num += 1
    print(f'target_func2函数结果:{global_num}')
    mutex.release()

if __name__ == '__main__':

    t1 = threading.Thread(target=target_func1)
    t2 = threading.Thread(target=target_func2)

    t1.start()
    t2.start()