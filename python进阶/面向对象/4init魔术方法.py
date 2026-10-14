"""
@File : 4.py
@Author : 王子墨
@Description : 
@Date :2026/4/20
"""
"""
在每次创建对象时自动调用init魔术方法   
"""
#无参
class Car:
    def __init__(self):
        self.color = "red"
        self.number = 4
    def run(self):
        print("汽车会跑！")
    def work(self):
        print(f"我是work函数，self是{self}")
        self.run()

c1 = Car()
print(c1.color)
print(c1.number)
c1.work()
print("-"*34)
c2 = Car()
print(c2.color)
print(c2.number)
c2.work()
print("-"*34)

#有参
class Car:
    def __init__(self,color,number):
        self.color = color
        self.number = number
    def run(self):
        print("汽车会跑！")
    def work(self):
        print(f"我是work函数，self是{self}")
        self.run()

c3 = Car("green",6)
print(c3.color)
print(c3.number)
c3.work()