"""
@File : 5str魔术方法.py
@Author : 王子墨
@Description : 
@Date :2026/4/21
"""
"""
使用 print() 函数打印对象时自动调用打印地址值，可重写，改为打印对象的各个属性值 
"""
class Car:
    def __init__(self,color,number):
        self.color = color
        self.number = number
    def __str__(self):
        return f"颜色:{self.color},轮胎数:{self.number}"
c1 = Car("red",4)
print(c1)