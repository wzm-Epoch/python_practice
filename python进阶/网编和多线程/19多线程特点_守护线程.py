"""
@File : 19多线程特点_守护线程.py
@Author : 王子墨
@Description : 
@Date :2026/8/28
"""

import threading
import time

def work():
    for i in range(1,10):
        time.sleep(0.2)
        print("工作中……")

if __name__ == '__main__':

    t = threading.Thread(target=work,daemon=True)
    # t.setDaemon(True)
    # t.daemon = True
    t.start()

    time.sleep(1)
    print("主线程结束了!")