"""
@File : 10演示单任务.py
@Author : 王子墨
@Description : 
@Date :2026/8/27
"""

#1定义函数a，输出十次 hello world
def func_a():
    for i in range(10):
        print('hello world')

#2定义函数b，输出十次 hello python
def func_b():
    for i in range(10):
        print('hello python')

func_a()
print('*'*23)
func_b()
