"""
@File : 3.py
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
c1.color = "红色"
c1.number = 4
print((f"c1是{c1}"))
print(f"颜色：{c1.color},轮胎数：{c1.number}")
c1.work()

print("-"*34)


class Car:
    def run(self):
        print("汽车会跑！")
    def work(self):
        print(f"我是work函数，self是{self}")
        self.run()
    def show(self):
        print(f"颜色是：{self.color},轮胎数是:{self.number}")
c2 = Car()
c2.color = "蓝色"
c2.number = 4
print((f"c2是：{c2}"))
c2.work()
c2.show()