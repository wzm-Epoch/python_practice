"""
@File : 2.py
@Author : 王子墨
@Description : 
@Date :2026/4/20
"""
class Car:
    def run(self):
        print("汽车会跑！")
    def work(self):
        print(f"我是work函数，self是{self}")
        self.run()
c1 = Car()
print(f"c1是{c1}")
c1.work()
print("-"*34)

c2 = Car()
print(f"c2是{c2}")
c2.work()