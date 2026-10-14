"""
@File : 20多线程特点_数据共享.py
@Author : 王子墨
@Description : 
@Date :2026/8/28
"""

import time
import threading

my_list = []

def write_data():
    for i in range(1,10):
        my_list.append(i)
        print(f"添加数据:{i}")
    print(f"write_data:{my_list}")

def read_data():
    time.sleep(1)
    print(f"read_data:{my_list}")

if __name__ == '__main__':

    t1 = threading.Thread(target=write_data)
    t2 = threading.Thread(target=read_data)
    t1.start()
    t2.start()