"""
@File : 10单继承.py
@Author : 王子墨
@Description : 
@Date :2026/4/22
"""
class Master:
    def __init__(self):
        self.kongfu = "剑术"

    def action(self):
        print(f"使用{self.kongfu}")

class Prentice(Master):
    pass

td = Prentice()
print(td.kongfu)
td.action()