"""
@File : 6del魔术方法.py
@Author : 王子墨
@Description : 
@Date :2026/4/21
"""
"""
当删除对象时(调用del删除对象或文件执行结束后),会默认调用del方法
"""
class Car:
    def __init__(self,brand):
        self.brand = brand
    def __str__(self):
        return f"品牌:{self.brand}"
    def __del__(self):
        print(f"{self}对象被删除了!")

c1 = Car(" 劳斯莱斯 ")
print(c1)
