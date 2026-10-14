"""
@File : 7案例 减肥.py
@Author : 王子墨
@Description : 
@Date :2026/4/21
"""
class Student:
    def __init__(self):
        self.current_weight = 100
    def run(self):
        self.current_weight -= 0.5
        print("跑步一次，体重减少0.5kg")
    def eat(self):
        self.current_weight += 2
        print("大吃大喝一次，体重增加2kg")
    def __str__(self):
        return f"当前体重: {self.current_weight}"


xm  = Student()
xm.run()
xm.eat()
print(xm)